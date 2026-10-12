"""Generate prelaunch review records from bytes, AST and Git; never run tests."""
from __future__ import annotations

import ast
import collections
import csv
import datetime as dt
import difflib
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
from typing import Any
import zipfile

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "p_konum_plus/calibration"
P = ROOT / "p_konum_plus/provenance"
DATE = "2026-10-10"
PREFIX = "f3_realdata_prep_rp1-r2_"
HARNESS = C / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
PARENT = C / "f3_step2_adequacy_harness_rp1-r1_2026-10-05.py"
R42 = C / "f3_step2_adequacy_harness_r4-2_2026-09-30.py"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, value: str | bytes) -> None:
    path.write_bytes(value.encode("utf8") if isinstance(value, str) else value)


def seal(path: Path) -> None:
    checksum = Path(str(path) + ".sha256")
    content = sha(path) + "  " + path.name + "\n"
    if checksum.exists():
        assert checksum.read_text(encoding="ascii") == content, "EXISTING_SIDECAR_MISMATCH " + str(path)
    else:
        checksum.write_text(content, encoding="ascii", newline="\n")


def json_record(stem: str, value: Any) -> Path:
    path = P / (PREFIX + stem + "_" + DATE + ".json")
    write(path, json.dumps(value, indent=2, ensure_ascii=True) + "\n")
    return path


def csv_record(stem: str, fields: list[str], rows: list[dict[str, Any]]) -> Path:
    path = P / (PREFIX + stem + "_" + DATE + ".csv")
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    write(path, buffer.getvalue())
    return path


FUNCTION_PURPOSES = {
    "authorize_rp2_launch": ("S5A", "External PI decision gate; executor cannot authorize IR1-13."),
    "real_mask_id": ("Q2", "The sole real-mode mask identity constructor."),
    "store_read_aggregate": ("Q7", "Aggregate the actual replay checks without a cold-zero condition."),
    "handoff_phase_valid": ("Q9", "Validate the handoff phase."),
    "handoff_accounting": ("Q10", "Reconcile actual optimizer events to handoff start/mode unit payloads."),
    "write_rp2_handoff_outputs": ("Q10", "Export family events, measured timing and scoped estimate."),
    "load_rp2_dependency": ("Q11", "Hash-bound dependency custody and fingerprint wiring."),
    "ckpt_load": ("Q8", "Every cache hit restores telemetry with replay provenance."),
    "_key_family": ("Q9", "Identify the underlying key family after stripping scope prefixes."),
    "f1_repro_gate": ("Q3", "PI-b form B manifest/raw-list custody and field re-derivation."),
    "t_f1_repro_gate_synth": ("Q3", "Eight synthetic reproduction gate cases."),
    "t_f1_loader_synth": ("Q4", "Compute each loader case result from got and expected."),
    "t_store_read_accounting": ("Q7", "Permit replayed cold units while checking exact stored payloads."),
    "t_f1_handoff_synth": ("Q10", "Retain returned family events and section timings for handoff accounting."),
    "_provenance_stripped_content_equal": ("Q6", "Replace whole-trace removal by semantic source-coordinate normalization."),
    "_flatten_leaves": ("Q5", "Replace subtree stopping by complete leaf recursion."),
    "_classify_e_typed": ("Q5", "Evaluate exact leaf declarations."),
    "_expectation_held": ("Q5", "Evaluate declared predicates even for equal values."),
    "_diff_full": ("Q5", "Compare full-depth documents and absent declarations."),
    "_tel_row_key": ("Q5", "Preserve per-row telemetry multiplicity instead of key collapsing."),
}
INHERITED_PURPOSES = {
    "_audit_hook": ("C3", "Carried actual file-open audit and synthetic-only data access barrier."),
    "ckpt_provenance": ("C2", "Carried restart unit provenance lookup."),
    "_classify_covered_from_traceback": ("C1", "Carried exact covered call-site traceback identification."),
    "f1_verify_raw_files": ("C3", "Carried F1 raw hash-table verification; exercised on synthetic inputs only."),
    "f1_load_raw_dir": ("C3", "Carried raw loader and full-support eligibility."),
    "_f1_share": ("C3", "Carried OD3 share division gate."),
    "f1_post_z_qc": ("C3", "Carried post-normalization QC gate."),
    "f1_repro_gate": ("R1", "Carried reproduction gate replaced by Q3 form B."),
    "t_f1_repro_gate_synth": ("R1", "Carried reproduction synthetic gate cases replaced by Q3."),
    "fit_family": ("C5", "Carried rp1 C-5 report-only completed-start accounting; arithmetic preserved."),
    "fit_spline": ("R5", "Carried rp1-r1 R-5 per-call replay and C-5 inadmissible-mode accounting."),
    "run_real_scenario": ("R1", "Carried R-1 real-array consumption/family-qualified ids and R-2 test checks."),
    "f1_read_raw": ("C3", "Carried synthetic-only F1 raw-format loader."),
    "f1_full_eligible": ("C3", "Carried frozen full-support eligibility loader."),
    "f1_normalize": ("C3", "Carried F1 normalization gate."),
    "f1_qc": ("C3", "Carried F1 QC gate."),
    "f1_build_scenarios": ("R1", "Carried real-mode scenario contract and mask maps."),
    "f1_context_id_table": ("R1", "Carried dry context-id table."),
    "t_f1_loader_synth": ("R2", "Carried synthetic loader positive/negative checks."),
    "t_f1_handoff_synth": ("R1", "Carried loader-to-consumer handoff test."),
    "t_f1_contract_gap": ("R1", "Carried required scenario-field exception test."),
    "t_context_id_unique": ("R1", "Carried consumer-captured context identity checks."),
    "t_inadmissible_observable": ("C5", "Carried report-only inadmissible-unit test."),
    "t_store_read_accounting": ("R5", "Carried stored-vs-replayed optimizer payload checks."),
    "install_spline_call_telemetry": ("R5", "Carried optimizer per-call fresh/replay provenance."),
    "ckpt_load": ("C2", "Carried restart read accounting; no scientific payload changes."),
    "ckpt_save": ("C2", "Carried own-scope restart writes and unit custody."),
    "_key_family": ("C2", "Carried key-family accounting."),
    "_full_key": ("C2", "Carried code/environment fingerprinted unit key."),
    "_restart_store_init": ("C2", "Carried own empty-at-start restart store initialization."),
    "_ckpt_safe_name": ("C2", "Carried safe restart unit filename conversion."),
    "_traceback_nnls_call_is_solver_a": ("C1", "Carried exact solver-A call-site coverage predicate."),
    "install_exc_capture": ("C1", "Carried covered/unrelated exception routing wrapper."),
}


