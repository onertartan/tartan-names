# p_konum_plus — rp1-r2 — PI evaluation of the AUDITOR-SCOPE-01 scope (D-16, D-15 §2 B-3) — 2026-10-12

> Child of D-15. Governed by D-11 r1 §5 and Ek-1 r1. Prepared by Claude (Claude Code cloud session) at the PI's
> request. The record is the PI's; every value may be changed before signature, and the sidecar is then
> recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-12 (§6); decision = 2 (C).**

```text
record                = f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md   (D-16)
draft                 = …_scope_evaluation_pi_decision_record_DRAFT_2026-10-12.md
                        deb6eeb89822d1532d0c6857b2bc9c5d109ec98a52afe54cbc2e6e053e69fd84 ; changes in §9
status                = SIGNED (PI approval, 2026-10-12; §6)
parent                = D-15 f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md  278532bf… (decision B)
subject               = the evaluation D-15 §2 B-3 requires: which content could have reached the stopped audit session,
                        its class under protocol §5, the consequence under protocol §9, and whether the repeated
                        audit opens
what_this_record_is_not = not a finding on the rp1-r2 package; not a closure of any ledger item; not a binding; not
                        QUALIFIED; not a real-data authorization; not a change to the audit instruction (25eb0e16…)
                        or to its pass criterion
```

## 1. Evidence (B-1 and B-2 of D-15)

```text
(1) B-1a, the argv test — run by the PI in Windows PowerShell on the machine of the stopped audit, 2026-10-12;
    output as relayed by the PI, verbatim:
      PS G:\> $PSVersionTable.PSVersion

      Major  Minor  Build  Revision
      -----  -----  -----  --------
      5      1      19041  6456

      PS G:\> python -c "import sys; print(sys.argv[1:])" -n 'write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY' 'ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
      ['-n', 'write_text|write_bytes|\\.open\\([wax]|to_csv|dump\\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py']
    reading: two arguments; the path is inside the pattern, so the program receives no path. This is the result
    the drafter's simulation predicted (D-15 §7). Python prints backslashes doubled; the pattern itself has
    single backslashes. Effective pattern E = the second element
(2) B-1b, the stopped session's answer, relayed by the PI, verbatim:
      Windows PowerShell. Aynı araç üzerinden şimdi doğrulanan sürüm: 5.1.19041.6456. Olay çağrısında sürüm ayrıca kaydedilmedi.
      Araç çağrısının taşıdığı komut metni, aynen:
      Get-Content -LiteralPath 'ref\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py' -Encoding UTF8 -TotalCount 320
      rg -n 'write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY' 'ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'

      Elimde kalan, kesilmiş araç çıktısı parçalarındaki yollar ve satır numaraları:
      ref\p_konum_plus\prompts\f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md:852
      ref\p_konum_plus\prompts\f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md:328,334,336,345,356,391,412,415,487,491,534,885,895,896,935,963,970,1679,1737,2132
      ref\p_konum_plus\prompts\f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md:1590,1609,1610,1652,1668,1669,1670,1671,1691,1729,1756,1803,1825,1849,1852,1897,1994,1995,2099,2130,2148,2257,2275,2396,2400,2418,2437,2452,2454,2464,2493,2537
      ref\p_konum_plus\manifests\f1_input_hash_table_2026-08-28.csv:207,208,209,210,211,212,213,214,215,216,217,218
      run\p_konum_plus\quarantine\f3_step2_rp1-r2_attempt1_2026-10-11\calibration\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:113,168,215
      ref\notebooks\2-web-scraping-yok-atlas.ipynb:168
      ref\modules\experimental\toy_datasets.py:181
      ref\modules\experimental\run_driver.py:625,653,679
    reading: the stopped session used the same shell and version as the test of (1), so (1) applies to the incident
    call. The session's working directory was G:\PycharmProjects\rp1r2_audit (audit record f3f24b6a…), so rg
    searched that directory recursively: both clones and the session's own files beside them
(3) B-2, count-only checks over the whole commit, run by the PI in Git Bash on 2026-10-12 (commands as relayed;
    output written to files, uploaded by the PI; full effective-pattern list in §8):
      git -C G:/PycharmProjects/rp1r2_audit/ref grep -c -E '<E>' 25c7d51 > G:/PycharmProjects/b2_effective_counts.txt
      git -C G:/PycharmProjects/rp1r2_audit/ref grep -c -E '<intended pattern>' 25c7d51 > G:/PycharmProjects/b2_intended_counts.txt
    effective (E): 67 files, 579 matching lines ; intended: 69 files, 600 lines. The two extra files of the intended
    pattern are the two stdout logs p_konum_plus/calibration/f3_step2_rp1-r2_attempt2_launch1_stdout_2026-10-10.log
    and p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration/f3_step2_rp1-r2_launch1_stdout_2026-10-10.log.
    A second upload under the effective file's name was empty (0 bytes); it is not used (§7)
(4) drafter's checks on the delivered commit (commands and output in §7; no line content printed):
    (a) every line number the stopped session reported, in the seven files other than the input hash table,
        matches E. In toy_datasets.py the intended pattern would also match line 180, E matches only 181, and
        the session reported 181 only — consistent with E being the pattern in effect
    (b) in the four notebooks of the list, every line matching E lies in the "source" field of a code cell; none
        in a cell output
    (c) the four binary files of the list (two .pyc under __pycache__/, which .gitignore excludes, and two .zip
        archives under temp/eps/) contain NUL bytes. By rg's documented defaults, ignored files are not searched
        and binary files found during a recursive search are not printed as text lines. rg's actual handling in
        the incident call is NOT OBSERVED; at most, matching bytes of compressed or compiled files could have been
        printed, which carry no readable data
(5) not covered: files in G:\PycharmProjects\rp1r2_audit outside the two clones (the session's own clone
    verification record and audit_support\ files written before the search). They are the auditor's own work
    files; their content is not established by B-2
```

