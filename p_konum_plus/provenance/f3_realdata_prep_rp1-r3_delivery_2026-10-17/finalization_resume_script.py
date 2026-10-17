"""Resume documentary finalization after resolving the manifest-path alias."""
from __future__ import annotations
import ast
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import zipfile

ROOT = Path('G:/PycharmProjects/pkp-worktree')
D = ROOT / 'p_konum_plus/provenance/f3_realdata_prep_rp1-r3_delivery_2026-10-17'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
rel = lambda p: p.relative_to(ROOT).as_posix()

def write(p: Path, text: str) -> None:
    with p.open('x', encoding='utf8', newline='\n') as f:
        f.write(text)
    with Path(str(p) + '.sha256').open('x', encoding='ascii') as f:
        f.write(sha(p) + '  ' + p.name + '\n')

def main() -> None:
    write(D / 'documentary_finalization_record.json', json.dumps(dict(
        previous_transfer='final_checks_transfer_script.py',
        event='Documentary finalizer stopped before the final transmission/ZIP because MANIFEST_PATH is an AST Name alias, not a literal. This resume resolves only literal assignments and aliases without importing or changing the harness.',
        source_code_changed=False, run_outputs_changed=False), indent=2) + '\n')
    shutil.copyfile(Path(__file__), D / 'finalization_resume_script.py')
    with Path(str(D / 'finalization_resume_script.py') + '.sha256').open('x', encoding='ascii') as f:
        f.write(sha(D / 'finalization_resume_script.py') + '  finalization_resume_script.py\n')
    with (D / 'transmission_list.csv').open(encoding='utf8') as f:
        oldrows = list(csv.DictReader(f))
    payloads = {ROOT / x['path'] for x in oldrows}
    constants = {}
    h = ROOT / 'p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py'
    for n in ast.parse(h.read_text(encoding='utf8')).body:
        if not isinstance(n, ast.Assign) or len(n.targets) != 1 or not isinstance(n.targets[0], ast.Name):
            continue
        try:
            constants[n.targets[0].id] = ast.literal_eval(n.value)
        except (ValueError, TypeError):
            if isinstance(n.value, ast.Name) and n.value.id in constants:
                constants[n.targets[0].id] = constants[n.value.id]
    payloads.update(ROOT / constants[k] for k in ['GEN_PATH', 'MANIFEST_PATH'])
    assert sha(ROOT / constants['GEN_PATH']) == constants['GEN_HASH_REUSED']
    assert sha(ROOT / constants['MANIFEST_PATH']) == constants['MANIFEST_HASH_REUSED']
    payloads.update(p for p in D.rglob('*') if p.is_file() and 'delivery_checksums' not in p.parts and p.suffix != '.sha256')
    old = {x['path']: x for x in oldrows}
    rows = []
    for f in sorted(payloads):
        name = rel(f)
        if name in old:
            row = old[name]
            assert sha(f) == row['sha256'] and sha(ROOT / row['sidecar_path']) == row['sidecar_sha256']
            rows.append(row)
            continue
        check = Path(str(f) + '.sha256')
        if not check.exists() or check.read_text(encoding='utf8').split()[0] != sha(f):
            check = D / 'delivery_checksums' / (name + '.sha256')
            check.parent.mkdir(parents=True, exist_ok=True)
            with check.open('x', encoding='ascii') as stream:
                stream.write(sha(f) + '  ' + f.name + '\n')
        rows.append(dict(path=name, sha256=sha(f), bytes=f.stat().st_size, sidecar_path=rel(check), sidecar_sha256=sha(check)))
    assert not subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT).strip()
    before = json.loads((D / 'preserved_source_inventory.json').read_bytes())
    assert all(sha(ROOT / x['path']) == x['sha256'] for x in before)
    final = D / 'transmission_list_final.csv'
    with final.open('x', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n');w.writeheader();w.writerows(rows)
    with Path(str(final) + '.sha256').open('x', encoding='ascii') as f:
        f.write(sha(final) + '  ' + final.name + '\n')
    files = {ROOT / row[k] for row in rows for k in ['path', 'sidecar_path']}
    files.update([final, Path(str(final) + '.sha256')])
    zpath = Path('C:/Users/Neo/Downloads/f3_realdata_prep_rp1-r3_delivery_FINAL_2026-10-17.zip')
    with zipfile.ZipFile(zpath, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in sorted(files):
            assert f.suffix not in ['.pkl', '.zip', '.pyc'] and '.rp1-r3_attempt' not in rel(f)
            z.write(f, rel(f))
    with Path(str(zpath) + '.sha256').open('x', encoding='ascii') as f:
        f.write(sha(zpath) + '  ' + zpath.name + '\n')
    with zipfile.ZipFile(zpath) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == {rel(f) for f in files}
        for row in rows:
            assert hashlib.sha256(z.read(row['path'])).hexdigest() == row['sha256']
            assert hashlib.sha256(z.read(row['sidecar_path'])).hexdigest() == row['sidecar_sha256']
    fix = json.loads((D / 'rerun_overwrite_inventory_r1.json').read_bytes())['observed_fixture_files']
    assert {r['path'] for r in fix} <= {r['path'] for r in rows}
    assert all(sha(ROOT / x['path']) == x['sha256'] for x in before)
    status = json.loads((D / 'executor_observations.json').read_bytes())['rp1_r3_status']
    text = '# rp1-r3 teslim paketi\n\nPaket tamamlandi. rp1-r3_status = `' + status + '`. Bagimsiz denetim bekleniyor; yeni kapanis karari verilmedi. Kod ve kosu ciktilari degistirilmedi. Commit/push yapilmadi.\n\n'
    for label, p in [('ZIP', zpath), ('ZIP sidecar', Path(str(zpath) + '.sha256')), ('Iletim listesi', final), ('Iletim listesi sidecar', Path(str(final) + '.sha256')), ('Rapor', D / 'executor_report_final.md'), ('Gereksinim haritasi', D / 'requirement_map_final.csv')]:
        text += '- [' + label + '](' + p.as_posix() + ')\n'
    text += '\nZIP SHA256: `' + sha(zpath) + '`\n\nIletim listesi SHA256: `' + sha(final) + '`\n\n'
    text += 'Iletim satiri: `' + str(len(rows)) + '`; ZIP girdisi: `' + str(len(files)) + '`. Tum icerik ve sidecar hashleri ZIP baytlarindan dogrulandi.\n'
    response = Path('C:/Users/Neo/Downloads/f3_realdata_prep_rp1-r3_teslim_yaniti_2026-10-17.md')
    write(response, text)
    print(json.dumps(dict(zip=str(zpath), zip_sha256=sha(zpath), transmission=rel(final), transmission_sha256=sha(final),
        payloads=len(rows), archive_entries=len(files), response=str(response), report=rel(D / 'executor_report_final.md'), status=status)), flush=True)

if __name__ == '__main__':
    main()