_FUNCTION_MAPS: dict[ast.Module, dict[int, str]] = {}


def function_at(tree: ast.Module, line: int) -> str:
    if tree not in _FUNCTION_MAPS:
        mapping = {}
        functions = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        for node in sorted(functions, key=lambda n: n.end_lineno - n.lineno, reverse=True):
            for coordinate in range(node.lineno, node.end_lineno + 1):
                mapping[coordinate] = node.name
        _FUNCTION_MAPS[tree] = mapping
    return _FUNCTION_MAPS[tree].get(line, "<module>")


def labels(source: str, tree: ast.Module, *, inherited: bool = False) -> dict[int, tuple[str, str]]:
    lines = source.splitlines()
    output = {}
    functions = INHERITED_PURPOSES if inherited else FUNCTION_PURPOSES
    for line in range(1, len(lines) + 1):
        fn = function_at(tree, line)
        output[line] = functions.get(fn, ("S8", "Authorized output/dispatch/test/custody wiring; existing scientific bodies unchanged."))
    if inherited:
        # Main contains added tests and outputs; nearest callable statement names
        # provide structural context, rather than searching textual keywords.
        for node in ast.walk(tree):
            if not isinstance(node, ast.stmt) or isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                continue
            calls = [n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
            if node.end_lineno - node.lineno > 12:
                continue
            purpose = next((INHERITED_PURPOSES[name] for name in calls if name in INHERITED_PURPOSES), None)
            if purpose and function_at(tree, node.lineno) in ("main", "one_run"):
                for line in range(node.lineno, node.end_lineno + 1):
                    output[line] = purpose
        return output
    # Exact authored edits have their purpose explicitly supplied at author time.
    edits = json.loads((P / (PREFIX + "authored_edits_" + DATE + ".json")).read_text(encoding="utf8"))
    for edit in sorted(edits, key=lambda item: len(item["new"]), reverse=True):
        body = edit["new"]
        if len(body) < 25:
            continue
        position = source.find(body)
        if position < 0:
            continue
        first = source.count("\n", 0, position) + 1
        last = first + body.count("\n")
        requirement = edit["requirement"]
        if requirement.startswith("Q"):
            for line in range(first, min(last + 1, len(lines) + 1)):
                output[line] = (requirement, "Exact authored edit for " + requirement + "; see authored-edits record.")
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if "EXPECTATIONS_E" in names:
                for line in range(node.lineno, node.end_lineno + 1):
                    output[line] = ("Q5", "Prelaunch exact leaf declarations, each with a reason; no observed run used to tune them.")
            elif set(names) & {"RP2_DEPENDENCY_PINS", "RP2_DISPATCH_PINS", "CUSTODY_PATH"}:
                for line in range(node.lineno, node.end_lineno + 1):
                    output[line] = ("Q11", "Current launch/dependency/dispatch identity is hash-bound before computation.")
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == "HANDOFF_TRAJECTORY_TIMINGS":
            output[node.lineno] = ("Q10", "Collect measured trajectory section timings for handoff export.")
    # Multi-purpose consumer edits are annotated by the actual named AST nodes.
    consumer = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "run_real_scenario")
    for node in ast.walk(consumer):
        if isinstance(node, ast.Assign):
            targets = {t.id for t in node.targets if isinstance(t, ast.Name)}
            purpose = ("Q1", "Check all real intake fields/maps before any fitting.") if "is_real" in targets else ("Q10", "Measure each trajectory's section boundaries.") if targets & {"_trajectory_start", "_trajectory_start_iso", "_trajectory_end"} else None
        elif isinstance(node, ast.FunctionDef) and node.name == "mid":
            purpose = ("Q2", "Consumer calls the shared real-mode mask identity builder.")
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute) and isinstance(node.value.func.value, ast.Name) and node.value.func.value.id == "HANDOFF_TRAJECTORY_TIMINGS":
            purpose = ("Q10", "Record measured trajectory section timing.")
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute) and isinstance(node.value.func.value, ast.Name) and node.value.func.value.id == "RP2_TOOLS" and node.value.func.attr == "check_intake":
            purpose = ("Q1", "Check every required real key/map entry before a fit.")
        elif isinstance(node, ast.For) and isinstance(node.iter, ast.Name) and node.iter.id == "RUN_REAL_SCENARIO_REQUIRED_KEYS":
            purpose = ("Q1", "Replace the four-field-only guard by the complete real-mode intake guard.")
        else:
            purpose = None
        if purpose:
            for line in range(node.lineno, node.end_lineno + 1):
                output[line] = purpose
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "fit_family")
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and any(k.arg == "unit_key" for k in node.keywords):
            for line in range(node.lineno, node.end_lineno + 1):
                output[line] = ("Q10", "Attach unit/phase/source identity to the actual optimizer event.")
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "f1_context_id_table")
    for line in range(fn.lineno, fn.end_lineno + 1):
        output[line] = ("Q2", "Dry table calls the same identity builder as the consumer.")
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "fit_spline")
    for node in ast.walk(fn):
        if isinstance(node, ast.keyword) and node.arg == "source":
            output[node.lineno] = ("Q8", "Mode-summary telemetry distinguishes fresh work from a restored mode.")
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "t_f1_handoff_synth")
    for node in ast.walk(fn):
        if not isinstance(node, ast.Assign):
            continue
        targets = [target for target in node.targets if isinstance(target, ast.Name) and target.id == "saved_phase"]
        phase_target = any(isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name) and target.value.id == "CURRENT_PHASE" for target in node.targets)
        if targets or phase_target:
            for line in range(node.lineno, node.end_lineno + 1):
                output[line] = ("Q9", "Attribute optimizer calls to f1_handoff and restore the caller's phase afterward.")
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == "RP2_TOOLS" and node.func.attr in ("normalize_traces", "compare_document"):
            purpose = ("Q6", "Preserve semantic traceback frame/function/statement/exception identity.") if node.func.attr == "normalize_traces" else ("Q5", "Compare all declared/differing leaves and evaluate missing declarations.")
            for line in range(node.lineno, node.end_lineno + 1):
                output[line] = purpose
    return output


