"""Section 5(a1): compare delivered historical documents; never run the harness."""
from __future__ import annotations

import ast
import csv
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


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root, output = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    assert root != output and root not in output.parents
    c = root / "p_konum_plus/calibration"
    parent = c / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    source = parent.read_text(encoding="utf-8")
    tree = ast.parse(source)
    body = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main").body
    declaration = next(n for n in body if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == "EXPECTATIONS_E" for t in n.targets))
    specs = ast.literal_eval(declaration.value)
    old_tools = load(c / "f3_rp1-r2_gate_tools_2026-10-10.py", "historical_old_tools")
    new_tools = load(c / "f3_rp1-r3_gate_tools_2026-10-15.py", "historical_new_tools")
    baseline = c / "f3_step2_adequacy_harness_r4-2_2026-09-30.py"
    baseline_source = baseline.read_text(encoding="utf-8")
    inputs = [parent, baseline, Path(old_tools.__file__), Path(new_tools.__file__)]
    all_rows: dict[str, list[dict[str, Any]]] = {"old": [], "new": []}
    for namespace, stem in (("results", "results"), ("test_evidence", "test_evidence")):
        a = c / f"f3_step2_{stem}_r4-2_2026-09-30.json"
        b = c / f"f3_step2_{stem}_rp1-r2_2026-10-10.json"
        inputs.extend([a, b])
        before, after = json.loads(a.read_bytes()), json.loads(b.read_bytes())
        for label, tools in (("old", old_tools), ("new", new_tools)):
            left = tools.normalize_traces(before, baseline_source, baseline.name)
            right = tools.normalize_traces(after, source, parent.name)
            if namespace == "results":
                scientific = {"evaluations", "stops", "run1_canonical_sha256",
                              "run2_canonical_sha256", "determinism"}
                left = {k: v for k, v in left.items() if k not in scientific}
                right = {k: v for k, v in right.items() if k not in scientific}
            rows, _ = tools.compare_document(left, right, specs[namespace], namespace)
            all_rows[label].extend(rows)

    # Use the production telemetry excerpt unchanged, rather than another comparator.
    def target(node: ast.stmt, name: str) -> bool:
        return isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)

    start = next(i for i, n in enumerate(body) if isinstance(n, ast.With)
                 and isinstance(n.items[0].context_expr, ast.Call)
                 and n.items[0].context_expr.args
                 and isinstance(n.items[0].context_expr.args[0], ast.Name)
                 and n.items[0].context_expr.args[0].id == "R4_2_TELEMETRY_PATH")
    end = next(i for i, n in enumerate(body) if target(n, "nonreg42_rows"))
    excerpt = body[start:end]
    assert len(excerpt) == 4
    (output / "executed_source_excerpts.txt").write_text(
        "\n\n".join(ast.get_source_segment(source, n) for n in excerpt) + "\n", encoding="utf-8")
    tel_a = c / "f3_step2_telemetry_r4-2_2026-09-30.csv"
    tel_b = c / "f3_step2_telemetry_rp1-r2_2026-10-10.csv"
    inputs.extend([tel_a, tel_b])
    env: dict[str, Any] = dict(csv=csv, R4_2_TELEMETRY_PATH=str(tel_a),
                               TELEMETRY_PATH=str(tel_b), e_rows=[], u_findings=[])
    exec(compile(ast.Module(body=excerpt, type_ignores=[]), str(parent), "exec"), env)
    for label in all_rows:
        all_rows[label].extend(env["e_rows"])
    delivered = c / "f3_step2_rp1-r2_nonregression_vs_r4-2_2026-10-10.csv"
    inputs.append(delivered)
    with delivered.open(encoding="utf-8", newline="") as stream:
        delivered_rows = {r["path"]: r for r in csv.DictReader(stream)}
    maps = {label: {r["path"]: r for r in rows} for label, rows in all_rows.items()}
    changed = []
    trace_rows = []
    for path in sorted(set(maps["old"]) | set(maps["new"])):
        a, b = maps["old"].get(path), maps["new"].get(path)
        if a != b:
            changed.append(dict(path=path, old=a, new=b, delivered=delivered_rows.get(path)))
        if path.endswith(".traceback"):
            trace_rows.append(dict(path=path, old=a, new=b, delivered=delivered_rows.get(path)))
    further = [r for r in changed if r["new"] is None or not r["new"]["held"]]
    # Finished results contain fields appended AFTER the historical comparison.
    # Compare both normalizers on the same delivered bytes and disclose these
    # pre-existing differences separately; they cannot hide any new trace finding.
    historical_finalization_findings = [r for r in all_rows["old"] if not r["held"]]
    trace_reference_matches = all(r["delivered"] is not None
        and r["new"]["classification"] == r["delivered"]["classification"]
        and str(r["new"]["held"]) == r["delivered"]["held"] for r in trace_rows)
    result = dict(scope="Section 5(a1); full delivered results/test_evidence and production telemetry excerpt; parent declarations only",
        inputs={str(p): digest(p) for p in inputs},
        delivered_row_count=len(delivered_rows), comparator_row_counts={k: len(v) for k, v in all_rows.items()},
        historical_postcomparison_finalization_findings=historical_finalization_findings,
        normalized_trace_rows=trace_rows, changed_rows=changed, further_findings=further,
        trace_classifications_match_delivered=trace_reference_matches,
        production_telemetry_findings=env["u_findings"],
        passed=not further and trace_reference_matches and not env["u_findings"],
        actual_optimizer_calls=0, store_access=False, real_data_access=False,
        output_disposition="RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE")
    (output / "comparison_result.json").write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="ascii")
    print(json.dumps({k: result[k] for k in ("passed", "comparator_row_counts", "trace_classifications_match_delivered")}))
    print(json.dumps(dict(further_finding_count=len(further), trace_count=len(trace_rows),
                          historical_finalization_finding_count=len(historical_finalization_findings))))
    if not result["passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
