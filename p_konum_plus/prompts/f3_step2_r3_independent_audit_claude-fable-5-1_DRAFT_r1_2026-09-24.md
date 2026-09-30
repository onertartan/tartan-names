# p_konum_plus — F3 STEP-2 r3 — Independent Audit — DRAFT r1 (2026-09-24)

```text
record                 = f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md
record_class           = independent audit of the STEP-2 r3 package (second delivery, 15 files received on
                         2026-09-24); child of the auditor preflight of 2026-09-23 (c893c5de…), which it supersedes
auditor                = claude-fable-5-1 (Claude, Cowork session; configured model identifier — the serving model
                         may differ). Not the executor. Decides nothing for the PI. Declares no QUALIFIED
reviewer_prior_exposure = true — this session drafted the r3 prompt (DRAFT v1 → v2), the dispatch-record template,
                         filled D-4 at the PI's written instruction, wrote the audit records of the r2 package
                         (DRAFT r1 … r5) and the preflight whose observations P-1 … P-7 the executor answered
other auditors' records = none received; none used
executor                = Claude Code (harness 5fea165c… ; generator cc23c9b5… ; manifest 9c944543…)
dispatched instruments = DRAFT v2 5b0e19ea… (D-3) ; D-4 4e623536… ; content da0c4064… (D-2) ; v6 17187d31… (D-1)
frozen upstream        = untouched by this record: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (r4 5e594136… as ratified
                         by freeze record r1 7055f186…). Nothing is reopened; no scientific literal is produced
evidence tiers         = [A] auditor-verified on the delivered bytes ; [A-S] auditor-environment reproduction
                         (Linux; Python 3.11.15, numpy 1.26.4, scipy 1.14.1 — the executor's numpy and scipy
                         versions, Python 3.11.7 and Windows there; never a claim of reproducing an executor
                         hash) ; [X] executor claim ; [E] external. An [A-S] result never counts as verification
                         of an executor hash
honesty rule           = every hash in this record was computed by the auditor with the commands shown in §10, or
                         is quoted from a named file; a check the auditor could not run is NOT PERFORMED
sidecar                = external .sha256 ; no self-hash ; the preflight and the r2 audit records are not rewritten
```

## 0. Verdict

```text
audit_verdict                 = NOT PASSED
global blockers               = 0
gate-specific blockers        = 6   (R3A-01 … R3A-06)
cleanup                       = 6   (R3A-07 … R3A-12)
informational                 = 5   (R3A-13 … R3A-17)
F3_STEP2_r3_status (executor) = PARTIAL_PENDING_PI — supported as the status; the field corrections_complete = true
                                that the executor reports is NOT supported (§9)
F3_STEP2 = QUALIFIED          = NOT declared (PI only)
S-R2-1                        = DEFERRED_THIS_CYCLE as dispatched; F3-STEP2-EXACT-03 open; wired as §5 of the
                                prompt prescribes [A]
```

In plain words. The r3 package is auditable, and its provenance is now established: the delivered harness,
generator and manifest are the bytes that computed every unit of the final output (the restart-store key prefix
equals the fingerprint the auditor recomputes from the delivered files, §2). The corrections that carry the
scientific weight of this cycle hold on the delivered evidence: the residual series are RUN1's own (Y-21), the
P03 handling of an invalid statistic is the one the prompt prescribes (Y-03 (i)), the consulted sets are built by
membership first (Y-02 (a)), the S-R2-1 deferral is wired everywhere it applies, and all 33 declared fixture
expectations hold when the auditor re-checks them from the manifest (§3). What keeps the verdict at NOT PASSED is
that several corrections are reported as applied but are not in the delivered code or files: the register of this
cycle does not exist; the canonical document is not enlarged (Y-07); an unrelated solver exception is still
converted or crashes the process (Y-04 (b)); the post-construction guard still fires from the test flag, not from
the data (Y-03 (ii)); the A.5 support predicate has no unit test and a contract violation becomes a C4a failure
(Y-05); and the per-call telemetry and counters cover the two runs but not the gates and unit tests that the final
process read from the store (Y-01). None of these changes the mechanism outcome of any fixture in this package:
the auditor's own run of the delivered code in one clean process reproduces every decision-layer object, every
stop and all 33 expectations, with RUN1 == RUN2 in that process (§7). The attempt log names the wrong hash for the
final harness, and the store still holds 11,723 entries of an unidentified code version; both are disclosure
defects, not provenance failures.

## 1. Custody at reception [A] — the 15 files received on 2026-09-24

| received as | canonical name (deliverable) | bytes | SHA256 |
|---|---|---|---|
| 90f1b34d-… | f3_step2_adequacy_harness_r3_2026-09-22.py (1) | 129,023 | 5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77 |
| f6a6b931-… | f3_step2_fixture_generator_r3_2026-09-22.py (2) | 46,877 | cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8 |
| 83f108b8-… | f3_step2_fixture_manifest_r3_2026-09-22.csv (3) | 19,623 | 9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a |
| 0650b2af-… | f3_step2_r3_preexecution_custody_2026-09-22.md (4) | 1,938 | a910e1b65f47d197387b1add29894cafc3267a7422ab22b9fd2bf99632f4e0c0 |
| 97f99f37-… | f3_step2_telemetry_r3_2026-09-22.csv (5) | 2,218,399 | 24f21811886c9aab3e2e57f649b0fa3d6964f729ae6978569f926fe32737d0d7 |
| c67f0d5f-… | f3_step2_results_r3_2026-09-22.json (6) | 1,599,379 | 352791648b7c3dc1151962905ec2270fe3ae4246846f2021c2dcda3e3dfe18fb |
| 72aa98b1-… | f3_step2_residual_series_r3_2026-09-22.json (7) | 42,820 | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 239a8492-… | f3_step2_test_evidence_r3_2026-09-22.json (8) | 24,166 | b7d3b861be33f6271d372dbe13a38826d2946c3acf97c227533dddad09edb03b |
| 3307d61a-… | f3_step2_spline_percall_telemetry_r3_2026-09-22.csv (added by the executor) | 1,775,410 | 9d0c627ebc5949e4b8e61c48e453d16c28ba61733047d737fcf3f8d2cb5a30fe |
| 5825632a-… | f3_step2_correction_report_r3_2026-09-24.md (10) | 12,535 | 80df7914940f0cdbdfd327d8d133fa556ad9ab024c1b218a4dd39eac09a8dfae |
| a8b33d4b-… | f3_step2_r3_start_state_inventory_2026-09-22.md (11) | 33,320 | 71a3f5a7cf98c3b122cb63eac36d2db1a6f8b20503fc05d0eeb7c6caafbed089 |
| e065f255-… | f3_step2_r3_attempt_log_2026-09-22.md (12) | 7,072 | 253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5 |
| aa0941a1-… | f3_step2_r3_restart_store_manifest_2026-09-22.csv (§8.3 store manifest) | 3,398,062 | 933dcaeeb979ae2872d91597c6c9c1ba8484266a4b3ac84e562e25248e6d39e9 |
| 4de86acf-… | f3_step2_r3_pi_dispatch_record_2026-09-22.md (repository copy of D-4) | 6,848 | 4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865 |
| 880ad739-… | f3_step2_r3_auditor_transmittal_note_2026-09-22.md (non-normative) | 7,198 | bbe898cc89086ff179349f2925a670301b87dd2dad31afd141de13e771aa4a33 |

No file contains a CR byte. The repository copy of D-4 is byte-equal to the record the auditor filled at the PI's
instruction (4e623536…). The transmittal note is byte-equal to the copy received on 2026-09-23. Not received:
deliverable 9 (the register r3 — the report says it was not authored, §4 R3A-01), the sidecars of items 1–12 (§9
item 14; none received, so sidecar agreement and the absence of a self-hash are NOT PERFORMED, R3A-13), and the
five quarantine notes the report names. The seven files of the first delivery (2026-09-23) are superseded by the
files above; their hashes stand in the preflight (c893c5de…).

## 2. Which bytes ran [A]

The harness computes a code-and-environment fingerprint at start (lines 2166–2171: SHA256 over the harness,
generator and manifest hashes, the two frozen engine hashes, the interpreter, numpy and scipy versions, the
platform string and the three thread pins; first 16 hex) and prefixes every restart-store key with it (line 158).
The auditor recomputed the formula (§10, block [2]):

```text
delivered triple (5fea165c…, cc23c9b5…, 9c944543…) with the executor's environment  →  1ba561daefb48b2e
   = the custody record's code_env_fingerprint
   = the prefix of 11,723 of the 23,446 store entries, among them realscen_run1/run2 SCEN-A/SCEN-B, nrgates_all,
     unittests_all, 2,081 onestart_* and 9,636 splmode_* units
the attempt log's revision-5 hash 99f895c1… with the delivered generator and manifest        →  327fcf82f949fc66
     (in no store entry)
revision-4 f882b922… with the delivered generator and manifest                              →  e3ccc7d133c9ff2f
     (in no store entry)
control: the first delivery's triple (d67e097d…, e35c2bf0…, 4544ff75…)                     →  6f4e29ccc903bce6
     = the fingerprint that custody record printed
```

Therefore every unit of the final output was computed by processes running exactly the delivered harness,
generator and manifest, in the environment the results JSON records. The final process (pid 1240, 2026-09-24
14:27:44 → 14:51:59) computed RUN2 in full and RUN1 in part: of the 5,256 RUN1 optimizer calls in the per-call
telemetry, 2,659 carry pid 10920 (attempt-log row 9, interrupted at SCEN-A:M0:probeR) and 2,597 carry pid 1240; the
non-regression gates and the unit tests were read from the store as coarse units (process block). The second
store prefix, 548ae790f6ac756a (11,723 entries of the same five kinds), corresponds to no combination of the
harness, generator and manifest hashes named in any delivered file; nothing under it can be read by the delivered
harness (prefix mismatch by construction), but §8.3 required it to be quarantined (R3A-07). The attempt log's
statement that rows 9–10 ran under 99f895c1… is contradicted by the custody record, the harness constant
SUPERSEDES_HARNESS_SHA256 (line 112) and the fingerprint: 99f895c1… is the superseded revision, 5fea165c… the
executed one (R3A-07).

## 3. Checklist

Executor claim and auditor result in separate columns. Tiers as in the header.

| # | check | executor claim | auditor result |
|---|---|---|---|
| C-01 | custody: 15 files hashed; D-4 copy = dispatched D-4; manifest hash = custody = results | — | PASS [A] |
| C-02 | delivered harness / generator / manifest = the bytes that produced the results (fingerprint) | implied | PASS [A] (§2) |
| C-03 | manifest regenerated from the delivered generator with the harness's own writer (csv, LF, ascii) | 9c944543… | PASS [A]: byte-identical, 9c944543… (§7) |
| C-04 | traceback line numbers of the natural COVERED capture against the delivered harness (509 wrapped_accept, 609 / 628 / 609 wrapped_nnls) | — | PASS [A]: every frame is the line it names |
| C-05 | residual series: 11 keys = link keys; float64-LE hash = link value = acf value; PIN-ACF recomputed with an independent index-order implementation | 11 series | PASS [A] 11 / 11 ; phi bitwise 11 / 11 |
| C-06 | exported keys = the RUN1 full-data fits that completed (telemetry); SCEN-B:M0:SPL absent (injected failure) | — | PASS [A] |
| C-07 | 9 of 11 exported phi equal the RUN1 sex-level C3 statistic bitwise; the two SCEN-B:M0 family keys have no sex-level counterpart (V3 empty in M) | — | PASS [A] |
| C-08 | T-EXPECT-ALL re-done by the auditor from the manifest's expected_* columns against the results | 33 / 33, none | PASS [A]: 33 declared, 0 mismatches |
| C-09 | INJ-NAN-STAT-SPL: C2 undefined = True for both families, both sexes (preflight P-5) | fixed | PASS [A] |
| C-10 | INJ-EXC-CAPTURE-S2: records at stages 1 and 2 (preflight P-4) | [1, 2] | PASS [A] on the delivered evidence; the records themselves are not delivered (R3A-03) |
| C-11 | loader: node-hash entries 73 = executed nodes 73, unique keys (Y-13) | 73 / 73 | PASS [A] |
| C-12 | per-call telemetry: 10,512 rows; run1 5,256 = run2 5,256; numeric nit on every row; pid and phase tags | balanced | PASS [A] for run1 / run2 ; FAIL for the phases nr_gates and unit_tests (0 rows, no counter) — R3A-06 |
| C-13 | process block: units read from the store carry the pids of their computing processes | nr_gates 1, unit_tests 1 read | FAIL: no pid per unit; the per-fit reads inside RUN1 (2,659 calls from pid 10920) are not counted — R3A-06 |
| C-14 | attempt log: every process with pid, start, end, the three W-3 hashes, how it ended | 10 rows | PARTIAL: harness hashes only; row 9–10 hash wrong — R3A-07 |
| C-15 | §8.3 store: emptied when the harness changed; manifest with path, size, SHA256 | reset at revision 4 | FAIL: 11,723 entries of an unidentified version remain — R3A-07 |
| C-16 | W-3 custody record written before the run, naming the executed bytes | ALL PASS | PARTIAL: the record is rewritten by every launch (lines 2173–2205); "ALL PASS" is a literal (2182); the D-4 hash is a constant (248) — R3A-07 |
| C-17 | P-4 evidence: the report names D-4 (path, hash) (Y-09) | done | PASS [A] |
| C-18 | Y-21: series from RUN1's own fit objects; no fit in the export; hash link | fixed | PASS [A] (code 2385–2404; C-05 … C-07; export calls 0 in the auditor run) |
| C-19 | Y-03 (i): P03 valid sets by flags; an invalid member ⇒ undefined = True, no comparison; C4b both sides validated; C3 per CL-F3-04 | applied | PASS [A] (code 1148–1253; fixtures INJ-NAN-STAT, -C4B, -C5, -SPL) |
| C-20 | Y-03 (ii): INCONSISTENT_U from a data-driven re-validation | applied | FAIL: from the test flag alone (1392–1395) — R3A-04 |
| C-21 | Y-03 (iii): comparator returns INCONSISTENT_U on a NaN scalar | T-COMPARATOR-NAN pass | FAIL: no guard (1434–1435); the test documents the hazard and passes by literal (1768) — R3A-04 |
| C-22 | Y-02 (a): U2 / U3 / U4 / U5 by frozen membership and finiteness; INJ-DP04-C2-DIVERGE \|U2\| = 8, RESOLVED P-01 | applied | PASS [A] (code 1367–1389; results) |
| C-23 | Y-02 (b): construction exposed as pure functions and tested directly | UT-USET ok | FAIL: the unit test re-types the rule (1726–1750) — R3A-10 |
| C-24 | Y-04 (a) / (c): call site and stage from the traceback; arming rule; S1 / S2 fire once per stage | applied | PASS [A] (469–488, 583–610, 1783–1805) |
| C-25 | Y-04 (b): UNRELATED exception captured, not converted, routed to an exactness finding, context STOPs, others continue | UNRELATED_TYPE pass | FAIL: RuntimeError ⇒ mode invalid without record or finding (923–930); other classes propagate uncaught (1811–1816) — R3A-03 |
| C-26 | Y-04 (d): wrappers installed for their scope and restored afterwards | T-WRAPPER-RESTORE true | PARTIAL: restored only at the end; three nnls wrappers stacked from the unit phase through RUN1 / RUN2 (1809, 1819; traceback) — R3A-03 |
| C-27 | Y-04: TEST_ONLY capture records delivered; RUN1 and RUN2 capture records identical | — | FAIL: unit-phase records discarded (2355); RUN2 records neither kept nor compared (2599) — R3A-03 |
| C-28 | Y-05: T-A5-SUPPORT unit test; violation ⇒ STOP record, PENDING, never a C4 pass / fail; FIX-A5-TRUE | UT_A5 pass, FIX-A5-TRUE pass | PARTIAL: FIX-A5-TRUE PASS [A]; T-A5-SUPPORT absent; a violation makes the probe a C4a failure (1548) — R3A-05 |
| C-29 | Y-06: fidelity over declared injection sites, execution-site keys | 5 / 5 | PASS [X] ; [A-S] in §7 |
| C-30 | Y-07: X-11 (a) … (f) — per-call rows; family rows with L and failure codes; §6 fields; enlarged canonical document; `sexes`; schema assertion; FIX-STARTS rows | applied | FAIL except (a) for run1 / run2 — R3A-02 |
| C-31 | Y-08: the six status fields computed from the run | computed | PARTIAL: mandatory_tests_all_run is a literal (2621); corrections_complete = (no expectation failure) (2620) — R3A-11 |
| C-32 | Y-10 / Y-13 (register row) / Y-14 / Y-19 | N/A, unchanged | FAIL: no r3 register exists — R3A-01 |
| C-33 | Y-11: K-05 coverage row in the wording of content §6 | unchanged | FAIL: still "C4b completeness fail with C4a pass impossible (K-05)" — R3A-08 |
| C-34 | Y-12: opened-file list unfiltered and classified in the report | — | PARTIAL: unfiltered list present in the results (9,550 entries: 9,276 restart-store files, 259 interpreter / site-packages files, 9 project files, 6 other paths incl. `nul` and a descriptor number); no classification in the report — R3A-12 |
| C-35 | Y-15: T-MASK-FULL-EXT ran and passed | pass | PASS [X] ; [A-S] §7 |
| C-36 | Y-16: coverage statuses derived from the run; one vocabulary; no pre-run constant | derived | FAIL: coverage = generator constant (2612); "C4b pass/fail (real)" covered with half PENDING — R3A-08 |
| C-37 | Y-17: STOP returns of the consulted-level code write a `stops` record | verified | FAIL in code: the return at 1429–1433 writes none — R3A-09 |
| C-38 | Y-18 / §9 items 13–15: report complete; r2 attempt history with sources; parents re-hashed with values | §§2–5 | FAIL: see R3A-12 |
| C-39 | end state: PARTIAL_PENDING_PI by v6 §13 | PARTIAL_PENDING_PI | PASS as status; corrections_complete = true not supported (§9) |
| C-40 | frozen upstream and parents untouched; no real data; no 6B; no QUALIFIED wording; no new scientific literal | asserted | PASS on the delivered files [A] (strings); the parent re-hash values are not delivered — NOT PERFORMED |
| C-41 | S-R2-1 = DEFERRED_THIS_CYCLE wired: C4b STOP_EXACTNESS_PENDING(EXACT-03) wherever the state occurs; INJ-DP04-C1, INJ-C4B-NOREF, INJ-C1-FAIL, SCEN-B outcomes as §7 of the prompt predeclares | applied | PASS [A] (code 1201–1211; results) |
| C-42 | decision-layer evaluations re-computed with the delivered harness and generator in the auditor environment | — | PASS [A-S]: 32 / 32 INJ objects identical; SCEN-A / SCEN-B outcomes, p03 fields, stops, construction audit, 33 / 33 expectations identical (§7) |
| C-43 | RUN1 == RUN2 in one auditor process; calls per phase incl. nr_gates and unit_tests; export calls 0; wrapper depth | — | [A-S]: RUN1 == RUN2 (a6310a06…); calls nr_gates 60, unit_tests 941, run1 5,244, run2 5,244; export calls 0; nnls wrapper depth 3; restore True (§7) |
| C-44 | NR-01 (i) 6f197b74… ; NR-SPL 30 rows repr-exact | PASS | [X]; auditor environment: native f07fdc82… ≠ 6f197b74…, hybrid = native (T-2a adapter), NR-SPL repr-exact false — cross-platform, as in the r2 audit; no claim either way |

