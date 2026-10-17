# p_konum_plus — rp1-r2 — PI record completing the AUDITOR-SCOPE-01 evaluation (D-17, D-16 §3a) — 2026-10-12

> Child of D-16. Governed by D-11 r1 §5 and Ek-1 r1. Prepared by Claude (Claude Code cloud session) at the PI's
> request. The record is the PI's; every value may be changed before signature, and the sidecar is then
> recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-12 (§6); decision = 1. It opens
> the repeated audit only: it is not PASSED, not a D-9 §2 (a) binding, not QUALIFIED and closes no ledger item.**

```text
record                = f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md   (D-17)
drafts                = …_completion_pi_decision_record_DRAFT_r1_2026-10-12.md
                        c8636e0fde56bcc64247b33d167775c2c13ec21612eeea9859c288ba25d3f292 (r1, the approved content;
                        changes to this final text in §10) ;
                        …_completion_pi_decision_record_DRAFT_2026-10-12.md
                        acb669e50161454970db3b5a80799dd54b8fd85de4a85bbd9f5eb470f50b5ee1 (changes → r1 in §9, the one
                        review round of D-11 r1 §6)
status                = SIGNED (PI approval, 2026-10-12; §6)
parent                = D-16 f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md  3e2a5fe3… (decision 2)
                        D-15 f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md  278532bf… (decision B)
subject               = the two open points P-1 and P-2 of D-16 §3a, and whether the repeated audit opens
what_this_record_is_not = not a finding on the rp1-r2 package; not PASSED; not a closure of any ledger item; not a
                        D-9 §2 (a) binding; not QUALIFIED; not a real-data authorization; not a change to the audit instruction (25eb0e16…)
                        or to its pass criterion; it does not redo the audit or B-1 / B-2 (D-16 §3a)
```

## 1. Evidence

```text
(1) incident window. Local times (UTC+3) of the audit directory listing in (2): audit_support/custody.json was last
    written 20:32:31.77, the instant the stopped record gives for its custody step (utc 17:32:31.72); the first
    stop file, audit_support/stop_report.py, 20:34:51.24. The search ran between the two. Listed times are
    modification times, not creation times
(2) P-1 — files of G:\PycharmProjects\rp1r2_audit outside the two clones; command and output as run and relayed by
    the PI (Git Bash, 2026-10-12), verbatim in §8.1. Files with a time before the window:
      .idea\…  (8 files, 19:55:22 – 19:59:54)          PyCharm project settings, in a hidden directory
      audit_clone_verification_2026-10-12.md (20:05:12) the auditor's clone check: git command outputs only
                                                        (the PI's upload, 2605 bytes = the listed 2605 bytes;
                                                        no line matches E — §7)
      audit_support\custody.py (20:32:08)               the auditor's custody script
      audit_support\intake.json (20:32:14), custody.json (20:32:31)   that script's outputs
    the three audit_support files equal the hashes the stopped record gives for them (PI's sha256sum, §8.2):
      7fdd3fa1… custody.py, e38f49f3… intake.json, 10965cb1… custody.json
    and the source of custody.py printed in the stopped record hashes to 7fdd3fa1… with 5111 bytes, the listed size
    (§7). By that source the script reads only the forwarded instruction file, the rp1-r2 transmission list and the
    files it lists (all under p_konum_plus/, asserted in the script), git outputs of the ref clone and the harness
    AST, and writes only intake.json and custody.json: their content comes from permitted checks
    files with a time after the window: stop_report.py, stop_state.json, scope_incident.json and the stopped record
    with its sidecar — written in response to the incident
(3) P-2, binary files — reproduction of the incident search in the incident's own output mode, run by the PI in
    Windows PowerShell in G:\PycharmProjects\rp1r2_audit on 2026-10-12, with the same rg.exe (path as reported by
    the stopped session), the same working directory and the same effective pattern E (D-16 §1 (1)):
      version (command and output as relayed by the PI):
        PS G:\PycharmProjects\rp1r2_audit> &'C:\Users\Neo\.codemoss\dependencies\codex-sdk\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\codex-path\rg.exe' --version
        ripgrep 15.2.0 (rev e89fff89ac)

        features:+pcre2
        simd(compile):+SSE2,-SSSE3,-AVX2
        simd(runtime):+SSE2,+SSSE3,+AVX2

        PCRE2 10.45 is available (JIT is available)
      (a) -n, the incident's mode, whole directory; each printed line reduced in memory to its path and counted, so
          that only path:count is written (commands as given to the PI by the drafter, §8.5):
            & $rg -n $E 2> …\b2_rg_n_stderr.txt | ForEach-Object { ($_ -split ':', 2)[0] } | Group-Object -NoElement | … | Set-Content … b2_rg_n_counts.txt
          b2_rg_n_counts.txt (d1d05c55…): 130 entries, 1,164 lines; b2_rg_n_stderr.txt: empty (0 bytes)
          in ref\ and in run\ alike: 63 files, 575 lines — exactly the 63 text files of D-16's git grep list, each
          with the same count; no .pyc, no .zip, nothing under .idea\, data\ or results\ other than the three
          plotting scripts; outside the clones: audit_support\custody.py (1 line) — before the window; the
          stopped record, stop_report.py and scope_incident.json — after it
      (b) -n over the four binary files' directories given explicitly, so that even the .pyc files, which
          .gitignore otherwise excludes, are searched (files found by recursion, as in the incident):
            & $rg -n $E ref\temp\eps run\temp\eps ref\clustering\__pycache__ run\clustering\__pycache__ ref\viz\plotters\__pycache__ run\viz\plotters\__pycache__ 2> …\b2_bin_stderr.txt | Measure-Object -Line
          output as relayed by the PI: Lines 0 (verbatim in §8.5); b2_bin_stderr.txt: empty (0 bytes). No line and no
          "matches suppressed" warning
      (c) the earlier -c run (b2_rg_repro_counts.txt, 05a5de98…) gives the identical path:count set (§7); it is kept
          as supporting evidence only
      (d) documentation: the PI's search of the 15.2.0 help text for the sentence on NUL bytes returned no line
          (§8.5; the sentence may be wrapped across two lines). No documentation claim for 15.2.0 is made. The
          drafter's control on rg 14.1.0 (a different version; background only): -n over copies of the four files,
          found by recursion, prints nothing; with --binary each has one match (§7)
    (where.exe rg found no rg on the PATH: "INFO: Could not find files for the given pattern(s).")
    the reproduction runs on the same bytes as the incident: the clones were clean at 25c7d51 when the session
    stopped (stopped record, final clone state) and the pre-window support files are unchanged ((2)). What it cannot
    reproduce is the incident call's output truncation, which only removes lines
(4) P-2, text lines — meaning of the 35 matching lines outside the audit's own reading scope (7 application-code
    files, 4 notebooks). Provenance: the PI displayed these lines on the PI's machine and pasted them into the
    drafting session on 2026-10-12; the drafter has therefore read them. The drafter proposes one class per line,
    with a reason that describes the line without reproducing it (§8.4, P2_text_lines_classification_2026-10-12.csv,
    8730b2f0…); the PI adopts or changes it by signing:
      K1  preprocessing output written; no clustering content                                       20 lines
      K2  clustering-pipeline or tool output written; generic or variable file name; no value        9 lines
      K3  file name or expression carries an algorithm, metric or "best" label, but no value and no
          comparison result (a label naming a quantity, not the quantity)                             6 lines
      K4  carries an outcome value, a winner or a comparative claim                                    0 lines
    the six K3 lines are in the three plotting scripts under results/: f-string file names built from variables
    with a fixed algorithm or metric name and, in three of them, a "best" suffix; none names which algorithm, k or
    setting is best, and none holds a number other than a rounding precision. The drafter's earlier feature and
    keyword screens (§7) are kept as supporting checks; the classification rests on reading the lines
    the remaining text lines are p_konum_plus code and records (51 files, 528 lines), which the audit reads anyway,
    and the 12 lines of the F1 input hash table already recorded in D-15 / D-16
```

