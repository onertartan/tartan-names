# p_konum_plus — F3 STEP-2 — CLASS_C Pin Register r4-1 (2026-09-29)

```text
artifact_role = CLASS_C implementation-pin register for the F3 adequacy-evaluation harness
                (deliverable 9 of the STEP-2 r4-1 correction revision inside the r4 cycle)
status        = NON-NORMATIVE
parent        = f3_step2_class_c_pin_register_r4_2026-09-27.md 0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4
frozen_contract = r4 5e594136 AS RATIFIED BY freeze record r1 7055f186 ; v11 wins (unchanged)
harness       = f3_step2_adequacy_harness_r4-1_2026-09-29.py
                4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f (attempt 3)
generator     = f3_step2_fixture_generator_r4-1_2026-09-29.py
                68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
PI-ratified content (D-2) = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
                da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
PI dispatch record (D-6)  = p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md
                a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0
                (child of D-5 0cd87ad5...; S-R2-1 = PI_RULE keeps citing D-5, carried unchanged by D-6 S2)
S/T as read   = S-1=(a) ; S-2=alpha ; T-1=AUTHORIZE ; T-2=T-2a ; T-3=AUTHORIZE ;
                T-4=T-4a ; T-5=CONFIRM_WITHIN_SCOPE ; S-R2-1=PI_RULE ; T-R2-2=AUTHORIZE_RESTART
scientific_freedom in every row = none ; new scientific literal additions by executor = 0
Every row is stated against the r4-1 run of 2026-09-30 (RUN1 == RUN2 canonical SHA256
556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77, attempt-log launch 4,
results 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385);
result = executor claim, independent verification pending.
Tag discipline (Y-10): a row tagged VERBATIM quotes its source as a BYTE-SUBSTRING of D-2 or
D-5 (machine-verified at authoring); every engineering description is tagged SUMMARY.
```

## Retained from r4 unchanged (re-verified against the r4-1 run; full rows in the parent register 0eed314c)

Every pin of the r4 register is implemented byte-for-byte as its parent-register row
describes and ran and passed in the r4-1 run, EXCEPT the three rows given in full below
(PIN-GUARDED-COMPARATOR, PIN-COVERAGE-DERIVED are AMENDED; PIN-SPLINE-PENDING-ROUTING and
PIN-NONREGRESSION-VS-R4 are NEW). Retained unchanged: PIN-S-R2-1-RULE (S-R2-1 = PI_RULE,
still the D-5 S3 verbatim text, tagged with the D-5 hash — D-6 carries it unchanged),
PIN-USET-PURE-FUNCTIONS, PIN-REVALIDATION-INCONSISTENT-U, PIN-EXC-CAPTURE,
PIN-A5-SUPPORT-CONTRACT, PIN-CANON-DOC, PIN-CALLCOUNT-PROVENANCE, PIN-RESTART-LAYER,
PIN-TESTONLY-EVALUATOR-BRANCHES, PIN-END-STATE-COMPUTED, and all r2-retained loader/masks/
statistics pins (PIN-F2-*, PIN-SPLINE-*, PIN-THREADS, PIN-MASKED-OBJECTIVE, PIN-MASKS,
PIN-FOLDS, PIN-ACF, PIN-STARTS, PIN-LOADER-NODE-HASHES 73/73, …). Each ran and passed in
the r4-1 run (T-EXPECT-ALL 36/36; captures RUN1==RUN2; T-CANON RUN1==RUN2; T-CALLCOUNT
run1 5256 == run2 5256).

