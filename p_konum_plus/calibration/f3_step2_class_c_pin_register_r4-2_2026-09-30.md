# p_konum_plus — F3 STEP-2 — CLASS_C Pin Register r4-2 (2026-09-30)

```text
artifact_role = CLASS_C implementation-pin register for the F3 adequacy-evaluation harness
                (deliverable 9 of the STEP-2 r4-2 correction revision inside the r4 cycle)
status        = NON-NORMATIVE
parent        = f3_step2_class_c_pin_register_r4-1_2026-09-29.md 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671
frozen_contract = r4 5e594136 AS RATIFIED BY freeze record r1 7055f186 ; v11 wins (unchanged)
harness       = f3_step2_adequacy_harness_r4-2_2026-09-30.py
                b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 (attempt 2)
generator     = f3_step2_fixture_generator_r4-1_2026-09-29.py — REUSED UNCHANGED
                68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
manifest      = f3_step2_fixture_manifest_r4-1_2026-09-29.csv — REUSED UNCHANGED
                5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
                (regenerated in memory and verified equal by the W-3 writer AND by main())
PI-ratified content (D-2) = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
PI dispatch record (D-7)  = f3_step2_r4-2_pi_dispatch_record_2026-09-30.md
                a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb
                (child of D-6 a92a0518…; S-R2-1 = PI_RULE keeps citing D-5 0cd87ad5…,
                carried unchanged by D-6 and D-7)
S/T as read   = S-1=(a) ; S-2=alpha ; T-1=AUTHORIZE ; T-2=T-2a ; T-3=AUTHORIZE ;
                T-4=T-4a ; T-5=CONFIRM_WITHIN_SCOPE ; S-R2-1=PI_RULE ; T-R2-2=AUTHORIZE_RESTART
scientific_freedom in every row = none ; new scientific literal additions by executor = 0
Every row is stated against the r4-2 run of 2026-09-30 (RUN1 == RUN2 canonical SHA256
556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 — equal to r4-1's, as
T-NONREG-R4-1 requires; attempt-log launch 2, results
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba);
result = executor claim, independent verification pending.
Tag discipline (Y-10): VERBATIM rows quote byte-substrings of D-2/D-5 (in the r4 register,
machine-verified); every engineering description is tagged SUMMARY.
```

## Retained from r4-1 unchanged (re-verified against the r4-2 run; full rows in the parent register 45a10494)

Every pin of the r4-1 register ran and passed in the r4-2 run and is implemented as its
parent row describes, EXCEPT the rows given in full below. Retained unchanged:
PIN-S-R2-1-RULE (the D-5 §3 verbatim text; D-6 and D-7 carry it unchanged),
PIN-USET-PURE-FUNCTIONS, PIN-EXC-CAPTURE, PIN-A5-SUPPORT-CONTRACT, PIN-CANON-DOC,
PIN-CALLCOUNT-PROVENANCE, PIN-TESTONLY-EVALUATOR-BRANCHES, PIN-COVERAGE-DERIVED,
PIN-NONREGRESSION-VS-R4, PIN-GUARDED-COMPARATOR, and all r2-retained loader/masks/statistics
pins. Evidence: T-EXPECT-ALL 36/36; 30/30 recorded tests passed; captures RUN1==RUN2;
T-CANON RUN1==RUN2=556106e7…; T-CALLCOUNT run1 5256 == run2 5256; T-NONREG-R4 findings=0.

