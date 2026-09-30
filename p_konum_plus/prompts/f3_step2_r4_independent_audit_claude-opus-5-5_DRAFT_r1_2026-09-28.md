# p_konum_plus — F3 STEP-2 r4 — Independent Audit — DRAFT r1 (2026-09-28)

```text
record                  = f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md
record_class            = independent audit of the STEP-2 r4 package (14 files received on 2026-09-28);
                          child of the r3 audit DRAFT r1 (A-1, 11cfa591…), which it does not rewrite
auditor                 = claude-opus-5-5 (Claude, Cowork session; the model the PI selected for this turn — the
                          serving model may differ; the earlier turns of this session, including A-1, ran as
                          claude-fable-5-1). Not the executor. Decides nothing for the PI. Declares no QUALIFIED
reviewer_prior_exposure = true — this session drafted D-3 and the r4 instruction, filled D-4 and D-5 at the PI's
                          written instructions, derived the INJ-C4B-NOREF row that D-5 pins, and wrote A-1. The
                          check that a delivered outcome equals its D-5 pin therefore compares the executor with this session's
                          own pre-dispatch derivation; it is not an independent derivation
other auditors' records = none received; none used. External review notes the PI shared about S-R2-1 are not inputs
executor                = Claude Code (harness 54274b4e… ; generator 39391730… ; manifest c0b38ceb…)
dispatched instruments  = D-3 5b0e19ea… ; r4 instruction e1283958… ; D-5 0cd87ad5… ; A-1 11cfa591… (input) ;
                          D-1 17187d31… ; D-2 da0c4064…
frozen upstream         = untouched: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (r4 5e594136… as ratified by freeze
                          record r1 7055f186…). Nothing reopened; no scientific literal produced
evidence tiers          = [A] auditor-verified on the delivered bytes ; [A-S] auditor-environment execution of the
                          delivered code (Linux; Python 3.11.15, numpy 1.26.4, scipy 1.14.1 — never a claim about
                          an executor hash) ; [X] executor claim ; [E] external
honesty rule            = every hash here was computed by the auditor with the scripts of §9 or is quoted from a
                          named file; a check the auditor could not run is NOT PERFORMED
sidecar                 = external .sha256 ; no self-hash
```

## 0. Verdict

```text
audit_verdict                 = NOT PASSED
global blockers               = 0
gate-specific blockers        = 1   (R4A-01)
cleanup                       = 3   (R4A-02 … R4A-04)
informational                 = 5   (R4A-05 … R4A-09)
F3_STEP2_r4_status (executor) = PARTIAL_PENDING_PI — supported; corrections_complete = true is not supported
                                (R4A-01; §7)
S-R2-1                        = PI_RULE implemented as D-5 §3 states [A]; EXACT-03 closed with D-5 as source [A]
F3_STEP2 = QUALIFIED          = NOT declared (PI only)
```

In plain words. The r4 package is a large step forward and almost all of it holds on the delivered bytes. The
provenance is clean: the fingerprint recomputed from the delivered harness, generator and manifest equals the
custody record's and is the only prefix in the store manifest (§2). The PI rule for S-R2-1 is implemented as
written — membership by the flags pL, pR, full, the old PENDING pre-check gone — and the four pinned fixtures
come out exactly as D-5 declared. All 33 declared expectations hold when re-checked from the manifest; the
delivered RUN1 content hashes to the claimed canonical value 777fca02…; the auditor's own execution of the
delivered decision layer reproduces all 32 decision-layer evaluation objects and all stops byte for byte, twice
in one process, with no leak between passes; the unit tests for the A.5 support predicate, the comparator guard
and the U-set construction reproduce exactly. Eleven of the twelve adopted r3 findings are closed.

One correction is incomplete. D-3 Y-04 (b) asks that an unrelated solver exception stop its spline context as
STOP_EXACTNESS_PENDING with the dependent statistics PENDING. The harness stops the fit and records the event,
but it then hands the decision layer an ordinary spline-fit failure (valid = False), so C2, C3, C4a/C4b of that
trajectory would be computed as definite outcomes from an unverifiable context. No such event occurred in this
run, so no outcome in the package is affected; the path is simply not implemented past the fit level (R4A-01).
The remaining items are reporting and labelling defects.

## 1. Custody at reception [A] — 14 files

| received as | file | bytes | SHA256 | transmission list |
|---|---|---|---|---|
| fffd324b-… | f3_step2_adequacy_harness_r4_2026-09-24.py | 170,054 | 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c | equal |
| 049507be-… | f3_step2_fixture_generator_r4_2026-09-24.py | 49,937 | 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c | equal |
| 0d8bda7f-… | f3_step2_fixture_manifest_r4_2026-09-24.csv | 20,144 | c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 | equal |
| b4e41aa3-… | f3_step2_r4_preexecution_custody_2026-09-24.md | 4,563 | 0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f | equal |
| 155e931a-… | f3_step2_telemetry_r4_2026-09-24.csv | 4,612,950 | 11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 | equal |
| b3f958c2-… | f3_step2_results_r4_2026-09-24.json | 2,788,639 | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | equal |
| 8bff0308-… | f3_step2_residual_series_r4_2026-09-24.json | 42,820 | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | equal |
| 31faf406-… | f3_step2_test_evidence_r4_2026-09-24.json | 33,741 | 118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 | equal |
| 887cc924-… | f3_step2_class_c_pin_register_r4_2026-09-27.md | 15,604 | 0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4 | equal |
| 77a1a691-… | f3_step2_correction_report_r4_2026-09-27.md | 18,901 | 5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848 | equal |
| 104233a9-… | f3_step2_r4_attempt_log_2026-09-24.md | 7,859 | 8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69 | equal |
| 481cb9c0-… | f3_step2_spline_percall_telemetry_r4_2026-09-24.csv | 2,087,176 | d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 | equal |
| b1605adf-… | f3_step2_r4_restart_store_manifest_2026-09-24.csv | 2,112,964 | f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 | equal |
| 6fbe6b0d-… | f3_step2_r4_transmission_list_2026-09-27.md | 9,936 | 10635daea95656bad089b1888663506cbefa7b6ac36a74793cd9e96ad8ee99b5 | (itself) |

No file contains a CR byte. The instruments named by the custody record and the harness are byte-equal to the
auditor's copies (D-3, r4 instruction, D-5, A-1, D-1, D-2; §9 block [2]). Not received: the 13 r4 sidecars, the
r3 sidecars (group B), the five r3 quarantine notes (C), the superseded r3 bytes (D), the r4 supersession chain
(E) and the T-R3-2 listing (F) — 58 of the 72 entries of the transmission list (R4A-05).

## 2. Which bytes ran [A]

```text
fingerprint formula (harness L2544–2549) on (54274b4e…, 39391730…, c0b38ceb…) and the executor environment
     = 5ef61a412c6bd76c = custody record code_env_fingerprint = the ONLY prefix of the 11,869 store entries
store pids: 31388 (6,086 units, start 2026-09-27T16:05:40) and 29564 (5,783 units, start 17:44:22) — the two
     revision-5 launches of the attempt log (rows 7–8); per-call telemetry carries exactly these two pids
the four superseded r4 revisions (f137299c…, 20d830e0…, 814e395a…, 90ea0ff3…) give four other fingerprints,
     none present in the store — the store was emptied on each harness change, as the attempt log states
manifest regenerated from the delivered generator with the harness's own writer = c0b38ceb… byte-identical
the harness reads the custody record and never opens it for writing (R3A-07)
canonical RUN1 document recomputed from the delivered results (evals + stops + pins{mask_full, fs = True})
     = 777fca02e1f514038e04cb3b5aac5365fa4dd851b03174820ef4692f8c73c2d8 = results.run1_canonical_sha256
```

So every unit of the final output was computed by the delivered bytes, and the delivered RUN1 content is the
content that was hashed. RUN2's equality with RUN1 is the executor's measurement [X]; the auditor's same-process
double evaluation of the decision layer (§5) is consistent with it.

## 3. Checklist

