"""Section 5(a2): run only pure changed test blocks and validate their leaves."""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


def load(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    root, output = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    assert root != output and root not in output.parents
    c = root / "p_konum_plus/calibration"
    harness = c / "f3_step2_adequacy_harness_rp1-r3_2026-10-15.py"
    parent = c / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    helper = c / "f3_rp1-r3_gate_tools_2026-10-15.py"
    test_path = c / "f3_rp1-r3_technical_tests_2026-10-15.py"
    tools, tests = load(helper, "synthetic_gate_tools"), load(test_path, "synthetic_technical_tests")
    source, parent_source = harness.read_bytes().decode("utf-8"), parent.read_bytes().decode("utf-8")
    evidence = dict(Q4=tests.q4_cases(source, tests.constant_ok_count),
                    Q5=tests.q5_cases(tools), Q6=tests.q6_cases(tools))
    scope = tests.rrs_cases(source, parent_source)
    main_node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef) and n.name == "main")
    node = next(n for n in main_node.body if isinstance(n, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == "EXPECTATIONS_E" for t in n.targets))
    specs = ast.literal_eval(node.value)
    namespace_results = {}
    for namespace in ("results", "test_evidence"):
        old = {"unchanged_control": "TEST_ONLY"}
        new = dict(old, rp1_r2_technical_tests=evidence, rp1_r3_scope_guard=scope,
                   tests_run={"T-RP1R3-RRS-UNCHANGED": dict(ran=True, passed=scope["pass_"])})
        if namespace == "results":
            new["end_state"] = dict(rp1_r3_status="PARTIAL_PENDING_PI", rp1_r3_open_findings=[])
        leaves = tools.flatten_document(new)
        selected = [s for s in specs[namespace] if any(tools.declaration_matches(s["path"], p) for p in leaves)]
        assert all(s["kind"] == "ADDITION" for s in selected)
        rows, failures = tools.compare_document(old, new, selected, namespace)
        namespace_results[namespace] = dict(old=old, new=new, declarations=selected, rows=rows,
                                             failures=failures, all_declarations_held=not failures)
    blocks = dict(evidence, RRS=scope)
    result = dict(scope="Section 5(a2); only pure Q4/Q5/Q6/RRS blocks; no harness import/main, optimizer or store",
        inputs={str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (harness, parent, helper, test_path)},
        tests=blocks, namespaces=namespace_results,
        passed=all(x["pass_"] for x in blocks.values()) and all(not x["failures"] for x in namespace_results.values()),
        actual_optimizer_calls=0, store_access=False, real_data_access=False,
        output_disposition="RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE")
    (output / "synthetic_result.json").write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="ascii")
    print(json.dumps(dict(passed=result["passed"], block_passes={k: v["pass_"] for k, v in blocks.items()},
                         block_case_counts={k: len(v["cases"]) for k, v in blocks.items()},
                         namespace_failures={k: len(v["failures"]) for k, v in namespace_results.items()})))
    if not result["passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