## 4. Findings

Classification: global blocker / gate-specific blocker / cleanup / informational. Authority: S = PI scientific,
T = PI task-scope, X = executor correction.

| id | classification | finding | gate effect | closure action | authority |
|---|---|---|---|---|---|
| R3A-01 | gate-specific blocker | Deliverable 9, the CLASS_C pin register r3, does not exist (report §7: "register not re-authored this cycle"). Y-10, Y-13 (row PIN-EXC-CAPTURE), Y-14, Y-19 and the register evidence named by Y-02, Y-03, Y-04, Y-05 have no object | the corrections whose evidence is a register row are not evidenced; the TEST_ONLY branches of the evaluator (`force_c4_pending`, the post-construction hook) and the restart layer are not disclosed in any register | author the r3 register as a child of R-09 with the rows v6 §11 and Y-10 … Y-19 name; VERBATIM rows byte-substrings of D-2 / D-4; SUMMARY rows for the engineering of Y-04 | X |
| R3A-02 | gate-specific blocker | Y-07 (v6 X-11) not closed: the canonical document is the r2-shaped one — no per-fit endpoint / masked L / start-bank size / FEATURE_START_REJECTED, no per-spline-fit winner mode, RSS, equivalent-mode set, per-mode validity (X-11 (d)); `sexes` = {} in 34 / 34 evaluations (e); family telemetry rows carry no L and no failure codes (b); the §6 fields of (c) beyond the DISC-F3-03 complements are absent; T-SCHEMA and T-CANON do not exist (f); FIX-STARTS-* write no rows (2267–2268); RUN2 mode rows absent. Per-call rows (a) exist for run1 / run2 only | RUN1 == RUN2 is evidenced over the un-enlarged document; the reporting fields of the frozen §6 remain unavailable | implement X-11 (b) … (f) as written; write FIX-STARTS-* rows; T-CANON over the enlarged document; T-SCHEMA as a machine assertion | X |
| R3A-03 | gate-specific blocker | Y-04 (b) / (d) not closed: an UNRELATED RuntimeError inside the solver becomes an invalid mode with no capture record and no exactness finding (fit_spline 923–930; the string ACCEPTANCE_UNVERIFIABLE_UNRELATED is consumed nowhere); a non-RuntimeError propagates uncaught (the process would end — INJ-EXC-UNRELATED-TYPE passes by "propagated_uncaught", 1811–1816); the TEST_ONLY capture records of S1 / S2 are discarded before RUN1 (2355) and the landing modes are not delivered; RUN2 capture records are neither kept nor compared with RUN1's (2599); three nnls wrappers are stacked from the unit phase onward (1809, 1819) and restored only at the very end; the injection contexts run once although the manifest says run_scope both | content §3.1's last sentence ("retain the existing error/exactness protocol") is not implemented for UNRELATED events; a natural UNRELATED event would alter a fit outcome silently or end the run; the S1 / S2 evidence is counts only | route an UNRELATED event to STOP_EXACTNESS_PENDING(<id>) for its context with a capture record (kind UNRELATED, TEST_ONLY where injected); catch every exception class at mode level for that purpose only; deliver every capture record; compare RUN1 / RUN2 records; install / uninstall per scope | X |
| R3A-04 | gate-specific blocker | Y-03 (ii) / (iii) not closed (r2 finding R2A-03 (b) unchanged): CONTRACT_VIOLATION_INCONSISTENT_U is raised when the test flag's index is a member of U (1392–1395) — the members' statistics are never re-read; the comparator has no NaN guard (1434–1435) and T-COMPARATOR-NAN passes by literal (1768) while stating that the hazard exists; the offending (fitter, observation) pairs of rule (i) are not recorded. Rule (i) itself is closed (C-19) | the post-construction guard guards nothing; INJ-U-POST-CONSTRUCTION-INVALID evidences the flag path only | re-validate every member from the data after construction; guard the comparator; make T-COMPARATOR-NAN call the guarded comparator; record the offending pairs | X |
| R3A-05 | gate-specific blocker | Y-05 not closed (r2 finding R2A-05 in part): T-A5-SUPPORT (threshold equality included, next float below excluded, disconnected components united, partly observed versus fully masked, constant reference ⇒ S = G, invalid references ⇒ violations) does not exist; a CONTRACT_VIOLATION_A5_REFERENCE makes the probe a C4a failure (`p_c4a = probe_raw and (a5_i is False)`, 1548) instead of the PENDING status content §2.3 prescribes. FIX-A5-TRUE and the violation record are in place | the A.5 (i) predicate is untested at unit level; a violation would be converted into a C4 outcome | write T-A5-SUPPORT; wire the violation as STOP_EXACTNESS_PENDING / PENDING for C4a and C4b of that sex | X |
| R3A-06 | gate-specific blocker | Y-01 (T-CALLCOUNT, T-RESTART-PROVENANCE) evidenced for run1 / run2 only: the coarse store units nrgates_all and unittests_all carry no per-call snapshot, so the final process — which read both — reports no rows and no counter for the phases nr_gates and unit_tests; the process block counts fixture-level units only, while 2,659 of the 5,256 RUN1 calls were read from per-fit units computed by pid 10920; the store manifest has no pid / start column; "the units read from the store, with their pids" (§8.3) is not reported | the optimizer-call evidence of NR-SPL and of the unit tests is absent from the package; the counters do not represent the total execution | replay the per-call snapshot for every unit kind; count per-fit reads; report per phase and per pid; add pid / start_iso to the store manifest | X |
| R3A-07 | cleanup | Attempt log and custody record: rows 9–10 name 99f895c1… as the final harness — the custody record, the harness (line 112) and the fingerprint show 5fea165c… executed and 99f895c1… superseded; the log records harness hashes only, not the three W-3 hashes per attempt (§8.2); 11,723 store entries under an unidentified prefix were not quarantined when the harness changed (§8.3); the W-3 record is rewritten by every launch (2173–2205) so its declaration "No W-4 process has yet been started under these three hashes" is false for a resumed launch; "dispatch_preconditions_P1_P4 = ALL PASS" is a literal (2182) and dispatch_record_sha256 a constant (248); docstring line 24 says "ATTEMPT 4 (this file, live), harness revision 4" | disclosure only; provenance is established by §2 | correct the log; record the three hashes per attempt; quarantine the foreign store entries; write W-3 once per revision outside the run process, with observed values | X |
| R3A-08 | cleanup | Y-16 / Y-11: the coverage array is the generator constant (2612) — the report's "computed from gen.COVERAGE_ROWS + this run's evaluations" is not what the code does; the row "C4b pass/fail (real)" stays `covered` while SCEN-B's C4b is PENDING (its caveat sits in the evidence cell); the K-05 row still reads "C4b completeness fail with C4a pass impossible (K-05)", the wording content §6 replaced | reporting accuracy | derive statuses from the run; split or mark the C4b row; adopt the T-3 wording | X |
| R3A-09 | cleanup | Y-17: the consulted-level return at 1429–1433 (STOP_CONTRACT_VIOLATION_EMPTY_U on a None scalar) still writes no `stops` record; the report's "verified by direct comparison" holds only because the path was not taken | none in this run | write the record or remove the branch | X |
| R3A-10 | cleanup | Y-02 (b): no pure construction function exists; UT-USET-CONSTRUCTION re-types the membership rule in test code (1726–1750; cases a–d without the cc flag), so it is evidence about the test, not about run_dp04 | none; the fixtures evidence run_dp04 | expose the construction as functions and call them from the test | X |
| R3A-11 | cleanup | Y-08: mandatory_tests_all_run = True is a literal (2621); corrections_complete is computed as the absence of expectation failures (2620), whereas DRAFT v2 §10 defines it over Y-01 … Y-19 and Y-21 and v6 §13 defines mandatory_tests_all_run over every applicable test; the report carries both as computed | end-state fields overstated (§9) | compute both fields from the test records | X |
| R3A-12 | cleanup | Y-18 / Y-12 / §9 items 13–15: the report has no custody table with observed hashes (four 64-hex values in the whole file), no per-finding table with test ids and results, no coverage matrix, no opened-file classification, no hash line block for the deliverables, no response table beyond Y-09 … Y-19, no attempt history of the r2 cycle (the inventory refers to it), and "parents_unchanged = true" without the re-hash values | the report cannot be checked without the other files | complete the report as v6 §12 item 10, §14 and DRAFT v2 §10 list | X |
| R3A-13 | informational | Transmission: the sidecars of deliverables 1–12 and the five quarantine notes were not received; sidecar agreement, "no self-hash" and the incident narratives (attempt 1, classifier defect, P-1 … P-7 corrections, attempt 8, transmittal-note corruption) are NOT PERFORMED / [X] | none on the verdict | PI: attach them; the auditor will fold them into a child revision | T |
| R3A-14 | informational | The start-state inventory discloses that the r2 checkpoint directory `.r2_checkpoint_2026-09-07` was deleted, not quarantined, at the end of the r2 cycle, so the r2 attempt history is NOT RECONSTRUCTIBLE from files. This closes the disclosure clause of R2A-01 as disclosed and not reconstructible | none on r3 | none; recorded | — |
| R3A-15 | informational | Preflight P-7 (c) withdrawn: the instruction not to create new document types was the PI's chat instruction to the drafter of DRAFT v2 (2026-09-21), not a clause of D-3 or D-4; the executor was never bound by it, and the report's §6 is answered here. The transmittal note stands as non-normative | none | closed by this record | — |
| R3A-16 | informational | T-EXPECT-ALL covers the 32 decision-layer fixtures and SCEN-B; SCEN-A has no structural expectation columns, and the FIX-*, UT-* and INJ-EXC-* rows carry none (their checks are assertions inside the harness). The prompt asked for structural expectations for as-computed fixtures | none | optional: add structural columns for SCEN-A and the unit-test rows | X (optional) |
| R3A-17 | informational | The auditor reproduction ([A-S], §7) confirms the platform-independent parts (all decision-layer objects, stops, expectations, residual key set, RUN1 == RUN2 in one process) and records the cross-platform differences (NR-01 (i) native hash f07fdc82…, NR-SPL rows, 5,244 versus 5,256 optimizer calls per run from the stage-3 fallback pattern, no natural COVERED capture in the auditor environment, statistics differing at relative ≤ 1.5e-4 with every comparison outcome unchanged); nothing in it verifies an executor hash | none | none | — |

## 5. Closure map

Corrections of the prompt (Y) and observations of the preflight (P). "CLOSED [A]" = verified on the delivered bytes.

| item | executor claim | auditor result |
|---|---|---|
| Y-01 | applied; T-RESTART-PROVENANCE 3 / 3 | PARTIAL — provenance established (§2); counters and per-call rows incomplete — R3A-06; disclosure — R3A-07 |
| Y-02 | applied | (a) CLOSED [A] ; (b) NOT CLOSED — R3A-10 ; (c) CLOSED [A] (C-08) |
| Y-03 | applied | (i) CLOSED [A] ; (ii) (iii) NOT CLOSED — R3A-04 ; (iv) constructions as §7 of the prompt: CLOSED [A] |
| Y-04 | applied | (a) (c) CLOSED [A] ; (b) (d) NOT CLOSED — R3A-03 |
| Y-05 | applied | PARTIAL — R3A-05 |
| Y-06 | 5 / 5 | CLOSED [X] ; [A-S] §7 |
| Y-07 | applied | NOT CLOSED — R3A-02 |
| Y-08 | computed | PARTIAL — R3A-11 |
| Y-09 | done | CLOSED [A] |
| Y-10 | N/A | NOT CLOSED — R3A-01 |
| Y-11 | unchanged | NOT CLOSED — R3A-08 |
| Y-12 | — | PARTIAL — R3A-12 |
| Y-13 | 73 / 73 | node hashes CLOSED [A] ; register row NOT CLOSED — R3A-01 |
| Y-14 | unchanged | NOT CLOSED — R3A-01 |
| Y-15 | pass | CLOSED [X] ; [A-S] §7 |
| Y-16 | confirmed | NOT CLOSED — R3A-08 |
| Y-17 | verified | NOT CLOSED in code — R3A-09 |
| Y-18 | §§2–5 | NOT CLOSED — R3A-12 |
| Y-19 | attempt history, parent re-hash | NOT CLOSED (register) — R3A-01 ; the attempt history of the r2 cycle is in no delivered file — R3A-12, R3A-14 |
| Y-20 | not applied (optional) | not applicable |
| Y-21 | fixed | CLOSED [A] (C-05 … C-07, C-18) |
| P-1 | closed | CLOSED [A] |
| P-2 | closed | PARTIAL — R3A-06, R3A-07 |
| P-3 | closed | PARTIAL — R3A-02, R3A-06 |
| P-4 | closed | PARTIAL — S2 stages [1, 2] [A]; the rest R3A-03 |
| P-5 | closed | CLOSED [A] |
| P-6 | closed | CLOSED [A] |
| P-7 (a) | closed | NOT CLOSED — R3A-08 |
| P-7 (b) | no change needed | report: CLOSED [A] (Y-09) ; custody record: R3A-07 |
| P-7 (c) | unresolved | withdrawn — R3A-15 |
| P-7 (d) | closed | CLOSED [X] |
| P-7 (e) | — | CLOSED [A] (fingerprint recomputed) |

## 6. Evidence for the gate-specific findings (line numbers of the delivered harness 5fea165c…)

