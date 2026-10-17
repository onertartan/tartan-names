"""Execute only the delivered test-evidence and telemetry comparator excerpts."""
from __future__ import annotations

import ast
import csv
import hashlib
import importlib.util
import json
import os
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(os.environ['F3_REPO_ROOT']).resolve()
C = ROOT / 'p_konum_plus/calibration'
Q = ROOT / 'p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration'
OUT = Path(os.environ['F3_COMPARATOR_OUTPUT_ROOT']).resolve()
H = C / 'f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main_and_specs(tree: ast.Module) -> tuple[ast.FunctionDef, dict[str, Any]]:
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    node = next(n for n in main.body if isinstance(n, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == 'EXPECTATIONS_E' for t in n.targets))
    return main, ast.literal_eval(node.value)


def target(node: ast.stmt, name: str) -> bool:
    return isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)


def main() -> None:
    assert ROOT not in OUT.parents and OUT != ROOT
    assert not (C / '.rp1-r2_restart_store_2026-10-10').exists()
    assert sha(H) == 'd34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3'
    attempt1_harness = Q / H.name
    assert sha(attempt1_harness) == '92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c'
    source = H.read_text(encoding='utf8')
    source1 = attempt1_harness.read_text(encoding='utf8')
    tree = ast.parse(source)
    harness_main, new_specs = main_and_specs(tree)
    _, old_specs = main_and_specs(ast.parse(source1))
    helper = C / 'f3_rp1-r2_gate_tools_2026-10-10.py'
    assert sha(helper) == 'ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7'
    spec = importlib.util.spec_from_file_location('rp2_comparator_only', helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    baseline_path = C / 'f3_step2_test_evidence_r4-2_2026-09-30.json'
    telemetry_baseline = C / 'f3_step2_telemetry_r4-2_2026-09-30.csv'
    assert sha(baseline_path) == 'c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf'
    assert sha(telemetry_baseline) == 'ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d'
    current_path = Q / 'f3_step2_test_evidence_rp1-r2_2026-10-10.json'
    current_tel = Q / 'f3_step2_telemetry_rp1-r2_2026-10-10.csv'
    baseline_source = (C / 'f3_step2_adequacy_harness_r4-2_2026-09-30.py').read_text(encoding='utf8')
    old_doc = json.loads(baseline_path.read_text(encoding='utf8'))
    current_doc = json.loads(current_path.read_text(encoding='utf8'))
    canon_node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'canon')
    start = next(i for i, n in enumerate(harness_main.body) if target(n, 'te_old'))
    te_nodes = harness_main.body[start:start + 3]
    assert target(te_nodes[1], 'te_new') and isinstance(te_nodes[2], ast.Assign)
    assert ast.unparse(te_nodes[2].targets[0]) == '(more_rows, more_findings)'
    tel_start = next(i for i, n in enumerate(harness_main.body) if isinstance(n, ast.With)
                     and isinstance(n.items[0].context_expr, ast.Call)
                     and isinstance(n.items[0].context_expr.args[0], ast.Name)
                     and n.items[0].context_expr.args[0].id == 'R4_2_TELEMETRY_PATH')
    tel_end = next(i for i, n in enumerate(harness_main.body) if target(n, 'nonreg42_rows'))
    tel_nodes = harness_main.body[tel_start:tel_end]
    assert len(tel_nodes) == 4 and isinstance(tel_nodes[-1], ast.For)
    excerpts = [canon_node, *te_nodes, *tel_nodes]
    excerpt_text = '\n\n'.join(ast.get_source_segment(source, node) for node in excerpts) + '\n'
    excerpt_path = OUT / 'executed_source_excerpts.txt'
    excerpt_path.write_text(excerpt_text, encoding='utf8')
    te_code = compile(ast.Module(body=te_nodes, type_ignores=[]), str(H), 'exec')
    tel_code = compile(ast.Module(body=tel_nodes, type_ignores=[]), str(H), 'exec')
    env: dict[str, Any] = dict(np=np, Path=Path, csv=csv, RP2_TOOLS=module,
        _r42te_doc=old_doc, test_evidence=current_doc, baseline_source=baseline_source,
        baseline_name='f3_step2_adequacy_harness_r4-2_2026-09-30.py',
        # Attempt-1 trace coordinates must be resolved against attempt-1 bytes.
        this_source=source1, __file__=str(H), R4_2_TELEMETRY_PATH=str(telemetry_baseline),
        TELEMETRY_PATH=str(current_tel), e_rows=[], u_findings=[])
    exec(compile(ast.Module(body=[canon_node], type_ignores=[]), str(H), 'exec'), env)
    env['EXPECTATIONS_E'] = old_specs
    exec(te_code, env)
    before = env['more_findings']
    expected_paths = {f'test_evidence.tests_run.T-RP1R2-Q{q}.{flag}'
                      for q in range(1, 12) for flag in ('ran', 'passed')}
    assert len(before) == 22 and {r['path'] for r in before} == expected_paths
    env['EXPECTATIONS_E'] = new_specs
    exec(te_code, env)
    after = env['more_findings']
    assert not after, 'CORRECTED_TEST_EVIDENCE_COMPARISON_FAILED ' + repr(after)
    added_rows = [r for r in env['more_rows'] if r['path'] in expected_paths]
    assert len(added_rows) == 22 and all(r['held'] and r['kind'] == 'ADDITION' for r in added_rows)
    test_rows = list(env['more_rows'])
    # The same production telemetry code, against the complete delivered CSV.
    exec(tel_code, env)
    assert not env['u_findings'], 'TELEMETRY_COMPARISON_FAILED ' + repr(env['u_findings'][:10])
    telemetry_rows = list(env['e_rows'])
    negative_specs = dict(new_specs, test_evidence=new_specs['test_evidence'][:-1])
    env['EXPECTATIONS_E'] = negative_specs
    exec(te_code, env)
    assert len(env['more_findings']) == 1 and env['more_findings'][0]['path'] in expected_paths
    with (Q / 'f3_step2_rp1-r2_nonregression_vs_r4-2_2026-10-10.csv').open(encoding='utf8', newline='') as stream:
        observed = list(csv.DictReader(stream))
    observed_u = [r for r in observed if r['classification'] == 'U_FINDING']
    assert len(observed_u) == 22 and {r['path'] for r in observed_u} == expected_paths
    assert not any(r['classification'] == 'S_FINDING' for r in observed)
    assert not (C / '.rp1-r2_restart_store_2026-10-10').exists()
    result = dict(scope='Full delivered test_evidence and telemetry, exact production comparator excerpts; no main, no optimizer, no checkpoint read/write',
        before_u_findings=before, after_test_evidence_u_findings=after, after_telemetry_u_findings=env['u_findings'],
        missing_one_declaration_negative_passed=True, added_declaration_rows=added_rows,
        test_evidence_comparison_rows=len(test_rows), telemetry_comparison_rows=len(telemetry_rows),
        telemetry_input_rows=len(env['new_tel']), attempt1_original_csv_s_findings=0,
        results_json_recomparison='NOT POSSIBLE: attempt 1 failed before results JSON serialization; original CSV S/E evidence retained, not re-executed or reconstructed',
        inputs={str(p): sha(p) for p in (H, attempt1_harness, helper, baseline_path, current_path, telemetry_baseline, current_tel)},
        excerpt_sha256=sha(excerpt_path), actual_optimizer_calls=0, attempt_store_absent=True,
        output_disposition='RETAINED_OUTSIDE_REPOSITORY; EXCLUDED_FROM_DELIVERABLES_AND_ALL_ATTEMPT_STORES', real_data_access=False)
    (OUT / 'comparison_result.json').write_text(json.dumps(result, indent=2, ensure_ascii=True) + '\n', encoding='ascii')
    for name, rows in (('test_evidence_comparison.csv', test_rows), ('telemetry_comparison.csv', telemetry_rows)):
        with (OUT / name).open('x', encoding='ascii', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=['path','classification','declaration_id','kind','held','reason','r4_2','rp1-r2'], lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(dict(before_u=22, after_test_evidence_u=0, after_telemetry_u=0,
                         telemetry_input_rows=len(env['new_tel']), negative_passed=True, attempt_store_absent=True)))


if __name__ == '__main__':
    main()
