# p_konum_plus — F3 STEP-2 r4-1 — Independent Audit — DRAFT r1 (2026-09-30)

```text
record                  = f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md
record_class            = independent audit of the STEP-2 r4-1 correction revision (inside the r4 cycle), received
                          2026-09-30 in seven batches; child of the r4 audit DRAFT r1 (A-2, b7217027…) and DRAFT r2
                          (A-3, 9c16abb5…), which it does not rewrite
auditor                 = claude-opus-5-5 (Claude, Cowork session; the model the PI selected — the serving model may
                          differ). Not the executor. Decides nothing for the PI. Declares no QUALIFIED
reviewer_prior_exposure = true — this session drafted D-3, the r4 and r4-1 instructions, filled D-4, D-5 and D-6 at the
                          PI's written instructions and wrote A-1, A-2 and A-3. The closure actions checked here are
                          this session's own; agreement with them is not an independent derivation
other auditors' records = none received; none used
executor                = Claude Code, claude-opus-4-8[1m] as the executor reports (harness 4e0dc8cf… ; generator
                          68d126cf… ; manifest 5c09c4f0…)
dispatched instruments  = r4-1 instruction 283ac4e2… ; D-6 a92a0518… ; standing: r4 instruction e1283958… ; D-5
                          0cd87ad5… ; D-3 5b0e19ea… ; D-1 17187d31… ; D-2 da0c4064… ; inputs A-1 11cfa591…, A-2, A-3
frozen upstream         = untouched: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (as ratified by freeze record r1). Nothing
                          reopened; no scientific literal produced
evidence tiers          = [A] auditor-verified on the delivered bytes ; [A-S] auditor-environment execution of the
                          delivered code (Linux; Python 3.11.15, numpy 2.4.4, scipy 1.17.1 — never a claim about an
                          executor hash) ; [X] executor claim ; [E] external
honesty rule            = every hash here was computed by the auditor with the scripts of §9 or is quoted from a named
                          file; a check the auditor could not run is NOT PERFORMED
sidecar                 = external .sha256 ; no self-hash
```

## 0. Verdict

```text
audit_verdict                 = PASSED — no global and no gate-specific blocker is open on the delivered bytes.
                                PASSED is this record's audit vocabulary only: it is not QUALIFIED, not an
                                acceptance of the package and not a status change
global blockers               = 0
gate-specific blockers        = 0   (A-2's R4A-01 closed: §5, §6)
cleanup                       = 6   (R41A-01 … R41A-06)
informational                 = 5   (R41A-07 … R41A-11)
F3_STEP2_r4_status (executor) = PARTIAL_PENDING_PI — supported [A]; narrowed_evidence [T-R2-2] and the uncovered
                                row "A.5 (iii) inadmissible refit" keep it there (PI decisions, §7)
F3_STEP2 = QUALIFIED          = NOT declared (PI only)
```

In plain words. The r4-1 revision does what it was asked to do on the point that blocked r4. When the spline solver
fails in a way that cannot be verified, the decision rules now put the affected criteria on hold instead of
reporting a pass or a fail. The auditor checked this in two ways: the delivered decision layer, re-run in the
auditor's own environment, reproduces all 35 decision-layer evaluation objects and all stops byte for byte, twice
in one process; and a probe that drives the delivered real-path code with stand-in numerical engines shows that a
natural (not injected) solver event in the full, fold or probe context of a trajectory puts exactly the dependent
criteria on hold with the tag F3-STEP2-EXACT-04, and never produces a definite outcome (§5). Nothing else moved:
all 34 evaluation objects shared with r4 are byte-identical to r4's, the only changed stop record is the corrected
de-duplicated one, the provenance chain from the delivered bytes to every stored unit is complete, and
the executor's own counts (36/36 expectations, 28 recorded tests all passed, 64 coverage rows, RUN1 canonical
556106e7…) check out.

Six cleanup items remain, none of which touches a delivered outcome. The most substantive one is latent: on the
real path, a deliberately injected (test-only) unverifiable event is treated as an ordinary failure rather than
put on hold, contrary to D-3 Y-04 (b). No fixture in this package can reach that path, and real SSA data contain
no test injections, so no result is affected; it should still be fixed (R41A-01). The others are records that
were not preserved or not completed: the custody records of the first two attempts and the console logs of one
launch were overwritten (disclosed by the executor in its supplement), the report's hash block and the second erratum are
incomplete, the end-state block names the parent dispatch record instead of D-6, and the report misdescribes the
corrected stop record.

## 1. Custody at reception [A]

Received 2026-09-30 in seven batches: 68 file instances, 58 distinct name-and-content pairs, no name with two
different contents (§9 block [1]). Every one of the 25 files of the transmission list (31b27c28…) arrived with the
listed hash, and every one of their 25 sidecars plus the list's own sidecar states the listed hash. The supplement
(0b3f4358…), the attempt-2 store listing (8dfbe9e6…) and the reconstructed attempt-1 harness (b22708d2…) equal
their sidecars. The four instrument copies the executor forwarded (r4-1 instruction, D-6, A-2, A-3) are
byte-identical to the auditor's.

| deliverable | file | SHA256 |
|---|---|---|
| 1 harness | f3_step2_adequacy_harness_r4-1_2026-09-29.py | 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f |
| 2 generator | f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3 manifest | f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4 custody (W-3, attempt 3) | f3_step2_r4-1_preexecution_custody_2026-09-29.md | 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d |
| 5 telemetry | f3_step2_telemetry_r4-1_2026-09-29.csv | 85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167 |
| 6 results | f3_step2_results_r4-1_2026-09-29.json | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 |
| 7 residual series | f3_step2_residual_series_r4-1_2026-09-29.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 test evidence | f3_step2_test_evidence_r4-1_2026-09-29.json | f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd |
| 9 register | f3_step2_class_c_pin_register_r4-1_2026-09-29.md | 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 |
| 10 correction report | f3_step2_correction_report_r4-1_2026-09-29.md | e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e |
| 11 start-state inventory | f3_step2_r4-1_start_state_inventory_2026-09-29.md | fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 |
| 12 attempt log | f3_step2_r4-1_attempt_log_2026-09-29.md | ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 |
| A per-call telemetry | f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv | 22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88 |
| B store manifest | f3_step2_r4-1_restart_store_manifest_2026-09-29.csv | cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1 |
| C non-regression CSV | f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |

The run logs of the final launch (stdout 77120f5b…, stderr 9b678df6…), the attempt-1 and attempt-2 notes, logs and
harness bytes, and the annotation note (3adbd089…) are in §9 block [1] with their hashes.

## 2. Which bytes ran [A]

```text
fingerprint formula (harness) on the delivered triple and the executor environment = dc228827920a9633
     = custody record code_env_fingerprint = the ONLY prefix of the 11,869 units of the final store
store pids: 22616 (7,271 units, start 2026-09-29T22:14:16) and 7972 (4,598 units, start 2026-09-30T12:44:02) —
     launches 3 and 4 of the attempt log; per-call telemetry carries exactly these two pids with the phase split
     of the process block (nr_gates, unit_tests, run1 by 22616; run2 by 7972)
every launch verifies the custody record by assertion before computing anything (harness L2745–2764), so the
     units of launch 3, whose console logs were not preserved, were computed after that check passed
attempt 2 (quarantined): all 11,869 units carry b6fc376b049c20e1 = fp of the reconstructed attempt-2 bytes
     28086989… — the run itself wrote that key, so the reconstruction is proven on run-time evidence
attempt 1: fp of the reconstructed bytes b22708d2… = 4c776ba53e4fbe9c, the value the attempt-1 note records; no
     run-time record exists (restart layer off, no store, custody record not preserved) — [X]
revision changes: attempt 1 -> 2 = 8 lines, all revision constants; attempt 2 -> 3 = 20 lines, 6 revision
     constants and 14 lines of the non-regression self-check only (§9 block [2] [4])
unit names of the final and the attempt-2 store = the r4 store's unit names (the three new fixtures are
     decision-layer only and add no fit)
manifest regenerated from the delivered generator with the harness's own writer = 5c09c4f0… byte-identical
canonical RUN1 document recomputed from the delivered results = 556106e7c4609ade… = results.run1_canonical_sha256
```

So every unit of the final output was computed by the delivered bytes after the custody check, and the delivered
RUN1 content is the content that was hashed. RUN1 and RUN2 were computed by different processes (22616, 7972);
their equality is the executor's measurement [X], and the report words it without a same-process claim.

## 3. Checklist

