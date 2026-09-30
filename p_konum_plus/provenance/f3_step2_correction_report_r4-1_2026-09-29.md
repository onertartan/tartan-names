# p_konum_plus — F3 STEP-2 r4-1 — Correction Report

```text
artifact_role = correction report (deliverable 10, r4-1 revision inside the r4 cycle)
status        = NON-NORMATIVE narrative over the hashed artifacts it cites
date          = 2026-09-29 (revision tag) ; launches 2026-09-29 .. 2026-09-30
```

No wording in this report asserts "verified", "QUALIFIED", or "audit PASS" about the
executor's own output. `F3_STEP2 = QUALIFIED` can be declared only by the PI after an
independent audit, which this report does not perform.

## 1. The PI's dispatch messages, verbatim (per the PI's own instruction)

Message dispatching the r4-1 revision (2026-09-29):

```text
Ekteki r4-1 talimatını ve dispatch kaydını (D-6) uygula. Kapsam D-6 §3'te: R4A-01, 02, 03, 04 ve 10; R4A-08
kapsam dışı. S-R2-1 ve T-R2-2 D-5'teki gibi. r3, r4 ve karantina dosyalarının hiçbirini değiştirme, yeniden
adlandırma veya taşıma. Her düzeltmeyi yalnız ilgili test gerçekten çalışıp geçtiğinde kapat. Sonunda
transmission listesindeki tüm dosyaları, stdout ve stderr log'ları dahil, eksiksiz gönder.
```

Follow-up (instrument verification, 2026-09-29):

```text
Üç .md dosyası Downloads'a eklendi. Dördünü de sidecar'larına karşı doğrula; talimattaki hash'ler D-6 §1 ve
sidecar'larla aynı olmalı. Sonra planladığın gibi devam et.
```

Both were carried out: the four r4-1 instruments were verified EQUAL to their sidecars and
D-6 §1 before the first write (§2); the scope applied is exactly D-6 §3 (R4A-01, 02, 03,
04, 10; R4A-08 NOT applied); each correction was closed only when its test ran and passed
(§4-5); no r3, r4 or quarantine file was modified, renamed or moved (§7); the full
transmission set, including both stdout and stderr logs, is in §8.

## 2. Custody (D-3 S3 / r4 instruction S1 / r4-1 instruction S1; every value OBSERVED)