## 2. Evaluation (the drafter's proposal — NOT adopted by the PI; open points in §3a)

```text
content that could have reached the stopped session = lines matching E in the 67 files of §8, further limited
by the tool's output truncation; files without a matching line were read by the rg process but none of their
content was printed to the session

class (protocol §5)                       files  lines  in the list
p_konum_plus code and records               51    528  harnesses (current, earlier, quarantined), launch / custody
                                                         scripts, diffs, audit records, attempt log — package
                                                         material the auditor reads anyway
F1 input hash table (F1 inventory)            1     12  lines 207–218, the lines the stopped auditor reported;
                                                         non-hash columns — a breach of audit instruction §0's
                                                         hash-column-only rule. The table lists input files and
                                                         their hashes: it is the custody list through which raw
                                                         SSA data (EV-01, allowed before F12, "only via the
                                                         frozen F1 inventory") is used, and holds no trajectory
                                                         value and no outcome. (D-15 §2 (a) states this more
                                                         briefly)
application code outside p_konum_plus         7     15  clustering/, modules/experimental/, viz/plotters/, three
                                                         plotting scripts under results/
notebook source cells                         4     20  notebooks/ — code lines only (§1 (4) (b))
binary (compiled / compressed)                4      4  no readable content (§1 (4) (c))

absent from the list: every file under data/ (which holds the real SSA files data/raw/names-usa/…), the F1
eligible manifest, every result file under results/ and every other data file. No file of the list holds
algorithm × CVI outcomes (EV-17) or legacy outcome results (EV-13 … EV-16)

consequence (protocol §9): no STOP-15 (no early algorithm × CVI outcome exposure) and no STOP-16 (no legacy or
premature outcome information, and no calibration pin set by the stopped session). What remains is the breach
of the audit instruction's reading rule for the 12 inventory lines, logged by D-15 and this record
```

## 3. Decision — the PI chose 2 (§6); option 1 is kept as presented

```text
1  SUSPICION SETTLED; THE REPEATED AUDIT OPENS                                              [recommended]
   - on §1 and §2, the PI finds the firewall suspicion of AUDITOR-SCOPE-01 settled: no real SSA content, no F1
     eligible-manifest content and no outcome content could reach the stopped session; the 12 input-hash-table
     lines are a logged breach of the audit reading rule, with no consequence under protocol §9
   - this record opens the repeated audit (D-15 O-0) under the unchanged instruction (25eb0e16…) and the
     operating rules D-15 §3, unamended
   - D-15's exclusion of the stopped session, and of any session that has read its transcript, stands
2  C (D-15 §2 C): the suspicion is not settled on this evidence; no repeated audit until a further PI record
```

