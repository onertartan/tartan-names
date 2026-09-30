# p_konum_plus - F3 STEP-2 - CLASS_C Pin Register r4 (2026-09-27)

```text
artifact_role = CLASS_C implementation-pin register for the F3 adequacy-evaluation
                harness (deliverable 9 of the STEP-2 r4 correction cycle; the r3 cycle
                authored none -- audit finding R3A-01 -- so this register also carries
                the r3-introduced pins, re-verified under r4)
status        = NON-NORMATIVE
parent        = f3_step2_class_c_pin_register_r2_2026-09-07.md f263eaceffb94a458f331fb80258e779f0a740634d2420e696406b191a7142d5
frozen_contract = r4 5e594136 AS RATIFIED BY freeze record r1 7055f186 ; v11 wins
harness       = f3_step2_adequacy_harness_r4_2026-09-24.py
                54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c (revision 5)
PI-ratified content (D-2) = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
                da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
PI dispatch record (D-5)  = p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md
                0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
S/T as read   = S-1=(a) ; S-2=alpha ; T-1=AUTHORIZE ; T-2=T-2a ; T-3=AUTHORIZE ;
                T-4=T-4a ; T-5=CONFIRM_WITHIN_SCOPE ; S-R2-1=PI_RULE ; T-R2-2=AUTHORIZE_RESTART
scientific_freedom in every row = none ; new scientific literal additions by executor = 0
Every row is stated against the r4 run of 2026-09-27 (RUN1 == RUN2 canonical SHA256
777fca02e1f514038e04cb3b5aac5365fa4dd851b03174820ef4692f8c73c2d8, attempt-log launch 8,
results a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374);
result = executor claim, independent verification pending.
Tag discipline (Y-10): a row tagged VERBATIM quotes its source as a BYTE-SUBSTRING of
D-2 or D-5 (machine-verified at authoring; the check script is quoted in the r4
report); every engineering description is tagged SUMMARY.
```

## Retained from r2 unchanged (re-verified against the r4 run; full rows in the parent register)

The following pins are implemented byte-for-byte as their parent-register rows describe
(the r2 register is in the repository under the parent hash above); each ran and passed
in the r4 run: PIN-F2-LOADER, PIN-F2-IMPORT-HASH, PIN-SPLINE-LOADER,
PIN-SPLINE-IMPORT-HASH, PIN-THREADS, PIN-MASKED-OBJECTIVE, PIN-MASKS, PIN-FOLDS,
PIN-FEATURE-START-MASKED, PIN-SPLINE-MASKED-RSS, PIN-ACF, PIN-RHOCV, PIN-RMSE-EDGE,
PIN-SSTAB-W, PIN-MEDIAN, PIN-IQR, PIN-TAU-COMPARE (now guarded -- see
PIN-GUARDED-COMPARATOR below), PIN-WORSE-SEX, PIN-CONSULTED-PATH, PIN-TERMINAL-FALLBACK,
PIN-P03-STATUS, PIN-STARTS, PIN-PROBE-SUCCESS, PIN-LOADER-NODE-HASHES (73/73 unique --
Y-13), PIN-TELEMETRY (extended -- see PIN-CALLCOUNT-PROVENANCE below).
X-12 wording items (Y-14) carried: the spline zero-variance predicate is exactly
`q.std(ddof=0) == 0.0` (exact zero, no epsilon); the TEST_CONSTANT tables remain split
(fixture-construction inputs vs verification-only); the PIN-ACF row's clause (a) scope
statement is unchanged from r2.

