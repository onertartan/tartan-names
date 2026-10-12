"""Source-authored positive/negative tests; called only inside a W-3 attempt."""
from __future__ import annotations

import ast
import copy
import hashlib
import json
from pathlib import Path
import shutil
from typing import Any


def case(name: str, got: Any, expected: Any) -> dict[str, Any]:
    return dict(name=name, expected=expected, got=got, ok=got == expected)


def summarize(cases: list[dict[str, Any]]) -> dict[str, Any]:
    return dict(ran=True, pass_=bool(cases) and all(row["ok"] for row in cases), cases=cases)


def constant_ok_count(source: str, function: str) -> int:
    tree = ast.parse(source)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function)
    count = 0
    for item in ast.walk(node):
        if isinstance(item, ast.keyword) and item.arg == "ok" and isinstance(item.value, ast.Constant):
            count += 1
        if isinstance(item, ast.Dict):
            count += sum(isinstance(k, ast.Constant) and k.value == "ok" and isinstance(v, ast.Constant)
                         for k, v in zip(item.keys, item.values))
    return count


def id_literal_count(source: str) -> int:
    return sum(isinstance(node, ast.Constant) and node.value == "real:%s:%s:%s"
               for node in ast.walk(ast.parse(source)))


def reproduction_cases(g: dict[str, Any], output: str) -> dict[str, Any]:
    """Q3: each mutation reaches its own check, including content after custody."""
    generator = g["RP2_GENERATOR"]
    tools = g["RP2_TOOLS"]
    fixture = generator.generate(str(Path(output) / "q3_complete"), tools.MANIFEST_COLUMNS)
    rows = fixture["manifest_rows"]
    table = fixture["hash_table"]
    raw = fixture["raw"]
    manifest = fixture["eligible_manifest"]
    cases = []

    def outcome(raw_dir: str, hashes: list[tuple[str, str]], path: str, pin: str) -> str:
        try:
            g["f1_repro_gate"](raw_dir, hashes, path, pin, synthetic=True)
        except g["F1ReproGateFailure"] as error:
            return str(error).split()[0]
        return "PASS"

    cases.append(case("complete", outcome(raw, table, manifest, fixture["manifest_hash"]), "PASS"))
    root = Path(output) / "q3_negative"
    for name, token in (("missing", "F1_REPRO_GATE_MISSING_FILE"),
                        ("extra", "F1_REPRO_GATE_EXTRA_FILE"),
                        ("changed_raw", "F1_REPRO_GATE_HASH_MISMATCH")):
        directory = root / name / "raw"
        if not directory.exists():
            shutil.copytree(raw, directory)
            if name == "missing":
                (directory / table[0][0]).unlink()
            elif name == "extra":
                (directory / "extra.txt").write_bytes(b"TEST_ONLY_EXTRA\n")
            else:
                (directory / table[0][0]).write_bytes(b"TEST_ONLY_CHANGED\n")
        for file in sorted(directory.iterdir()):
            generator.write_fixture(file, file.read_bytes(), directory.parent / "checksums" / (file.name + ".sha256"))
        cases.append(case(name, outcome(str(directory), table, manifest, fixture["manifest_hash"]), token))
    for name, token in (("manifest_hash", "F1_REPRO_GATE_MANIFEST_HASH_MISMATCH"),
                        ("field", "F1_REPRO_GATE_FIELD_MISMATCH"),
                        ("row", "F1_REPRO_GATE_ROW_COUNT"),
                        ("ordering", "F1_REPRO_GATE_ORDERING")):
        changed = copy.deepcopy(rows)
        if name in ("field", "manifest_hash"):
            changed[0]["trajectory_id"] = "TEST_ONLY_WRONG_ID"
        elif name == "row":
            changed.pop()
        else:
            changed[0], changed[1] = changed[1], changed[0]
        path = root / name / "eligible_manifest.csv"
        modified_hash = generator.write_fixture(path, generator.csv_bytes(tools.MANIFEST_COLUMNS, changed))
        # Only the hash case retains its original pin; other cases pass custody.
        pin = fixture["manifest_hash"] if name == "manifest_hash" else modified_hash
        cases.append(case(name, outcome(raw, table, str(path), pin), token))
    return summarize(cases)