| # | check | executor claim | auditor result |
|---|---|---|---|
| C-01 | 25 listed files + 26 sidecars received and equal to the list; supplement files equal to their sidecars | equal | PASS [A] |
| C-02 | custody record's observed instrument hashes = the auditor's copies (10 instruments) | EQUAL ×9 | PASS [A] (10 / 10, D-1 and D-2 included) |
| C-03 | delivered triple = executed bytes (fingerprint; store prefix; pids) | implied | PASS [A] (§2) |
| C-04 | manifest regenerated byte-identical | 5c09c4f0… | PASS [A] |
| C-05 | canonical RUN1 content = claimed hash | 556106e7… | PASS [A] |
| C-06 | RUN1 == RUN2 | true | [X]; two processes, disclosed as such |
| C-07 | T-EXPECT-ALL re-done from the manifest | 36 / 36 | PASS [A] (36 declared, 0 mismatches) |
| C-08 | R4A-01 decision grammar: fold → C2, full → C3 and C4b, probe → C4b, C4a never; the three new fixtures; evaluation-level assertion | PASS | PASS [A] (code L1283–1386) and [A-S] (35 / 35 objects; pending cells exactly as declared) |
| C-09 | R4A-01 real path, natural event: flag set in the right context; criteria routed to STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04); the event opens EXACT-04 | no end-to-end test | PASS [A-S] (probe, §5.2) and [A] (L3082–3088) |
| C-10 | R4A-01 real path, injected UNRELATED event routed to STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED) | excluded by design | FAIL, latent (unreachable in this manifest) — R41A-01 |
| C-11 | R4A-01 (f) non-regression against r4 | 0 findings | PASS [A]: 33 identical, 1 expected change (stop record), 3 new; all 34 shared evaluation objects byte-identical to r4's |
| C-12 | R4A-02 coverage: the four r4 rows resolve from evidence that ran and passed; only A.5 (iii) uncovered | 64 rows, 0 downgraded | PASS [A] (named fixtures pass C2 and C3 in both families and sexes; T-COMPARATOR-NAN and T-CALLCOUNT passed) |
| C-13 | R4A-03 labels and pairs | closed | PASS [A] (L1771; TEST_ONLY_INJECTED at L1074) and [A-S]; narrative — R41A-06 |
| C-14 | R4A-04 (i) inventory, (ii) r3 triples, (iii) report hash block | closed | (i) (ii) PASS [A]; (iii) PARTIAL — R41A-04 |
| C-15 | R4A-10 ERRATUM-2, annotation note, NOT_PRESERVED search, r4 report §8 (c) corrected | closed | PARTIAL — R41A-05; the search result is [X] |
| C-16 | per-call telemetry by phase and pid = process block; RUN1 = RUN2 row counts; store pids | 12,174 | PASS [A] (mode-level run1 = run2 = 4,645) |
| C-17 | residual series | = r4 export | PASS [A] (byte-identical, 3ee624f3…) |
| C-18 | end-state fields computed; PI_dispatch_record_hash | D-5 | fields PASS [A]; hash PARTIAL — R41A-03 |
| C-19 | register child of the r4 register; D-6 cited | stated | PASS [A] |
| C-20 | superseded bytes of this revision | reconstructed | attempt 2 PASS [A] (store keys); attempt 1 [X] — R41A-02 |
| C-21 | custody records of attempts 1–2; logs of launch 3 | NOT_PRESERVED | disclosed [A]; R41A-02 |
| C-22 | parents unchanged: the 13 r4 package files | true | PASS [A] (inventory §2 = the auditor's r4 bytes) |
| C-23 | no real data; no QUALIFIED claim; no new scientific literal | asserted | PASS [A] (real_data_access false; the report mentions QUALIFIED only to say the executor cannot declare it; register literal count 0) |
| C-24 | end state PARTIAL_PENDING_PI | as D-6 §5 expected | PASS as status |

## 4. Findings

| id | classification | finding | gate effect | closure action | authority |
|---|---|---|---|---|---|
| R41A-01 | cleanup (latent) | On the real path the three spline-pending flags are set only when the failure string lacks TEST_ONLY (L1927–1929, L1954–1955, L1966–1967); the harness comment justifies this as a declared ordinary failure, but the declared spline-failure injection returns a different string (TEST_ONLY_INJECTION_SPLINE_FAILURE, no STOP prefix, L976), so the clause only removes injected UNRELATED events. Probe (§5.2): an injected UNRELATED event in F0 full gives C3 and C4b of F a definite FAIL, p03 (FAIL, FAIL) and BOTH_FAIL_REDESIGN. D-3 Y-04 (b) requires such an event to stop its path as STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED), and the r4-1 instruction R4A-01 (c) asks for the tag "TEST_ONLY_INJECTED for a manifest-declared injection (not entered)". The routing tag is also taken from c4_source (L1283–1285), not from the event | none: no REAL_SCENARIOS entry carries an UNRELATED injection (§5.2), the only one is armed around a direct fit_spline call in T-EXC-UNRELATED-TYPE (L2333–2337), and real SSA data contain no test injection; natural events route correctly | drop the TEST_ONLY clause in the three flag assignments, take the routing tag from the event's own failure string, and add one real-path test with an injected UNRELATED event (the stub technique of §5.2 suffices) | X |
| R41A-02 | cleanup | Custody of the superseded attempts of this revision: (a) the W-3 records of attempts 1 and 2 were overwritten on the fixed custody path and are NOT_PRESERVED, so SUPERSEDES_CUSTODY_SHA256 = None; (b) the harness was edited in place before the quarantine copy, against the r4-1 instruction §4 ("copy BEFORE any edit"), so the attempt-1 and attempt-2 bytes are reconstructions — attempt 2 proven [A] by its store keys, attempt 1 resting on executor records only [X]; (c) launch 3's console logs were overwritten by launch 4 (same redirection target) and are NOT_PRESERVED, while its computational provenance survives [A] (7,271 store units and 6,918 per-call rows under pid 22616, custody asserted before computing). All three were disclosed by the executor in the supplement | none on any delivered output | from the next cycle: one custody file per attempt (attempt-numbered name) with SUPERSEDES_CUSTODY_SHA256 filled; copy the harness to quarantine before the first edit; one log file pair per launch | X |
| R41A-03 | cleanup | The end-state block records PI_dispatch_record_hash = 0cd87ad5… (D-5); the r4-1 instruction §6 asks for "PI_dispatch_record_hash = the hash of D-6 as observed". D-6's hash (a92a0518…) appears in no machine-written output (results, test evidence, stdout); report §10 discloses the choice | none | the next revision's end state names its own dispatch record | X |
| R41A-04 | cleanup | R4A-04 (iii) not completed: the report's hash block still gives the register, the start-state inventory and the attempt log as sidecar references instead of their hashes (45a10494…, fedd964a…, ee5b4862…; none of the three cites the report's hash, so nothing circular prevents printing them). For the report itself the reference is correct (no self-hash) | none | print the three hashes | X |
| R41A-05 | cleanup | R4A-10 partly completed: ERRATUM-2 states points (a)–(c) and corrects the r4 report §8 (c), but point (d) — the r3 log's rows 6–8 name revision 4 = f882b922… while the revision-4 custody record names 390f42b7… — appears in no r4-1 record (report, register, attempt log, inventory, annotation note, supplement); ERRATUM-2 cites neither the r3 attempt log hash (25316389…) nor item 3 of the r4 log's erratum ("matching no combination named in any r3 file") as the statement it corrects | none | add (d) and the two references in the next record child | X |
| R41A-06 | cleanup | Report §4 describes the corrected stop of INJ-U-POST-CONSTRUCTION-INVALID as "one deduped pair {sex:F,fitter:P01,obs:0}" (the register says the same); the delivered record — reproduced [A-S] — lists two pairs, (F, P01, 0) and (M, P01, 0), under a record whose sex field is F. The code lists every offending pair of the level across both sexes and keeps the first hit's sex as the record's (L1713–1725), so the data follow the code; the narrative is wrong | none | correct the two descriptions; state that the record's sex is the first hit's | X |
| R41A-07 | informational | The r4 store was left in place, not quarantined. Here the r4-1 instruction contradicts itself: §4 says quarantine the r4 store directory whole, §7 forbids moving r4 files. The executor followed §7 and disclosed it in the custody record; no r4 unit is readable under dc228827… (prefix mismatch) and the r4 store manifest (f3c923b1…) lists its content. The defect is the drafter's (this session) | none | none | — |
| R41A-08 | informational | The criterion states of the three new fixtures are predeclared in the manifest prose and in the harness test (T-EXC-UNRELATED-TYPE expected mapping), not in expected_* columns, which hold only p03 and the mechanism; the manifest has no column for criterion states. T-NONREG-R4 is not on MANDATORY_TESTS (L219–228) but asserts and halts the run on failure (attempt 2) | none | optional: add a criterion-state expectation column | X (optional) |
| R41A-09 | informational | The attempt-2 store listing is written with CRLF line endings (11,870 CR bytes); every deliverable is LF | none | none | — |
| R41A-10 | informational | Models: the executor reports claude-opus-4-8[1m] for r4-1; this record is written by claude-opus-5-5. The auditor environment for [A-S] (Python 3.11.15, numpy 2.4.4, scipy 1.17.1) differs from the executor's; the decision layer nevertheless reproduces byte for byte | none | none | — |
| R41A-11 | informational | Real-fit re-execution [A-S] NOT PERFORMED: the fit code is unchanged apart from the tag string at L1074 (§9 block [6]: fit_family and the statistics pins unchanged; run_real_scenario changes only the flag recording), the residual export is byte-identical to r4's, all 34 shared evaluation objects (fits included) are byte-identical to r4's, and A-1 §7 holds the r3 real-fit re-execution; the new real-path control flow was exercised by the stub probe of §5.2 instead | none | on request, a child revision with a full re-execution | — |

## 5. Auditor execution [A-S]

### 5.1 Decision layer

The script r41_03_decision_layer_repro.py (§9) imports the unmodified harness and generator from the auditor's
repository mirror, evaluates all 35 decision-layer fixtures twice in one process and calls the pure unit tests.
main() is not called.

```text
harness sha256: 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f
generator sha256: 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
decision-layer fixtures: 35 | pass1 == pass2 (same process): True | fixture data changed by pass 1: False
identical to the executor's evaluation objects: 35 / 35 | differing: []
INJ stops identical to the executor's: True [('INJ-BOTH-FAIL', 'BOTH_FAIL_REDESIGN'), ('INJ-DP04-EMPTY-U', 'CONTRACT_VIOLATION_EMPTY_U'), ('INJ-U-POST-CONSTRUCTION-INVALID', 'CONTRACT_VIOLATION_INCONSISTENT_U'), ('INJ-NAN-STAT-SPL', 'BOTH_FAIL_REDESIGN'), ('INJ-P03-BOTHFAIL-C4PENDING', 'BOTH_FAIL_REDESIGN')]
INCONSISTENT_U stop record (auditor run): [{'fixture': 'INJ-U-POST-CONSTRUCTION-INVALID', 'level': 'C2', 'member': 0, 'offending_pairs': [{'fitter': 'P01', 'observation': 0, 'sex': 'F'}, {'fitter': 'P01', 'observation': 0, 'sex': 'M'}], 'sex': 'F', 'stop': 'CONTRACT_VIOLATION_INCONSISTENT_U'}]
  INJ-SPL-PENDING-FULL   pending cells ['P01:C3:F', 'P01:C4b:F', 'P02:C3:F', 'P02:C4b:F'] | expected ['P01:C3:F', 'P01:C4b:F', 'P02:C3:F', 'P02:C4b:F'] | C4a F passed True | p03 ('PENDING', 'PENDING') | mech MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)
  INJ-SPL-PENDING-FOLD   pending cells ['P01:C2:F', 'P02:C2:F'] | expected ['P01:C2:F', 'P02:C2:F'] | C4a F passed True | p03 ('PENDING', 'PENDING') | mech MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)
  INJ-SPL-PENDING-PROBE  pending cells ['P01:C4b:F', 'P02:C4b:F'] | expected ['P01:C4b:F', 'P02:C4b:F'] | C4a F passed True | p03 ('PENDING', 'PENDING') | mech MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)
t_a5_support equal to delivered: True | pass: True
t_comparator_nan equal to delivered: True | pass: True | label: STOP_CONTRACT_VIOLATION_INCONSISTENT_U
ut_uset_construction equal to delivered: True | cases ok: {'a': True, 'b': True, 'c': True, 'd': True, 'e': True}
guard: {'0.5': True, 'nan': False, 'inf': False, 'None': False}
```

### 5.2 Real path with stand-in engines (R4A-01, natural and injected events)

The script r41_04_realpath_probe.py calls the unmodified run_real_scenario and evaluate_fixture on the generator's
REAL_SCENARIOS, with fit_family and fit_spline replaced by stubs: family fits always eligible; spline fits valid
except in the contexts a case names, where the stub returns the failure string the real fit_spline returns after an
UNRELATED event (L1074–1075), and the real fit_spline's return for a declared injected failure when asked for one.
The numbers the stubs produce mean nothing; the probe tests which failures set a pending flag and how the flags
are routed with c4_source = REAL.

```text
harness sha256: 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f
REAL_SCENARIOS: {'SCEN-A': (1, []), 'SCEN-B': (1, [(('F', 0), 'P-01', 'fold2', 'F2_FAULT_INJECTION'), (('M', 0), 'P-02', 'probeL', 'F2_FAULT_INJECTION'), (('F', 0), 'P-02', 'fold0', 'TEST_ONLY_INJECTION'), (('M', 0), 'SPL', 'full', 'TEST_ONLY_INJECTION'), (('M', 0), 'SPL', 'fold1', 'TEST_ONLY_INJECTION')])}

[SCEN-A] baseline (no event)
  flags: {'F': {'full': [False], 'fold': [False], 'probe': [False]}, 'M': {'full': [False], 'fold': [False], 'probe': [False]}} | SPL full: {'F': [True], 'M': [True]} | SPL cc: {'F': [True], 'M': [True]}
  pending cells: none
  p03: ('PASS', 'PASS') | mechanism: TERMINAL_FALLBACK_MECHANISM_P01 | stops: []
  C2/C3/C4b definite outcomes: ['P01:C2:F=PASS', 'P01:C2:M=PASS', 'P01:C3:F=PASS', 'P01:C3:M=PASS', 'P01:C4b:F=PASS', 'P01:C4b:M=PASS', 'P02:C2:F=PASS', 'P02:C2:M=PASS', 'P02:C3:F=PASS', 'P02:C3:M=PASS', 'P02:C4b:F=PASS', 'P02:C4b:M=PASS']

[SCEN-A] natural event, F0 full
  flags: {'F': {'full': [True], 'fold': [False], 'probe': [False]}, 'M': {'full': [False], 'fold': [False], 'probe': [False]}} | SPL full: {'F': [False], 'M': [True]} | SPL cc: {'F': [True], 'M': [True]}
  pending cells: ['P01:C3:F=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)', 'P01:C4b:F=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)', 'P02:C3:F=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)', 'P02:C4b:F=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)']
  p03: ('PENDING', 'PENDING') | mechanism: MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops: []

[SCEN-A] natural event, F0 fold2
  flags: {'F': {'full': [False], 'fold': [True], 'probe': [False]}, 'M': {'full': [False], 'fold': [False], 'probe': [False]}} | SPL full: {'F': [True], 'M': [True]} | SPL cc: {'F': [False], 'M': [True]}
  pending cells: ['P01:C2:F=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)', 'P02:C2:F=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)']
  p03: ('PENDING', 'PENDING') | mechanism: MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops: []

[SCEN-A] natural event, M0 probeL
  flags: {'F': {'full': [False], 'fold': [False], 'probe': [False]}, 'M': {'full': [False], 'fold': [False], 'probe': [True]}} | SPL full: {'F': [True], 'M': [True]} | SPL cc: {'F': [True], 'M': [True]}
  pending cells: ['P01:C4b:M=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)', 'P02:C4b:M=STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)']
  p03: ('PENDING', 'PENDING') | mechanism: MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops: []

[SCEN-A] injected UNRELATED event, F0 full
  flags: {'F': {'full': [False], 'fold': [False], 'probe': [False]}, 'M': {'full': [False], 'fold': [False], 'probe': [False]}} | SPL full: {'F': [False], 'M': [True]} | SPL cc: {'F': [True], 'M': [True]}
  pending cells: none
  p03: ('FAIL', 'FAIL') | mechanism: STOP_BOTH_FAIL_REDESIGN | stops: ['BOTH_FAIL_REDESIGN']
  C2/C3/C4b definite outcomes: ['P01:C2:F=PASS', 'P01:C2:M=PASS', 'P01:C3:F=FAIL', 'P01:C3:M=PASS', 'P01:C4b:F=FAIL', 'P01:C4b:M=PASS', 'P02:C2:F=PASS', 'P02:C2:M=PASS', 'P02:C3:F=FAIL', 'P02:C3:M=PASS', 'P02:C4b:F=FAIL', 'P02:C4b:M=PASS']

[SCEN-A] injected UNRELATED event, F0 fold2
  flags: {'F': {'full': [False], 'fold': [False], 'probe': [False]}, 'M': {'full': [False], 'fold': [False], 'probe': [False]}} | SPL full: {'F': [True], 'M': [True]} | SPL cc: {'F': [False], 'M': [True]}
  pending cells: none
  p03: ('FAIL', 'FAIL') | mechanism: STOP_BOTH_FAIL_REDESIGN | stops: ['BOTH_FAIL_REDESIGN']
  C2/C3/C4b definite outcomes: ['P01:C2:F=FAIL', 'P01:C2:M=PASS', 'P01:C3:F=PASS', 'P01:C3:M=PASS', 'P01:C4b:F=PASS', 'P01:C4b:M=PASS', 'P02:C2:F=FAIL', 'P02:C2:M=PASS', 'P02:C3:F=PASS', 'P02:C3:M=PASS', 'P02:C4b:F=PASS', 'P02:C4b:M=PASS']

[SCEN-B] declared spline failure only (manifest)
  flags: {'F': {'full': [False], 'fold': [False], 'probe': [False]}, 'M': {'full': [False], 'fold': [False], 'probe': [False]}} | SPL full: {'F': [True], 'M': [False]} | SPL cc: {'F': [True], 'M': [False]}
  pending cells: none
  p03: ('FAIL', 'FAIL') | mechanism: STOP_BOTH_FAIL_REDESIGN | stops: ['BOTH_FAIL_REDESIGN']
  C2/C3/C4b definite outcomes: ['P01:C2:F=PASS', 'P01:C2:M=FAIL', 'P01:C3:F=PASS', 'P01:C3:M=FAIL', 'P01:C4b:F=PASS', 'P01:C4b:M=FAIL', 'P02:C2:F=PASS', 'P02:C2:M=FAIL', 'P02:C3:F=PASS', 'P02:C3:M=FAIL', 'P02:C4b:F=PASS', 'P02:C4b:M=FAIL']
```