## Amended or new in r4-1 (full rows)

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result (r4-1 run 2026-09-30) | tag / scientific_freedom |
|---|---|---|---|---|---|
| PIN-SPLINE-PENDING-ROUTING (NEW) | R4A-01 (A-2/A-3), adopted by D-6 §3; drafter choice (1): a pending spline context propagates exactly as the A.5 reference violation (a5v) already does | a spline-context UNRELATED-pending flag, recorded per (sex, fitter=SPL, context) as `spl_pending_full` / `spl_pending_fold` / `spl_pending_probe`, routes the dependent criteria to `STOP_EXACTNESS_PENDING(tag)` inside the decision grammar, mirroring a5v: **full → C3 and C4b**, **fold → C2**, **probe → C4b**; **C4a is NOT routed** (family-only ident — A-2 code-derived mapping); tag = `TEST_ONLY_INJECTED` for the injected fixtures (Y-04(b): not a finding) else `F3-STEP2-EXACT-04`; a routed criterion carries a PENDING status, never a passed/failed field; S-R2-1 = PI_RULE is preserved (C4b membership stays a construction condition — a spline-context pending is a numerical-availability event upstream of membership, not a PENDING C4b) | INJ-SPL-PENDING-FULL / -FOLD / -PROBE (manifest-declared expects) + the eval-level assertion in T-EXC-UNRELATED-TYPE + T-EXPECT-ALL | PASS: FULL → C3, C4b PENDING; FOLD → C2 PENDING; PROBE → C4b PENDING; C4a stays PASS in all three; p03 = (PENDING, PENDING); mechanism = MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED); eval_level_ok = True; RUN1==RUN2 (passes_identical) | SUMMARY / none |
| PIN-NONREGRESSION-VS-R4 (NEW) | R4A-01(f) (A-2/A-3), adopted by D-6 §3 | for every fixture present in BOTH the audited r4 results (a15b7eff) and this run, p03, every criterion outcome, the D-P04 block, the mechanism outcome and the fixture's stops are compared; BOTH sides are normalized through `canon()` + `sort_keys` before comparison (r4 stored canon()-ized/hex, this run's evals1 is in-memory/native-float — the raw compare is a representation artefact, R4A-10-adjacent, fixed at attempt 3); any surviving difference is a per-fixture finding and fails T-NONREG-R4; INJ-U-POST-CONSTRUCTION-INVALID (R4A-03 offending-pairs shape) is whitelisted EXPECTED_R4A03; the real-path spline-pending count is reported and must be 0 absent a natural UNRELATED event | T-NONREG-R4 + the delivered nonregression CSV | PASS: shared=34, new=3 (the INJ-SPL-PENDING fixtures), dropped=0, **findings=0**, real_path_spline_pending=0 | SUMMARY / none |
| PIN-GUARDED-COMPARATOR (AMENDED) | Y-03(iii)/R3A-04 + R4A-03 (A-2/A-3) | `_guarded_scalar_ok(v) = (v is not None and math.isfinite(v))` is the single guard the D-P04 comparator calls before `abs(delta) <= tau`; a refused scalar now yields **CONTRACT_VIOLATION_INCONSISTENT_U** (r4-1 relabel per R4A-03; was EMPTY_U) WITH its stops record; the crafted-S end-to-end path asserts the label | T-COMPARATOR-NAN (calls the real guard AND runs a crafted inconsistent-U scenario end-to-end; pass_ computed, no literal) | PASS: refuses NaN/None/inf, accepts finite; crafted-S run yields CONTRACT_VIOLATION_INCONSISTENT_U | SUMMARY / none |
| PIN-REVALIDATION-INCONSISTENT-U (AMENDED, R4A-03) | Y-03(ii)/R3A-04 + R4A-03 | as the parent row, plus: the offending-pairs list is **deduplicated on (sex, fitter, observation)** and each pair carries its **sex** (`dict(sex, fitter, observation)`); the fit_spline injection tag is `TEST_ONLY_INJECTED` (was TEST_ONLY_INJECTION) | INJ-U-POST-CONSTRUCTION-INVALID + T-CANON + T-NONREG-R4 (the whitelisted EXPECTED_R4A03 diff) | PASS: STOP_CONTRACT_VIOLATION_INCONSISTENT_U(level C2, member 0), offending_pairs = one deduped {sex:F, fitter:P01, observation:0}; RUN1==RUN2 | SUMMARY / none |
| PIN-COVERAGE-DERIVED (AMENDED, R4A-02) | Y-16/R3A-08 + R4A-02 (A-2/A-3); PI instruction 2026-09-24 (coverage closed only when its test ran and passed) | as the parent row, plus: the evidence-token grammar now ADMITS generic `T-*` and `NR-*` test ids (`elif tok in TESTS_RUN`), so rows evidenced by e.g. T-COMPARATOR-NAN, T-CALLCOUNT, T-NONREG-R4 resolve from their ran/passed record instead of being conservatively downgraded; three coverage rows added for the R4A-01 spline-pending fixtures | COVERAGE_DERIVED output + end_state | PASS: **64 rows derived; downgraded_to_UNCOVERED = []** (the r4 conservative downgrades are resolved); A.5(iii) remains authored-UNCOVERED (no construction without touching frozen code) | SUMMARY / none |

## VERBATIM quotes

The D-5 S3 rule text (PIN-S-R2-1-RULE), the D-2 S6 K-05 wording (PIN-COVERAGE-DERIVED) and
the freeze-record r1 double-count declaration are unchanged from the parent r4 register
(0eed314c) and are not re-transcribed here; S-R2-1 = PI_RULE is implemented byte-for-byte as
that register's PIN-S-R2-1-RULE row and its quoted D-5 text, carried unchanged by D-6 §2.

```text
new_scientific_literal_by_executor = 0
PI_RATIFIED content transcribed verbatim in the parent register: PIN-S-R2-1-RULE (D-5,
  0cd87ad5...); PIN-A5-SUPPORT and PIN-SOLVER-B-UNVERIFIABLE stand in the r2 register (D-2)
Every result above is bound to f3_step2_correction_report_r4-1_2026-09-29.md and
f3_step2_results_r4-1_2026-09-29.json (6dd4185b...); "see report" resolves there.
commit = false
```
