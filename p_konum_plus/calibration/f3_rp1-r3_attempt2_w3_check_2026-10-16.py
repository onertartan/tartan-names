"""D-20 C-5: execute the exact W-3 writer in a metadata-only external control copy."""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    c = root / "p_konum_plus/calibration"
    harness = c / "f3_step2_adequacy_harness_rp1-r3_2026-10-15.py"
    writer = c / "f3_rp1-r3_write_custody_2026-10-15.py"
    tree = ast.parse(harness.read_text(encoding="utf-8"))
    spec = importlib.util.spec_from_file_location("attempt2_actual_writer_constants", writer)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    constants = module.literal_constants(tree)
    assert constants["ATTEMPT_NUMBER"] == 2 and constants["REAL_DATA_MODE"] is False
    assert constants["RP2_DISPATCH_PINS"] == constants["RP3_INCOMING_DISPATCH_PINS"] + constants["RP3_CARRIED_DISPATCH_PINS"]
    source_main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    expected: dict[str, str] = {}
    for node in ast.walk(source_main):
        if not isinstance(node, ast.For) or not isinstance(node.target, ast.Tuple): continue
        if [getattr(t, "id", "") for t in node.target.elts] != ["ipath", "ihash", "iname"]: continue
        if isinstance(node.iter, ast.Name):
            entries = constants[node.iter.id]
        else:
            entries = [[constants[x.id] if isinstance(x, ast.Name) else ast.literal_eval(x) for x in entry.elts]
                       for entry in node.iter.elts]
        for path, pin, _ in entries:
            assert path not in expected or expected[path] == pin
            expected[path] = pin
    expected[constants["SUPERSEDES_ATTEMPT1_WRITER_RECORD_PATH"]] = constants["SUPERSEDES_ATTEMPT1_WRITER_RECORD_SHA256"]
    for name, pin in constants["RP2_DEPENDENCY_PINS"].items():
        expected["p_konum_plus/calibration/" + name] = pin
    expected[harness.relative_to(root).as_posix()] = sha(harness)
    expected[writer.relative_to(root).as_posix()] = sha(writer)
    scratch = out / "metadata_control_copy"
    scratch.mkdir()
    copied = []
    for rel, pin in expected.items():
        assert rel.startswith("p_konum_plus/") and ".." not in Path(rel).parts
        assert not rel.startswith(("p_konum_plus/manifests/", "p_konum_plus/data/")), "REAL_INPUT_COPY_FORBIDDEN"
        source = root / rel
        assert sha(source) == pin, "CONTROL_INPUT_PIN_STOP " + rel
        target = scratch / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream: stream.write(source.read_bytes())
        assert sha(target) == pin
        copied.append(dict(path=rel, sha256=pin))
        check = Path(str(source) + ".sha256")
        if check.is_file():
            target_check = Path(str(target) + ".sha256")
            with target_check.open("xb") as stream: stream.write(check.read_bytes())
    copied_writer = scratch / writer.relative_to(root)
    environment = dict(os.environ, F3_REPO_ROOT=str(scratch), F3_RP1R3_LAUNCH="1", PYTHONDONTWRITEBYTECODE="1",
                       OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    with (out / "actual_writer_stdout.log").open("xb") as stdout, (out / "actual_writer_stderr.log").open("xb") as stderr:
        process = subprocess.run([sys.executable, "-B", str(copied_writer)], cwd=scratch, env=environment, stdout=stdout, stderr=stderr)
    relative_custody = "p_konum_plus/provenance/f3_step2_rp1-r3_preexecution_custody_attempt2_launch1_2026-10-15.md"
    custody = scratch / relative_custody
    parsed: dict[str, Any] = {}
    if custody.exists():
        text = custody.read_text(encoding="ascii")
        metadata = text.split("```json\n", 1)[1].split("\n```", 1)[0]
        parsed = json.loads(metadata)
        for field, value in (("supersedes_attempt1_writer_record_sha256", constants["SUPERSEDES_ATTEMPT1_WRITER_RECORD_SHA256"]),
                             ("supersedes_attempt1_W3_record", "no attempt-1 W-3 record")):
            assert field + " = " + value in text
        assert not parsed["current_launch_started"]
    passed = process.returncode == 0 and bool(parsed) and all(x["expected"] == x["observed"] for x in parsed["pin_checks"])
    assert not (root / relative_custody).exists(), "ACTIVE_W3_MUST_NOT_BE_CREATED"
    assert not (root / constants["RESTART_STORE_DIR"]).exists(), "ACTIVE_ATTEMPT2_STORE_MUST_REMAIN_ABSENT"
    result = dict(passed=passed, writer_return_code=process.returncode, original_writer_sha256=sha(writer),
        control_copy_writer_sha256=sha(copied_writer), harness_sha256=sha(harness),
        copied_control_inputs=copied, pin_checks=parsed.get("pin_checks", []),
        external_test_custody_path=str(custody), external_test_custody_sha256=sha(custody) if custody.exists() else None,
        active_custody_created=False, harness_launched=False, actual_optimizer_calls=0, real_data_access=False,
        output_disposition="EXTERNAL TEST ARTIFACT ONLY; NEVER ACTIVE CUSTODY OR STORE INPUT")
    (out / "W3_check_result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(dict(passed=passed, writer_return_code=process.returncode, pin_checks=len(result["pin_checks"]),
                         active_custody_created=False, harness_launched=False)))
    if not passed: raise SystemExit(2)


if __name__ == "__main__":
    main()
