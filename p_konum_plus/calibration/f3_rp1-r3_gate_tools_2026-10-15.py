"""Technical gates for D-13; no module-level file access or computation."""
from __future__ import annotations

import ast
import csv
import hashlib
import io
import json
from pathlib import Path
import re
from typing import Any, Callable

MANIFEST_COLUMNS = (
    "trajectory_id", "sex", "name", "year_min", "year_max", "T", "source_scope",
    "eligibility_rule_id", "trajectory_value_id", "source_record_status",
    "n_observed_years", "n_missing_total", "eligible", "exclusion_reason",
)
F1_MANIFEST_PIN = "8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32"
HASH_ONLY_COLUMNS = ("source_scope", "source_record_status", "exclusion_reason")
ABSENT = object()
D14_PATH = "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md"
D14_SHA256 = "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7"


def authorize_ir1_13(root: Path) -> dict[str, str]:
    """D-14 releases the launch gate by its fixed signed bytes, never a flag."""
    path = root / D14_PATH
    if not path.is_file() or not Path(str(path) + ".sha256").is_file():
        raise ValueError("D14_RECORD_OR_SIDECAR_MISSING")
    data = path.read_bytes()
    observed = hashlib.sha256(data).hexdigest()
    sidecar = Path(str(path) + ".sha256").read_text(encoding="ascii").split()
    if observed != D14_SHA256 or len(sidecar) != 2 or sidecar[0] != D14_SHA256 or sidecar[1] != path.name:
        raise ValueError("D14_HASH_STOP")
    text = data.decode("utf8")
    if not all(token in text for token in ("status                = SIGNED", "IR1-13   = RECORDED_LIMITATION", "attempt 1 once every", "OPEN / B")):
        raise ValueError("D14_SIGNED_DISPOSITION_STOP")
    return dict(finding="IR1-13", disposition="RECORDED_LIMITATION", ledger_status="OPEN / B",
                pi_record_path=D14_PATH, pi_record_sha256=observed,
                standalone_evidence_status="NOT OBSERVED", executor_status="PARTIAL_PENDING_PI")


def check_intake(scenario: dict[str, Any], gap: type[Exception]) -> bool:
    """Q1: reject incomplete real intake before the consumer reaches a fitter."""
    strata = scenario.get("strata", {})
    is_real = ("real_x" in scenario or "real_mask_ids" in scenario
               or any(row[0] == "F1REAL" for rows in strata.values() for row in rows))
    required = ["fixture_id", "strata", "start_bank", "injections"]
    if is_real:
        required += ["real_x", "real_mask_ids"]
    for key in required:
        if key not in scenario:
            raise gap(key)
    if is_real:
        for sex, trajectories in strata.items():
            for index, _ in enumerate(trajectories):
                for key in ("real_x", "real_mask_ids"):
                    if not isinstance(scenario[key], dict) or (sex, index) not in scenario[key]:
                        raise gap("%s[%s,%d]" % (key, sex, index))
    return is_real


def restored(value: Any) -> Any:
    """Q8: label all nested optimizer telemetry copies on a cache hit."""
    if isinstance(value, dict):
        result = {key: restored(item) for key, item in value.items()}
        if "wall_clock_seconds" in value and (
                "optimizer_path" in value or "method" in value or "source" in value):
            result["source"] = "replay"
        return result
    if isinstance(value, list):
        return [restored(item) for item in value]
    if isinstance(value, tuple):
        return tuple(restored(item) for item in value)
    return value


def equal_replay(stored_rows: list[dict[str, Any]], replay_rows: list[dict[str, Any]]) -> bool:
    """Q7: every stored value is preserved, with only source changed to replay."""
    expected = [dict(row, source="replay") for row in stored_rows]
    return expected == replay_rows


def family_of_key(key: str) -> str:
    """Q9: remove scope prefixes before identifying the underlying unit."""
    while "__" in key and not key.startswith(("onestart_", "splmode_", "realscen_", "nrgates_all", "unittests_all")):
        key = key.split("__", 1)[1]
    for family in ("onestart", "splmode", "realscen", "nrgates_all", "unittests_all"):
        if key.startswith(family):
            return family
    return key.split("_", 1)[0]


def launch_matches(record: str | None, number: int) -> bool:
    """Q11: a missing, malformed or different launch number fails custody."""
    return bool(record and record.isdecimal() and int(record) == number and number > 0)


