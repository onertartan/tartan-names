"""Record a standalone preflight without allowing its outputs into an attempt."""
from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    code = Path(sys.argv[1]).resolve()
    execution_id = sys.argv[2]
    out = Path.home() / "Downloads/rp1r3_preflight" / execution_id
    out.mkdir(parents=True, exist_ok=False)
    log = root / "p_konum_plus/provenance/f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md"

    def record(value: dict[str, Any]) -> None:
        with log.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write("\n```json\n" + json.dumps(value, indent=2, ensure_ascii=True) + "\n```\n")
        Path(str(log) + ".sha256").write_text(sha(log) + "  " + log.name + "\n", encoding="ascii")

    start = dict(event="OUTSIDE_W3_START", execution_id=execution_id,
        time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        code_path=str(code), code_sha256=sha(code), wrapper_path=str(Path(__file__).resolve()),
        wrapper_sha256=sha(Path(__file__)), directory=str(root), output_root=str(out),
        command=[sys.executable, "-B", str(code), str(root), str(out)],
        output_disposition="RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
        inputs_scope="Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
        actual_optimizer_calls=0, store_access=False, real_data_access=False)
    record(start)
    with (out / "stdout.log").open("wb") as stdout, (out / "stderr.log").open("wb") as stderr:
        process = subprocess.run(start["command"], cwd=root, stdout=stdout, stderr=stderr)
    files = [{"path": str(p), "sha256": sha(p), "bytes": p.stat().st_size}
             for p in sorted(out.iterdir()) if p.is_file()]
    finish = dict(event="OUTSIDE_W3_END", execution_id=execution_id,
        time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        returncode=process.returncode, retained_outputs=files,
        output_disposition=start["output_disposition"], actual_optimizer_calls=0,
        store_access=False, real_data_access=False)
    record(finish)
    (out / "execution_record.json").write_text(json.dumps(dict(start=start, end=finish), indent=2) + "\n", encoding="ascii")
    print(json.dumps(finish))
    raise SystemExit(process.returncode)


if __name__ == "__main__":
    main()