## Changed or new in r3/r4 (full rows)

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result (r4 run 2026-09-27) | tag / scientific_freedom |
|---|---|---|---|---|---|
| PIN-S-R2-1-RULE | **PI_RATIFIED, VERBATIM** -- D-5 S3 rule text, quoted in full below this table; tagged with the D-5 hash 0cd87ad5... | V4_s(F) membership = the recorded flags pL AND pR AND full of the named fitter AND of the spline, per sex (evaluate_fixture C4b; crit_stats probes_idx); U4_s = uset_c4b = V4(P01) intersect V4(P02); membership NEVER read from RMSE_edge presence (rule item 4); n_s retained; empty V4 -> statistic undefined -> C4b not passed (S8.1); the DEFERRED-era STOP_EXACTNESS_PENDING pre-check is REMOVED (rule item 2: membership condition, never PENDING); EXACT-03 closed with D-5 as source | T-EXPECT-ALL over the four D-5-pinned fixtures + UT-PROBE-DECOUPLE second half + UT-USET case (d) | PASS: SCEN-B FAIL/FAIL + C4b undefined in M (V4 empty); INJ-C1-FAIL (FAIL,PASS) C1-first; INJ-DP04-C1 RESOLVED_MECHANISM_P01 at C1, subset recompute counts all 0; INJ-C4B-NOREF TERMINAL_FALLBACK, U2=U5=10, U3=U4=8 per sex | none -- transcribed word for word, PI_RATIFIED |
| PIN-USET-PURE-FUNCTIONS | Y-02(b)/R3A-10 | uset_c2/uset_c3/uset_c4b/uset_c5 are the ONLY implementation of the consulted-set membership rules; run_dp04 calls them; UT-USET-CONSTRUCTION calls the SAME functions on crit_stats built by the real crit_stats() from constructed strata (SPL fitter included; cc honored) | UT-USET-CONSTRUCTION (a)-(e) | PASS 5/5; case (d) proves the PI_RULE architecture: flags-only U4 INCLUDES the NaN-edge member and the run_dp04 re-validation predicate flags it | SUMMARY / none |
| PIN-REVALIDATION-INCONSISTENT-U | Y-03(ii)/R3A-04 | run_dp04 re-reads every U member's statistic from the CURRENT data for every fitter the criterion names (C2 rho, C3 phi, C4b combined edge, C5 sst -- no spline term in C5); any non-finite member -> CONTRACT_VIOLATION_INCONSISTENT_U with the offending (fitter, observation) pairs recorded, first hit kept as stop detail; the TEST_ONLY hook mutates the data BEFORE run_dp04 and RESTORES it after (revision 5: the mutation must never leak into the other run's evaluation) | INJ-U-POST-CONSTRUCTION-INVALID + T-CANON | PASS: STOP_CONTRACT_VIOLATION_INCONSISTENT_U(level C2, member 0) with offending pairs; T-CANON PASS proves no cross-run leak | SUMMARY / none |
| PIN-GUARDED-COMPARATOR | Y-03(iii)/R3A-04 | _guarded_scalar_ok(v) = (v is not None and math.isfinite(v)) is the single guard the D-P04 comparator calls before abs(delta) <= tau; a refused scalar -> CONTRACT_VIOLATION_EMPTY_U WITH its stops record (R3A-09) | T-COMPARATOR-NAN (calls the real guard; pass_ computed from its behavior, no literal) | PASS: refuses NaN/None/inf, accepts finite | SUMMARY / none |
| PIN-EXC-CAPTURE | S-2=alpha (content S3, D-2 -- parent rows PIN-SOLVER-B-UNVERIFIABLE retained); Y-04/R3A-03 engineering | covered-vs-unrelated from the exception's OWN traceback (accept immediately followed by kkt_res in extract_tb order); fit_spline catches EVERY class at mode level for classification only; ANY unrelated capture -> whole context STOP_EXACTNESS_PENDING(tag) where tag = TEST_ONLY_INJECTION (injected; not a finding, Y-04(b)) else F3-STEP2-EXACT-04; every capture record phase/pid/start_iso-tagged and DELIVERED (unit phase + RUN1 + RUN2); RUN1/RUN2 capture records compared and asserted equal; wrappers installed one layer at a time and restored by direct reassignment (never re-install -- the r3 stacking defect); INJ-EXC-* run as the manifest declares: two full deterministic passes, results asserted identical | T-EXC-CAPTURE-S1/S2, T-EXC-UNRELATED-TYPE, UT-EXC-UNRELATED-REFERENCE, EXC_CAPTURES_RUN1_EQ_RUN2 | PASS: S1 [1]; S2 [1,2]; UNRELATED-TYPE caught-not-crashed, ValueError recorded, context unverifiable; 1a/1b propagate; passes identical; RUN1==RUN2 captures (1 natural COVERED each) | SUMMARY / none |
| PIN-A5-SUPPORT-CONTRACT | content S2.3 (D-2 -- parent row PIN-A5-SUPPORT retained); Y-05/R3A-05 | an A5ContractViolation NEVER becomes a C4 pass or fail: the per-trajectory a5v flag routes C4a AND C4b of that sex to STOP_EXACTNESS_PENDING(CONTRACT_VIOLATION_A5_REFERENCE); the predicate itself is unit-tested | T-A5-SUPPORT (10 sub-cases: threshold equality included; next float below excluded; disconnected components united; edge-mask condition both ways; constant reference -> S = G; NaN/wrong-length/inf -> violations) + FIX-A5-TRUE | PASS 10/10; FIX-A5-TRUE pass both sides | SUMMARY / none |
| PIN-CANON-DOC | X-11(d)/R3A-02 | canonical RUN1/RUN2 document = evals + stops + pins; per family fit: theta (hex), masked L (hex), start-bank size, FEATURE_START_REJECTED, failure codes; per spline fit: winner mode, RSS (hex), equivalent-mode set, per-mode validity; ACF/A5/unit-test objects EXCLUDED (separate test-evidence document); `sexes` REMOVED; k05_result embeds the PER-FIXTURE check delta (revision 4: never the process-global counter); T-SCHEMA machine-asserts every enlarged field present | T-CANON + T-SCHEMA | PASS: RUN1 == RUN2 = 777fca02... ; T-SCHEMA missing=[] | SUMMARY / none |
| PIN-CALLCOUNT-PROVENANCE | Y-01/R3A-06; D-3 S8.3 | every per-call optimizer row and every capture record carries phase (nr_gates/unit_tests/run1/run2/residual_export) + pid + start_iso; coarse store units (nrgates_all, unittests_all) carry and replay their per-call snapshots; totals reported per phase AND per (phase, pid); store manifest carries pid/start_iso per unit; RUN1 total == RUN2 total; residual-export phase makes 0 optimizer calls | T-CALLCOUNT + T-RESIDUAL-LINK(3) + store manifest | PASS: nr_gates 60, unit_tests 1602, run1 5256 == run2 5256, export 0; phase/pid split = exactly the two revision-5 pids; manifest 11,869 rows | SUMMARY / none |
| PIN-RESTART-LAYER | D-3 S8.2/S8.3; T-R2-2=AUTHORIZE_RESTART (D-5) | attempt 1 of the cycle: ONE process, layer OFF; layer introduced only after the first genuine interruption; store keys prefixed by the code+input+environment fingerprint; store quarantined WHOLE on every harness change; W-3 written once per revision OUTSIDE the run process with observed values, harness VERIFIES it and never writes it (R3A-07) | T-RESTART-PROVENANCE (3 conditions, attempt log) ; custody VERIFY at every launch | PASS: conditions 1-3 in the r4 attempt log; custody verified at all 8 launches | SUMMARY / none |
| PIN-TESTONLY-EVALUATOR-BRANCHES | Y-04(b) disclosure; R3A-01 | the evaluator's TEST_ONLY branches are exactly: force_c4_pending (INJ-P03-*-C4PENDING fixtures; C4a/C4b -> STOP_EXACTNESS_PENDING(TEST_ONLY_FORCED_C4_PENDING)) and the post-construction corruption hook (inject_post_construction_invalid_<crit> flag; mutate -> run_dp04 re-validation -> RESTORE); inject_empty_U2 (INJ-DP04-EMPTY-U); TEST_ONLY events are never findings | fixture outcomes above; T-CANON (restore) | PASS | SUMMARY / none |
| PIN-COVERAGE-DERIVED | Y-16/R3A-08; PI instruction of 2026-09-24 ("Coverage kapanislarini yalniz ilgili test gercekten calisip gectiginde kaydet") | the status column of every coverage row is recomputed from THIS run's fixture evaluations, expectation results and the TESTS_RUN registry; an authored "covered" that cannot be established is downgraded to UNCOVERED(...) loudly and enters end_state.uncovered_coverage_rows; K-05 row wording = content S6 VERBATIM (quoted below) | COVERAGE_DERIVED output + end_state | PASS: 61 rows derived; 4 conservative downgrades disclosed (see the r4 report S6) + A.5(iii) authored-UNCOVERED | SUMMARY / none |
| PIN-END-STATE-COMPUTED | Y-08/R3A-11 | corrections_complete = all 27 MANDATORY_TESTS ran AND passed AND no expectation failure; mandatory_tests_all_run = every mandatory id has a ran=True record; k05/exactness/open_findings/deferred all computed, no literals | tests_run block in results | PASS: 27/27; EXPECTATION_FAIL=[]; deferred_decisions=[]; open_findings=[] | SUMMARY / none |