Instruments, observed = pinned = EQUAL for all nine (verified by the external W-3 writer
AND re-verified by every harness launch — "DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS; 9
instruments"):

| instrument | path (p_konum_plus/prompts/) | sha256 |
|---|---|---|
| D-1 (v6) | Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md | 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 |
| D-2 (content) | f3_step2_pi_ratified_content_2026-09-07.md | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 |
| D-3 (standing) | Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 |
| r4 instruction (standing) | Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md | e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 |
| D-5 (r4 dispatch record; parent) | f3_step2_r4_pi_dispatch_record_2026-09-24.md | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 |
| **r4-1 instruction** | Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md | 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330 |
| **D-6 (r4-1 dispatch record)** | f3_step2_r4-1_pi_dispatch_record_2026-09-29.md | a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0 |
| A-1 (r3 audit; input) | f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md | 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6 |
| A-2 (r4 audit DRAFT r1; input) | f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md | b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a |
| A-3 (r4 audit DRAFT r2; input) | f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md | 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9 |

P-4 evidence = D-6 (path and hash above; child of D-5). S/T as read, carried unchanged
from D-5 by D-6 §2: S-1=(a); S-2=alpha; T-1=AUTHORIZE; T-2=T-2a; T-3=AUTHORIZE; T-4=T-4a;
T-5=CONFIRM_WITHIN_SCOPE; **S-R2-1=PI_RULE** (rule text D-5 S3, still cited to D-5);
**T-R2-2=AUTHORIZE_RESTART**.

Deliverables of this revision (hash block; every file with an external .sha256 sidecar):

| # | file | sha256 |
|---|---|---|
| 1 | calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py (attempt 3) | 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f |
| 2 | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3 | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4 | provenance/f3_step2_r4-1_preexecution_custody_2026-09-29.md (attempt 3; written externally) | 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d |
| 5 | calibration/f3_step2_telemetry_r4-1_2026-09-29.csv | 85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167 |
| 6 | calibration/f3_step2_results_r4-1_2026-09-29.json | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 |
| 7 | calibration/f3_step2_residual_series_r4-1_2026-09-29.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 | calibration/f3_step2_test_evidence_r4-1_2026-09-29.json | f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd |
| 9 | calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md (child of r4 register 0eed314c) | (sidecar) |
| 10 | provenance/f3_step2_correction_report_r4-1_2026-09-29.md (this file) | (sidecar) |
| 11 | provenance/f3_step2_r4-1_start_state_inventory_2026-09-29.md (R4A-04) | (sidecar) |
| 12 | provenance/f3_step2_r4-1_attempt_log_2026-09-29.md (incl. ERRATUM-2, R4A-10) | (sidecar) |
| A | calibration/f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv (12,174 rows, all phases, all pids) | 22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88 |
| B | calibration/f3_step2_r4-1_restart_store_manifest_2026-09-29.csv (11,869 rows; path, size, sha256, pid, start_iso) | cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1 |
| C | calibration/f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv (R4A-01(f); 37 rows) | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| D | run logs (stdout + stderr) + quarantine notes/snapshots — see §8 | (sidecars) |

The residual-series hash equals the r4 verified export byte-for-byte (same fits, same
injection-aware Y-21 exporter) — continuity evidence, not reuse (recomputed from RUN1's own
fit objects this revision; export-phase optimizer calls = 0, asserted).

## 3. Execution (D-3 S8; full detail in the attempt log)

3 attempts (harness byte changes), 4 launches, 2026-09-29 20:24 .. 2026-09-30 13:03.
Attempt 1 ran with the restart layer OFF and was interrupted externally at SPL ctx 41 — the
FIRST genuine interruption of the r4-1 revision; the layer was introduced at attempt 2 per
D-3 S8.2/S8.3. Attempt 2 ran the WHOLE computation but stopped at the T-NONREG-R4 self-check
(a representation bug in the check, not a regression — §4, R4A-01(f)); its store was
quarantined whole and attempt 3 restarted empty. Attempt 3 spanned two launches (interrupted
after RUN1, resumed from the 7,271-unit store). Final launch (4; pid 7972): exit 0,
**DETERMINISM = True** (RUN1 == RUN2 canonical SHA256 =
`556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77`); T-SINGLE-PROCESS =
NOT_RUN (units from 2 processes); T-RESTART-PROVENANCE 3/3 (attempt log).

One defect was found and fixed INSIDE this revision by its own new gate: the R4A-01(f)
non-regression check (T-NONREG-R4) compared in-memory native floats against the canon()-ized
(hex) r4 results, spuriously flagging 33/34 shared fixtures; fixed by canonicalizing both
sides. No fit or decision was affected (T-EXPECT-ALL and the determinism gate passed in the
same attempt-2 run). Quarantine note: `f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md`.

## 4. Response table — the r4 audit's R4A items (scope D-6 §3)

| item | status | evidence |
|---|---|---|
| **R4A-01** (blocker) | **CLOSED** | spline-context UNRELATED-pending routed into the decision grammar (register PIN-SPLINE-PENDING-ROUTING): full→C3/C4b, fold→C2, probe→C4b, C4a NOT routed; tag TEST_ONLY_INJECTED / F3-STEP2-EXACT-04. Fixtures INJ-SPL-PENDING-FULL/FOLD/PROBE + the eval-level assertion in T-EXC-UNRELATED-TYPE + T-EXPECT-ALL 36/36 all PASS; p03=(PENDING,PENDING), mechanism=MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED); C4a stays PASS; RUN1==RUN2. Drafter choice (1) honored: propagates exactly as a5v does |
| **R4A-01(f)** | **CLOSED** | non-regression vs r4 results a15b7eff (register PIN-NONREGRESSION-VS-R4): p03/criteria/dp04/mechanism/stops compared per shared fixture, both sides canon-normalized; T-NONREG-R4 PASS — shared=34, new=3, dropped=0, **findings=0**, real_path_spline_pending=0. Delivered CSV (item C) |
| **R4A-02** | **CLOSED** | coverage resolver admits generic T-*/NR-* ids (register PIN-COVERAGE-DERIVED amended); COVERAGE_DERIVED = 64 rows, **downgraded_to_UNCOVERED = []** — the four r4 conservative downgrades (C2 pass, C3 pass, D-P04-comparator-NaN, clean-execution) now resolve from their ran/passed test records; three coverage rows added for the R4A-01 fixtures |
| **R4A-03** | **CLOSED** | guarded-comparator STOP relabelled CONTRACT_VIOLATION_INCONSISTENT_U (register PIN-GUARDED-COMPARATOR amended); offending-pairs deduped on (sex,fitter,observation) each carrying sex (PIN-REVALIDATION-INCONSISTENT-U amended); tag TEST_ONLY_INJECTED. T-COMPARATOR-NAN (now with a crafted end-to-end inconsistent-U path) PASS; INJ-U-POST-CONSTRUCTION-INVALID one deduped pair {sex:F,fitter:P01,obs:0}; the change is the sole whitelisted EXPECTED_R4A03 diff in T-NONREG-R4 |
| **R4A-04** | **CLOSED** | r4-1 start-state inventory authored (deliverable 11): instrument hashes; the r4 package read-only non-retro hashes; the five r3 per-revision custody triples recomputed exactly (fingerprints incl. 548ae790 = ATTEMPT8 triple); R4A-10(iii) hash search |
| **R4A-08** | **NOT APPLIED** | optional; excluded by D-6 §3 (PI selection "Blocker + tüm cleanup", R4A-08 out of scope) |
| **R4A-10** | **CLOSED** | ERRATUM-2 in the r4-1 attempt log (r3/r4 files untouched, hash-referenced); quarantine ANNOTATION note (renames nothing); the three named-but-unfiled r3 bytes (d67e097d, e35c2bf0, 390f42b7) NOT_PRESERVED; the r4 report §8(c) statement corrected in §8 below |