Reading. A natural event in F0 full, F0 fold2 or M0 probeL sets exactly the flag of that context and sex; the
dependent criteria of that sex go to STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04) for both families; p03 is
(PENDING, PENDING), the mechanism is undetermined with the EXACT-04 tag, no stop is written and D-P04 is not
reached — the closure action of R4A-01 holds on the real path. The same events injected as TEST_ONLY set no flag
and end in definite failures (R41A-01). SCEN-B's manifest-declared spline failure stays an ordinary failure, as
D-5 pins it.

## 6. Closure map (A-2 / A-3 findings in the scope of D-6 §3)

| item | executor claim | auditor result |
|---|---|---|
| R4A-01 (blocker) | CLOSED | CLOSED — decision grammar [A] [A-S]; real path for natural events [A-S] (§5.2); latent residue for injected events — R41A-01 |
| R4A-01 (f) | CLOSED | CLOSED [A] |
| R4A-02 | CLOSED | CLOSED [A] |
| R4A-03 | CLOSED | CLOSED [A] [A-S]; narrative — R41A-06 |
| R4A-04 | CLOSED | (i) (ii) CLOSED [A]; (iii) OPEN — R41A-04 |
| R4A-10 | CLOSED | (a)–(c), annotation note and §8 (c) correction CLOSED [A]; (d) and the references OPEN — R41A-05; NOT_PRESERVED search [X] |
| R4A-08 | NOT APPLIED | as scoped by the PI (D-6 §3) |
| R4A-05 … R4A-07, R4A-09 | — | unchanged (A-2, A-3) |

## 7. Register (S / T / X) and status

```text
S  none open. S-R2-1 = PI_RULE (D-5) — unchanged; nothing here reopens it
T  T-R2-2 = AUTHORIZE_RESTART (in narrowed_evidence; the restart layer was used: RUN1 by pid 22616, RUN2 by pid 7972)
X  cleanup R41A-01 … R41A-06 ; optional R41A-08

corrections_complete      = true by its test-based definition [A]; in the auditor's view two documentation
                            corrections are incomplete (R4A-04 (iii), R4A-10 (d)) — cleanup, not blocking
mandatory_tests_all_run   = true [A] (27 mandatory, all among the 28 recorded, all passed)
deferred_decisions        = []
narrowed_evidence         = [T-R2-2]
uncovered_coverage_rows   = ["A.5 (iii) inadmissible refit"] [A]
open_findings             = [] (no natural UNRELATED event)
F3_STEP2_r4_status        = PARTIAL_PENDING_PI (agrees with the executor)
F3_STEP2 = QUALIFIED      = NOT declared ; F3_EXECUTION_READY = false ; commit = false
```

What remains. From the PI: the two decisions that keep the status at PARTIAL_PENDING_PI — whether the narrowed
evidence of T-R2-2 (determinism across two processes, restart provenance instead of a single process) is
acceptable, and whether the untestable row A.5 (iii) is accepted as a recorded limitation — and, separately,
whether the cleanup items must be closed before the next step or may travel with the next cycle. From the
executor: the cleanup items, of which only R41A-01 touches code. Whether this end state is enough to move on is the
PI's decision, not this record's.

## 8. Evidence cited (delivered harness, verbatim)

```text
harness sha256: 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f | lines: 3678

-- fit_spline: a declared injected failure returns TEST_ONLY_INJECTION_SPLINE_FAILURE (no STOP prefix) (L965-976)
  965: def fit_spline(spl, fixture_id, x, obs_idx, telemetry, mask_id,
  966:                inject_failure=False):
  967:     SPL_CTX_DONE[0] += 1
  968:     print("PROGRESS SPL ctx %d %s %s" % (SPL_CTX_DONE[0], fixture_id, mask_id),
  969:           flush=True)
  970:     if inject_failure:
  971:         telemetry.append(dict(fixture=fixture_id, mask_id=mask_id, fitter="SPL",
  972:                               start_id="INJECTED_FAILURE", optimizer_path="none",
  973:                               status="TEST_ONLY_INJECTION", success=False,
  974:                               nit=-1, nfev=-1, njev=-1,
  975:                               wall_clock_seconds=0.0, message="injected"))
  976:         return dict(valid=False, failure="TEST_ONLY_INJECTION_SPLINE_FAILURE")

-- fit_spline: an UNRELATED event returns STOP_EXACTNESS_PENDING(<tag>) (L1065-1076)
 1065:     if any_mode_unrelated:
 1066:         ctx_unrel = [c for c in EXC_CAPTURES
 1067:                      if c.get("kind") == "UNRELATED"
 1068:                      and c.get("fixture") == fixture_id
 1069:                      and c.get("mask_id") == mask_id]
 1070:         all_test_only = ctx_unrel and all(
 1071:             "TEST_ONLY" in c.get("message", "") for c in ctx_unrel)
 1072:         # R4A-03 (r4-1): D-3 Y-04(b) writes the tag "TEST_ONLY_INJECTED"
 1073:         # (r4 had "TEST_ONLY_INJECTION"); use the D-3 label.
 1074:         tag = "TEST_ONLY_INJECTED" if all_test_only else "F3-STEP2-EXACT-04"
 1075:         return dict(valid=False, failure="STOP_EXACTNESS_PENDING(%s)" % tag,
 1076:                     per_mode_valid=per_mode_valid)

-- evaluate_fixture: routing tag from c4_source (L1283-1285)
 1283:     _spl_pend_tag = ("TEST_ONLY_INJECTED"
 1284:                      if c4_source == "TEST_ONLY_INJECTION_DECISION_LAYER"
 1285:                      else "F3-STEP2-EXACT-04")

-- evaluate_fixture: C2 <- spline fold context (L1300-1308)
 1300:                     # R4A-01 (r4-1): the spline FOLD context supplies C2's
 1301:                     # spline rho benchmark (dS["cc"] membership + dS["rho"]).
 1302:                     # If that context is unverifiable, C2 for this sex is
 1303:                     # PENDING for BOTH families -- no definite PASS/FAIL from
 1304:                     # an unverifiable benchmark (Y-04(b)).
 1305:                     if any(dS.get("spl_pending_fold", [])):
 1306:                         per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
 1307:                                                   % _spl_pend_tag)
 1308:                         continue

-- evaluate_fixture: C3 <- spline full context (L1335-1341)
 1335:                     # R4A-01 (r4-1): the spline FULL context supplies C3's
 1336:                     # spline phi benchmark (dS["phi"] + dS["full"] membership
 1337:                     # in phi_idx). Unverifiable -> C3 PENDING (both families).
 1338:                     if any(dS.get("spl_pending_full", [])):
 1339:                         per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
 1340:                                                   % _spl_pend_tag)
 1341:                         continue

-- evaluate_fixture: C4b <- spline full or probe context (L1378-1386)
 1378:                         continue
 1379:                     # R4A-01 (r4-1): C4b reads the spline FULL context
 1380:                     # (dS["full"] in V4 membership) and the spline PROBE
 1381:                     # context (dS["pL"]/["pR"] membership, dS["rL"]/["rR"]
 1382:                     # edge benchmark). Either unverifiable -> C4b PENDING.
 1383:                     if (any(dS.get("spl_pending_full", []))
 1384:                             or any(dS.get("spl_pending_probe", []))):
 1385:                         per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
 1386:                                                   % _spl_pend_tag)

-- run_real_scenario: full-context flag (TEST_ONLY excluded) (L1924-1929)
 1924:             # R4A-01: a natural UNRELATED event on the full context -> pending
 1925:             # (a TEST_ONLY-injected failure is NOT pending -- it is a
 1926:             # declared ordinary failure, per Y-04(b)).
 1927:             recs["SPL"]["spl_pending_full"].append(
 1928:                 str(spf.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
 1929:                 and "TEST_ONLY" not in str(spf.get("failure", "")))

-- run_real_scenario: fold-context flag (TEST_ONLY excluded) (L1951-1957)
 1951:                     pred_cv[held] = r["ghat"][held]
 1952:                 else:
 1953:                     cc = False
 1954:                     if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
 1955:                             and "TEST_ONLY" not in str(r.get("failure", ""))):
 1956:                         fold_pending = True   # R4A-01: any fold unverifiable
 1957:             recs["SPL"]["spl_pending_fold"].append(fold_pending)

-- run_real_scenario: probe-context flag (TEST_ONLY excluded) (L1961-1968)
 1961:             probe_pending = False
 1962:             for side, obsP, edge, a5_i in (("L", LEFT_PROBE_O, np.arange(0, 15), a5_i_L),
 1963:                                            ("R", RIGHT_PROBE_O, np.arange(131, 146), a5_i_R)):
 1964:                 r = fit_spline(spl, sc["fixture_id"], x, obsP, telemetry,
 1965:                                mid(f"{sx}{ti}:probe{side}"))
 1966:                 if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
 1967:                         and "TEST_ONLY" not in str(r.get("failure", ""))):
 1968:                     probe_pending = True   # R4A-01: either probe unverifiable

-- main: a natural UNRELATED event opens F3-STEP2-EXACT-04 (L3082-3088)
 3082:     natural_unrelated = [c for c in EXC_CAPTURES
 3083:                          if c.get("kind") == "UNRELATED"
 3084:                          and "TEST_ONLY" not in c.get("message", "")]
 3085:     natural_unrelated_findings = (
 3086:         ["F3-STEP2-EXACT-04"] if natural_unrelated else [])
 3087:     print("NATURAL_UNRELATED_EVENTS = %d ; exactness_findings = %s"
 3088:           % (len(natural_unrelated), json.dumps(natural_unrelated_findings)))

-- run_dp04: offending pairs keyed (sex, fitter, observation); first hit is the record's sex (L1713-1725)
 1713:                             if not bad:
 1714:                                 continue
 1715:                             key = (sx, fname_v, i)
 1716:                             if key in _inconsistent_pairs_seen:
 1717:                                 continue
 1718:                             _inconsistent_pairs_seen.add(key)
 1719:                             pair = dict(sex=sx, fitter=fname_v, observation=i)
 1720:                             if inconsistent_hit is None:
 1721:                                 inconsistent_hit = dict(
 1722:                                     level=crit, sex=sx, member=i,
 1723:                                     offending_pairs=[pair])
 1724:                             else:
 1725:                                 inconsistent_hit["offending_pairs"].append(pair)

-- run_dp04: guarded comparator STOP label (R4A-03) (L1770-1776)
 1770:         if not (_guarded_scalar_ok(scal["P01"]) and _guarded_scalar_ok(scal["P02"])):
 1771:             stops.append(dict(fixture=fx_id, stop="CONTRACT_VIOLATION_INCONSISTENT_U",
 1772:                               level=crit,
 1773:                               detail="guarded comparator refused a None/non-finite scalar"))
 1774:             return dict(consulted_path=consulted,
 1775:                         mechanism_outcome="STOP_CONTRACT_VIOLATION_INCONSISTENT_U",
 1776:                         disclosure=disclosure,

-- main: W-3 custody record verified by assertion before any computation (L2745-2764)
 2745:     assert os.path.exists(CUSTODY_PATH), \
 2746:         "W-3 STOP: custody record absent -- write it (externally) before the first run"
 2747:     OPENED_FILES.append(CUSTODY_PATH)
 2748:     with open(CUSTODY_PATH, "r", encoding="ascii") as f:
 2749:         custody_text = f.read()
 2750: 
 2751:     def _custody_field(name):
 2752:         for line in custody_text.splitlines():
 2753:             if line.startswith(name + " = "):
 2754:                 return line.split(" = ", 1)[1].strip()
 2755:         return None
 2756:     for fname_c, observed in (("harness_sha256", harness_hash),
 2757:                               ("generator_sha256", gen_hash),
 2758:                               ("manifest_sha256", man_hash),
 2759:                               ("code_env_fingerprint", _CODE_ENV_FINGERPRINT[0])):
 2760:         recorded = _custody_field(fname_c)
 2761:         assert recorded == observed, (
 2762:             "W-3 STOP: custody record %s = %s but observed %s"
 2763:             % (fname_c, recorded, observed))
 2764:     print("PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = true (" + CUSTODY_PATH + ")")

-- T-EXC-UNRELATED-TYPE: the only UNRELATED injection is armed around a direct fit_spline call (L2333-2337)
 2333:     nnls_before_unrelated_test = spl["nnls"]
 2334:     install_exc_unrelated_type_injection(spl)
 2335:     VALUEERROR_INJECT_TARGET.update(active=True, fixture="INJ-EXC-UNRELATED-TYPE")
 2336:     before = len(EXC_CAPTURES)
 2337:     unrel_result = fit_spline(spl, "INJ-EXC-UNRELATED-TYPE", x3, FULL_O, tel, "exc:unrel")

-- MANDATORY_TESTS (T-NONREG-R4 not listed) (L219-228)
  219: MANDATORY_TESTS = [
  220:     "NR-01i", "NR-01ii", "NR-SPL", "T-LOADER-NODES", "T-MASK-FULL-EXT",
  221:     "PIN-MASKED-OBJECTIVE", "PIN-FEATURE-START-MASKED", "UT-A5-II",
  222:     "UT-A5-III", "UT-PROBE-DECOUPLE", "UT-USET-CONSTRUCTION",
  223:     "T-COMPARATOR-NAN", "T-STARTS-DEFAULT", "T-STARTS-DUP", "FIX-A5-TRUE",
  224:     "T-A5-SUPPORT", "T-EXC-CAPTURE-S1", "T-EXC-CAPTURE-S2",
  225:     "T-EXC-UNRELATED-TYPE", "UT-EXC-UNRELATED-REFERENCE", "T-SCHEMA",
  226:     "T-CANON", "T-EXPECT-ALL", "T-CALLCOUNT", "T-RESIDUAL-LINK",
  227:     "T-WRAPPER-RESTORE", "PIN-ACF",
  228: ]
```

