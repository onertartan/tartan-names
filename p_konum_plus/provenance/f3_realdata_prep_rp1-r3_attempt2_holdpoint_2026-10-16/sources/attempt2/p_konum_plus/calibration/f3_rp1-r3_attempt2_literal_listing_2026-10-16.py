"""D-20 C-3 literal inventory; never read real SSA/F1 inputs."""
from __future__ import annotations

import ast
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any

FILES = ["f3_step2_adequacy_harness_rp1-r3_2026-10-15.py"] + [
    "f3_rp1-r3_" + stem + "_2026-10-15.py"
    for stem in ("gate_tools", "technical_tests", "launch_attempt", "write_custody")]
FORBIDDEN = {"p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv",
             "p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect(source: str) -> tuple[dict[Any, ast.Constant], dict[ast.AST, ast.AST]]:
    tree = ast.parse(source)
    found, parents = {}, {}

    def visit(node: ast.AST, anchor: str, route: tuple[Any, ...]) -> None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            found[(anchor, route)] = node
        for field, value in ast.iter_fields(node):
            children = enumerate(value) if isinstance(value, list) else [(None, value)]
            for index, child in children:
                if isinstance(child, ast.AST):
                    parents[child] = node
                    visit(child, anchor, route + ((field, index),))

    for index, node in enumerate(tree.body):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            anchor = node.name
        elif isinstance(node, ast.Assign):
            anchor = "assign:" + ",".join(ast.unparse(t) for t in node.targets)
        else:
            anchor = type(node).__name__ + ":" + str(index)
        visit(node, anchor, ())
    return found, parents


def pin_context(node: ast.AST, parents: dict[ast.AST, ast.AST]) -> tuple[str, int] | None:
    parent = parents.get(node)
    if isinstance(parent, ast.Tuple) and len(parent.elts) == 3 and isinstance(parent.elts[1], ast.Constant):
        pin = parent.elts[1].value
        if isinstance(pin, str) and len(pin) == 64:
            return pin, parent.elts.index(node)
    return None


def pin_values(nodes: dict[Any, ast.Constant], parents: dict[ast.AST, ast.AST]) -> dict[Any, str]:
    return {context: node.value for node in nodes.values() if (context := pin_context(node, parents)) is not None}


def resolve(root: Path, value: str) -> Path | None:
    if "\n" in value or "\r" in value or len(value) > 500 or value.startswith(" "):
        return None
    for base in (root, root / "p_konum_plus/calibration", root / "p_konum_plus/prompts", root / "p_konum_plus/provenance"):
        path = base / value
        try:
            if path.is_file(): return path
        except (OSError, ValueError):
            pass
    return None


def assignment_value(node: ast.AST, parents: dict[ast.AST, ast.AST],
                     other: dict[Any, ast.Constant], other_parents: dict[ast.AST, ast.AST]) -> str | None:
    """Match local literals by assignment target, avoiding shifted body indexes."""
    route = []
    current = node
    while current in parents and not isinstance(current, ast.Assign):
        parent = parents[current]
        step = next((field, index if isinstance(value, list) else None)
                    for field, value in ast.iter_fields(parent)
                    for index, child in (enumerate(value) if isinstance(value, list) else [(None, value)])
                    if child is current)
        route.append(step)
        current = parent
    if not isinstance(current, ast.Assign): return None
    target = ",".join(ast.unparse(t) for t in current.targets)
    owner = current
    while owner in parents and not isinstance(owner, ast.FunctionDef): owner = parents[owner]
    if not isinstance(owner, ast.FunctionDef): return None
    candidates = set()
    for value in other.values():
        candidate = value
        while candidate in other_parents and not isinstance(candidate, ast.Assign): candidate = other_parents[candidate]
        if not isinstance(candidate, ast.Assign): continue
        function = candidate
        while function in other_parents and not isinstance(function, ast.FunctionDef): function = other_parents[function]
        if isinstance(function, ast.FunctionDef) and function.name == owner.name and ",".join(ast.unparse(t) for t in candidate.targets) == target:
            candidates.add(candidate)
    if len(candidates) != 1: return None
    candidate = candidates.pop()
    try:
        for field, index in reversed(route):
            candidate = getattr(candidate, field)
            if index is not None: candidate = candidate[index]
        return candidate.value if isinstance(candidate, ast.Constant) and isinstance(candidate.value, str) else None
    except (AttributeError, IndexError, TypeError):
        return None


def main() -> None:
    root, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    q = root / "p_konum_plus/quarantine/f3_step2_rp1-r3_attempt1_2026-10-16/workspace"
    rows = []
    for name in FILES:
        rel = "p_konum_plus/calibration/" + name
        current = (root / rel).read_text(encoding="utf-8")
        baseline = (q / rel).read_text(encoding="utf-8")
        parent_name = (name.replace("rp1-r3", "rp1-r2").replace("2026-10-15", "2026-10-10"))
        parent_source = subprocess.check_output(["git", "show", "25c7d51:p_konum_plus/calibration/" + parent_name], cwd=root).decode("utf-8")
        nodes, parents = collect(current)
        before, before_parents = collect(baseline)
        prior, prior_parents = collect(parent_source)
        before_pins, prior_pins = pin_values(before, before_parents), pin_values(prior, prior_parents)
        prior_values = {n.value for n in prior.values()}
        for key, node in nodes.items():
            value = node.value
            if not any(token in value for token in ("p_konum_plus/", "rp1-r", "2026-")): continue
            context = pin_context(node, parents)
            old = before[key].value if key in before else before_pins.get(context)
            previous = prior[key].value if key in prior else prior_pins.get(context)
            ancestor = node
            while ancestor in parents and not isinstance(ancestor, ast.FunctionDef): ancestor = parents[ancestor]
            if isinstance(ancestor, ast.FunctionDef):
                old = assignment_value(node, parents, before, before_parents)
                if old is None and value in {n.value for n in before.values()}: old = value
                previous = assignment_value(node, parents, prior, prior_parents)
            if previous is None and value in prior_values: previous = value
            actual = resolve(root, value)
            previous_file = resolve(root, previous) if previous is not None else None
            is_pin = context is not None and context[1] == 0 or key[0] in ("assign:D14_PATH", "_d13_path")
            if value == "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md": is_pin = True
            looks_path = value.startswith("p_konum_plus/") or "\n" not in value and value.startswith(("f3_", "Claude_Code_", "F3_"))
            fragment = isinstance(parents.get(node), ast.JoinedStr)
            own = looks_path and "rp1-r3" in value.lower() or fragment and "2026-10-15" in value
            classification = "PIN" if is_pin else "NEW" if own else "HISTPATH" if actual or looks_path and previous_file else "TEXT"
            forbidden = value in FORBIDDEN
            actual_hash = "NOT OBSERVED: D-20 forbids reading/hash-checking real F1 input" if forbidden else sha(actual) if actual else None
            needs_restore = classification == "HISTPATH" and previous is not None and value != previous
            rows.append(dict(file=rel, line=node.lineno, owner=key[0], value=value, attempt1_value=old,
                rp1_r2_counterpart=previous, classification=classification,
                names_existing_file=actual is not None, resolved_path=str(actual) if actual else None,
                observed_file_sha256=actual_hash, fragment=fragment, real_input_not_read=forbidden,
                restoration_required=needs_restore,
                TEXT_review_only=classification == "TEXT" and old is not None and value != old))
    result = dict(observed_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        hash_scope="Hashes are observed during this logged listing; mutable attempt-log final hash is separately frozen in the hold-point manifest",
        scope="D-20 C-3; all matching string constants in the five named files", rows=rows,
        source_hashes={"p_konum_plus/calibration/" + n: sha(root / "p_konum_plus/calibration" / n) for n in FILES},
        count_by_class={k: sum(r["classification"] == k for r in rows) for k in ("NEW", "PIN", "HISTPATH", "TEXT")},
        restoration_required=[r for r in rows if r["restoration_required"]],
        real_input_hashes_not_observed=[r["value"] for r in rows if r["real_input_not_read"]],
        TEXT_literals_changed_from_attempt1=[r for r in rows if r["TEXT_review_only"]],
        TEXT_historical_descriptors_retained=[r for r in rows if r["classification"] == "TEXT"
            and r["attempt1_value"] == r["value"] and r["rp1_r2_counterpart"] is not None
            and r["value"] != r["rp1_r2_counterpart"]],
        real_data_access=False)
    (out / "C3_literal_listing.json").write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="ascii")
    with (out / "C3_literal_listing.csv").open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, ensure_ascii=True))
    if result["restoration_required"]: raise SystemExit("C3_FURTHER_RESTORATION_REQUIRES_REVIEW")


if __name__ == "__main__":
    main()