## 2. Evaluation (the drafter's proposal; the PI decides)

```text
P-1 completed: every file beside the clones at the time of the search is accounted for — IDE settings in a hidden
    directory (not printed by rg, (3)), the auditor's clone check (git outputs), and the custody script with its two
    outputs, whose bytes match the stopped record and whose content comes from permitted checks
P-2 completed:
    binary files — in the incident's mode (-n), with the same rg, directory, bytes and pattern, rg prints no line and
    no warning from them, also when their directories are given explicitly ((3) (a), (b)); this is an observation,
    not an inference from another mode or from documentation
    text lines — every one of the 35 lines outside the audit's reading scope is classed K1–K3 by its meaning
    ((4), §8.4); none carries an outcome value, a winner or a comparative claim
    the F1 input hash table's 12 lines are the only content outside package material and application code that
    reached the session
consequence (protocol §9): no STOP-15, no STOP-16. What remains is the breach of the audit instruction's reading
    rule for the 12 inventory lines, logged by D-15, D-16 and this record
residual, stated: the reproduction shows what the same rg prints in the same mode on the same bytes today; that the
    incident call printed the same, before its output was truncated, is an inference from the identical binary,
    mode, directory, bytes and pattern
provenance note: the 35 lines of (4) are now known to the drafting session; under (4) they carry no outcome content,
    so this has no consequence for that session's role
```

## 3. Decision — the PI chose 1 (§6); option 2 is kept as presented

```text
1  SUSPICION SETTLED; THE REPEATED AUDIT OPENS                                              [recommended]
   - on §1 and §2 the PI finds the firewall suspicion of AUDITOR-SCOPE-01 settled, P-1 and P-2 of D-16 §3a
     completed, adopts the line classification of §8.4, and accepts the residual of §2
   - this record opens the repeated audit (D-15 O-0) under the unchanged instruction (25eb0e16…) and D-15 §3,
     unamended; D-15's exclusion of the stopped session, and of any session that has read its transcript, stands
   - it opens the repeated audit only: the audit is not PASSED, no bytes are bound under D-9 §2 (a), nothing is
     QUALIFIED and no ledger item is closed by this record
2  NOT SETTLED: D-15 §2 C continues; no repeated audit until a further PI record
```

## 4. Hand-over (under decision 1)

```text
to the new auditor (a new session in a new directory, D-15 O-1), into inputs\ (D-15 O-3 (c)), each with its sidecar:
  the audit instruction F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md (25eb0e16…) ; D-15 (278532bf…) ;
  D-16 (3e2a5fe3…) ; this record, signed ; optionally the stopped audit record (f3f24b6a…)
not handed over: the count files, the directory listing, the line classification, the drafter's handover note,
  earlier drafts, review comments
to the executor: nothing now; D-15, D-16, this record and the audit records go into p_konum_plus/prompts/ with the
  next dispatch record
G:\PycharmProjects\rp1r2_audit is left as it is and not used again (D-15 O-1)
```

## 5. End state

```text
under 1: firewall question of AUDITOR-SCOPE-01 settled ; repeated audit open (not started) ; under 2: as D-16 §5
in both: rp1-r2 status = PARTIAL_PENDING_PI (executor) ; audit NOT PASSED (stopped, incomplete) until the repeated
audit ; no ledger item changes ; IR1-13 OPEN / B under D-14 ; real_data_access = false ;
F3_EXECUTION_READY = false ; commit = false
```

## 6. Signature

```text
PI                    = Öner
decision              = 1  SUSPICION SETTLED; THE REPEATED AUDIT OPENS (§3), as written in DRAFT r1
adopted               = the line classification of §8.4 (P2_text_lines_classification_2026-10-12.csv, 8730b2f0…)
accepted              = the residual of §2: that the incident call printed what the reproduction prints is an inference
                        from the identical binary, mode, directory, bytes and pattern, not an observation
scope                 = opens the repeated audit only; not PASSED, not a D-9 §2 (a) binding, not QUALIFIED, no ledger
                        item closed
signature / approval  = APPROVED. The PI's message of 2026-10-12, verbatim:
                        ben de aynılarını onaylıyorum, imzala,
                        "aynılarını" refers to the two texts immediately before it in the conversation, quoted here as
                        context (verbatim):
                        (a) the review relayed by the PI: «İmzada karar 1, §8.4 sınıflandırmasının benimsenmesi ve §2’deki
                            tarihsel yeniden oluşturma belirsizliğinin kabulü açıkça yer alsın. İmzalı dosyanın hash’i
                            yeniden üretildikten sonra §4’teki paket yeni bağımsız denetçiye iletilebilir. Bu karar yalnız
                            yeniden denetimi açar; PASSED veya PI bağlaması anlamına gelmez.»
                        (b) the drafter's example approval: «D-17 DRAFT r1'i karar 1 ile onaylıyorum; §8.4 sınıflandırmasını
                            benimsiyor, §2'deki tarihsel yeniden oluşturma belirsizliğini kabul ediyorum.»
                        The approved content is DRAFT r1 (c8636e0f…); this final text differs from it only as listed in
                        §10. This final text was delivered to the PI; the PI's forwarding it adopts it
date_time_local       = 2026-10-12 22:42, UTC+3 — the time the drafting session recorded the PI's message (command
                        output: `TZ=Europe/Istanbul date` → 2026-10-12 22:42 +03; UTC 2026-10-12T19:42:44Z). The
                        message's own send time is NOT OBSERVED by the drafter
```

