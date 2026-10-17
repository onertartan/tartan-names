"""Wait for recorded gates, check custody, then run and package one authorized attempt."""
from __future__ import annotations

import ast
import csv
import ctypes
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "p_konum_plus/calibration"
P = ROOT / "p_konum_plus/provenance"
LOG = P / "f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def side(path: Path) -> None:
    Path(str(path) + ".sha256").write_text(sha(path) + "  " + path.name + "\n", encoding="ascii")


def event(payload: dict[str, Any]) -> None:
    payload = dict(time_utc=dt.datetime.now(dt.timezone.utc).isoformat(), **payload)
    with LOG.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write("\n```json\n" + json.dumps(payload, indent=2, ensure_ascii=True) + "\n```\n")
    side(LOG)
    print(json.dumps(payload), flush=True)


def functions(source: str) -> dict[str, ast.FunctionDef]:
    return {n.name: n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)}


def declarations(source: str) -> dict[str, Any]:
    main = functions(source)["main"]
    node = next(n for n in main.body if isinstance(n, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == "EXPECTATIONS_E" for t in n.targets))
    return ast.literal_eval(node.value)


def scope_checks() -> dict[str, Any]:
    old = (C / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py").read_bytes().decode("utf-8")
    new = (C / "f3_step2_adequacy_harness_rp1-r3_2026-10-15.py").read_bytes().decode("utf-8")
    a, b = functions(old), functions(new)
    assert set(a) == set(b)
    for name in a:
        if name != "main":
            assert ast.dump(a[name]) == ast.dump(b[name]), "UNAUTHORIZED_HARNESS_FUNCTION_CHANGE " + name
    assert ast.get_source_segment(old, a["run_real_scenario"]) == ast.get_source_segment(new, b["run_real_scenario"])
    before, after = declarations(old), declarations(new)
    allowed = {"end_state.PI_dispatch_record_hash", "end_state.PI_dispatch_record_path"}
    added_counts = {}
    for ns in before:
        lookup = {x["id"]: x for x in after[ns]}
        assert len(lookup) == len(after[ns])
        for row in before[ns]:
            actual = lookup.pop(row["id"])
            if ns == "results" and row["path"] in allowed:
                assert {k: v for k, v in row.items() if k != "reason"} == {k: v for k, v in actual.items() if k != "reason"}
                assert "f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md" in actual["reason"]
            else:
                assert row == actual, "INHERITED_DECLARATION_CHANGED " + row["id"]
        expected = {"rp1_r3_scope_guard." + x for x in ("ran", "pass_", "cases[*].name", "cases[*].expected", "cases[*].got", "cases[*].ok")}
        expected |= {"tests_run.T-RP1R3-RRS-UNCHANGED." + x for x in ("ran", "passed")}
        if ns == "results": expected |= {"end_state.rp1_r3_status", "end_state.rp1_r3_open_findings"}
        assert {x["path"] for x in lookup.values()} == expected
        assert all(x["kind"] == "ADDITION" and x["reason"] for x in lookup.values())
        added_counts[ns] = len(lookup)
    for stem, allowed_changes, allowed_additions in (
        ("gate_tools", {"traceback_signature"}, set()),
        ("technical_tests", {"constant_ok_count", "technical_cases"}, {"q4_cases", "q5_cases", "q6_cases", "rrs_cases"})):
        left = functions((C / f"f3_rp1-r2_{stem}_2026-10-10.py").read_text(encoding="utf-8"))
        right = functions((C / f"f3_rp1-r3_{stem}_2026-10-15.py").read_text(encoding="utf-8"))
        assert set(right) - set(left) == allowed_additions and not set(left) - set(right)
        for name in left:
            if name not in allowed_changes: assert ast.dump(left[name]) == ast.dump(right[name]), stem + ":" + name
    for stem in ("launch_attempt", "write_custody"):
        source = (C / f"f3_rp1-r2_{stem}_2026-10-10.py").read_text(encoding="utf-8")
        expected_source = source.replace("rp1-r2", "rp1-r3").replace("2026-10-10", "2026-10-15").replace("F3_RP1R2_LAUNCH", "F3_RP1R3_LAUNCH")
        if stem == "write_custody":
            marker = '    metadata = dict(writer_sha256=sha(Path(__file__))'
            chain = ('    observed.update(supersedes_harness_sha256=constants["SUPERSEDES_HARNESS_SHA256"],\n'
                     '                    supersedes_custody_sha256=constants["SUPERSEDES_CUSTODY_SHA256"],\n'
                     '                    supersedes_note_path=constants["SUPERSEDES_NOTE_PATH"])\n')
            assert marker in expected_source
            expected_source = expected_source.replace(marker, chain + marker, 1)
        assert (C / f"f3_rp1-r3_{stem}_2026-10-15.py").read_text(encoding="utf-8") == expected_source
    return dict(unchanged_nonmain_harness_functions=len(a) - 1, immutable_consumer_segment_equal=True,
                inherited_declarations_preserved_except_two_authorized_reasons=True, new_addition_declarations=added_counts,
                launcher_writer_identity_and_authorized_supersession_only=True)


def alive(pid: int) -> bool:
    handle = ctypes.windll.kernel32.OpenProcess(0x100000, False, pid)
    if not handle:
        return False
    try:
        return ctypes.windll.kernel32.WaitForSingleObject(handle, 0) == 258
    finally:
        ctypes.windll.kernel32.CloseHandle(handle)


def main() -> None:
    config_path = Path(sys.argv[1]).resolve()
    assert sha(config_path) == sys.argv[2], "CONTROLLER_CONFIG_HASH_STOP"
    config = json.loads(config_path.read_bytes())
    for rel, pin in config["source_pins"].items():
        assert sha(ROOT / rel) == pin, "SOURCE_PIN_STOP " + rel
    event(dict(event="NATIVE_CONTROLLER_STARTED", controller_pid=os.getpid(), config_path=str(config_path),
               config_sha256=sha(config_path), state="WAITING_FOR_RECORDED_HISTORICAL_COMPARISON", commit=False))
    history = Path(config["historical_output_root"])
    metadata_path = history / "execution_record.json"
    while not metadata_path.exists():
        if not alive(config["historical_wrapper_pid"]):
            time.sleep(1)
            assert metadata_path.exists(), "HISTORICAL_EXECUTION_INTERRUPTED_WITHOUT_RESULT"
        time.sleep(10)
    metadata = json.loads(metadata_path.read_bytes())
    assert metadata["end"]["returncode"] == 0, "HISTORICAL_COMPARISON_STOP_SEE_EXTERNAL_LOGS"
    comparison_path = history / "comparison_result.json"
    comparison = json.loads(comparison_path.read_bytes())
    assert comparison["passed"] and not comparison["further_findings"], "NEW_EXCEPTION_TEXT_DIFFERENCE_STOP_NO_DECLARATION_CHANGE"
    assert metadata["start"]["code_sha256"] == config["source_pins"]["p_konum_plus/calibration/f3_rp1-r3_cached_historical_comparison_2026-10-15.py"]
    for path, pin in comparison["inputs"].items(): assert sha(Path(path)) == pin, "HISTORICAL_INPUT_CHANGED"
    synthetic_root = Path(config["synthetic_output_root"])
    synthetic = json.loads((synthetic_root / "synthetic_result.json").read_bytes())
    assert synthetic["passed"] and all(x["pass_"] for x in synthetic["tests"].values())
    assert all(not x["failures"] for x in synthetic["namespaces"].values())
    for path, pin in synthetic["inputs"].items(): assert sha(Path(path)) == pin, "SYNTHETIC_INPUT_CHANGED"
    scope = scope_checks()
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == config["parent_commit"]
    assert not subprocess.check_output(["git", "diff", "--name-only", "HEAD"], cwd=ROOT).strip(), "TRACKED_CHANGES_STOP"
    initial = json.loads((P / "f3_realdata_prep_rp1-r3_start_state_inventory_2026-10-15.json").read_bytes())
    for item in initial["preconditions"]["attachments"]: assert sha(Path(item["destination"])) == item["sha256"]
    transmission = P / "f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv"
    assert sha(transmission) == "e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75"
    with transmission.open(encoding="utf-8", newline="") as stream: previous = list(csv.DictReader(stream))
    for row in previous:
        assert sha(ROOT / row["path"]) == row["sha256"], "PARENT_PAYLOAD_CHANGED"
        assert sha(ROOT / row["sidecar"]) == row["sidecar_sha256"], "PARENT_SIDECAR_CHANGED"
    ledger = json.loads((P / "f3_realdata_prep_rp1-r3_ledger_2026-10-15.json").read_bytes())
    due = [x for x in ledger["items"] if x.get("due_in_rp1_r3")]
    assert due and all(x["status"] == "IMPLEMENTED_PENDING_VERIFICATION" and x["evidence"] for x in due)
    carried = next(x for x in ledger["items"] if x["id"] == "IR1-13")
    assert carried["status"] == "OPEN" and not carried["due_in_rp1_r3"]
    diff_record = json.loads((P / "f3_realdata_prep_rp1-r3_diff_custody_2026-10-15.json").read_bytes())
    for entry in diff_record["diffs"]:
        for field in ("diff", "labels", "target", "baseline"):
            if entry.get(field + "_sha256"): assert sha(Path(entry[field])) == entry[field + "_sha256"]
    store = C / ".rp1-r3_attempt1_restart_store_2026-10-15"
    assert not store.exists() or not any(store.iterdir()), "ATTEMPT1_STORE_NOT_EMPTY"
    for rel, pin in config["source_pins"].items():
        assert sha(ROOT / rel) == pin, "PRELAUNCH_SOURCE_PIN_STOP " + rel
    record = P / ("f3_realdata_prep_rp1-r3_" + config["historical_execution_id"] + "_execution_record.json")
    with record.open("xb") as stream: stream.write(metadata_path.read_bytes())
    side(record)
    checks = dict(event="ALL_NATIVE_PRELAUNCH_CHECKS_PASSED", scope_checks=scope,
        historical_execution_record_sha256=sha(record), historical_comparison_output_sha256=sha(comparison_path),
        historical_further_finding_count=len(comparison["further_findings"]),
        synthetic_result_output_sha256=sha(synthetic_root / "synthetic_result.json"),
        parent_payloads_reverified=len(previous), due_implemented_items=len(due), store_before_launch="EMPTY_OR_ABSENT",
        real_data_access=False, authority="Signed D-19 plus exact D-14 authorization checked by the unchanged launcher/writer rule", commit=False)
    check_path = P / "f3_realdata_prep_rp1-r3_prelaunch_checks_2026-10-15.json"
    with check_path.open("x", encoding="ascii", newline="\n") as stream: stream.write(json.dumps(checks, indent=2) + "\n")
    side(check_path)
    event(checks)
    environment = dict(os.environ, F3_REPO_ROOT=str(ROOT), F3_RP1R3_LAUNCH="1", PYTHONDONTWRITEBYTECODE="1",
                       PYTHONUNBUFFERED="1", OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    with (Path(config["controller_log_root"]) / "attempt_launcher_stdout.log").open("xb") as stdout, (Path(config["controller_log_root"]) / "attempt_launcher_stderr.log").open("xb") as stderr:
        outcome = subprocess.run([sys.executable, "-B", str(C / "f3_rp1-r3_launch_attempt_2026-10-15.py")], cwd=ROOT, env=environment, stdout=stdout, stderr=stderr)
    assert outcome.returncode == 0, "ATTEMPT1_FAILED_NO_AUTOMATIC_CORRECTION"
    event(dict(event="ATTEMPT1_COMPLETED_STARTING_NATIVE_DELIVERY_FINALIZATION", returncode=outcome.returncode, commit=False))
    finalized = subprocess.run([sys.executable, "-B", str(C / "f3_rp1-r3_finalize_delivery_2026-10-15.py")], cwd=ROOT, env=environment)
    assert finalized.returncode == 0, "DELIVERY_FINALIZATION_STOP"


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        payload = dict(event="CONTROLLER_STOP", reason=str(error), exception_type=type(error).__name__,
                       full_run_authorized_only_after_all_gates=True, no_automatic_code_or_declaration_changes=True,
                       real_data_access=False, commit=False)
        event(payload)
        path = P / "f3_realdata_prep_rp1-r3_STOP_record_2026-10-15.json"
        with path.open("x", encoding="ascii", newline="\n") as stream: stream.write(json.dumps(payload, indent=2) + "\n")
        side(path)
        raise
