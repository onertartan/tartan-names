"""Execute the same historical comparator with a larger Python regex cache."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import re


def main() -> None:
    path = Path(__file__).with_name("f3_rp1-r3_historical_comparison_2026-10-15.py")
    spec = importlib.util.spec_from_file_location("unchanged_historical_comparison", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Only the standard-library cache capacity changes. Pattern construction,
    # matching, gate logic, declarations, input documents and comparisons are
    # the same code. Avoid recompiling the same declarations for every leaf.
    re._MAXCACHE = 16384
    module.main()


if __name__ == "__main__":
    main()
