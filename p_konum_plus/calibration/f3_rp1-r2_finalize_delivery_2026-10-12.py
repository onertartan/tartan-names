"""Build final rp1-r2 delivery records from immutable observed run artifacts."""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
import csv
import datetime as dt
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / 'p_konum_plus/calibration'
P = ROOT / 'p_konum_plus/provenance'
Q = ROOT / 'p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11'
DATE = '2026-10-12'
PREFIX = 'f3_realdata_prep_rp1-r2_'
H = C / 'f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
RESULT = C / 'f3_step2_results_rp1-r2_2026-10-10.json'
LOG = P / 'f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md'
TRANSMISSION = P / (PREFIX + 'transmission_list_' + DATE + '.csv')
PAYLOADS: dict[Path, str] = {}
SIDECARS: dict[Path, Path] = {}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def seal(path: Path, target: Path | None = None) -> Path:
    checksum = target or Path(str(path) + '.sha256')
    checksum.parent.mkdir(parents=True, exist_ok=True)
    body = sha(path) + '  ' + path.name + '\n'
    if checksum.exists():
        assert checksum.read_text(encoding='ascii') == body, 'EXISTING_SIDECAR_CHANGED ' + str(checksum)
    else:
        checksum.write_text(body, encoding='ascii', newline='\n')
    SIDECARS[path] = checksum
    return checksum


def add(path: Path, role: str, *, sidecar: Path | None = None) -> None:
    assert path.is_file(), 'MISSING_DELIVERABLE ' + str(path)
    parts = path.relative_to(ROOT).parts
    assert path.suffix not in ('.pkl', '.zip') and not any('restart_store_' in x and x.startswith('.') for x in parts)
    assert 'rp1r1_audit' not in str(path).lower()
    PAYLOADS[path] = role
    seal(path, sidecar)


def write(path: Path, text: str, role: str) -> Path:
    # These are new final-release filenames, never historical package files.
    assert DATE in path.name or path == LOG
    path.write_text(text, encoding='utf8', newline='\n')
    old = Path(str(path) + '.sha256')
    if old.exists():
        old.write_text(sha(path) + '  ' + path.name + '\n', encoding='ascii')
    add(path, role)
    return path


def record(stem: str, value: Any, role: str = 'final provenance record') -> Path:
    return write(P / (PREFIX + stem + '_' + DATE + '.json'), json.dumps(value, indent=2, ensure_ascii=True) + '\n', role)


def table(stem: str, fields: list[str], rows: list[dict[str, Any]], role: str) -> Path:
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return write(P / (PREFIX + stem + '_' + DATE + '.csv'), stream.getvalue(), role)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf8', newline='') as stream:
        return list(csv.DictReader(stream))


def location(path: Path, function: str) -> str:
    node = next(n for n in ast.walk(ast.parse(path.read_text(encoding='utf8')))
                if isinstance(n, ast.FunctionDef) and n.name == function)
    return rel(path) + ':' + str(node.lineno)


