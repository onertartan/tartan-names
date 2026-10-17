"""Build source-derived line-range labels and immutable-parent diff records."""
from __future__ import annotations

import ast
import csv
import difflib
import hashlib
import json
from pathlib import Path
import re
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "p_konum_plus/calibration"
P = ROOT / "p_konum_plus/provenance"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def side(path: Path) -> None:
    Path(str(path) + ".sha256").write_text(sha(path) + "  " + path.name + "\n", encoding="ascii")


def csv_write(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    assert "rp1-r3" in path.name or "labels_r1_2026-10-15" in path.name
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    side(path)


def read(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines(keepends=True)


def propagate(a: list[str], b: list[str], labels: dict[int, str]) -> dict[int, str]:
    result = {}
    for block in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for offset in range(block.size):
            if block.a + offset + 1 in labels:
                result[block.b + offset + 1] = labels[block.a + offset + 1]
    return result


def annotations(path: Path) -> tuple[dict[int, str], dict[int, str]]:
    old, new = {}, {}
    label = ""
    a = b = 0
    for line in read(path):
        if line.startswith("#HUNK"):
            label = re.search(r" LABEL (\S+)", line).group(1)
            label = ("rp1:" if label.startswith("C-") else "rp1-r1:") + label
        elif line.startswith("@@"):
            match = re.match(r"@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
            a, b = map(int, match.groups())
        elif line.startswith(("---", "+++", "#")):
            continue
        elif line.startswith("-"):
            old[a] = label
            a += 1
        elif line.startswith("+"):
            new[b] = label
            b += 1
        elif line.startswith(" "):
            a += 1
            b += 1
    return old, new


def harness_labels(source: str) -> dict[int, str]:
    lines = source.splitlines()
    result = {i + 1: "R3-5" for i in range(len(lines))}
    for i, line in enumerate(lines, 1):
        if ('["rp1_r3_status"]' in line or '["rp1_r3_open_findings"]' in line):
            result[i] = "S8"
    tree = ast.parse(source)
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    declaration = next(n for n in main.body if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == "EXPECTATIONS_E" for t in n.targets))
    for namespace, values in zip(declaration.value.keys, declaration.value.values):
        if ast.literal_eval(namespace) != "results":
            continue
        for entry in values.elts:
            item = ast.literal_eval(entry)
            if item["path"] in ("end_state.PI_dispatch_record_hash", "end_state.PI_dispatch_record_path"):
                value = next(v for k, v in zip(entry.keys, entry.values) if ast.literal_eval(k) == "reason")
                for number in range(value.lineno, value.end_lineno + 1):
                    result[number] = "R3-4"
    start = next(i for i, line in enumerate(lines, 1) if line.startswith("    current_open = [row"))
    end = next(i for i in range(start, len(lines)) if 'six["standalone_evidence_status"]' in lines[i - 1])
    for number in range(start - 1, end):
        result[number] = "S8"
    return result


def function_labels(source: str, family: str) -> dict[int, str]:
    result = {i + 1: "R3-5" for i in range(len(source.splitlines()))}
    names = dict(constant_ok_count="R3-2", q4_cases="R3-2", q5_cases="R3-3", q6_cases="R3-1",
                 traceback_signature="R3-1", rrs_cases="R3-5")
    for node in ast.parse(source).body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for number in range(node.lineno, node.end_lineno + 1):
                result[number] = names[node.name]
    if family == "tests":
        lines = source.splitlines()
        for number, line in enumerate(lines, 1):
            if 'out["Q4"]' in line or 'out["Q5"]' in line or 'out["Q6"]' in line:
                result[number] = {"Q4": "R3-2", "Q5": "R3-3", "Q6": "R3-1"}[next(q for q in ("Q4", "Q5", "Q6") if q in line)]
        # Parent Q4/Q5/Q6 constructions are removed by the respective replacement.
        if '    bad = [' in source:
            a = next(i for i, line in enumerate(lines, 1) if 'out["Q4"]' in line)
            b = next(i for i, line in enumerate(lines, 1) if '    bad = [' in line)
            d = next(i for i, line in enumerate(lines, 1) if '    text = ' in line)
            e = next(i for i, line in enumerate(lines, 1) if '    stored = [' in line)
            for number in range(a, b): result[number] = "R3-2"
            for number in range(b, d): result[number] = "R3-3"
            for number in range(d, e): result[number] = "R3-1"
    return result


def emit(old_path: Path | None, new_path: Path, tag: str,
         old_labels: dict[int, str], new_labels: dict[int, str]) -> dict[str, Any]:
    old, new = read(old_path) if old_path else [], read(new_path)
    diff = list(difflib.unified_diff(old, new, fromfile=str(old_path or "/dev/null"), tofile=str(new_path), n=0))
    path = P / f"f3_realdata_prep_rp1-r3_{tag}_2026-10-15.diff"
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.writelines(diff)
    side(path)
    rows = []
    hunk = 0
    a = b = 0
    changed = 0
    for line in diff[2:]:
        if line.startswith("@@"):
            hunk += 1
            match = re.match(r"@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
            a, b = map(int, match.groups())
        elif line.startswith(("-", "+")):
            which, number, mapping = ("old", a, old_labels) if line[0] == "-" else ("new", b, new_labels)
            if number not in mapping and not line[1:].strip():
                # Blank separators belong to the nearest labelled statement.
                nearest = min(mapping, key=lambda k: (abs(k - number), k))
                mapping[number] = mapping[nearest]
            assert number in mapping, (tag, which, number, line)
            label = mapping[number]
            assert " with " not in label and label
            if rows and all(rows[-1][k] == v for k, v in dict(hunk=hunk, side=which, label=label).items()) and rows[-1]["last"] == number - 1:
                rows[-1]["last"] = number
            else:
                rows.append(dict(hunk=hunk, side=which, first=number, last=number, label=label,
                                 reason="Source content and originating package; exact non-overlapping changed-line range."))
            changed += 1
            if which == "old": a += 1
            else: b += 1
    labels = path.with_name(path.stem + "_labels.csv")
    csv_write(labels, rows, ["hunk", "side", "first", "last", "label", "reason"])
    assert sum(x["last"] - x["first"] + 1 for x in rows) == changed
    return dict(baseline=str(old_path), baseline_sha256=sha(old_path) if old_path else None,
                target=str(new_path), target_sha256=sha(new_path), diff=str(path), diff_sha256=sha(path),
                labels=str(labels), labels_sha256=sha(labels), hunk_count=hunk, covered_changed_lines=changed)


def main() -> None:
    parent = C / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    current = C / "f3_step2_adequacy_harness_rp1-r3_2026-10-15.py"
    r1 = C / "f3_step2_adequacy_harness_rp1-r1_2026-10-05.py"
    r42 = C / "f3_step2_adequacy_harness_r4-2_2026-09-30.py"
    corrected = {}
    for baseline in ("rp1-r1", "r4-2"):
        source = P / f"f3_realdata_prep_rp1-r2_harness_diff_vs_{baseline}_labels_2026-10-12.csv"
        with source.open(encoding="utf-8", newline="") as stream: rows = list(csv.DictReader(stream))
        result = []
        for row in rows:
            if row["label"] != "Q10 with Q9 phase ranges":
                result.append(row)
                continue
            lines = read(parent if row["side"] == "new" else r1 if baseline == "rp1-r1" else r42)
            for number in range(int(row["first"]), int(row["last"]) + 1):
                text = lines[number - 1]
                label = "Q9" if "CURRENT_PHASE" in text or "saved_phase" in text else "Q10"
                result.append(dict(row, first=number, last=number, label=label,
                                   reason="Q9 phase attribution/restoration." if label == "Q9" else "Q10 trajectory timing/family telemetry; no phase statement in this range."))
        target = P / f"f3_realdata_prep_rp1-r2_harness_diff_vs_{baseline}_labels_r1_2026-10-15.csv"
        csv_write(target, result, list(rows[0]))
        corrected[baseline] = result
    records = [emit(parent, current, "harness_diff_vs_rp1-r2", harness_labels(parent.read_text(encoding="utf-8")),
                    harness_labels(current.read_text(encoding="utf-8")))]
    old_origins, r1_origins = annotations(C / "f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff")
    parent_origins = propagate(read(r1), read(parent), r1_origins)
    for row in corrected["rp1-r1"]:
        if row["side"] == "new":
            for number in range(int(row["first"]), int(row["last"]) + 1):
                parent_origins[number] = "rp1-r2:" + row["label"]
    current_origins = propagate(read(parent), read(current), parent_origins)
    own = harness_labels(current.read_text(encoding="utf-8"))
    for opcode, a, b, x, y in difflib.SequenceMatcher(None, read(parent), read(current), autojunk=False).get_opcodes():
        if opcode != "equal":
            for number in range(x + 1, y + 1): current_origins[number] = "rp1-r3:" + own[number]
    for row in corrected["r4-2"]:
        if row["side"] == "old":
            for number in range(int(row["first"]), int(row["last"]) + 1):
                old_origins.setdefault(number, "rp1-r2:" + row["label"])
    # A baseline line untouched by both ancestors but changed in this child is a child change.
    for opcode, a, b, x, y in difflib.SequenceMatcher(None, read(r42), read(current), autojunk=False).get_opcodes():
        if opcode != "equal":
            for number in range(a + 1, b + 1): old_origins.setdefault(number, "rp1-r3:R3-5")
    records.append(emit(r42, current, "harness_diff_vs_r4-2", old_origins, current_origins))
    for family, stem in (("tools", "gate_tools"), ("tests", "technical_tests"),
                         ("launcher", "launch_attempt"), ("writer", "write_custody")):
        old = C / f"f3_rp1-r2_{stem}_2026-10-10.py"
        new = C / f"f3_rp1-r3_{stem}_2026-10-15.py"
        left, right = function_labels(old.read_text(encoding="utf-8"), family), function_labels(new.read_text(encoding="utf-8"), family)
        records.append(emit(old, new, family + "_diff_vs_rp1-r2", left, right))
    path = P / "f3_realdata_prep_rp1-r3_diff_custody_2026-10-15.json"
    with path.open("w", encoding="ascii", newline="\n") as stream:
        json.dump(dict(method="Context 0; one label per changed-line range; inherited annotations propagated through unchanged source lines; corrected Q9/Q10 ranges; originals untouched", diffs=records), stream, indent=2)
        stream.write("\n")
    side(path)
    print(json.dumps(dict(records=len(records), custody_sha256=sha(path))))


if __name__ == "__main__":
    main()
