"""Transfer completed executor results into records; never execute scientific code."""
from __future__ import annotations

import ast
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "p_konum_plus/calibration"
P = ROOT / "p_konum_plus/provenance"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def side(path: Path) -> None:
    Path(str(path) + ".sha256").write_text(sha(path) + "  " + path.name + "\n", encoding="ascii")


def main() -> None:
    result_path = C / "f3_step2_results_rp1-r3_2026-10-15.json"
    result = json.loads(result_path.read_bytes())
    end_path = P / "f3_step2_rp1-r3_attempt1_launch1_end_2026-10-15.json"
    end = json.loads(end_path.read_bytes())
    assert end["return_code"] == 0, "REFUSE_INCOMPLETE_ATTEMPT"
    initial = json.loads((P / "f3_realdata_prep_rp1-r3_start_state_inventory_2026-10-15.json").read_bytes())
    incoming = {Path(x["destination"]).resolve(): x["sha256"] for x in initial["preconditions"]["attachments"]}
    for path, pin in incoming.items():
        assert sha(path) == pin, "INCOMING_BYTES_CHANGED " + str(path)
    assert not subprocess.check_output(["git", "diff", "--name-only", "HEAD"], cwd=ROOT).strip(), "TRACKED_CHANGE_STOP"
    nonreg_path = C / "f3_step2_rp1-r3_nonregression_vs_r4-2_2026-10-15.csv"
    with nonreg_path.open(encoding="utf-8", newline="") as stream:
        nonreg = list(csv.DictReader(stream))
    ledger_path = P / "f3_realdata_prep_rp1-r3_ledger_2026-10-15.json"
    ledger = json.loads(ledger_path.read_bytes())
    for row in ledger["items"]:
        if row.get("due_in_rp1_r3"):
            row["executor_results_evidence"] = dict(path=str(result_path.relative_to(ROOT)), sha256=sha(result_path))
            row["execution_scope_note"] = "Executor results delivered; status remains IMPLEMENTED_PENDING_VERIFICATION. Only the independent auditor closes this item."
    ledger["executor_run_status"] = "COMPLETED"
    ledger["status"] = result["end_state"]["rp1_r3_status"]
    ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=True) + "\n", encoding="ascii")
    side(ledger_path)
    tests = result["rp1_r2_technical_tests"]
    scope = result["rp1_r3_scope_guard"]
    requirements = []
    mapping = [("R3-1", "Q6", "q6_cases", "path_normalized", "multiline_type/multiline_nonfinal/chained_cause_type/changed_raise_rejected"),
               ("R3-2", "Q4", "constant_ok_count/q4_cases", "no_constant_ok", "keyword/dictionary/subscript/name/attribute counts"),
               ("R3-3", "Q5", "q5_cases", "count_transition", "wrong_equal_count/addition_in_both/unequal_equal/deep_not_hidden/absent_in_both"),
               ("R3-5", "RRS", "rrs_cases", "parent_segment_equal", "constructed_statement_change_rejected")]
    for requirement, block, function, positive, negative in mapping:
        observed = scope if block == "RRS" else tests[block]
        requirements.append(dict(requirement=requirement, code="f3_rp1-r3_technical_tests_2026-10-15.py:" + function,
            positive=positive, negative=negative, verification="Copied by script from executor results test block",
            result_source=str(result_path.relative_to(ROOT)) + ":" + ("rp1_r3_scope_guard" if block == "RRS" else "rp1_r2_technical_tests." + block),
            ran=observed["ran"], passed=observed["pass_"], evidence_sha256=sha(result_path)))
    by_id = {x["id"]: x for x in ledger["items"]}
    for requirement, finding in (("R3-4", "IR2-06"), ("IR1-16", "IR1-16"), ("IR2-04", "IR2-04"),
                                  ("IR2-05", "IR2-05"), ("IR2-07", "IR2-07")):
        row = by_id[finding]
        requirements.append(dict(requirement=requirement, code="", positive="", negative="",
            verification="Named record evidence and sidecar; implementation pending independent verification",
            result_source=json.dumps(row["evidence"], ensure_ascii=True), ran="", passed="",
            evidence_sha256=sha(ledger_path)))
    for requirement, execution in (("5(a1)", "2026-10-15_historical_execution04"),
                                    ("5(a2)", "2026-10-15_synthetic_execution04")):
        metadata_path = P / f"f3_realdata_prep_rp1-r3_{execution}_execution_record.json"
        metadata = json.loads(metadata_path.read_bytes())
        assert metadata["end"]["returncode"] == 0
        requirements.append(dict(requirement=requirement, code=metadata["start"]["code_path"],
            positive="", negative="", verification="Recorded standalone execution; outputs excluded from deliverables and stores",
            result_source=str(metadata_path.relative_to(ROOT)), ran="", passed="", evidence_sha256=sha(metadata_path)))
    requirements.append(dict(requirement="5(b)", code="f3_rp1-r3_logged_preflight_2026-10-15.py / f3_rp1-r3_launch_attempt_2026-10-15.py",
        positive="", negative="", verification="Attempt log plus immutable native execution and W-3 launch records",
        result_source=str(end_path.relative_to(ROOT)), ran="", passed="", evidence_sha256=sha(end_path)))
    requirement_path = P / "f3_realdata_prep_rp1-r3_requirement_map_2026-10-15.csv"
    with requirement_path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(requirements[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(requirements)
    side(requirement_path)
    observed = dict(rp1_r3_status=result["end_state"]["rp1_r3_status"],
        result_path=str(result_path.relative_to(ROOT)), result_sha256=sha(result_path),
        executor_start_utc=end["start_utc"], executor_end_utc=end["end_utc"],
        executor_seconds=(dt.datetime.fromisoformat(end["end_utc"]) - dt.datetime.fromisoformat(end["start_utc"])).total_seconds(),
        scientific_objects=len(result["evaluations"]), run1_canonical_sha256=result["run1_canonical_sha256"],
        run2_canonical_sha256=result["run2_canonical_sha256"], determinism=result["determinism"],
        mandatory_tests_all_run=result["end_state"]["mandatory_tests_all_run"],
        corrections_complete=result["end_state"]["corrections_complete"],
        recorded_tests=len(result["tests_run"]), nonregression_rows=len(nonreg),
        s_findings=sum(r["classification"] == "S_FINDING" for r in nonreg),
        u_findings=sum(r["classification"] == "U_FINDING" for r in nonreg),
        declared_expectations_held=all(r["held"] == "True" for r in nonreg if r.get("declaration_id")),
        nonregression_path=str(nonreg_path.relative_to(ROOT)), nonregression_sha256=sha(nonreg_path),
        test_case_counts={k: len(v["cases"]) for k, v in dict(tests, RRS=scope).items()},
        ledger_items=len(ledger["items"]), real_data_access=result["real_data_access"], commit=False, independent_audit_performed=False)
    observation_path = P / "f3_realdata_prep_rp1-r3_executor_observations_2026-10-15.json"
    observation_path.write_text(json.dumps(observed, indent=2, ensure_ascii=True) + "\n", encoding="ascii")
    side(observation_path)
    report = P / "f3_realdata_prep_rp1-r3_executor_report_2026-10-15.md"
    text = "# rp1-r3 executor report\n\nrp1-r3_status = " + observed["rp1_r3_status"] + "\n\n"
    text += "All numbers, hashes and result statuses below are transferred by script from delivered files or native command results. This report does not perform an independent audit or close a finding.\n\n```json\n"
    text += json.dumps(observed, indent=2, ensure_ascii=True) + "\n```\n\n"
    text += "IR1-13 remains OPEN / B under signed D-14 RECORDED_LIMITATION and is not due in this package. D-19 dispatches this cycle; D-18 PI-2 disposes IR2-03 subject to the next auditor's scope verification. The ledger attributes prior closures to the named audit. The next audit must independently verify the implementation and rerun.\n\n"
    text += "The outside-W3 execution metadata is delivered as records; its test outputs remain outside every delivery/store. IR2-07 historical evidence is separately named and hash-checked; no missing record was reconstructed or admitted to an attempt store. Prior packages and pre-existing untracked files were preserved. No commit or push was performed.\n"
    report.write_text(text, encoding="utf-8", newline="\n")
    side(report)
    log = P / "f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md"
    with log.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write("\n```json\n" + json.dumps(dict(event="EXECUTOR_DELIVERY_RECORDS_WRITTEN", result_sha256=sha(result_path), report_sha256=sha(report), observations_sha256=sha(observation_path), status=observed["rp1_r3_status"], commit=False), indent=2) + "\n```\n")
    side(log)
    preexisting = {x["path"] for x in initial["preexisting_untracked"]}
    fixture_root = C / "f3_step2_rp1-r3_f1_synth_fixtures_2026-10-15"
    runtime_table = P / "f3_realdata_prep_rp1-r3_runtime_fixture_custody_attempt1_launch1_2026-10-15.csv"
    with runtime_table.open(encoding="ascii", newline="") as stream:
        runtime_rows = list(csv.DictReader(stream))
    actual_fixture_paths = {x.relative_to(ROOT).as_posix() for x in fixture_root.rglob("*") if x.is_file()}
    assert {x["path"] for x in runtime_rows} == actual_fixture_paths, "FIXTURE_CUSTODY_PATH_SET_STOP"
    for row in runtime_rows:
        assert sha(ROOT / row["path"]) == row["sha256"], "FIXTURE_CUSTODY_BYTES_STOP"
    overwrite_path = P / "f3_realdata_prep_rp1-r3_rerun_overwrite_inventory_r1_2026-10-15.json"
    overwrite = json.loads(overwrite_path.read_bytes())
    overwrite["observed_fixture_files"] = runtime_rows
    overwrite["runtime_fixture_custody_path"] = runtime_table.relative_to(ROOT).as_posix()
    overwrite["runtime_fixture_custody_sha256"] = sha(runtime_table)
    overwrite["observed_fixture_file_count"] = len(runtime_rows)
    overwrite_path.write_text(json.dumps(overwrite, indent=2, ensure_ascii=True) + "\n", encoding="ascii")
    side(overwrite_path)
    fixture_checksums = {}
    for check in fixture_root.rglob("*.sha256"):
        tokens = check.read_text(encoding="ascii").split()
        if len(tokens) == 2:
            fixture_checksums.setdefault((tokens[0], tokens[1]), check)
    raw = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=ROOT)
    payloads = []
    for rel in (x.decode("utf-8") for x in raw.split(b"\0") if x):
        path = ROOT / rel
        fixture_file = fixture_root in path.parents
        if rel in preexisting or not rel.startswith("p_konum_plus/") or path.suffix in (".pkl", ".zip", ".pyc"):
            continue
        if path.suffix == ".sha256" and not fixture_file:
            continue
        if "__pycache__" in path.parts or any(part.startswith(".rp1-r3") for part in path.parts):
            continue
        if "rp1-r3" not in rel.lower() and path.resolve() not in incoming:
            if "rp1-r2_harness_diff" not in rel or "labels_r1_2026-10-15" not in rel:
                continue
        payloads.append(path)
    transmission = P / "f3_realdata_prep_rp1-r3_transmission_list_2026-10-15.csv"
    payloads = [x for x in payloads if x != transmission]
    rows = []
    for path in sorted(payloads):
        check = Path(str(path) + ".sha256")
        if fixture_root in path.parents:
            check = fixture_checksums.get((sha(path), path.name))
            if check is None:
                # Raw input directories must never acquire checksum files.
                check = P / "f3_realdata_prep_rp1-r3_delivery_checksums_2026-10-15" / (path.relative_to(ROOT).as_posix() + ".sha256")
                check.parent.mkdir(parents=True, exist_ok=True)
                check.write_text(sha(path) + "  " + path.name + "\n", encoding="ascii")
            assert check.read_text(encoding="ascii").split()[0] == sha(path)
        elif path.resolve() in incoming:
            assert sha(path) == incoming[path.resolve()]
            assert check.read_text(encoding="ascii").split()[0] == sha(path)
        else:
            side(path)
        rows.append(dict(path=path.relative_to(ROOT).as_posix(), sha256=sha(path),
                         sidecar_path=check.relative_to(ROOT).as_posix(), sidecar_sha256=sha(check)))
    with transmission.open("x", encoding="ascii", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["path", "sha256", "sidecar_path", "sidecar_sha256"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    side(transmission)
    print(json.dumps(dict(status=observed["rp1_r3_status"], transmission_path=str(transmission), transmission_sha256=sha(transmission), payload_count=len(rows), commit=False)))


if __name__ == "__main__":
    main()