## 3a. Open points named in the PI's approval (§6), as the basis of decision 2

```text
P-1 files outside the two clones. §1 (5) leaves the content of the auditor's own files beside the clones
    unestablished, yet §2 bounds what could reach the session by the 67 files of B-2 and option 1 states that no
    outcome content could reach it. To be completed: the sources and content scope of those files before the
    incident, from their existing creation records; only if they are shown to come from permitted checks can
    that be recorded. Otherwise no general "could not have reached" finding is made
P-2 file type and field are not evidence of content. NUL bytes do not show that a compiled or compressed file
    carries no readable data, and a notebook line in a "source" field may still embed results or their reading.
    To be completed: the inspection basis on which each text match carries no outcome content; for the binary
    files, evidence whether their content was passed to the tool output in the incident. Prohibited content is
    not spread to new sessions while this is established
both points concern the basis of the firewall finding, not the package: no new B or K. Neither the audit nor
B-1 / B-2 is to be redone. When both are completed, a further PI record may take decision 1
```

## 4. Hand-over (under decision 1; NOT in effect under decision 2)

```text
to the new auditor (a new session in a new directory, D-15 O-1), into inputs\ (D-15 O-3 (c)):
  the audit instruction F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md (25eb0e16…) with its sidecar ;
  D-15 (278532bf…) with its sidecar ; this record, signed, with its sidecar ; optionally the stopped audit record
  (f3f24b6a…) with its sidecar
not handed over: the count files, the drafter's handover note, earlier drafts, review comments
to the executor: nothing now; D-15, this record and the audit records go into p_konum_plus/prompts/ with the next
  dispatch record
G:\PycharmProjects\rp1r2_audit is left as it is and not used again (D-15 O-1)
```

## 5. End state

```text
rp1-r2 status = PARTIAL_PENDING_PI (executor) ; audit NOT PASSED (stopped, incomplete) ; firewall question of
AUDITOR-SCOPE-01 open (P-1, P-2) ; no repeated audit until a further PI record (D-15 §2 C) ; no ledger item
changes ; IR1-13 OPEN / B under D-14 ; real_data_access = false ; F3_EXECUTION_READY = false ; commit = false
```

## 6. Signature

```text
PI                    = Öner
decision              = 2  (D-15 §2 C): the suspicion is not settled on this evidence; no repeated audit until a
                        further PI record. Chosen by the rule of the PI's message: the two points are not completed
                        and the signature is required now
signature / approval  = APPROVED. The PI's message of 2026-10-12, verbatim (it relays a review; the PI's first,
                        shorter sending of its last paragraph was interrupted and resent in full as below):
                        aşağıdaki öneriye göre benim için imzala:
                        1. Kapsam dışında bırakılan dosyalar, karar cümlesinde unutuluyor.
                        §1(5), klonların dışındaki denetçi dosyalarının içeriğinin B-2 ile belirlenmediğini açıkça söylüyor. Buna rağmen §2, oturuma ulaşabilecek içeriği 67 dosyayla sınırlandırıyor; §3 ise hiçbir sonuç içeriğinin ulaşamayacağını kesinleştiriyor.
                        Düzeltme: Bu yardımcı dosyaların olay öncesindeki kaynaklarını ve içerik kapsamını mevcut oluşturma kayıtlarıyla açıkla. Yalnız izinli kontrollerden üretildikleri gösterilebiliyorsa bunu gerekçesiyle kaydet. Gösterilemiyorsa genel “ulaşamazdı” hükmü kurulamaz.
                        2. Dosya türü, sonuç içeriği bulunmadığını tek başına kanıtlamıyor.
                        §1(4)(c)’deki “derlenmiş/sıkıştırılmış baytlar okunabilir veri taşımaz” çıkarımı geçerli değil. NUL bulunması bunu kanıtlamaz. Benzer şekilde notebook’un source alanında olmak, satırın gömülü sonuç veya sonuç yorumu içermediğini tek başına göstermez. Sunulan betik ağırlıkla dosya yolu ve alan sınıflandırmasını doğruluyor.
                        Düzeltme: Metin eşleşmelerinin neden sonuç içeriği taşımadığının inceleme dayanağını belirt. Binary dosyalar için de “içerikleri okunamaz” yerine, olayda içeriklerinin çıktıya aktarılıp aktarılmadığına ilişkin kanıtı kullan. Bunu araştırırken yasaklı içeriği yeni oturumlara yayma.
                        Karar önerim: Bu iki nokta tamamlanmadan imza gerekiyorsa 2’yi seç. Tamamlanırsa 1 değerlendirilebilir. Bunlar pakette yeni B/K bulguları değildir; D-16’nın kesin firewall hükmünün dayanağıyla ilgilidir. Tüm denetimi veya B-1/B-2 çalışmasını baştan yapmak gerekmiyor.
                        This final text was delivered to the PI; the PI's forwarding it adopts it
date_time_local       = 2026-10-12 22:14, UTC+3 — the time the drafting session recorded the PI's message (command
                        output: `TZ=Europe/Istanbul date` → 2026-10-12 22:14 +03; UTC 2026-10-12T19:14:59Z). The
                        message's own send time is NOT OBSERVED by the drafter
```