## 5. Carried forward from r4 (re-verified under the r4-1 run)

The r4 cycle's Y-01..Y-21 and R3A-01..R3A-17 closures (r4 report §4-5) stand; every retained
pin ran and passed in the r4-1 run (T-EXPECT-ALL 36/36, EXPECTATION_FAIL=[]; captures
RUN1==RUN2; T-CANON RUN1==RUN2=556106e7; T-CALLCOUNT run1 5256 == run2 5256; 28/28 tests_run
passed). S-R2-1 = PI_RULE and T-R2-2 = AUTHORIZE_RESTART are unchanged (D-6 §2).

## 6. Coverage matrix (derived; 64 rows)

64 rows derived; **downgraded_to_UNCOVERED = []**. The only UNCOVERED row is the authored
`A.5 (iii) inadmissible refit` (unchanged; D-5 S7 anticipated it; no construction possible
without touching frozen code — Y-16). The four r4 conservative downgrades (C2 pass, C3 pass,
D-P04-comparator-NaN, clean-execution) are RESOLVED by the R4A-02 resolver-id grammar, each
from a test that ran and passed this run. No downgrade hides a failed test (28/28 passed).

## 7. Attempt histories and parents

- r4-1: 3 attempts / 4 launches — the attempt log (deliverable 12).
- r4: 8 launches / 5 revisions — historical, read-only (r4 attempt log, referenced not
  modified). r3: 10 launches / 5 revisions — historical. r2/r1: as disclosed in prior cycles.
- parents_unchanged = true: the r4 package (harness 54274b4e, generator 39391730, manifest
  c0b38ceb, results a15b7eff, residual 3ee624f3, test-evidence 118c3507, register 0eed314c,
  report 5c9dea88, attempt log 84090147, percall d7f689fe, store manifest f3c923b1) is at the
  exact hashes the r4-1 instruction's non-retroactivity block prints, re-verified 2026-09-29
  (start-state inventory §2). No r3, r4 or pre-existing quarantine file was modified, renamed
  or moved by this revision.

## 8. Transmission set (r4-1 instruction S2) + R4A-10 correction of r4 report §8(c)

(a) sidecars of the r4-1 deliverables 1-12 + A/B/C: written this revision, all verifying.
(b) run logs: `calibration/f3_step2_r4-1_run_stdout_2026-09-29.log` and
    `..._run_stderr_2026-09-29.log` (final attempt-3 launch), plus the per-attempt copies in
    quarantine (attempt1/attempt2 stdout+stderr).