## 7. Hashes and checks (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ sha256sum <records, drafts and the PI's uploads, as received>
3e2a5fe3373ae08fc91831d7312c5f994ff332efdf3bae50818cced98d608e45  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md
278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md
25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
acb669e50161454970db3b5a80799dd54b8fd85de4a85bbd9f5eb470f50b5ee1  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_DRAFT_2026-10-12.md
8730b2f0bd09af65ee3338499c31cfee761442a8413db156aa04be954cae841e  P2_text_lines_classification_2026-10-12.csv
f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
d1d05c55425fb63145b064e40e3726edec9d540b58c2bd77b236cf2cac5d233e  b2_rg_n_counts.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  b2_rg_n_stderr.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  b2_bin_stderr.txt
05a5de9848c42d72641c4f9e5fa63b519af48595144631b542e52207570dcb19  b2_rg_repro_counts.txt
0c8a85814cd18e67bb2d21f30d162f2a66e2567d6a9f715e77f5f5be62775948  b2_effective_counts.txt
2b7a400d4a79261cdb44d5f4f011f7e151fbeab49fd93dc90cc277c378ceefcf  audit_clone_verification_2026-10-12.md
10852 b2_rg_n_counts.txt
    0 b2_rg_n_stderr.txt
    0 b2_bin_stderr.txt
10852 b2_rg_repro_counts.txt
21704 total

$ python3 -I d17_p1_checks.py <stopped record> <clone check upload>
custody.py as printed in the stopped record: bytes 5111 sha256 7fdd3fa1748b5f431d15518a53d723c0b9fdfb4186704df5d0186d88ec5f9c40
clone check upload: bytes 2605 sha256 2b7a400d4a79261cdb44d5f4f011f7e151fbeab49fd93dc90cc277c378ceefcf lines matching E 0