def frozen_fields(eligible: Any) -> list[dict[str, str]]:
    """F1 freeze section 7: loader output contains only FULL-support keys."""
    return [dict(trajectory_id=f"{sex}_{name}", sex=sex, name=name,
                 year_min="1880", year_max="2025", T="146", n_observed_years="146",
                 n_missing_total="0", eligible="true",
                 eligibility_rule_id="OD5_FULL_observed_support_1880_2025",
                 trajectory_value_id="OD3_released_record_share_by_year_and_sex")
            for sex, name in sorted(eligible)]


def check_f1_manifest(raw: str, hashes: list[tuple[str, str]], manifest: str,
                      manifest_pin: str, eligible_loader: Callable[[str], Any],
                      failure: type[Exception], *, synthetic: bool = False) -> bool:
    """Q3 form B: custody, complete raw list, schema, ordering, content."""
    if not synthetic and manifest_pin != F1_MANIFEST_PIN:
        raise failure("F1_REPRO_GATE_REAL_PIN")
    root = Path(raw)
    names = [name for name, _ in hashes]
    if len(set(names)) != len(names) or any(Path(name).name != name for name in names):
        raise failure("F1_REPRO_GATE_HASH_TABLE_SCHEMA")
    actual = set(p.name for p in root.iterdir())
    wanted = set(names)
    if wanted - actual:
        raise failure("F1_REPRO_GATE_MISSING_FILE")
    if actual - wanted:
        raise failure("F1_REPRO_GATE_EXTRA_FILE")
    for name, pin in hashes:
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != pin:
            raise failure("F1_REPRO_GATE_HASH_MISMATCH")
    data = Path(manifest).read_bytes()
    if hashlib.sha256(data).hexdigest() != manifest_pin:
        raise failure("F1_REPRO_GATE_MANIFEST_HASH_MISMATCH")
    try:
        reader = csv.DictReader(io.StringIO(data.decode("ascii"), newline=""))
        if tuple(reader.fieldnames or []) != MANIFEST_COLUMNS:
            raise failure("F1_REPRO_GATE_MANIFEST_SCHEMA")
        rows = list(reader)
        if any(None in row or None in row.values() for row in rows):
            raise failure("F1_REPRO_GATE_MANIFEST_SCHEMA")
    except (UnicodeError, csv.Error) as error:
        raise failure("F1_REPRO_GATE_MANIFEST_SCHEMA") from error
    counts = {sex: sum(row["sex"] == sex for row in rows) for sex in ("F", "M")}
    expected_counts = {"F": 3, "M": 3} if synthetic else {"F": 435, "M": 471}
    if counts != expected_counts or len(rows) != sum(expected_counts.values()):
        raise failure("F1_REPRO_GATE_ROW_COUNT")
    keys = [(row["sex"], row["name"]) for row in rows]
    if keys != sorted(keys) or len(set(keys)) != len(keys):
        raise failure("F1_REPRO_GATE_ORDERING")
    derived = frozen_fields(eligible_loader(raw))
    if len(rows) != len(derived):
        raise failure("F1_REPRO_GATE_ROW_COUNT_REDERIVED")
    number_fields = {"year_min", "year_max", "T", "n_observed_years", "n_missing_total"}
    for index, (row, expected) in enumerate(zip(rows, derived)):
        for field, value in expected.items():
            got = row[field]
            if field in number_fields:
                try:
                    got = str(int(got))
                except ValueError:
                    pass
            if field == "eligible":
                got = got.lower()
            if got != value:
                raise failure("F1_REPRO_GATE_FIELD_MISMATCH row=%d field=%s" % (index, field))
    return True


def flatten_document(document: Any, path: str = "") -> dict[str, Any]:
    """Q5: dictionaries and lists recurse; empty containers retain a leaf."""
    result: dict[str, Any] = {}
    if isinstance(document, dict) and document:
        for key, value in document.items():
            result.update(flatten_document(value, path + "." + str(key) if path else str(key)))
    elif isinstance(document, list) and document:
        for index, value in enumerate(document):
            result.update(flatten_document(value, "%s[%d]" % (path, index)))
    else:
        result[path or "(root)"] = document
    return result


def declaration_matches(pattern: str, path: str) -> bool:
    expression = re.escape(pattern).replace(r"\[\*\]", r"\[\d+\]")
    return re.fullmatch(expression, path) is not None