## 9. Appendix — evidence scripts and their verbatim output

Block [1] — r41_01_reception.py:

```python
"""Reception check (F3 STEP-2 r4-1 independent audit; auditor claude-opus-5-5). Read-only.
For every file received so far (recv*/): SHA256, CR count, sidecar format and the hash it states;
comparison with the r4-1 transmission list (31b27c28...). Prints what of the list is still missing."""
import hashlib, os, re, collections
B = "/home/claude/audit_r41/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
TLN = "f3_step2_r4-1_transmission_list_2026-09-29.md"
batches = sorted(d for d in os.listdir(B) if d.startswith("recv") and os.path.isdir(B + d))
files = {}
for d in batches:
    for f in sorted(os.listdir(B + d)):
        p = B + d + "/" + f
        if os.path.isfile(p): files.setdefault(f, []).append((d, sha(p), os.path.getsize(p), open(p, "rb").read().count(b"\r")))
conflicts = {f: v for f, v in files.items() if len(set(h for _, h, _, _ in v)) > 1}
print("batches:", batches, "| distinct names:", len(files), "| same name, different bytes:", conflicts or "none")
tl_path = [B + d + "/" + TLN for d, *_ in files[TLN]][0]
tl = open(tl_path, encoding="utf-8").read()
listed = {os.path.basename(m.group(1)): m.group(2) for m in re.finditer(r"\| [^|]*\| (?:[a-z]+/)?(\S+) \| ([0-9a-f]{64}) \|", tl)}
listed = {os.path.basename(k): v for k, v in listed.items()}
print("transmission list sha256:", sha(tl_path), "| listed files with a hash:", len(listed))
print("\n== received data files vs the list")
for f in sorted(listed):
    if f in files:
        h = files[f][0][1]; print("  %-78s %s %s" % (f, h[:12], "EQUAL" if h == listed[f] else "DIFF (list %s)" % listed[f][:12]))
print("\n== received sidecars: format, named file, stated hash vs list vs received file")
for f in sorted(x for x in files if x.endswith(".sha256")):
    d, h, size, cr = files[f][0]
    t = open(B + d + "/" + f, "rb").read().decode("utf-8")
    m = re.fullmatch(r"([0-9a-f]{64})  (\S+)\n", t)
    if not m: print("  %-82s MALFORMED %r" % (f, t)); continue
    sh, sn = m.groups()
    vs_list = ("list EQUAL" if listed.get(sn) == sh else ("list DIFF" if sn in listed else ("names the list itself" if sn == TLN else "not listed")))
    vs_file = ("file EQUAL" if sn in files and files[sn][0][1] == sh else ("file DIFF" if sn in files else "file not yet received"))
    print("  %-82s names %s | CR=%d | %s | %s%s" % (f, "ok" if sn + ".sha256" == f else "MISMATCH " + sn, cr, vs_list, vs_file,
          " | = sha(list) " + str(sh == sha(tl_path)) if sn == TLN else ""))
print("\n== still missing")
print("  data files of the list not received:", [f for f in sorted(listed) if f not in files] )
print("  sidecars of listed files not received:", [f + ".sha256" for f in sorted(listed) if f + ".sha256" not in files])
```

```text
batches: ['recv', 'recv2', 'recv3', 'recv4', 'recv5', 'recv6', 'recv7'] | distinct names: 58 | same name, different bytes: none
transmission list sha256: 31b27c28383cd4ffb6e3f10b32c8502adf5eda2dc517854074a9f071911949e1 | listed files with a hash: 25

== received data files vs the list
  f3_step2_adequacy_harness_r4-1_2026-09-29.py                                   4e0dc8cfb815 EQUAL
  f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py         280869892d8a EQUAL
  f3_step2_class_c_pin_register_r4-1_2026-09-29.md                               45a10494eb89 EQUAL
  f3_step2_correction_report_r4-1_2026-09-29.md                                  e7939a220b26 EQUAL
  f3_step2_fixture_generator_r4-1_2026-09-29.py                                  68d126cf07b1 EQUAL
  f3_step2_fixture_manifest_r4-1_2026-09-29.csv                                  5c09c4f0811f EQUAL
  f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md                         7ff79add1a72 EQUAL
  f3_step2_r4-1_attempt1_stderr_2026-09-29.log                                   8fa1cab46ecf EQUAL
  f3_step2_r4-1_attempt1_stdout_2026-09-29.log                                   f0398c8e7350 EQUAL
  f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md                     e27b29b2ae87 EQUAL
  f3_step2_r4-1_attempt2_stderr_2026-09-29.log                                   83c1e4a49778 EQUAL
  f3_step2_r4-1_attempt2_stdout_2026-09-29.log                                   9381d124f61d EQUAL
  f3_step2_r4-1_attempt_log_2026-09-29.md                                        ee5b48623a84 EQUAL
  f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv                               41dca0ba7fab EQUAL
  f3_step2_r4-1_preexecution_custody_2026-09-29.md                               3bc4e5784b7d EQUAL
  f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md                   3adbd089c03c EQUAL
  f3_step2_r4-1_restart_store_manifest_2026-09-29.csv                            cc59cf571ad4 EQUAL
  f3_step2_r4-1_run_stderr_2026-09-29.log                                        9b678df6d6be EQUAL
  f3_step2_r4-1_run_stdout_2026-09-29.log                                        77120f5be87d EQUAL
  f3_step2_r4-1_start_state_inventory_2026-09-29.md                              fedd964a95da EQUAL
  f3_step2_residual_series_r4-1_2026-09-29.json                                  3ee624f3a3e0 EQUAL
  f3_step2_results_r4-1_2026-09-29.json                                          6dd4185b895d EQUAL
  f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv                          22a5ae8f9cdc EQUAL
  f3_step2_telemetry_r4-1_2026-09-29.csv                                         85cf7620b360 EQUAL
  f3_step2_test_evidence_r4-1_2026-09-29.json                                    f74dccf0dfaa EQUAL

== received sidecars: format, named file, stated hash vs list vs received file
  f3_step2_adequacy_harness_r4-1_2026-09-29.py.sha256                                names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py.sha256     names ok | CR=0 | not listed | file EQUAL
  f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py.sha256      names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_class_c_pin_register_r4-1_2026-09-29.md.sha256                            names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_correction_report_r4-1_2026-09-29.md.sha256                               names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_fixture_generator_r4-1_2026-09-29.py.sha256                               names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_fixture_manifest_r4-1_2026-09-29.csv.sha256                               names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md.sha256                      names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_attempt1_stderr_2026-09-29.log.sha256                                names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_attempt1_stdout_2026-09-29.log.sha256                                names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md.sha256                  names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_attempt2_stderr_2026-09-29.log.sha256                                names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_attempt2_stdout_2026-09-29.log.sha256                                names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_attempt2_store_listing_2026-09-30.csv.sha256                         names ok | CR=0 | not listed | file EQUAL
  f3_step2_r4-1_attempt_log_2026-09-29.md.sha256                                     names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv.sha256                            names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_preexecution_custody_2026-09-29.md.sha256                            names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md.sha256                names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_restart_store_manifest_2026-09-29.csv.sha256                         names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_run_stderr_2026-09-29.log.sha256                                     names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_run_stdout_2026-09-29.log.sha256                                     names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_start_state_inventory_2026-09-29.md.sha256                           names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_r4-1_transmission_list_2026-09-29.md.sha256                               names ok | CR=0 | names the list itself | file EQUAL | = sha(list) True
  f3_step2_r4-1_transmission_supplement_2026-09-30.md.sha256                         names ok | CR=0 | not listed | file EQUAL
  f3_step2_residual_series_r4-1_2026-09-29.json.sha256                               names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_results_r4-1_2026-09-29.json.sha256                                       names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv.sha256                       names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_telemetry_r4-1_2026-09-29.csv.sha256                                      names ok | CR=0 | list EQUAL | file EQUAL
  f3_step2_test_evidence_r4-1_2026-09-29.json.sha256                                 names ok | CR=0 | list EQUAL | file EQUAL

== still missing
  data files of the list not received: []
  sidecars of listed files not received: []
```

Block [2] — r41_02_package_checks.py (§ numbers in its output are its own):