(c) r4-1 quarantine artifacts (all NEW r4-1 files; nothing renamed/moved from r3/r4):
    attempt-1 interruption note; attempt-2 nonreg-canon-bug supersession note; the recovered
    attempt-2 harness snapshot (`..._ATTEMPT2_NONREG_CANON_BUG.py`, byte-exact 280869892d);
    the attempt-2 store quarantined whole (`r4-1_restart_store_..._ATTEMPT2_NONREG_CANON_BUG/`,
    11,869 units); the quarantine label annotation note (R4A-10(ii)).
(d) **Correction of the r4 report §8(c) (R4A-10).** The r4 correction report §8(c) lists
    `d67e097d...` among superseded r3 harness bytes "present in quarantine". This is
    **incorrect**: a repository + quarantine search (2026-09-29, restart-store dirs excluded)
    found `d67e097d...` NOT_PRESERVED; the file under the ATTEMPT5 harness label is
    `f882b922...`. Likewise the ATTEMPT8 label holds `99f895c1...` (not `390f42b7...`) and the
    generator `e35c2bf0...` (attempts 1-5) is NOT_PRESERVED. Full reconciliation in the
    quarantine annotation note and the attempt-log ERRATUM-2. The r4 report itself is
    historical and is NOT edited; this is the record of the correction. No delivered output is
    affected (§ERRATUM-2(4)).

## 9. Process block (incl. the models note)

```text
attempts                = 3 (harness byte changes: b22708d2 OFF, 280869892d ON, 4e0dc8cf ON)
launches                = 4 (pids 19528, 3348, 22616, 7972) ; W-3 written once per attempt,
                          externally, observed values
final process           = pid 7972, 2026-09-30T12:44:02 .. 13:03:07, exit 0
units (final process)   = computed: run2 2, residual_export 1 ; read from store: nr_gates 1,
                          unit_tests 1, run1 2 (store 11,869; 7,271 pid 22616 + 4,598 pid 7972)
per-call optimizer rows = 12,174 (nr_gates 60 ; unit_tests 1602 ; run1 5256 ; run2 5256 ;
                          export 0) ; by pid: 22616 -> 6918, 7972 -> 5256
executor_models         = the r4-1 revision ran under claude-opus-4-8[1m] (Opus 4.8, 1M
                          context). Reasoning-effort: no explicit effort override configured
                          (harness default); the executor cannot observe an internal effort
                          parameter and reports only what the session exposed.
real_data_access        = false ; commit = false (throughout)
```

## 10. End state (v6 S13/S14, D-3 S10; every field computed — from results end_state)

```text
PI_dispatch_record_hash     = 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 (D-5, as END_STATE records; D-6 a92a0518 is this revision's dispatch, §2)
S-R2-1 = PI_RULE (verbatim, as read) ; T-R2-2 = AUTHORIZE_RESTART (verbatim, as read)
corrections_complete        = true   (all mandatory tests ran AND passed; EXPECTATION_FAIL = [])
mandatory_tests_all_run     = true   (mandatory_tests_missing = [])
expectation_checks          = 36 / 36 ; EXPECTATION_FAIL = none
tests_run                   = 28 / 28 passed
non_regression_vs_r4        = shared 34, new 3, dropped 0, findings 0 (T-NONREG-R4 PASS)
deferred_decisions          = []     (EXACT-03 CLOSED with D-5 as source, D-5 S4(d))
narrowed_evidence           = [T-R2-2]
uncovered_coverage_rows     = ["A.5 (iii) inadmissible refit"]   (the r4 conservative downgrades resolved, R4A-02)
open_findings               = []     (no natural UNRELATED event; NATURAL_UNRELATED_EVENTS = 0; EXACT-04 not opened)
parents_unchanged           = true   (r4 package at the non-retro hashes; §7)
determinism                 = true   (RUN1 == RUN2 = 556106e7... over the enlarged document)
F3_STEP2_r4_status          = PARTIAL_PENDING_PI   (per v6 S13 and D-6 §5: narrowed_evidence
                              [T-R2-2] and the authored A.5(iii) uncovered row present — exactly
                              the status D-6 §5 declared expected; no other status is claimed)
F3_EXECUTION_READY = false ; F3_started = false ; real_data_access = false ; commit = false
```