```text
R3A-01  report lines 155 and 158: "N/A this report — checked at register authoring; no register row added or
        changed this cycle" ; "unchanged from r2 (register not re-authored this cycle)". No file named
        f3_step2_class_c_pin_register_r3_* is in the package and the report names none.
R3A-02  results: evaluation keys = c4_source, criteria, disc_f3_03_complement, dp04, fixture_id, interpretation,
        mechanism_outcome, p03, p03_fields, sexes ; sexes = {} in 34 / 34. canonical document (2476–2479) =
        evals, stops, a5, ut_probe_decouple, pins — no per-fit object. telemetry fields (2514–2516): no L, no
        predicates. fix_starts_full / fix_starts_dup called with a throwaway list (2267–2268); all_tel_rows =
        telemetry1 + exc_fixture_tel + a5_true_tel (2517). No T-SCHEMA / T-CANON symbol in the harness.
R3A-03  fit_spline 923–930: `except RuntimeError` ⇒ c, v = None, False ; src = "ACCEPTANCE_UNVERIFIABLE_UNRELATED"
        — the string occurs once in the file; exactness_findings = [EXACT-03] by construction (2600).
        run_exc_injection_fixtures 1807–1819: install_exc_unrelated_type_injection (1809), the ValueError caught by
        the test itself (1812–1815), install_nnls_test_injection again (1819), no uninstall ⇒ the traceback of
        the natural capture passes wrapped_nnls at 609, 628, 609. EXC_CAPTURES.clear() at 2355 precedes RUN1;
        solver_exceptions = exc_after_run1 (2599). Manifest rows INJ-EXC-*: run_scope both; executed once (2271).
R3A-04  run_dp04 1392–1395: inj_key / corrupt_idx / `corrupt_idx in U` ⇒ inconsistent_hit — no statistic is read.
        1429–1435: `if scal["P01"] is None or scal["P02"] is None` ⇒ return (no stops record) ; delta, `abs(delta)
        <= tau` unguarded. t_comparator_nan 1754–1771: pass_=True.
R3A-05  no symbol T-A5-SUPPORT; a5_unit_tests 1594–1607 are fit-based (A.5 (ii)/(iii)); 1548:
        `p_c4a = probe_raw and (a5_i is False)` with a5_i = None on violation (1494–1495) ⇒ probe excluded from
        the C4a numerator ⇒ a C4a outcome, contrary to content §2.3 and Y-05.
R3A-06  main 2209–2217 and 2261–2282: nrgates_all / unittests_all cached as tuples without SPLINE_TELEMETRY_CALLS;
        results.process: units_read_from_store nr_gates 1, unit_tests 1; per-call rows by (phase, pid):
        run1 / 10920 = 2,659, run1 / 1240 = 2,597, run2 / 1240 = 5,256; no nr_gates or unit_tests row; store
        manifest columns path, size_bytes, sha256.
```

## 7. Auditor reproduction [A-S]

The driver `aud_r3_full_repro.py` (§10) imports the unmodified harness 5fea165c… and the unmodified generator
cc23c9b5… into one Linux process (pid 532; Python 3.11.15, numpy 1.26.4, scipy 1.14.1; OMP / OPENBLAS / MKL = 1)
with the restart-store directory absent at start, and re-issues main()'s orchestration in main()'s order: loader,
non-regression gates (recorded, not asserted), pins, unit tests, RUN1, RUN2, check_expectations, residual export
from RUN1's own fit objects, canonical hashes, wrapper uninstall. Nothing is read from the store; no executor
deliverable path is written. Elapsed 1,792 s. The comparison script `r3_02_repro_compare.py` and its verbatim
output are in §10; every number below is copied from that output.

Platform-independent results — identical to the executor's results JSON (352791648b7c…):

```text
manifest         regenerated in memory with the harness's own writer: 9c944543… byte-identical [A]
loader           prelude match; 73 node-hash entries for 73 executed nodes (52 retained + 21 prelude)
pins             mask_full / mask_le / fs = True ; T-MASK-FULL-EXT pass
unit tests       the nine blocks a5_unit_tests, ut_probe_decouple, uset_construction, comparator_nan,
                 starts_default, starts_dup, fix_a5_true, exc_injection_fixtures, ut_exc_unrelated_reference are
                 equal to the executor's blocks field by field (notes excluded)
decision layer   32 / 32 INJ evaluation objects identical (canonical JSON) ; the 6 stops identical ; the
                 mechanism-outcome histogram identical ; SCEN-A and SCEN-B: p03, p03_fields, c4_source, the D-P04
                 consulted path and every boolean / integer field of the criteria identical (56 + 70 fields);
                 construction_audit identical (A.5 support sizes 42 / 54 / 41 / 32) ; `sexes` = {} in 34 / 34 here
                 as well (R3A-02 (e) is a property of the code, not of the platform)
expectations     check_expectations from the regenerated manifest: 33 declared, 33 ran, 0 fails
RUN1 == RUN2     a6310a06… == a6310a06… in one process (auditor environment) — not the executor's 7d40df61…, as
                 expected across platforms; no claim about the executor's value follows from this
residual export  11 keys = the executor's key set ; 0 optimizer calls during the export (export_calls = 0) ;
                 PIN-ACF bitwise 11 / 11 ; fitters P01 4, P02 4, SPL 3 ; the series values differ from the
                 executor's by at most 4.8e-6 (SCEN-A:F0:P01) and by 1e-14 … 1e-15 on the SPL keys — platform,
                 not code (the key set, the link and the hash chain are what Y-21 asks for; C-05 … C-07 are [A])
fidelity         5 declared / 5 executed ; wrapper_restore_ok True after uninstall ; nnls wrapper depth 3 after the
                 unit phase (R3A-03 (d) observed here as well)
captures (unit)  INJ-EXC-CAPTURE-S1 stage 1 ; INJ-EXC-CAPTURE-S2 stages 2 and 1 — P-4 closed on the auditor side too
mode telemetry   5,553 rows with the same per-fixture composition as the executor's file (SCEN-A 2,464, SCEN-B 2,181,
                 S1 146, S2 146, FIX-A5-TRUE 616)
```

Cross-platform differences — recorded, not adjudicated; none changes a comparison outcome:

```text
NR-01 (i)        native canonical f07fdc82… ≠ 6f197b74… ; hybrid == native (the T-2a adapter is exact with respect
                 to the native engine in this environment as well) ; NR-SPL 30 rows, repr-exact equality false —
                 the same two differences the r2 audit recorded
optimizer calls  5,244 per run here versus 5,256 there: 14 of the 32 real-scenario masks differ by one to four
                 stage-3 fallback (SLSQP) calls, which SOLVER-B issues when neither post-polished endpoint of the
                 primary trust-constr result is accepted at stage 1 or stage 2 — which modes need one depends on
                 the optimizer path (e.g. SCEN-A run1:F0:full — executor: modes 28, 55, 113 ; auditor: modes 21,
                 28, 29, 55) ; the status histograms differ accordingly (status 1: 4,001 vs 4,050 ; 2: 379 vs
                 330 ; 0: 824 vs 830 ; 8: 40 vs 46) ; the same counts in RUN1 and RUN2 on each side
natural capture  the executor's one COVERED capture (SCEN-A, F, run1:F0:full, mode 113, stage 2, "Maximum number
                 of iterations reached.") does not occur here: in this environment the post-polished endpoint of
                 mode 113 is accepted (one trust-constr call, no stage-3 fallback), so the nnls inside the
                 stage-2 acceptance check never raises. The auditor's RUN1 and RUN2 yield 0 captures. The
                 traceback line-number check C-04 is therefore on the executor's delivered record only [A]
SCEN statistics  40 of 84 (SCEN-A) and 18 of 62 (SCEN-B) hex-encoded statistics differ, relative 3.2e-16 … 1.5e-4
                 (SCEN-A: the largest on the P-01 C4b statistic of sex F ; SCEN-B: 6.5e-15 … 2.4e-6) — the
                 optimizer-path dependence of the family fits ; every threshold comparison, undefined flag, share
                 and n_valid is identical
```

What this section establishes: the delivered code, run once in a clean process with no store, produces the same
decision-layer objects, the same stops, the same expectation results and the same residual key set as the
delivered package; the corrections verified [A] in §3 behave in execution as read; and the phases nr_gates and
unit_tests do issue optimizer calls (60 and 941 here) that the executor's per-call file and counters lack because
the final process read those phases from the store as coarse units (R3A-06). What it does not establish: any
executor hash. RUN1 == RUN2 here is an auditor-environment fact; the executor's 7d40df61… is evidenced by the
executor's own RUN2 only [X], and the executor's NR-01 / NR-SPL passes remain [X].

## 8. Register (S / T / X)

```text
S  (PI scientific)
   S-R2-1  unchanged: DEFERRED_THIS_CYCLE in this cycle; F3-STEP2-EXACT-03 open. The wiring is verified (C-41).
           The decision is still the PI's; nothing in this record recommends a value.

T  (PI as dispatcher)
   T-R2-1  unchanged (r2 attestation; not made in D-4 §6).
   T-R2-2  AUTHORIZE_RESTART, as dispatched; in narrowed_evidence; the layer was used (§2).
   T-R3-1  transmission, not a decision: the sidecars of deliverables 1–12 ; the five quarantine notes named in
           the report ; the superseded custody records and harness revisions (6ddcc26d…, 891574fc…, d67e097d…,
           f882b922…, 99f895c1…) if the PI wants the attempt chain at tier [A]. Nothing in the verdict depends on
           them (R3A-13).
   T-R3-2  bookkeeping, not a decision: the next instrument names the second store prefix 548ae790… as an object
           to quarantine and list (R3A-07), and states whether the r3 register is to be authored before or
           within the next cycle (R3A-01).

X  (executor)
   blockers  R3A-01 (register) ; R3A-02 (Y-07) ; R3A-03 (Y-04 b, d) ; R3A-04 (Y-03 ii, iii) ; R3A-05 (Y-05) ;
             R3A-06 (Y-01 counters and provenance evidence)
   cleanup   R3A-07 … R3A-12
   optional  R3A-16
```

## 9. Status computation (auditor's view, v6 §13)

```text
corrections_complete      = false   (R3A-01 … R3A-06 ; the executor reports true — its own computation is the absence of
                                     expectation failures, line 2620)
mandatory_tests_all_run   = not established (literal at 2621 ; T-A5-SUPPORT, T-SCHEMA, T-CANON absent ;
                                     T-COMPARATOR-NAN passes by literal)
deferred_decisions        = [S-R2-1]
narrowed_evidence         = [T-R2-2]
uncovered_coverage_rows   = ["A.5 (iii) inadmissible refit", "D-P04 resolve at C1"] as reported; "C4b pass/fail
                            (real)" belongs to it in part (R3A-08)
open_findings             = [F3-STEP2-EXACT-03] ; no ENG finding recorded by the executor ; this record opens
                            R3A-01 … R3A-06 as X corrections
F3_STEP2_r3_status        = PARTIAL_PENDING_PI  (agrees with the executor)
F3_STEP2 = QUALIFIED      = NOT declared ; F3_EXECUTION_READY = false ; commit = false
```

What the next cycle needs from the PI: nothing scientific beyond S-R2-1, which stays deferred unless the PI decides
otherwise; the transmission items of T-R3-1; the bookkeeping of T-R3-2. What it needs from the executor: R3A-01 …
R3A-06 with their tests, and the cleanup items.

## 10. Appendix — evidence scripts and their verbatim output

Script `r3_01_package_checks.py` (read-only; run on 2026-09-24 in the auditor environment):

```python
#!/usr/bin/env python3
# p_konum_plus F3 STEP-2 r3 -- independent audit, evidence script 01: checks on the delivered package (15 files
# received 2026-09-24). Read-only. Every value printed is computed from the received bytes or from the
# auditor's own reproduction outputs named below.
import json, hashlib, struct, math, csv, collections, os, re, itertools
R = "/home/claude/audit_r3/recv2/"; UP = "/root/.claude/uploads/9c789a02-f865-56de-9f2f-e299f3cfca3a/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
def up(prefix):
    fn = [f for f in os.listdir(UP) if f.startswith(prefix)]; assert len(fn) == 1, (prefix, fn); return UP + fn[0]
N = {"har": "f3_step2_adequacy_harness_r3_2026-09-22.py", "gen": "f3_step2_fixture_generator_r3_2026-09-22.py",
     "man": "f3_step2_fixture_manifest_r3_2026-09-22.csv", "cust": "f3_step2_r3_preexecution_custody_2026-09-22.md",
     "tel": "f3_step2_telemetry_r3_2026-09-22.csv", "res": "f3_step2_results_r3_2026-09-22.json",
     "resid": "f3_step2_residual_series_r3_2026-09-22.json", "te": "f3_step2_test_evidence_r3_2026-09-22.json",
     "pc": "f3_step2_spline_percall_telemetry_r3_2026-09-22.csv", "rep": "f3_step2_correction_report_r3_2026-09-24.md",
     "inv": "f3_step2_r3_start_state_inventory_2026-09-22.md", "alog": "f3_step2_r3_attempt_log_2026-09-22.md",
     "store": "f3_step2_r3_restart_store_manifest_2026-09-22.csv", "d4": "f3_step2_r3_pi_dispatch_record_2026-09-22.md",
     "tn": "f3_step2_r3_auditor_transmittal_note_2026-09-22.md"}
PRE = {"har": "90f1b34d-", "gen": "f6a6b931-", "man": "83f108b8-", "cust": "0650b2af-", "tel": "97f99f37-", "res": "c67f0d5f-",
       "resid": "72aa98b1-", "te": "239a8492-", "pc": "3307d61a-", "rep": "5825632a-", "inv": "a8b33d4b-", "alog": "e065f255-",
       "store": "aa0941a1-", "d4": "4de86acf-", "tn": "880ad739-"}
H = {}
print("== [1] received files (upload prefix -> canonical name): SHA256, bytes, CR bytes")
for k, name in N.items():
    b = open(R + name, "rb").read(); assert b == open(up(PRE[k]), "rb").read(); H[k] = hashlib.sha256(b).hexdigest()
    print(f"  {H[k]}  {len(b):8d}  CR={b.count(bytes([13]))}  {PRE[k]}{name}")
print("  D-4 copy == dispatched D-4 (4e623536...):", H["d4"] == "4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865")
print("  transmittal note == first delivery (bbe898cc...):", H["tn"] == "bbe898cc89086ff179349f2925a670301b87dd2dad31afd141de13e771aa4a33")
print("  files of DRAFT v2 s9 NOT received: 9 register r3 ; 14 sidecars of 1-12 ; quarantine notes named by the report (5)")

har = open(R + N["har"], encoding="utf-8").read(); hl = har.split("\n")
cust = open(R + N["cust"], encoding="utf-8").read(); alog = open(R + N["alog"], encoding="utf-8").read()
rep = open(R + N["rep"], encoding="utf-8").read(); r = json.load(open(R + N["res"])); te = json.load(open(R + N["te"]))
print("\n== [2] which bytes ran: custody record / harness constants / attempt log / results / store fingerprints")
g = lambda k, s: (re.search(r"^%s = (.+)$" % k, s, re.M) or [None, "ABSENT"])[1]
print("  custody.harness_sha256   =", g("harness_sha256", cust), "| == delivered harness:", g("harness_sha256", cust) == H["har"])
print("  custody.generator_sha256 =", g("generator_sha256", cust), "| == delivered generator:", g("generator_sha256", cust) == H["gen"])
print("  custody.manifest_sha256  =", g("manifest_sha256", cust), "| == delivered manifest:", g("manifest_sha256", cust) == H["man"], "| == results.fixture_manifest_sha256:", r["fixture_manifest_sha256"] == H["man"])
print("  custody.supersedes_harness_sha256 =", g("supersedes_harness_sha256", cust), "| harness constant SUPERSEDES_HARNESS_SHA256 line 112:", hl[111].strip())
print("  custody.attempt_number =", g("attempt_number", cust), "| harness ATTEMPT_NUMBER line 128:", hl[127].strip(), "| harness docstring line 24:", hl[23].strip())
print("  custody.code_env_fingerprint =", g("code_env_fingerprint", cust), "| restart_layer_active_at_this_W3 =", g("restart_layer_active_at_this_W3", cust))
print("  custody line 40 declaration:", hl[2193].strip()[:60], "... (template written by every launch: harness lines 2173-2205)")
print("  custody 'dispatch_preconditions_P1_P4 = ALL PASS' is a literal in the harness (line 2182):", "ALL PASS" in hl[2181])
print("  custody dispatch_record_sha256 is the constant DISPATCH_RECORD_HASH (line 248), not computed:", "DISPATCH_RECORD_HASH = " in hl[247] and "DISPATCH_RECORD_HASH" in hl[2201])
print("  results.process:", json.dumps({k: r["process"][k] for k in ("pid", "start", "end", "attempt_number", "restart_layer_active", "supersedes_harness_sha256", "units_computed_this_process", "units_read_from_store", "spline_telemetry_calls_by_phase")}, sort_keys=True))
rows_alog = [l for l in alog.split("\n") if l.startswith("| ") and l[2].isdigit()]
print("  attempt log rows:", len(rows_alog))
for l in rows_alog:
    c = [x.strip() for x in l.strip("|").split("|")]
    print("    #%s rev %s pid %s start %s -> %s" % (c[0], c[1][:64].replace("`", ""), c[2], c[3][:19], c[5][:60]))
