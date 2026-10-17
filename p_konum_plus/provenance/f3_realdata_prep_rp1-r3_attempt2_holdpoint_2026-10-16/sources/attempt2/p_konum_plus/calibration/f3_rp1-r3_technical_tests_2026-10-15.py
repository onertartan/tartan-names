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
        if isinstance(item, (ast.Assign, ast.AnnAssign)) and isinstance(item.value, ast.Constant):
            targets = item.targets if isinstance(item, ast.Assign) else [item.target]
            for target in targets:
                if (isinstance(target, ast.Name) and target.id == "ok"
                        or isinstance(target, ast.Attribute) and target.attr == "ok"
                        or isinstance(target, ast.Subscript) and isinstance(target.slice, ast.Constant)
                        and target.slice.value == "ok"):
                    count += 1
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


def q4_cases(source: str, counter: Any) -> dict[str, Any]:
    name = "t_f1_loader_synth"
    rows = [case("no_constant_ok", counter(source, name), 0),
            case("constant_rejected", counter('def t_f1_loader_synth():\n    return dict(ok=True)\n', name) > 0, True)]
    statements = dict(keyword="return dict(ok=True)", dictionary='return {"ok": True}',
                      subscript='x["ok"] = True', name="ok = True", attribute="x.ok = True",
                      annotated_subscript='x["ok"]: bool = True', annotated_name="ok: bool = True",
                      annotated_attribute="x.ok: bool = True")
    for spelling, statement in statements.items():
        rows.append(case(spelling + "_count", counter("def " + name + "():\n    " + statement + "\n", name), 1))
    return summarize(rows)


def q5_cases(tools: Any) -> dict[str, Any]:
    rows = []
    good = dict(path="n", id="positive", kind="COUNT", old=1, new=3, reason="authored test transition")
    rows.append(case("count_transition", not tools.compare_document({"n": 1}, {"n": 3}, [good], "test")[1], True))
    negatives = [
        ("wrong_equal_count", {"n": 1}, {"n": 2}, dict(path="n", kind="COUNT", old=1, new=3)),
        ("addition_in_both", {"n": 2}, {"n": 2}, dict(path="n", kind="ADDITION")),
        ("unequal_equal", {"n": 2}, {"n": 3}, dict(path="n", kind="EQUAL")),
        ("deep_not_hidden", {"n": {}}, {"n": {"leaf": 3}}, dict(path="n", kind="MAY_DIFFER")),
        ("absent_in_both", {}, {}, dict(path="missing", kind="ADDITION")),
    ]
    for name, before, after, spec in negatives:
        spec = dict(spec, id=name, reason="source-authored negative")
        actual, failures = tools.compare_document(before, after, [spec], "test")
        deep = name == "deep_not_hidden"
        rows.extend([case(name, bool(failures), True), case(name + ".rows", len(actual), 2 if deep else 1),
                     case(name + ".failures", len(failures), 1)])
        expected = dict(path="test.n.leaf" if deep else "test." + spec["path"], classification="U_FINDING",
                        declaration_id="" if deep else name, kind="UNDECLARED" if deep else spec["kind"], held=False,
                        reason="undeclared differing leaf" if deep else "declared path absent from both documents"
                        if name == "absent_in_both" else spec["reason"])
        for field, value in expected.items():
            rows.append(case(name + ".failure." + field, failures[0].get(field) if len(failures) == 1 else "WRONG_FAILURE_COUNT", value))
        if deep:
            parent = [r for r in actual if r["path"] == "test.n"]
            rows.append(case(name + ".parent_count", len(parent), 1))
            for field, value in dict(classification="E", declaration_id=name, kind="MAY_DIFFER", held=True).items():
                rows.append(case(name + ".parent." + field, parent[0].get(field) if len(parent) == 1 else None, value))
    return summarize(rows)


def q6_cases(tools: Any) -> dict[str, Any]:
    source = 'def raise_site():\n    raise RuntimeError("first")\n'
    prefix = 'Traceback (most recent call last):\n  File "C:/a/demo.py", line 2, in raise_site\n'
    trace = prefix + "RuntimeError: first\n"
    other = trace.replace("C:/a/", "C:/b/")
    changed_source = source.replace('"first"', '"another_statement"')
    pairs = [
        ("path_normalized", trace, source, other, source, True, True, True),
        ("changed_raise_rejected", trace, source, trace, changed_source, False, True, False),
        ("path_in_exception_text", prefix + "RuntimeError: field=C:/a/demo.py\n", source,
         prefix.replace("C:/a/", "C:/b/") + "RuntimeError: field=C:/b/demo.py\n", source, True, True, True),
        ("field_before_path_preserved", prefix + "RuntimeError: field_a=C:/a/demo.py\n", source,
         prefix + "RuntimeError: field_b=C:/a/demo.py\n", source, True, False, False),
        ("multiline_type", prefix + "TypeError: first\nidentical final line\n", source,
         prefix + "RuntimeError: first\nidentical final line\n", source, True, False, False),
        ("multiline_nonfinal", prefix + "RuntimeError: first\nidentical final line\n", source,
         prefix + "RuntimeError: changed\nidentical final line\n", source, True, False, False),
        ("chained_cause_type", prefix + "TypeError: cause\n\nThe above exception was the direct cause of the following exception:\n\n" + prefix + "RuntimeError: first\n", source,
         prefix + "ValueError: cause\n\nThe above exception was the direct cause of the following exception:\n\n" + prefix + "RuntimeError: first\n", source, True, False, False),
    ]
    rows = []
    for name, ta, sa, tb, sb, frame_equal, exception_equal, signature_equal in pairs:
        a, b = tools.traceback_signature(ta, sa, "demo.py"), tools.traceback_signature(tb, sb, "demo.py")
        pa, pb = json.loads(a), json.loads(b)
        rows.extend([case(name + ".frames_equal", pa["frames"] == pb["frames"], frame_equal),
                     case(name + ".exception_equal", pa["exception"] == pb["exception"], exception_equal),
                     case(name + ".signature_equal", a == b, signature_equal)])
        if name == "path_normalized":
            rows.append(case(name, a == b, True))
        if name == "changed_raise_rejected":
            rows.append(case(name, a != b, True))
    return summarize(rows)


def rrs_cases(source: str, parent_source: str) -> dict[str, Any]:
    def segment(text: str) -> str:
        node = next(n for n in ast.parse(text).body if isinstance(n, ast.FunctionDef) and n.name == "run_real_scenario")
        result = ast.get_source_segment(text, node)
        assert result is not None
        return result

    actual, parent = segment(source), segment(parent_source)
    # A constructed copy adds one statement inside the function, keeping it parsable.
    index = actual.rfind("\n")
    constructed = actual[:index] + "\n    pass\n" + actual[index:]
    return summarize([case("parent_segment_equal", actual.encode("utf-8") == parent.encode("utf-8"), True),
                      case("constructed_statement_change_rejected", segment(constructed) != parent, True)])


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
    out["Q4"] = q4_cases(source, constant_ok_count)
    out["Q5"] = q5_cases(tools)
    out["Q6"] = q6_cases(tools)
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