## Amended or new in r4-2 (full rows)

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result (r4-2 run 2026-09-30) | tag / scientific_freedom |
|---|---|---|---|---|---|
| PIN-SPLINE-PENDING-ROUTING (AMENDED, R41A-01(a)(b)) | A-4 R41A-01, adopted by D-7 §3; D-3 Y-04(b) | the three real-path flag sites call `spl_pending_tag(failure)`: ANY `STOP_EXACTNESS_PENDING(<tag>)` sets the context's flag and the flag CARRIES `<tag>` (the tag fit_spline itself derived from the captured event: natural → F3-STEP2-EXACT-04, injected → TEST_ONLY_INJECTED); the r4-1 `"TEST_ONLY" not in failure` clause is DROPPED; the c4_source-derived routing tag is REMOVED — each routed criterion calls `merge_pending_tags` over the flag lists of the contexts THAT CRITERION reads (full → C3, C4b; fold → C2; probe → C4b; C4a not routed); a decision-layer fixture's boolean True folds to TEST_ONLY_INJECTED; the declared spline-failure injection returns `TEST_ONLY_INJECTION_SPLINE_FAILURE` (no STOP prefix), sets no flag, and stays an ordinary failure — D-5's SCEN-B pin unchanged | T-SPL-PENDING-REALPATH (all 9 cases) + T-EXPECT-ALL over INJ-SPL-PENDING-* + T-NONREG-R4-1 | PASS: natural full/fold/probe → dependent criteria STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04), both families; same three injected → (TEST_ONLY_INJECTED), no definite outcome; declared failure → ordinary failure, no pending cell; SCEN-B unchanged (T-NONREG-R4-1 0 findings) | SUMMARY / none |
| **PIN-SPLINE-PENDING-TAG-SCOPE (NEW — the R41A-01(b) reading, stated for the auditor)** | r4-2 instruction §3 R41A-01(b); **the reading below was put to the PI and ACCEPTED by the PI's dispatch message of 2026-09-30 ("R41A-01 (b) için kriter bazındaki okuman kabul")** | the mixed-tag rule is resolved **PER CRITERION**, not per sex: a routed criterion carries the tag folded from the contexts IT reads, and "if a sex has both kinds for the criteria it routes, F3-STEP2-EXACT-04 is used" applies where both kinds actually reach the SAME criterion (`merge_pending_tags`: natural wins inside one criterion's contexts). Concretely — injected event in `full` + natural event in `probeL`, same sex: **C3 (reads full only) → TEST_ONLY_INJECTED; C4b (reads full + probe) → F3-STEP2-EXACT-04**. The natural event is never masked: it surfaces in C4b and in the mechanism outcome (whose folded tag also prefers the natural id). The REJECTED alternative — escalating every routed criterion of the sex — would attribute a natural exactness finding to a criterion (C3) no natural event touched | T-SPL-PENDING-REALPATH case "natural and injected, same sex" (expectation written before the run) | PASS: C3:F = STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED), C4b:F = STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04), mechanism = MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | SUMMARY / none — an interpretation choice, disclosed and PI-accepted, not a scientific value |
| PIN-SPL-PENDING-REALPATH-STUBS (NEW, R41A-01(c) disclosure) | D-3 Y-04(d); A-4 §5.2 technique | T-SPL-PENDING-REALPATH calls the REAL `run_real_scenario` and `evaluate_fixture` on a real REAL_SCENARIOS trajectory with ONLY `fit_family`/`fit_spline` replaced by TEST_ONLY stubs (family: always-eligible; spline: valid except in the contexts a case names, where it returns the exact failure strings the real fit_spline returns); stub numbers are meaningless and enter no deliverable; stubs installed for this test only, restored by direct reassignment WITH the restoration asserted; every touched global (FIDELITY lists, telemetry, EXC_CAPTURES, SPL_CTX_DONE, CURRENT_PHASE) snapshotted and restored, equality asserted; every case's expectation written in the test BEFORE the run; a routed cell carrying a `passed` field fails the test (the machine form of "no definite outcome") | T-SPL-PENDING-REALPATH (MANDATORY) | PASS: 9/9 cases; restored = all true; pending_cells_with_a_verdict = none, in-run | SUMMARY / none |
| PIN-NONREGRESSION-VS-R4-1 (NEW, R41A-01(d)) | r4-2 instruction §3 R41A-01(d) | every one of the 37 evaluation objects and every stop record compared against the audited r4-1 results (6dd4185b…, hash re-verified before reading) in canon() form with sorted keys; **NO whitelist**; stops compared as an order-independent document; the RUN1 canonical document and the residual series checked as the NAMED values 556106e7… and 3ee624f3…, not as "whatever came out"; any difference reported per fixture, never absorbed; T-NONREG-R4 (vs r4) retained unchanged beside it | T-NONREG-R4-1 (MANDATORY) + the delivered CSV (item D) | PASS: compared=37, findings=0, stops_equal=True, run1_canonical observed == expected (556106e7…), residual observed == expected (3ee624f3…) | SUMMARY / none |
| PIN-CUSTODY-PER-ATTEMPT (NEW, R41A-02) | A-4 R41A-02, adopted by D-7 §3 | (a) CUSTODY_PATH carries ATTEMPT_NUMBER (`..._custody_attempt<k>_...md`); the external W-3 writer REFUSES an existing path; from attempt 2 on SUPERSEDES_CUSTODY_SHA256 (harness) and supersedes_custody_sha256 (record) carry the superseded record's hash — filled this revision: ae0f0768…; (b) before ANY superseding edit the harness bytes are copied to quarantine and the copy's hash must equal the custody-named hash (applied at the attempt-1→2 transition: copy == 9e4d2803…, preserved bytes, no reconstruction); (c) every launch writes its own launch-numbered log pair, never overwritten; the launch number comes from the environment (F3_R42_LAUNCH) so a resumed launch cannot change the harness bytes/fingerprint — main() refuses to run without it | custody records attempt1 (ae0f0768…) + attempt2 (766ad7b6…) on disk together; the quarantined attempt-1 bytes; launch1/launch2 log pairs on disk together; PRE_EXECUTION_CUSTODY_RECORD_VERIFIED at both launches | PASS: both records preserved; copy-before-edit hash-equal; both log pairs intact; single process (pid 10412) computed all 11,869 units | SUMMARY / none |
| PIN-END-STATE-DISPATCH (AMENDED, R41A-03) | r4-2 instruction §3 R41A-03 | `end_state.PI_dispatch_record_hash` = the hash of D-7 **as observed on disk during the run** (re-read at end-state assembly, asserted equal to the pin AND asserted equal to what is written); the S-R2-1 source (D-5, 0cd87ad5…) stands in its own fields `S_R2_1_source_dispatch_record_hash/path`, never in PI_dispatch_record_hash; a third assertion requires the two records to be distinct | the three R41A-03 assertions in main() + the delivered end_state | PASS: PI_dispatch_record_hash = a3e70509… (D-7 observed); S-R2-1 source field = 0cd87ad5… (D-5); run reached exit 0 through all three assertions | SUMMARY / none |
| PIN-REVALIDATION-INCONSISTENT-U (description CORRECTED, R41A-06 — code unchanged) | Y-03(ii)/R3A-04 + R4A-03; A-4 R41A-06 | the code is byte-identical to r4-1's on this path and is NOT changed this revision. The parent register's DESCRIPTION of the delivered INJ-U-POST-CONSTRUCTION-INVALID stop record was wrong ("one deduped pair {sex:F,...}"); the record as delivered — and as reproduced by the auditor [A-S] — lists **two offending pairs, (F, P01, 0) and (M, P01, 0)**: the builder lists every offending pair of the level across BOTH sexes, deduplicated on (sex, fitter, observation), and **the record-level `sex` field is the sex of the FIRST hit (F)**, kept as stop detail | INJ-U-POST-CONSTRUCTION-INVALID + T-NONREG-R4-1 (the record is byte-identical to r4-1's) | PASS: two pairs as described; record sex = F; 0 non-regression findings | SUMMARY / none |

## VERBATIM quotes

The D-5 §3 rule text (PIN-S-R2-1-RULE), the D-2 S6 K-05 wording and the freeze-record r1
double-count declaration stand in the r4 register (0eed314c) unchanged and are not
re-transcribed; S-R2-1 = PI_RULE is implemented byte-for-byte as that register's quoted
text, carried unchanged by D-6 §2 and D-7 §2.

```text
new_scientific_literal_by_executor = 0
Every result above is bound to f3_step2_correction_report_r4-2_2026-09-30.md and
f3_step2_results_r4-2_2026-09-30.json (f2a0a4d5...); "see report" resolves there.
commit = false (at authoring time; the PI has since directed the p_konum_plus branch to be
committed and pushed to the project repository -- recorded in the report's process section)
```
