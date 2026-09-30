# p_konum_plus - F3 STEP-2 r4 - Correction Report

```text
artifact_role = correction report (deliverable 10, r4)
status        = NON-NORMATIVE narrative over the hashed artifacts it cites
date          = 2026-09-27 (cycle tag 2026-09-24; launches 2026-09-26 .. 2026-09-27)
```

No wording in this report asserts "verified", "QUALIFIED", or "audit PASS" about the
executor's own output. `F3_STEP2 = QUALIFIED` can be declared only by the PI after an
independent audit, which this report does not perform.

## 1. The PI's dispatch messages, verbatim (per the PI's own instruction)

Message of 2026-09-24 (the r4 dispatch; attachment tokens as received):

```text
Ekteki r4 talimatını ve dispatch kaydını hash'e karşı doğrulayıp uygula. S-R2-1 = PI_RULE metnini bu
gönderimle onaylıyorum. R3A-07 kapsamındaki attempt-log düzeltmelerini r4 attempt log'unda ve raporda, r3
dosyasının hash'ine atıfla erratum olarak yap; tarihsel r3 dosyasını değiştirme. Coverage kapanışlarını yalnız
ilgili test gerçekten çalışıp geçtiğinde kaydet. Yeni taslak döngüsü açmadan mevcut kapsam içindeki
düzeltmeleri ve doğrulamaları tamamla. Bu mesajı r4 raporunda verbatim aktar.@C:\Users\Neo\Downloads\f3step2\Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md @C:\Users\Neo\Downloads\f3step2\Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md.sha256 @C:\Users\Neo\Downloads\f3step2\Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md @C:\Users\Neo\Downloads\f3step2\Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md.sha256 @C:\Users\Neo\Downloads\f3step2\f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md @C:\Users\Neo\Downloads\f3step2\f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md.sha256 @C:\Users\Neo\Downloads\f3step2\f3_step2_r4_pi_dispatch_record_2026-09-24.md @C:\Users\Neo\Downloads\f3step2\f3_step2_r4_pi_dispatch_record_2026-09-24.md.sha256
```

Mid-cycle message of 2026-09-25 (model switch; quoted because it instructs this report's
process section):

```text
Model değişti. Şimdiye kadar yaptığın her değişikliği (dosya, satır) listele ve talimata karşı doğrula;
hatalı veya eksik olanı düzelt, sonra r4 talimatını kaldığın yerden sürdür. Raporun process bloğuna
kullanılan modelleri ve effort düzeyini, Sonnet 5 ile yapılan kısımlar dahil, yaz.
```

Both instructions were carried out: the mid-cycle verification found and fixed nine
defects/omissions in the then-current r4 work (S2 of this report and the register);
the erratum is in the r4 attempt log (r3 file untouched, referenced by hash); coverage
statuses are DERIVED from what ran and passed; no new draft cycle was opened; the models
note is in S9.

## 2. Custody (D-3 S3 / r4 instruction S1; every value OBSERVED)

Instruments, observed = pinned = EQUAL for all six (verified by the external W-3 writer
AND re-verified by every harness launch):

| instrument | path (p_konum_plus/prompts/) | sha256 |
|---|---|---|
| D-1 (v6) | Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md | 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 |
| D-2 (content) | f3_step2_pi_ratified_content_2026-09-07.md | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 |
| D-3 (r3 prompt, standing) | Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 |
| r4 instruction | Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md | e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 |
| D-5 (r4 dispatch record) | f3_step2_r4_pi_dispatch_record_2026-09-24.md | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 |
| A-1 (r3 audit; input, not directive) | f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md | 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6 |

P-4 evidence = D-5 (path and hash above). S/T as read: S-1=(a); S-2=alpha; T-1=AUTHORIZE;
T-2=T-2a; T-3=AUTHORIZE; T-4=T-4a; T-5=CONFIRM_WITHIN_SCOPE; **S-R2-1=PI_RULE** (rule
text D-5 S3, implemented word for word; the register's PIN-S-R2-1-RULE quotes it as a
machine-verified byte-substring); **T-R2-2=AUTHORIZE_RESTART**.