$ python3 -I d17_rg_compare.py b2_rg_n_counts.txt b2_effective_counts.txt   (the -n reproduction against D-16's git grep list)
rg output lines 130 matched lines 1164
ref files 63 lines 575 | in git-grep list, not printed by rg: ['clustering/__pycache__/base_clustering.cpython-311.pyc', 'temp/eps/Figure14.zip', 'temp/eps/Figures_and_readme.zip', 'viz/plotters/__pycache__/geo_names_plotter.cpython-311.pyc'] | printed by rg, not in list: [] | count differences: []
run files 63 lines 575 | in git-grep list, not printed by rg: ['clustering/__pycache__/base_clustering.cpython-311.pyc', 'temp/eps/Figure14.zip', 'temp/eps/Figures_and_readme.zip', 'viz/plotters/__pycache__/geo_names_plotter.cpython-311.pyc'] | printed by rg, not in list: [] | count differences: []
outside the clones: {'f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md': 7, 'audit_support/scope_incident.json': 1, 'audit_support/stop_report.py': 5, 'audit_support/custody.py': 1}
.idea paths: [] | data/ paths: [] | results/ non-.py: []

$ python3 -I d17_n_vs_c.py b2_rg_n_counts.txt b2_rg_repro_counts.txt
-n: entries 130 lines 1164 | -c: entries 130 lines 1164 | identical: True
binary paths in -n output: []

$ bash d17_local_binary_control.sh <dir with copies of the four binary files> <scratch>
rg 14.1.0; -n; files found by recursion under '.'
exit 1 stdout_lines 0 stderr_lines 0
control: -c --binary (path:count)
./clustering/__pycache__/base_clustering.cpython-311.pyc:1
./temp/eps/Figure14.zip:1
./temp/eps/Figures_and_readme.zip:1
./viz/plotters/__pycache__/geo_names_plotter.cpython-311.pyc:1

$ python3 -I p2_text_classify.py   (in a clone at 25c7d51; supporting check)
clustering/base_clustering.py                      302 -        token=to_csv       parses=True  len= 59 strings=['path'] numerals=0 maxdigits=0
clustering/base_clustering.py                      303 -        token=to_csv       parses=True  len=104 strings=['path'] numerals=0 maxdigits=0
modules/experimental/run_driver.py                 625 -        token=dump(        parses=True  len= 36 strings=[] numerals=1 maxdigits=1
modules/experimental/run_driver.py                 653 -        token=to_csv       parses=True  len= 55 strings=['path'] numerals=0 maxdigits=0
modules/experimental/run_driver.py                 679 -        token=dump(        parses=False len= 56 strings=['fstring/other'] numerals=0 maxdigits=0
modules/experimental/toy_datasets.py               181 -        token=dump(        parses=True  len= 35 strings=[] numerals=0 maxdigits=0
results/result_plotter_KMeans_KMedoids.py          101 -        token=to_csv       parses=True  len= 65 strings=['path'] numerals=1 maxdigits=1
results/result_plotter_KMeans_KMedoids.py          103 -        token=to_csv       parses=True  len= 77 strings=['path'] numerals=1 maxdigits=1
results/result_plotter_Spectral.py                 382 -        token=to_csv       parses=True  len= 77 strings=['path'] numerals=0 maxdigits=0
results/result_plotter_Spectral.py                 385 -        token=to_csv       parses=True  len= 69 strings=['path'] numerals=0 maxdigits=0
results/results_plotter_GMM.py                     176 -        token=to_csv       parses=True  len= 64 strings=['path'] numerals=0 maxdigits=0
results/results_plotter_GMM.py                     179 -        token=to_csv       parses=True  len= 54 strings=['path'] numerals=0 maxdigits=0
results/results_plotter_GMM.py                     182 -        token=to_csv       parses=True  len= 47 strings=['path'] numerals=0 maxdigits=0
viz/plotters/geo_names_plotter.py                  337 -        token=to_csv       parses=True  len= 39 strings=['fstring/other'] numerals=0 maxdigits=0
viz/plotters/geo_names_plotter.py                  537 -        token=to_csv       parses=True  len= 65 strings=['fstring/other'] numerals=0 maxdigits=0
notebooks/2-web-scraping-yok-atlas.ipynb           168 source   token=to_csv       parses=True  len= 57 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-election.ipynb       1669 source   token=to_csv       parses=True  len= 55 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-election.ipynb       2455 source   token=to_csv       parses=True  len= 65 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-maps.ipynb            260 source   token=to_csv       parses=True  len= 73 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      165 source   token=to_csv       parses=True  len= 79 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      272 source   token=to_csv       parses=True  len= 82 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      385 source   token=to_csv       parses=True  len= 84 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      463 source   token=to_csv       parses=True  len= 87 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      537 source   token=to_csv       parses=True  len= 83 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      609 source   token=to_csv       parses=True  len= 50 strings=['path'] numerals=1 maxdigits=1
notebooks/data-preprocessing-population.ipynb      622 source   token=to_csv       parses=True  len= 35 strings=[] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      677 source   token=to_csv       parses=True  len= 85 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb      730 source   token=to_csv       parses=True  len= 99 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb     1081 source   token=to_csv       parses=True  len=106 strings=['fstring/other', 'path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb     1268 source   token=to_csv       parses=True  len= 93 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb     1358 source   token=to_csv       parses=True  len= 67 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb     1790 source   token=to_csv       parses=True  len= 79 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb     1993 source   token=to_csv       parses=True  len= 83 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb     2083 source   token=to_csv       parses=True  len= 57 strings=['path'] numerals=0 maxdigits=0
notebooks/data-preprocessing-population.ipynb     2307 source   token=to_csv       parses=True  len= 87 strings=['path'] numerals=0 maxdigits=0
lines classified: 35
--- digits inside string literals of the same lines (counts only)
clustering/base_clustering.py                      302 digit_runs_in_strings=0 longest=0 decimal_numbers=0
clustering/base_clustering.py                      303 digit_runs_in_strings=0 longest=0 decimal_numbers=0
modules/experimental/run_driver.py                 625 digit_runs_in_strings=0 longest=0 decimal_numbers=0
modules/experimental/run_driver.py                 653 digit_runs_in_strings=0 longest=0 decimal_numbers=0
modules/experimental/run_driver.py                 679 digit_runs_in_strings=0 longest=0 decimal_numbers=0
modules/experimental/toy_datasets.py               181 digit_runs_in_strings=0 longest=0 decimal_numbers=0
results/result_plotter_KMeans_KMedoids.py          101 digit_runs_in_strings=1 longest=1 decimal_numbers=0
results/result_plotter_KMeans_KMedoids.py          103 digit_runs_in_strings=1 longest=1 decimal_numbers=0
results/result_plotter_Spectral.py                 382 digit_runs_in_strings=0 longest=0 decimal_numbers=0
results/result_plotter_Spectral.py                 385 digit_runs_in_strings=0 longest=0 decimal_numbers=0
results/results_plotter_GMM.py                     176 digit_runs_in_strings=0 longest=0 decimal_numbers=0
results/results_plotter_GMM.py                     179 digit_runs_in_strings=0 longest=0 decimal_numbers=0
results/results_plotter_GMM.py                     182 digit_runs_in_strings=0 longest=0 decimal_numbers=0
viz/plotters/geo_names_plotter.py                  337 digit_runs_in_strings=0 longest=0 decimal_numbers=0
viz/plotters/geo_names_plotter.py                  537 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/2-web-scraping-yok-atlas.ipynb           168 digit_runs_in_strings=1 longest=1 decimal_numbers=0
notebooks/data-preprocessing-election.ipynb       1669 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-election.ipynb       2455 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-maps.ipynb            260 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      165 digit_runs_in_strings=3 longest=4 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      272 digit_runs_in_strings=2 longest=4 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      385 digit_runs_in_strings=3 longest=4 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      463 digit_runs_in_strings=2 longest=4 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      537 digit_runs_in_strings=3 longest=4 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      609 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      622 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      677 digit_runs_in_strings=2 longest=4 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb      730 digit_runs_in_strings=3 longest=4 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb     1081 digit_runs_in_strings=1 longest=1 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb     1268 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb     1358 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb     1790 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb     1993 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb     2083 digit_runs_in_strings=0 longest=0 decimal_numbers=0
notebooks/data-preprocessing-population.ipynb     2307 digit_runs_in_strings=0 longest=0 decimal_numbers=0

$ python3 -I p2_keyword_screen.py   (in a clone at 25c7d51; supporting check; flags only)
clustering/base_clustering.py:302 | in strings: - | in code: ['result/summary word']
clustering/base_clustering.py:303 | in strings: ['result/summary word'] | in code: ['result/summary word']
modules/experimental/run_driver.py:625 | in strings: - | in code: -
modules/experimental/run_driver.py:653 | in strings: ['result/summary word'] | in code: -
modules/experimental/run_driver.py:679 | in strings: - | in code: -
modules/experimental/toy_datasets.py:181 | in strings: - | in code: ['result/summary word']
results/result_plotter_KMeans_KMedoids.py:101 | in strings: - | in code: -
results/result_plotter_KMeans_KMedoids.py:103 | in strings: ['superlative/evaluative'] | in code: ['superlative/evaluative']
results/result_plotter_Spectral.py:382 | in strings: ['superlative/evaluative', 'algorithm name'] | in code: ['superlative/evaluative']
results/result_plotter_Spectral.py:385 | in strings: ['algorithm name'] | in code: -
results/results_plotter_GMM.py:176 | in strings: ['superlative/evaluative', 'cvi/metric name', 'algorithm name'] | in code: ['superlative/evaluative']
results/results_plotter_GMM.py:179 | in strings: ['cvi/metric name', 'algorithm name'] | in code: -
results/results_plotter_GMM.py:182 | in strings: ['cvi/metric name', 'algorithm name'] | in code: -
viz/plotters/geo_names_plotter.py:337 | in strings: - | in code: ['result/summary word']
viz/plotters/geo_names_plotter.py:537 | in strings: - | in code: -
notebooks/2-web-scraping-yok-atlas.ipynb:168 | in strings: - | in code: -
notebooks/data-preprocessing-election.ipynb:1669 | in strings: - | in code: -
notebooks/data-preprocessing-election.ipynb:2455 | in strings: - | in code: -
notebooks/data-preprocessing-maps.ipynb:260 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:165 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:272 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:385 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:463 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:537 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:609 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:622 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:677 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:730 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:1081 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:1268 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:1358 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:1790 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:1993 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:2083 | in strings: - | in code: -
notebooks/data-preprocessing-population.ipynb:2307 | in strings: - | in code: -
```

`d17_p1_checks.py`:

```python
"""D-17 P-1: hash the custody.py source printed in the stopped record; E-matches in the PI's clone-check upload."""
import hashlib, re, sys
rec = open(sys.argv[1], encoding='utf-8').read()
src = re.search(r"the script source follows\.\n+```python\n(.*?)\n```", rec, re.S).group(1).encode()
print('custody.py as printed in the stopped record: bytes', len(src), 'sha256', hashlib.sha256(src).hexdigest())
E = re.compile(r'write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10\.py')
cv = open(sys.argv[2], 'rb').read()
print('clone check upload: bytes', len(cv), 'sha256', hashlib.sha256(cv).hexdigest(), 'lines matching E', sum(1 for l in cv.decode('utf-8').splitlines() if E.search(l)))
```

`d17_rg_compare.py`:

```python
"""D-17: compare the rg reproduction (path:count) with D-16's git grep list (25c7d51:path:count)."""
import sys
rg = {}
for ln in open(sys.argv[1], 'rb').read().decode('utf-8-sig').splitlines():
    if ln.strip():
        p, n = ln.rsplit(':', 1); rg[p.replace('\\', '/')] = int(n)
gg = {}
for ln in open(sys.argv[2], encoding='utf-8'):
    ln = ln.strip()
    if ln:
        _, rest = ln.split(':', 1); p, n = rest.rsplit(':', 1); gg[p] = int(n)
print('rg output lines', len(rg), 'matched lines', sum(rg.values()))
for clone in ('ref', 'run'):
    sub = {p[len(clone) + 1:]: n for p, n in rg.items() if p.startswith(clone + '/')}
    print(clone, 'files', len(sub), 'lines', sum(sub.values()), '| in git-grep list, not printed by rg:', sorted(set(gg) - set(sub)),
          '| printed by rg, not in list:', sorted(set(sub) - set(gg)), '| count differences:', sorted(p for p in set(gg) & set(sub) if gg[p] != sub[p]))
print('outside the clones:', {p: n for p, n in rg.items() if not p.startswith(('ref/', 'run/'))})
print('.idea paths:', [p for p in rg if '.idea' in p], '| data/ paths:', [p for p in rg if '/data/' in '/' + p], '| results/ non-.py:', [p for p in rg if '/results/' in '/' + p and not p.endswith('.py')])
```

`d17_n_vs_c.py`:

```python
"""D-17 r1: compare the -n reproduction with the -c reproduction (both path:count, UTF-8 with or without BOM)."""
import sys
def load(p):
    d = {}
    for ln in open(p, 'rb').read().decode('utf-8-sig').splitlines():
        if ln.strip():
            k, n = ln.rsplit(':', 1); d[k] = int(n)
    return d
n, c = load(sys.argv[1]), load(sys.argv[2])
print('-n: entries %d lines %d | -c: entries %d lines %d | identical: %s' % (len(n), sum(n.values()), len(c), sum(c.values()), n == c))
print('binary paths in -n output:', [k for k in n if k.endswith(('.pyc', '.zip'))])
```

`d17_local_binary_control.sh`:

```bash
#!/bin/bash
# Background control on rg 14.1.0 (not the incident's 15.2.0): copies of the four binary files from 25c7d51.
cd "$1" || exit 2
E='write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
echo "rg $(rg --version | head -1 | cut -d' ' -f2); -n; files found by recursion under '.'"
rg -n "$E" . > "$2/o.txt" 2> "$2/e.txt" < /dev/null; echo "exit $? stdout_lines $(wc -l < "$2/o.txt") stderr_lines $(wc -l < "$2/e.txt")"
echo "control: -c --binary (path:count)"
rg -c --binary "$E" . < /dev/null | sort
rm -f "$2/o.txt" "$2/e.txt"
```

`p2_text_classify.py`:

```python
"""P-2: classify E-matching lines outside the audit's own reading scope, printing features only (never line content)."""
import ast, json, re, subprocess
E = re.compile(r'write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10\.py')
FILES = ['clustering/base_clustering.py', 'modules/experimental/run_driver.py', 'modules/experimental/toy_datasets.py',
         'results/result_plotter_KMeans_KMedoids.py', 'results/result_plotter_Spectral.py', 'results/results_plotter_GMM.py',
         'viz/plotters/geo_names_plotter.py', 'notebooks/2-web-scraping-yok-atlas.ipynb', 'notebooks/data-preprocessing-election.ipynb',
         'notebooks/data-preprocessing-maps.ipynb', 'notebooks/data-preprocessing-population.ipynb']
def features(code):
    s = code.strip()
    parsed = False
    for cand in (s, s.rstrip(':') , s + ' pass' if s.endswith(':') else s, s.rstrip(',')):
        try: ast.parse(cand); parsed = True; break
        except SyntaxError: pass
    strs = re.findall(r'(["\'])(.*?)\1', s)
    str_kinds = sorted({('path' if re.search(r'[/\\]|\.(csv|xlsx|xls|pkl|json|png|eps|pdf|txt|geojson)$', v) else 'fstring/other') for _, v in strs})
    nums = [n for n in re.findall(r'(?<![\w.])\d+(?:\.\d+)?(?![\w.])', re.sub(r'(["\']).*?\1', '', s))]
    return parsed, len(s), str_kinds, len(nums), max((len(n) for n in nums), default=0)
total = 0
for p in FILES:
    lines = subprocess.run(['git', 'show', '25c7d51:' + p], capture_output=True, check=True).stdout.decode('utf-8').splitlines()
    nb = p.endswith('.ipynb'); region = None
    for k, ln in enumerate(lines, 1):
        st = ln.strip()
        if nb:
            if st.startswith('"source"'): region = 'source'
            elif st.startswith('"outputs"'): region = 'outputs'
        m = E.search(ln)
        if not m: continue
        total += 1
        code = ln
        if nb:
            frag = st.rstrip(',')
            try: code = json.loads(frag) if frag.startswith('"') else frag
            except Exception: code = frag
        parsed, length, kinds, nnum, maxdig = features(code)
        tok = m.group(0) if len(m.group(0)) < 20 else m.group(0)[:17] + '...'
        print('%-48s %5d %-8s token=%-12s parses=%-5s len=%3d strings=%s numerals=%d maxdigits=%d' % (p, k, region or '-', tok, parsed, length, kinds, nnum, maxdig))
print('lines classified:', total)

print('--- digits inside string literals of the same lines (counts only)')
for p in FILES:
    lines = subprocess.run(['git', 'show', '25c7d51:' + p], capture_output=True, check=True).stdout.decode('utf-8').splitlines()
    for k, ln in enumerate(lines, 1):
        if not E.search(ln): continue
        code = ln.strip()
        if p.endswith('.ipynb'):
            frag = code.rstrip(',')
            try: code = json.loads(frag) if frag.startswith('"') else frag
            except Exception: code = frag
        inner = ''.join(v for _, v in re.findall(r'(["\'])(.*?)\1', code))
        runs = re.findall(r'\d+', inner)
        decimals = re.findall(r'\d+\.\d+', inner)
        print('%-48s %5d digit_runs_in_strings=%d longest=%d decimal_numbers=%d' % (p, k, len(runs), max((len(r) for r in runs), default=0), len(decimals)))
```

`p2_keyword_screen.py`:

```python
"""P-2 screen: for each of the 35 out-of-scope E-matching lines, flag evaluative / outcome vocabulary.
Prints file:line and the NAMES of the flags that fire, never the line content."""
import json, re, subprocess
E = re.compile(r'write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10\.py')
FILES = ['clustering/base_clustering.py', 'modules/experimental/run_driver.py', 'modules/experimental/toy_datasets.py',
         'results/result_plotter_KMeans_KMedoids.py', 'results/result_plotter_Spectral.py', 'results/results_plotter_GMM.py',
         'viz/plotters/geo_names_plotter.py', 'notebooks/2-web-scraping-yok-atlas.ipynb', 'notebooks/data-preprocessing-election.ipynb',
         'notebooks/data-preprocessing-maps.ipynb', 'notebooks/data-preprocessing-population.ipynb']
FLAGS = {
 'superlative/evaluative': r'best|worst|optimal|optimum|winner|win|better|top|rank|en_?iyi|iyi|kotu|kötü|üstün|ustun|başar|basar',
 'cvi/metric name': r'silhouette|dunn|davies|calinski|ari\b|nmi|ami|inertia|aic|bic|score|metric|cvi|loglik|likelihood|accuracy|purity',
 'k / cluster count': r'\bk\s*=|_k\d|k_?\d|n_clusters|best_k|optimal_k|num_clusters|cluster_count',
 'result/summary word': r'result|summary|sonuc|sonuç|ozet|özet|report|rapor|consensus|label',
 'algorithm name': r'kmeans|kmedoids|gmm|spectral|hierarch|dbscan|agglom|tskmeans|timeseries',
}
for p in FILES:
    lines = subprocess.run(['git', 'show', '25c7d51:' + p], capture_output=True, check=True).stdout.decode('utf-8').splitlines()
    for k, ln in enumerate(lines, 1):
        if not E.search(ln): continue
        code = ln.strip()
        if p.endswith('.ipynb'):
            frag = code.rstrip(',')
            try: code = json.loads(frag) if frag.startswith('"') else frag
            except Exception: code = frag
        strings = ' '.join(v for _, v in re.findall(r'(["\'])(.*?)\1', code)).lower()
        rest = re.sub(r'(["\']).*?\1', ' ', code).lower()
        fs = [name for name, rx in FLAGS.items() if re.search(rx, strings)]
        fc = [name for name, rx in FLAGS.items() if re.search(rx, rest)]
        print('%s:%d | in strings: %s | in code: %s' % (p, k, fs or '-', fc or '-'))
```

## 8. The PI's outputs, verbatim

### 8.1 Directory listing outside the clones (Git Bash, as relayed by the PI)

```text
$ find /g/PycharmProjects/rp1r2_audit -path '*/ref' -prune -o -path '*/run' -prune -o -type f -printf '%TY-%Tm-%Td %TH:%TM:%TS %s %p\n' | sort
2026-10-12 19:55:22.2287779000 410 /g/PycharmProjects/rp1r2_audit/.idea/inspectionProfiles/Project_Default.xml
2026-10-12 19:55:22.7060308000 342 /g/PycharmProjects/rp1r2_audit/.idea/rp1r2_audit.iml
2026-10-12 19:55:22.7399379000 281 /g/PycharmProjects/rp1r2_audit/.idea/modules.xml
2026-10-12 19:55:22.7509094000 206 /g/PycharmProjects/rp1r2_audit/.idea/misc.xml
2026-10-12 19:55:22.7608822000 2944 /g/PycharmProjects/rp1r2_audit/.idea/workspace.xml
2026-10-12 19:55:22.7967855000 694 /g/PycharmProjects/rp1r2_audit/.idea/claudeCodeTabState.xml
2026-10-12 19:55:22.8596180000 174 /g/PycharmProjects/rp1r2_audit/.idea/inspectionProfiles/profiles_settings.xml
2026-10-12 19:59:54.1356064000 238 /g/PycharmProjects/rp1r2_audit/.idea/.gitignore
2026-10-12 20:05:12.4529752000 2605 /g/PycharmProjects/rp1r2_audit/audit_clone_verification_2026-10-12.md
2026-10-12 20:32:08.1102117000 5111 /g/PycharmProjects/rp1r2_audit/audit_support/custody.py
2026-10-12 20:32:14.9846562000 2968 /g/PycharmProjects/rp1r2_audit/audit_support/intake.json
2026-10-12 20:32:31.7679143000 820057 /g/PycharmProjects/rp1r2_audit/audit_support/custody.json
2026-10-12 20:34:51.2368026000 12531 /g/PycharmProjects/rp1r2_audit/audit_support/stop_report.py
2026-10-12 20:34:59.8577939000 1884 /g/PycharmProjects/rp1r2_audit/audit_support/stop_state.json
2026-10-12 20:34:59.8587912000 2169 /g/PycharmProjects/rp1r2_audit/audit_support/scope_incident.json
2026-10-12 20:34:59.8667922000 40913 /g/PycharmProjects/rp1r2_audit/f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
2026-10-12 20:34:59.8687622000 143 /g/PycharmProjects/rp1r2_audit/f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md.sha256
```

### 8.2 Hashes of the pre-window support files (Git Bash, as relayed by the PI)

```text
$ sha256sum /g/PycharmProjects/rp1r2_audit/audit_support/custody.py /g/PycharmProjects/rp1r2_audit/audit_support/intake.json /g/PycharmProjects/rp1r2_audit/audit_support/custody.json
7fdd3fa1748b5f431d15518a53d723c0b9fdfb4186704df5d0186d88ec5f9c40 */g/PycharmProjects/rp1r2_audit/audit_support/custody.py
e38f49f35371aa61463b5f17a4f0e87d301bb18c0f7810e75b032d3f5e4bc67f */g/PycharmProjects/rp1r2_audit/audit_support/intake.json
10965cb107c1d4498745e83252da79e9480f23f7edf9e31dae19b2a690fe94b7 */g/PycharmProjects/rp1r2_audit/audit_support/custody.json

$ where.exe rg

INFO: Could not find files for the given pattern(s).
```

### 8.3 b2_rg_repro_counts.txt (05a5de98…, as uploaded; BOM removed for display)

```text
f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md:7
audit_support\custody.py:1
audit_support\scope_incident.json:1
audit_support\stop_report.py:5
run\modules\experimental\toy_datasets.py:1
run\viz\plotters\geo_names_plotter.py:2
run\modules\experimental\run_driver.py:3
ref\notebooks\data-preprocessing-population.ipynb:16
run\clustering\base_clustering.py:2
ref\notebooks\data-preprocessing-maps.ipynb:1
ref\viz\plotters\geo_names_plotter.py:2
ref\notebooks\data-preprocessing-election.ipynb:2
ref\notebooks\2-web-scraping-yok-atlas.ipynb:1
ref\modules\experimental\toy_datasets.py:1
ref\modules\experimental\run_driver.py:3
run\results\result_plotter_Spectral.py:2
run\results\result_plotter_KMeans_KMedoids.py:2
run\results\results_plotter_GMM.py:3
run\p_konum_plus\manifests\f1_input_hash_table_2026-08-28.csv:12
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py:18
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py:18
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py:18
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py:18
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py:18
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py:13
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py:13
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py:13
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py:13
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py:15
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py:13
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py:13
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py:10
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py:10
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py:10
run\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py:10
run\p_konum_plus\calibration\f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py:3
run\p_konum_plus\calibration\f3_rp1-r2_prepare_review_records_2026-10-10.py:5
run\p_konum_plus\calibration\f3_rp1-r2_logged_preflight_2026-10-10.py:4
run\p_konum_plus\calibration\f3_rp1-r2_launch_attempt_2026-10-10.py:3
run\p_konum_plus\calibration\f3_rp1-r2_finalize_delivery_2026-10-12.py:5
run\p_konum_plus\quarantine\f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md:1
run\p_konum_plus\quarantine\f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md:1
run\p_konum_plus\quarantine\f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md:1
run\p_konum_plus\quarantine\f3_step2_rp1-r2_attempt1_2026-10-11\calibration\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
run\notebooks\data-preprocessing-population.ipynb:16
run\notebooks\data-preprocessing-maps.ipynb:1
run\notebooks\data-preprocessing-election.ipynb:2
run\notebooks\2-web-scraping-yok-atlas.ipynb:1
run\p_konum_plus\calibration\f3_step2_adequacy_harness_r4-2_2026-09-30.py:17
run\p_konum_plus\calibration\f3_step2_adequacy_harness_r4-1_2026-09-29.py:14
run\p_konum_plus\calibration\f3_step2_adequacy_harness_r3_2026-09-22.py:10
run\p_konum_plus\calibration\f3_step2_adequacy_harness_r2_2026-09-07.py:4
run\p_konum_plus\calibration\f3_step2_adequacy_harness_r1_2026-09-06.py:1
run\p_konum_plus\calibration\f3_rp1-r2_write_custody_2026-10-10.py:2
run\p_konum_plus\calibration\f3_rp1-r2_technical_tests_2026-10-10.py:2
run\p_konum_plus\calibration\f3_rp1-r2_small_input_tests_2026-10-10.py:10
run\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1_2026-10-02.py:18
run\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
run\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:18
run\p_konum_plus\calibration\f3_step2_adequacy_harness_r4_2026-09-24.py:13
run\p_konum_plus\provenance\f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
run\p_konum_plus\provenance\f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11\f3_rp1-r2_launch_attempt_2026-10-10.py:3
run\p_konum_plus\calibration\f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff:4
run\p_konum_plus\calibration\f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff:9
ref\results\result_plotter_Spectral.py:2
ref\results\result_plotter_KMeans_KMedoids.py:2
ref\results\results_plotter_GMM.py:3
run\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_harness_diff_vs_rp1-r1_2026-10-12.diff:6
run\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_harness_diff_vs_r4-2_2026-10-12.diff:7
run\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_authored_edits_2026-10-10.json:3
run\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_attempt2_harness_provenance_diff_2026-10-11.diff:3
run\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md:2
run\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_attempt2_provenance_changes_2026-10-11.json:2
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py:18
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py:18
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py:18
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py:18
run\p_konum_plus\prompts\f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md:11
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py:18
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py:13
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py:13
ref\p_konum_plus\manifests\f1_input_hash_table_2026-08-28.csv:12
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py:13
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py:13
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py:15
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py:13
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py:13
run\p_konum_plus\prompts\f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md:5
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py:10
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py:10
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py:10
ref\p_konum_plus\quarantine\f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py:10
ref\clustering\base_clustering.py:2
run\p_konum_plus\prompts\f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md:20
ref\p_konum_plus\calibration\f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py:3
ref\p_konum_plus\calibration\f3_rp1-r2_prepare_review_records_2026-10-10.py:5
run\p_konum_plus\prompts\f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md:32
ref\p_konum_plus\quarantine\f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md:1
ref\p_konum_plus\quarantine\f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md:1
ref\p_konum_plus\calibration\f3_rp1-r2_logged_preflight_2026-10-10.py:4
ref\p_konum_plus\calibration\f3_rp1-r2_launch_attempt_2026-10-10.py:3
ref\p_konum_plus\calibration\f3_rp1-r2_finalize_delivery_2026-10-12.py:5
ref\p_konum_plus\quarantine\f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md:1
ref\p_konum_plus\quarantine\f3_step2_rp1-r2_attempt1_2026-10-11\calibration\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_r4_2026-09-24.py:13
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_r4-2_2026-09-30.py:17
ref\p_konum_plus\calibration\f3_rp1-r2_technical_tests_2026-10-10.py:2
ref\p_konum_plus\calibration\f3_rp1-r2_small_input_tests_2026-10-10.py:10
ref\p_konum_plus\calibration\f3_rp1-r2_write_custody_2026-10-10.py:2
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_r4-1_2026-09-29.py:14
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_r1_2026-09-06.py:1
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1_2026-10-02.py:18
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:18
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_r2_2026-09-07.py:4
ref\p_konum_plus\calibration\f3_step2_adequacy_harness_r3_2026-09-22.py:10
ref\p_konum_plus\provenance\f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py:22
ref\p_konum_plus\provenance\f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11\f3_rp1-r2_launch_attempt_2026-10-10.py:3
ref\p_konum_plus\calibration\f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff:4
ref\p_konum_plus\calibration\f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff:9
ref\p_konum_plus\prompts\f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md:11
ref\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_harness_diff_vs_rp1-r1_2026-10-12.diff:6
ref\p_konum_plus\prompts\f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md:5
ref\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_harness_diff_vs_r4-2_2026-10-12.diff:7
ref\p_konum_plus\prompts\f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md:20
ref\p_konum_plus\prompts\f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md:32
ref\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_authored_edits_2026-10-10.json:3
ref\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md:2
ref\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_attempt2_provenance_changes_2026-10-11.json:2
ref\p_konum_plus\provenance\f3_realdata_prep_rp1-r2_attempt2_harness_provenance_diff_2026-10-11.diff:3
```

### 8.4 Line classification proposed by the drafter (P2_text_lines_classification_2026-10-12.csv, 8730b2f0…, verbatim)

```text
file,line,screen_flags_in_strings,screen_flags_in_code,proposed_class,reason
clustering/base_clustering.py,302,-,result/summary word,K2,writes a summary table to CSV; file name built from variables only
clustering/base_clustering.py,303,result/summary word,result/summary word,K2,writes consensus labels to CSV; file name is a fixed descriptive label plus a variable; no value
modules/experimental/run_driver.py,625,-,-,K2,serialises a payload variable to JSON; numeral = indent width
modules/experimental/run_driver.py,653,result/summary word,-,K2,writes a QC summary table to CSV under a fixed descriptive file name
modules/experimental/run_driver.py,679,-,-,K2,"first line of a JSON dump of timing variables; key names only, no values"
modules/experimental/toy_datasets.py,181,-,result/summary word,K2,pickles a run-summary variable
results/result_plotter_KMeans_KMedoids.py,101,-,-,K2,writes a rounded table to CSV; file name built from two variables only; the numeral is the rounding precision argument
results/result_plotter_KMeans_KMedoids.py,103,superlative/evaluative,superlative/evaluative,K3,"writes a rounded, transposed table of best rows to CSV; file name built from variables plus a ""best"" label; numeral = rounding precision; no value"
results/result_plotter_Spectral.py,382,"superlative/evaluative, algorithm name",superlative/evaluative,K3,"writes a transposed table of best rows to CSV; f-string file name carries the algorithm name, two variables and a ""best"" label; no value"
results/result_plotter_Spectral.py,385,algorithm name,-,K3,writes the full table to CSV; f-string file name carries the algorithm name and two variables; no value
results/results_plotter_GMM.py,176,"superlative/evaluative, cvi/metric name, algorithm name",superlative/evaluative,K3,"writes a per-setting table of the best rows to CSV; f-string file name carries the algorithm name, the metric name and a ""best"" label; no value, no comparison result"
results/results_plotter_GMM.py,179,"cvi/metric name, algorithm name",-,K3,writes a metric table to CSV; f-string file name carries algorithm and metric names; no value
results/results_plotter_GMM.py,182,"cvi/metric name, algorithm name",-,K3,writes a metric table to CSV; f-string file name carries algorithm and metric names; no value
viz/plotters/geo_names_plotter.py,337,-,result/summary word,K2,converts two columns of a frame to CSV text in memory; column names only
viz/plotters/geo_names_plotter.py,537,-,-,K2,converts two display columns to CSV text in memory for a cache key; column names only
notebooks/2-web-scraping-yok-atlas.ipynb,168,-,-,K1,code cell: writes a scraped template table to CSV; fixed file name
notebooks/data-preprocessing-election.ipynb,1669,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-election.ipynb,2455,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-maps.ipynb,260,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,165,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,272,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,385,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,463,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,537,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,609,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,622,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,677,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,730,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,1081,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,1268,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,1358,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,1790,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,1993,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,2083,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
notebooks/data-preprocessing-population.ipynb,2307,-,-,K1,"code cell: writes a preprocessed table to a CSV under data/preprocessed/ or temp/; file name names the dataset and, in some cases, its year range; no clustering content"
```

### 8.5 The PI's PowerShell outputs for P-2 (as relayed by the PI, verbatim) and the commands given

```text
commands as given to the PI by the drafter (G:\PycharmProjects\rp1r2_audit, Windows PowerShell):
  $rg = 'C:\Users\Neo\.codemoss\dependencies\codex-sdk\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\codex-path\rg.exe'
  $E = 'write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
  & $rg --help | Select-String -Pattern 'NUL byte occurs after a match' -Context 3,3
  & $rg -n $E ref\temp\eps run\temp\eps ref\clustering\__pycache__ run\clustering\__pycache__ ref\viz\plotters\__pycache__ run\viz\plotters\__pycache__ 2> G:\PycharmProjects\b2_bin_stderr.txt | Measure-Object -Line
  & $rg -n $E 2> G:\PycharmProjects\b2_rg_n_stderr.txt | ForEach-Object { ($_ -split ':', 2)[0] } | Group-Object -NoElement | ForEach-Object { '{0}:{1}' -f $_.Name, $_.Count } | Set-Content -Encoding UTF8 G:\PycharmProjects\b2_rg_n_counts.txt

output of the binary-directory command, as relayed:
Lines Words Characters Property
----- ----- ---------- --------
    0

help search, as relayed:
PS G:\PycharmProjects\rp1r2_audit> & $rg --help | Select-String -Pattern 'NUL byte occurs after a match' -Context 3,3
PS G:\PycharmProjects\rp1r2_audit>
```

## 9. Changes from the DRAFT (acb669e5…) — review relayed by the PI on 2026-10-12 (ChatGPT; the one review round of D-11 r1 §6)

| # | where | change | reason |
|---|---|---|---|
| 1 | §1 (3), §2, §7, §8.5 | binary files: the decisive evidence is now the reproduction in the incident's own mode (-n), whole directory and the binary directories given explicitly (no line, no warning); the -c run is kept as supporting only; the 15.2.0 help search (no line) recorded without a documentation claim; the 14.1.0 control marked as background | the DRAFT used the -c run as a reproduction of the incident's -n output behaviour |
| 2 | §1 (4), §2, §3, §8.4 | text lines: a file:line – class – reason record of all 35 lines by their meaning (K1 20, K2 9, K3 6, K4 0), adopted by the PI's signature under decision 1; the feature and keyword screens kept as supporting checks; provenance of the drafter's reading of the lines stated | the DRAFT's feature script did not assess meaning (e.g. a file name could carry a superiority claim) |

No other change.

## 10. Changes from DRAFT r1 (c8636e0f…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, banner, header | DRAFT r1 → signed; file name without DRAFT; drafts and status lines; banner states decision 1 and that the record opens the repeated audit only | PI approval |
| 2 | header "what_this_record_is_not", §3 | "not PASSED" and "not a D-9 §2 (a) binding" stated; §3 records decision 1, option 2 kept as presented, and adds the scope line | PI approval (relayed review: "PASSED veya PI bağlaması anlamına gelmez") |
| 3 | §6 | decision 1; adoption of §8.4; acceptance of the §2 residual; scope; approval message verbatim with its referents; time of recording | PI approval |

No other change: §1, §2, §4, §5, §7, §8 and §9 stand as in DRAFT r1.