```python
"""Evidence script 02 (F3 STEP-2 r4-1 independent audit; auditor claude-opus-5-5; 2026-09-30). Read-only.
Every value printed is computed here from the received r4-1 files (recv*/), the auditor's copies of the
instruments (outputs/, uploads/) and the audited r4 package (audit_r4/recv/). Nothing is asserted about a file
that was not received."""
import hashlib, json, csv, os, re, io, collections, importlib.util, difflib, sys
B = "/home/claude/audit_r41/"; OUT = "/mnt/user-data/outputs/"; UP = "/root/.claude/uploads/9c789a02-f865-56de-9f2f-e299f3cfca3a/"
R4 = "/home/claude/audit_r4/recv/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
def up(prefix):
    f = [x for x in os.listdir(UP) if x.startswith(prefix)]; assert len(f) == 1, prefix; return UP + f[0]
P = {}
for d in sorted(x for x in os.listdir(B) if x.startswith("recv")):
    for f in sorted(os.listdir(B + d)):
        if os.path.isfile(B + d + "/" + f): P.setdefault(f, B + d + "/" + f)
T = "_r4-1_2026-09-29"
N = dict(har="f3_step2_adequacy_harness_r4-1_2026-09-29.py", gen="f3_step2_fixture_generator_r4-1_2026-09-29.py",
         man="f3_step2_fixture_manifest_r4-1_2026-09-29.csv", cus="f3_step2_r4-1_preexecution_custody_2026-09-29.md",
         tel="f3_step2_telemetry_r4-1_2026-09-29.csv", res="f3_step2_results_r4-1_2026-09-29.json",
         resid="f3_step2_residual_series_r4-1_2026-09-29.json", te="f3_step2_test_evidence_r4-1_2026-09-29.json",
         reg="f3_step2_class_c_pin_register_r4-1_2026-09-29.md", rep="f3_step2_correction_report_r4-1_2026-09-29.md",
         inv="f3_step2_r4-1_start_state_inventory_2026-09-29.md", log="f3_step2_r4-1_attempt_log_2026-09-29.md",
         pc="f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv", store="f3_step2_r4-1_restart_store_manifest_2026-09-29.csv",
         nonreg="f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv", out="f3_step2_r4-1_run_stdout_2026-09-29.log",
         err="f3_step2_r4-1_run_stderr_2026-09-29.log", ann="f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md",
         a1n="f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md", a2n="f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md",
         a1h="f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py",
         a2h="f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py",
         a1o="f3_step2_r4-1_attempt1_stdout_2026-09-29.log", a1e="f3_step2_r4-1_attempt1_stderr_2026-09-29.log",
         a2o="f3_step2_r4-1_attempt2_stdout_2026-09-29.log", a2e="f3_step2_r4-1_attempt2_stderr_2026-09-29.log",
         sup="f3_step2_r4-1_transmission_supplement_2026-09-30.md", a2s="f3_step2_r4-1_attempt2_store_listing_2026-09-30.csv",
         tl="f3_step2_r4-1_transmission_list_2026-09-29.md")
H = {k: sha(P[v]) for k, v in N.items()}
txt = lambda k: open(P[N[k]], encoding="utf-8").read()

print("== [1] supplement files: hash vs their sidecars; line endings")
for k in ("sup", "a2s", "a1h"):
    sc = open(P[N[k] + ".sha256"], encoding="utf-8").read().split()
    print("  %-72s %s | sidecar %s | CR bytes %d" % (N[k], H[k][:16], "EQUAL" if sc[0] == H[k] and sc[1] == N[k] else "DIFF",
          open(P[N[k]], "rb").read().count(b"\r")))

print("\n== [2] instruments: custody record's observed values vs the auditor's own copies")
cus = txt("cus")
mine = dict(D3=OUT + "Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
            r4_instruction=OUT + "Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md",
            D5=OUT + "f3_step2_r4_pi_dispatch_record_2026-09-24.md",
            r4_1_instruction=OUT + "Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md",
            D6=OUT + "f3_step2_r4-1_pi_dispatch_record_2026-09-29.md",
            A1=OUT + "f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md",
            A2=OUT + "f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md",
            A3=OUT + "f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md",
            D1=up("892d0f75-"), D2=up("8dbc7dd4-"))
keymap = dict(D3="D-3", r4_instruction="r4_instruction", D5="D-5", r4_1_instruction="r4-1_instruction", D6="D-6",
              A1="A-1", A2="A-2", A3="A-3", D1="D-1", D2="D-2")
for k, p in mine.items():
    h = sha(p); m = re.search(r"^%s_sha256_observed = ([0-9a-f]{64})" % re.escape(keymap[k]), cus, re.M)
    print("  %-17s auditor %s… | custody observed %s | equal: %s" % (k, h[:12], (m.group(1)[:12] + "…") if m else "absent", bool(m) and m.group(1) == h))

for f in sorted(os.listdir(B + "instr/")):
    if f.endswith(".md"): print("  forwarded copy %-72s byte-identical to the auditor's: %s" % (f, open(B + "instr/" + f, "rb").read() == open(OUT + f, "rb").read()))
print("\n== [3] which bytes ran: fingerprints (harness formula) and store prefixes")
har = txt("har")
F2 = re.search(r'^F2_HASH = "([0-9a-f]{64})"', har, re.M).group(1); SPL = re.search(r'^SPL_HASH = "([0-9a-f]{64})"', har, re.M).group(1)
fp = lambda h, g, m: hashlib.sha256("|".join([h, g, m, F2, SPL, "3.11.7", "1.26.4", "1.14.1", "Windows-10-10.0.19045-SP0", "1", "1", "1"]).encode()).hexdigest()[:16]
g_ = lambda k: re.search(r"^%s = (\S+)" % k, cus, re.M).group(1)
print("  custody names H %s… G %s… M %s… ; delivered H/G/M equal: %s %s %s" % (g_("harness_sha256")[:8], g_("generator_sha256")[:8], g_("manifest_sha256")[:8],
      g_("harness_sha256") == H["har"], g_("generator_sha256") == H["gen"], g_("manifest_sha256") == H["man"]))
print("  fp(delivered triple) = %s | custody records %s" % (fp(H["har"], H["gen"], H["man"]), g_("code_env_fingerprint")))
store = list(csv.DictReader(open(P[N["store"]], newline="", encoding="utf-8")))
print("  final store manifest: rows %d | prefixes %s | (pid, start_iso) %s" % (len(store), dict(collections.Counter(r["path"].split("/")[-1].split("__")[0] for r in store)),
      dict(collections.Counter((r["pid"], r["start_iso"]) for r in store))))
a2s = list(csv.DictReader(open(P[N["a2s"]], newline="", encoding="utf-8")))
print("  attempt-2 store listing: rows %d | prefixes %s | fp(attempt-2 bytes %s…) = %s" % (len(a2s), dict(collections.Counter(r["path"].split("/")[-1].split("__")[0] for r in a2s)),
      H["a2h"][:8], fp(H["a2h"], H["gen"], H["man"])))
print("  attempt-1 bytes %s… -> fp %s (recorded only in the attempt-1 note: %s)" % (H["a1h"][:8], fp(H["a1h"], H["gen"], H["man"]), "4c776ba53e4fbe9c" in txt("a1n")))
r4store = list(csv.DictReader(open(R4 + "f3_step2_r4_restart_store_manifest_2026-09-24.csv", newline="", encoding="utf-8")))
k_ = lambda p: re.sub(r"^[0-9a-f]{16}__", "", p.split("/")[-1])
print("  unit names (prefix stripped): final == r4: %s | attempt-2 == r4: %s" % (sorted(k_(r["path"]) for r in store) == sorted(k_(r["path"]) for r in r4store),
      sorted(k_(r["path"]) for r in a2s) == sorted(k_(r["path"]) for r in r4store)))
print("  harness constants:", re.findall(r'^(ATTEMPT_NUMBER = \d+|RESTART_LAYER_ACTIVE = \w+|SUPERSEDES_CUSTODY_SHA256 = \w+)', har, re.M))

print("\n== [4] revisions of this cycle: non-comment line changes")
def code_lines(p): return [l.rstrip() for l in open(p, encoding="utf-8").read().split("\n") if l.strip() and not l.strip().startswith("#")]
for a, b in (("a1h", "a2h"), ("a2h", "har")):
    d = [l for l in difflib.unified_diff(code_lines(P[N[a]]), code_lines(P[N[b]]), lineterm="", n=0) if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    meta = [l for l in d if re.match(r"^[+-](SUPERSEDES_|ATTEMPT_NUMBER|RESTART_LAYER_ACTIVE)", l)]
    print("  %s %s… -> %s %s…: %d changed lines, %d of them revision constants" % (a, H[a][:8], b, H[b][:8], len(d), len(meta)))
    for l in d:
        if l not in meta: print("     " + l.strip()[:140])

print("\n== [5] manifest regenerated from the delivered generator with the harness's writer (csv, LF, ascii)")
spec = importlib.util.spec_from_file_location("gen_r41_audit", P[N["gen"]]); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)
buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(gen.MANIFEST_HEADER); w.writerows(gen.manifest_rows())
print("  regenerated %s | delivered %s | equal %s" % (hashlib.sha256(buf.getvalue().encode("ascii")).hexdigest()[:16], H["man"][:16],
      hashlib.sha256(buf.getvalue().encode("ascii")).hexdigest() == H["man"]))

print("\n== [6] results: canonical document, expectations, tests, end state")
r = json.load(open(P[N["res"]])); ev = {e["fixture_id"]: e for e in r["evaluations"]}
doc = dict(evals=r["evaluations"], stops=r["stops"], pins=dict(mask_full=True, fs=True))
hc = hashlib.sha256(json.dumps(doc, sort_keys=True).encode("utf-8")).hexdigest()
print("  canonical recomputed %s | results.run1 %s | run1 == run2 (executor): %s" % (hc[:16], r["run1_canonical_sha256"][:16], r["run1_canonical_sha256"] == r["run2_canonical_sha256"]))
man = list(csv.DictReader(open(P[N["man"]], newline="", encoding="utf-8")))
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
                if ((disc.get(UL[uk]) or {}).get("per_sex") or {}).get(s2, {}).get("U_size") != int(val): mism.append(f"{uk}{s2}")
    if exp["expected_stops"] and exp["expected_stops"] not in [s["stop"] for s in r["stops"] if s["fixture"] == fid]: mism.append("stops")
    if exp["expected_undefined"]:
        for part in exp["expected_undefined"].split(";"):
            key, val = part.split("="); fam, crit, sx = key.split(":")
            if e["criteria"][fam][crit][sx].get("undefined") != (val == "True"): mism.append(f"undefined[{key}]")
    if mism: fails.append((fid, mism))
print("  T-EXPECT-ALL re-done: declared %d | mismatches %s | results.expectation_checks %s" % (declared, fails or "none",
      {k: v for k, v in r["expectation_checks"].items() if k != "detail"}))
mand = re.findall(r"\"([^\"]+)\"", re.search(r"MANDATORY_TESTS = \[(.*?)\]", har, re.S).group(1))
print("  mandatory tests in harness %d | tests_run %d | all passed %s | mandatory missing from tests_run %s" % (len(mand), len(r["tests_run"]),
      all(v["passed"] for v in r["tests_run"].values()), [t for t in mand if t not in r["tests_run"]]))
print("  end_state:", json.dumps(r["end_state"], sort_keys=True))
alltext = {k: open(P[N[k]], encoding="utf-8").read() for k in ("res", "te", "out")}
print("  D-6 hash a92a0518… present in results / test evidence / stdout:", {k: "a92a0518" in v for k, v in alltext.items()},
      "| D-5 hash 0cd87ad5… present:", {k: "0cd87ad5" in v for k, v in alltext.items()})
print("  exactness_findings %s | open_findings %s | engineering_findings %s" % (r["exactness_findings"], r["end_state"]["open_findings"], r["engineering_findings"]))
print("  process: pid %s attempt %s restart_layer %s calls_by_phase_pid %s" % (r["process"]["pid"], r["process"]["attempt_number"], r["process"]["restart_layer_active"], r["process"]["spline_telemetry_calls_by_phase_pid"]))
print("  process.supersedes_harness_sha256:", r["process"].get("supersedes_harness_sha256"), "| executor_models:", r["process"].get("executor_models"))

print("\n== [7] the three R4A-01 fixtures as delivered (criterion states in F and M, p03, mechanism, stops)")
for fid in ("INJ-SPL-PENDING-FULL", "INJ-SPL-PENDING-FOLD", "INJ-SPL-PENDING-PROBE"):
    e = ev[fid]; states = {}
    for fam in ("P01", "P02"):
        for crit in ("C1", "C2", "C3", "C4a", "C4b", "C5", "C6"):
            for sx in ("F", "M"):
                c = e["criteria"][fam][crit][sx]
                states.setdefault(c.get("status") or ("PASS" if c.get("passed") else "FAIL"), []).append(f"{fam}:{crit}:{sx}")
    print("  %-22s p03=%s mech=%s stops=%s" % (fid, (e["p03"]["P01"], e["p03"]["P02"]), e["mechanism_outcome"], [s for s in r["stops"] if s["fixture"] == fid]))
    for st, cells in states.items(): print("       %-48s %s" % (st, cells if len(cells) < 12 else f"{len(cells)} cells"))

print("\n== [8] non-regression, recomputed by the auditor from the two results files (r4 a15b7eff…, r4-1)")
r4 = json.load(open(R4 + "f3_step2_results_r4_2026-09-24.json")); ev4 = {e["fixture_id"]: e for e in r4["evaluations"]}
proj = ("p03", "criteria", "dp04", "mechanism_outcome")
cmp_rows = []
for fid in sorted(set(ev4) | set(ev)):
    if fid not in ev4: cmp_rows.append((fid, "NEW_IN_R4-1", [])); continue
    if fid not in ev: cmp_rows.append((fid, "DROPPED", [])); continue
    ch = [k for k in proj if json.dumps(ev4[fid].get(k), sort_keys=True) != json.dumps(ev[fid].get(k), sort_keys=True)]
    s4 = sorted(json.dumps(s, sort_keys=True) for s in r4["stops"] if s["fixture"] == fid); s41 = sorted(json.dumps(s, sort_keys=True) for s in r["stops"] if s["fixture"] == fid)
    if s4 != s41: ch.append("stops")
    other = sorted(k for k in set(ev4[fid]) | set(ev[fid]) if k not in proj and json.dumps(ev4[fid].get(k), sort_keys=True) != json.dumps(ev[fid].get(k), sort_keys=True))
    cmp_rows.append((fid, "CHANGED" if ch else "IDENTICAL", ch + (["(other keys: %s)" % other] if other else [])))
print("  status counts:", dict(collections.Counter(s for _, s, _ in cmp_rows)))
print("  whole evaluation objects byte-identical (json, sorted keys) for shared fixtures: %d of %d" % (sum(1 for f in ev4 if f in ev and json.dumps(ev4[f], sort_keys=True) == json.dumps(ev[f], sort_keys=True)), len(ev4)))
for fid, s, ch in cmp_rows:
    if s != "IDENTICAL": print("   ", fid, s, ch)
nr = list(csv.DictReader(open(P[N["nonreg"]], newline="", encoding="utf-8")))
print("  executor CSV: rows %d | status %s | agrees with the auditor's per-fixture status: %s" % (len(nr), dict(collections.Counter(x["status"] for x in nr)),
      all(dict((f, s) for f, s, _ in cmp_rows).get(x["fixture"]) == x["status"] for x in nr)))
ipc = [s for s in r["stops"] if s["fixture"] == "INJ-U-POST-CONSTRUCTION-INVALID"]; ipc4 = [s for s in r4["stops"] if s["fixture"] == "INJ-U-POST-CONSTRUCTION-INVALID"]
print("  INCONSISTENT_U stop, r4  :", json.dumps(ipc4)); print("  INCONSISTENT_U stop, r4-1:", json.dumps(ipc))

print("\n== [9] telemetry, store and residual")
pc = list(csv.DictReader(open(P[N["pc"]], newline="", encoding="utf-8")))
bypp = collections.Counter(f"{x['phase']}/{x['pid']}" for x in pc)
print("  per-call rows %d | by phase/pid %s | == results.process: %s" % (len(pc), dict(bypp), dict(bypp) == r["process"]["spline_telemetry_calls_by_phase_pid"]))
tel = list(csv.DictReader(open(P[N["tel"]], newline="", encoding="utf-8")))
print("  mode-level rows %d | by mask prefix %s" % (len(tel), dict(collections.Counter(x["mask_id"].split(":")[0] for x in tel))))
print("  residual series == r4 export byte-identical: %s" % (H["resid"] == sha(R4 + "f3_step2_residual_series_r4_2026-09-24.json")))
print("  stdout T_CALLCOUNT line:", [l for l in txt("out").split("\n") if l.startswith("T_CALLCOUNT")])

print("\n== [10] coverage (R4A-02)")
cov = r["coverage"]
print("  rows %d | statuses %s | downgraded %s" % (len(cov), dict(collections.Counter(str(x[3]).split("(")[0] for x in cov)), r["coverage_downgraded_rows"]))
def c_pass(fid, crit): return all(ev[fid]["criteria"][fam][crit][sx].get("passed") is True for fam in ("P01", "P02") for sx in ("F", "M"))
for fid in ("INJ-DP04-TERMINAL", "INJ-DP04-C3", "INJ-DP04-4A", "INJ-DP04-4B"):
    print("   %-18s C2 pass both families/sexes %s | C3 pass %s" % (fid, c_pass(fid, "C2"), c_pass(fid, "C3")))
print("   T-COMPARATOR-NAN passed %s | T-CALLCOUNT passed %s" % (r["tests_run"]["T-COMPARATOR-NAN"]["passed"], r["tests_run"]["T-CALLCOUNT"]["passed"]))
print("   UNCOVERED rows:", [x[0] for x in cov if str(x[3]).startswith("UNCOVERED")])

print("\n== [11] report, register, inventory, erratum (R4A-04, R4A-10)")
rep = txt("rep"); reg = txt("reg"); inv = txt("inv"); log = txt("log"); ann = txt("ann")
print("  report hash-block rows without a hash:", [re.sub(r"\s+", " ", l)[:70] for l in rep.split("\n") if re.match(r"^\| (9|10|11|12|D) \|", l) and not re.search(r"[0-9a-f]{64}", l)])
print("  report §10 PI_dispatch_record_hash line:", [l.strip()[:120] for l in rep.split("\n") if l.startswith("PI_dispatch_record_hash")])
print("  register parent = r4 register 0eed314c…: %s | register names D-6 a92a0518…: %s" % ("0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4" in reg, "a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0" in reg))
print("  register/report say one deduped pair for INJ-U-POST-CONSTRUCTION-INVALID:", "one deduped" in reg, "one deduped pair" in rep)
r4pk = dict(har="54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c", gen="393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c",
            man="c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8", cus="0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f",
            tel="11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910", res="a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374",
            resid="3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f", te="118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2",
            reg="0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4", rep="5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848",
            log="8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69", pc="d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5",
            store="f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1")
r4files = dict(har="f3_step2_adequacy_harness_r4_2026-09-24.py", gen="f3_step2_fixture_generator_r4_2026-09-24.py", man="f3_step2_fixture_manifest_r4_2026-09-24.csv",
               cus="f3_step2_r4_preexecution_custody_2026-09-24.md", tel="f3_step2_telemetry_r4_2026-09-24.csv", res="f3_step2_results_r4_2026-09-24.json",
               resid="f3_step2_residual_series_r4_2026-09-24.json", te="f3_step2_test_evidence_r4_2026-09-24.json", reg="f3_step2_class_c_pin_register_r4_2026-09-27.md",
               rep="f3_step2_correction_report_r4_2026-09-27.md", log="f3_step2_r4_attempt_log_2026-09-24.md", pc="f3_step2_spline_percall_telemetry_r4_2026-09-24.csv",
               store="f3_step2_r4_restart_store_manifest_2026-09-24.csv")
print("  inventory §2: 13 r4 hashes == the auditor's r4 bytes and == inventory text: %s" % all(sha(R4 + r4files[k]) == h and h in inv for k, h in r4pk.items()))
trip = [("5fea165c", "cc23c9b5", "9c944543", "1ba561daefb48b2e"), ("6ddcc26d", "e35c2bf0", "4544ff75", "2cf50b2f18cfb34e"), ("891574fc", "e35c2bf0", "4544ff75", "d505bf76994abf60"),
        ("d67e097d", "e35c2bf0", "4544ff75", "6f4e29ccc903bce6"), ("390f42b7", "cc23c9b5", "9c944543", "548ae790f6ac756a")]
rows_inv = [l for l in inv.split("\n") if l.startswith("| r3 ")]
print("  inventory §3: the five r3 triples of A-3 §5.2 each present as one row: %s" % all(any(all(t in l for t in tr) for l in rows_inv) for tr in trip))
checks = {"(a) 548ae790 = fingerprint of the attempt-8 custody triple": "548ae790" in log and "ATTEMPT8 custody triple" in log,
          "(b) ATTEMPT8 label holds 99f895c1, not 390f42b7": "99f895c1" in log and "390f42b7" in log,
          "(c) ATTEMPT5 harness/generator labels": "f882b922" in log and "e35c2bf0" in log and "cc23c9b5" in log,
          "(d) r3 log revision-4 row vs revision-4 custody record": bool(re.search(r"revision[ -]4", log[log.find("ERRATUM-2"):])),
          "r3 attempt log hash 25316389 cited in ERRATUM-2": "25316389" in log[log.find("ERRATUM-2"):],
          "r4 erratum item 3 named as corrected": bool(re.search(r"item 3", log[log.find("ERRATUM-2"):]))}
for k, v in checks.items(): print("   ERRATUM-2 %-62s %s" % (k, v))
print("  annotation note: four label rows with match yes/NO: %s" % re.findall(r"\| \*\*(?:yes|NO)\*\*|\| yes \||\*\*NO\*\*", ann)[:8])

print("\n== [12] run logs of this cycle")
for k in ("a1o", "a1e", "a2o", "a2e", "out", "err"):
    t = open(P[N[k]], encoding="utf-8", errors="replace").read()
    pids = re.findall(r"^PID = (\d+)", t, re.M)
    print("  %-50s %7d B | PID %s | Traceback %s | AssertionError %s | last PROGRESS %s" % (N[k], os.path.getsize(P[N[k]]), pids or "-", "Traceback" in t,
          [l[:90] for l in re.findall(r"AssertionError[^\n]*", t)][:1] or "-", (re.findall(r"^PROGRESS SPL ctx (\d+)", t, re.M) or ["-"])[-1]))
for k in ("a2o", "out"):
    t = txt(k)
    print("  %s: %s" % (k, [l[:110] for l in t.split("\n") if l.startswith(("T_EXPECT_ALL", "NONREGRESSION_VS_R4", "DETERMINISM", "RUN1_CANONICAL", "EXC_CAPTURES_RUN1_EQ_RUN2"))]))

print("\n== [13] scope strings")
print("  results.real_data_access:", r.get("real_data_access"), "| register new_scientific_literal_by_executor line:",
      [l.strip() for l in txt("reg").split("\n") if l.startswith("new_scientific_literal_by_executor")])
for k in ("rep", "reg", "log", "inv"):
    print("  %s lines mentioning QUALIFIED:" % k, [re.sub(r"\s+", " ", l.strip())[:110] for l in txt(k).split("\n") if "QUALIFIED" in l])
```