Deliverables of this cycle (hash line block; every file with an external .sha256 sidecar):

| # | file | sha256 |
|---|---|---|
| 1 | calibration/f3_step2_adequacy_harness_r4_2026-09-24.py (revision 5) | 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c |
| 2 | calibration/f3_step2_fixture_generator_r4_2026-09-24.py | 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c |
| 3 | calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv | c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 |
| 4 | provenance/f3_step2_r4_preexecution_custody_2026-09-24.md (revision 5; written externally) | 0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f |
| 5 | calibration/f3_step2_telemetry_r4_2026-09-24.csv (RUN1+RUN2 rows, L + failure codes) | 11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 |
| 6 | calibration/f3_step2_results_r4_2026-09-24.json | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 |
| 7 | calibration/f3_step2_residual_series_r4_2026-09-24.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 | calibration/f3_step2_test_evidence_r4_2026-09-24.json | 118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 |
| 9 | calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md (MANDATORY this cycle, R3A-01) | (sidecar) |
| 10 | provenance/f3_step2_correction_report_r4_2026-09-27.md (this file) | (sidecar) |
| 11 | r3 start-state stands (r4 opened from the audited r3 end state; no separate r4 inventory beyond the attempt log's revision blocks) | n/a -- disclosed |
| 12 | provenance/f3_step2_r4_attempt_log_2026-09-24.md (incl. the R3A-07 ERRATUM) | (sidecar) |
| A | calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv (12,174 rows, all phases, all pids) | d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 |
| B | calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv (11,869 rows; path, size, sha256, pid, start_iso) | f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 |
| C | capture records: results.solver_exceptions + test_evidence.exc_captures{,_unit_phase,_run2} + exc_captures_run1_eq_run2 = true | in 6/8 |
| D | transmission items of r4 instruction S2 -- see S8 |

The residual-series hash equals the r3 verified export byte-for-byte (same fits, same
injection-aware Y-21 exporter) -- continuity evidence, not reuse (recomputed from RUN1's
own fit objects this cycle; export-phase optimizer calls = 0, asserted).

## 3. Execution (D-3 S8; full detail in the attempt log)

8 launches, 5 revisions, 2026-09-26 13:04 .. 2026-09-27 18:06. Revision 1-2 ran with the
restart layer OFF (D-3 S8.1); the layer was introduced at revision 3 after the cycle's
first genuine interruption; on BOTH defect fixes (revisions 4 and 5) the store was
quarantined WHOLE and restarted empty per D-3 S8.3. Final launch (8; pid 29564):
exit 0; **DETERMINISM = True** (RUN1 == RUN2 canonical SHA256 =
`777fca02e1f514038e04cb3b5aac5365fa4dd851b03174820ef4692f8c73c2d8`); T-SINGLE-PROCESS =
NOT_RUN(units from 2 processes); T-RESTART-PROVENANCE 3/3 (attempt log).

Three defects were found and fixed INSIDE this cycle by this cycle's own new gates --
each is disclosure of the gates working, and each has a quarantine note with byte-exact
(or hash-proven reconstructed, disclosed) superseded bytes:
1. `any_mode_unrelated` never set on the fresh-compute path (caught by the new
   T-EXC-UNRELATED-TYPE on its FIRST execution -- the exact defect class the audit said
   the r3 test could not catch).
2. `k05_result` embedded the process-global counter (caught by T-CANON; RUN1 hash pair
   changed after the fix, proving it effective).
3. The Y-03(ii) post-construction mutation leaked into RUN2 via the generator's
   module-level fixture object (caught by T-CANON again; fixed by restore-after).

## 4. Response table -- D-3's Y items

| item | status | evidence |
|---|---|---|
| Y-01 | PASS | restart layer per S8.3 (attempt log; store manifests; per-(phase,pid) counts; T-RESTART-PROVENANCE 3/3); W-3 external per revision |
| Y-02 (a)(b)(c) | PASS | (a) membership-first U sets (register PIN-USET-PURE-FUNCTIONS); (b) pure functions called by run_dp04 AND UT-USET (R3A-10); (c) T-EXPECT-ALL 33/33, EXPECTATION_FAIL=[] |
| Y-03 (i)(ii)(iii)(iv) | PASS | (i) flag-membership + undefined (INJ-NAN-STAT-*); (ii) data-driven re-validation w/ (fitter, observation) pairs + restore (INJ-U-POST...); (iii) _guarded_scalar_ok called by comparator AND T-COMPARATOR-NAN; (iv) constructions per S7 |
| Y-04 (a)(b)(c)(d) | PASS | traceback classifier; UNRELATED -> capture + context STOP_EXACTNESS_PENDING(tag), every class caught at mode level; S1/S2 arming (stages [1],[1,2]); wrappers scope-restored, no stacking; all captures delivered, RUN1==RUN2 compared |
| Y-05 | PASS | T-A5-SUPPORT 10/10; violation -> a5v -> C4a AND C4b STOP_EXACTNESS_PENDING(CONTRACT_VIOLATION_A5_REFERENCE); FIX-A5-TRUE |
| Y-06 | PASS | fidelity 5/5 declared injection sites, execution-site keys |
| Y-07 | PASS | X-11 (a)-(f): per-call rows all phases; family rows with L + predicates; S6 fields (DISC-F3-03, invalid counts, probe-failure shares, K-05 RESULT, double-count echo VERBATIM); enlarged canonical doc; `sexes` removed; T-SCHEMA machine assert; FIX-STARTS rows written; RUN2 rows kept |
| Y-08 | PASS | end-state fields computed from TESTS_RUN (27/27) + expectation results; no literal |
| Y-09 | PASS | S2 above names D-5 as P-4's evidence |
| Y-10 | PASS | register tag discipline; VERBATIM blocks machine-verified byte-substrings of D-2/D-5 |
| Y-11 | PASS | K-05 row wording = content S6 VERBATIM (register + coverage row) |
| Y-12 | PASS | opened-file list unfiltered in results (17,932 audit-derived); classification: 17,652 restart-store, 259 interpreter/site-packages, 19 project, 2 other; 16 declared |
| Y-13 | PASS | 73/73 unique node hashes; register row present |
| Y-14 | PASS | X-12 items carried in the register |
| Y-15 | PASS | T-MASK-FULL-EXT ran and passed |
| Y-16 | PASS | coverage statuses DERIVED from the run (S6); one vocabulary; downgrades loud |
| Y-17 | PASS | every STOP return writes a stops record (incl. the guarded-comparator branch, R3A-09) |
| Y-18 | PASS | this report: custody table, per-finding table, coverage matrix, opened-file classes, hash block, response table, attempt histories, parents re-hash |
| Y-19 | PASS | attempt history disclosures (S7); register rows |
| Y-20 | not applied (optional) | -- |
| Y-21 | PASS | residual series from RUN1's own fit objects; T-RESIDUAL-LINK keys equal; export calls 0 |

## 5. Response table -- the r3 audit's R3A items (as adopted by r4 instruction S3)

| item | status | evidence |
|---|---|---|
| R3A-01 | CLOSED | register r4 authored (deliverable 9), child of the r2 register f263eace...; PI_RULE row PI_RATIFIED w/ D-5 hash; restart-layer + TEST_ONLY-branch rows present |
| R3A-02 | CLOSED | Y-07 row above |
| R3A-03 | CLOSED | Y-04 row above + INJ-EXC-* two passes asserted identical (manifest run_scope honored) |
| R3A-04 | CLOSED | Y-03 (ii)(iii) row above |
| R3A-05 | CLOSED | Y-05 row above |
| R3A-06 | CLOSED | coarse units carry+replay per-call snapshots; per-(phase,pid) counts (nr_gates 60, unit_tests 1602, run1 5256 == run2 5256); store manifest w/ pid+start_iso |
| R3A-07 | CLOSED | ERRATUM in the r4 attempt log (r3 file untouched, hash-referenced per the PI's instruction); three W-3 hashes per revision; foreign prefix 548ae790 (11,723 entries) quarantined + listed (T-R3-2); W-3 written once per revision OUTSIDE the process with observed values; docstring rewritten |
| R3A-08 | CLOSED | coverage derived (S6); C4b-real row split pass/fail w/ SCEN-B evidence per D-5 S4(d); K-05 wording VERBATIM |
| R3A-09 | CLOSED | guarded branch writes its stops record |
| R3A-10 | CLOSED | pure uset_* functions; UT calls the product path (SPL + cc honored) |
| R3A-11 | CLOSED | corrections_complete + mandatory_tests_all_run computed from TESTS_RUN |
| R3A-12 | CLOSED | this report |
| R3A-13 | ADDRESSED | transmission set in S8 (sidecars, five r3 quarantine notes, superseded revisions) |
| R3A-14 | ACKNOWLEDGED | r2 attempt history NOT RECONSTRUCTIBLE from files (r2 checkpoint dir deleted at r2 end, disclosed in the r3 start-state inventory); nothing further possible |
| R3A-15 | CLOSED by the audit itself | P-7(c) withdrawn; transmittal note stands as non-normative |
| R3A-16 | NOT APPLIED (optional) | SCEN-A deliberately carries no structural expectation (circularity; generator comment); unit-test rows are asserted in-harness |
| R3A-17 | noted | informational |

## 6. Coverage matrix (derived; 61 rows)

56 covered / covered_injection_only; 5 UNCOVERED:
- `A.5 (iii) inadmissible refit` -- authored UNCOVERED (unchanged; D-5 S7 anticipated it).
- `C2 pass`, `C3 pass` -- CONSERVATIVE DOWNGRADES: their authored evidence text ("INJ
  baselines") names no machine-checkable fixture/test id, and per the PI's instruction a
  closure is recorded ONLY on demonstrated pass. The underlying evidence exists in the
  delivered results (every INJ baseline fixture passed its expectation check) -- the
  auditor can weigh it; the executor does not silently claim it.
- `D-P04 comparator never RESOLVED/EQUIVALENT on NaN` -- same: resolver token gap
  (T-COMPARATOR-NAN is not in the token grammar); TESTS_RUN["T-COMPARATOR-NAN"].passed
  = true is in the results.
- `clean execution / process provenance disclosed` -- evidence is the attempt log +
  process block themselves, not a fixture/test id; disclosed here.
The 4 downgrades err toward UNCOVERED by design; none hides a failed test (27/27
mandatory tests passed).

## 7. Attempt histories and parents

- r4: 8 launches / 5 revisions -- the attempt log (deliverable 12).
- r3: 10 launches / 5 revisions -- the r3 attempt log
  `253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5`, CORRECTED BY
  ERRATUM in the r4 attempt log (rows 9-10 ran `5fea165c...`, not `99f895c1...`); the
  r3 file itself untouched per the PI's instruction.
- r2: attempt history NOT RECONSTRUCTIBLE from files (R3A-14; disclosed in the r3
  start-state inventory `71a3f5a7...`).
- parents_unchanged = true: 40/40 non-quarantine sidecars verify OK on 2026-09-27
  (r1/r2/r3 deliverables included). One STRAY, MALFORMED 46-byte sidecar (no hash field,
  filename only) was found at the p_konum_plus ROOT for the r3 report -- the real
  provenance/ pair verifies OK with the audit-received hash `80df7914...`; the stray file
  (an r3-era generation artifact written to the wrong directory) was moved to
  `quarantine/STRAY_MALFORMED_root_f3_step2_correction_report_r3_2026-09-24.md.sha256`,
  not deleted.

## 8. Transmission set (r4 instruction S2 + R3A-13)

(a) sidecars of the r3 deliverables 1-12: in the repository, all verifying (S7).
(b) the five r3 quarantine notes named by the r3 report: attempt-1 supersession note,
    exc-classification-bug note, independent-audit-corrections note (P-1..P-7),
    attempt-8 telemetry-replay note, transmittal-note corruption incident note -- all in
    p_konum_plus/quarantine/ with unchanged names.
(c) superseded r3 harness revisions and custody records: present in quarantine/
    (6ddcc26d..., 891574fc..., d67e097d..., f882b922..., 99f895c1... and their custody
    files). Superseded r4 revisions likewise (f137299c... [hash-proven reconstruction,
    caveat disclosed in its note], 20d830e0..., 814e395a..., 90ea0ff3...).
(d) r3 final store: quarantined whole (23,446 units) as
    `quarantine/r3_restart_store_2026-09-22_FINAL_T-R3-2/`; the 11,723 foreign-prefix
    (548ae790...) entries individually listed in
    `quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv` (T-R3-2).

## 9. Process block (incl. the models note the PI instructed)

```text
launches                = 8 (pids 30160, 29296, 27308, 24680, 25924, 35860, 31388, 29564)
revisions               = 5 ; W-3 written once per revision, externally, observed values
final process           = pid 29564, 2026-09-27T17:44:22 .. 18:06:15, exit 0
units (final process)   = computed: run1 1, run2 2, residual_export 1 ;
                          read from store: nr_gates 1, unit_tests 1, run1 1
per-call optimizer rows = 12,174 (nr_gates 60 ; unit_tests 1602 ; run1 5256 ; run2 5256 ;
                          export 0) ; by pid: 31388 -> 5618, 29564 -> 6556
executor_models         = the r2 and r3 cycles and the r4 cycle up to and including the
                          comparator-guard edit of 2026-09-25 ran under claude-sonnet-5[1m]
                          (Sonnet 5); from the T-COMPARATOR-NAN completion onward
                          (2026-09-25 /model switch, mid-R3A-04) under claude-fable-5[1m]
                          (Fable 5). Reasoning-effort: no explicit effort override was
                          configured in either configuration (harness default); the
                          executor cannot observe an internal effort parameter and
                          reports only what the session exposed.
real_data_access        = false ; commit = false (throughout)
```

## 10. End state (v6 S13/S14, D-3 S10; every field computed)

```text
PI_dispatch_record_hash     = 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 (observed)
S-R2-1 = PI_RULE (verbatim, as read) ; T-R2-2 = AUTHORIZE_RESTART (verbatim, as read)
corrections_complete        = true   (27/27 mandatory tests ran AND passed; EXPECTATION_FAIL = [])
mandatory_tests_all_run     = true   (mandatory_tests_missing = [])
expectation_checks          = 33 / 33 ; EXPECTATION_FAIL = none
deferred_decisions          = []     (EXACT-03 CLOSED with D-5 as source, D-5 S4(d))
narrowed_evidence           = [T-R2-2]
uncovered_coverage_rows     = ["C2 pass", "C3 pass", "A.5 (iii) inadmissible refit",
                               "D-P04 comparator never RESOLVED/EQUIVALENT on NaN",
                               "clean execution / process provenance disclosed"]  (S6)
open_findings               = []     (no natural UNRELATED event; EXACT-04 not opened)
parents_unchanged           = true   (40/40 sidecars re-verified; stray-file disclosure S7)
determinism                 = true   (RUN1 == RUN2 = 777fca02... over the ENLARGED document)
F3_STEP2_r4_status          = PARTIAL_PENDING_PI   (per v6 S13: narrowed_evidence and
                              uncovered rows present -- exactly the end status D-5 S7
                              declared expected; no other status is claimed)
F3_EXECUTION_READY = false ; F3_started = false ; real_data_access = false ; commit = false
```