def holds(spec: dict[str, Any], old: Any, new: Any) -> bool:
    if old is ABSENT and new is ABSENT:
        return False
    kind = spec["kind"]
    if kind == "EQUAL":
        return old == new
    if kind == "ADDITION":
        return old is ABSENT and new is not ABSENT
    if kind == "COUNT":
        old_matches = old is ABSENT if spec.get("old_absent") else old == spec["old"]
        return old_matches and new == spec["new"]
    return kind == "MAY_DIFFER"


def compare_document(old: Any, new: Any, declarations: list[dict[str, Any]],
                     namespace: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    old_leaves, new_leaves = flatten_document(old), flatten_document(new)
    rows: list[dict[str, Any]] = []
    matched: set[str] = set()
    for path in sorted(set(old_leaves) | set(new_leaves)):
        a, b = old_leaves.get(path, ABSENT), new_leaves.get(path, ABSENT)
        specs = [entry for entry in declarations if declaration_matches(entry["path"], path)]
        if len(specs) > 1:
            raise ValueError("OVERLAPPING_DECLARATIONS " + path)
        spec = specs[0] if specs else None
        if spec is None and a == b:
            continue
        held = holds(spec, a, b) if spec else False
        if spec:
            matched.add(spec["id"])
        rows.append(dict(path=namespace + "." + path, classification="E" if held else "U_FINDING",
                         declaration_id=spec["id"] if spec else "", kind=spec["kind"] if spec else "UNDECLARED",
                         held=held, reason=spec["reason"] if spec else "undeclared differing leaf",
                         r4_2=json.dumps("<ABSENT>" if a is ABSENT else a, sort_keys=True, ensure_ascii=True),
                         **{"rp1-r2": json.dumps("<ABSENT>" if b is ABSENT else b, sort_keys=True, ensure_ascii=True)}))
    for spec in declarations:
        if spec["id"] not in matched:
            rows.append(dict(path=namespace + "." + spec["path"], classification="U_FINDING",
                             declaration_id=spec["id"], kind=spec["kind"], held=False,
                             reason="declared path absent from both documents", r4_2="<ABSENT>", **{"rp1-r2": "<ABSENT>"}))
    return rows, [row for row in rows if not row["held"]]


def traceback_signature(trace: str, source: str, harness_name: str) -> str:
    """Q6: retain the frame sequence and exception; map harness lines to statements."""
    statements = [n for n in ast.walk(ast.parse(source)) if isinstance(n, ast.stmt)]
    frames = []
    for filename, line_text, function in re.findall(r'File "([^"]+)", line (\d+), in ([^\n\r]+)', trace):
        if Path(filename).name == harness_name:
            number = int(line_text)
            candidates = [n for n in statements if n.lineno <= number <= n.end_lineno]
            if not candidates:
                raise ValueError("TRACEBACK_SOURCE_COORDINATE_NOT_FOUND")
            node = min(candidates, key=lambda n: (n.end_lineno - n.lineno, -n.lineno))
            frames.append(("<HARNESS>", function, ast.get_source_segment(source, node)))
        else:
            frames.append((filename, function, int(line_text)))
    exception_lines: list[str] = []
    harness_paths = {filename for filename, _, _ in re.findall(
        r'File "([^"]+)", line (\d+), in ([^\n\r]+)', trace)
        if Path(filename).name == harness_name}
    after_frame = False
    frame_pattern = re.compile(r'^\s*File "[^"]+", line \d+, in [^\r\n]+$')
    for line in trace.splitlines():
        if line.strip() == "Traceback (most recent call last):":
            after_frame = False
            continue
        if frame_pattern.match(line):
            after_frame = True
            continue
        if after_frame and line.startswith("    "):
            after_frame = False
            continue
        after_frame = False
        # Exception text may itself contain the harness path.
        for filename in sorted(harness_paths, key=len, reverse=True):
            line = line.replace(filename, "<HARNESS>")
        line = re.sub(r'(?:(?:[A-Za-z]:[\\/]|/|\\\\)(?:[^\s\"\'<>]*[\\/])?)?'
                      + re.escape(harness_name), "<HARNESS>", line)
        exception_lines.append(line)
    return json.dumps(dict(frames=frames, exception="\n".join(exception_lines)),
                      sort_keys=True, ensure_ascii=True)



def normalize_traces(document: Any, source: str, harness_name: str) -> Any:
    if isinstance(document, dict):
        return {key: traceback_signature(value, source, harness_name)
                if key == "traceback" and isinstance(value, str)
                else normalize_traces(value, source, harness_name) for key, value in document.items()}
    if isinstance(document, list):
        return [normalize_traces(item, source, harness_name) for item in document]
    return document