```text
== [1] supplement files: hash vs their sidecars; line endings
  f3_step2_r4-1_transmission_supplement_2026-09-30.md                      0b3f4358c1eac53d | sidecar EQUAL | CR bytes 0
  f3_step2_r4-1_attempt2_store_listing_2026-09-30.csv                      8dfbe9e6fdd52666 | sidecar EQUAL | CR bytes 11870
  f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py  b22708d2fd7e1a68 | sidecar EQUAL | CR bytes 0

== [2] instruments: custody record's observed values vs the auditor's own copies
  D3                auditor 5b0e19ea58dd… | custody observed 5b0e19ea58dd… | equal: True
  r4_instruction    auditor e12839587153… | custody observed e12839587153… | equal: True
  D5                auditor 0cd87ad5b952… | custody observed 0cd87ad5b952… | equal: True
  r4_1_instruction  auditor 283ac4e29b6a… | custody observed 283ac4e29b6a… | equal: True
  D6                auditor a92a0518dd05… | custody observed a92a0518dd05… | equal: True
  A1                auditor 11cfa591cee0… | custody observed 11cfa591cee0… | equal: True
  A2                auditor b721702785d0… | custody observed b721702785d0… | equal: True
  A3                auditor 9c16abb5beb1… | custody observed 9c16abb5beb1… | equal: True
  D1                auditor 17187d31f772… | custody observed 17187d31f772… | equal: True
  D2                auditor da0c40646152… | custody observed da0c40646152… | equal: True
  forwarded copy Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md           byte-identical to the auditor's: True
  forwarded copy f3_step2_r4-1_pi_dispatch_record_2026-09-29.md                           byte-identical to the auditor's: True
  forwarded copy f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md     byte-identical to the auditor's: True
  forwarded copy f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md     byte-identical to the auditor's: True

== [3] which bytes ran: fingerprints (harness formula) and store prefixes
  custody names H 4e0dc8cf… G 68d126cf… M 5c09c4f0… ; delivered H/G/M equal: True True True
  fp(delivered triple) = dc228827920a9633 | custody records dc228827920a9633
  final store manifest: rows 11869 | prefixes {'dc228827920a9633': 11869} | (pid, start_iso) {('22616', '2026-09-29T22:14:16.468915'): 7271, ('7972', '2026-09-30T12:44:02.351036'): 4598}
  attempt-2 store listing: rows 11869 | prefixes {'b6fc376b049c20e1': 11869} | fp(attempt-2 bytes 28086989…) = b6fc376b049c20e1
  attempt-1 bytes b22708d2… -> fp 4c776ba53e4fbe9c (recorded only in the attempt-1 note: True)
  unit names (prefix stripped): final == r4: True | attempt-2 == r4: True
  harness constants: ['RESTART_LAYER_ACTIVE = True', 'SUPERSEDES_CUSTODY_SHA256 = None', 'ATTEMPT_NUMBER = 3']

== [4] revisions of this cycle: non-comment line changes
  a1h b22708d2… -> a2h 28086989…: 8 changed lines, 8 of them revision constants
  a2h 28086989… -> har 4e0dc8cf…: 20 changed lines, 6 of them revision constants
     +    def _cn(x):
     +        return json.dumps(canon(x), sort_keys=True)
     -            (json.dumps(s, sort_keys=True) for s in stops
     -             if s.get("fixture") == fid))
     +            (s for s in stops if s.get("fixture") == fid), key=_cn)
     -        changed = sorted(k for k in a if a[k] != b[k])
     +        changed = sorted(k for k in a if _cn(a[k]) != _cn(b[k]))
     -            r4=json.dumps({k: a[k] for k in changed}, default=str),
     -            r4_1=json.dumps({k: b[k] for k in changed}, default=str)))
     +            r4=_cn({k: a[k] for k in changed}),
     +            r4_1=_cn({k: b[k] for k in changed})))
     -            r4="", r4_1=json.dumps(_fix_proj(_r41_ev, _r41_stops, fid),
     -                                    default=str)))
     +            r4="", r4_1=_cn(_fix_proj(_r41_ev, _r41_stops, fid))))

== [5] manifest regenerated from the delivered generator with the harness's writer (csv, LF, ascii)
  regenerated 5c09c4f0811fa51b | delivered 5c09c4f0811fa51b | equal True

== [6] results: canonical document, expectations, tests, end state
  canonical recomputed 556106e7c4609ade | results.run1 556106e7c4609ade | run1 == run2 (executor): True
  T-EXPECT-ALL re-done: declared 36 | mismatches none | results.expectation_checks {'EXPECTATION_FAIL': 'none', 'declared': 36, 'ran': 36}
  mandatory tests in harness 27 | tests_run 28 | all passed True | mandatory missing from tests_run []
  end_state: {"F3_STEP2_r4_status": "PARTIAL_PENDING_PI", "PI_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851", "corrections_complete": true, "deferred_decisions": [], "mandatory_tests_all_run": true, "mandatory_tests_missing": [], "narrowed_evidence": ["T-R2-2"], "open_findings": [], "uncovered_coverage_rows": ["A.5 (iii) inadmissible refit"]}
  D-6 hash a92a0518… present in results / test evidence / stdout: {'res': False, 'te': False, 'out': False} | D-5 hash 0cd87ad5… present: {'res': True, 'te': False, 'out': True}
  exactness_findings [] | open_findings [] | engineering_findings []
  process: pid 7972 attempt 3 restart_layer True calls_by_phase_pid {'nr_gates/22616': 60, 'run1/22616': 5256, 'run2/7972': 5256, 'unit_tests/22616': 1602}
  process.supersedes_harness_sha256: 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2 | executor_models: claude-opus-4-8[1m]; see r4-1 report

== [7] the three R4A-01 fixtures as delivered (criterion states in F and M, p03, mechanism, stops)
  INJ-SPL-PENDING-FULL   p03=('PENDING', 'PENDING') mech=MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED) stops=[]
       PASS                                             24 cells
       STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)       ['P01:C3:F', 'P01:C4b:F', 'P02:C3:F', 'P02:C4b:F']
  INJ-SPL-PENDING-FOLD   p03=('PENDING', 'PENDING') mech=MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED) stops=[]
       PASS                                             26 cells
       STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)       ['P01:C2:F', 'P02:C2:F']
  INJ-SPL-PENDING-PROBE  p03=('PENDING', 'PENDING') mech=MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED) stops=[]
       PASS                                             26 cells
       STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)       ['P01:C4b:F', 'P02:C4b:F']

== [8] non-regression, recomputed by the auditor from the two results files (r4 a15b7eff…, r4-1)
  status counts: {'IDENTICAL': 33, 'NEW_IN_R4-1': 3, 'CHANGED': 1}
  whole evaluation objects byte-identical (json, sorted keys) for shared fixtures: 34 of 34
    INJ-SPL-PENDING-FOLD NEW_IN_R4-1 []
    INJ-SPL-PENDING-FULL NEW_IN_R4-1 []
    INJ-SPL-PENDING-PROBE NEW_IN_R4-1 []
    INJ-U-POST-CONSTRUCTION-INVALID CHANGED ['stops']
  executor CSV: rows 37 | status {'IDENTICAL': 33, 'CHANGED': 1, 'NEW_IN_R4-1': 3} | agrees with the auditor's per-fixture status: True
  INCONSISTENT_U stop, r4  : [{"fixture": "INJ-U-POST-CONSTRUCTION-INVALID", "level": "C2", "member": 0, "offending_pairs": [{"fitter": "P01", "observation": 0}, {"fitter": "P01", "observation": 0}, {"fitter": "P01", "observation": 0}, {"fitter": "P01", "observation": 0}], "sex": "F", "stop": "CONTRACT_VIOLATION_INCONSISTENT_U"}]
  INCONSISTENT_U stop, r4-1: [{"fixture": "INJ-U-POST-CONSTRUCTION-INVALID", "level": "C2", "member": 0, "offending_pairs": [{"fitter": "P01", "observation": 0, "sex": "F"}, {"fitter": "P01", "observation": 0, "sex": "M"}], "sex": "F", "stop": "CONTRACT_VIOLATION_INCONSISTENT_U"}]

== [9] telemetry, store and residual
  per-call rows 12174 | by phase/pid {'nr_gates/22616': 60, 'unit_tests/22616': 1602, 'run1/22616': 5256, 'run2/7972': 5256} | == results.process: True
  mode-level rows 12298 | by mask prefix {'run1': 4645, 'run2': 4645, 'exc': 876, 'a5true': 616, 'full': 994, 'dup': 522}
  residual series == r4 export byte-identical: True
  stdout T_CALLCOUNT line: ['T_CALLCOUNT per phase = {"nr_gates": 60, "run1": 5256, "run2": 5256, "unit_tests": 1602}', 'T_CALLCOUNT per phase/pid = {"nr_gates/22616": 60, "run1/22616": 5256, "run2/7972": 5256, "unit_tests/22616": 1602}']

== [10] coverage (R4A-02)
  rows 64 | statuses {'covered': 61, 'covered_injection_only': 2, 'UNCOVERED': 1} | downgraded []
   INJ-DP04-TERMINAL  C2 pass both families/sexes True | C3 pass True
   INJ-DP04-C3        C2 pass both families/sexes True | C3 pass True
   INJ-DP04-4A        C2 pass both families/sexes True | C3 pass True
   INJ-DP04-4B        C2 pass both families/sexes True | C3 pass True
   T-COMPARATOR-NAN passed True | T-CALLCOUNT passed True
   UNCOVERED rows: ['A.5 (iii) inadmissible refit']

== [11] report, register, inventory, erratum (R4A-04, R4A-10)
  report hash-block rows without a hash: ['| 9 | calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md (ch', '| 10 | provenance/f3_step2_correction_report_r4-1_2026-09-29.md (this ', '| 11 | provenance/f3_step2_r4-1_start_state_inventory_2026-09-29.md (R', '| 12 | provenance/f3_step2_r4-1_attempt_log_2026-09-29.md (incl. ERRAT', '| D | run logs (stdout + stderr) + quarantine notes/snapshots — see §8']
  report §10 PI_dispatch_record_hash line: ['PI_dispatch_record_hash     = 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 (D-5, as END_STATE record']
  register parent = r4 register 0eed314c…: True | register names D-6 a92a0518…: True
  register/report say one deduped pair for INJ-U-POST-CONSTRUCTION-INVALID: True True
  inventory §2: 13 r4 hashes == the auditor's r4 bytes and == inventory text: True
  inventory §3: the five r3 triples of A-3 §5.2 each present as one row: True
   ERRATUM-2 (a) 548ae790 = fingerprint of the attempt-8 custody triple     True
   ERRATUM-2 (b) ATTEMPT8 label holds 99f895c1, not 390f42b7                True
   ERRATUM-2 (c) ATTEMPT5 harness/generator labels                          True
   ERRATUM-2 (d) r3 log revision-4 row vs revision-4 custody record         False
   ERRATUM-2 r3 attempt log hash 25316389 cited in ERRATUM-2                False
   ERRATUM-2 r4 erratum item 3 named as corrected                           False
  annotation note: four label rows with match yes/NO: ['| **yes**', '| **yes**', '| **NO**', '| **NO**', '| **NO**', '| **yes**']

== [12] run logs of this cycle
  f3_step2_r4-1_attempt1_stdout_2026-09-29.log          9476 B | PID ['19528'] | Traceback False | AssertionError - | last PROGRESS 41
  f3_step2_r4-1_attempt1_stderr_2026-09-29.log        268781 B | PID - | Traceback False | AssertionError - | last PROGRESS -
  f3_step2_r4-1_attempt2_stdout_2026-09-29.log         15402 B | PID ['3348'] | Traceback True | AssertionError - | last PROGRESS 74
  f3_step2_r4-1_attempt2_stderr_2026-09-29.log        308323 B | PID - | Traceback True | AssertionError ['AssertionError: T-NONREG-R4: unexpected non-regression findings vs r4: [{"fixture": "INJ-B'] | last PROGRESS -
  f3_step2_r4-1_run_stdout_2026-09-29.log              16660 B | PID ['7972'] | Traceback True | AssertionError - | last PROGRESS 32
  f3_step2_r4-1_run_stderr_2026-09-29.log              29531 B | PID - | Traceback False | AssertionError - | last PROGRESS -
  a2o: ['EXC_CAPTURES_RUN1_EQ_RUN2 = True (run1=1, run2=1)', 'T_EXPECT_ALL = declared/ran 36/36 ; EXPECTATION_FAIL = []', 'NONREGRESSION_VS_R4 shared=34 new=3 dropped=0 findings=33 real_path_spline_pending=0']
  out: ['EXC_CAPTURES_RUN1_EQ_RUN2 = True (run1=1, run2=1)', 'T_EXPECT_ALL = declared/ran 36/36 ; EXPECTATION_FAIL = []', 'NONREGRESSION_VS_R4 shared=34 new=3 dropped=0 findings=0 real_path_spline_pending=0', 'RUN1_CANONICAL_SHA256 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77', 'DETERMINISM = True']

== [13] scope strings
  results.real_data_access: False | register new_scientific_literal_by_executor line: ['new_scientific_literal_by_executor = 0']
  rep lines mentioning QUALIFIED: ['No wording in this report asserts "verified", "QUALIFIED", or "audit PASS" about the', "executor's own output. `F3_STEP2 = QUALIFIED` can be declared only by the PI after an"]
  reg lines mentioning QUALIFIED: []
  log lines mentioning QUALIFIED: []
  inv lines mentioning QUALIFIED: []
```

