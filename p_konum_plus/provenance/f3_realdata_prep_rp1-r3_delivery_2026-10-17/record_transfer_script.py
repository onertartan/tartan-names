"""Build documentary delivery records without changing execution inputs or outputs."""
from __future__ import annotations

import ast
import csv
import datetime as dt
import difflib
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import zipfile

ROOT = Path('G:/PycharmProjects/pkp-worktree')
C = ROOT / 'p_konum_plus/calibration'
P = ROOT / 'p_konum_plus/provenance'
D = P / 'f3_realdata_prep_rp1-r3_delivery_2026-10-17'
H = C / 'f3_step2_adequacy_harness_rp1-r3_2026-10-15.py'
FIX = C / 'f3_step2_rp1-r3_f1_synth_fixtures_2026-10-15'


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def side(p: Path) -> Path:
    s = Path(str(p) + '.sha256')
    with s.open('x', encoding='ascii', newline='\n') as f:
        f.write(sha(p) + '  ' + p.name + '\n')
    return s


def write(p: Path, value: str) -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf8', newline='\n') as f:
        f.write(value)
    side(p)
    return p


def js(p: Path, value: object) -> Path:
    return write(p, json.dumps(value, ensure_ascii=True, indent=2) + '\n')


def table(p: Path, rows: list[dict], fields: list[str] | None = None) -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields or list(rows[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    side(p)
    return p


def load(p: Path) -> object:
    return json.loads(p.read_bytes())


def lines(p: Path) -> list[str]:
    return p.read_text(encoding='utf8').splitlines(keepends=True)


def emit(old: Path, new: Path, name: str, old_labels: dict, new_labels: dict) -> dict:
    a, b = lines(old), lines(new)
    raw = list(difflib.unified_diff(a, b, fromfile=rel(old), tofile=rel(new), n=0))
    patch = write(D / 'IR1-16' / (name + '.diff'), ''.join(raw))
    rowlist = []
    hunk = 0
    i = j = 0
    changed = set()
    rebuilt = []
    cursor = 0
    for op, x, y, q, z in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            rebuilt.extend(a[x:y])
        else:
            rebuilt.extend(b[q:z])
    assert rebuilt == b
    for line in raw[2:]:
        if line.startswith('@@'):
            hunk += 1
            m = re.match(r'@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@', line)
            i, j = map(int, m.groups())
        elif line.startswith(('-', '+')):
            which, n, mapping = ('old', i, old_labels) if line[0] == '-' else ('new', j, new_labels)
            label = mapping.get(n)
            if label is None and not line[1:].strip():
                label = mapping[min(mapping, key=lambda k: (abs(k - n), k))]
            assert label, (name, which, n, line)
            assert ' with ' not in label
            key = (hunk, which, n)
            assert key not in changed
            changed.add(key)
            if rowlist and all(rowlist[-1][k] == v for k, v in dict(hunk=hunk, side=which, label=label).items()) and rowlist[-1]['last'] == n - 1:
                rowlist[-1]['last'] = n
            else:
                rowlist.append(dict(hunk=hunk, side=which, first=n, last=n, label=label,
                                    reason='Source-derived label for this exact changed-line interval; disjoint intervals split mixed hunks.'))
            if which == 'old':
                i += 1
            else:
                j += 1
    covered = {(r['hunk'], r['side'], n) for r in rowlist for n in range(r['first'], r['last'] + 1)}
    assert changed == covered
    labels = table(patch.with_suffix('.labels.csv'), rowlist)
    return dict(baseline=rel(old), baseline_sha256=sha(old), target=rel(new), target_sha256=sha(new),
                diff=rel(patch), diff_sha256=sha(patch), labels=rel(labels), labels_sha256=sha(labels),
                hunks=hunk, changed_lines=len(changed), exact_label_coverage=True,
                label_set=sorted({r['label'] for r in rowlist}))


def main() -> None:
    assert not D.exists(), 'REFUSE_EXISTING_DELIVERY'
    assert not subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT).strip()
    # Protect every existing rp1-r3 record, source and execution output, including all fixture descendants.
    protected = set(C.glob('*rp1-r3*')) | set(P.glob('*rp1-r3*')) | set(P.glob('*rp1-r2*labels_r1*'))
    expanded = set()
    for p in protected:
        if p.is_file():
            expanded.add(p)
        elif p.is_dir():
            expanded.update(x for x in p.rglob('*') if x.is_file())
    protected = {p: sha(p) for p in expanded if p.suffix not in ('.pkl', '.pyc')}
    initial = load(P / 'f3_realdata_prep_rp1-r3_start_state_inventory_2026-10-15.json')
    incoming = [Path(x['destination']) for x in initial['preconditions']['attachments']]
    for item in initial['preconditions']['attachments']:
        assert sha(Path(item['destination'])) == item['sha256']
    result_path = C / 'f3_step2_results_rp1-r3_2026-10-15.json'
    te_path = C / 'f3_step2_test_evidence_rp1-r3_2026-10-15.json'
    result, te = load(result_path), load(te_path)
    end_path = P / 'f3_step2_rp1-r3_attempt2_launch1_end_2026-10-15.json'
    end = load(end_path)
    assert end['return_code'] == 0
    for f in ['stdout', 'stderr']:
        assert sha(Path(end[f])) == end[f + '_sha256']
    state = result['end_state']
    assert state['mandatory_tests_all_run'] and state['corrections_complete']
    assert all(v['ran'] and v['passed'] for v in result['tests_run'].values())
    nr_path = C / 'f3_step2_rp1-r3_nonregression_vs_r4-2_2026-10-15.csv'
    with nr_path.open(encoding='utf8') as f:
        nr = list(csv.DictReader(f))
    assert not any(x['classification'] in ('U_FINDING', 'S_FINDING') for x in nr)
    assert all(x['held'] == 'True' for x in nr if x['declaration_id'])
    D.mkdir()
    js(D / 'preserved_source_inventory.json', [dict(path=rel(p), sha256=h) for p, h in sorted(protected.items())])
    print('PHASE: immutable input/output snapshot captured', flush=True)

    # Reuse only the record-generation utilities, never main or scientific harness imports.
    helper_path = C / 'f3_rp1-r3_write_diff_records_2026-10-15.py'
    spec = importlib.util.spec_from_file_location('record_labels', helper_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    parent = C / 'f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
    r1 = C / 'f3_step2_adequacy_harness_rp1-r1_2026-10-05.py'
    r42 = C / 'f3_step2_adequacy_harness_r4-2_2026-09-30.py'
    corrected = {}
    for baseline in ['rp1-r1', 'r4-2']:
        src = P / ('f3_realdata_prep_rp1-r2_harness_diff_vs_' + baseline + '_labels_r1_2026-10-15.csv')
        with src.open(encoding='utf8') as f:
            corrected[baseline] = list(csv.DictReader(f))
        assert all(' with ' not in r['label'] for r in corrected[baseline])
    diffs = [emit(parent, H, 'rp1-r3_vs_rp1-r2_harness', m.harness_labels(parent.read_text(encoding='utf8')), m.harness_labels(H.read_text(encoding='utf8')))]
    print('PHASE: rp1-r2 harness diff generated', flush=True)
    old_origins, r1_origins = m.annotations(C / 'f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff')
    parent_origins = m.propagate(lines(r1), lines(parent), r1_origins)
    for row in corrected['rp1-r1']:
        if row['side'] == 'new':
            for n in range(int(row['first']), int(row['last']) + 1):
                parent_origins[n] = 'rp1-r2:' + row['label']
    current_origins = m.propagate(lines(parent), lines(H), parent_origins)
    own = m.harness_labels(H.read_text(encoding='utf8'))
    for op, a, b, x, y in difflib.SequenceMatcher(None, lines(parent), lines(H), autojunk=False).get_opcodes():
        if op != 'equal':
            for n in range(x + 1, y + 1):
                current_origins[n] = 'rp1-r3:' + own[n]
    for row in corrected['r4-2']:
        if row['side'] == 'old':
            for n in range(int(row['first']), int(row['last']) + 1):
                old_origins.setdefault(n, 'rp1-r2:' + row['label'])
    for op, a, b, x, y in difflib.SequenceMatcher(None, lines(r42), lines(H), autojunk=False).get_opcodes():
        if op != 'equal':
            for n in range(a + 1, b + 1):
                old_origins.setdefault(n, 'rp1-r3:R3-5')
    diffs.append(emit(r42, H, 'rp1-r3_vs_r4-2_harness', old_origins, current_origins))
    for family, stem in [('tools', 'gate_tools'), ('tests', 'technical_tests'), ('launcher', 'launch_attempt'), ('writer', 'write_custody')]:
        old = C / ('f3_rp1-r2_' + stem + '_2026-10-10.py')
        new = C / ('f3_rp1-r3_' + stem + '_2026-10-15.py')
        diffs.append(emit(old, new, 'rp1-r3_vs_rp1-r2_' + family, m.function_labels(old.read_text(encoding='utf8'), family), m.function_labels(new.read_text(encoding='utf8'), family)))
    js(D / 'IR1-16' / 'diff_custody.json', dict(diffs=diffs, method='Context zero; mixed hunks are partitioned by exact old/new changed-line intervals, each carrying one originating-package label. S8 means section 8 wiring. rp1-r3_vs_rp1-r2 labels are R3-1 through R3-5 or S8 only; the r4-2 set retains historical package/item labels.', corrected_rp1_r2_labels=[rel(P / ('f3_realdata_prep_rp1-r2_harness_diff_vs_' + b + '_labels_r1_2026-10-15.csv')) for b in corrected], old_attempt1_rp1_r3_diff_records='Historical only; superseded for attempt 2 by this diff_custody.json.'))
    print('PHASE: all source diffs generated', flush=True)

    # IR2-07: only the named, already-authorized provenance records are admitted.
    obs_path = P / 'f3_realdata_prep_rp1-r3_IR2-07_observations_2026-10-15.json'
    oldobs = load(obs_path)
    reviewed = []
    ir2_payloads = []
    for record in oldobs['records']:
        item = dict(record)
        if record['status'] == 'OBSERVED_HASH_MATCH':
            authority = ROOT / record['authority_path']
            delivered = ROOT / record['delivered_path']
            valid = authority.exists() and sha(authority) == record['authority_sha256']
            valid = valid and record['expected_sha256'] in authority.read_text(encoding='utf8')
            valid = valid and delivered.exists() and sha(delivered) == record['expected_sha256']
            if valid:
                item['delivery_reverification'] = 'AUTHORITY_AND_DELIVERED_BYTES_MATCH'
                ir2_payloads.append(delivered)
            else:
                item['status'] = 'NOT OBSERVED'
                item['reason'] = 'Named authority or delivered record unavailable or hash mismatch at final delivery; no reconstruction.'
        reviewed.append(item)
    ir2 = js(D / 'IR2-07_reverification.json', dict(source=rel(obs_path), source_sha256=sha(obs_path), records=reviewed,
        observed_hash_match_count=sum(x['status'] == 'OBSERVED_HASH_MATCH' for x in reviewed),
        not_observed_count=sum(x['status'] == 'NOT OBSERVED' for x in reviewed),
        real_data_access=False, contamination_inferred=False, D14_extended=False))
    audit_path = ROOT / 'p_konum_plus/prompts/f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md'
    audit_lines = audit_path.read_text(encoding='utf8').splitlines()
    audit_row = next((i, s) for i, s in enumerate(audit_lines, 1) if s.startswith('| R42A-09 |') and '[A]/[A-S]' in s)
    reason = audit_row[1].split('|')[-2].strip()
    ir205 = js(D / 'IR2-05_R42A-09_current_evidence.json', dict(item='IR2-05', executor_status='IMPLEMENTED_PENDING_VERIFICATION',
        subject='R42A-09', prior_auditor_attribution='closed by the rp1-r2 independent audit; this is attribution, not an executor closure',
        auditor_record=rel(audit_path), auditor_record_sha256=sha(audit_path), auditor_record_line=audit_row[0], auditor_reason=reason,
        current_correction_test_source=rel(result_path), current_correction_test_source_sha256=sha(result_path),
        handoff_accounting=result['handoff_outputs']['accounting'], current_context_id_unique=result['context_id_unique'],
        pi_binding_inferred=False))
    ledger = load(P / 'f3_realdata_prep_rp1-r3_ledger_2026-10-15.json')
    ledger_rows = []
    evidence_map = {'IR1-16': D / 'IR1-16/diff_custody.json', 'IR2-04': D / 'auditor_rerun_procedure_r1.md', 'IR2-05': ir205, 'IR2-07': ir2}
    for old in ledger['items']:
        row = {k: v for k, v in old.items() if k not in ('status', 'auditor_status', 'execution_scope_note', 'prelaunch_evidence', 'evidence')}
        row['status'] = 'IMPLEMENTED_PENDING_VERIFICATION' if old.get('due_in_rp1_r3') else ('HISTORICAL_AUDIT_ATTRIBUTION' if str(old.get('status', '')).startswith('CLOSED') else old.get('status', 'OPEN'))
        row['source_ledger'] = rel(P / 'f3_realdata_prep_rp1-r3_ledger_2026-10-15.json')
        row['source_evidence'] = old.get('evidence')
        if old['id'] == 'R42A-09':
            row['source_evidence'] = reason
            row['current_evidence'] = rel(ir205)
        elif old['id'] in evidence_map:
            row['current_evidence'] = rel(evidence_map[old['id']])
        elif old.get('due_in_rp1_r3'):
            row['current_evidence'] = rel(result_path)
        ledger_rows.append(row)
    js(D / 'ledger_delivery.json', dict(status=state['rp1_r3_status'], source_ledger_sha256=sha(P / 'f3_realdata_prep_rp1-r3_ledger_2026-10-15.json'),
        closure_policy='No executor closure; historical dispositions are attributed only. All current items await independent verification.', items=ledger_rows))

    # Extract the actual path expressions without importing the harness.
    tree = ast.parse(H.read_text(encoding='utf8'))
    constants = dict(ATTEMPT_NUMBER=2, LAUNCH_NUMBER=1)
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            key = node.targets[0].id
            try:
                value = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                if isinstance(node.value, ast.JoinedStr):
                    try:
                        value = ''.join(v.value if isinstance(v, ast.Constant) else str(constants[v.value.id]) for v in node.value.values)
                    except (KeyError, AttributeError):
                        continue
                else:
                    continue
            constants[key] = value
    output_paths = set()
    for k, v in constants.items():
        if isinstance(v, str) and v.startswith('p_konum_plus/') and 'rp1-r3' in v and (k.endswith('_PATH') or k in ['RESTART_STORE_DIR']):
            output_paths.add(v)
    for f in list(C.glob('*rp1-r3*')) + list(P.glob('*rp1-r3*')):
        if f.is_file() and (f.name.startswith('f3_step2_') or 'runtime_fixture_custody_attempt2' in f.name or 'size_estimate' in f.name):
            output_paths.add(rel(f))
    output_paths.add(rel(P / 'f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md'))
    runtime_rows = list(csv.DictReader((P / 'f3_realdata_prep_rp1-r3_runtime_fixture_custody_attempt2_launch1_2026-10-15.csv').open(encoding='ascii')))
    fixture_files = {rel(f): sha(f) for f in FIX.rglob('*') if f.is_file()}
    assert {r['path']: r['sha256'] for r in runtime_rows} == fixture_files
    overwrite_rows = []
    for s in sorted(output_paths):
        f = ROOT / s
        overwrite_rows.append(dict(path=s, exists=f.exists(), sha256=sha(f) if f.is_file() else None,
            preservation='Copy and verify this file plus sidecar before exclusive-create removal or overwrite in disposable root only.' if f.is_file() else 'Reserved path or directory; preserve every descendant if present.'))
    overwrite = js(D / 'rerun_overwrite_inventory_r1.json', dict(harness=rel(H), harness_sha256=sha(H), attempt=constants['ATTEMPT_NUMBER'], launch=constants['LAUNCH_NUMBER'],
        files=overwrite_rows, each_sidecar_also_preserved=True, fixture_tree=rel(FIX), observed_fixture_files=runtime_rows,
        attempt_store=constants['RESTART_STORE_DIR'], store_rule='Preserve recursive store inventory outside disposable root; never admit executor .pkl files into rerun store.',
        runtime_fixture_custody=rel(P / 'f3_realdata_prep_rp1-r3_runtime_fixture_custody_attempt2_launch1_2026-10-15.csv'),
        all_transmission_files_also_preserved=True))
    procedure = '# Independent auditor rerun procedure r1\n\n'
    procedure += 'This delivery record applies to the completed attempt/launch identified in rerun_overwrite_inventory_r1.json. The older attempt-1 procedure is historical. It does not authorize an independent auditor to change the frozen source.\n\n'
    procedure += 'Create a disposable checkout of commit `' + initial['head'] + '` and overlay the delivered paths after verifying the transmission list and all sidecars. Keep all real SSA/F1 inputs outside that root. The ZIP is a delivery overlay, not a substitute for the pinned parent checkout.\n\n'
    procedure += 'Before running, copy every existing listed file and its sidecar, the complete synthetic fixture tree (including all negative cases and checksum directories), every runtime artifact named by the transmission list, and every store descendant to a kept-aside directory outside the disposable root. Record relative path, size and SHA256 for each original and copy, and verify equality before any removal. Keep the executor workspace unchanged. Preserve the attempt log and leave a working copy for appended auditor entries.\n\n'
    procedure += 'After verified preservation, remove only disposable copies of exclusive-create custody/writer/start/pid/end records, launch stdout/stderr pairs and sidecars, and the regenerated synthetic fixture tree. Start with an absent or empty attempt store; preserve and remove any old disposable store first. Other generated outputs may be overwritten only after preservation. Preserve the runtime fixture custody record and sidecar as well. No delivered code, prompt, baseline or scientific generator is changed.\n\n'
    procedure += 'Match the Python, NumPy, SciPy, platform and thread settings in the delivered W-3/environment records. Record every invocation. Use the unchanged launcher; it creates the external W-3 and verifies D-14 before computation. In the disposable root set:\n\n```powershell\n$env:F3_REPO_ROOT = (Get-Location).Path\n$env:F3_RP1R3_LAUNCH = "1"\n$env:PYTHONDONTWRITEBYTECODE = "1"\n$env:OMP_NUM_THREADS = "1"\n$env:OPENBLAS_NUM_THREADS = "1"\n$env:MKL_NUM_THREADS = "1"\npython -B p_konum_plus/calibration/f3_rp1-r3_launch_attempt_2026-10-15.py\n```\n\n'
    procedure += 'All source-derived output/reserved paths follow. Preserve each sidecar too; reserved paths absent from the executor output are not fabricated.\n\n'
    procedure += ''.join('- `' + r['path'] + '`\n' for r in overwrite_rows)
    procedure += '\nThe recursive fixture file list and hashes are in rerun_overwrite_inventory_r1.json. Preserve additional files discovered in the actual rerun and transmission inventory. Compare complete result leaves, tests, negative targets, S objects/stops/RUN hashes/residual, fresh/replay accounting and input-open audit; no real SSA/F1 path may be opened or hashed. Any S difference is a failure. This procedure closes no item.\n'
    write(D / 'auditor_rerun_procedure_r1.md', procedure)
    print('PHASE: provenance, ledger and rerun records written', flush=True)

    rows = []
    tech = result['rp1_r2_technical_tests']
    tests_file = C / 'f3_rp1-r3_technical_tests_2026-10-15.py'
    tools_file = C / 'f3_rp1-r3_gate_tools_2026-10-15.py'
    def location(f: Path, function: str) -> str:
        n = next(n for n in ast.walk(ast.parse(f.read_text(encoding='utf8'))) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == function)
        return rel(f) + ':' + str(n.lineno)
    for requirement, block, function, positive, negative in [('R3-1', 'Q6', 'traceback_signature', 'path_normalized', 'multiline type/nonfinal/chained cause and raising-site targets'), ('R3-2', 'Q4', 'constant_ok_count', 'no_constant_ok', 'keyword/dictionary/subscript/name/attribute'), ('R3-3', 'Q5', 'q5_cases', 'count_transition', 'exact failing leaf and classification for each negative'), ('R3-5', 'RRS', 'rrs_cases', 'parent_segment_equal', 'constructed_statement_change_rejected')]:
        source = tools_file if block == 'Q6' else tests_file
        observed = result['rp1_r3_scope_guard'] if block == 'RRS' else tech[block]
        rows.append(dict(requirement=requirement, code_or_record=location(source, function), positive=positive, negative=negative,
            verification='Transferred from executor result block; independent verification pending', result_source=rel(result_path) + ':' + ('rp1_r3_scope_guard' if block == 'RRS' else 'rp1_r2_technical_tests.' + block),
            ran=observed['ran'], passed=observed['pass_'], cases=len(observed['cases']), evidence_sha256=sha(result_path), status='IMPLEMENTED_PENDING_VERIFICATION'))
    for req, evidence in [('R3-4', H), ('5(a1)', D / 'auditor_review_notes.json'), ('5(a2)', P / 'f3_realdata_prep_rp1-r3_attempt2_holdpoint_2026-10-16/C5_results.json'), ('5(b)', P / 'f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md'), ('IR1-16', D / 'IR1-16/diff_custody.json'), ('IR2-04', D / 'auditor_rerun_procedure_r1.md'), ('IR2-05', ir205), ('IR2-07', ir2)]:
        rows.append(dict(requirement=req, code_or_record=rel(evidence), positive='', negative='', verification='Named record, hash and sidecar; independent verification pending', result_source=rel(result_path) if req == 'R3-4' else '', ran='', passed='', cases='', evidence_sha256=sha(evidence) if evidence.exists() else '', status='IMPLEMENTED_PENDING_VERIFICATION'))

    c3 = load(P / 'f3_realdata_prep_rp1-r3_attempt2_holdpoint_2026-10-16/C3_literal_listing.json')
    hist_path = Path('C:/Users/Neo/Downloads/rp1r3_preflight/2026-10-16_attempt2_C5_a1_execution01/comparison_result.json')
    hist = load(hist_path)
    literal_rows = [dict(file=rel(H), line=n, text=H.read_text(encoding='utf8').splitlines()[n - 1]) for n in range(158, 180)]
    review = js(D / 'auditor_review_notes.json', dict(description_literals=literal_rows,
        retained_TEXT_descriptors=c3['TEXT_historical_descriptors_retained'],
        description_effect='The carried third-field labels are documentary sources written into W-3 pin_checks.source. Some names/dates are historically inconsistent with adjacent operational path/hash pairs; all are unchanged in the approved attempt-2 code.',
        historical_comparison_source=str(hist_path), historical_comparison_sha256=sha(hist_path),
        historical_postcomparison_finalization_findings=hist['historical_postcomparison_finalization_findings'],
        further_findings=hist['further_findings'], historical_comparison_output_delivery='Raw outside-W3 output stays outside delivery/store; this is a documentary transcription of the findings.',
        distinction='Historical extra rows belong to delivered rp1-r2 postcomparison finalization; final attempt-2 nonregression is checked independently. The absent-in-both mandatory_tests_missing[*] row is not a new field.'))
    for row in rows:
        if row['requirement'] == '5(a1)':
            row['evidence_sha256'] = sha(review)
    table(D / 'requirement_map.csv', rows)

    residual = C / 'f3_step2_residual_series_rp1-r3_2026-10-15.json'
    resid_record = te['nonregression_vs_r4_1']
    assert sha(residual) == resid_record['residual_series_observed'] == resid_record['residual_series_expected']
    nr_summary = result['nonregression_vs_r4_2']
    scientific = dict(scientific_objects=len(result['evaluations']), stop_count=len(result['stops']), stops=result['stops'],
        RUN1=result['run1_canonical_sha256'], RUN2=result['run2_canonical_sha256'], determinism=result['determinism'],
        residual_sha256=resid_record['residual_series_observed'], residual_bytes_sha256=sha(residual),
        residual_source=rel(te_path) + ':nonregression_vs_r4_1.residual_series_observed',
        residual_source_note='The results JSON has no residual hash leaf. This value is copied from the actual test_evidence result record and independently checked against residual bytes; no output was altered.',
        result_source=rel(result_path), result_sha256=sha(result_path), test_evidence_sha256=sha(te_path))
    observation = dict(rp1_r3_status=state['rp1_r3_status'], scientific=scientific, end_state=state,
        nonregression=nr_summary, all_recorded_tests_ran_and_passed=all(v['ran'] and v['passed'] for v in result['tests_run'].values()),
        recorded_tests=len(result['tests_run']), nonregression_csv_rows=len(nr), every_declared_expectation_held=all(r['held'] == 'True' for r in nr if r['declaration_id']),
        executor_elapsed_seconds=(dt.datetime.fromisoformat(end['end_utc']) - dt.datetime.fromisoformat(end['start_utc'])).total_seconds(),
        launch_end_record=rel(end_path), launch_end_record_sha256=sha(end_path),
        IR2_07_observed=sum(x['status'] == 'OBSERVED_HASH_MATCH' for x in reviewed), IR2_07_not_observed=sum(x['status'] == 'NOT OBSERVED' for x in reviewed),
        real_data_access=result['real_data_access'], commit=False, push=False, independent_audit_performed=False)
    js(D / 'executor_observations.json', observation)
    report = '# rp1-r3 teslim raporu\n\nrp1-r3_status = `' + state['rp1_r3_status'] + '`\n\n'
    report += 'Bu rapordaki hash, sayi ve sonuc durumlari dosyalardan betikle aktarildi. Kod ve kosu ciktilari degistirilmedi. Bagimsiz denetim yapilmadi; hicbir madde icin yurutucu kapanis karari verilmedi.\n\n'
    report += '## S sinifi ve kosu sonucu\n\n```json\n' + json.dumps(observation, ensure_ascii=True, indent=2) + '\n```\n\n'
    report += 'Residual hash sonuc JSON dosyasinda bulunmuyor; yukaridaki kaynak notunda belirtildigi gibi test_evidence sonuc kaydindan aktarildi ve residual baytlariyla dogrulandi.\n\n'
    report += '## Denetci icin bilinen aciklama dizgileri\n\n'
    report += 'Asagidaki kaynak dizgileri onaylanan kodda aynen korundu. Ucuncu tuple alani W-3 pin_checks.source alanina yazilir; operasyonel yol/hash alanlariyla karistirilmamalidir.\n\n```text\n'
    report += ''.join(str(r['line']) + ': ' + r['text'] + '\n' for r in literal_rows) + '```\n\n'
    report += '## Tarihsel karsilastirmanin ek satirlari\n\n'
    report += 'Bu liste §5(a1) tarihsel rp1-r2 karsilastirmasinin kaydindan aktarilmistir. Yeni exception-normalization farki listesiyle ayni sey degildir. Eksik-yol satiri dahil tam degerler auditor_review_notes.json icindedir.\n\n```text\n'
    report += ''.join(x['path'] + '\n' for x in hist['historical_postcomparison_finalization_findings']) + '```\n\n'
    report += '## Kayitlar ve sinirlar\n\n'
    report += 'Guncel diff ve etiket otoritesi IR1-16/diff_custody.json dosyasidir. Eski attempt-1 diff/prosedur kayitlari tarihseldir. rp1-r2 duzeltilmis r1 etiket dosyalari ayri teslim edilir; onceki etiketler degistirilmez.\n\n'
    report += 'IR2-04 icin auditor_rerun_procedure_r1.md ve recursive dosya envanteri; IR2-05 icin kaynak denetci gerekcesiyle R42A-09 kaydi; IR2-07 icin hash eslesen adlandirilmis dosyalar ve kalan NOT OBSERVED kayitlari teslim edilir. Yokluktan kontaminasyon sonucu cikarilmadi, D-14 genisletilmedi.\n\n'
    report += 'IR1-13 OPEN / B olarak kalir. Onceki denetci kararlarinin atfi yeni bir executor kapanisi degildir. Guncel teslim maddeleri IMPLEMENTED_PENDING_VERIFICATION durumundadir.\n\n'
    report += 'ZIP, sabit parent checkout uzerine uygulanan teslim katmanidir. Restart store dizinleri, .pkl, __pycache__, onceki ZIP paketleri ve rp1r1_audit dosyalari teslim ZIPine alinmaz. Ham dis-W3 test ciktilari bu pakete veya storea alinmaz; yalniz yurutme kayitlari ve sonuc aktarma belgeleri teslim edilir. IR2-07 kapsaminda acikca adlandirilmis tarihsel provenance dosyalari ayridir.\n\n'
    report += 'Commit veya push yapilmadi. Tam kosu yeniden baslatilmadi.\n'
    write(D / 'executor_report.md', report)
    js(D / 'attempt_log_delivery_addendum.json', dict(parent_attempt_log=rel(P / 'f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md'),
        parent_attempt_log_sha256=sha(P / 'f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md'),
        event='POSTRUN_DOCUMENTARY_DELIVERY_ONLY', source_end=rel(end_path), return_code=end['return_code'],
        prior_attempt_failure='Attempt 1 stopped in the W-3 writer before computation; signed D-20 B authorized bounded attempt-2 repairs and hold point. Attempt-2 code was separately approved by the PI before launch.',
        IR1_13='OPEN / B under signed D-14; RECORDED_LIMITATION', code_changed=False, run_outputs_changed=False, commit=False, push=False))

    # Select only this cycle's deliverables and named incoming records. Never sweep old untracked files.
    payloads = {p for p in expanded if p.is_file() and p.suffix != '.sha256' and p.suffix not in ('.pkl', '.pyc', '.zip')}
    payloads.update(incoming)
    payloads.update(ir2_payloads)
    payloads.add(obs_path)
    for name in ['f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_2026-10-16.md', 'f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md', 'f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md']:
        payloads.add(ROOT / 'p_konum_plus/prompts' / name)
    # Incoming sidecars are immutable, including the CRLF sidecar.
    payloads = {p for p in payloads if p.suffix != '.sha256'}
    payloads.update(f for f in FIX.rglob('*') if f.is_file())
    payloads.update(p for p in D.rglob('*') if p.is_file() and p.suffix != '.sha256')
    # Import the record-producing script as documentary evidence only, outside repository code.
    builder = Path(__file__)
    copied_builder = D / 'record_transfer_script.py'
    shutil.copyfile(builder, copied_builder)
    side(copied_builder)
    payloads.add(copied_builder)
    # Verify every original source/output remains exactly as snapshotted.
    assert all(sha(p) == h for p, h in protected.items()), 'PROTECTED_BYTES_CHANGED'
    verify = js(D / 'delivery_verification.json', dict(protected_files=len(protected), protected_mismatches=[],
        source_code_changed=False, run_outputs_changed=False, tracked_diff=subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT, text=True),
        fixture_files_verified=len(fixture_files), diff_records=len(diffs), changed_line_label_coverage=all(x['exact_label_coverage'] for x in diffs),
        result_status=state['rp1_r3_status'], s_findings=len(nr_summary['s_findings']), u_findings=len(nr_summary['u_findings']),
        declared_expectations_held=observation['every_declared_expectation_held'], all_recorded_tests_ran_and_passed=observation['all_recorded_tests_ran_and_passed'], commit=False, push=False))
    payloads.add(verify)
    transmission_rows = []
    for f in sorted(payloads):
        assert '.rp1-r3_attempt' not in rel(f) and f.suffix not in ('.zip', '.pkl', '.pyc')
        existing = Path(str(f) + '.sha256')
        if existing.exists() and existing.read_text(encoding='utf8').split()[0] == sha(f):
            check = existing
        else:
            # Do not create or repair any sidecar beside a protected output.
            check = D / 'delivery_checksums' / (rel(f) + '.sha256')
            check.parent.mkdir(parents=True, exist_ok=True)
            with check.open('x', encoding='ascii') as stream:
                stream.write(sha(f) + '  ' + f.name + '\n')
        transmission_rows.append(dict(path=rel(f), sha256=sha(f), bytes=f.stat().st_size,
            sidecar_path=rel(check), sidecar_sha256=sha(check)))
    transmission = table(D / 'transmission_list.csv', transmission_rows)
    zpath = Path('C:/Users/Neo/Downloads/f3_realdata_prep_rp1-r3_delivery_2026-10-17.zip')
    assert not zpath.exists()
    archive_paths = {ROOT / r[k] for r in transmission_rows for k in ['path', 'sidecar_path']}
    archive_paths.update([transmission, Path(str(transmission) + '.sha256')])
    with zipfile.ZipFile(zpath, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in sorted(archive_paths):
            z.write(f, rel(f))
    side(zpath)
    with zipfile.ZipFile(zpath) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == {rel(p) for p in archive_paths}
        for r in transmission_rows:
            assert hashlib.sha256(z.read(r['path'])).hexdigest() == r['sha256']
            assert hashlib.sha256(z.read(r['sidecar_path'])).hexdigest() == r['sidecar_sha256']
    assert all(sha(p) == h for p, h in protected.items())
    print(json.dumps(dict(zip=str(zpath), zip_sha256=sha(zpath), transmission=rel(transmission), transmission_sha256=sha(transmission),
        payloads=len(transmission_rows), archive_entries=len(archive_paths), report=rel(D / 'executor_report.md'), scientific=scientific,
        status=state['rp1_r3_status'], protected_files=len(protected)), ensure_ascii=True), flush=True)


if __name__ == '__main__':
    main()