def fp(h, gg, m, env=("3.11.7", "1.26.4", "1.14.1", "Windows-10-10.0.19045-SP0")):
    return hashlib.sha256("|".join([h, gg, m, "01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077",
        "b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d", *env, "1", "1", "1"]).encode()).hexdigest()[:16]
print("  fingerprint formula (harness lines 2166-2171) recomputed by the auditor:")
print("    delivered (5fea165c, cc23c9b5, 9c944543) ->", fp(H["har"], H["gen"], H["man"]), "| == custody fingerprint:", fp(H["har"], H["gen"], H["man"]) == g("code_env_fingerprint", cust))
print("    attempt-log rev-5 hash 99f895c1 with delivered gen/man ->", fp("99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a", H["gen"], H["man"]))
print("    rev-4 f882b922 with delivered gen/man ->", fp("f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5", H["gen"], H["man"]))
print("    control: first delivery (d67e097d, e35c2bf0, 4544ff75) ->", fp("d67e097dc158c4909276b026ce66533f33dfab7a94d800e57342eb86e76f58ff", "e35c2bf06ee4087bac97bd5b6e81d35d079ff1dddf8d2e68555c6c7d18859638", "4544ff7565165f7541c0264b886bc2692374caf2ee875ec65a877c1a2909ec33"), "(that custody record printed 6f4e29ccc903bce6)")
st = list(csv.DictReader(open(R + N["store"], newline="")))
pref = collections.Counter(x["path"].split("__")[0] for x in st)
print("  store manifest rows:", len(st), "| columns:", list(st[0].keys()), "| fingerprint prefixes:", dict(pref))
kinds = collections.Counter((x["path"].split("__")[0], x["path"].split("__")[1].split("_")[0]) for x in st)
print("  entry kinds per prefix:", {f"{a}:{b}": n for (a, b), n in sorted(kinds.items())})
print("  store manifest carries pid / start_iso columns:", any(c in st[0] for c in ("pid", "start_iso")), "| harness writes the store manifest (grep STORE_MANIFEST_PATH uses):", [i + 1 for i, l in enumerate(hl) if "STORE_MANIFEST_PATH" in l])

print("\n== [3] per-call telemetry (deliverable added this cycle) vs process block")
pc = list(csv.DictReader(open(R + N["pc"], newline="")))
print("  rows:", len(pc), "| by phase:", dict(collections.Counter(x["phase"] for x in pc)), "| by pid:", dict(collections.Counter(x["pid"] for x in pc)))
print("  by (phase, pid):", dict(collections.Counter((x["phase"], x["pid"]) for x in pc)))
print("  run1 rows from pid 10920 by mask (SCEN-A):", {m: n for (f, m, p), n in sorted(collections.Counter((x["fixture"], x["mask_id"], x["pid"]) for x in pc if x["phase"] == "run1").items()) if p == "10920"})
print("  rows with numeric nit:", sum(1 for x in pc if x["nit"].lstrip("-").isdigit()), "| methods:", dict(collections.Counter(x["method"] for x in pc)))
print("  rows of phase nr_gates / unit_tests / residual_export:", sum(1 for x in pc if x["phase"] in ("nr_gates", "unit_tests", "residual_export")))
print("  harness: coarse store units nrgates_all / unittests_all carry no per-call snapshot (lines 2209-2217, 2261-2282); the final process read both (process block)")
tel = list(csv.DictReader(open(R + N["tel"], newline="")))
print("  mode-level telemetry rows:", len(tel), "| by fixture:", dict(collections.Counter(x["fixture"] for x in tel)), "| run2 rows:", sum(1 for x in tel if x["mask_id"].startswith("run2")))
print("  FIX-STARTS rows:", sum(1 for x in tel if x["fixture"].startswith("FIX-STARTS")), "(harness lines 2267-2268 pass a throwaway list)")
print("  'sexes' non-empty in evaluations:", sum(1 for e in r["evaluations"] if e["sexes"]), "of", len(r["evaluations"]))

print("\n== [4] traceback line numbers of the natural COVERED capture vs the delivered harness bytes")
for x in te["exc_captures"]:
    frames = re.findall(r'File "([^"]+)", line (\d+), in (\w+)', x["traceback"])
    print("  record:", {k: x[k] for k in ("fixture", "sex", "trajectory", "mask_id", "mode", "stage", "kind", "exception_type")})
    for f, l, fn in frames:
        if "adequacy_harness_r3" in f:
            print(f"    harness line {l} in {fn}: {hl[int(l) - 1].strip()}")
        else:
            print(f"    {os.path.basename(f)} line {l} in {fn}")
print("  install order: main 2143 install_nnls_test_injection ; run_exc_injection_fixtures 1809 install_exc_unrelated_type_injection, 1819 install_nnls_test_injection again (no uninstall):",
      "install_nnls_test_injection(spl)" in hl[2142] and "install_exc_unrelated_type_injection(spl)" in hl[1808] and "install_nnls_test_injection(spl)" in hl[1818])
print("  exc_injection_fixtures:", json.dumps(te["exc_injection_fixtures"], sort_keys=True), "| solver_exceptions records:", len(r["solver_exceptions"]), "(RUN1 only: line 2599 exc_after_run1; EXC_CAPTURES.clear() at 2355 discards the unit-phase TEST_ONLY records)")

print("\n== [5] residual series vs link records, PIN-ACF recomputed, RUN1 C3 counterparts, Y-21 key set")
rs = json.load(open(R + N["resid"])); link = te["residual_link"]; acfmap = {x["vector"]: x for x in te["acf"]}
ev = {e["fixture_id"]: e for e in r["evaluations"]}
def acf(vals):
    T = len(vals); s = 0.0
    for t in range(T): s = s + vals[t]
    rbar = s / float(T); a = [v - rbar for v in vals]; num = 0.0
    for t in range(T - 1): num = num + a[t] * a[t + 1]
    den = 0.0
    for t in range(T): den = den + a[t] * a[t]
    return abs(num / den)
print("  keys:", len(rs), "| == link keys:", set(rs) == set(link), "| SCEN-B:M0:SPL present:", "SCEN-B:M0:SPL" in rs, "| file == r2 R-07:", H["resid"] == "f28bd6a02978154d1ba71d83a8ffe42cdc5e95d12a26c43b886439cca19b94f5")
for k in sorted(rs):
    vals = [float.fromhex(v) for v in rs[k]]; hh = hashlib.sha256(struct.pack("<%dd" % len(vals), *vals)).hexdigest(); phi = acf(vals)
    fx, stj, fit = k.split(":"); sx = stj[0]; c3 = ev[fx]["criteria"]["P02" if fit == "P02" else "P01"]["C3"][sx]
    run1 = c3["spline_stat"] if fit == "SPL" else c3["stat"]
    print(f"  {k:15s} n={len(vals)} finite={all(math.isfinite(v) for v in vals)!s:5s} sha==link:{hh == link[k]['sha256']!s:5s} sha==acf:{hh == acfmap[k]['sha256_146_float64_le']!s:5s} phi==executor:{phi.hex() == acfmap[k]['phi']!s:5s} RUN1 sex-level C3: {'== export' if run1 == phi.hex() else ('none (V3 empty)' if run1 is None else 'DIFFERS')}")
print("  RUN1 keys expected by Y-21 (a) = completed full-data fits at which RUN1 computes phi: telemetry full-mask fits that ran:",
      sorted(set((x["fixture"], x["mask_id"].split(":")[1], x["fitter"]) for x in tel if x["mask_id"].endswith(":full") and x["status"] != "TEST_ONLY_INJECTION" and x["mask_id"].startswith("run1"))) == sorted(set((k.split(":")[0], k.split(":")[1], {"P01": "P-01", "P02": "P-02", "SPL": "SPL"}[k.split(":")[2]]) for k in rs)))

print("\n== [6] T-EXPECT-ALL re-done by the auditor from the manifest columns and the results")
man = list(csv.DictReader(open(R + N["man"], newline="")))
UL = {"U2": "C2", "U3": "C3", "U4": "C4b", "U5": "C5"}
declared = 0; fails = []
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
                if got != int(val): mism.append(f"U{uk}{s2}={got}")
    if exp["expected_stops"] and exp["expected_stops"] not in [s["stop"] for s in r["stops"] if s["fixture"] == fid]: mism.append("stops")
    if exp["expected_undefined"]:
        for part in exp["expected_undefined"].split(";"):
            key, val = part.split("="); fam, crit, sx = key.split(":")
            got = e["criteria"][fam][crit][sx].get("undefined")
            if got != (val == "True"): mism.append(f"undefined[{key}]={got}")
    if mism: fails.append((fid, mism))
print("  declared:", declared, "| results.expectation_checks:", json.dumps(r["expectation_checks"]), "| auditor mismatches:", fails or "none")
print("  manifest rows without any expected_* value:", [row["fixture_id"] for row in man if not any(row[k] for k in ("expected_p03", "expected_mechanism_outcome", "expected_resolved_level", "expected_U_sizes", "expected_stops", "expected_undefined"))])
print("  INJ-NAN-STAT-SPL C2 undefined flags now:", {f"{fam}:{sx}": ev["INJ-NAN-STAT-SPL"]["criteria"][fam]["C2"][sx]["undefined"] for fam in ("P01", "P02") for sx in ("F", "M")})
print("  mechanism outcomes:", dict(collections.Counter(e["mechanism_outcome"] for e in r["evaluations"])))

print("\n== [7] code facts cited in the findings (line numbers of the delivered harness)")
for ln, what in ((2612, "coverage = generator constant"), (2621, "mandatory_tests_all_run literal"), (1392, "INCONSISTENT_U from test flag"), (1394, "INCONSISTENT_U from test flag"),
                 (1429, "early return without stops record"), (1431, "early return label"), (1548, "A5 None -> probe counted as C4a failure"), (929, "UNRELATED RuntimeError -> mode invalid"),
                 (1815, "ValueError propagates past fit_spline"), (1768, "t_comparator_nan pass_=True literal"), (1726, "UT-USET re-types the rule"), (2267, "fix_starts_full throwaway telemetry"),
                 (2268, "fix_starts_dup throwaway telemetry"), (2355, "EXC_CAPTURES.clear() before run1"), (2599, "solver_exceptions = RUN1 captures only")):
    print(f"  L{ln} ({what}): {hl[ln - 1].strip()[:110]}")
print("  coverage statuses in results:", dict(collections.Counter(c[3] for c in r["coverage"])), "| generator COVERAGE_ROWS count:", sum(1 for l in open(R + N["gen"], encoding='utf-8') if l.startswith('    ("')))
print("  end_state:", json.dumps(r["end_state"], sort_keys=True))
print("  report claims checked against code: Y-16 'computed from gen.COVERAGE_ROWS + this run's evaluations':", "this run's evaluations" in rep, "| Y-17 'every STOP-outcome consulted-level return writes a stops record':", "every STOP-outcome consulted-level return writes" in rep)
print("  register r3 named in report:", "class_c_pin_register_r3" in rep, "| report Y-10/Y-14 rows say register not re-authored:", "register not re-authored this cycle" in rep)
```

Output:

```text
== [1] received files (upload prefix -> canonical name): SHA256, bytes, CR bytes
  5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77    129023  CR=0  90f1b34d-f3_step2_adequacy_harness_r3_2026-09-22.py
  cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8     46877  CR=0  f6a6b931-f3_step2_fixture_generator_r3_2026-09-22.py
  9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a     19623  CR=0  83f108b8-f3_step2_fixture_manifest_r3_2026-09-22.csv
  a910e1b65f47d197387b1add29894cafc3267a7422ab22b9fd2bf99632f4e0c0      1938  CR=0  0650b2af-f3_step2_r3_preexecution_custody_2026-09-22.md
  24f21811886c9aab3e2e57f649b0fa3d6964f729ae6978569f926fe32737d0d7   2218399  CR=0  97f99f37-f3_step2_telemetry_r3_2026-09-22.csv
  352791648b7c3dc1151962905ec2270fe3ae4246846f2021c2dcda3e3dfe18fb   1599379  CR=0  c67f0d5f-f3_step2_results_r3_2026-09-22.json
  3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f     42820  CR=0  72aa98b1-f3_step2_residual_series_r3_2026-09-22.json
  b7d3b861be33f6271d372dbe13a38826d2946c3acf97c227533dddad09edb03b     24166  CR=0  239a8492-f3_step2_test_evidence_r3_2026-09-22.json
  9d0c627ebc5949e4b8e61c48e453d16c28ba61733047d737fcf3f8d2cb5a30fe   1775410  CR=0  3307d61a-f3_step2_spline_percall_telemetry_r3_2026-09-22.csv
  80df7914940f0cdbdfd327d8d133fa556ad9ab024c1b218a4dd39eac09a8dfae     12535  CR=0  5825632a-f3_step2_correction_report_r3_2026-09-24.md
  71a3f5a7cf98c3b122cb63eac36d2db1a6f8b20503fc05d0eeb7c6caafbed089     33320  CR=0  a8b33d4b-f3_step2_r3_start_state_inventory_2026-09-22.md
  253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5      7072  CR=0  e065f255-f3_step2_r3_attempt_log_2026-09-22.md
  933dcaeeb979ae2872d91597c6c9c1ba8484266a4b3ac84e562e25248e6d39e9   3398062  CR=0  aa0941a1-f3_step2_r3_restart_store_manifest_2026-09-22.csv
  4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865      6848  CR=0  4de86acf-f3_step2_r3_pi_dispatch_record_2026-09-22.md
  bbe898cc89086ff179349f2925a670301b87dd2dad31afd141de13e771aa4a33      7198  CR=0  880ad739-f3_step2_r3_auditor_transmittal_note_2026-09-22.md
  D-4 copy == dispatched D-4 (4e623536...): True
  transmittal note == first delivery (bbe898cc...): True
  files of DRAFT v2 s9 NOT received: 9 register r3 ; 14 sidecars of 1-12 ; quarantine notes named by the report (5)

== [2] which bytes ran: custody record / harness constants / attempt log / results / store fingerprints
  custody.harness_sha256   = 5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77 | == delivered harness: True
  custody.generator_sha256 = cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8 | == delivered generator: True
  custody.manifest_sha256  = 9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a | == delivered manifest: True | == results.fixture_manifest_sha256: True
  custody.supersedes_harness_sha256 = 99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a | harness constant SUPERSEDES_HARNESS_SHA256 line 112: SUPERSEDES_HARNESS_SHA256 = "99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a"
  custody.attempt_number = 5 | harness ATTEMPT_NUMBER line 128: ATTEMPT_NUMBER = 5 | harness docstring line 24: ATTEMPT 4 (this file, live), harness revision 4. Revision 1
  custody.code_env_fingerprint = 1ba561daefb48b2e | restart_layer_active_at_this_W3 = True
  custody line 40 declaration: "and manifest exist and are hashed, and BEFORE the first tes ... (template written by every launch: harness lines 2173-2205)
  custody 'dispatch_preconditions_P1_P4 = ALL PASS' is a literal in the harness (line 2182): True
  custody dispatch_record_sha256 is the constant DISPATCH_RECORD_HASH (line 248), not computed: True
  results.process: {"attempt_number": 5, "end": "2026-09-24T14:51:59.765920", "pid": 1240, "restart_layer_active": true, "spline_telemetry_calls_by_phase": {"run1": 5256, "run2": 5256}, "start": "2026-09-24T14:27:44.558016", "supersedes_harness_sha256": "99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a", "units_computed_this_process": {"nr_gates": 0, "residual_export": 1, "run1": 2, "run2": 2, "unit_tests": 0}, "units_read_from_store": {"nr_gates": 1, "residual_export": 0, "run1": 0, "run2": 0, "unit_tests": 1}}
  attempt log rows: 10
    #1 rev 1 (6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b pid 4220 start 2026-09-22T12:22:28 -> **interrupted** — host process exited outside harness contro
    #2 rev 2 (891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a pid 5232 start 2026-09-22T14:43:48 -> **interrupted**, same external pattern. Restart store began 
    #3 rev 2 (same bytes as #2, resumed) pid 8740 start 2026-09-23T13:37:05 -> **completed**, but later found defective: the post-hoc excep
    #4 rev 3 (d67e097dc158c4909276b026ce66533f33dfab7a94d800e57342eb86e76f pid 21380 start 2026-09-23T13:56:21 -> **interrupted**, same external pattern.
    #5 rev 3 (same bytes as #4, resumed) pid 24220 start 2026-09-23T19:32:32 -> **completed**, verified: RUN1==RUN2 (`943d14ab...`), natural
    #6 rev 4 (f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0eb pid 18036 start 2026-09-23T21:51:13 -> **interrupted**, same external pattern. Restart store had be
    #7 rev 4 (same bytes as #6) pid — (never started) start 2026-09-24 -> **operator error, not a harness or environment event**: a `c
    #8 rev 4 (same bytes as #6, resumed via absolute path) pid 15252 start 2026-09-24T11:37:01 -> **crashed on its own new assertion** — a real gap in this cy
    #9 rev 5 (99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f21225 pid 10920 start 2026-09-24T12:02:04 -> **interrupted**, same external pattern.
    #10 rev 5 (same bytes as #9, resumed via absolute path) pid 1240 start 2026-09-24T14:27:44 -> **completed, verified**: RUN1==RUN2 (`7d40df61...`), `T_CALL
  fingerprint formula (harness lines 2166-2171) recomputed by the auditor:
    delivered (5fea165c, cc23c9b5, 9c944543) -> 1ba561daefb48b2e | == custody fingerprint: True
    attempt-log rev-5 hash 99f895c1 with delivered gen/man -> 327fcf82f949fc66
    rev-4 f882b922 with delivered gen/man -> e3ccc7d133c9ff2f
    control: first delivery (d67e097d, e35c2bf0, 4544ff75) -> 6f4e29ccc903bce6 (that custody record printed 6f4e29ccc903bce6)
  store manifest rows: 23446 | columns: ['path', 'size_bytes', 'sha256'] | fingerprint prefixes: {'1ba561daefb48b2e': 11723, '548ae790f6ac756a': 11723}
  entry kinds per prefix: {'1ba561daefb48b2e:nrgates': 1, '1ba561daefb48b2e:onestart': 2081, '1ba561daefb48b2e:realscen': 4, '1ba561daefb48b2e:splmode': 9636, '1ba561daefb48b2e:unittests': 1, '548ae790f6ac756a:nrgates': 1, '548ae790f6ac756a:onestart': 2081, '548ae790f6ac756a:realscen': 4, '548ae790f6ac756a:splmode': 9636, '548ae790f6ac756a:unittests': 1}
  store manifest carries pid / start_iso columns: False | harness writes the store manifest (grep STORE_MANIFEST_PATH uses): [241, 2574]

