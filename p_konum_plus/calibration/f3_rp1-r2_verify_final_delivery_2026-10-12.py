"""Verify the explicit delivery allowlist and optionally stage exact bytes."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / 'p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def allowed(path: str) -> bool:
    p = Path(path)
    return p.parts[0]=='p_konum_plus' and p.suffix not in ('.pkl','.zip') and 'rp1r1_audit' not in path.lower() and not any(x.startswith('.') and 'restart_store' in x for x in p.parts) and 'package_' not in p.name


def verify(stage: bool, check_index: bool) -> None:
    with T.open(encoding='utf8',newline='') as stream:
        rows=list(csv.DictReader(stream))
    selected: set[str] = set()
    for row in rows:
        path=ROOT/row['path']; side=ROOT/row['sidecar']
        assert sha(path)==row['sha256'] and path.stat().st_size==int(row['bytes'])
        assert sha(side)==row['sidecar_sha256']
        assert side.read_text(encoding='ascii')==row['sha256']+'  '+path.name+'\n'
        selected.update((row['path'],row['sidecar']))
    selected.update((T.relative_to(ROOT).as_posix(),Path(str(T)+'.sha256').relative_to(ROOT).as_posix()))
    assert Path(str(T)+'.sha256').read_text().split()[0]==sha(T)
    assert all(allowed(path) for path in selected), 'FORBIDDEN_DELIVERY_PATH'
    fixture_root=ROOT/'p_konum_plus/calibration/f3_step2_rp1-r2_f1_synth_fixtures_2026-10-10'
    assert all(p.relative_to(ROOT).as_posix() in selected for p in fixture_root.rglob('*') if p.is_file())
    result=json.loads((ROOT/'p_konum_plus/calibration/f3_step2_results_rp1-r2_2026-10-10.json').read_text())
    final_map=ROOT/'p_konum_plus/provenance/f3_realdata_prep_rp1-r2_requirement_map_final_2026-10-12.csv'
    with final_map.open(encoding='utf8',newline='') as stream:
        for row in csv.DictReader(stream):
            if row['requirement'].startswith('Q'):
                observed=json.loads(row['final_launch_result']); q=row['requirement']
                assert observed['test']==result['rp1_r2_technical_tests'][q] and observed['registry']==result['tests_run']['T-RP1R2-'+q]
    ledger=json.loads((ROOT/'p_konum_plus/provenance/f3_realdata_prep_rp1-r2_ledger_final_2026-10-12.json').read_text())
    ir13=next(x for x in ledger['items'] if x['id']=='IR1-13')
    assert ir13['status']=='OPEN' and ir13['classification']=='B' and 'D-14' in ir13['evidence']
    report=(ROOT/'p_konum_plus/provenance/f3_realdata_prep_rp1-r2_report_2026-10-12.md').read_text()
    assert 'rp1-r2_status = **'+result['end_state']['rp1_r2_status']+'**' in report
    assert not subprocess.check_output(['git','diff','--name-only'],cwd=ROOT).strip()
    if stage:
        assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT).strip(), 'PREEXISTING_STAGED_FILES'
        with tempfile.NamedTemporaryFile(prefix='rp1r2_stage_',suffix='.paths',delete=False) as stream:
            stream.write(b'\0'.join(p.encode('utf8') for p in sorted(selected))+b'\0')
            pathspec=stream.name
        try:
            subprocess.run(['git','add','--pathspec-from-file='+pathspec,'--pathspec-file-nul'],cwd=ROOT,check=True)
        finally:
            Path(pathspec).unlink()
        check_index=True
    if check_index:
        records=subprocess.check_output(['git','ls-files','--stage','-z'],cwd=ROOT).split(b'\0')
        index={}
        for record in records:
            if record:
                meta,path=record.split(b'\t',1)
                index[path.decode('utf8')]=meta.split()[1].decode('ascii')
        staged=set(subprocess.check_output(['git','diff','--cached','--name-only','-z'],cwd=ROOT).decode('utf8').split('\0'))-{''}
        assert staged==selected, 'STAGED_SET_DIFFERS_FROM_ALLOWLIST'
        for path in selected:
            raw=(ROOT/path).read_bytes()
            expected=hashlib.sha1(b'blob '+str(len(raw)).encode('ascii')+b'\0'+raw).hexdigest()
            assert index[path]==expected,'GIT_BYTE_CONVERSION '+path
        statuses=subprocess.check_output(['git','diff','--cached','--name-status'],cwd=ROOT).decode('utf8').splitlines()
        assert all(line.startswith('A\t') for line in statuses),'PREVIOUS_PACKAGE_FILE_CHANGED'
    print(json.dumps(dict(payload_rows=len(rows),selected_files=len(selected),staged=stage or check_index,
                         rp1_r2_status=result['end_state']['rp1_r2_status'],hashes_verified=True,previous_package_changes=0)))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--stage',action='store_true')
    parser.add_argument('--check-index',action='store_true')
    args=parser.parse_args()
    verify(args.stage,args.check_index)