def make_diff(baseline: Path, name: str, new_source: str, own_lines: set[int]) -> dict[str, Any]:
    old_source = baseline.read_text(encoding="utf8")
    old_lines, new_lines = old_source.splitlines(keepends=True), new_source.splitlines(keepends=True)
    old_labels = labels(old_source, ast.parse(old_source), inherited=(baseline == R42))
    new_labels = labels(new_source, ast.parse(new_source))
    inherited_labels = labels(new_source, ast.parse(new_source), inherited=True)
    if baseline == R42:
        new_labels = {line: new_labels[line] if line in own_lines else inherited_labels[line] for line in new_labels}
    diff = list(difflib.unified_diff(old_lines, new_lines, fromfile=baseline.name, tofile=HARNESS.name, n=0))
    records = []
    hunk = 0
    before_line = after_line = 0
    for row in diff:
        if row.startswith("@@"):
            hunk += 1
            match = re.match(r"@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@", row)
            before_line, after_line = int(match[1]), int(match[2])
        elif row.startswith("---") or row.startswith("+++"):
            continue
        elif row.startswith("-"):
            label, reason = old_labels[before_line]
            records.append(dict(hunk=hunk, side="old", first=before_line, last=before_line, label=label, reason=reason))
            before_line += 1
        elif row.startswith("+"):
            label, reason = new_labels[after_line]
            records.append(dict(hunk=hunk, side="new", first=after_line, last=after_line, label=label, reason=reason))
            after_line += 1
    compact = []
    for row in records:
        if compact and all(compact[-1][k] == row[k] for k in ("hunk", "side", "label", "reason")) and compact[-1]["last"] + 1 == row["first"]:
            compact[-1]["last"] = row["last"]
        else:
            compact.append(row)
    diff_path = P / (PREFIX + "harness_diff_vs_" + name + "_" + DATE + ".diff")
    write(diff_path, "".join(diff))
    label_path = csv_record("harness_diff_vs_" + name + "_labels", ["hunk", "side", "first", "last", "label", "reason"], compact)
    return dict(baseline=baseline.as_posix(), baseline_sha256=sha(baseline), diff=diff_path.as_posix(),
                labels=label_path.as_posix(), hunk_count=hunk, covered_changed_lines=len(records),
                method="Context 0; each old/new changed-line range has exactly one authored semantic-purpose label. Mixed hunks use separate range rows.")