== [3] per-call telemetry (deliverable added this cycle) vs process block
  rows: 10512 | by phase: {'run1': 5256, 'run2': 5256} | by pid: {'10920': 2659, '1240': 7853}
  by (phase, pid): {('run1', '10920'): 2659, ('run1', '1240'): 2597, ('run2', '1240'): 5256}
  run1 rows from pid 10920 by mask (SCEN-A): {'run1:F0:fold0': 249, 'run1:F0:fold1': 149, 'run1:F0:fold2': 153, 'run1:F0:fold3': 155, 'run1:F0:fold4': 252, 'run1:F0:full': 149, 'run1:F0:probeL': 153, 'run1:F0:probeR': 149, 'run1:M0:fold0': 232, 'run1:M0:fold1': 148, 'run1:M0:fold2': 150, 'run1:M0:fold3': 147, 'run1:M0:fold4': 245, 'run1:M0:full': 153, 'run1:M0:probeL': 147, 'run1:M0:probeR': 28}
  rows with numeric nit: 10512 | methods: {'trust-constr': 8760, 'SLSQP': 1752}
  rows of phase nr_gates / unit_tests / residual_export: 0
  harness: coarse store units nrgates_all / unittests_all carry no per-call snapshot (lines 2209-2217, 2261-2282); the final process read both (process block)
  mode-level telemetry rows: 5553 | by fixture: {'SCEN-A': 2464, 'SCEN-B': 2181, 'INJ-EXC-CAPTURE-S1': 146, 'INJ-EXC-CAPTURE-S2': 146, 'FIX-A5-TRUE': 616} | run2 rows: 0
  FIX-STARTS rows: 0 (harness lines 2267-2268 pass a throwaway list)
  'sexes' non-empty in evaluations: 0 of 34

== [4] traceback line numbers of the natural COVERED capture vs the delivered harness bytes
  record: {'fixture': 'SCEN-A', 'sex': 'F', 'trajectory': 0, 'mask_id': 'run1:F0:full', 'mode': 113, 'stage': 2, 'kind': 'COVERED', 'exception_type': 'RuntimeError'}
    harness line 509 in wrapped_accept: return real_accept(c, z, O, A)
    f3_spline_solver_qualification_harness_r2_2026-09-03.py line 313 in accept
    f3_spline_solver_qualification_harness_r2_2026-09-03.py line 304 in kkt_res
    harness line 609 in wrapped_nnls: return real_nnls(*args, **kwargs)
    harness line 628 in wrapped_nnls: return real_nnls(*args, **kwargs)
    harness line 609 in wrapped_nnls: return real_nnls(*args, **kwargs)
    C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_nnls.py line 93 in nnls
  install order: main 2143 install_nnls_test_injection ; run_exc_injection_fixtures 1809 install_exc_unrelated_type_injection, 1819 install_nnls_test_injection again (no uninstall): True
  exc_injection_fixtures: {"S1": {"count": 1, "pass_": true, "stages": [1]}, "S2": {"count": 2, "pass_": true, "stages": [1, 2]}, "UNRELATED_TYPE": {"pass_": true, "propagated_uncaught": true}} | solver_exceptions records: 1 (RUN1 only: line 2599 exc_after_run1; EXC_CAPTURES.clear() at 2355 discards the unit-phase TEST_ONLY records)

== [5] residual series vs link records, PIN-ACF recomputed, RUN1 C3 counterparts, Y-21 key set
  keys: 11 | == link keys: True | SCEN-B:M0:SPL present: False | file == r2 R-07: False
  SCEN-A:F0:P01   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-A:F0:P02   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-A:F0:SPL   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-A:M0:P01   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-A:M0:P02   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-A:M0:SPL   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-B:F0:P01   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-B:F0:P02   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-B:F0:SPL   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: == export
  SCEN-B:M0:P01   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: none (V3 empty)
  SCEN-B:M0:P02   n=146 finite=True  sha==link:True  sha==acf:True  phi==executor:True  RUN1 sex-level C3: none (V3 empty)
  RUN1 keys expected by Y-21 (a) = completed full-data fits at which RUN1 computes phi: telemetry full-mask fits that ran: True

== [6] T-EXPECT-ALL re-done by the auditor from the manifest columns and the results
  declared: 33 | results.expectation_checks: {"EXPECTATION_FAIL": "none", "declared": 33, "detail": [], "ran": 33} | auditor mismatches: none
  manifest rows without any expected_* value: ['SCEN-A', 'FIX-STARTS-FULL', 'FIX-STARTS-DUP', 'FIX-A5-TRUE', 'UT-USET-CONSTRUCTION-a', 'UT-USET-CONSTRUCTION-b', 'UT-USET-CONSTRUCTION-c', 'UT-USET-CONSTRUCTION-d', 'UT-USET-CONSTRUCTION-e', 'INJ-EXC-CAPTURE-S1', 'INJ-EXC-CAPTURE-S2', 'INJ-EXC-UNRELATED-TYPE', 'UT-EXC-UNRELATED-REFERENCE']
  INJ-NAN-STAT-SPL C2 undefined flags now: {'P01:F': True, 'P01:M': True, 'P02:F': True, 'P02:M': True}
  mechanism outcomes: {'RESOLVED_MECHANISM_P01': 6, 'STOP_BOTH_FAIL_REDESIGN': 4, 'ONLY_P02_PASSES': 13, 'ONLY_P01_PASSES': 1, 'MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-03)': 2, 'TERMINAL_FALLBACK_MECHANISM_P01': 5, 'STOP_CONTRACT_VIOLATION_EMPTY_U': 1, 'STOP_CONTRACT_VIOLATION_INCONSISTENT_U': 1, 'MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING)': 1}

== [7] code facts cited in the findings (line numbers of the delivered harness)
  L2612 (coverage = generator constant): coverage=[list(r) for r in gen.COVERAGE_ROWS],
  L2621 (mandatory_tests_all_run literal): mandatory_tests_all_run=True,
  L1392 (INCONSISTENT_U from test flag): inj_key = f"inject_post_construction_invalid_{crit}"
  L1394 (INCONSISTENT_U from test flag): if corrupt_idx is not None and corrupt_idx in U:
  L1429 (early return without stops record): if scal["P01"] is None or scal["P02"] is None:
  L1431 (early return label): mechanism_outcome="STOP_CONTRACT_VIOLATION_EMPTY_U",
  L1548 (A5 None -> probe counted as C4a failure): p_c4a = probe_raw and (a5_i is False)   # A5 unresolved (None) => exclude, not pass
  L929 (UNRELATED RuntimeError -> mode invalid): src, pst = "ACCEPTANCE_UNVERIFIABLE_UNRELATED", "EXC:" + type(exc).__name__
  L1815 (ValueError propagates past fit_spline): raised = True   # NOT converted -- propagates past fit_spline entirely
  L1768 (t_comparator_nan pass_=True literal): pass_=True,
  L1726 (UT-USET re-types the rule): U2 = [i for i in range(n_s) if valid(p1["rho"][i]) and valid(p2["rho"][i])]
  L2267 (fix_starts_full throwaway telemetry): starts_full = fix_starts_full(f2m, grids, [])
  L2268 (fix_starts_dup throwaway telemetry): starts_dup = fix_starts_dup(f2m, grids, [])
  L2355 (EXC_CAPTURES.clear() before run1): EXC_CAPTURES.clear()
  L2599 (solver_exceptions = RUN1 captures only): solver_exceptions=exc_after_run1,
  coverage statuses in results: {'covered': 57, 'covered_injection_only': 2, 'UNCOVERED(no construction possible without touching frozen code)': 1, 'UNCOVERED(S-R2-1 DEFERRED)': 1} | generator COVERAGE_ROWS count: 61
  end_state: {"F3_STEP2_r3_status": "PARTIAL_PENDING_PI", "PI_dispatch_record_hash": "4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865", "corrections_complete": true, "deferred_decisions": ["S-R2-1"], "mandatory_tests_all_run": true, "narrowed_evidence": ["T-R2-2"], "open_findings": ["F3-STEP2-EXACT-03"], "uncovered_coverage_rows": ["A.5 (iii) inadmissible refit", "D-P04 resolve at C1"]}
  report claims checked against code: Y-16 'computed from gen.COVERAGE_ROWS + this run's evaluations': True | Y-17 'every STOP-outcome consulted-level return writes a stops record': True
  register r3 named in report: False | report Y-10/Y-14 rows say register not re-authored: True
```

Reproduction driver `aud_r3_full_repro.py` (imports the unmodified harness and generator; §7):

```python
"""Auditor same-environment reproduction driver (F3 STEP-2 r3 independent audit, 2026-09-24).
Imports the UNMODIFIED r3 harness (5fea165c...) and the UNMODIFIED r3 generator (cc23c9b5...) and
re-issues main()'s orchestration (harness lines 2130-2492) with exactly these differences:
 (1) the platform-bound asserts (NR-01(i) hash == 6f197b74..., NR-SPL repr-exact row equality) are RECORDED
     instead of asserted;
 (2) no executor deliverable path is written: the custody record, manifest, results, telemetry, residual and
     test-evidence files of the harness are NOT written; everything is recorded under auditor/;
 (3) the restart store directory is asserted ABSENT at start (one clean process; RESTART_LAYER_ACTIVE is left
     as delivered = True, so the store fills as a side effect but nothing is ever read from it).
Single process. Synthetic fixtures only. No real SSA data."""
import importlib.util, sys, json, os, hashlib, time, platform, warnings, io, csv
warnings.filterwarnings("ignore")
T0 = time.time()
OUT = "/home/claude/audit_ws/auditor/r3_full_repro_out.json"
HP = "G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_r3_2026-09-22.py"
spec = importlib.util.spec_from_file_location("h_r3", HP); h = importlib.util.module_from_spec(spec)
sys.modules["h_r3"] = h; spec.loader.exec_module(h)      # module import: os.chdir(REPO) happens here
import numpy as np, scipy
assert not os.path.isdir(h.RESTART_STORE_DIR), "restart store dir exists at start"
res = dict(env=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                    platform=platform.platform()),
           pid=os.getpid(), start_iso=h.PROCESS_START_ISO,
           harness_sha256=hashlib.sha256(open(h.__file__, "rb").read()).hexdigest(),
           generator_sha256=hashlib.sha256(open(h.GEN_PATH, "rb").read()).hexdigest(),
           restart_layer_active_as_delivered=h.RESTART_LAYER_ACTIVE, store_absent_at_start=True)
def save():
    res["elapsed_s"] = time.time() - T0
    json.dump(h.canon(res), open(OUT, "w"), indent=1, sort_keys=True, default=str)
def log(msg):
    print("[%6.0fs] %s" % (time.time() - T0, msg), flush=True)

sys.path.insert(0, "p_konum_plus/calibration")
gs = importlib.util.spec_from_file_location(h.GEN_MODULE_NAME, h.GEN_PATH); gen = importlib.util.module_from_spec(gs)
sys.modules[h.GEN_MODULE_NAME] = gen; gs.loader.exec_module(gen)
f2m, f2_hash = h.load_f2(); spl, spl_hash, spl_names = h.load_spline_ns()
wrapper_originals = h.install_wrapper_restoration_probe(spl)
h.install_exc_capture(spl); h.install_spline_call_telemetry(spl); h.install_nnls_test_injection(spl)
res["f2_hash"] = f2_hash; res["spl_hash"] = spl_hash
res["loader"] = dict(prelude_match=spl_names["prelude"] == h.AUTHORIZED_PRELUDE,
                     node_hash_entries=len(spl_names["node_hashes"]), executed_node_count=spl_names["executed_node_count"],
                     node_hashes=spl_names["node_hashes"], solver_b_function_hashes=spl_names["solver_b_function_hashes"])
grids = {fam: f2m.build_grid(fam)[1] for fam in ("P-01", "P-02")}
res["grid_sizes"] = {k: len(v) for k, v in grids.items()}
# manifest regeneration exactly as main() writes it (csv.writer, lineterminator LF, ascii), hashed in memory
rows = gen.manifest_rows()
buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(gen.MANIFEST_HEADER); w.writerows(rows)
man_bytes = buf.getvalue().encode("ascii")
man_hash = hashlib.sha256(man_bytes).hexdigest()
open("/home/claude/audit_ws/auditor/r3_manifest_regen.csv", "wb").write(man_bytes)
res["manifest_regen_sha256"] = man_hash
h._CODE_ENV_FINGERPRINT[0] = hashlib.sha256("|".join([
    res["harness_sha256"], res["generator_sha256"], man_hash, h.F2_HASH, h.SPL_HASH,
    platform.python_version(), np.__version__, scipy.__version__, platform.platform(),
    os.environ["OMP_NUM_THREADS"], os.environ["OPENBLAS_NUM_THREADS"], os.environ["MKL_NUM_THREADS"]]).encode()).hexdigest()[:16]
res["fingerprint_auditor_env"] = h._CODE_ENV_FINGERPRINT[0]
save(); log("setup done; manifest regen %s" % man_hash)

# NR gates: recorded, not asserted (platform-bound)
h.CURRENT_PHASE[0] = "nr_gates"
try:
    r1 = f2m.run_all_fixtures()
    def doc(records):
        return dict(records=records, self_tests=r1[1], construction_audit=r1[3], special_evidence=r1[4]["special_evidence"],
                    falsifiability=r1[4]["falsifiability"], rejections_outside_invalid_init=r1[4]["rejections_outside_invalid_init"])
    h_native = hashlib.sha256(f2m.canonicalize(doc(r1[0])).encode("utf-8")).hexdigest()
    with open(h.F2_TELEMETRY_PATH, newline="", encoding="utf-8") as f:
        frozen = list(csv.DictReader(f))
    tel_ok = (len(frozen) == len(r1[2]) and all(all(str(row.get(k)) == frozen[i][k] for k in frozen[i] if k != "wall_clock_seconds")
                                                for i, row in enumerate(r1[2])))
    sub = h.nr01_wrapper_adapter(f2m, grids); spliced = {k: False for k in sub}; hyb = []
    for r in r1[0]:
        fid = r["fixture_id"]
        if fid in sub:
            if not spliced[fid]:
                hyb.extend(sub[fid]); spliced[fid] = True
            continue
        hyb.append(r)
    h_hybrid = hashlib.sha256(f2m.canonicalize(doc(hyb)).encode("utf-8")).hexdigest()
    res["nr01"] = dict(native=h_native, hybrid=h_hybrid, executor_expected=h.F2_NR_HASH,
                       native_eq_expected=h_native == h.F2_NR_HASH, hybrid_eq_native=h_hybrid == h_native,
                       telemetry_fields_equal=tel_ok)
except Exception as e:
    res["nr01"] = dict(error=repr(e))