Block [3] — r41_03_decision_layer_repro.py (output in §5.1):

```python
"""Evidence script 03 (F3 STEP-2 r4-1 independent audit; auditor claude-opus-5-5; 2026-09-30). [A-S] auditor-environment
reproduction of the platform-independent parts: imports the UNMODIFIED r4-1 harness (4e0dc8cf...) and generator
(68d126cf...) and calls (a) evaluate_fixture on every decision-layer fixture in generator order, twice in one process,
(b) the pure unit tests t_a5_support, t_comparator_nan, ut_uset_construction, and compares with the delivered results /
test evidence; (c) re-applies the evaluation-level assertion of T-EXC-UNRELATED-TYPE to the three R4A-01 fixtures.
main() is NOT called; no real fit is run; no executor path is written."""
import importlib.util, sys, json, hashlib, warnings
warnings.filterwarnings("ignore")
HP = "G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py"
spec = importlib.util.spec_from_file_location("h_r41", HP); h = importlib.util.module_from_spec(spec); sys.modules["h_r41"] = h; spec.loader.exec_module(h)
gs = importlib.util.spec_from_file_location(h.GEN_MODULE_NAME, h.GEN_PATH); gen = importlib.util.module_from_spec(gs); sys.modules[h.GEN_MODULE_NAME] = gen; gs.loader.exec_module(gen)
print("harness sha256:", hashlib.sha256(open(h.__file__, "rb").read()).hexdigest())
print("generator sha256:", hashlib.sha256(open(h.GEN_PATH, "rb").read()).hexdigest())
D = "/home/claude/audit_r41/recv3/"
R = json.load(open(D + "f3_step2_results_r4-1_2026-09-29.json")); TE = json.load(open(D + "f3_step2_test_evidence_r4-1_2026-09-29.json"))
ER = {e["fixture_id"]: e for e in R["evaluations"]}
J = lambda o: json.dumps(o, sort_keys=True)
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
print("decision-layer fixtures:", len(e1), "| pass1 == pass2 (same process):", J(e1) == J(e2) and J(s1) == J(s2), "| fixture data changed by pass 1:", leak)
same = [e["fixture_id"] for e in e1 if J(e) == J(ER[e["fixture_id"]])]
print("identical to the executor's evaluation objects:", len(same), "/", len(e1), "| differing:", [e["fixture_id"] for e in e1 if e["fixture_id"] not in same])
exp_stops = [s for s in R["stops"] if s["fixture"].startswith("INJ-")]
print("INJ stops identical to the executor's:", J(s1) == J(exp_stops), [(s["fixture"], s["stop"]) for s in s1])
print("INCONSISTENT_U stop record (auditor run):", [s for s in s1 if s["fixture"] == "INJ-U-POST-CONSTRUCTION-INVALID"])
expected_pending = {"INJ-SPL-PENDING-FULL": ["C3", "C4b"], "INJ-SPL-PENDING-FOLD": ["C2"], "INJ-SPL-PENDING-PROBE": ["C4b"]}
for fid, crits in expected_pending.items():
    e = [x for x in e1 if x["fixture_id"] == fid][0]
    pend = sorted(f"{fam}:{c}:{sx}" for fam in ("P01", "P02") for c in e["criteria"][fam] for sx in ("F", "M")
                  if "status" in e["criteria"][fam][c][sx])
    print("  %-22s pending cells %s | expected %s | C4a F passed %s | p03 %s | mech %s" % (fid, pend,
          sorted(f"{fam}:{c}:F" for fam in ("P01", "P02") for c in crits), e["criteria"]["P01"]["C4a"]["F"].get("passed"),
          (e["p03"]["P01"], e["p03"]["P02"]), e["mechanism_outcome"]))
ta = h.t_a5_support(); tc = h.t_comparator_nan(); uu = h.ut_uset_construction(gen)
print("t_a5_support equal to delivered:", J(h.canon(ta)) == J(TE["t_a5_support"]), "| pass:", ta.get("pass_"))
print("t_comparator_nan equal to delivered:", J(h.canon(tc)) == J(TE["comparator_nan"]), "| pass:", tc.get("pass_"), "| label:", tc.get("guarded_comparator_label"))
print("ut_uset_construction equal to delivered:", J(h.canon(uu)) == J(TE["uset_construction"]), "| cases ok:", {k: v.get("ok") for k, v in uu.items()})
print("guard:", {repr(v): h._guarded_scalar_ok(v) for v in (0.5, float("nan"), float("inf"), None)})
```

