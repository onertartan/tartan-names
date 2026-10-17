"""Record the isolated comparator execution under instruction section 5(b)."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path('G:/PycharmProjects/pkp-worktree').resolve()
OUT = Path('C:/Users/Neo/Downloads/rp1r2_preflight/2026-10-11_comparator_execution01').resolve()
LOG = ROOT / 'p_konum_plus/provenance/f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md'
H = ROOT / 'p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def append(payload: dict[str, Any]) -> None:
    with LOG.open('a', encoding='utf8', newline='\n') as stream:
        stream.write('\n## Section 5(b): isolated attempt-1 comparator execution\n\n```json\n' + json.dumps(payload, indent=2, ensure_ascii=True) + '\n```\n')
    Path(str(LOG) + '.sha256').write_text(sha(LOG) + '  ' + LOG.name + '\n', encoding='ascii')


def main() -> None:
    assert not OUT.exists() and ROOT not in OUT.parents
    assert not (ROOT / 'p_konum_plus/calibration/.rp1-r2_restart_store_2026-10-10').exists()
    runner = Path(__file__).with_name('compare_attempt1.py')
    OUT.mkdir(parents=True)
    for path in (runner, Path(__file__)):
        Path(str(path) + '.sha256').write_text(sha(path) + '  ' + path.name + '\n', encoding='ascii')
    metadata: dict[str, Any] = dict(kind='OUTSIDE_W3_COMPARATOR_EXCERPT_EXECUTION', execution_id='2026-10-11_comparator_execution01',
        code_path=str(runner), code_sha256=sha(runner), wrapper_sha256=sha(Path(__file__)), harness_path=str(H), harness_sha256=sha(H),
        directory=str(ROOT), start_utc=dt.datetime.now(dt.timezone.utc).isoformat(), end_utc='NOT OBSERVED (running)',
        command=[sys.executable,str(runner)], interpreter=sys.executable,
        stdout=str(OUT / 'stdout.log'), stderr=str(OUT / 'stderr.log'), output_root=str(OUT),
        outputs_discarded=False, output_disposition='RETAINED_IN_EXTERNAL_QUARANTINE; EXCLUDED_FROM_ALL_DELIVERABLES_AND_ATTEMPT_STORES',
        outside_w3_attempt=True, actual_optimizer_calls=0, store_access='NONE', real_data_access=False,
        scope='Exact test_evidence and telemetry comparator excerpts only; attempt-1 results JSON is absent, so results/S recomparison cannot be executed')
    append(metadata)
    environment = dict(os.environ, F3_REPO_ROOT=str(ROOT), F3_COMPARATOR_OUTPUT_ROOT=str(OUT),
        PYTHONUNBUFFERED='1', PYTHONDONTWRITEBYTECODE='1', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
    with (OUT / 'stdout.log').open('xb') as stdout, (OUT / 'stderr.log').open('xb') as stderr:
        child = subprocess.Popen([sys.executable,str(runner)], cwd=ROOT, env=environment, stdout=stdout, stderr=stderr)
        metadata['pid'] = child.pid
        append(dict(execution_id=metadata['execution_id'], kind='OUTSIDE_W3_CHILD_PID', pid=child.pid))
        code = child.wait()
    files = [dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size) for path in sorted(OUT.iterdir()) if path.is_file()]
    inventory = OUT / 'retained_output_inventory.json'
    inventory.write_text(json.dumps(files, indent=2, ensure_ascii=True) + '\n', encoding='ascii')
    metadata.update(end_utc=dt.datetime.now(dt.timezone.utc).isoformat(), return_code=code,
        stdout_sha256=sha(OUT / 'stdout.log'), stderr_sha256=sha(OUT / 'stderr.log'),
        retained_output_inventory=str(inventory), retained_output_inventory_sha256=sha(inventory),
        attempt_store_absent=not (ROOT / 'p_konum_plus/calibration/.rp1-r2_restart_store_2026-10-10').exists())
    if (OUT / 'executed_source_excerpts.txt').exists():
        metadata['executed_excerpt_sha256'] = sha(OUT / 'executed_source_excerpts.txt')
    append(metadata)
    (OUT / 'execution_record.json').write_text(json.dumps(metadata, indent=2, ensure_ascii=True) + '\n', encoding='ascii')
    print(json.dumps(dict(return_code=code, pid=child.pid, output_root=str(OUT), attempt_store_absent=metadata['attempt_store_absent'])))
    raise SystemExit(code)


if __name__ == '__main__':
    main()