log("NR-01 done: " + json.dumps({k: v for k, v in res["nr01"].items() if k != "error"}))
try:
    ok, n = h.spline_nr(spl); res["nr_spl"] = dict(repr_exact_equal=bool(ok), rows=n)
except Exception as e:
    res["nr_spl"] = dict(error=repr(e))
res["calls_after_nr"] = len(h.SPLINE_TELEMETRY_CALLS); save(); log("NR-SPL done: " + json.dumps(res["nr_spl"]))

tmfe = h.t_mask_full_ext(f2m, grids); res["t_mask_full_ext"] = tmfe
import math
T = h.T
alt = [(-1.0) ** t for t in range(T)]; lin = [float(t) for t in range(T)]; const = [1.0] * T
mix = [math.sin(0.37 * t) + 0.25 * math.cos(1.7 * t) for t in range(T)]
acf_closed = h.acf_verify([("alternating", alt), ("linear", lin), ("constant_den0", const), ("mixed_trig", mix)])
res["acf_closed"] = acf_closed
xv = np.asarray(mix); xv = (xv - xv.mean()) / xv.std(ddof=0); th = (0.3, 0.7, 20.0, 20.0)
f_orig = f2m.make_objective_and_x("P-01", xv); f_mask = h.make_masked_moax(f2m, h.FULL_O)("P-01", xv)
pin_mask_full = float.hex(f_orig(th)) == float.hex(f_mask(th))
obs = np.arange(20, 120); pin_mask_le = h.make_masked_moax(f2m, obs)("P-01", xv)(th) <= f_orig(th)
fs_pad = h.feature_start_masked(f2m, "P-01", xv, obs)
js = int(min(j for j in obs if xv[j] == max(xv[k] for k in obs)))
pin_fs = fs_pad[2] == js and abs(fs_pad[0][0] - (js / 145.0 - 0.125)) == 0.0
res["pins"] = dict(mask_full=bool(pin_mask_full), mask_le=bool(pin_mask_le), fs=bool(pin_fs)); save()

h.CURRENT_PHASE[0] = "unit_tests"
a5 = h.a5_unit_tests(f2m, grids); ut_pd = h.ut_probe_decouple(f2m, grids); uset_ut = h.ut_uset_construction(gen)
comparator_nan = h.t_comparator_nan(); starts_full = h.fix_starts_full(f2m, grids, []); starts_dup = h.fix_starts_dup(f2m, grids, [])
log("unit tests A: done")
a5_true_tel = []; a5_true = h.fix_a5_true(f2m, spl, grids, a5_true_tel); log("FIX-A5-TRUE done")
exc_before = len(h.EXC_CAPTURES)
exc_fixture_results, exc_fixture_tel = h.run_exc_injection_fixtures(spl)
res["exc_injected_records_unit_phase"] = [dict(r, traceback=None) for r in h.EXC_CAPTURES[exc_before:]]
ut_unrel_ref = h.ut_exc_unrelated_reference(spl)
res.update(a5=a5, ut_probe_decouple=ut_pd, uset_construction=uset_ut, comparator_nan=comparator_nan,
           starts_full=starts_full, starts_dup=starts_dup, fix_a5_true=a5_true,
           exc_injection_fixtures=exc_fixture_results, ut_exc_unrelated_reference=ut_unrel_ref,
           calls_after_unit_tests=len(h.SPLINE_TELEMETRY_CALLS))
# wrapper chain depth after the exception fixtures (Y-04 (d) observation)
depth = 0; fn = spl["nnls"]
while getattr(fn, "__closure__", None):
    inner = [c.cell_contents for c in fn.__closure__ if callable(c.cell_contents)]
    if not inner: break
    fn = inner[0]; depth += 1
res["nnls_wrapper_depth_after_unit_tests"] = depth
save(); log("unit tests done; nnls wrapper depth %d" % depth)

a5_findings = []
def one_run(run_label):
    h.CURRENT_PHASE[0] = run_label
    telemetry, stops, evals, construction_audit = [], [], [], []
    full_mask_fits_all = {}
    for sc in gen.REAL_SCENARIOS:
        strata_recs, n_s, tel_part, ca_part, full_mask_fits = h.run_real_scenario(f2m, spl, grids, sc, run_label, a5_findings)
        fx_stops = []
        ev = h.evaluate_fixture(sc["fixture_id"], strata_recs, n_s, "REAL", {}, fx_stops)
        evals.append(ev); telemetry.extend(tel_part); construction_audit.extend(ca_part); stops.extend(fx_stops)
        for (sx, ti, fk), fit in full_mask_fits.items():
            full_mask_fits_all[(sc["fixture_id"], sx, ti, fk)] = fit
        log("%s %s done (calls %d)" % (run_label, sc["fixture_id"], len(h.SPLINE_TELEMETRY_CALLS)))
    for fx in gen.INJ_FIXTURES:
        force_pending = fx["fixture_id"] in gen.FORCE_C4_PENDING_FIXTURE_IDS
        evals.append(h.evaluate_fixture(fx["fixture_id"], fx["strata"], gen.N_INJ, "TEST_ONLY_INJECTION_DECISION_LAYER",
                                        fx["flags"], stops, force_c4_pending=force_pending))
    return evals, telemetry, stops, construction_audit, full_mask_fits_all
h.EXC_CAPTURES.clear()
evals1, telemetry1, stops1, ca1, full_mask_fits_run1 = one_run("run1")
exc_after_run1 = list(h.EXC_CAPTURES)
calls_after_run1 = len(h.SPLINE_TELEMETRY_CALLS); save()
evals2, telemetry2, stops2, ca2, _ = one_run("run2")
exc_after_run2 = list(h.EXC_CAPTURES)
h.GLOBAL_STOPS_REF[0] = stops1
expect_result = h.check_expectations(evals1, rows, gen.MANIFEST_HEADER)
res["expectation_checks"] = dict(declared=expect_result["declared"], ran=expect_result["ran"], fails=expect_result["fails"])
res["exc_captures_run1"] = [dict(r, traceback=None) for r in exc_after_run1]
res["exc_captures_run2_only"] = [dict(r, traceback=None) for r in exc_after_run2[len(exc_after_run1):]]
res["exc_traceback_run1"] = [r["traceback"] for r in exc_after_run1]

h.CURRENT_PHASE[0] = "residual_export"
residual_series, residual_link, acf_run = {}, {}, []
n_calls_before_export = len(h.SPLINE_TELEMETRY_CALLS)
for (fixture_id, sx, ti, fitter_tag), fit in sorted(full_mask_fits_run1.items(), key=lambda kv: kv[0]):
    if not fit["valid"]:
        continue
    key = f"{fixture_id}:{sx}{ti}"; resid = fit["x"] - fit["ghat"]
    residual_series[f"{key}:{fitter_tag}"] = [float(v).hex() for v in resid]
    residual_link[f"{key}:{fitter_tag}"] = dict(fitter=fitter_tag, fixture=fixture_id, sex=sx, trajectory=ti,
                                                mask_id="run1:%s%d:full" % (sx, ti),
                                                sha256=hashlib.sha256(np.asarray(resid, dtype="<f8").tobytes()).hexdigest())
    acf_run.extend(h.acf_verify([(f"{key}:{fitter_tag}", list(resid))]))
res["export_calls"] = len(h.SPLINE_TELEMETRY_CALLS) - n_calls_before_export
json.dump(residual_series, open("/home/claude/audit_ws/auditor/r3_full_repro_residuals.json", "w"), sort_keys=True, indent=1)
res["residual_link"] = residual_link; res["acf_run"] = acf_run

doc1 = dict(evals=evals1, stops=stops1, a5=a5, ut_probe_decouple=ut_pd, pins=dict(mask_full=pin_mask_full, fs=pin_fs))
doc2 = dict(evals=evals2, stops=stops2, a5=a5, ut_probe_decouple=ut_pd, pins=dict(mask_full=pin_mask_full, fs=pin_fs))
res["run1_canonical"] = h.canonical_hash(doc1); res["run2_canonical"] = h.canonical_hash(doc2)
res["determinism_same_process"] = res["run1_canonical"] == res["run2_canonical"]
res["fidelity"] = dict(declared=len(set(h.FIDELITY_DECLARED)), executed=len(set(h.FIDELITY_EXECUTED)))
h.uninstall_wrappers(spl, wrapper_originals)
res["wrapper_restore_ok"] = (spl["accept"] is wrapper_originals["accept"] and spl["minimize"] is wrapper_originals["minimize"]
                            and spl["nnls"] is wrapper_originals["nnls"])
from collections import Counter
res["calls_by_phase"] = dict(Counter(r["phase"] for r in h.SPLINE_TELEMETRY_CALLS))
res["calls_by_pid"] = dict(Counter(str(r["pid"]) for r in h.SPLINE_TELEMETRY_CALLS))
res["units_computed"] = dict(h.UNITS_COMPUTED_THIS_PROCESS); res["units_read"] = dict(h.UNITS_READ_FROM_STORE)
res["evals1"] = evals1; res["stops1"] = stops1; res["construction_audit1"] = ca1
res["mechanism_outcomes"] = {e["fixture_id"]: e["mechanism_outcome"] for e in evals1}
res["telemetry_rows_run1"] = len(telemetry1); res["a5_contract_violations"] = a5_findings
res["store_entries_written"] = len(os.listdir(h.RESTART_STORE_DIR)) if os.path.isdir(h.RESTART_STORE_DIR) else 0
save()
json.dump(h.canon(dict(mode_rows=telemetry1 + exc_fixture_tel + a5_true_tel, percall=h.SPLINE_TELEMETRY_CALLS)),
          open("/home/claude/audit_ws/auditor/r3_full_repro_telemetry.json", "w"))
log("RUN_COMPLETE_AUDITOR pid %d ; run1==run2 %s ; calls_by_phase %s" % (os.getpid(), res["determinism_same_process"], res["calls_by_phase"]))
```

Comparison script `r3_02_repro_compare.py` and its output:

```python
"""Evidence script 02 (F3 STEP-2 r3 independent audit, auditor claude-fable-5-1, 2026-09-24).
Compares the auditor's same-environment single-process reproduction (aud_r3_full_repro.py output) with the
executor's delivered results JSON (352791648b7c...), residual series (3ee624f3a3e0...), per-call telemetry
(9d0c627ebc59...) and mode-level telemetry (24f21811886c...). Every value printed here is computed from those
files; nothing is asserted about executor hashes. Cross-platform differences (Windows executor vs Linux auditor)
are reported, not adjudicated. Tier of everything below: [A-S] unless marked otherwise."""
import json, csv, hashlib, collections, os, sys
fh = lambda v: (float.fromhex(v) if isinstance(v, str) and v.startswith(("0x", "-0x")) else v)
AUD = "/home/claude/audit_ws/auditor"
RECV = "/home/claude/audit_r3/recv2"
A = json.load(open(f"{AUD}/r3_full_repro_out.json"))
R = json.load(open(f"{RECV}/f3_step2_results_r3_2026-09-22.json"))
RS = json.load(open(f"{RECV}/f3_step2_residual_series_r3_2026-09-22.json"))
AS = json.load(open(f"{AUD}/r3_full_repro_residuals.json"))
AT = json.load(open(f"{AUD}/r3_full_repro_telemetry.json"))
with open(f"{RECV}/f3_step2_spline_percall_telemetry_r3_2026-09-22.csv", newline="", encoding="utf-8") as f:
    EPC = list(csv.DictReader(f))
with open(f"{RECV}/f3_step2_telemetry_r3_2026-09-22.csv", newline="", encoding="utf-8") as f:
    EMODE = list(csv.DictReader(f))

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def j(o): return json.dumps(o, sort_keys=True)
print("== inputs ==")
for p in ("f3_step2_results_r3_2026-09-22.json", "f3_step2_residual_series_r3_2026-09-22.json",
          "f3_step2_spline_percall_telemetry_r3_2026-09-22.csv", "f3_step2_telemetry_r3_2026-09-22.csv"):
    print("  %s sha256=%s" % (p, sha(f"{RECV}/{p}")))
print("  auditor out json sha256=%s" % sha(f"{AUD}/r3_full_repro_out.json"))
print("  auditor residuals json sha256=%s" % sha(f"{AUD}/r3_full_repro_residuals.json"))

print("\n== 1. process / environment ==")
print("  auditor env:", A["env"], "| pid:", A["pid"], "| elapsed_s: %.0f" % fh(A["elapsed_s"]))
print("  executor env:", R["environment"], "| pid:", R["process"]["pid"], "| attempt_number:", R["process"]["attempt_number"])
print("  harness sha256 imported by auditor == delivered 5fea165c...:", A["harness_sha256"] == "5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77", A["harness_sha256"])
print("  generator sha256 imported by auditor == delivered cc23c9b5...:", A["generator_sha256"] == "cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8", A["generator_sha256"])
print("  manifest regenerated in memory sha256:", A["manifest_regen_sha256"], "== executor fixture_manifest_sha256:", A["manifest_regen_sha256"] == R["fixture_manifest_sha256"])
print("  F2 hash:", A["f2_hash"], "| SPL hash:", A["spl_hash"])
print("  fingerprint (auditor env, same formula as harness L2166-2171):", A["fingerprint_auditor_env"], "(differs from executor's 1ba561daefb48b2e by platform/python fields; informational)")
print("  restart store absent at start:", A["store_absent_at_start"], "| RESTART_LAYER_ACTIVE as delivered:", A["restart_layer_active_as_delivered"])
print("  units_computed (auditor process):", A.get("units_computed"), "| units_read (auditor process):", A.get("units_read"))
print("  executor units_computed_this_process:", R["process"]["units_computed_this_process"], "| units_read_from_store:", R["process"]["units_read_from_store"])
print("  store entries written by auditor process:", A.get("store_entries_written"))
print("  loader: prelude_match=%s node_hash_entries=%s executed_node_count=%s" % (A["loader"]["prelude_match"], A["loader"]["node_hash_entries"], A["loader"]["executed_node_count"]))
print("  executor spline_loader_nodes: executed_node_count=%s excluded_count=%s" % (R["spline_loader_nodes"]["executed_node_count"], R["spline_loader_nodes"]["excluded_count"]))
print("  grid sizes:", A["grid_sizes"])

print("\n== 2. platform-bound gates (recorded, not asserted) ==")
n = A["nr01"]
print("  NR-01 native canonical (auditor env):", n.get("native"), "| executor-expected:", n.get("executor_expected"), "| native==expected:", n.get("native_eq_expected"), "| hybrid==native:", n.get("hybrid_eq_native"), "| telemetry_fields_equal:", n.get("telemetry_fields_equal"))
print("  NR-SPL (auditor env):", A["nr_spl"], "| executor spline_nonregression:", R["spline_nonregression"])
print("  executor nr01.i passed:", R["nr01"]["i"]["passed"], "canonical:", R["nr01"]["i"]["canonical"], "| nr01.ii option:", R["nr01"]["ii"]["option"], "passed:", R["nr01"]["ii"]["passed"])

print("\n== 3. pins and unit tests (auditor env vs executor JSON) ==")
print("  pins (auditor):", A["pins"], "| executor t_mask_full_ext:", R["t_mask_full_ext"])
def cmp_block(name, a, r, drop=("note",)):
    a2 = {k: v for k, v in a.items() if k not in drop} if isinstance(a, dict) else a
    r2 = {k: v for k, v in r.items() if k not in drop} if isinstance(r, dict) else r
    eq = j(a2) == j(r2)
    print("  %-28s equal(excl. note)=%s" % (name, eq), "" if eq else "\n     auditor: %s\n     executor: %s" % (j(a2)[:600], j(r2)[:600]))
    return eq
cmp_block("a5_unit_tests", A["a5"], R["a5_unit_tests"])
cmp_block("ut_probe_decouple", A["ut_probe_decouple"], R["ut_probe_decouple"])
cmp_block("uset_construction", A["uset_construction"], R["uset_construction"])
cmp_block("comparator_nan", A["comparator_nan"], R["comparator_nan"])
cmp_block("starts_default(full)", A["starts_full"], R["starts_default"])
cmp_block("starts_dup", A["starts_dup"], R["starts_dup"])
cmp_block("fix_a5_true", A["fix_a5_true"], R["fix_a5_true"])
cmp_block("exc_injection_fixtures", A["exc_injection_fixtures"], R["exc_injection_fixtures"])
cmp_block("ut_exc_unrelated_reference", A["ut_exc_unrelated_reference"], R["ut_exc_unrelated_reference"])
print("  t_mask_full_ext (auditor):", A["t_mask_full_ext"])
print("  acf_closed (auditor): n=%d all bitwise_equal=%s" % (len(A["acf_closed"]), all(x.get("bitwise_equal") for x in A["acf_closed"])))
print("  exc records captured during the unit-test phase (auditor):", [(e.get("fixture"), e.get("mask_id"), e.get("stage"), e.get("kind"), e.get("exception_type")) for e in A["exc_injected_records_unit_phase"]])
print("  nnls wrapper depth after unit tests (auditor):", A["nnls_wrapper_depth_after_unit_tests"])
print("  wrapper_restore_ok (auditor, after uninstall):", A.get("wrapper_restore_ok"))