Block [4] — r41_04_realpath_probe.py (output in §5.2):

```python
"""Evidence script 04 (F3 STEP-2 r4-1 independent audit; auditor claude-opus-5-5; 2026-09-30). [A-S] probe of the
real-path half of R4A-01: the UNMODIFIED r4-1 harness functions run_real_scenario and evaluate_fixture are called on
the generator's REAL_SCENARIOS, with the two numerical engines replaced by auditor stubs (fit_family always
eligible; fit_spline valid except in the contexts a case names, where it returns the failure string the real
fit_spline returns for an UNRELATED event). The stubs make the probe fast and deterministic; what it tests is the
control flow the executor's tests do not reach: which spline failures set spl_pending_* on the real path, and how
evaluate_fixture routes them with c4_source = "REAL". Numerical values produced under the stubs mean nothing."""
import importlib.util, sys, json, hashlib, warnings
import numpy as np
warnings.filterwarnings("ignore")
HP = "G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py"
spec = importlib.util.spec_from_file_location("h_r41p", HP); h = importlib.util.module_from_spec(spec); sys.modules["h_r41p"] = h; spec.loader.exec_module(h)
gs = importlib.util.spec_from_file_location(h.GEN_MODULE_NAME, h.GEN_PATH); gen = importlib.util.module_from_spec(gs); sys.modules[h.GEN_MODULE_NAME] = gen; gs.loader.exec_module(gen)
print("harness sha256:", hashlib.sha256(open(h.__file__, "rb").read()).hexdigest())
REAL = {sc["fixture_id"]: sc for sc in gen.REAL_SCENARIOS}
print("REAL_SCENARIOS:", {k: (len(v["strata"]["F"]), [(i["traj"], i["family"], i["context"], i["mode"]) for i in v["injections"]]) for k, v in REAL.items()})

def smooth(x):
    k = 5; pad = np.pad(np.asarray(x, dtype=float), (k // 2, k // 2), mode="edge"); return np.convolve(pad, np.ones(k) / k, mode="valid")
PLAN = {}
def stub_family(f2m, grids, fixture_id, family, x, obs_idx, telemetry, mask_id, **kw):
    return dict(eligible=True, ghat=smooth(x), theta=np.ones(len(h.W_C5[family])), L=0.0, start_bank_size=0,
                feature_start_rejected=False, failure_codes=[])
def stub_spline(spl, fixture_id, x, obs_idx, telemetry, mask_id, inject_failure=False):
    if inject_failure:     # same return as the real fit_spline for a declared (ordinary) injected failure
        return dict(valid=False, failure="TEST_ONLY_INJECTION_SPLINE_FAILURE")
    if mask_id in PLAN:    # same return shape as the real fit_spline after an UNRELATED event
        return dict(valid=False, failure=PLAN[mask_id], per_mode_valid={})
    return dict(valid=True, ghat=smooth(x), mode=0, rss=0.0, equivalent_modes=[0], per_mode_valid={})
h.fit_family, h.fit_spline = stub_family, stub_spline

NAT, INJ = "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"
cases = [("SCEN-A", "baseline (no event)", {}),
         ("SCEN-A", "natural event, F0 full", {"probe:F0:full": NAT}),
         ("SCEN-A", "natural event, F0 fold2", {"probe:F0:fold2": NAT}),
         ("SCEN-A", "natural event, M0 probeL", {"probe:M0:probeL": NAT}),
         ("SCEN-A", "injected UNRELATED event, F0 full", {"probe:F0:full": INJ}),
         ("SCEN-A", "injected UNRELATED event, F0 fold2", {"probe:F0:fold2": INJ}),
         ("SCEN-B", "declared spline failure only (manifest)", {})]
for fid, label, plan in cases:
    PLAN.clear(); PLAN.update(plan)
    recs, n_s, tel, ca, fmf = h.run_real_scenario(None, None, None, REAL[fid], "probe", [])
    flags = {sx: {k: recs[sx]["SPL"][k] for k in ("spl_pending_full", "spl_pending_fold", "spl_pending_probe")} for sx in ("F", "M")}
    stops = []
    ev = h.canon(h.evaluate_fixture(fid, recs, n_s, "REAL", {}, stops))
    pend = sorted(f"{fam}:{c}:{sx}={ev['criteria'][fam][c][sx]['status']}" for fam in ("P01", "P02") for c in ev["criteria"][fam]
                  for sx in ("F", "M") if "status" in ev["criteria"][fam][c][sx])
    spl_full = {sx: recs[sx]["SPL"]["full"] for sx in ("F", "M")}; spl_cc = {sx: recs[sx]["SPL"]["cc"] for sx in ("F", "M")}
    print("\n[%s] %s" % (fid, label))
    print("  flags:", {sx: {k.replace("spl_pending_", ""): v for k, v in f.items()} for sx, f in flags.items()}, "| SPL full:", spl_full, "| SPL cc:", spl_cc)
    print("  pending cells:", pend or "none")
    print("  p03:", (ev["p03"]["P01"], ev["p03"]["P02"]), "| mechanism:", ev["mechanism_outcome"], "| stops:", [s["stop"] for s in stops])
    if not pend:
        definite = sorted(f"{fam}:{c}:{sx}={'PASS' if ev['criteria'][fam][c][sx].get('passed') else 'FAIL'}" for fam in ("P01", "P02")
                          for c in ("C2", "C3", "C4b") for sx in ("F", "M"))
        print("  C2/C3/C4b definite outcomes:", definite)
```

Block [5] — r41_05_line_facts.py (output in §8):

```python
"""Evidence script 05 (F3 STEP-2 r4-1 independent audit; auditor claude-opus-5-5; 2026-09-30). Read-only.
Prints, with line numbers, the lines of the delivered r4-1 harness (4e0dc8cf...) that the record cites."""
import hashlib
P = "/home/claude/audit_r41/recv4/f3_step2_adequacy_harness_r4-1_2026-09-29.py"
b = open(P, "rb").read(); L = b.decode("utf-8").split("\n")
print("harness sha256:", hashlib.sha256(b).hexdigest(), "| lines:", len(L))
SPANS = [("fit_spline: a declared injected failure returns TEST_ONLY_INJECTION_SPLINE_FAILURE (no STOP prefix)", 965, 976),
         ("fit_spline: an UNRELATED event returns STOP_EXACTNESS_PENDING(<tag>)", 1065, 1076),
         ("evaluate_fixture: routing tag from c4_source", 1283, 1285),
         ("evaluate_fixture: C2 <- spline fold context", 1300, 1308),
         ("evaluate_fixture: C3 <- spline full context", 1335, 1341),
         ("evaluate_fixture: C4b <- spline full or probe context", 1378, 1386),
         ("run_real_scenario: full-context flag (TEST_ONLY excluded)", 1924, 1929),
         ("run_real_scenario: fold-context flag (TEST_ONLY excluded)", 1951, 1957),
         ("run_real_scenario: probe-context flag (TEST_ONLY excluded)", 1961, 1968),
         ("main: a natural UNRELATED event opens F3-STEP2-EXACT-04", 3082, 3088),
         ("run_dp04: offending pairs keyed (sex, fitter, observation); first hit is the record's sex", 1713, 1725),
         ("run_dp04: guarded comparator STOP label (R4A-03)", 1770, 1776),
         ("main: W-3 custody record verified by assertion before any computation", 2745, 2764),
         ("T-EXC-UNRELATED-TYPE: the only UNRELATED injection is armed around a direct fit_spline call", 2333, 2337),
         ("MANDATORY_TESTS (T-NONREG-R4 not listed)", 219, 228)]
for title, a, z in SPANS:
    print("\n-- %s (L%d-%d)" % (title, a, z))
    for n in range(a, z + 1): print("%5d: %s" % (n, L[n - 1]))
```

Block [6] — r41_06_code_diff.py:

```python
"""Evidence script 06 (F3 STEP-2 r4-1 independent audit; auditor claude-opus-5-5; 2026-09-30). Read-only.
Non-comment line changes between the audited r4 harness (54274b4e...) and the r4-1 harness (4e0dc8cf...), grouped by
the enclosing top-level definition of the r4-1 file; the lines themselves are printed for the fitting and
real-path functions."""
import difflib, hashlib, re
A = "/home/claude/audit_r4/recv/f3_step2_adequacy_harness_r4_2026-09-24.py"
Bp = "/home/claude/audit_r41/recv4/f3_step2_adequacy_harness_r4-1_2026-09-29.py"
a = open(A, encoding="utf-8").read().split("\n"); b = open(Bp, encoding="utf-8").read().split("\n")
print("r4 harness", hashlib.sha256(open(A, "rb").read()).hexdigest()[:16], "| r4-1 harness", hashlib.sha256(open(Bp, "rb").read()).hexdigest()[:16])
def owner(lines):
    own, cur = [], "<module>"
    for l in lines:
        m = re.match(r"^(?:def|class) (\w+)", l)
        if m: cur = m.group(1)
        elif l and not l[0].isspace() and not l.startswith(("#", ")", "]", "}", "@")): cur = "<module>"
        own.append(cur)
    return own
oa, ob = owner(a), owner(b)
is_code = lambda l: l.strip() and not l.strip().startswith("#")
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
changed = {}
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal": continue
    for i in range(i1, i2):
        if is_code(a[i]): changed.setdefault(oa[i], []).append(("-", i + 1, a[i]))
    for j in range(j1, j2):
        if is_code(b[j]): changed.setdefault(ob[j], []).append(("+", j + 1, b[j]))
for fn in sorted(changed, key=lambda k: min(n for _, n, _ in changed[k])):
    print("%-34s %3d changed code lines" % (fn, len(changed[fn])))
SHOW = ("fit_family", "fit_spline", "acf_classical", "rho_cv_pin", "rmse_edge_pin", "s_stab_pin", "median_pin", "crit_stats", "run_real_scenario")
for fn in SHOW:
    print("\n-- %s: %s" % (fn, "no code change" if fn not in changed else "%d changed code lines" % len(changed[fn])))
    for sign, n, l in changed.get(fn, []):
        print("  %s L%-5d %s" % (sign, n, l.strip()[:130]))
```

```text
r4 harness 54274b4e1edfb13f | r4-1 harness 4e0dc8cfb81543ee
<module>                            79 changed code lines
fit_spline                           2 changed code lines
evaluate_fixture                    27 changed code lines
run_dp04                            22 changed code lines
run_real_scenario                   19 changed code lines
t_comparator_nan                    26 changed code lines
_exc_injection_pass                 32 changed code lines
main                                97 changed code lines

-- fit_family: no code change

-- fit_spline: 2 changed code lines
  - L1036  tag = "TEST_ONLY_INJECTION" if all_test_only else "F3-STEP2-EXACT-04"
  + L1074  tag = "TEST_ONLY_INJECTED" if all_test_only else "F3-STEP2-EXACT-04"

-- acf_classical: no code change

-- rho_cv_pin: no code change

-- rmse_edge_pin: no code change

-- s_stab_pin: no code change

-- median_pin: no code change

-- crit_stats: no code change

-- run_real_scenario: 19 changed code lines
  - L1734  rL=[], rR=[], sst=[], a5v=[]) for k in ("P01", "P02", "SPL")}
  + L1836  rL=[], rR=[], sst=[], a5v=[],
  + L1841  spl_pending_full=[], spl_pending_fold=[],
  + L1842  spl_pending_probe=[])
  + L1843  for k in ("P01", "P02", "SPL")}
  + L1927  recs["SPL"]["spl_pending_full"].append(
  + L1928  str(spf.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
  + L1929  and "TEST_ONLY" not in str(spf.get("failure", "")))
  - L1828  cc, pred_cv = True, np.full(T, np.nan)
  + L1943  cc, pred_cv, fold_pending = True, np.full(T, np.nan), False
  + L1954  if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
  + L1955  and "TEST_ONLY" not in str(r.get("failure", ""))):
  + L1956  fold_pending = True   # R4A-01: any fold unverifiable
  + L1957  recs["SPL"]["spl_pending_fold"].append(fold_pending)
  + L1961  probe_pending = False
  + L1966  if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
  + L1967  and "TEST_ONLY" not in str(r.get("failure", ""))):
  + L1968  probe_pending = True   # R4A-01: either probe unverifiable
  + L1975  recs["SPL"]["spl_pending_probe"].append(probe_pending)
```