def build() -> None:
    assert not subprocess.check_output(['git','diff','--name-only'],cwd=ROOT).strip()
    assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT).strip()
    result_hash = sha(RESULT)
    data = json.loads(RESULT.read_text(encoding='utf8'))
    end_path = P / 'f3_step2_rp1-r2_attempt2_launch1_end_2026-10-10.json'
    end = json.loads(end_path.read_text(encoding='ascii'))
    assert end['return_code'] == 0 and data['process']['attempt_number'] == 2 and data['process']['pid'] == end['pid']
    assert sha(H) == end['code_sha256']
    for kind in ('stdout','stderr'):
        assert sha(Path(end[kind])) == end[kind + '_sha256']
    assert data['end_state']['rp1_r2_status'] == 'PARTIAL_PENDING_PI'
    assert data['end_state']['mandatory_tests_all_run'] and not data['end_state']['mandatory_tests_missing']
    assert all(v['ran'] and v['passed'] for v in data['tests_run'].values())
    assert data['nonregression_vs_r4_2']['pass_'] and not data['nonregression_vs_r4_2']['s_findings'] and not data['nonregression_vs_r4_2']['u_findings']
    assert data['run1_canonical_sha256'] == data['run2_canonical_sha256']
    assert data['real_data_access'] is False
    primary_code = [H.name,'f3_rp1-r2_gate_tools_2026-10-10.py','f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py',
        'f3_rp1-r2_technical_tests_2026-10-10.py','f3_rp1-r2_launch_attempt_2026-10-10.py','f3_rp1-r2_write_custody_2026-10-10.py',
        'f3_rp1-r2_small_input_tests_2026-10-10.py','f3_rp1-r2_logged_preflight_2026-10-10.py',
        'f3_rp1-r2_prepare_review_records_2026-10-10.py',Path(__file__).name,'f3_rp1-r2_verify_final_delivery_2026-10-12.py']
    for name in primary_code:
        add(C / name, 'rp1-r2 source; historical record-builder main must not be rerun' if 'prepare_review_records' in name else 'rp1-r2 source')
    for path in C.glob('*rp1-r2*'):
        if path.is_file() and path.name.startswith('f3_step2_') and path.suffix in ('.json','.csv','.log'):
            add(path, 'attempt-2 observed run artifact')
    stems = ['start_state_inventory','ledger','existing_synthetic_fixture_custody','historical_count_errata',
        'authored_edits','d14_intake_receipt','launch_authorization','ir1-13_stop_record',
        'prelaunch_checks_after_d14','attempt2_prelaunch_checks','attempt2_prelaunch_stop',
        'attempt2_declaration_correction','attempt2_declaration_only_diff','attempt1_22_u_findings',
        'attempt2_provenance_changes','attempt2_harness_provenance_diff','attempt2_launcher_provenance_diff',
        'attempt2_launch_start_verified','size_estimate']
    for stem in stems:
        paths = [p for p in P.glob(PREFIX + stem + '_*') if p.is_file() and p.suffix != '.sha256']
        assert paths, 'MISSING_RECORD ' + stem
        for path in paths:
            add(path,'historical/current rp1-r2 provenance; authoritative final records are separately named')
    for path in P.glob('f3_step2_rp1-r2_*'):
        if path.is_file() and path.suffix != '.sha256':
            add(path,'immutable launch/custody/controller evidence')
    for path in P.glob(PREFIX + 'runtime_fixture_custody_*'):
        if path.suffix != '.sha256':
            add(path,'runtime synthetic fixture custody')
    for path in (P / 'f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11').iterdir():
        if path.suffix != '.sha256':
            add(path,'intermediate source backup; identifies isolated comparator source bytes')
    prompts = ['Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md',
        'f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md',
        'f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md',
        'F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md',
        'f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md']
    for name in prompts:
        add(ROOT / 'p_konum_plus/prompts' / name,'current dispatch/instruction or supplied audit input; unchanged bytes')
    quarantine_names = [H.name,'f3_step2_rp1-r2_launch1_stdout_2026-10-10.log','f3_step2_rp1-r2_launch1_stderr_2026-10-10.log',
        'f3_step2_rp1-r2_nonregression_vs_r4-2_2026-10-10.csv','f3_step2_test_evidence_rp1-r2_2026-10-10.json',
        'f3_step2_rp1-r2_restart_store_manifest_2026-10-10.csv']
    for name in quarantine_names:
        add(Q / 'calibration' / name,'attempt-1 quarantined source/error evidence; store units excluded')
    for name in ('verified_quarantine_inventory_2026-10-11.csv','initial_source_and_provenance_inventory.json','move_plan.json'):
        add(Q / name,'attempt-1 quarantine custody; index includes omitted local store references')
    fixture_root = C / 'f3_step2_rp1-r2_f1_synth_fixtures_2026-10-10'
    fixture_paths = sorted(p for p in fixture_root.rglob('*') if p.is_file())
    fixture_rows = []
    checksum_root = P / ('f3_rp1-r2_fixture_delivery_sidecars_' + DATE)
    for path in fixture_paths:
        # Inner checksum files are test INPUTS, including deliberately stale
        # negative-case checksums. Package every input byte with a separate
        # outer delivery checksum; do not add files to any raw directory.
        sidecar = checksum_root / (path.relative_to(fixture_root).as_posix() + '.sha256')
        add(path,'synthetic test input (inner .sha256 files are also input data)',sidecar=sidecar)
        fixture_rows.append(dict(path=rel(path),sha256=sha(path),bytes=path.stat().st_size,delivery_sidecar=rel(sidecar),role='TEST_ONLY_SYNTHETIC'))
    fixtures = table('synthetic_fixture_delivery_custody',['path','sha256','bytes','delivery_sidecar','role'],fixture_rows,'final synthetic fixture custody')
    for row in read_csv(P / 'f3_realdata_prep_rp1-r2_existing_synthetic_fixture_custody_2026-10-10.csv'):
        assert sha(ROOT / row['path']) == row['sha256'], 'PREVIOUS_SYNTHETIC_FIXTURE_CHANGED'
    nonreg = read_csv(C / 'f3_step2_rp1-r2_nonregression_vs_r4-2_2026-10-10.csv')
    assert set(nonreg[0]) == {'path','classification','declaration_id','kind','held','reason','r4_2','rp1-r2'}
    assert all(row['held'] == 'True' for row in nonreg)
    assert not any(row['classification'] in ('S_FINDING','U_FINDING') for row in nonreg)
    assert sum(bool(row['declaration_id']) for row in nonreg) == data['nonregression_vs_r4_2']['e_declared']
    declarations_node = next(n for n in ast.walk(ast.parse(H.read_text(encoding='utf8'))) if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == 'EXPECTATIONS_E' for t in n.targets))
    declarations = record('final_source_leaf_declarations',ast.literal_eval(declarations_node.value),'exact final source declarations; no changes to expectations')
    # Generate both final source diffs through the delivered record-only helper.
    review_path = C / 'f3_rp1-r2_prepare_review_records_2026-10-10.py'
    spec = importlib.util.spec_from_file_location('rp2_record_diff_helpers',review_path)
    review = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(review)
    review.DATE = DATE
    original_labels = review.labels
    def labels(source: str, tree: ast.Module, *, inherited: bool = False) -> dict[int, tuple[str,str]]:
        output_date = review.DATE
        review.DATE = '2026-10-10'
        try:
            result = original_labels(source,tree,inherited=inherited)
        finally:
            review.DATE = output_date
        for node in ast.walk(tree):
            if isinstance(node,ast.Assign):
                names = {t.id for t in node.targets if isinstance(t,ast.Name)}
                if 'EXPECTATIONS_E' in names:
                    for line in range(node.lineno,node.end_lineno+1):
                        result[line] = ('Q5','Exact leaf declarations; 22 missing test_evidence additions corrected under section 0 in attempt 2; no test value or scientific expectation changed.')
                elif names & {'ATTEMPT_NUMBER','SUPERSEDES_HARNESS_SHA256','SUPERSEDES_CUSTODY_SHA256','SUPERSEDES_NOTE_PATH','RESTART_STORE_DIR','LAUNCH_STDOUT_PATH','LAUNCH_STDERR_PATH'}:
                    for line in range(node.lineno,node.end_lineno+1):
                        result[line] = ('S8','PI-authorized attempt identity, supersession, isolated store and immutable launch naming; provenance only.')
        return result
    review.labels = labels
    source = H.read_text(encoding='utf8')
    import difflib
    old_lines = review.PARENT.read_text(encoding='utf8').splitlines(keepends=True)
    new_lines = source.splitlines(keepends=True)
    own_lines: set[int] = set()
    for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(None,old_lines,new_lines,autojunk=False).get_opcodes():
        if tag != 'equal':
            own_lines.update(range(j1+1,j2+1))
    diffs = [review.make_diff(review.PARENT,'rp1-r1',source,own_lines),review.make_diff(review.R42,'r4-2',source,own_lines)]
    for item in diffs:
        for key in ('diff','labels'):
            add(Path(item[key]),'final source diff' if key == 'diff' else 'semantic changed-line labels (one per range)')
        item['diff_sha256'] = sha(Path(item['diff']))
        item['labels_sha256'] = sha(Path(item['labels']))
    diff_custody = record('final_diff_custody',dict(harness_sha256=sha(H),diffs=diffs))
    family_path = ROOT / data['handoff_outputs']['family']['path']
    timing_path = ROOT / data['handoff_outputs']['timing']['path']
    family = read_csv(family_path)
    timings = read_csv(timing_path)
    assert len(family) == data['handoff_outputs']['family']['rows'] and sha(family_path) == data['handoff_outputs']['family']['sha256']
    assert len(timings) == data['handoff_outputs']['timing']['rows'] and sha(timing_path) == data['handoff_outputs']['timing']['sha256']
    groups: dict[tuple[str,str],list[float]] = defaultdict(list)
    for row in family:
        value = float(row['wall_clock_seconds'])
        if math.isfinite(value):
            groups[(row['family'],row['context'])].append(value)
    measured = sum(float(row['elapsed_seconds']) for row in timings)
    measured_trajectories = len({(row['sex'],row['trajectory']) for row in timings})
    existing_estimate = json.loads((P / 'f3_realdata_prep_rp1-r2_size_estimate_2026-10-10.json').read_text())
    target_field = next(k for k in existing_estimate if k.startswith('extrapolated_') and k.endswith('_trajectory_seconds'))
    target_trajectories = int(target_field.split('_')[1])
    estimate = record('size_estimate_final',dict(label='ESTIMATE',scope='Synthetic F1 handoff, both sexes, full frozen start banks and all measured consumer contexts, one process in the recorded binding environment. No real-data timing observed.',
        measured_trajectories=measured_trajectories,measured_elapsed_seconds=measured,observed_finite_family_optimizer_seconds=sum(sum(v) for v in groups.values()),
        target_trajectory_count=target_trajectories,target_count_source=rel(P / 'f3_realdata_prep_rp1-r2_size_estimate_2026-10-10.json'),
        extrapolated_seconds=measured/measured_trajectories*target_trajectories,
        method='Sum per-trajectory elapsed seconds, divide by observed trajectory count, multiply by the frozen target count; informational linear extrapolation, no execution permission.',
        family_context=[dict(family=k[0],context=k[1],finite_call_count=len(v),total_seconds=sum(v),mean_seconds=sum(v)/len(v)) for k,v in sorted(groups.items())],
        inputs={rel(family_path):sha(family_path),rel(timing_path):sha(timing_path)},real_data_access=data['real_data_access']), 'ESTIMATE from measured Q10 bytes')
    map_old = read_csv(P / 'f3_realdata_prep_rp1-r2_requirement_map_after_d14_2026-10-10.csv')
    functions = {'Q1':('f3_rp1-r2_gate_tools_2026-10-10.py','check_intake'),'Q2':(H.name,'real_mask_id'),
        'Q3':('f3_rp1-r2_gate_tools_2026-10-10.py','check_f1_manifest'),'Q4':(H.name,'t_f1_loader_synth'),
        'Q5':('f3_rp1-r2_gate_tools_2026-10-10.py','compare_document'),'Q6':('f3_rp1-r2_gate_tools_2026-10-10.py','traceback_signature'),
        'Q7':(H.name,'store_read_aggregate'),'Q8':(H.name,'ckpt_load'),'Q9':('f3_rp1-r2_gate_tools_2026-10-10.py','family_of_key'),
        'Q10':(H.name,'handoff_accounting'),'Q11':('f3_rp1-r2_gate_tools_2026-10-10.py','launch_matches')}
    map_rows = []
    final_ledger_path = P / (PREFIX + 'ledger_final_' + DATE + '.json')
    record_paths = {'S5A':ROOT/'p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md',
        'IR1-14':P/'f3_realdata_prep_rp1-r2_ir1-13_stop_record_2026-10-10.md','IR1-15':P/'f3_realdata_prep_rp1-r2_historical_count_errata_2026-10-10.json',
        'IR1-16':diff_custody,'IR1-17':final_ledger_path,'IR1-19':fixtures}
    for row in map_old:
        out = dict(row)
        key = row['requirement']
        out['source_results_file'] = rel(RESULT)
        out['source_results_sha256'] = result_hash
        if key in functions:
            filename,function = functions[key]
            out['code_or_record'] = location(C/filename,function)
            out['test_location'] = location(C/'f3_rp1-r2_technical_tests_2026-10-10.py','reproduction_cases' if key=='Q3' else 'technical_cases')
            out['verification'] = 'Transferred verbatim from final results JSON; executor observation only'
            out['evidence'] = 'rp1_r2_technical_tests.' + key + '; tests_run.T-RP1R2-' + key
            out['final_launch_result'] = json.dumps(dict(test=data['rp1_r2_technical_tests'][key],registry=data['tests_run']['T-RP1R2-'+key]),sort_keys=True)
        elif key == 'S5B':
            out.update(code_or_record=location(C/'f3_rp1-r2_launch_attempt_2026-10-10.py','main'),
                verification='Immutable launch records and append-only attempt log; D-14 hash-bound authorization',evidence=rel(end_path),
                final_launch_result=json.dumps({k:end[k] for k in ('attempt','launch','code_sha256','directory','start_utc','end_utc','return_code','outputs_discarded','outside_w3_attempt')},sort_keys=True))
        else:
            path = record_paths[key]
            out['code_or_record'] = rel(path) + ':1'
            out['verification'] = 'Named final record and its external checksum; independent audit pending'
            out['final_launch_result'] = 'N/A (record requirement; no independent closure claimed)'
            out['evidence'] = rel(path)
        map_rows.append(out)
    requirement_map = table('requirement_map_final',list(map_rows[0]),map_rows,'final requirement map; results copied from immutable JSON')
    original_ledger = json.loads((P / 'f3_realdata_prep_rp1-r2_ledger_2026-10-10.json').read_text(encoding='utf8'))
    final_ledger = json.loads(json.dumps(original_ledger))
    code_items = {'IR1-02':'Q1','IR1-03':'Q2','IR1-04':'Q3','IR1-05':'Q4','IR1-06':'Q5','IR1-07':'Q5',
        'IR1-08':'Q6','IR1-09':'Q7','IR1-10':'Q8','IR1-11':'Q9','IR1-12':'Q10','IR1-18':'Q11'}
    inherited_tests = {'RP1A-01':'T-F1-HANDOFF-SYNTH','RP1A-02':'T-F1-LOADER-SYNTH','RP1A-03':'T-NONREG-R4-2',
        'RP1A-04':'T-STORE-READ-ACCOUNTING','R42A-03 (b)':'T-STORE-READ-ACCOUNTING'}
    doc_evidence = {'RP1A-05':estimate,'RP1A-06':requirement_map,'IR1-14':record_paths['IR1-14'],
        'IR1-15':record_paths['IR1-15'],'IR1-16':diff_custody,'IR1-17':requirement_map,'IR1-19':fixtures}
    for row in final_ledger['items']:
        if row['status'].startswith('CLOSED'):
            continue
        identifier = row['id']
        row['prelaunch_status'] = row['status']
        row['prelaunch_evidence'] = row['evidence']
        test = 'T-RP1R2-' + code_items[identifier] if identifier in code_items else inherited_tests.get(identifier)
        if test:
            observed = data['tests_run'][test]
            assert observed['ran'] and observed['passed']
            row['status'] = 'IMPLEMENTED_PENDING_VERIFICATION'
            row['evidence'] = rel(RESULT) + '#tests_run.' + test + '; SHA256 ' + result_hash
        elif identifier in doc_evidence:
            row['status'] = 'IMPLEMENTED_PENDING_VERIFICATION'
            row['evidence'] = rel(doc_evidence[identifier]) + '; record delivered, independent verification pending'
        elif identifier == 'IR1-13':
            row['status'] = 'OPEN'
            row['evidence'] = 'D-14 RECORDED_LIMITATION; ' + rel(record_paths['S5A']) + '; SHA256 ' + sha(record_paths['S5A']) + '; original standalone source hash NOT OBSERVED; no closure claimed'
    final_ledger.update(status=data['end_state']['rp1_r2_status'],source_results=rel(RESULT),source_results_sha256=result_hash,
        note='Final documentary evidence update only. Run results preserve the prelaunch ledger snapshot. No current item is CLOSED by this executor.')
    ledger = write(final_ledger_path,json.dumps(final_ledger,indent=2,ensure_ascii=True)+'\n','final ledger; independent closure pending')
    stats = dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),rp1_r2_status=data['end_state']['rp1_r2_status'],
        final_attempt=end['attempt'],final_launch=end['launch'],pid=end['pid'],exit_code=end['return_code'],start_utc=end['start_utc'],end_utc=end['end_utc'],
        elapsed_seconds=(dt.datetime.fromisoformat(end['end_utc'])-dt.datetime.fromisoformat(end['start_utc'])).total_seconds(),
        recorded_tests=len(data['tests_run']),passed_tests=sum(v['ran'] and v['passed'] for v in data['tests_run'].values()),
        technical_cases=sum(len(v['cases']) for v in data['rp1_r2_technical_tests'].values()),technical_q3_cases=len(data['rp1_r2_technical_tests']['Q3']['cases']),
        nonregression_rows=len(nonreg),e_declared=data['nonregression_vs_r4_2']['e_declared'],s_findings=len(data['nonregression_vs_r4_2']['s_findings']),u_findings=len(data['nonregression_vs_r4_2']['u_findings']),
        telemetry_rows=len(read_csv(C/'f3_step2_telemetry_rp1-r2_2026-10-10.csv')),percall_rows=len(read_csv(C/'f3_step2_spline_percall_telemetry_rp1-r2_2026-10-10.csv')),
        family_rows=len(family),timing_rows=len(timings),store_manifest_rows=len(read_csv(C/'f3_step2_rp1-r2_restart_store_manifest_2026-10-10.csv')),
        store_read_rows=len(read_csv(C/'f3_step2_rp1-r2_store_read_log_2026-10-10.csv')),fixture_input_files=len(fixture_paths),
        run1_canonical_sha256=data['run1_canonical_sha256'],run2_canonical_sha256=data['run2_canonical_sha256'],
        result_sha256=result_hash,harness_sha256=sha(H),ledger_status_counts=dict(Counter(x['status'] for x in final_ledger['items'])),
        result_end_state=data['end_state'],real_data_access=data['real_data_access'],environment=data['environment'],historical_errata=json.loads((P/'f3_realdata_prep_rp1-r2_historical_count_errata_2026-10-10.json').read_text()),
        final_ledger_open_findings=[x['id'] for x in final_ledger['items'] if x['status']=='OPEN'])
    summary = record('final_observed_summary',stats,'final observed statistics; values derived from named bytes')
    with LOG.open('a',encoding='utf8',newline='\n') as stream:
        stream.write('\n## Final section-8 delivery preparation\n\nNative record generation only; no harness, copy, test excerpt, optimizer or real-data execution. Attempt 1 failed with missing ADDITION declarations; the logged section-0 correction and PI-authorized attempt-2 provenance patch are retained. Attempt 2 completed with exit code '+str(end['return_code'])+'. No outside-W3 execution output is imported. Restart stores, pickle payloads and ZIPs are excluded from Git delivery.\n\n```json\n'+json.dumps(stats,indent=2,ensure_ascii=True)+'\n```\n')
    Path(str(LOG)+'.sha256').write_text(sha(LOG)+'  '+LOG.name+'\n',encoding='ascii')
    add(LOG,'complete attempt log, including failed attempt, correction and outside-W3 custody')
    register_text = '# rp1-r2 final implementation pin register\n\nNON-NORMATIVE. Child of '+rel(C/'f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md')+' (SHA256 '+sha(C/'f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md')+'). No frozen scientific rule changes.\n\nHarness SHA256: '+sha(H)+'\n\nrp1-r2_status: '+data['end_state']['rp1_r2_status']+'\n\nKey namespace and optimizer/store accounting, transferred from final results:\n\n```json\n'+json.dumps(dict(namespace=data['key_namespace_table'],process=data['process'],handoff=data['handoff_outputs'],inadmissible=data['inadmissible_completed_counts']),indent=2,ensure_ascii=True)+'\n```\n\nQ1-Q11 observed checks:\n\n```json\n'+json.dumps(data['rp1_r2_technical_tests'],indent=2,ensure_ascii=True)+'\n```\n'
    register = write(C/('f3_step2_class_c_pin_register_rp1-r2_'+DATE+'.md'),register_text,'final implementation pin register')
    procedure = write(P/(PREFIX+'auditor_rerun_procedure_'+DATE+'.md'),
        '# rp1-r2 independent auditor rerun procedure\n\nUse a disposable copy of this committed package, with the unchanged delivered harness and dependencies. This is a procedure, not an executor self-audit. Match the binding environment recorded in results and W-3.\n\n'
        'Move the copy\'s attempt-2/launch-1 W-3 file and its sidecar, launch/controller start/end/pid/writer records, and attempt-2 stdout/stderr logs to a kept-aside directory. Preserve the originals. The writer refuses an existing custody file and the launcher refuses existing records. The copy\'s `.rp1-r2_attempt2_restart_store_2026-10-10` starts empty and is never the executor store.\n\n'
        'Set F3_REPO_ROOT to the disposable copy, F3_RP1R2_LAUNCH to the actual launch number (1 for the first launch), and OMP_NUM_THREADS/OPENBLAS_NUM_THREADS/MKL_NUM_THREADS to 1. Run the delivered launcher with Python 3.11.7. It writes its own W-3 before the harness. Keep every launch pair and log every invocation under section 5(b). Outputs remain in the copy. Do not edit D-14 or bypass its fixed hash.\n\n'
        'Compare environment, mandatory tests, S scientific objects, RUN1/RUN2 canonical hashes, complete leaf-level non-regression CSV, positive/negative Q cases, Q10 family/mode accounting, and every delivery checksum. Any S difference is a failure regardless of environment; an environment difference does not establish its cause. No real F1/SSA files or eligible/hash tables are read. Only the independent auditor or a named PI decision may close findings.\n', 'independent audit procedure; no new dry-run claimed')
    response_rows = []
    for q,observed in data['rp1_r2_technical_tests'].items():
        response_rows.append(dict(requirement=q,kind='HESAPLAMA',evidence='rp1_r2_technical_tests.'+q,result=json.dumps(observed,sort_keys=True)))
    response_map = {'R-1':['T-F1-HANDOFF-SYNTH','T-F1-CONTRACT-GAP','T-F1-REPRO-GATE-SYNTH'],'R-2':['T-F1-LOADER-SYNTH'],
        'R-3':['T-NONREG-R4-2'],'R-4':[],'R-5':['T-STORE-READ-ACCOUNTING'],'R-6':[],
        'C-1':['T-CALLCOUNT'],'C-2':['T-KEY-NAMESPACE'],'C-3':['T-F1-LOADER-SYNTH'],'C-4':['T-CONTEXT-ID-UNIQUE'],'C-5':['T-INADMISSIBLE-OBSERVABLE'],'C-6':['T-NONREG-R4-2']}
    for name,tests in response_map.items():
        response_rows.append(dict(requirement=name,kind='carried requirement',evidence=rel(procedure if name=='R-4' else register if name=='R-6' else RESULT),result=json.dumps({t:data['tests_run'][t] for t in tests},sort_keys=True) if tests else 'Record delivered; independent verification pending'))
    for row in final_ledger['items']:
        if row['id'].startswith('RP1A-'):
            response_rows.append(dict(requirement=row['id'],kind=row['classification'],evidence=row['evidence'],result=row['status']))
    response = table('response_table_final',['requirement','kind','evidence','result'],response_rows,'instruction response table from observed tests and final ledger')
    reused = []
    tree = ast.parse(H.read_text(encoding='utf8'))
    for name in ('GEN_PATH','MANIFEST_REUSED_PATH'):
        node = next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))
        path = ROOT / ast.literal_eval(node.value)
        reused.append(dict(path=rel(path),sha256=sha(path),role='REUSED UNCHANGED; already tracked; not restaged'))
    # No self-hash cycles: the report hashes its payloads; the later
    # transmission list hashes the report and itself has an external sidecar.
    hash_rows = ['| Path | Role | SHA256 |','|---|---|---|']
    hash_rows += ['| '+rel(path)+' | '+role+' | '+sha(path)+' |' for path,role in sorted(PAYLOADS.items(),key=lambda x:rel(x[0]))]
    report_text = '# F3 rp1-r2 final delivery report\n\nrp1-r2_status = **'+data['end_state']['rp1_r2_status']+'**. This is an executor delivery report, not an independent audit or qualification.\n\n'
    report_text += 'Observed final execution and counts (copied by script from named run artifacts):\n\n```json\n'+json.dumps(stats,indent=2,ensure_ascii=True)+'\n```\n\n'
    report_text += 'The run passed every recorded test and the full-depth non-regression gate. Package status remains partial: the original standalone source hash is NOT OBSERVED under D-14 RECORDED_LIMITATION, IR1-13 remains OPEN / B, and the result end-state lists carried limitations. The final ledger adds observed evidence without rewriting the run\'s prelaunch ledger snapshot or closing any finding.\n\n'
    report_text += 'Attempt 1 failed solely at the recorded 22 undeclared test_evidence ran/passed leaves, all absent in r4-2. No existing test flag changed. Section-0 declaration-defect correction appended those exact ADDITION declarations with individual reasons. The PI then authorized attempt counter 2 and supersession/log/store provenance; other code and declarations stayed unchanged. Attempt 1 is quarantined. Store payloads are locally retained and omitted from Git; their manifests and quarantine index are delivered.\n\n'
    report_text += 'Outside-W3 small tests and isolated comparison are fully logged with source hashes, directory, times, outputs and disposition. Their outputs remain outside this repository and every attempt store. They are not imported into this delivery. The results JSON of failed attempt 1 did not exist; only its delivered test_evidence and telemetry could be re-compared before attempt 2.\n\n'
    report_text += 'ESTIMATE is recomputed from Q10 family telemetry and trajectory timing. It describes synthetic full-bank handoff on the binding environment only; it is informational and does not authorize a real-data run. Original historical counts and limitations are listed in the observed-summary errata above; previous reports/packages are unchanged.\n\n'
    report_text += 'Synthetic raw inputs are unchanged. External delivery sidecars live outside the raw trees. Existing checksum files inside negative fixtures are themselves test input data, not rewritten packaging checksums; every such file has an outer delivery checksum.\n\n'
    report_text += 'Record locations: '+rel(requirement_map)+', '+rel(ledger)+', '+rel(response)+', '+rel(register)+', '+rel(estimate)+', '+rel(diff_custody)+'.\n\nReused frozen inputs:\n\n```json\n'+json.dumps(reused,indent=2)+'\n```\n\n'
    report_text += 'Real-data access remains false. No F3 execution readiness or QUALIFIED status is declared. Independent audit remains pending. Commit/push occur only under the PI\'s separate delivery instruction; this report does not infer publication from the synthetic run.\n\n'
    report_text += 'A transport-only ZIP is generated from the verified transmission list after record finalization. It and its checksum remain outside the Git commit, as instructed. No restart directory or pickle payload enters either the commit or transport ZIP.\n\n'
    report_text += 'Full payload hash block (excluding this report and the transmission list generated afterwards to avoid self-hash cycles):\n\n'+'\n'.join(hash_rows)+'\n'
    report = write(P/(PREFIX+'report_'+DATE+'.md'),report_text,'final executor report; explicit rp1-r2_status')
    rows = [dict(path=rel(path),role=role,bytes=path.stat().st_size,sha256=sha(path),sidecar=rel(SIDECARS[path]),sidecar_sha256=sha(SIDECARS[path]))
            for path,role in sorted(PAYLOADS.items(),key=lambda x:rel(x[0]))]
    table('transmission_list',['path','role','bytes','sha256','sidecar','sidecar_sha256'],rows,'final transmission list; own hash external only')
    assert sha(H) == end['code_sha256'] and sha(RESULT) == result_hash
    assert not subprocess.check_output(['git','diff','--name-only'],cwd=ROOT).strip()
    print(json.dumps(dict(transmission=rel(TRANSMISSION),payload_count=len(rows),synthetic_input_files=len(fixture_paths),
                         rp1_r2_status=data['end_state']['rp1_r2_status'],harness_unchanged=True,results_unchanged=True,
                         report=rel(report),tests_passed=stats['passed_tests'],s_findings=stats['s_findings'],u_findings=stats['u_findings'])))


if __name__ == '__main__':
    build()