print("\n== 4. RUN1 / RUN2 in one auditor process ==")
print("  run1_canonical (auditor env):", A["run1_canonical"])
print("  run2_canonical (auditor env):", A["run2_canonical"], "| run1==run2 (same process):", A["determinism_same_process"])
print("  executor run1_canonical:", R["run1_canonical_sha256"], "| executor run2:", R["run2_canonical_sha256"], "| executor determinism flag:", R["determinism"])
print("  auditor run1_canonical == executor run1_canonical:", A["run1_canonical"] == R["run1_canonical_sha256"], "(cross-platform; informational)")
print("  fidelity (auditor):", A["fidelity"], "| executor:", R["fidelity"])
print("  a5_contract_violations (auditor):", A["a5_contract_violations"], "| executor:", R["a5_contract_violations"])
EA = {e["fixture_id"]: e for e in A["evals1"]}; ER = {e["fixture_id"]: e for e in R["evaluations"]}
print("  fixture id sets equal:", set(EA) == set(ER), "| n=%d" % len(ER))
inj = [k for k in ER if k.startswith("INJ-")]
same = [k for k in inj if j(EA[k]) == j(ER[k])]
print("  INJ fixtures: %d ; evaluation objects identical (auditor env vs executor JSON): %d" % (len(inj), len(same)), "| differing:", [k for k in inj if k not in same])
print("  mechanism outcomes (auditor):", collections.Counter(e["mechanism_outcome"] for e in A["evals1"]))
print("  mechanism outcomes (executor):", collections.Counter(e["mechanism_outcome"] for e in R["evaluations"]))
print("  stops identical (auditor run1 vs executor):", j(A["stops1"]) == j(R["stops"]), "| auditor stops:", [(s["fixture"], s["stop"]) for s in A["stops1"]])
print("  sexes field: auditor", collections.Counter(j(e.get("sexes")) for e in A["evals1"]), "| executor", collections.Counter(j(e.get("sexes")) for e in R["evaluations"]))
for fid in ("SCEN-A", "SCEN-B"):
    a, r = EA[fid], ER[fid]
    print("  %s: auditor p03=%s -> %s | executor p03=%s -> %s | c4_source %s/%s" % (fid, a["p03"], a["mechanism_outcome"], r["p03"], r["mechanism_outcome"], a["c4_source"], r["c4_source"]))
    for fam in sorted(a["p03_fields"]):
        da, dr = a["p03_fields"][fam], r["p03_fields"].get(fam)
        print("     p03_fields %-4s auditor=%s | executor=%s | equal=%s" % (fam, j(da)[:160], j(dr)[:160] if dr else None, j(da) == j(dr)))
    if a.get("dp04") or r.get("dp04"):
        print("     dp04 auditor:", j(a.get("dp04"))[:300]); print("     dp04 executor:", j(r.get("dp04"))[:300])
    # criteria: compare booleans and hex stats per family/criterion/sex
    nb = ne = nhex_eq = nhex_ne = 0; hex_ne_list = []
    for fam in sorted(set(a["criteria"]) | set(r["criteria"])):
        for crit in sorted(set(a["criteria"].get(fam, {})) | set(r["criteria"].get(fam, {}))):
            for sx in sorted(set(a["criteria"].get(fam, {}).get(crit, {})) | set(r["criteria"].get(fam, {}).get(crit, {}))):
                ca = a["criteria"].get(fam, {}).get(crit, {}).get(sx, {}); cr = r["criteria"].get(fam, {}).get(crit, {}).get(sx, {})
                for k in sorted(set(ca) | set(cr)):
                    va, vr = ca.get(k), cr.get(k)
                    if isinstance(va, bool) or isinstance(vr, bool) or va is None or vr is None or isinstance(va, int):
                        if va == vr: nb += 1
                        else: ne += 1; print("     BOOL/INT DIFF %s %s %s %s: auditor=%s executor=%s" % (fam, crit, sx, k, va, vr))
                    else:
                        if va == vr: nhex_eq += 1
                        else: nhex_ne += 1; hex_ne_list.append((fam, crit, sx, k, va, vr))
    print("     criteria booleans/ints equal=%d differing=%d | hex stats equal=%d differing=%d" % (nb, ne, nhex_eq, nhex_ne))
    for t in hex_ne_list[:12]:
        print("       hex diff %s %s %s %s: auditor=%s executor=%s (rel=%.3e)" % (t[0], t[1], t[2], t[3], t[4], t[5], abs(fh(t[4]) - fh(t[5])) / max(1e-300, abs(fh(t[5])))))
    if hex_ne_list:
        rels = [(abs(fh(t[4]) - fh(t[5])) / max(1e-300, abs(fh(t[5]))), t[:4]) for t in hex_ne_list]
        print("     hex stats relative difference: min=%.3e at %s ; max=%.3e at %s" % (min(rels)[0], min(rels)[1], max(rels)[0], max(rels)[1]))
    print("     disc_f3_03_complement equal:", j(a.get("disc_f3_03_complement")) == j(r.get("disc_f3_03_complement")), "| interpretation equal:", a.get("interpretation") == r.get("interpretation"))
print("  construction_audit (auditor):", [(c["fixture_id"], c["sex"], c.get("a5_support_size"), c.get("a5_i_L"), c.get("a5_i_R")) for c in A["construction_audit1"]])
print("  construction_audit (executor):", [(c["fixture_id"], c["sex"], c.get("a5_support_size"), c.get("a5_i_L"), c.get("a5_i_R")) for c in R["construction_audit"]])
print("  construction_audit identical:", j(A["construction_audit1"]) == j(R["construction_audit"]))

print("\n== 5. expectation checks (harness check_expectations, auditor run1 evals) ==")
print("  auditor: declared=%s ran=%s fails=%s" % (A["expectation_checks"]["declared"], A["expectation_checks"]["ran"], A["expectation_checks"]["fails"]))
print("  executor: declared=%s ran=%s EXPECTATION_FAIL=%s detail=%s" % (R["expectation_checks"]["declared"], R["expectation_checks"]["ran"], R["expectation_checks"]["EXPECTATION_FAIL"], R["expectation_checks"]["detail"]))

print("\n== 6. solver exception captures (Y-04 / Y-16) ==")
key = lambda e: (e.get("fixture"), e.get("sex"), e.get("mask_id"), e.get("mode"), e.get("stage"), e.get("kind"), e.get("exception_type"), (e.get("message") or "")[:60])
print("  auditor run1 captures:", [key(e) for e in A["exc_captures_run1"]])
print("  auditor run2-only captures:", [key(e) for e in A["exc_captures_run2_only"]])
print("  executor solver_exceptions:", [key(e) for e in R["solver_exceptions"]])
print("  run1 capture keys identical to executor solver_exceptions:", [key(e) for e in A["exc_captures_run1"]] == [key(e) for e in R["solver_exceptions"]])
for tb in A["exc_traceback_run1"]:
    lines = [ln.strip() for ln in tb.splitlines() if ln.strip().startswith("File ")]
    print("  auditor traceback frames:", [ln.split(",")[0].split("/")[-1].split("\\")[-1] + "," + ln.split(",")[1] for ln in lines])

print("\n== 7. per-call telemetry (auditor process) vs executor per-call CSV ==")
pc = AT["percall"]
print("  auditor per-call rows:", len(pc), "| calls_by_phase:", A["calls_by_phase"], "| calls_by_pid:", A["calls_by_pid"])
print("  auditor calls after NR=%s after unit tests=%s | export_calls=%s" % (A["calls_after_nr"], A["calls_after_unit_tests"], A["export_calls"]))
print("  executor per-call rows:", len(EPC), "| by phase:", dict(collections.Counter(r["phase"] for r in EPC)), "| by pid:", dict(collections.Counter(r["pid"] for r in EPC)))
print("  executor process.spline_telemetry_calls_by_phase:", R["process"]["spline_telemetry_calls_by_phase"], "| call_total:", R["process"]["spline_telemetry_call_total"])
print("  auditor per-call columns:", sorted(pc[0].keys()) if pc else None)
print("  executor per-call columns:", list(EPC[0].keys()) if EPC else None)
def seq(rows, phase):
    return [(r["fixture"], r["sex"], str(r["trajectory"]), r["mask_id"], str(r["mode"]), r["method"]) for r in rows if r["phase"] == phase]
for ph in ("run1", "run2"):
    sa, se = seq(pc, ph), seq(EPC, ph)
    print("  %s: auditor call sequence n=%d | executor n=%d | sequences identical (fixture,sex,traj,mask,mode,method): %s" % (ph, len(sa), len(se), sa == se))
    if sa != se and len(sa) == len(se):
        d = [i for i in range(len(sa)) if sa[i] != se[i]]
        print("     first differing positions:", d[:5], [(sa[i], se[i]) for i in d[:2]])
    sta = collections.Counter(str(r["status"]) for r in pc if r["phase"] == ph); ste = collections.Counter(r["status"] for r in EPC if r["phase"] == ph)
    print("     status counts auditor:", dict(sta), "| executor:", dict(ste))
    if len(sa) == len(se):
        ra = [r for r in pc if r["phase"] == ph]; re_ = [r for r in EPC if r["phase"] == ph]
        nit_eq = sum(1 for x, y in zip(ra, re_) if str(x.get("nit")) == y.get("nit")); nfev_eq = sum(1 for x, y in zip(ra, re_) if str(x.get("nfev")) == y.get("nfev"))
        obj_eq = sum(1 for x, y in zip(ra, re_) if str(x.get("objective")) == y.get("objective"))
        print("     positionwise equal: nit %d/%d, nfev %d/%d, objective(hex) %d/%d (cross-platform; informational)" % (nit_eq, len(ra), nfev_eq, len(ra), obj_eq, len(ra)))
print("  auditor rows in phases nr_gates/unit_tests/residual_export:", {ph: A["calls_by_phase"].get(ph, 0) for ph in ("nr_gates", "unit_tests", "residual_export")})
print("  executor rows in phases nr_gates/unit_tests/residual_export:", {ph: sum(1 for r in EPC if r["phase"] == ph) for ph in ("nr_gates", "unit_tests", "residual_export")})
mr = AT["mode_rows"]
print("  auditor mode-level rows (run1 + exc fixtures + FIX-A5-TRUE):", len(mr), "| executor mode-level CSV rows:", len(EMODE))
print("  auditor mode-level rows by fixture:", dict(collections.Counter(r.get("fixture") for r in mr)))
print("  executor mode-level rows by fixture:", dict(collections.Counter(r.get("fixture") for r in EMODE)))

print("\n== 8. RUN1 residual export (Y-21) ==")
print("  auditor residual keys: n=%d" % len(AS), sorted(AS))
print("  executor residual keys: n=%d" % len(RS), "| key sets equal:", set(AS) == set(RS))
eq_keys = [k for k in sorted(AS) if k in RS and AS[k] == RS[k]]
print("  per-key hex-series identical (auditor env vs executor): %d/%d" % (len(eq_keys), len(AS)), "| differing:", [k for k in sorted(AS) if k not in eq_keys])
for k in sorted(AS):
    if k in RS and AS[k] != RS[k]:
        va = [fh(v) for v in AS[k]]; vr = [fh(v) for v in RS[k]]
        print("     %s max|diff|=%.3e (len %d/%d)" % (k, max(abs(x - y) for x, y in zip(va, vr)), len(va), len(vr)))
print("  auditor residual_link fitters:", dict(collections.Counter(v["fitter"] for v in A["residual_link"].values())))
print("  acf_run (auditor): n=%d all bitwise_equal=%s" % (len(A["acf_run"]), all(x.get("bitwise_equal") for x in A["acf_run"])))
print("  export_calls (spline minimize calls during residual export, auditor):", A["export_calls"])
print("\nDONE r3_02_repro_compare")
```

```text
== inputs ==
  f3_step2_results_r3_2026-09-22.json sha256=352791648b7c3dc1151962905ec2270fe3ae4246846f2021c2dcda3e3dfe18fb
  f3_step2_residual_series_r3_2026-09-22.json sha256=3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f
  f3_step2_spline_percall_telemetry_r3_2026-09-22.csv sha256=9d0c627ebc5949e4b8e61c48e453d16c28ba61733047d737fcf3f8d2cb5a30fe
  f3_step2_telemetry_r3_2026-09-22.csv sha256=24f21811886c9aab3e2e57f649b0fa3d6964f729ae6978569f926fe32737d0d7
  auditor out json sha256=7e5c6ba8b59e966a331b90788d265b110572ca890f447ff683276c5abb6460a0
  auditor residuals json sha256=977e9a869e02cd6e64d1d5a635cbc0b1e0763d48ec1b9dafd708866d12730299