## 7. Hashes and checks (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ sha256sum <files>
278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md
25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
$ wc -c / sha256sum <the PI's uploads, as received>
 5733 b2_effective_counts.txt
    0 b2_effective_counts.txt
 5951 b2_intended_counts.txt
11684 total
0c8a85814cd18e67bb2d21f30d162f2a66e2567d6a9f715e77f5f5be62775948  b2_effective_counts.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  b2_effective_counts.txt
7e23bdfcea95f61c96a98734b0931b8ae1aa218ca7eacd096a0b5e5cc7a87f4d  b2_intended_counts.txt
$ python3 -I d16_checks.py b2_effective_counts.txt b2_intended_counts.txt   (in a clone at 25c7d51; source below)
(a) reported line numbers vs E (input hash table excluded)
  p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md | reported 1, all match E: True | E lines 5, intended lines 5, intended-only []
  p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md | reported 20, all match E: True | E lines 20, intended lines 20, intended-only []
  p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md | reported 32, all match E: True | E lines 32, intended lines 32, intended-only []
  p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py | reported 3, all match E: True | E lines 22, intended lines 23, intended-only [4234]
  notebooks/2-web-scraping-yok-atlas.ipynb | reported 1, all match E: True | E lines 1, intended lines 1, intended-only []
  modules/experimental/toy_datasets.py | reported 1, all match E: True | E lines 1, intended lines 2, intended-only [180]
  modules/experimental/run_driver.py | reported 3, all match E: True | E lines 3, intended lines 3, intended-only []
(b) notebook lines matching E, by field
  notebooks/2-web-scraping-yok-atlas.ipynb {'source': 1}
  notebooks/data-preprocessing-election.ipynb {'source': 2}
  notebooks/data-preprocessing-maps.ipynb {'source': 1}
  notebooks/data-preprocessing-population.ipynb {'source': 16}
(c) binary files in the list
  clustering/__pycache__/base_clustering.cpython-311.pyc bytes 24031 NUL-in-first-8KiB True
  temp/eps/Figure14.zip bytes 2664069 NUL-in-first-8KiB True
  temp/eps/Figures_and_readme.zip bytes 40096347 NUL-in-first-8KiB True
  viz/plotters/__pycache__/geo_names_plotter.cpython-311.pyc bytes 37839 NUL-in-first-8KiB True
  .gitignore lists __pycache__/: True
(d) list comparison
  effective files 67 lines 579 ; intended files 69 lines 600
  only in intended: ['p_konum_plus/calibration/f3_step2_rp1-r2_attempt2_launch1_stdout_2026-10-10.log', 'p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration/f3_step2_rp1-r2_launch1_stdout_2026-10-10.log'] ; only in effective: []
  F1 input hash table            files   1 lines   12
  application code               files   7 lines   15
  binary                         files   4 lines    4
  notebook                       files   4 lines   20
  p_konum_plus code and records  files  51 lines  528
  under data/: [] ; eligible manifest: [] ; results/ other than .py: []