| # | check | executor claim | auditor result |
|---|---|---|---|
| C-01 | 13 deliverables + transmission list hashed; equal to the transmission list, the report hash block, the custody record | equal | PASS [A] |
| C-02 | delivered triple = executed bytes (fingerprint; store prefix) | implied | PASS [A] (§2) |
| C-03 | manifest regenerated byte-identical | c0b38ceb… | PASS [A] |
| C-04 | W-3 custody written outside the process; instruments observed = pinned | EQUAL ×6 | PASS [A] for the six values (auditor's copies); "written externally" [X] (writer not delivered); harness never writes the record [A] |
| C-05 | S-R2-1 = PI_RULE: V4 by pL ∧ pR ∧ full of the named fitter and the spline (P03 L1330–1332; D-P04 via probes_idx L1204 and uset_c4b); pre-check not called | word for word | PASS [A] (code; no call of _s_r2_1_present) |
| C-06 | the four D-5 pins: SCEN-B, INJ-C1-FAIL, INJ-DP04-C1, INJ-C4B-NOREF | hold | PASS [A] on delivered results; [A-S] for the three decision-layer ones (§5) |
| C-07 | EXACT-03 closed with D-5 as source; no STOP_EXACTNESS_PENDING(EXACT-03) anywhere; deferred_decisions = [] | closed | PASS [A] |
| C-08 | register VERBATIM blocks are byte-substrings: rule text of D-5, K-05 wording of D-2, double-count declaration of the freeze record | machine-checked | PASS [A] (3 / 3) |
| C-09 | T-EXPECT-ALL re-done from the manifest | 33 / 33 | PASS [A] (33 declared, 0 mismatches) |
| C-10 | canonical RUN1 content = claimed hash; enlarged document (per-fit theta, L, start-bank size, feature-start flag, failure codes; per spline fit mode, RSS, equivalent modes, per-mode validity); `sexes` removed | 777fca02… | PASS [A] |
| C-11 | RUN1 == RUN2 | true | [X]; consistent with [A-S] same-process double evaluation of the decision layer |
| C-12 | per-call telemetry all phases, per pid; totals per (phase, pid) equal the process block; RUN1 = RUN2 row counts | 12,174 | PASS [A] (nr_gates 60, unit_tests 1,602, run1 3,956 + 1,300, run2 5,256) |
| C-13 | store manifest with pid, start_iso; one fingerprint | 11,869 | PASS [A] |
| C-14 | mode-level telemetry: L and predicates on family rows; RUN2 rows; FIX-STARTS rows | present | PASS [A] (L empty only on SPL rows, which carry RSS in the message; run1 = run2 = 4,645 rows; FIX-STARTS 994 + 522) |
| C-15 | residual series: RUN1 keys, hash links, PIN-ACF bitwise; byte-identical to the r3 export | 11 | PASS [A] (11 / 11; file hash = r3's 3ee624f3…) |
| C-16 | Y-03 (ii) data-driven re-validation with offending pairs; mutation restored | applied | PASS [A-S] (INCONSISTENT_U from re-reading the data; no leak between passes); pairs duplicated and without sex — R4A-03 |
| C-17 | Y-03 (iii) guarded comparator; T-COMPARATOR-NAN calls it | applied | PASS [A-S]; STOP label deviates from D-3 — R4A-03 |
| C-18 | Y-05 T-A5-SUPPORT; violation → C4a and C4b PENDING | applied | PASS [A-S] (10 sub-cases reproduce) and [A] (code L1303–1315) |
| C-19 | Y-02 (b) pure U-set functions used by run_dp04 and UT-USET | applied | PASS [A-S] (5 / 5 reproduce) |
| C-20 | Y-04 (a) (c) (d): classifier, arming, S1 / S2 stages, wrappers restored by reassignment, two passes identical, captures delivered, RUN1 = RUN2 captures | applied | PASS [A] on delivered evidence (S1 [1]; S2 [1, 2]; unit-phase, RUN1 and RUN2 records present; one natural COVERED capture in each run) |
| C-21 | Y-04 (b): UNRELATED event → capture; context STOP; dependent statistics PENDING | applied | FAIL in part — capture and fit-level stop present; dependent statistics not PENDING (R4A-01) |
| C-22 | Y-01 / R3A-06 provenance and counters | 3 / 3 | PASS [A] (store, telemetry, attempt log consistent) |
| C-23 | R3A-07 erratum in the r4 log; r3 log untouched, referenced by hash | done | PASS [A] for content and hash 25316389…; the r3 per-revision triples it points to are not in the report — R4A-04 |
| C-24 | Y-16 / R3A-08 coverage derived; K-05 row verbatim | derived | PASS for the mechanism [A]; four downgrades are resolver artefacts — R4A-02 |
| C-25 | Y-08 / R3A-11 end-state fields computed; 27 mandatory tests | 27 / 27 | PASS [A] for computation (27 on the list, 27 recorded, all passed); what the field covers — R4A-08 |
| C-26 | Y-17 / R3A-09 every STOP return writes a stops record | yes | PASS [A] (code) |
| C-27 | R3A-01 register authored, child of r2 register f263eace… | authored | PASS [A] (parent hash equals the auditor's copy of the r2 register) |
| C-28 | report completeness (R3A-12) | complete | PARTIAL — deliverable 11 not authored; register, report and log hashes given as "(sidecar)"; dangling r3 cross-reference — R4A-04 |
| C-29 | parents unchanged, 40 / 40 sidecars | true | [X] — sidecars not received |
| C-30 | NR-01 (i) / NR-SPL / real-fit run | pass | [X]; real-fit [A-S] re-execution NOT PERFORMED this revision (R4A-09) |
| C-31 | no real data; no 6B; no QUALIFIED wording; no new scientific literal | asserted | PASS [A] (strings; register "new_scientific_literal_by_executor = 0") |
| C-32 | end state PARTIAL_PENDING_PI | as D-5 §7 expected | PASS as status |

## 4. Findings

| id | classification | finding | gate effect | closure action | authority |
|---|---|---|---|---|---|
| R4A-01 | gate-specific blocker | Y-04 (b) / R3A-03 not closed past the fit level. On an UNRELATED event fit_spline returns valid = False with failure = STOP_EXACTNESS_PENDING(tag) (L1029–1038), but run_real_scenario records only the validity: full-data context → the spline full flag False (L1815); fold context → `cc = False` (L1835–1839); probe context → probe failure (L1846–1848). The decision layer therefore treats an unverifiable context as a definite spline failure (V2 / V3 / V4 exclusion, C4a numerator), not PENDING. T-EXC-UNRELATED-TYPE checks the fit-level return only (L2186–2195) | none in this run (natural UNRELATED events = 0); on a natural event the P03 / D-P04 outcomes of that sex would be reported as definite while D-3 requires "dependent statistics PENDING"; the status would still be PARTIAL_PENDING_PI through EXACT-04 | carry a per-trajectory, per-context pending flag into the decision grammar (as `a5v` is carried) for the spline full, fold and probe contexts; route every criterion that uses that context (C2, C3, C4a, C4b of that sex, and the D-P04 levels built on them) to STOP_EXACTNESS_PENDING(<id>); one decision-layer fixture with the flag set and an evaluation-level assertion added to T-EXC-UNRELATED-TYPE | X |
| R4A-02 | cleanup | Coverage resolver: four rows are downgraded to UNCOVERED although their evidence ran and passed — "C2 pass" and "C3 pass" (authored evidence "INJ baselines" names no fixture id), "D-P04 comparator never RESOLVED/EQUIVALENT on NaN" (the token pattern admits no "T-COMPARATOR-NAN"), "clean execution / process provenance disclosed" (evidence is the attempt log). The report discloses this | uncovered_coverage_rows overstates the gaps; no status effect (T-R2-2 and A.5 (iii) keep the status PARTIAL_PENDING_PI) | name fixture / test ids in the authored evidence texts and admit T-* test ids in the resolver | X |
| R4A-03 | cleanup | Labels and detail: the guarded comparator's STOP is recorded as CONTRACT_VIOLATION_EMPTY_U (L1669) where D-3 Y-03 (iii) says CONTRACT_VIOLATION_INCONSISTENT_U; the TEST_ONLY tag is "TEST_ONLY_INJECTION" where D-3 Y-04 (b) writes "TEST_ONLY_INJECTED"; the INCONSISTENT_U stop record lists the pair (P01, 0) four times and without the sex (both reproduced [A-S]) | none (the comparator branch is unreachable after P03 by construction) | use the D-3 labels; de-duplicate the offending pairs and add the sex | X |
| R4A-04 | cleanup | Report and log: deliverable 11 (W-1 (a) start-state inventory) not authored, disclosed as "r3 start-state stands"; the r4 attempt log says the r3 generator / manifest hashes per revision "are given per-revision in the r3 section of the r4 correction report" — the report contains none of them; the report's hash block gives register, report and log as "(sidecar)" | none on the verdict; the r3 half of R3A-07's "three hashes per attempt" remains open | author the inventory or record the PI-visible deviation; add the r3 per-revision triples; print the register and log hashes in the report | X |
| R4A-05 | informational | Transmission: 14 of the 72 transmission-list entries were received (the message speaks of 58 attachments). Sidecar agreement, the quarantine notes, the superseded bytes, the r3 store quarantine and the T-R3-2 listing are NOT PERFORMED | none on the verdict | PI: attach groups A-sidecars … F if the chain is wanted at tier [A] | T |
| R4A-06 | informational | S-R2-1 pins: the four fixture outcomes equal D-5's pins; the INJ-C4B-NOREF pin was derived by this session before dispatch, so agreement is not an independent derivation (header) | none | none | — |
| R4A-07 | informational | Models: the executor reports claude-sonnet-5[1m] for the r2, r3 and early r4 work and claude-fable-5[1m] after the mid-cycle switch, with no effort override; this record is written by claude-opus-5-5, A-1 by claude-fable-5-1 | none | none | — |
| R4A-08 | informational | corrections_complete is computed as: 27 mandatory tests passed and no expectation failure; corrections evidenced by a document rather than a test (register, report, erratum) lie outside that computation. The r3 closure action asked for exactly this computation; the auditor's view is in §7 | none | optional: add document-level checks to the list | X (optional) |
| R4A-09 | informational | Real-fit re-execution [A-S] not performed this revision: a line diff of fit_family against r3 shows 5 non-comment lines, of the ACF / pin code none, the residual export is byte-identical to r3's, and A-1 §7 holds the r3 [A-S] re-execution; the decision layer and the pure unit tests were re-executed (§5). spline_nonregression carries `passed=True` as a literal (L3278) after the NR-SPL assertion and record (L2615) | none | on request, a child revision with a full re-execution | — |

## 5. Auditor execution of the delivered decision layer [A-S]

The script `r4_02_decision_layer_repro.py` (§9) imports the unmodified harness and generator, evaluates the 32
decision-layer fixtures twice in one process and calls the three pure unit tests. main() is not called.

```text
harness sha256: 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c
generator sha256: 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c
decision-layer fixtures: 32 | pass1 == pass2 (same process): True | fixture data changed by pass 1: False
identical to the executor's evaluation objects: 32 / 32 | differing: []
INJ stops identical to the executor's: True [('INJ-BOTH-FAIL', 'BOTH_FAIL_REDESIGN'), ('INJ-DP04-EMPTY-U', 'CONTRACT_VIOLATION_EMPTY_U'), ('INJ-U-POST-CONSTRUCTION-INVALID', 'CONTRACT_VIOLATION_INCONSISTENT_U'), ('INJ-NAN-STAT-SPL', 'BOTH_FAIL_REDESIGN'), ('INJ-P03-BOTHFAIL-C4PENDING', 'BOTH_FAIL_REDESIGN')]
  INJ-C1-FAIL                      p03=('FAIL', 'PASS') mech=ONLY_P02_PASSES
  INJ-DP04-C1                      p03=('PASS', 'PASS') mech=RESOLVED_MECHANISM_P01
  INJ-C4B-NOREF                    p03=('PASS', 'PASS') mech=TERMINAL_FALLBACK_MECHANISM_P01
  INJ-U-POST-CONSTRUCTION-INVALID  p03=('PASS', 'PASS') mech=STOP_CONTRACT_VIOLATION_INCONSISTENT_U
  INCONSISTENT_U stop record: [{'fixture': 'INJ-U-POST-CONSTRUCTION-INVALID', 'level': 'C2', 'member': 0, 'offending_pairs': [{'fitter': 'P01', 'observation': 0}, {'fitter': 'P01', 'observation': 0}, {'fitter': 'P01', 'observation': 0}, {'fitter': 'P01', 'observation': 0}], 'sex': 'F', 'stop': 'CONTRACT_VIOLATION_INCONSISTENT_U'}]
t_a5_support equal to delivered: True | pass: True
t_comparator_nan equal to delivered: True | pass: True
ut_uset_construction equal to delivered: True | cases ok: {'a': True, 'b': True, 'c': True, 'd': True, 'e': True}
guard: {'0.5': True, 'nan': False, 'inf': False, 'None': False}
```

## 6. Closure map (r3 findings as adopted by the r4 instruction §3)

| item | executor claim | auditor result |
|---|---|---|
| R3A-01 register | closed | CLOSED [A] |
| R3A-02 Y-07 / X-11 | closed | CLOSED [A] |
| R3A-03 Y-04 (b) (d) | closed | (d) CLOSED [A]; (b) capture and fit-level stop CLOSED [A], dependent statistics NOT CLOSED — R4A-01 |
| R3A-04 Y-03 (ii) (iii) | closed | CLOSED [A-S]; labels and pair detail — R4A-03 |
| R3A-05 Y-05 | closed | CLOSED [A-S] |
| R3A-06 Y-01 counters | closed | CLOSED [A] |
| R3A-07 attempt log / custody | closed | CLOSED [A] except the r3 per-revision triples — R4A-04 |
| R3A-08 coverage / K-05 | closed | CLOSED [A] as mechanism; resolver artefacts — R4A-02 |
| R3A-09 Y-17 | closed | CLOSED [A] |
| R3A-10 Y-02 (b) | closed | CLOSED [A-S] |
| R3A-11 Y-08 | closed | CLOSED [A] (R4A-08) |
| R3A-12 report | closed | PARTIAL — R4A-04 |
| R3A-13 transmission | addressed | PARTIAL — R4A-05 |
| R3A-14 r2 history | acknowledged | stands as disclosed |
| R3A-16 optional | not applied, reasoned | accepted (SCEN-A circularity argument is sound) |

## 7. Register (S / T / X) and status

```text
S  none open. S-R2-1 = PI_RULE (D-5) — implemented; nothing in this record reopens or re-reads it
T  T-R2-2 = AUTHORIZE_RESTART (in narrowed_evidence) ; T-R4-1 transmission of the 58 missing entries (R4A-05)
X  blocker  R4A-01 ; cleanup R4A-02 … R4A-04 ; optional R4A-08

corrections_complete      = false in the auditor's view (R4A-01); the executor's value true is its test-based
                            computation
mandatory_tests_all_run   = true [A] (27 / 27 recorded and passed)
deferred_decisions        = []
narrowed_evidence         = [T-R2-2]
uncovered_coverage_rows   = ["A.5 (iii) inadmissible refit"] on the evidence; the four other listed rows are
                            resolver artefacts (R4A-02)
open_findings             = [] (no natural UNRELATED event)
F3_STEP2_r4_status        = PARTIAL_PENDING_PI (agrees with the executor)
F3_STEP2 = QUALIFIED      = NOT declared ; F3_EXECUTION_READY = false ; commit = false
```

What the next step needs: from the executor, R4A-01 (a narrow change: one flag carried into the decision
grammar, one fixture, one assertion) and the cleanup items; from the PI, nothing scientific. Even with R4A-01
closed, the status stays PARTIAL_PENDING_PI while T-R2-2 is in narrowed_evidence and A.5 (iii) is uncovered;
whether that end state is acceptable for moving on is the PI's decision, not this record's.

## 8. Evidence for R4A-01 (delivered harness, verbatim)

```text
 1029:     if any_mode_unrelated:
 1030:         ctx_unrel = [c for c in EXC_CAPTURES
 1031:                      if c.get("kind") == "UNRELATED"
 1032:                      and c.get("fixture") == fixture_id
 1033:                      and c.get("mask_id") == mask_id]
 1034:         all_test_only = ctx_unrel and all(
 1035:             "TEST_ONLY" in c.get("message", "") for c in ctx_unrel)
 1036:         tag = "TEST_ONLY_INJECTION" if all_test_only else "F3-STEP2-EXACT-04"
 1037:         return dict(valid=False, failure="STOP_EXACTNESS_PENDING(%s)" % tag,
 1038:                     per_mode_valid=per_mode_valid)
  ...
 1815:             recs["SPL"]["full"].append(spf["valid"])
  ...
 1829:             for fname, train, held in fold_masks():
 1830:                 inj = injmap.get((trg, "SPL", fname)) == "TEST_ONLY_INJECTION"
 1831:                 if (trg, "SPL", fname) in injmap:
 1832:                     FIDELITY_EXECUTED.append((sc["fixture_id"], trg, "SPL", fname))
 1833:                 r = fit_spline(spl, sc["fixture_id"], x, train, telemetry,
 1834:                                mid(f"{sx}{ti}:{fname}"), inject_failure=inj)
 1835:                 if r["valid"]:
 1836:                     pred_cv[held] = r["ghat"][held]
 1837:                 else:
 1838:                     cc = False
 1839:             recs["SPL"]["cc"].append(cc)
  ...
 1843:                                            ("R", RIGHT_PROBE_O, np.arange(131, 146), a5_i_R)):
 1844:                 r = fit_spline(spl, sc["fixture_id"], x, obsP, telemetry,
 1845:                                mid(f"{sx}{ti}:probe{side}"))
 1846:                 probe_raw = bool(r["valid"])
 1847:                 p_c4a = probe_raw and (a5_i is False)
 1848:                 recs["SPL"]["p" + side].append(p_c4a)
  ...
 1455:         # between this point and run_dp04's re-validation, then undone.
 1456:         stat_field = {"C2": "rho", "C3": "phi", "C4b": "rR", "C5": "sst"}
 1457:         mutations_to_restore = []
 1458:         for crit_name, field in stat_field.items():
 1459:             idx = flags.get(f"inject_post_construction_invalid_{crit_name}")
 1460:             if idx is not None:
 1461:                 for sx in SEXES:
 1462:                     arr = S[sx]["P01"]["d"][field]
 1463:                     mutations_to_restore.append((arr, idx, arr[idx]))
 1464:                     arr[idx] = float("nan")
 1465:         ev["dp04"] = run_dp04(fx_id, S, n_s, flags, stops)
 1466:         for arr, idx, orig in mutations_to_restore:
  ...
 1580:                         U = uset_c2(st1, st2, sp)
 1581:                         if flags.get("inject_empty_U2"):
 1582:                             U = []
 1583:                         src = S[sx][fam]
 1584:                         v = src["med_over"](src["d"]["rho"], U)
 1585:                     elif crit == "C3":
 1586:                         U = uset_c3(st1, st2, sp)
 1587:                         src = S[sx][fam]
 1588:                         v = src["med_over"]([abs(x) if x is not None else None
 1589:                                              for x in src["d"]["phi"]], U)
 1590:                     elif crit == "C4b":
 1591:                         U = uset_c4b(st1, st2, sp)
 1592:                         src = S[sx][fam]
 1593:                         v = src["med_over"]([_combined_edge(src["d"], i)
 1594:                                              for i in range(n_s)], U)
 1595:                     else:  # C5 -- P-01/P-02 only, NO spline term
 1596:                         U = uset_c5(st1, st2)
 1597:                         src = S[sx][fam]
  ...
 1663:         # (NaN/inf) on either side is a contract violation, never a silent
 1664:         # "abs(nan) <= tau" (which Python evaluates False, masquerading as
 1665:         # a legitimate RESOLVED outcome -- see T_COMPARATOR_NAN). R3A-09:
 1666:         # this STOP return writes its `stops` record like every other one
 1667:         # (Y-17: every STOP-outcome consulted-level return writes one).
 1668:         if not (_guarded_scalar_ok(scal["P01"]) and _guarded_scalar_ok(scal["P02"])):
 1669:             stops.append(dict(fixture=fx_id, stop="CONTRACT_VIOLATION_EMPTY_U",
  ...
 2186:     unrel_result = fit_spline(spl, "INJ-EXC-UNRELATED-TYPE", x3, FULL_O, tel, "exc:unrel")
 2187:     unrel_caps = [c for c in EXC_CAPTURES[before:] if c.get("kind") == "UNRELATED"
 2188:                  and "unrelated exception type" in c.get("message", "")]
 2189:     out["UNRELATED_TYPE"] = dict(
 2190:         caught_not_crashed=(len(unrel_caps) == 1),
 2191:         exception_type_recorded=(unrel_caps[0]["exception_type"] if unrel_caps else None),
 2192:         context_unverifiable=(not unrel_result.get("valid", True)),
 2193:         pass_=(len(unrel_caps) == 1
 2194:               and unrel_caps[0]["exception_type"] == "ValueError"
 2195:               and not unrel_result.get("valid", True)))
 2196:     VALUEERROR_INJECT_TARGET.update(active=False)
  ...
 3278:         spline_nonregression=dict(passed=True, rows=snr_rows),
  ...
```

## 9. Appendix — evidence scripts and their verbatim output

Script `r4_01_package_checks.py`:

```python
"""Evidence script 01 (F3 STEP-2 r4 independent audit, auditor claude-opus-5-5, 2026-09-28). Read-only.
Every value printed is computed from the 14 received files (recv/) and from the instrument files the auditor
holds (outputs/ and uploads/). Nothing is asserted about files that were not received."""
import hashlib, json, csv, os, re, io, struct, math, collections, importlib.util, sys
R = "/home/claude/audit_r4/recv/"; OUT = "/mnt/user-data/outputs/"; UP = "/root/.claude/uploads/9c789a02-f865-56de-9f2f-e299f3cfca3a/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
def up(prefix):
    f = [x for x in os.listdir(UP) if x.startswith(prefix)]; assert len(f) == 1, prefix; return UP + f[0]
N = dict(har="f3_step2_adequacy_harness_r4_2026-09-24.py", gen="f3_step2_fixture_generator_r4_2026-09-24.py",
         man="f3_step2_fixture_manifest_r4_2026-09-24.csv", cus="f3_step2_r4_preexecution_custody_2026-09-24.md",
         tel="f3_step2_telemetry_r4_2026-09-24.csv", res="f3_step2_results_r4_2026-09-24.json",
         resid="f3_step2_residual_series_r4_2026-09-24.json", te="f3_step2_test_evidence_r4_2026-09-24.json",
         reg="f3_step2_class_c_pin_register_r4_2026-09-27.md", rep="f3_step2_correction_report_r4_2026-09-27.md",
         log="f3_step2_r4_attempt_log_2026-09-24.md", pc="f3_step2_spline_percall_telemetry_r4_2026-09-24.csv",
         store="f3_step2_r4_restart_store_manifest_2026-09-24.csv", tl="f3_step2_r4_transmission_list_2026-09-27.md")
H = {k: sha(R + v) for k, v in N.items()}

print("== [1] custody at reception: observed hash vs transmission list vs report hash block vs custody record")
tl = open(R + N["tl"], encoding="utf-8").read(); rep = open(R + N["rep"], encoding="utf-8").read(); cus = open(R + N["cus"], encoding="utf-8").read()
tlmap = {m.group(2).split("/")[-1]: m.group(1) for m in re.finditer(r"^([0-9a-f]{64})  (\S+)$", tl, re.M)}
for k, v in N.items():
    cr = open(R + v, "rb").read().count(bytes([13]))
    print("  %-4s %s CR=%d | transmission_list=%s | in report=%s | in custody=%s" % (k, H[k], cr,
          {True: "EQUAL", False: "DIFF"}[tlmap.get(v) == H[k]] if v in tlmap else "absent",
          H[k] in rep, H[k] in cus))
print("  transmission list entries:", len(tlmap), "| sidecar entries listed:", sum(1 for x in tlmap if x.endswith(".sha256")))

print("\n== [2] instruments named by the package vs the auditor's copies")
inst = dict(D3=OUT + "Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
            R4=OUT + "Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md",
            D5=OUT + "f3_step2_r4_pi_dispatch_record_2026-09-24.md",
            A1=OUT + "f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md",
            D1=up("892d0f75-"), D2=up("8dbc7dd4-"), FRZ=up("9ebba060-"))
for k, p in inst.items():
    h = sha(p); print("  %-3s %s | in custody record: %s | in harness: %s" % (k, h, h in cus, h in open(R + N["har"], encoding="utf-8").read()))

print("\n== [3] which bytes ran: fingerprint (harness L2544-2549 formula) and store-manifest prefixes")
har = open(R + N["har"], encoding="utf-8").read()
F2 = re.search(r'^F2_HASH = "([0-9a-f]{64})"', har, re.M).group(1); SPL = re.search(r'^SPL_HASH = "([0-9a-f]{64})"', har, re.M).group(1)
def fp(h, g, m, env=("3.11.7", "1.26.4", "1.14.1", "Windows-10-10.0.19045-SP0")):
    return hashlib.sha256("|".join([h, g, m, F2, SPL, *env, "1", "1", "1"]).encode()).hexdigest()[:16]
f_deliv = fp(H["har"], H["gen"], H["man"])
print("  fingerprint(delivered triple, executor env) =", f_deliv, "| custody record says:", re.search(r"code_env_fingerprint = (\w+)", cus).group(1))
store = list(csv.DictReader(open(R + N["store"], newline="", encoding="utf-8")))
pref = collections.Counter(r["path"].split("__")[0] for r in store)
print("  store manifest rows:", len(store), "| columns:", list(store[0].keys()), "| prefixes:", dict(pref))
print("  store pids:", dict(collections.Counter(r["pid"] for r in store)), "| start_iso by pid:", {p: sorted(set(r["start_iso"] for r in store if r["pid"] == p)) for p in set(r["pid"] for r in store)})
kinds = collections.Counter(re.sub(r"^[0-9a-f]{16}__", "", r["path"]).split("_")[0] for r in store)
print("  unit kinds:", dict(kinds))
for name, h in (("rev1 f137299c", "f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418"), ("rev2 20d830e0", "20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306"),
                ("rev3 814e395a", "814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f"), ("rev4 90ea0ff3", "90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805")):
    print("  fingerprint(%s, delivered gen+manifest) = %s ; in store: %s" % (name, fp(h, H["gen"], H["man"]), fp(h, H["gen"], H["man"]) in pref))
print("  custody record names harness/generator/manifest:", all(H[k] in cus for k in ("har", "gen", "man")),
      "| attempt_number:", re.search(r"attempt_number = ([^\n]+)", cus).group(1), "| harness ATTEMPT_NUMBER:", re.search(r"^ATTEMPT_NUMBER = (\d+)", har, re.M).group(1))
print("  harness writes the custody file? open(CUSTODY_PATH, 'w'...):", bool(re.search(r"open\(CUSTODY_PATH,\s*\"w\"", har)), "| reads it:", 'open(CUSTODY_PATH, "r"' in har)

print("\n== [4] manifest regenerated from the delivered generator with the harness's own writer (csv, LF, ascii)")
spec = importlib.util.spec_from_file_location("gen_r4", R + N["gen"]); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)
buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(gen.MANIFEST_HEADER); w.writerows(gen.manifest_rows())
print("  regenerated sha256 =", hashlib.sha256(buf.getvalue().encode("ascii")).hexdigest(), "| delivered =", H["man"])
print("  harness writer form present (csv.writer lineterminator LF):", 'lineterminator="\\n"' in har)

print("\n== [5] results structure, canonical document recomputed from the delivered RUN1 content")
r = json.load(open(R + N["res"])); te = json.load(open(R + N["te"]))
ev = {e["fixture_id"]: e for e in r["evaluations"]}
print("  evaluations:", len(ev), "| any 'sexes' key:", any("sexes" in e for e in r["evaluations"]), "| keys (SCEN-A):", sorted(ev["SCEN-A"].keys()))
fits = ev["SCEN-A"]["fits"]; f0 = fits["F0"]
print("  SCEN-A fits F0 keys:", sorted(f0.keys())[:12], "...")
def show(o, d=0):
    return {k: (sorted(v.keys())[:14] if isinstance(v, dict) else type(v).__name__) for k, v in o.items()} if isinstance(o, dict) else type(o).__name__
first = next(iter(f0.values())); print("  one fits entry:", show(first))
pins_guess = dict(mask_full=True, fs=True)
doc = dict(evals=r["evaluations"], stops=r["stops"], pins=pins_guess)
hc = hashlib.sha256(json.dumps(doc, sort_keys=True).encode("utf-8")).hexdigest()
print("  sha256(json.dumps({evals, stops, pins{mask_full:True, fs:True}}, sort_keys)) =", hc)
print("  == results.run1_canonical_sha256:", hc == r["run1_canonical_sha256"], "| run1 == run2 (executor):", r["run1_canonical_sha256"] == r["run2_canonical_sha256"], r["run1_canonical_sha256"])

print("\n== [6] T-EXPECT-ALL re-done by the auditor from the manifest's expected_* columns")
man = list(csv.DictReader(open(R + N["man"], newline="")))
UL = {"U2": "C2", "U3": "C3", "U4": "C4b", "U5": "C5"}; declared = 0; fails = []
for row in man:
    fid = row["fixture_id"]; e = ev.get(fid)
    exp = {k: row[k] for k in ("expected_p03", "expected_mechanism_outcome", "expected_resolved_level", "expected_U_sizes", "expected_stops", "expected_undefined")}
    if not any(exp.values()): continue
    declared += 1; mism = []
    if e is None: fails.append((fid, "no evaluation")); continue
    if exp["expected_p03"] and tuple(exp["expected_p03"].split(";")) != (e["p03"]["P01"], e["p03"]["P02"]): mism.append("p03")
    if exp["expected_mechanism_outcome"] and exp["expected_mechanism_outcome"] != e["mechanism_outcome"]: mism.append("mechanism")
    if exp["expected_resolved_level"] and (e.get("dp04") or {}).get("resolved_level") != exp["expected_resolved_level"]: mism.append("level")
    if exp["expected_U_sizes"]:
        disc = {b["level"]: b for b in (e.get("dp04") or {}).get("disclosure", [])}
        for part in exp["expected_U_sizes"].split(";"):
            key, val = part.split("="); uk, sx = (key.split(":") + ["*"])[:2]
            for s2 in (("F", "M") if sx == "*" else (sx,)):
                got = ((disc.get(UL[uk]) or {}).get("per_sex") or {}).get(s2, {}).get("U_size")
                if got != int(val): mism.append(f"{uk}{s2}={got}")
    if exp["expected_stops"] and exp["expected_stops"] not in [s["stop"] for s in r["stops"] if s["fixture"] == fid]: mism.append("stops")
    if exp["expected_undefined"]:
        for part in exp["expected_undefined"].split(";"):
            key, val = part.split("="); fam, crit, sx = key.split(":")
            if e["criteria"][fam][crit][sx].get("undefined") != (val == "True"): mism.append(f"undefined[{key}]")
    if mism: fails.append((fid, mism))
print("  declared:", declared, "| auditor mismatches:", fails or "none", "| results.expectation_checks:", {k: v for k, v in r["expectation_checks"].items() if k != "detail"})

print("\n== [7] the four D-5-pinned S-R2-1 fixtures, as delivered")
for fid in ("SCEN-B", "INJ-C1-FAIL", "INJ-DP04-C1", "INJ-C4B-NOREF"):
    e = ev[fid]; d = e.get("dp04") or {}
    usz = {b["level"]: {sx: b["per_sex"][sx]["U_size"] for sx in b["per_sex"]} for b in d.get("disclosure", []) if "per_sex" in b}
    c4b = {f"{fam}:{sx}": (e["criteria"][fam]["C4b"][sx].get("share"), e["criteria"][fam]["C4b"][sx].get("n_valid"), e["criteria"][fam]["C4b"][sx].get("passed"), e["criteria"][fam]["C4b"][sx].get("undefined")) for fam in ("P01", "P02") for sx in ("F", "M")}
    print("  %-14s p03=%s mech=%s level=%s path=%s U=%s stops=%s" % (fid, (e["p03"]["P01"], e["p03"]["P02"]), e["mechanism_outcome"], d.get("resolved_level"), d.get("consulted_path"), usz, [s["stop"] for s in r["stops"] if s["fixture"] == fid]))
    print("     C4b (share hex, n_valid, passed, undefined):", c4b)
print("  any STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-03) anywhere in evaluations:", "F3-STEP2-EXACT-03" in json.dumps(r["evaluations"]))
print("  exactness_findings:", r["exactness_findings"], "| closed:", r["exactness_findings_closed_this_cycle"])

print("\n== [8] telemetry: per-call (all phases, pids) and mode-level (L, predicates, RUN2 rows, FIX-STARTS rows)")
pc = list(csv.DictReader(open(R + N["pc"], newline="", encoding="utf-8")))
print("  per-call rows:", len(pc), "| by (phase,pid):", dict(collections.Counter((x["phase"], x["pid"]) for x in pc)), "| == results.process:", {f"{a}/{b}": c for (a, b), c in collections.Counter((x["phase"], x["pid"]) for x in pc).items()} == r["process"]["spline_telemetry_calls_by_phase_pid"])
print("  run1 == run2 row counts:", sum(1 for x in pc if x["phase"] == "run1") == sum(1 for x in pc if x["phase"] == "run2"))
tel = list(csv.DictReader(open(R + N["tel"], newline="", encoding="utf-8")))
print("  mode-level rows:", len(tel), "| columns:", list(tel[0].keys()))
print("  rows by mask prefix:", dict(collections.Counter(x["mask_id"].split(":")[0] for x in tel)), "| by fixture:", dict(collections.Counter(x["fixture"] for x in tel)))
print("  L empty by fitter:", dict(collections.Counter((x["fitter"], x["L"] in ("", "None")) for x in tel)))
print("  L empty count:", sum(1 for x in tel if x["L"] in ("", "None")), "| rows with non-empty predicates:", sum(1 for x in tel if x["predicates"] not in ("", "[]")), "| distinct predicates:", sorted(set(x["predicates"] for x in tel))[:10])

print("\n== [9] residual series (Y-21)")
rs = json.load(open(R + N["resid"])); link = te["residual_link"]; acfmap = {x["vector"]: x for x in te["acf"]}
def acf(vals):
    T = len(vals); s = 0.0
    for t in range(T): s = s + vals[t]
    rbar = s / float(T); a = [v - rbar for v in vals]; num = 0.0
    for t in range(T - 1): num = num + a[t] * a[t + 1]
    den = 0.0
    for t in range(T): den = den + a[t] * a[t]
    return abs(num / den)
ok = 0
for k in sorted(rs):
    vals = [float.fromhex(v) for v in rs[k]]; hh = hashlib.sha256(struct.pack("<%dd" % len(vals), *vals)).hexdigest()
    ok += (hh == link[k]["sha256"] == acfmap[k]["sha256_146_float64_le"] and acf(vals).hex() == acfmap[k]["phi"])
print("  keys:", len(rs), "== link:", set(rs) == set(link), "| sha==link==acf and phi bitwise:", ok, "/", len(rs), "| file == r3 export 3ee624f3…:", H["resid"] == "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f")

print("\n== [10] register VERBATIM blocks vs sources (byte-substring)")
reg = open(R + N["reg"], encoding="utf-8").read()
FENCE = chr(96) * 3
blocks = re.findall(FENCE + r"text\n(.*?)\n" + FENCE, reg, re.S)
src = {k: open(inst[k], encoding="utf-8").read() for k in ("D5", "D2", "FRZ")}
for i, b in enumerate(blocks[1:4], 1):
    print("  block %d (%d chars): in D-5=%s in D-2=%s in freeze record=%s" % (i, len(b), b in src["D5"], b in src["D2"], b in src["FRZ"]))
print("  results.double_count_declaration substring of freeze record (whitespace-normalized):", re.sub(r"\s+", " ", r["double_count_declaration"]) in re.sub(r"\s+", " ", src["FRZ"]))
k05 = [x for x in r["coverage"] if x[0].startswith("K-05")][0][0]
print("  coverage K-05 row title in D-2 (whitespace-normalized):", re.sub(r"\s+", " ", k05) in re.sub(r"\s+", " ", src["D2"]))

print("\n== [11] tests and end state")
print("  mandatory list (harness):", len([t for t in re.findall(r"\"([^\"]+)\"", re.search(r"MANDATORY_TESTS = \[(.*?)\]", har, re.S).group(1))]), "| results.tests_run:", len(r["tests_run"]), "all passed:", all(v["passed"] for v in r["tests_run"].values()))
print("  end_state:", json.dumps(r["end_state"]))
print("  coverage rows:", len(r["coverage"]), "| downgraded:", r["coverage_downgraded_rows"])
for row in r["coverage"]:
    if str(row[3]).startswith("UNCOVERED"): print("    UNCOVERED:", row[0], "|", row[3][:90])

print("\n== [12] code facts (line numbers of the delivered harness)")
L = har.split("\n")
def find(pat): return [i + 1 for i, l in enumerate(L) if re.search(pat, l)]
print("  _s_r2_1_present called from code (excluding its def):", [i for i in find(r"_s_r2_1_present\(") if not L[i - 1].lstrip().startswith("def ")])
print("  V4 in evaluate_fixture includes full flags:", find(r'and d\["full"\]\[i\]$'), "| probes_idx includes full:", find(r'probes_idx = \[i for i in range\(n_s\) if d\["pL"\]\[i\] and d\["pR"\]\[i\]$'))
print("  guarded comparator STOP label:", [L[i - 1].strip() for i in find(r'stop="CONTRACT_VIOLATION_EMPTY_U",$')], "at", find(r'stop="CONTRACT_VIOLATION_EMPTY_U",$'))
print("  spline_nonregression passed literal:", find(r"spline_nonregression=dict\(passed=True"), "| NR-SPL record_test:", find(r'record_test\("NR-SPL"'))
print("  docstring mentions ATTEMPT 4 live:", find(r"ATTEMPT 4 \(this file, live\)"))
print("  report: deliverable 11 line:", [l for l in rep.split("\n") if l.startswith("| 11 |")])
print("  report 64-hex values:", len(set(re.findall(r"\b[0-9a-f]{64}\b", rep))))
```

Output:

```text
== [1] custody at reception: observed hash vs transmission list vs report hash block vs custody record
  har  54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c CR=0 | transmission_list=EQUAL | in report=True | in custody=True
  gen  393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c CR=0 | transmission_list=EQUAL | in report=True | in custody=True
  man  c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 CR=0 | transmission_list=EQUAL | in report=True | in custody=True
  cus  0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f CR=0 | transmission_list=EQUAL | in report=True | in custody=False
  tel  11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 CR=0 | transmission_list=EQUAL | in report=True | in custody=False
  res  a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 CR=0 | transmission_list=EQUAL | in report=True | in custody=False
  resid 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f CR=0 | transmission_list=EQUAL | in report=True | in custody=False
  te   118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 CR=0 | transmission_list=EQUAL | in report=True | in custody=False
  reg  0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4 CR=0 | transmission_list=EQUAL | in report=False | in custody=False
  rep  5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848 CR=0 | transmission_list=EQUAL | in report=False | in custody=False
  log  8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69 CR=0 | transmission_list=EQUAL | in report=False | in custody=False
  pc   d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 CR=0 | transmission_list=EQUAL | in report=True | in custody=False
  store f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 CR=0 | transmission_list=EQUAL | in report=True | in custody=False
  tl   10635daea95656bad089b1888663506cbefa7b6ac36a74793cd9e96ad8ee99b5 CR=0 | transmission_list=absent | in report=False | in custody=False
  transmission list entries: 72 | sidecar entries listed: 27

== [2] instruments named by the package vs the auditor's copies
  D3  5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 | in custody record: True | in harness: True
  R4  e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 | in custody record: True | in harness: True
  D5  0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 | in custody record: True | in harness: True
  A1  11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6 | in custody record: True | in harness: True
  D1  17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 | in custody record: True | in harness: False
  D2  da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 | in custody record: True | in harness: True
  FRZ 7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460 | in custody record: False | in harness: False

== [3] which bytes ran: fingerprint (harness L2544-2549 formula) and store-manifest prefixes
  fingerprint(delivered triple, executor env) = 5ef61a412c6bd76c | custody record says: 5ef61a412c6bd76c
  store manifest rows: 11869 | columns: ['path', 'size_bytes', 'sha256', 'pid', 'start_iso'] | prefixes: {'5ef61a412c6bd76c': 11869}
  store pids: {'31388': 6086, '29564': 5783} | start_iso by pid: {'29564': ['2026-09-27T17:44:22.567929'], '31388': ['2026-09-27T16:05:40.581906']}
  unit kinds: {'nrgates': 1, 'onestart': 2081, 'realscen': 4, 'splmode': 9782, 'unittests': 1}
  fingerprint(rev1 f137299c, delivered gen+manifest) = e9d93b0e7e5a9834 ; in store: False
  fingerprint(rev2 20d830e0, delivered gen+manifest) = f03efb7069fa533e ; in store: False
  fingerprint(rev3 814e395a, delivered gen+manifest) = de4720325eb70003 ; in store: False
  fingerprint(rev4 90ea0ff3, delivered gen+manifest) = 6ec6fc2a42343433 ; in store: False
  custody record names harness/generator/manifest: True | attempt_number: 7 (revision 5) | harness ATTEMPT_NUMBER: 7
  harness writes the custody file? open(CUSTODY_PATH, 'w'...): False | reads it: True

== [4] manifest regenerated from the delivered generator with the harness's own writer (csv, LF, ascii)
  regenerated sha256 = c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 | delivered = c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8
  harness writer form present (csv.writer lineterminator LF): True

== [5] results structure, canonical document recomputed from the delivered RUN1 content
  evaluations: 34 | any 'sexes' key: False | keys (SCEN-A): ['c4_source', 'criteria', 'disc_f3_03_complement', 'dp04', 'fits', 'fixture_id', 'interpretation', 'invalid_counts_by_criterion', 'k05_result', 'mechanism_outcome', 'p03', 'p03_fields', 'probe_failure_shares']
  SCEN-A fits F0 keys: ['P01', 'P02', 'SPL'] ...
  one fits entry: {'L': 'str', 'failure_codes': 'list', 'feature_start_rejected': 'bool', 'start_bank_size': 'int', 'theta': 'list', 'valid': 'bool'}
  sha256(json.dumps({evals, stops, pins{mask_full:True, fs:True}}, sort_keys)) = 777fca02e1f514038e04cb3b5aac5365fa4dd851b03174820ef4692f8c73c2d8
  == results.run1_canonical_sha256: True | run1 == run2 (executor): True 777fca02e1f514038e04cb3b5aac5365fa4dd851b03174820ef4692f8c73c2d8

== [6] T-EXPECT-ALL re-done by the auditor from the manifest's expected_* columns
  declared: 33 | auditor mismatches: none | results.expectation_checks: {'EXPECTATION_FAIL': 'none', 'declared': 33, 'ran': 33}

== [7] the four D-5-pinned S-R2-1 fixtures, as delivered
  SCEN-B         p03=('FAIL', 'FAIL') mech=STOP_BOTH_FAIL_REDESIGN level=None path=None U={} stops=['BOTH_FAIL_REDESIGN']
     C4b (share hex, n_valid, passed, undefined): {'P01:F': ('0x1.0000000000000p+0', 1, True, False), 'P01:M': ('0x0.0p+0', 0, False, True), 'P02:F': ('0x1.0000000000000p+0', 1, True, False), 'P02:M': ('0x0.0p+0', 0, False, True)}
  INJ-C1-FAIL    p03=('FAIL', 'PASS') mech=ONLY_P02_PASSES level=None path=None U={} stops=[]
     C4b (share hex, n_valid, passed, undefined): {'P01:F': ('0x1.6666666666666p-1', 7, False, False), 'P01:M': ('0x1.0000000000000p+0', 10, True, False), 'P02:F': ('0x1.0000000000000p+0', 10, True, False), 'P02:M': ('0x1.0000000000000p+0', 10, True, False)}
  INJ-DP04-C1    p03=('PASS', 'PASS') mech=RESOLVED_MECHANISM_P01 level=C1 path=['C1'] U={} stops=[]
     C4b (share hex, n_valid, passed, undefined): {'P01:F': ('0x1.0000000000000p+0', 10, True, False), 'P01:M': ('0x1.0000000000000p+0', 10, True, False), 'P02:F': ('0x1.ccccccccccccdp-1', 9, True, False), 'P02:M': ('0x1.ccccccccccccdp-1', 9, True, False)}
  INJ-C4B-NOREF  p03=('PASS', 'PASS') mech=TERMINAL_FALLBACK_MECHANISM_P01 level=None path=['C1', 'C2', 'C3', 'C4a', 'C4b', 'C5', 'C6'] U={'C2': {'F': 10, 'M': 10}, 'C3': {'F': 8, 'M': 8}, 'C4b': {'F': 8, 'M': 8}, 'C5': {'F': 10, 'M': 10}} stops=[]
     C4b (share hex, n_valid, passed, undefined): {'P01:F': ('0x1.ccccccccccccdp-1', 9, True, False), 'P01:M': ('0x1.ccccccccccccdp-1', 9, True, False), 'P02:F': ('0x1.ccccccccccccdp-1', 9, True, False), 'P02:M': ('0x1.ccccccccccccdp-1', 9, True, False)}
  any STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-03) anywhere in evaluations: False
  exactness_findings: [] | closed: [{'id': 'F3-STEP2-EXACT-03', 'source': 'p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md', 'source_sha256': '0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851'}]

== [8] telemetry: per-call (all phases, pids) and mode-level (L, predicates, RUN2 rows, FIX-STARTS rows)
  per-call rows: 12174 | by (phase,pid): {('nr_gates', '31388'): 60, ('unit_tests', '31388'): 1602, ('run1', '31388'): 3956, ('run1', '29564'): 1300, ('run2', '29564'): 5256} | == results.process: True
  run1 == run2 row counts: True
  mode-level rows: 12298 | columns: ['fixture', 'fitter', 'mask_id', 'fixture_id', 'family', 'start_id', 'optimizer_path', 'status', 'message', 'success', 'nit', 'nfev', 'njev', 'wall_clock_seconds', 'L', 'predicates']
  rows by mask prefix: {'run1': 4645, 'run2': 4645, 'exc': 876, 'a5true': 616, 'full': 994, 'dup': 522} | by fixture: {'SCEN-A': 4928, 'SCEN-B': 4362, 'INJ-EXC-CAPTURE-S1': 292, 'INJ-EXC-CAPTURE-S2': 292, 'INJ-EXC-UNRELATED-TYPE': 292, 'FIX-A5-TRUE': 616, 'FIX-STARTS-FULL': 994, 'FIX-STARTS-DUP': 522}
  L empty by fitter: {('P-01', False): 1012, ('P-02', False): 1062, ('SPL', True): 10224}
  L empty count: 10224 | rows with non-empty predicates: 501 | distinct predicates: ['', "['MORPHOLOGY_INADMISSIBLE', 'OPTIMIZER_NONCONVERGENCE']", "['MORPHOLOGY_INADMISSIBLE']", "['NONFINITE_PARAMETER', 'OTHER_PREDECLARED_NUMERICAL_FAILURE']", "['OPTIMIZER_NONCONVERGENCE']", "['ZERO_VARIANCE_FIT']", '[]']

== [9] residual series (Y-21)
  keys: 11 == link: True | sha==link==acf and phi bitwise: 11 / 11 | file == r3 export 3ee624f3…: True

== [10] register VERBATIM blocks vs sources (byte-substring)
  block 1 (2769 chars): in D-5=True in D-2=False in freeze record=False
  block 2 (193 chars): in D-5=False in D-2=True in freeze record=False
  block 3 (228 chars): in D-5=False in D-2=False in freeze record=True
  results.double_count_declaration substring of freeze record (whitespace-normalized): True
  coverage K-05 row title in D-2 (whitespace-normalized): True

== [11] tests and end state
  mandatory list (harness): 27 | results.tests_run: 27 all passed: True
  end_state: {"F3_STEP2_r4_status": "PARTIAL_PENDING_PI", "PI_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851", "corrections_complete": true, "deferred_decisions": [], "mandatory_tests_all_run": true, "mandatory_tests_missing": [], "narrowed_evidence": ["T-R2-2"], "open_findings": [], "uncovered_coverage_rows": ["C2 pass", "C3 pass", "A.5 (iii) inadmissible refit", "D-P04 comparator never RESOLVED/EQUIVALENT on NaN", "clean execution / process provenance disclosed"]}
  coverage rows: 61 | downgraded: ['C2 pass', 'C3 pass', 'D-P04 comparator never RESOLVED/EQUIVALENT on NaN', 'clean execution / process provenance disclosed']
    UNCOVERED: C2 pass | UNCOVERED(evidence not established in this run: 0 evidence tokens)
    UNCOVERED: C3 pass | UNCOVERED(evidence not established in this run: 0 evidence tokens)
    UNCOVERED: A.5 (iii) inadmissible refit | UNCOVERED(no construction possible without touching frozen code)
    UNCOVERED: D-P04 comparator never RESOLVED/EQUIVALENT on NaN | UNCOVERED(evidence not established in this run: 0 evidence tokens)
    UNCOVERED: clean execution / process provenance disclosed | UNCOVERED(evidence not established in this run: 0 evidence tokens)

== [12] code facts (line numbers of the delivered harness)
  _s_r2_1_present called from code (excluding its def): []
  V4 in evaluate_fixture includes full flags: [1331] | probes_idx includes full: [1204]
  guarded comparator STOP label: ['stop="CONTRACT_VIOLATION_EMPTY_U",', 'stops.append(dict(fixture=fx_id, stop="CONTRACT_VIOLATION_EMPTY_U",'] at [1638, 1669]
  spline_nonregression passed literal: [3278] | NR-SPL record_test: [2615]
  docstring mentions ATTEMPT 4 live: []
  report: deliverable 11 line: ["| 11 | r3 start-state stands (r4 opened from the audited r3 end state; no separate r4 inventory beyond the attempt log's revision blocks) | n/a -- disclosed |"]
  report 64-hex values: 18
```

Script `r4_02_decision_layer_repro.py` (run from the auditor workspace that mirrors the repository path):

```python
"""Evidence script 02 (F3 STEP-2 r4 independent audit, 2026-09-28). [A-S] auditor-environment reproduction of the
platform-independent parts: imports the UNMODIFIED r4 harness (54274b4e...) and generator (39391730...) and calls
(a) evaluate_fixture on the 32 decision-layer fixtures in manifest order, twice (RUN1-like, RUN2-like, same process),
(b) the pure unit tests t_a5_support, t_comparator_nan, ut_uset_construction, and compares with the delivered
results / test evidence. main() is NOT called; no real fit is run; no executor path is written."""
import importlib.util, sys, json, hashlib, copy, warnings
warnings.filterwarnings("ignore")
HP = "G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_r4_2026-09-24.py"
spec = importlib.util.spec_from_file_location("h_r4", HP); h = importlib.util.module_from_spec(spec); sys.modules["h_r4"] = h; spec.loader.exec_module(h)
sys.path.insert(0, "p_konum_plus/calibration")
gs = importlib.util.spec_from_file_location(h.GEN_MODULE_NAME, h.GEN_PATH); gen = importlib.util.module_from_spec(gs); sys.modules[h.GEN_MODULE_NAME] = gen; gs.loader.exec_module(gen)
print("harness sha256:", hashlib.sha256(open(h.__file__, "rb").read()).hexdigest())
print("generator sha256:", hashlib.sha256(open(h.GEN_PATH, "rb").read()).hexdigest())
R = json.load(open("/home/claude/audit_r4/recv/f3_step2_results_r4_2026-09-24.json"))
TE = json.load(open("/home/claude/audit_r4/recv/f3_step2_test_evidence_r4_2026-09-24.json"))
ER = {e["fixture_id"]: e for e in R["evaluations"]}
def one_pass():
    stops, evals = [], []
    for fx in gen.INJ_FIXTURES:
        evals.append(h.canon(h.evaluate_fixture(fx["fixture_id"], fx["strata"], gen.N_INJ, "TEST_ONLY_INJECTION_DECISION_LAYER",
                                                fx["flags"], stops, force_c4_pending=fx["fixture_id"] in gen.FORCE_C4_PENDING_FIXTURE_IDS)))
    return evals, h.canon(stops)
snap = json.dumps([fx["strata"] for fx in gen.INJ_FIXTURES], sort_keys=True, default=str)
e1, s1 = one_pass()
leak = json.dumps([fx["strata"] for fx in gen.INJ_FIXTURES], sort_keys=True, default=str) != snap
e2, s2 = one_pass()
J = lambda o: json.dumps(o, sort_keys=True)
print("decision-layer fixtures:", len(e1), "| pass1 == pass2 (same process):", J(e1) == J(e2) and J(s1) == J(s2), "| fixture data changed by pass 1:", leak)
same = [e["fixture_id"] for e in e1 if J(e) == J(ER[e["fixture_id"]])]
print("identical to the executor's evaluation objects:", len(same), "/", len(e1), "| differing:", [e["fixture_id"] for e in e1 if e["fixture_id"] not in same])
exp_stops = [s for s in R["stops"] if s["fixture"].startswith("INJ-")]
print("INJ stops identical to the executor's:", J(s1) == J(exp_stops), [(s["fixture"], s["stop"]) for s in s1])
for fid in ("INJ-C1-FAIL", "INJ-DP04-C1", "INJ-C4B-NOREF", "INJ-U-POST-CONSTRUCTION-INVALID"):
    e = [x for x in e1 if x["fixture_id"] == fid][0]
    print("  %-32s p03=%s mech=%s" % (fid, (e["p03"]["P01"], e["p03"]["P02"]), e["mechanism_outcome"]))
post = [s for s in s1 if s["fixture"] == "INJ-U-POST-CONSTRUCTION-INVALID"]
print("  INCONSISTENT_U stop record:", post)
ta = h.t_a5_support(); tc = h.t_comparator_nan(); uu = h.ut_uset_construction(gen)
print("t_a5_support equal to delivered:", J(h.canon(ta)) == J(TE["t_a5_support"]), "| pass:", ta.get("pass_"))
print("t_comparator_nan equal to delivered:", J(h.canon(tc)) == J(TE["comparator_nan"]), "| pass:", tc.get("pass_"))
print("ut_uset_construction equal to delivered:", J(h.canon(uu)) == J(TE["uset_construction"]), "| cases ok:", {k: v.get("ok") for k, v in uu.items()})
print("guard:", {repr(v): h._guarded_scalar_ok(v) for v in (0.5, float("nan"), float("inf"), None)})
```

Script `r4_03_line_facts.py`:

```python
"""Evidence script 03 (r4 audit, 2026-09-28): prints the delivered harness lines the findings cite, verbatim."""
L = open("/home/claude/audit_r4/recv/f3_step2_adequacy_harness_r4_2026-09-24.py", encoding="utf-8").read().split("\n")
for a, b in ((1029, 1038), (1815, 1815), (1829, 1839), (1843, 1848), (1455, 1466), (1580, 1597), (1663, 1669), (2186, 2196), (3278, 3278)):
    for i in range(a, b + 1): print("%5d: %s" % (i, L[i - 1]))
    print("  ...")
```