== 1. process / environment ==
  auditor env: {'numpy': '1.26.4', 'platform': 'Linux-6.18.44-fc-v37-x86_64-with-glibc2.39', 'python': '3.11.15', 'scipy': '1.14.1'} | pid: 532 | elapsed_s: 1792
  executor env: {'MKL': '1', 'OMP': '1', 'OPENBLAS': '1', 'numpy': '1.26.4', 'platform': 'Windows-10-10.0.19045-SP0', 'python': '3.11.7', 'scipy': '1.14.1'} | pid: 1240 | attempt_number: 5
  harness sha256 imported by auditor == delivered 5fea165c...: True 5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77
  generator sha256 imported by auditor == delivered cc23c9b5...: True cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8
  manifest regenerated in memory sha256: 9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a == executor fixture_manifest_sha256: True
  F2 hash: 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 | SPL hash: b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d
  fingerprint (auditor env, same formula as harness L2166-2171): 075e525c3b4c265b (differs from executor's 1ba561daefb48b2e by platform/python fields; informational)
  restart store absent at start: True | RESTART_LAYER_ACTIVE as delivered: True
  units_computed (auditor process): {'nr_gates': 0, 'residual_export': 0, 'run1': 0, 'run2': 0, 'unit_tests': 0} | units_read (auditor process): {'nr_gates': 0, 'residual_export': 0, 'run1': 0, 'run2': 0, 'unit_tests': 0}
  executor units_computed_this_process: {'nr_gates': 0, 'residual_export': 1, 'run1': 2, 'run2': 2, 'unit_tests': 0} | units_read_from_store: {'nr_gates': 1, 'residual_export': 0, 'run1': 0, 'run2': 0, 'unit_tests': 1}
  store entries written by auditor process: 11717
  loader: prelude_match=True node_hash_entries=73 executed_node_count=73
  executor spline_loader_nodes: executed_node_count=73 excluded_count=31
  grid sizes: {'P-01': 731, 'P-02': 261}

== 2. platform-bound gates (recorded, not asserted) ==
  NR-01 native canonical (auditor env): f07fdc828abcbf3c6207926ab69266e299014631edc0370893d6f518a6e0e584 | executor-expected: 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403 | native==expected: False | hybrid==native: True | telemetry_fields_equal: False
  NR-SPL (auditor env): {'repr_exact_equal': False, 'rows': 30} | executor spline_nonregression: {'passed': True, 'rows': 30}
  executor nr01.i passed: True canonical: 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403 | nr01.ii option: T-2a passed: True

== 3. pins and unit tests (auditor env vs executor JSON) ==
  pins (auditor): {'fs': True, 'mask_full': True, 'mask_le': True} | executor t_mask_full_ext: {'pass_': True}
  a5_unit_tests                equal(excl. note)=True 
  ut_probe_decouple            equal(excl. note)=True 
  uset_construction            equal(excl. note)=True 
  comparator_nan               equal(excl. note)=True 
  starts_default(full)         equal(excl. note)=True 
  starts_dup                   equal(excl. note)=True 
  fix_a5_true                  equal(excl. note)=True 
  exc_injection_fixtures       equal(excl. note)=True 
  ut_exc_unrelated_reference   equal(excl. note)=True 
  t_mask_full_ext (auditor): {'pass_': True}
  acf_closed (auditor): n=4 all bitwise_equal=True
  exc records captured during the unit-test phase (auditor): [('INJ-EXC-CAPTURE-S1', 'exc:s1', 1, 'COVERED', 'RuntimeError'), ('INJ-EXC-CAPTURE-S2', 'exc:s2', 2, 'COVERED', 'RuntimeError'), ('INJ-EXC-CAPTURE-S2', 'exc:s2', 1, 'COVERED', 'RuntimeError')]
  nnls wrapper depth after unit tests (auditor): 3
  wrapper_restore_ok (auditor, after uninstall): True

== 4. RUN1 / RUN2 in one auditor process ==
  run1_canonical (auditor env): a6310a0623619538cfd96d2540d072df4669781b3b143a779e0d9aca0ce92b7f
  run2_canonical (auditor env): a6310a0623619538cfd96d2540d072df4669781b3b143a779e0d9aca0ce92b7f | run1==run2 (same process): True
  executor run1_canonical: 7d40df6137e3b300a1cb92c4895a8ac4f0ff6f45f8c5669b3c2eb0ee22d42f57 | executor run2: 7d40df6137e3b300a1cb92c4895a8ac4f0ff6f45f8c5669b3c2eb0ee22d42f57 | executor determinism flag: True
  auditor run1_canonical == executor run1_canonical: False (cross-platform; informational)
  fidelity (auditor): {'declared': 5, 'executed': 5} | executor: {'declared': 5, 'executed': 5, 'implemented': 5}
  a5_contract_violations (auditor): [] | executor: []
  fixture id sets equal: True | n=34
  INJ fixtures: 32 ; evaluation objects identical (auditor env vs executor JSON): 32 | differing: []
  mechanism outcomes (auditor): Counter({'ONLY_P02_PASSES': 13, 'RESOLVED_MECHANISM_P01': 6, 'TERMINAL_FALLBACK_MECHANISM_P01': 5, 'STOP_BOTH_FAIL_REDESIGN': 4, 'MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-03)': 2, 'ONLY_P01_PASSES': 1, 'STOP_CONTRACT_VIOLATION_EMPTY_U': 1, 'STOP_CONTRACT_VIOLATION_INCONSISTENT_U': 1, 'MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING)': 1})
  mechanism outcomes (executor): Counter({'ONLY_P02_PASSES': 13, 'RESOLVED_MECHANISM_P01': 6, 'TERMINAL_FALLBACK_MECHANISM_P01': 5, 'STOP_BOTH_FAIL_REDESIGN': 4, 'MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-03)': 2, 'ONLY_P01_PASSES': 1, 'STOP_CONTRACT_VIOLATION_EMPTY_U': 1, 'STOP_CONTRACT_VIOLATION_INCONSISTENT_U': 1, 'MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING)': 1})
  stops identical (auditor run1 vs executor): True | auditor stops: [('SCEN-B', 'BOTH_FAIL_REDESIGN'), ('INJ-BOTH-FAIL', 'BOTH_FAIL_REDESIGN'), ('INJ-DP04-EMPTY-U', 'CONTRACT_VIOLATION_EMPTY_U'), ('INJ-U-POST-CONSTRUCTION-INVALID', 'CONTRACT_VIOLATION_INCONSISTENT_U'), ('INJ-NAN-STAT-SPL', 'BOTH_FAIL_REDESIGN'), ('INJ-P03-BOTHFAIL-C4PENDING', 'BOTH_FAIL_REDESIGN')]
  sexes field: auditor Counter({'{}': 34}) | executor Counter({'{}': 34})
  SCEN-A: auditor p03={'P01': 'PASS', 'P02': 'PASS'} -> RESOLVED_MECHANISM_P01 | executor p03={'P01': 'PASS', 'P02': 'PASS'} -> RESOLVED_MECHANISM_P01 | c4_source REAL/REAL
     p03_fields P01  auditor={"c4_status": "RESOLVED", "definite_failures": [], "first_failed_criterion": null, "p03_status": "PASS", "pending_criteria": []} | executor={"c4_status": "RESOLVED", "definite_failures": [], "first_failed_criterion": null, "p03_status": "PASS", "pending_criteria": []} | equal=True
     p03_fields P02  auditor={"c4_status": "RESOLVED", "definite_failures": [], "first_failed_criterion": null, "p03_status": "PASS", "pending_criteria": []} | executor={"c4_status": "RESOLVED", "definite_failures": [], "first_failed_criterion": null, "p03_status": "PASS", "pending_criteria": []} | equal=True
     dp04 auditor: {"consulted_path": ["C1", "C2", "C3", "C4a", "C4b", "C5"], "disclosure": [{"level": "C1", "outcome": "EQUIVALENT", "scalars": {"P01": "0x1.0000000000000p+0", "P02": "0x1.0000000000000p+0"}, "signed_delta": "0x0.0p+0", "tau": "0x1.47ae147ae147bp-7"}, {"level": "C2", "outcome": "EQUIVALENT", "per_sex"
     dp04 executor: {"consulted_path": ["C1", "C2", "C3", "C4a", "C4b", "C5"], "disclosure": [{"level": "C1", "outcome": "EQUIVALENT", "scalars": {"P01": "0x1.0000000000000p+0", "P02": "0x1.0000000000000p+0"}, "signed_delta": "0x0.0p+0", "tau": "0x1.47ae147ae147bp-7"}, {"level": "C2", "outcome": "EQUIVALENT", "per_sex"
     criteria booleans/ints equal=56 differing=0 | hex stats equal=44 differing=40
       hex diff P01 C2 F spline_stat: auditor=0x1.5f7a00c6ad494p-1 executor=0x1.5f7a00c6ad496p-1 (rel=3.235e-16)
       hex diff P01 C2 F stat: auditor=0x1.eb2a9dbdeb9a2p-1 executor=0x1.eb2a936cf465cp-1 (rel=3.205e-07)
       hex diff P01 C2 F threshold_FIXTURE_ONLY: auditor=0x1.45e0672d13afap-1 executor=0x1.45e0672d13afcp-1 (rel=3.489e-16)
       hex diff P01 C2 M spline_stat: auditor=0x1.e4d657cbed71bp-1 executor=0x1.e4d657cbed6f4p-1 (rel=4.572e-15)
       hex diff P01 C2 M stat: auditor=0x1.ec537facdf85ap-1 executor=0x1.ec538169d005bp-1 (rel=5.387e-08)
       hex diff P01 C2 M threshold_FIXTURE_ONLY: auditor=0x1.cb3cbe3253d81p-1 executor=0x1.cb3cbe3253d5ap-1 (rel=4.827e-15)
       hex diff P01 C3 F spline_stat: auditor=0x1.a56bc8b7294d3p-3 executor=0x1.a56bc8b7294bbp-3 (rel=3.237e-15)
       hex diff P01 C3 F stat: auditor=0x1.5fc2ff80dde0cp-5 executor=0x1.5fc3259e02705p-5 (rel=1.653e-06)
       hex diff P01 C3 F threshold_FIXTURE_ONLY: auditor=0x1.05e9178ec7d9dp-2 executor=0x1.05e9178ec7d91p-2 (rel=2.604e-15)
       hex diff P01 C3 M spline_stat: auditor=0x1.dffbf906783c8p-5 executor=0x1.dffbf906783a2p-5 (rel=4.500e-15)
       hex diff P01 C3 M stat: auditor=0x1.6e244ea721faep-4 executor=0x1.6e244ea633d37p-4 (rel=1.514e-10)
       hex diff P01 C3 M threshold_FIXTURE_ONLY: auditor=0x1.bccac95008eb1p-4 executor=0x1.bccac95008e9ep-4 (rel=2.428e-15)
     hex stats relative difference: min=3.235e-16 at ('P01', 'C2', 'F', 'spline_stat') ; max=1.453e-04 at ('P01', 'C4b', 'F', 'stat')
     disc_f3_03_complement equal: True | interpretation equal: True
  SCEN-B: auditor p03={'P01': 'FAIL', 'P02': 'FAIL'} -> STOP_BOTH_FAIL_REDESIGN | executor p03={'P01': 'FAIL', 'P02': 'FAIL'} -> STOP_BOTH_FAIL_REDESIGN | c4_source REAL/REAL
     p03_fields P01  auditor={"c4_status": "RESOLVED", "definite_failures": ["C2", "C3", "C5"], "first_failed_criterion": "C2", "p03_status": "FAIL", "pending_criteria": ["C4b"]} | executor={"c4_status": "RESOLVED", "definite_failures": ["C2", "C3", "C5"], "first_failed_criterion": "C2", "p03_status": "FAIL", "pending_criteria": ["C4b"]} | equal=True
     p03_fields P02  auditor={"c4_status": "RESOLVED", "definite_failures": ["C2", "C3", "C4a"], "first_failed_criterion": "C2", "p03_status": "FAIL", "pending_criteria": ["C4b"]} | executor={"c4_status": "RESOLVED", "definite_failures": ["C2", "C3", "C4a"], "first_failed_criterion": "C2", "p03_status": "FAIL", "pending_criteria": ["C4b"]} | equal=True
     criteria booleans/ints equal=70 differing=0 | hex stats equal=44 differing=18
       hex diff P01 C3 F spline_stat: auditor=0x1.853360ea60dafp-5 executor=0x1.853360ea60d4ap-5 (rel=1.475e-14)
       hex diff P01 C3 F stat: auditor=0x1.df896e2179d23p-4 executor=0x1.df896e38a16f9p-4 (rel=2.878e-09)
       hex diff P01 C3 F threshold_FIXTURE_ONLY: auditor=0x1.8f667d41fd3a4p-4 executor=0x1.8f667d41fd372p-4 (rel=7.116e-15)
       hex diff P01 C4b F spline_stat: auditor=0x1.3748c6fbb85fcp-1 executor=0x1.3748c6fbb8567p-1 (rel=2.721e-14)
       hex diff P01 C4b F stat: auditor=0x1.ed08491a69c7cp-7 executor=0x1.ed084d0976460p-7 (rel=1.217e-07)
       hex diff P01 C4b F threshold_FIXTURE_ONLY: auditor=0x1.6a7bfa2eeb92fp-1 executor=0x1.6a7bfa2eeb89ap-1 (rel=2.337e-14)
       hex diff P01 C5 M stat: auditor=0x1.89f9d772e20ddp-6 executor=0x1.89f9bd535cef6p-6 (rel=1.012e-06)
       hex diff P02 C2 F spline_stat: auditor=0x1.544cce9e4311ep-1 executor=0x1.544cce9e430f7p-1 (rel=6.515e-15)
       hex diff P02 C2 F stat: auditor=0x1.ec0c1bcb0c158p-1 executor=0x1.ec0c1bd6ff8b6p-1 (rel=1.448e-09)
       hex diff P02 C2 F threshold_FIXTURE_ONLY: auditor=0x1.3ab33504a9784p-1 executor=0x1.3ab33504a975dp-1 (rel=7.044e-15)
       hex diff P02 C3 F spline_stat: auditor=0x1.853360ea60dafp-5 executor=0x1.853360ea60d4ap-5 (rel=1.475e-14)
       hex diff P02 C3 F stat: auditor=0x1.0b78b48f39fa2p-3 executor=0x1.0b78b4ac94b0ep-3 (rel=6.541e-09)
     hex stats relative difference: min=6.515e-15 at ('P02', 'C2', 'F', 'spline_stat') ; max=2.434e-06 at ('P02', 'C5', 'F', 'stat')
     disc_f3_03_complement equal: False | interpretation equal: True
  construction_audit (auditor): [('SCEN-A', 'F', 42, False, False), ('SCEN-A', 'M', 54, False, False), ('SCEN-B', 'F', 41, False, False), ('SCEN-B', 'M', 32, False, False)]
  construction_audit (executor): [('SCEN-A', 'F', 42, False, False), ('SCEN-A', 'M', 54, False, False), ('SCEN-B', 'F', 41, False, False), ('SCEN-B', 'M', 32, False, False)]
  construction_audit identical: True

== 5. expectation checks (harness check_expectations, auditor run1 evals) ==
  auditor: declared=33 ran=33 fails=[]
  executor: declared=33 ran=33 EXPECTATION_FAIL=none detail=[]

== 6. solver exception captures (Y-04 / Y-16) ==
  auditor run1 captures: []
  auditor run2-only captures: []
  executor solver_exceptions: [('SCEN-A', 'F', 'run1:F0:full', 113, 2, 'COVERED', 'RuntimeError', 'Maximum number of iterations reached.')]
  run1 capture keys identical to executor solver_exceptions: False

== 7. per-call telemetry (auditor process) vs executor per-call CSV ==
  auditor per-call rows: 11489 | calls_by_phase: {'nr_gates': 60, 'run1': 5244, 'run2': 5244, 'unit_tests': 941} | calls_by_pid: {'532': 11489}
  auditor calls after NR=60 after unit tests=1001 | export_calls=0
  executor per-call rows: 10512 | by phase: {'run1': 5256, 'run2': 5256} | by pid: {'10920': 2659, '1240': 7853}
  executor process.spline_telemetry_calls_by_phase: {'run1': 5256, 'run2': 5256} | call_total: 10512
  auditor per-call columns: ['fixture', 'mask_id', 'message', 'method', 'mode', 'nfev', 'nit', 'njev', 'objective', 'phase', 'pid', 'sex', 'start_iso', 'status', 'trajectory', 'wall_clock_seconds']
  executor per-call columns: ['phase', 'pid', 'start_iso', 'fixture', 'sex', 'trajectory', 'mask_id', 'mode', 'method', 'status', 'message', 'nit', 'nfev', 'njev', 'wall_clock_seconds', 'objective']
  run1: auditor call sequence n=5244 | executor n=5256 | sequences identical (fixture,sex,traj,mask,mode,method): False
     status counts auditor: {'1': 4001, '0': 824, '2': 379, '8': 40} | executor: {'1': 4050, '2': 330, '0': 830, '8': 46}
  run2: auditor call sequence n=5244 | executor n=5256 | sequences identical (fixture,sex,traj,mask,mode,method): False
     status counts auditor: {'1': 4001, '0': 824, '2': 379, '8': 40} | executor: {'1': 4050, '2': 330, '0': 830, '8': 46}
  auditor rows in phases nr_gates/unit_tests/residual_export: {'nr_gates': 60, 'unit_tests': 941, 'residual_export': 0}
  executor rows in phases nr_gates/unit_tests/residual_export: {'nr_gates': 0, 'unit_tests': 0, 'residual_export': 0}
  auditor mode-level rows (run1 + exc fixtures + FIX-A5-TRUE): 5553 | executor mode-level CSV rows: 5553
  auditor mode-level rows by fixture: {'SCEN-A': 2464, 'SCEN-B': 2181, 'INJ-EXC-CAPTURE-S1': 146, 'INJ-EXC-CAPTURE-S2': 146, 'FIX-A5-TRUE': 616}
  executor mode-level rows by fixture: {'SCEN-A': 2464, 'SCEN-B': 2181, 'INJ-EXC-CAPTURE-S1': 146, 'INJ-EXC-CAPTURE-S2': 146, 'FIX-A5-TRUE': 616}

== 8. RUN1 residual export (Y-21) ==
  auditor residual keys: n=11 ['SCEN-A:F0:P01', 'SCEN-A:F0:P02', 'SCEN-A:F0:SPL', 'SCEN-A:M0:P01', 'SCEN-A:M0:P02', 'SCEN-A:M0:SPL', 'SCEN-B:F0:P01', 'SCEN-B:F0:P02', 'SCEN-B:F0:SPL', 'SCEN-B:M0:P01', 'SCEN-B:M0:P02']
  executor residual keys: n=11 | key sets equal: True
  per-key hex-series identical (auditor env vs executor): 0/11 | differing: ['SCEN-A:F0:P01', 'SCEN-A:F0:P02', 'SCEN-A:F0:SPL', 'SCEN-A:M0:P01', 'SCEN-A:M0:P02', 'SCEN-A:M0:SPL', 'SCEN-B:F0:P01', 'SCEN-B:F0:P02', 'SCEN-B:F0:SPL', 'SCEN-B:M0:P01', 'SCEN-B:M0:P02']
     SCEN-A:F0:P01 max|diff|=4.818e-06 (len 146/146)
     SCEN-A:F0:P02 max|diff|=2.614e-08 (len 146/146)
     SCEN-A:F0:SPL max|diff|=2.387e-15 (len 146/146)
     SCEN-A:M0:P01 max|diff|=2.407e-08 (len 146/146)
     SCEN-A:M0:P02 max|diff|=1.326e-08 (len 146/146)
     SCEN-A:M0:SPL max|diff|=2.665e-15 (len 146/146)
     SCEN-B:F0:P01 max|diff|=1.766e-08 (len 146/146)
     SCEN-B:F0:P02 max|diff|=8.154e-08 (len 146/146)
     SCEN-B:F0:SPL max|diff|=1.210e-14 (len 146/146)
     SCEN-B:M0:P01 max|diff|=3.300e-06 (len 146/146)
     SCEN-B:M0:P02 max|diff|=4.269e-07 (len 146/146)
  auditor residual_link fitters: {'P01': 4, 'P02': 4, 'SPL': 3}
  acf_run (auditor): n=11 all bitwise_equal=True
  export_calls (spline minimize calls during residual export, auditor): 0

DONE r3_02_repro_compare
```