```

```python
"""D-16 checks on commit 25c7d51 (run inside a clone): prints classifications and counts only, never line content."""
import re, subprocess, sys, collections
E = re.compile(r'write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10\.py')
I = re.compile(r'write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY')
def blob(p): return subprocess.run(['git', 'show', '25c7d51:' + p], capture_output=True, check=True).stdout
def load(p):
    d = {}
    for ln in open(p, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln:
            _, rest = ln.split(':', 1); path, n = rest.rsplit(':', 1); d[path] = int(n)
    return d
eff, intd = load(sys.argv[1]), load(sys.argv[2])
print('(a) reported line numbers vs E (input hash table excluded)')
reported = {
 'p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md': [852],
 'p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md': [328,334,336,345,356,391,412,415,487,491,534,885,895,896,935,963,970,1679,1737,2132],
 'p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md': [1590,1609,1610,1652,1668,1669,1670,1671,1691,1729,1756,1803,1825,1849,1852,1897,1994,1995,2099,2130,2148,2257,2275,2396,2400,2418,2437,2452,2454,2464,2493,2537],
 'p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py': [113,168,215],
 'notebooks/2-web-scraping-yok-atlas.ipynb': [168],
 'modules/experimental/toy_datasets.py': [181],
 'modules/experimental/run_driver.py': [625,653,679]}
for p, nums in reported.items():
    lines = blob(p).decode('utf-8').splitlines()
    e = [k for k in range(1, len(lines) + 1) if E.search(lines[k - 1])]
    i = [k for k in range(1, len(lines) + 1) if I.search(lines[k - 1])]
    print('  %s | reported %d, all match E: %s | E lines %d, intended lines %d, intended-only %s' % (p, len(nums), all(n in e for n in nums), len(e), len(i), sorted(set(i) - set(e))))
print('(b) notebook lines matching E, by field')
for p in sorted(x for x in eff if x.startswith('notebooks/')):
    region, c = None, collections.Counter()
    for ln in blob(p).decode('utf-8').splitlines():
        s = ln.strip()
        if s.startswith('"source"'): region = 'source'
        elif s.startswith('"outputs"'): region = 'outputs'
        elif s.startswith('"metadata"'): region = 'metadata'
        if E.search(ln): c[region] += 1
    print('  %s %s' % (p, dict(c)))
print('(c) binary files in the list')
for p in sorted(x for x in eff if x.endswith(('.pyc', '.zip'))):
    b = blob(p); print('  %s bytes %d NUL-in-first-8KiB %s' % (p, len(b), b'\x00' in b[:8192]))
print('  .gitignore lists __pycache__/:', '__pycache__/' in blob('.gitignore').decode().split())
print('(d) list comparison')
print('  effective files %d lines %d ; intended files %d lines %d' % (len(eff), sum(eff.values()), len(intd), sum(intd.values())))
print('  only in intended:', sorted(set(intd) - set(eff)), '; only in effective:', sorted(set(eff) - set(intd)))
def cls(p):
    if p == 'p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv': return 'F1 input hash table'
    if p.endswith(('.pyc', '.zip')): return 'binary'
    if p.startswith('p_konum_plus/'): return 'p_konum_plus code and records'
    if p.startswith('notebooks/'): return 'notebook'
    return 'application code'
f, l = collections.Counter(), collections.Counter()
for p, n in eff.items(): f[cls(p)] += 1; l[cls(p)] += n
for k in sorted(f): print('  %-30s files %3d lines %4d' % (k, f[k], l[k]))
print('  under data/:', [p for p in eff if p.startswith('data/')], '; eligible manifest:', [p for p in eff if 'eligible' in p], '; results/ other than .py:', [p for p in eff if p.startswith('results/') and not p.endswith('.py')])
```

## 8. The effective-pattern count list (b2_effective_counts.txt, 0c8a8581…, verbatim)

```text
25c7d51:clustering/__pycache__/base_clustering.cpython-311.pyc:1
25c7d51:clustering/base_clustering.py:2
25c7d51:modules/experimental/run_driver.py:3
25c7d51:modules/experimental/toy_datasets.py:1
25c7d51:notebooks/2-web-scraping-yok-atlas.ipynb:1
25c7d51:notebooks/data-preprocessing-election.ipynb:2
25c7d51:notebooks/data-preprocessing-maps.ipynb:1
25c7d51:notebooks/data-preprocessing-population.ipynb:16
25c7d51:p_konum_plus/calibration/f3_rp1-r2_finalize_delivery_2026-10-12.py:5
25c7d51:p_konum_plus/calibration/f3_rp1-r2_launch_attempt_2026-10-10.py:3
25c7d51:p_konum_plus/calibration/f3_rp1-r2_logged_preflight_2026-10-10.py:4
25c7d51:p_konum_plus/calibration/f3_rp1-r2_prepare_review_records_2026-10-10.py:5
25c7d51:p_konum_plus/calibration/f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py:3
25c7d51:p_konum_plus/calibration/f3_rp1-r2_small_input_tests_2026-10-10.py:10
25c7d51:p_konum_plus/calibration/f3_rp1-r2_technical_tests_2026-10-10.py:2
25c7d51:p_konum_plus/calibration/f3_rp1-r2_write_custody_2026-10-10.py:2
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_r1_2026-09-06.py:1
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_r2_2026-09-07.py:4
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_r3_2026-09-22.py:10
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py:14
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py:17
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_r4_2026-09-24.py:13
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:18
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
25c7d51:p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py:18
25c7d51:p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff:9
25c7d51:p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff:4
25c7d51:p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv:12
25c7d51:p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md:32
25c7d51:p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md:20
25c7d51:p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md:5
25c7d51:p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md:11
25c7d51:p_konum_plus/provenance/f3_realdata_prep_rp1-r2_attempt2_harness_provenance_diff_2026-10-11.diff:3
25c7d51:p_konum_plus/provenance/f3_realdata_prep_rp1-r2_attempt2_provenance_changes_2026-10-11.json:2
25c7d51:p_konum_plus/provenance/f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md:2
25c7d51:p_konum_plus/provenance/f3_realdata_prep_rp1-r2_authored_edits_2026-10-10.json:3
25c7d51:p_konum_plus/provenance/f3_realdata_prep_rp1-r2_harness_diff_vs_r4-2_2026-10-12.diff:7
25c7d51:p_konum_plus/provenance/f3_realdata_prep_rp1-r2_harness_diff_vs_rp1-r1_2026-10-12.diff:6
25c7d51:p_konum_plus/provenance/f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11/f3_rp1-r2_launch_attempt_2026-10-10.py:3
25c7d51:p_konum_plus/provenance/f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py:10
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py:10
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py:10
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py:10
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py:13
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py:13
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py:15
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py:13
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py:13
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py:13
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py:13
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py:18
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py:18
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py:18
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py:18
25c7d51:p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py:18
25c7d51:p_konum_plus/quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md:1
25c7d51:p_konum_plus/quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md:1
25c7d51:p_konum_plus/quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md:1
25c7d51:p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
25c7d51:results/result_plotter_KMeans_KMedoids.py:2
25c7d51:results/result_plotter_Spectral.py:2
25c7d51:results/results_plotter_GMM.py:3
25c7d51:temp/eps/Figure14.zip:1
25c7d51:temp/eps/Figures_and_readme.zip:1
25c7d51:viz/plotters/__pycache__/geo_names_plotter.cpython-311.pyc:1
25c7d51:viz/plotters/geo_names_plotter.py:2
```

## 9. Changes from the DRAFT (deb6eeb8…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, header | DRAFT → signed; file name without DRAFT; draft and status lines | PI approval |
| 2 | §2, §3 headings | §2 marked as not adopted; §3 records decision 2, option 1 kept as presented | PI approval |
| 3 | §3a new, §4 heading, §5 | the two open points of the PI's message as the basis of decision 2; hand-over not in effect; end state with the firewall question open and no repeated audit | PI approval (decision 2) |
| 4 | §6 | decision 2, approval message verbatim, time of recording | PI approval |

No other change: §1, the body of §2 and §3, §7 and §8 stand as in the DRAFT.
