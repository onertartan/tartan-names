"""Add actual patch-application evidence and finish the documentary delivery manifest."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import zipfile

ROOT = Path('G:/PycharmProjects/pkp-worktree')
D = ROOT / 'p_konum_plus/provenance/f3_realdata_prep_rp1-r3_delivery_2026-10-17'


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def write(p: Path, s: str) -> None:
    with p.open('x', encoding='utf8', newline='\n') as f:
        f.write(s)
    side(p)


def side(p: Path) -> Path:
    s = Path(str(p) + '.sha256')
    with s.open('x', encoding='ascii') as f:
        f.write(sha(p) + '  ' + p.name + '\n')
    return s


def table(p: Path, rows: list[dict]) -> None:
    with p.open('x', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    side(p)


def main() -> None:
    source = Path('C:/Users/Neo/Downloads/rp1r3_LF_patch_verification_34uj630a/verification.json')
    verification = json.loads(source.read_bytes())
    assert all(x['return_code'] == 0 and x['target_hash_match'] for x in verification['checks'])
    write(D / 'IR1-16/patch_application_verification.json', json.dumps(verification, indent=2) + '\n')
    write(D / 'IR1-16/PATCH_APPLICATION.md', '# Cross-version diff application\n\nThe patches compare UTF-8 source lines with LF line endings. The executor targets are LF; a Windows checkout of the historical parent can be CRLF. The original files and approved source bytes were never changed.\n\nFor each patch, create a disposable copy of the baseline under the target relative path named in diff_custody.json. Convert CRLF to LF only in that disposable copy, then run:\n\n```text\ngit -c core.autocrlf=false apply --unidiff-zero --whitespace=nowarn -p0 <patch>\n```\n\nThe recorded actual application checks require the resulting byte SHA256 to equal the approved target hash. All recorded checks passed. Context-zero patches require --unidiff-zero. Initial checks with historical bytes placed only under the baseline filename failed because git apply chooses the target filename; a later check with Windows autocrlf produced CRLF output. Those checks changed disposable copies only. The explicit LF procedure above produced the exact approved bytes. The label tables partition each mixed hunk into non-overlapping old/new line intervals, each with one originating-package label.\n')

    with (D / 'requirement_map.csv').open(encoding='utf8') as f:
        req = list(csv.DictReader(f))
    for name, path, method in [('IR1-14', D / 'executor_report.md', 'Executor verification wording; no independent audit or new closure claimed'),
                               ('IR1-15', D / 'executor_observations.json', 'Counts and hashes transferred from result files and verified bytes'),
                               ('IR1-17', D / 'ledger_delivery.json', 'All carried ledger rows retained with source attribution; no new closure'),
                               ('IR1-19', ROOT / 'p_konum_plus/provenance/f3_realdata_prep_rp1-r3_runtime_fixture_custody_attempt2_launch1_2026-10-15.csv', 'Actual recursive runtime fixture inventory rehashed and compared to the delivered tree')]:
        req.append(dict(requirement=name, code_or_record=rel(path), positive='', negative='', verification=method,
                        result_source='', ran='', passed='', cases='', evidence_sha256=sha(path), status='IMPLEMENTED_PENDING_VERIFICATION'))
    table(D / 'requirement_map_final.csv', req)

    report = (D / 'executor_report.md').read_text(encoding='utf8')
    report += '\n## Son iletim kayitlari\n\nGuncel iletim otoritesi transmission_list_final.csv; gereksinim haritasi requirement_map_final.csv dosyasidir. Ilk olusturulan transmission_list.csv ve requirement_map.csv ara paketleme kayitlari olarak korunmustur. Diff uygulamasinin gercek komut ve sonuc kaydi IR1-16/patch_application_verification.json dosyasindadir; Windows CRLF/LF kullanim adimlari IR1-16/PATCH_APPLICATION.md icindedir. Bu adimlar yalniz denetciye ait gecici kopyalarda uygulanir.\n'
    write(D / 'executor_report_final.md', report)
    shutil.copyfile(Path(__file__), D / 'final_checks_transfer_script.py')
    side(D / 'final_checks_transfer_script.py')
    with (D / 'transmission_list.csv').open(encoding='utf8') as f:
        oldrows = list(csv.DictReader(f))
    payloads = {ROOT / x['path'] for x in oldrows}
    # Carry the pinned synthetic generator/manifest as bytes, alongside the parent-checkout requirement.
    h = ROOT / 'p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py'
    for node in ast.parse(h.read_text(encoding='utf8')).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ('GEN_PATH', 'MANIFEST_PATH'):
            payloads.add(ROOT / ast.literal_eval(node.value))
    payloads.update(p for p in D.rglob('*') if p.is_file() and 'delivery_checksums' not in p.parts and p.suffix != '.sha256')
    final_list = D / 'transmission_list_final.csv'
    assert final_list not in payloads
    # The initial list already carries the full runtime tree, including fixture checksum files.
    existing_rows = {x['path']: x for x in oldrows}
    rows = []
    for f in sorted(payloads):
        name = rel(f)
        if name in existing_rows:
            row = existing_rows[name]
            assert sha(f) == row['sha256']
            assert sha(ROOT / row['sidecar_path']) == row['sidecar_sha256']
            rows.append(row)
            continue
        check = Path(str(f) + '.sha256')
        if not check.exists() or check.read_text(encoding='utf8').split()[0] != sha(f):
            check = D / 'delivery_checksums' / (rel(f) + '.sha256')
            check.parent.mkdir(parents=True, exist_ok=True)
            with check.open('x', encoding='ascii') as stream:
                stream.write(sha(f) + '  ' + f.name + '\n')
        rows.append(dict(path=name, sha256=sha(f), bytes=f.stat().st_size, sidecar_path=rel(check), sidecar_sha256=sha(check)))
    assert not subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT).strip()
    before = json.loads((D / 'preserved_source_inventory.json').read_bytes())
    assert all(sha(ROOT / x['path']) == x['sha256'] for x in before)
    table(final_list, rows)
    archive_files = {ROOT / r[k] for r in rows for k in ['path', 'sidecar_path']}
    archive_files.update([final_list, Path(str(final_list) + '.sha256')])
    zpath = Path('C:/Users/Neo/Downloads/f3_realdata_prep_rp1-r3_delivery_FINAL_2026-10-17.zip')
    with zipfile.ZipFile(zpath, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in sorted(archive_files):
            assert f.suffix not in ('.pkl', '.zip', '.pyc') and '.rp1-r3_attempt' not in rel(f)
            z.write(f, rel(f))
    side(zpath)
    with zipfile.ZipFile(zpath) as z:
        assert z.testzip() is None
        for r in rows:
            assert hashlib.sha256(z.read(r['path'])).hexdigest() == r['sha256']
            assert hashlib.sha256(z.read(r['sidecar_path'])).hexdigest() == r['sidecar_sha256']
        assert set(z.namelist()) == {rel(f) for f in archive_files}
    fixture_rows = json.loads((D / 'rerun_overwrite_inventory_r1.json').read_bytes())['observed_fixture_files']
    assert {x['path'] for x in fixture_rows} <= {r['path'] for r in rows}
    status = json.loads((D / 'executor_observations.json').read_bytes())['rp1_r3_status']
    response = D / 'TESLIM_YANITI.md'
    text = '# rp1-r3 teslim paketi\n\nPaket tamamlandi. rp1-r3_status = `' + status + '`. Bagimsiz denetim bekleniyor; yeni kapanis karari verilmedi. Kod ve kosu ciktilari degistirilmedi. Commit/push yapilmadi.\n\n'
    for label, p in [('ZIP', zpath), ('ZIP sidecar', Path(str(zpath) + '.sha256')), ('Iletim listesi', final_list), ('Iletim listesi sidecar', Path(str(final_list) + '.sha256')), ('Rapor', D / 'executor_report_final.md'), ('Gereksinim haritasi', D / 'requirement_map_final.csv')]:
        text += '- [' + label + '](' + p.as_posix() + ')\n'
    text += '\nZIP SHA256: `' + sha(zpath) + '`\n\nIletim listesi SHA256: `' + sha(final_list) + '`\n\n'
    text += 'Iletim satiri: `' + str(len(rows)) + '`; ZIP girdisi: `' + str(len(archive_files)) + '`. Tum icerik ve sidecar hashleri ZIP baytlarindan dogrulandi.\n'
    # Response is outside the archived delivery to avoid recursive archive hashing.
    response = Path('C:/Users/Neo/Downloads/f3_realdata_prep_rp1-r3_teslim_yaniti_2026-10-17.md')
    write(response, text)
    print(json.dumps(dict(zip=str(zpath), zip_sha256=sha(zpath), transmission=rel(final_list), transmission_sha256=sha(final_list),
        payloads=len(rows), archive_entries=len(archive_files), response=str(response), report=rel(D / 'executor_report_final.md'), status=status), ensure_ascii=True), flush=True)


if __name__ == '__main__':
    main()