def line_of(path: Path, function: str) -> str:
    tree = ast.parse(path.read_text(encoding="utf8"))
    node = next(n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == function)
    return path.relative_to(ROOT).as_posix() + ":" + str(node.lineno)


def main() -> None:
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    assert not (P / (PREFIX + "prelaunch_report_" + DATE + ".md")).exists(), "REFUSE_REPEATED_SEALED_REPORT"
    source = HARNESS.read_text(encoding="utf8")
    tree = ast.parse(source)
    deps = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "RP2_DEPENDENCY_PINS" for t in n.targets))
    pins = {name: sha(C / name) for name in ast.literal_eval(deps.value)}
    lines = source.splitlines(keepends=True)
    lines[deps.lineno - 1:deps.end_lineno] = ["RP2_DEPENDENCY_PINS = " + repr(pins) + "\n"]
    source = "".join(lines)
    write(HARNESS, source)
    tree = ast.parse(source)
    code_files = sorted(path for path in C.glob("*rp1-r2*2026-10-10.py"))
    observations = []
    for path in code_files:
        text = path.read_text(encoding="utf8")
        parsed = ast.parse(text, filename=str(path))
        compile(parsed, str(path), "exec")
        observations.append(dict(path=path.relative_to(ROOT).as_posix(), sha256=sha(path), syntax="PARSED_AND_COMPILED_WITHOUT_EXECUTION"))
    old_tree = ast.parse(PARENT.read_text(encoding="utf8"))
    old_functions = {n.name: ast.dump(n, include_attributes=False) for n in old_tree.body if isinstance(n, ast.FunctionDef)}
    new_functions = {n.name: ast.dump(n, include_attributes=False) for n in tree.body if isinstance(n, ast.FunctionDef)}
    unchanged = sorted(name for name in old_functions if old_functions[name] == new_functions.get(name))
    changed = sorted(name for name in old_functions if old_functions[name] != new_functions.get(name))
    inventory_path = P / (PREFIX + "start_state_inventory_" + DATE + ".md")
    inventory = json.loads(inventory_path.read_text(encoding="utf8").split("```json\n", 1)[1].split("```", 1)[0])
    items = inventory["ledger"]
    code_ids = {"IR1-02": "Q1", "IR1-03": "Q2", "IR1-05": "Q4", "IR1-06": "Q5", "IR1-07": "Q5", "IR1-08": "Q6",
                "IR1-09": "Q7", "IR1-10": "Q8", "IR1-11": "Q9", "IR1-12": "Q10", "IR1-18": "Q11"}
    record_ids = {"IR1-14", "IR1-15", "IR1-16", "IR1-17", "IR1-19"}
    for item in items:
        item["historical_evidence"] = item["evidence"]
        if item["status"].startswith("CLOSED"):
            item["closure_attribution"] = "Prior supplied auditor only; no current executor closure."
            continue
        if item["id"] in code_ids or item["id"] in record_ids:
            item["status"] = "IMPLEMENTED_PENDING_VERIFICATION"
            item["closure_point"] = "rp1-r2 audit"
            item["evidence"] = "Source/record preparation in this package; requirement map " + code_ids.get(item["id"], item["id"]) + "; runtime/independent verification NOT OBSERVED."
        else:
            item["status"] = "OPEN"
        if item["id"] == "IR1-04":
            item["evidence"] = "Q3 source/generator authored; synthetic fixture bytes and runtime checks NOT OBSERVED pending IR1-13."
        if item["id"] == "IR1-13":
            item["evidence"] = "S5A STOP record; original execution hash/output segregation and PI decision NOT OBSERVED."
    ledger_path = json_record("ledger", dict(status="PARTIAL_PENDING_PI", items=items, current_executor_closures=[],
        real_data_access=False, current_runtime="NOT OBSERVED", source_inventory_sha256=sha(inventory_path)))
    log_path = P / (PREFIX + "attempt_log_" + DATE + ".md")
    log = log_path.read_text(encoding="utf8")
    disclosure = "rp1-r2 talimatı önce yanlışlıkla rp1-r1 denetçi oturumuna verildi; o oturum rp1r1_audit\\repo içinde bir taslak yazdı; bu taslak rp1-r2'de kullanılmadı."
    assert disclosure in log, "REQUIRED_DISCLOSURE_MISSING"
    log += "\n## Prelaunch source preparation\n\nOnly record-generation and source-editing scripts ran. No harness, harness copy, test-section excerpt, optimizer, or W-3 writer ran. The declaration-authoring process was stopped when its repeated schema flattening was slow; its authoring script was corrected to cache those schemas and rerun. This was an authoring-process interruption, not a scientific attempt. The source-finalization script and this record generator parse/compile source without importing or executing it. Historical execution details are not reconstructed.\n"
    log += "\nRuntime launch timestamps, runtime PIDs, tests and optimizer measurements: NOT OBSERVED. The initialization timestamp and source hashes below refer to preparation only.\n"
    log += "\n```json\n" + json.dumps(dict(record_preparation_started_utc=started, initial_inventory_created_utc=inventory["created_utc"],
        record_generator_sha256=sha(Path(__file__)), record_generator_directory=str(ROOT), harness_sha256=sha(HARNESS),
        launch_authorized=False, harness_invocations=0, test_excerpt_invocations=0, real_data_access=False), indent=2) + "\n```\n"
    write(log_path, log)
    historical_log = P / "f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md"
    evidence_lines = historical_log.read_text(encoding="utf8").splitlines()
    quote = "\n".join(evidence_lines[84:87])
    stop = P / (PREFIX + "ir1-13_stop_record_" + DATE + ".md")
    write(stop, "# IR1-13 prelaunch STOP record\n\nStatus: OPEN / B. Launch: PROHIBITED_PENDING_PI_DECISION.\n\n"
        + "The historical attempt log supplies a narrative assertion at line 85; reading that assertion does not verify the execution. This preparation cannot supply its original code hash, working directory, launch/custody record, exact observed start/end, output paths, output hashes, or evidence excluding its outputs from deliverables/attempt-2 store. Each remains X / NOT OBSERVED. No value is inferred from a later harness hash, file timestamps or approximate durations.\n\n"
        + "Historical source: `" + historical_log.relative_to(ROOT).as_posix() + ":85`, SHA256 `" + sha(historical_log) + "`. Exact source excerpt:\n\n```text\n" + quote + "\n```\n\n"
        + "PI decision naming and disposing of IR1-13 under D-11 r1 sections 5-6, including its reason: NOT OBSERVED. D-13's confirmation of class B is not such a disposition. The authorization control remains false. An authorization alone does not supply missing evidence or make the package PREPARED. This executor claims no closure.\n")
    fixture_root = C / "f3_step2_rp1_f1_synth_fixtures_2026-10-05"
    fixture_rows = [dict(path=path.relative_to(ROOT).as_posix(), sha256=sha(path), bytes=path.stat().st_size)
                    for path in sorted(fixture_root.rglob("*")) if path.is_file()]
    custody_path = csv_record("existing_synthetic_fixture_custody", ["path", "sha256", "bytes"], fixture_rows)
    # Regenerate narrative counts from the named historical bytes only.
    percall = C / "f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv"
    with percall.open(encoding="utf8", newline="") as stream:
        percall_rows = list(csv.DictReader(stream))
    handoff_rows = [row for row in percall_rows if row.get("fixture") == "F3-REAL"]
    stderr = C / "f3_step2_rp1-r1_launch2_stderr_2026-10-05.log"
    warning_lines = stderr.read_text(encoding="utf8").splitlines()
    warning_records = sum("Warning:" in line for line in warning_lines)
    runtime_warnings = sum("RuntimeWarning:" in line for line in warning_lines)
    old_writer = C / "_w3_writer_rp1-r1_tmp.py"
    if not old_writer.exists():
        candidates = list(C.glob("*rp1-r1*write*custody*.py"))
        old_writer = candidates[0] if len(candidates) == 1 else old_writer
    instr_count: int | str = "NOT OBSERVED"
    if old_writer.exists():
        writer_tree = ast.parse(old_writer.read_text(encoding="utf8"))
        for node in ast.walk(writer_tree):
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "INSTR" for t in node.targets):
                instr_count = len(ast.literal_eval(node.value))
    errata = dict(handoff_spline_rows=dict(historical_narrative=8895, observed=len(handoff_rows), path=percall.relative_to(ROOT).as_posix(), sha256=sha(percall)),
        warning_records=dict(historical_narrative="42k+", observed=warning_records, lines=len(warning_lines), runtime_warnings=runtime_warnings,
                             path=stderr.relative_to(ROOT).as_posix(), sha256=sha(stderr)),
        external_writer_pins=dict(historical_narrative=31, observed=instr_count, path=old_writer.relative_to(ROOT).as_posix(),
                                  sha256=sha(old_writer) if old_writer.exists() else "NOT OBSERVED"),
        upstream_inventory_count=dict(historical_narrative=11, audit_corrected=12, status="Audit attribution; no historical document modified."),
        scen_a_estimate_scope="Historical SCEN-A family telemetry is MINI_BANK; a full-bank description is unsupported. New size estimate requires measured Q10 bytes; NOT OBSERVED.",
        missing_historical_custody="Deleted dry-copy custody and historical ZIP associations: X / NOT OBSERVED. Existing untracked ZIPs are not used to reconstruct historical identity.")
    json_record("historical_count_errata", errata)
    matcher = difflib.SequenceMatcher(None, PARENT.read_text(encoding="utf8").splitlines(), source.splitlines(), autojunk=False)
    own_lines = {line + 1 for tag, _, _, first, last in matcher.get_opcodes() if tag in ("replace", "insert") for line in range(first, last)}
    diffs = [make_diff(PARENT, "rp1-r1", source, own_lines), make_diff(R42, "r4-2", source, own_lines)]
    json_record("diff_custody", diffs)
    tools = C / "f3_rp1-r2_gate_tools_2026-10-10.py"
    tests = C / "f3_rp1-r2_technical_tests_2026-10-10.py"
    specs = {
        "Q1": (tools, "check_intake", "complete_intake; inherited synthetic path", "real_x; real_mask_ids; real_x[F,0]; real_mask_ids[F,0]; no_optimizer_reached"),
        "Q2": (HARNESS, "real_mask_id", "one_literal; actual_equals_dry", "duplicate_rejected"),
        "Q3": (tools, "check_f1_manifest", "complete", "missing; extra; changed_raw; manifest_hash; field; row; ordering"),
        "Q4": (HARNESS, "t_f1_loader_synth", "no_constant_ok; computed loader cases", "constant_rejected"),
        "Q5": (tools, "compare_document", "count_transition", "wrong_equal_count; addition_in_both; unequal_equal; deep_not_hidden; absent_in_both"),
        "Q6": (tools, "traceback_signature", "path_normalized", "changed_raise_rejected"),
        "Q7": (HARNESS, "store_read_aggregate", "resumed_cold; stored_payload_matches", "corrupt_payload_rejected"),
        "Q8": (HARNESS, "ckpt_load", "nrgates_all; unittests_all; realscen replay and value equality", "fresh_is_not_replay"),
        "Q9": (tools, "family_of_key", "onestart_scope; splmode_scope; phase", "wrong_phase_rejected"),
        "Q10": (HARNESS, "handoff_accounting", "family_units_reconciled; spline_rows_reconciled; trajectory_timings", "missing_optimizer_row_rejected"),
        "Q11": (tools, "launch_matches", "same_launch", "different_launch; missing_launch"),
    }
    map_rows = []
    for requirement, (path, function, positive, negative) in specs.items():
        map_rows.append(dict(requirement=requirement, code_or_record=line_of(path, function), positive_test=positive,
            negative_test=negative, test_location=line_of(tests, "reproduction_cases" if requirement == "Q3" else "technical_cases"),
            verification="Future T-RP1R2-" + requirement + " in W-3 attempt only", evidence="NOT OBSERVED", final_launch_result="NOT OBSERVED"))
    map_rows.append(dict(requirement="S5B", code_or_record=line_of(C / "f3_rp1-r2_launch_attempt_2026-10-10.py", "main"),
        positive_test="authorized invocation records code/dir/start/end/outputs/disposition", negative_test="missing PI authorization refuses before writer/harness",
        test_location="source-defined launch guard; runtime NOT OBSERVED", verification="Per-launch immutable records plus append-only attempt log", evidence="NOT OBSERVED", final_launch_result="NOT OBSERVED"))
    for requirement, path, evidence, method in (
        ("S5A", stop, "Original details X / NOT OBSERVED; STOP before launch", "Read named historical log; do not infer custody"),
        ("IR1-14", stop, "X labels retained for absent original execution/custody bytes", "Check evidence wording against named-byte availability"),
        ("IR1-15", P / (PREFIX + "historical_count_errata_" + DATE + ".json"), "Counts from named CSV/log/AST bytes; original records unchanged", "Script counts with source paths and hashes"),
        ("IR1-16", P / (PREFIX + "diff_custody_" + DATE + ".json"), "Two context-0 diffs with per-line-range semantic labels", "Range coverage for every removed/added line"),
        ("IR1-17", ledger_path, "Complete inventory ledger plus deferred real-F1 sidecar; no new CLOSED", "Ledger rows carried from sealed start inventory"),
        ("IR1-19", custody_path, "Every existing synthetic fixture byte hash; files not rewritten", "Enumerate synthetic tree; Q3 future generator writes sidecars"),
    ):
        map_rows.append(dict(requirement=requirement, code_or_record=path.relative_to(ROOT).as_posix() + ":1",
            positive_test="N/A (record requirement)", negative_test="N/A (record requirement)", test_location="N/A (record requirement)",
            verification=method, evidence=evidence, final_launch_result="N/A; record verification pending independent audit"))
    map_path = csv_record("requirement_map", list(map_rows[0]), map_rows)
    static = dict(preparation_only=True, harness_invocations=0, test_excerpt_invocations=0,
        observations=observations, unchanged_parent_function_count=len(unchanged), unchanged_parent_functions=unchanged,
        changed_parent_functions=changed, parent_sha256=sha(PARENT), current_head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        tracked_diff=subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True),
        syntax_only="No harness/test modules imported, harness/test functions executed, tests run or optimizer measurements made.",
        current_status=subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True),
        finished_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    assert static["tracked_diff"] == "", "HISTORICAL_TRACKED_FILE_CHANGED"
    static_path = json_record("static_source_observations", static)
    report = P / (PREFIX + "prelaunch_report_" + DATE + ".md")
    counts = collections.Counter(item["status"] for item in items)
    report_data = dict(status="PARTIAL_PENDING_PI", launch_authorized=False, real_data_access=False,
        executed_tests="NOT OBSERVED", Q3_generated_fixture_bytes="NOT OBSERVED", Q10_measurements="NOT OBSERVED", size_estimate="NOT OBSERVED",
        source_parent=dict(path=PARENT.relative_to(ROOT).as_posix(), sha256=sha(PARENT)),
        harness=dict(path=HARNESS.relative_to(ROOT).as_posix(), sha256=sha(HARNESS)),
        inventory_sha256=sha(inventory_path), requirement_map=map_path.relative_to(ROOT).as_posix(),
        ledger_rows=len(items), ledger_status_counts=dict(counts), synthetic_files_hashed=len(fixture_rows),
        synthetic_unique_sha256=len({row["sha256"] for row in fixture_rows}), fixture_custody_sha256=sha(custody_path),
        static_source_observations=static_path.relative_to(ROOT).as_posix(), code_file_count=len(code_files), diff_records=diffs,
        missing_deliverables=["Authorized W-3 custody and launch logs", "Final results/test evidence/non-regression CSV", "Q3 generated synthetic deliverables", "Q10 family telemetry/timing/estimate", "IR1-13 original custody evidence or item-specific PI disposition"])
    write(report, "# rp1-r2 prelaunch preparation report\n\nStatus: PARTIAL_PENDING_PI. The user prohibits a launch until the IR1-13 PI decision arrives.\n\n"
        + "The implementation was authored in pkp-worktree from its pinned rp1-r1 parent and the supplied instruction. The other session's rp1-r2 draft in rp1r1_audit/repo was excluded: no copying, use or modification. The user's exact disclosure is in the attempt log. No harness/copy/test excerpt or optimizer was executed. Syntax parsing/compilation is observed; runtime correctness remains NOT OBSERVED.\n\n"
        + "Q1-Q11 source and positive/negative test definitions are supplied. New execution and restart paths use rp1-r2; every launch requires a false-by-default IR1-13 authorization and a matching immutable W-3 launch record. Q3 is PI-b form B: eleven rule-defined fields are re-derived, while source_scope, source_record_status and exclusion_reason are custody-hash-only. Its fixture generator and all Q3 test branches will run only inside the authorized attempt. Q10 exports actual family optimizer events, reconciles start/mode payloads and supplies measured per-trajectory timing; its future size estimate is labelled ESTIMATE and scoped to those synthetic measurements.\n\n"
        + "No current item is CLOSED by the executor. Implemented source/records remain pending verification; IR1-13 and not-yet-generated Q3 evidence remain OPEN. The deferred F1 input-hash-table sidecar remains OPEN until real-data step 1; its real table was not opened. Historical documents and original fixtures remain unchanged. This is preparation by the executor, not an independent audit.\n\n"
        + "## Historical count errata\n\nCounts below are generated from named bytes or explicitly attributed to the supplied audit. Existing rp1-r1 documents are not edited.\n\n```json\n" + json.dumps(errata, indent=2) + "\n```\n\n"
        + "## Machine-transferred preparation observations\n\n```json\n" + json.dumps(report_data, indent=2) + "\n```\n")
    # Sealing covers only this session's newly created files and unchanged copies
    # of the supplied inputs. Historical artifacts are never re-sealed or edited.
    new_files = [*code_files, *P.glob("*rp1-r2*2026-10-10.*")]
    for row in inventory["incoming"]:
        new_files.append(ROOT / "p_konum_plus/prompts" / Path(row["path"]).name)
    new_files = sorted({path for path in new_files if path.is_file() and not path.name.endswith(".sha256")})
    for path in new_files:
        seal(path)
    manifest = csv_record("prelaunch_transmission_list", ["path", "sha256", "bytes", "role"],
        [dict(path=path.relative_to(ROOT).as_posix(), sha256=sha(path), bytes=path.stat().st_size,
              role="PRELAUNCH_REVIEW_ONLY; runtime NOT OBSERVED") for path in new_files])
    seal(manifest)
    archive = ROOT / "p_konum_plus" / (PREFIX + "prelaunch_review_package_" + DATE + ".zip")
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as package:
        for path in [*new_files, manifest]:
            package.write(path, path.relative_to(ROOT).as_posix())
            sidecar = Path(str(path) + ".sha256")
            package.write(sidecar, sidecar.relative_to(ROOT).as_posix())
    seal(archive)
    print(json.dumps(dict(status="PARTIAL_PENDING_PI", code_files=len(code_files), ledger_rows=len(items),
        existing_synthetic_files=len(fixture_rows), report=report.relative_to(ROOT).as_posix(),
        package=archive.relative_to(ROOT).as_posix(), harness_invocations=0)))


if __name__ == "__main__":
    main()
