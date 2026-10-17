"""D-20 C-5: rerun the existing mandatory RRS block without importing the harness."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


def main() -> None:
    root, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    c = root / "p_konum_plus/calibration"
    harness = c / "f3_step2_adequacy_harness_rp1-r3_2026-10-15.py"
    parent = c / "f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    tests = c / "f3_rp1-r3_technical_tests_2026-10-15.py"
    spec = importlib.util.spec_from_file_location("attempt2_existing_rrs_block", tests)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.rrs_cases(harness.read_bytes().decode("utf-8"), parent.read_bytes().decode("utf-8"))
    record = dict(test_id="T-RP1R3-RRS-UNCHANGED", test=result,
        inputs={str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (harness, parent, tests)},
        scope="Existing positive and constructed negative only; no harness import/main, optimizer or store",
        real_data_access=False)
    (out / "RRS_result.json").write_text(json.dumps(record, indent=2) + "\n", encoding="ascii")
    print(json.dumps(dict(test_id=record["test_id"], passed=result["pass_"], cases=len(result["cases"]))))
    if not result["pass_"]: raise SystemExit(2)


if __name__ == "__main__":
    main()