def technical_cases(g: dict[str, Any], scenarios: list[dict[str, Any]],
                    handoff: dict[str, Any], reproduction: dict[str, Any]) -> dict[str, Any]:
    tools = g["RP2_TOOLS"]
    source = Path(g["__file__"]).read_text(encoding="utf8")
    out: dict[str, Any] = {}
    original = scenarios[0]
    q1 = [case("complete_intake", tools.check_intake(original, g["F1ContractGap"]), True)]
    calls = [0]
    old_family, old_spline = g["fit_family"], g["fit_spline"]

    def no_fit(*args: Any, **kwargs: Any) -> None:
        calls[0] += 1
        raise AssertionError("OPTIMIZER_REACHED_IN_INTAKE_TEST")

    g["fit_family"] = g["fit_spline"] = no_fit
    try:
        for key in ("real_x", "real_mask_ids"):
            for entry_only in (False, True):
                scenario = copy.deepcopy(original)
                if entry_only:
                    scenario[key].pop(("F", 0))
                    expected = key + "[F,0]"
                else:
                    scenario.pop(key)
                    expected = key
                try:
                    g["run_real_scenario"](None, None, {}, scenario, "TEST_ONLY_Q1", [])
                except g["F1ContractGap"] as error:
                    got = error.key
                else:
                    got = "NO_STOP"
                q1.append(case(expected, got, expected))
        q1.append(case("no_optimizer_reached", calls[0], 0))
    finally:
        g["fit_family"], g["fit_spline"] = old_family, old_spline
    out["Q1"] = summarize(q1)
    out["Q2"] = summarize([
        case("one_literal", id_literal_count(source), 1),
        case("duplicate_rejected", id_literal_count(source + '\nTEST_ONLY_DUPLICATE = "real:%s:%s:%s"\n') != 1, True),
        case("actual_equals_dry", handoff["actual_rows_equal_dry_table"], True)])
    out["Q3"] = reproduction
    out["Q4"] = summarize([
        case("no_constant_ok", constant_ok_count(source, "t_f1_loader_synth"), 0),
        case("constant_rejected", constant_ok_count('def t_f1_loader_synth():\n    return dict(ok=True)\n', "t_f1_loader_synth") > 0, True)])
    bad = [
        ("wrong_equal_count", {"n": 2}, {"n": 2}, dict(path="n", kind="COUNT", old=1, new=3)),
        ("addition_in_both", {"n": 2}, {"n": 2}, dict(path="n", kind="ADDITION")),
        ("unequal_equal", {"n": 2}, {"n": 3}, dict(path="n", kind="EQUAL")),
        ("deep_not_hidden", {"n": {"leaf": 2}}, {"n": {"leaf": 3}}, dict(path="n", kind="MAY_DIFFER")),
        ("absent_in_both", {}, {}, dict(path="missing", kind="ADDITION")),
    ]
    q5 = []
    good = dict(path="n", id="positive", kind="COUNT", old=1, new=3, reason="authored test transition")
    q5.append(case("count_transition", not tools.compare_document({"n": 1}, {"n": 3}, [good], "test")[1], True))
    for name, a, b, spec in bad:
        spec = dict(spec, id=name, reason="source-authored negative")
        q5.append(case(name, bool(tools.compare_document(a, b, [spec], "test")[1]), True))
    out["Q5"] = summarize(q5)
    text = 'def raise_site():\n    raise RuntimeError("first")\n'
    trace = 'Traceback (most recent call last):\n  File "C:/a/demo.py", line 2, in raise_site\nRuntimeError: first\n'
    other_path = trace.replace("C:/a/", "C:/b/")
    different = text.replace('"first"', '"another_statement"')
    a = tools.traceback_signature(trace, text, "demo.py")
    out["Q6"] = summarize([
        case("path_normalized", a == tools.traceback_signature(other_path, text, "demo.py"), True),
        case("changed_raise_rejected", a != tools.traceback_signature(trace, different, "demo.py"), True)])
    stored = [dict(source="fresh", wall_clock_seconds=1.0, method="TEST_ONLY", status="OK")]
    replay = [dict(stored[0], source="replay")]
    corrupted = [dict(replay[0], status="CHANGED")]
    out["Q7"] = summarize([
        case("resumed_cold", g["store_read_aggregate"](dict(pass_=True, fit1_reads=146), dict(pass_=True, fit1_reads=146)), True),
        case("stored_payload_matches", tools.equal_replay(stored, replay), True),
        case("corrupt_payload_rejected", tools.equal_replay(stored, corrupted), False)])
    old_scope = g["KEY_SCOPE"][0]
    q8 = []
    try:
        g["KEY_SCOPE"][0] = "TEST_ONLY_Q8__"
        for family in ("nrgates_all", "unittests_all", "realscen"):
            key = family + "_provenance"
            if g["ckpt_load"](key) is None:
                g["ckpt_save"](key, (dict(unchanged="scientific_value"), [stored[0]]))
            restored = g["ckpt_load"](key)
            q8.append(case(family, restored[1][0]["source"], "replay"))
            q8.append(case(family + "_value", restored[0]["unchanged"], "scientific_value"))
        q8.append(case("fresh_is_not_replay", tools.equal_replay(stored, stored), False))
    finally:
        g["KEY_SCOPE"][0] = old_scope
    out["Q8"] = summarize(q8)
    q9 = [case("onestart_scope", g["_key_family"]("f1handoff__onestart_demo"), "onestart"),
          case("splmode_scope", g["_key_family"]("f1handoff__splmode_demo"), "splmode"),
          case("phase", all(row["phase"] == "f1_handoff" for row in handoff["_family_telemetry"]), True),
          case("wrong_phase_rejected", g["handoff_phase_valid"]([dict(phase="nr_gates")]), False)]
    out["Q9"] = summarize(q9)
    accounting = g["handoff_accounting"](handoff["_family_telemetry"])
    out["Q10"] = summarize([
        case("family_units_reconciled", accounting["pass_"], True),
        case("spline_rows_reconciled", accounting["spline_rows_reconciled"], True),
        case("missing_optimizer_row_rejected", g["handoff_accounting"](handoff["_family_telemetry"][1:])["pass_"], False),
        case("trajectory_timings", len(handoff["_timings"]), sum(len(rows) for rows in original["strata"].values()))])
    out["Q11"] = summarize([
        case("same_launch", tools.launch_matches("7", 7), True),
        case("different_launch", tools.launch_matches("6", 7), False),
        case("missing_launch", tools.launch_matches(None, 7), False)])
    return out
