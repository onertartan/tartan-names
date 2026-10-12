"""Log every authorized W-3 launch; preserve all custody records and log pairs."""
from __future__ import annotations

import datetime as dt
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


def record(path: Path, payload: dict[str, Any]) -> None:
    with path.open("x", encoding="ascii", newline="\n") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
    Path(str(path) + ".sha256").write_text(sha(path) + "  " + path.name + "\n", encoding="ascii")


def main() -> None:
    root = Path(os.environ.get("F3_REPO_ROOT", Path(__file__).resolve().parents[2])).resolve()
    value = os.environ.get("F3_RP1R2_LAUNCH", "")
    assert value.isdecimal() and int(value) > 0, "LAUNCH_REQUIRED"
    number = int(value)
    provenance = root / "p_konum_plus/provenance"
    calibration = root / "p_konum_plus/calibration"
    harness = calibration / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    tree = ast.parse(harness.read_text(encoding="utf8"))
    dependency_node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "RP2_DEPENDENCY_PINS" for t in n.targets))
    helper = calibration / "f3_rp1-r2_gate_tools_2026-10-10.py"
    assert sha(helper) == ast.literal_eval(dependency_node.value)[helper.name]
    helper_spec = importlib.util.spec_from_file_location("rp2_launcher_authorization", helper)
    helper_module = importlib.util.module_from_spec(helper_spec)
    helper_spec.loader.exec_module(helper_module)
    gate = helper_module.authorize_ir1_13(root)
    prefix = "f3_step2_rp1-r2_launch%d" % number
    out = calibration / (prefix + "_stdout_2026-10-10.log")
    err = calibration / (prefix + "_stderr_2026-10-10.log")
    assert not out.exists() and not err.exists(), "REFUSE_EXISTING_LOG_PAIR"
    environment = dict(os.environ, F3_REPO_ROOT=str(root), PYTHONUNBUFFERED="1", PYTHONDONTWRITEBYTECODE="1")
    writer = calibration / "f3_rp1-r2_write_custody_2026-10-10.py"
    writer_start = dt.datetime.now(dt.timezone.utc).isoformat()
    custody = subprocess.run([sys.executable, str(writer)], cwd=root, env=environment, capture_output=True, text=True)
    record(provenance / (prefix + "_w3_writer_2026-10-10.json"),
           dict(code_sha256=sha(writer), directory=str(root), start_utc=writer_start,
                end_utc=dt.datetime.now(dt.timezone.utc).isoformat(), return_code=custody.returncode,
                stdout=custody.stdout, stderr=custody.stderr, kind="EXTERNAL_W3_WRITER"))
    assert custody.returncode == 0, "W3_WRITER_STOP"
    metadata = dict(launch=number, code_path=str(harness), code_sha256=sha(harness), directory=str(root),
                    start_utc=dt.datetime.now(dt.timezone.utc).isoformat(), end_utc="NOT OBSERVED (running)",
                    stdout=str(out), stderr=str(err), output_scope=str(calibration), outputs_discarded=False,
                    outside_w3_attempt=False, real_data_access=False, interpreter=sys.executable, authorization=gate)
    record(provenance / (prefix + "_start_2026-10-10.json"), metadata)
    log = provenance / "f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md"
    with log.open("a", encoding="utf8", newline="\n") as stream:
        stream.write("\n## Launch start (machine-transferred)\n\n```json\n" + json.dumps(metadata, indent=2) + "\n```\n")
    with out.open("xb") as stdout, err.open("xb") as stderr:
        process = subprocess.Popen([sys.executable, str(harness)], cwd=root, env=environment, stdout=stdout, stderr=stderr)
        record(provenance / (prefix + "_pid_2026-10-10.json"), dict(pid=process.pid, launch=number))
        code = process.wait()
    metadata.update(pid=process.pid, return_code=code, end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                    stdout_sha256=sha(out), stderr_sha256=sha(err))
    record(provenance / (prefix + "_end_2026-10-10.json"), metadata)
    with log.open("a", encoding="utf8", newline="\n") as stream:
        stream.write("\n## Launch end (machine-transferred)\n\n```json\n" + json.dumps(metadata, indent=2) + "\n```\n")
    for path in (out, err, log):
        Path(str(path) + ".sha256").write_text(sha(path) + "  " + path.name + "\n", encoding="ascii")
    print(json.dumps(metadata))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
