"""Log small-input test execution under section 5(b), with isolated outputs."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "p_konum_plus/calibration"
P = ROOT / "p_konum_plus/provenance"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def log_record(payload: dict[str, Any]) -> None:
    path = P / "f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md"
    with path.open("a", encoding="utf8", newline="\n") as stream:
        stream.write("\n## Logged outside-W3 small-input execution\n\n```json\n" + json.dumps(payload, indent=2) + "\n```\n")
    Path(str(path) + ".sha256").write_text(sha(path) + "  " + path.name + "\n", encoding="ascii")


def main() -> None:
    quarantine = Path("C:/Users/Neo/Downloads/rp1r2_preflight/2026-10-10_execution01").resolve()
    assert ROOT not in quarantine.parents and ROOT != quarantine
    assert not quarantine.exists(), "REFUSE_EXISTING_PREFLIGHT_OUTPUTS"
    assert not (C / ".rp1-r2_restart_store_2026-10-10").exists()
    quarantine.mkdir(parents=True)
    runner = C / "f3_rp1-r2_small_input_tests_2026-10-10.py"
    harness = C / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    artifacts = [runner, harness, *[C / name for name in (
        "f3_rp1-r2_gate_tools_2026-10-10.py", "f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py",
        "f3_rp1-r2_technical_tests_2026-10-10.py")]]
    metadata = dict(kind="OUTSIDE_W3_SMALL_INPUT_TEST_EXECUTION", execution_id="2026-10-10_execution01",
        code_path=str(runner), code_sha256=sha(runner), harness_path=str(harness), harness_sha256=sha(harness),
        source_hashes={str(path): sha(path) for path in artifacts}, directory=str(ROOT),
        start_utc=dt.datetime.now(dt.timezone.utc).isoformat(), end_utc="NOT OBSERVED (running)",
        stdout=str(quarantine / "stdout.log"), stderr=str(quarantine / "stderr.log"), output_root=str(quarantine),
        store_root=str(quarantine / "small_test_store"), outputs_discarded=False,
        output_disposition="RETAINED_IN_EXTERNAL_QUARANTINE; EXCLUDED_FROM_ALL_DELIVERABLES_AND_ATTEMPT_STORE",
        outside_w3_attempt=True, actual_optimizer_calls=0, real_data_access=False,
        command=[sys.executable, str(runner)], interpreter=sys.executable)
    log_record(metadata)
    environment = dict(os.environ, F3_REPO_ROOT=str(ROOT), F3_RP1R2_PREFLIGHT_ROOT=str(quarantine),
        PYTHONUNBUFFERED="1", PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    with (quarantine / "stdout.log").open("xb") as stdout, (quarantine / "stderr.log").open("xb") as stderr:
        child = subprocess.Popen([sys.executable, str(runner)], cwd=ROOT, env=environment, stdout=stdout, stderr=stderr)
        metadata["pid"] = child.pid
        log_record(dict(kind="PREFLIGHT_PID_OBSERVED", execution_id=metadata["execution_id"], pid=child.pid))
        code = child.wait()
    files = [dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
             for path in sorted(quarantine.rglob("*")) if path.is_file()]
    inventory = quarantine / "retained_output_inventory.json"
    inventory.write_text(json.dumps(files, indent=2) + "\n", encoding="ascii")
    metadata.update(return_code=code, end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        stdout_sha256=sha(quarantine / "stdout.log"), stderr_sha256=sha(quarantine / "stderr.log"),
        retained_output_inventory=str(inventory), retained_output_inventory_sha256=sha(inventory),
        attempt_store_absent=not (C / ".rp1-r2_restart_store_2026-10-10").exists())
    assert metadata["attempt_store_absent"]
    log_record(metadata)
    (quarantine / "execution_record.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="ascii")
    print(json.dumps(dict(return_code=code, quarantine=str(quarantine), pid=child.pid, attempt_store_absent=True)))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