## VERBATIM quotes (byte-substrings of their sources, machine-verified)

### D-5 S3 rule text (PIN-S-R2-1-RULE; source D-5, hash 0cd87ad5...)

```text
        (1) Membership. For each sex s ∈ {F, M} and each family F ∈ {P01, P02}, the C4b paired-valid set is
            V4_s(F) = { i : pL[F,s,i] AND pR[F,s,i] AND full[F,s,i]
                            AND pL[SPL,s,i] AND pR[SPL,s,i] AND full[SPL,s,i] }
            where pL, pR are the decision-layer LEFT / RIGHT probe-success flags and full is the
            decision-layer full-data reference flag of the fitter named (P01, P02: an eligible admissible
            full-data fit under FREEZE r1; SPL: a valid full-data spline fit), exactly as recorded under the
            fields pL, pR, full and the fitter keys P01, P02, SPL. A trajectory for which a named fitter has
            no full-data reference is not a member of any V4_s whose definition names that fitter; if the
            missing reference is the spline's, it is a member of neither family's V4_s.
        (2) D-P04. The consulted common set at level C4b is U4_s = V4_s(P01) ∩ V4_s(P02), built from the same
            flags; both candidates' C4b scalars are recomputed on this same U4_s (freeze record r1 §3 items
            4.1 and 4.2). The trajectory is absent from U4_s by construction. This is a construction-time
            membership condition, not a post-construction invalidity: it never raises
            CONTRACT_VIOLATION_INCONSISTENT_U. CONTRACT_VIOLATION_EMPTY_U keeps its existing meaning. No D-P04
            common-support floor exists and no common-support failure branch exists (freeze record r1 §3
            items 4.2 and 4.3, ratified as MODIFY and NOT_APPLICABLE); under the ratified P03 completeness
            floors an empty consulted set is mathematically excluded on the real path (freeze record r1
            §4.3), and should it nevertheless occur it is a contract-consistency violation, not a scientific
            branch: STOP, provenance investigation, no automated winner, no imputation, no sentinel.
        (3) Denominators and values. n_s is retained. No imputation, sentinel, NaN-valued C4b statistic or
            numeric outcome is produced for an absent reference. After the exclusion the ratified C4b rules
            apply unchanged: the completeness floor |V4_s|/n_s >= c_complete on the reduced set; a sex-level
            statistic over an empty V4_s is undefined and follows §8.1 (C4b not passed for that sex); the
            C4b reporting rule (C4b_F,s, C4b_S,s, |V4_s|/n_s, per-side probe-failure shares) is unchanged.
        (4) Scope. C4a probe-success records, ident_F,s and their denominators are unchanged; C3 and
            CL-F3-04 are unchanged. Membership is determined from the recorded decision-layer flags on the
            real path and in the fixtures alike, never from the presence or absence of an RMSE_edge value.
```

