"""Generate exclusively synthetic Q3 fixtures during an authorized W-3 launch."""
from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
from typing import Any

import numpy as np

FIXTURE_CONFIG = {"seed": 20261010, "rng": "numpy.default_rng / PCG64", "years": [1880, 2025],
                  "names": {"F": ["QA", "QB", "QC"], "M": ["QD", "QE", "QF"]},
                  "count_bounds": [5, 801], "source": "TEST_ONLY_SYNTHETIC"}


def csv_bytes(fields: list[str] | tuple[str, ...], rows: list[dict[str, Any]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("ascii")


def write_fixture(path: Path, data: bytes, sidecar: Path | None = None) -> str:
    """Repeated launches verify existing bytes rather than overwriting fixtures."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        assert path.read_bytes() == data, "SYNTHETIC_FIXTURE_BYTES_CHANGED " + str(path)
    else:
        with path.open("xb") as stream:
            stream.write(data)
    value = hashlib.sha256(data).hexdigest()
    checksum = sidecar or Path(str(path) + ".sha256")
    checksum.parent.mkdir(parents=True, exist_ok=True)
    content = (value + "  " + path.name + "\n").encode("ascii")
    if checksum.exists():
        assert checksum.read_bytes() == content
    else:
        checksum.write_bytes(content)
    return value


def generate(destination: str, fields: tuple[str, ...]) -> dict[str, Any]:
    """The serialization declared here applies only to new synthetic files."""
    root = Path(destination)
    raw = root / "raw"
    rng = np.random.default_rng(FIXTURE_CONFIG["seed"])
    table = []
    for year in range(1880, 2026):
        lines = []
        for sex, names in FIXTURE_CONFIG["names"].items():
            for name in names:
                lines.append("%s,%s,%d\n" % (name, sex, int(rng.integers(5, 801))))
            if year == 1880:
                lines.append("QPART,%s,17\n" % sex)
        filename = "yob%d.txt" % year
        value = write_fixture(raw / filename, "".join(lines).encode("ascii"),
                              root / "checksums/raw" / (filename + ".sha256"))
        table.append((filename, value))
    rows = []
    for sex, names in FIXTURE_CONFIG["names"].items():
        for name in names:
            rows.append(dict(trajectory_id=sex + "_" + name, sex=sex, name=name,
                             year_min="1880", year_max="2025", T="146",
                             source_scope="TEST_ONLY_SYNTHETIC", source_record_status="SYNTHETIC_PUBLISHED",
                             exclusion_reason="", eligibility_rule_id="OD5_FULL_observed_support_1880_2025",
                             trajectory_value_id="OD3_released_record_share_by_year_and_sex",
                             n_observed_years="146", n_missing_total="0", eligible="true"))
    manifest = root / "synthetic_eligible_manifest.csv"
    manifest_hash = write_fixture(manifest, csv_bytes(fields, rows))
    write_fixture(root / "synthetic_input_hash_table.csv",
                  csv_bytes(["filename", "sha256"], [dict(filename=name, sha256=h) for name, h in table]))
    config = dict(FIXTURE_CONFIG, serialization=dict(encoding="ascii", delimiter=",", quoting="csv.QUOTE_MINIMAL",
                                                   line_ending="LF", columns=list(fields)),
                  raw_checksum_location="checksums/raw; excluded from the raw input directory")
    write_fixture(root / "SYNTHETIC_GENERATION_MANIFEST.json",
                  (json.dumps(config, indent=2, sort_keys=True) + "\n").encode("ascii"))
    return dict(raw=str(raw), hash_table=table, eligible_manifest=str(manifest),
                manifest_hash=manifest_hash, manifest_rows=rows)


def write_runtime_custody(destination: str, target: str) -> dict[str, Any]:
    """Hash every new synthetic file without changing any original fixture."""
    root = Path(destination)
    rows = [dict(path=path.as_posix(), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                 bytes=path.stat().st_size)
            for path in sorted(root.rglob("*")) if path.is_file()]
    body = csv_bytes(["path", "sha256", "bytes"], rows)
    # This is a new launch's observed custody table, outside the fixture tree.
    path = Path(target)
    path.write_bytes(body)
    digest = hashlib.sha256(body).hexdigest()
    Path(str(path) + ".sha256").write_text(digest + "  " + path.name + "\n", encoding="ascii")
    return dict(path=target, sha256=digest, rows=len(rows))
