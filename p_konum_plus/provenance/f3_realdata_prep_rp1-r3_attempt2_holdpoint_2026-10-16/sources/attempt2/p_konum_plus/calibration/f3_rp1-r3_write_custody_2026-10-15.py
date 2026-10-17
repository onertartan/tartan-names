"""External W-3 writer; never imports the harness or executes its tests."""
from __future__ import annotations

import os
for _thread_pin in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_pin] = "1"

import ast
import csv
import datetime as dt
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import platform
from typing import Any

import numpy as np
import scipy


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def literal_constants(tree: ast.Module) -> dict[str, Any]:
    constants = {}
    for statement in tree.body:
        if not isinstance(statement, ast.Assign) or len(statement.targets) != 1 or not isinstance(statement.targets[0], ast.Name):
            continue
        try:
            value = ast.literal_eval(statement.value)
        except (ValueError, TypeError):
            if isinstance(statement.value, ast.Name) and statement.value.id in constants:
                value = constants[statement.value.id]
            elif (statement.targets[0].id == "RP2_DISPATCH_PINS"
                  and isinstance(statement.value, ast.BinOp) and isinstance(statement.value.op, ast.Add)
                  and isinstance(statement.value.left, ast.Name) and isinstance(statement.value.right, ast.Name)
                  and statement.value.left.id == "RP3_INCOMING_DISPATCH_PINS"
                  and statement.value.right.id == "RP3_CARRIED_DISPATCH_PINS"):
                value = constants[statement.value.left.id] + constants[statement.value.right.id]
            else:
                continue
        constants[statement.targets[0].id] = value
    return constants


def main() -> None:
    root = Path(os.environ.get("F3_REPO_ROOT", Path(__file__).resolve().parents[2])).resolve()
    value = os.environ.get("F3_RP1R3_LAUNCH", "")
    assert value.isdecimal() and int(value) > 0, "W3_LAUNCH_REQUIRED"
    launch = int(value)
    harness = root / "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py"
    assert Path(str(harness) + ".sha256").read_text(encoding="ascii").split()[0] == sha(harness)
    tree = ast.parse(harness.read_text(encoding="utf8"))
    constants = literal_constants(tree)
    helper = harness.with_name("f3_rp1-r3_gate_tools_2026-10-15.py")
    assert sha(helper) == constants["RP2_DEPENDENCY_PINS"][helper.name]
    helper_spec = importlib.util.spec_from_file_location("rp2_w3_authorization", helper)
    helper_module = importlib.util.module_from_spec(helper_spec)
    helper_spec.loader.exec_module(helper_module)
    gate = helper_module.authorize_ir1_13(root)
    assert constants["REAL_DATA_MODE"] is False
    attempt = constants["ATTEMPT_NUMBER"]
    target = root / ("p_konum_plus/provenance/f3_step2_rp1-r3_preexecution_custody_attempt%d_launch%d_2026-10-15.md" % (attempt, launch))
    assert not target.exists(), "W3_REFUSE_EXISTING_CUSTODY"
    main_node = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
    checks = []
    for node in ast.walk(main_node):
        if not isinstance(node, ast.For) or not isinstance(node.target, ast.Tuple):
            continue
        if [getattr(child, "id", "") for child in node.target.elts] != ["ipath", "ihash", "iname"]:
            continue
        items = constants[node.iter.id] if isinstance(node.iter, ast.Name) else None
        iterable = items if items is not None else node.iter.elts
        for item in iterable:
            if items is not None:
                path, pin, name = item
            else:
                path, pin, name = [constants[part.id] if isinstance(part, ast.Name) else ast.literal_eval(part) for part in item.elts]
            observed = sha(root / path)
            assert observed == pin, "W3_DISPATCH_PIN_STOP " + name
            checks.append(dict(path=path, expected=pin, observed=observed, source=name))
    for filename, pin in constants["RP2_DEPENDENCY_PINS"].items():
        assert sha(harness.with_name(filename)) == pin, "W3_DEPENDENCY_PIN_STOP " + filename
    generator = root / constants["GEN_PATH"]
    manifest = root / constants["MANIFEST_PATH"]
    spec = importlib.util.spec_from_file_location("rp2_w3_generator", generator)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(module.MANIFEST_HEADER)
    writer.writerows(module.manifest_rows())
    assert buffer.getvalue().encode("ascii") == manifest.read_bytes(), "W3_MANIFEST_REGEN_STOP"
    store = root / constants["RESTART_STORE_DIR"]
    if launch == 1:
        assert not store.exists() or not any(store.iterdir()), "W3_FIRST_LAUNCH_STORE_NOT_EMPTY"
    env = dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
               platform=platform.platform(), OMP="1", OPENBLAS="1", MKL="1")
    identities = [sha(harness), sha(generator), sha(manifest), constants["F2_HASH"], constants["SPL_HASH"],
                  *[constants["RP2_DEPENDENCY_PINS"][key] for key in sorted(constants["RP2_DEPENDENCY_PINS"])],
                  env["python"], env["numpy"], env["scipy"], env["platform"], "1", "1", "1"]
    observed = dict(harness_sha256=sha(harness), generator_sha256=sha(generator), manifest_sha256=sha(manifest),
                    code_env_fingerprint=hashlib.sha256("|".join(identities).encode()).hexdigest()[:16],
                    attempt_number=attempt, launch_number=launch, **constants["RP2_DEPENDENCY_PINS"])
    observed.update(supersedes_harness_sha256=constants["SUPERSEDES_HARNESS_SHA256"],
                    supersedes_custody_sha256=constants["SUPERSEDES_CUSTODY_SHA256"],
                    supersedes_note_path=constants["SUPERSEDES_NOTE_PATH"])
    observed.update(supersedes_attempt1_writer_record_path=constants["SUPERSEDES_ATTEMPT1_WRITER_RECORD_PATH"],
                    supersedes_attempt1_writer_record_sha256=constants["SUPERSEDES_ATTEMPT1_WRITER_RECORD_SHA256"],
                    supersedes_attempt1_W3_record=constants["SUPERSEDES_ATTEMPT1_W3_RECORD"])
    metadata = dict(writer_sha256=sha(Path(__file__)), created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                    repo_root=str(root), environment=env, pin_checks=checks,
                    launch_authorization=gate, launch_authorization_sha256=gate["pi_record_sha256"], current_launch_started=False,
                    real_data_access=False, store_at_first_launch="EMPTY" if launch == 1 else "EXISTING_ATTEMPT_STORE")
    content = "# rp1-r3 pre-execution custody\n\nOne immutable W-3 record for this actual launch; all earlier records are preserved.\n\n```text\n"
    content += "\n".join("%s = %s" % item for item in observed.items()) + "\n```\n\n```json\n" + json.dumps(metadata, indent=2) + "\n```\n"
    with target.open("x", encoding="ascii", newline="\n") as stream:
        stream.write(content)
    Path(str(target) + ".sha256").write_text(sha(target) + "  " + target.name + "\n", encoding="ascii")
    print(json.dumps(dict(custody=str(target), sha256=sha(target), launch=launch, pin_checks=len(checks))))


if __name__ == "__main__":
    main()