### D-2 S6 K-05 wording (PIN-COVERAGE-DERIVED / coverage row; source D-2, hash da0c4064...)

```text
K-05 invariant: C4b completeness PASS implies C4a PASS.
The excluded combination is C4b-completeness-PASS + C4a-FAIL.
C4b-completeness-FAIL + C4a-PASS is a legitimate case (INJ-C4B-FLOOR-FAIL).
```

### Freeze record r1 S4 double-count declaration (X-11(c) echo; source f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md)

```text
Double-count declaration: a failed probe is counted once as a C4a non-success
(numerator excluded, denominator 2·n_s retained) and once as C4b incompleteness
(absent from V4_s, denominator n_s retained). Declared, not corrected.
```

## TEST_CONSTANT additions of r4 (verification-only; enter no result)

| constant | where | role |
|---|---|---|
| T-A5-SUPPORT vectors (0.5-threshold triple with nextafter(0.5, 0); two-point disconnected support; left-edge pair at indices 3, 7; constant 3.25 vector; NaN/inf/wrong-length invalids) | t_a5_support | TEST_CONSTANT |
| UT-PROBE-DECOUPLE second-half n_s=1 recs pair | ut_probe_decouple | TEST_CONSTANT |
| UT-USET base triple (0.95, 0.10, 0.20, 0.05) x3 incl. SPL | generator uset_construction_cases | TEST_CONSTANT (declared in the r4 manifest) |

```text
new_scientific_literal_by_executor = 0
PI_RATIFIED content transcribed verbatim: PIN-S-R2-1-RULE (D-5, 0cd87ad5...);
  PIN-A5-SUPPORT and PIN-SOLVER-B-UNVERIFIABLE stand in the parent register (D-2, da0c4064...)
Every result above is bound to f3_step2_correction_report_r4_2026-09-27.md and
f3_step2_results_r4_2026-09-24.json (a15b7eff...); "see report" resolves there.
commit = false
```
