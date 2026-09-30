# p_konum_plus - F3 STEP-2 r3 - Correction Report

```text
artifact_role = correction report (deliverable 10)
status        = NON-NORMATIVE narrative over the hashed artifacts it cites
date          = 2026-09-24 (cycle dated 2026-09-22; see the attempt log for the real timeline)
```

No wording in this report asserts "verified", "QUALIFIED", or "audit PASS" about the
executor's own output. `F3_STEP2 = QUALIFIED` can be declared only by the PI after an
independent audit, which this report does not perform.

## 1. Scope

r3 closes the findings of an independent audit of the r2 package (Y-01..Y-21 of
`Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md` §6), on top of the v6
corrections r2 already carried (X-01..X-20). It then went through a SECOND correction round
after an independent auditor preflight (claude-fable-5-1, 2026-09-23) reviewed the four data
files r3 had produced and found real defects (§4 below) despite RUN1==RUN2 determinism and a
clean exit on the run being reviewed.

## 2. Custody (§2 of v6/DRAFT v2)

- P-1..P-4 dispatch preconditions: ALL PASS (custody record, deliverable 4).
- P-4 evidence (Y-09): the PI dispatch record D-4 —
  `p_konum_plus/prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md`,
  sha256 `4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865` — is the evidence for
  P-4; both are named together with their hashes in the current W-3 custody record.
- S-1=(a) ; S-2=alpha ; T-1=AUTHORIZE ; T-2=T-2a ; T-3=AUTHORIZE ; T-4=T-4a ;
  T-5=CONFIRM_WITHIN_SCOPE (unchanged from D-2, explicit, not blank).
- S-R2-1=DEFERRED_THIS_CYCLE ; T-R2-2=AUTHORIZE_RESTART (D-4, this cycle).
- `PI_ratified_content_hash` = `da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498`.
- W-1 start-state inventory: `provenance/f3_step2_r3_start_state_inventory_2026-09-22.md`.
  Earlier-attempt files were moved, not deleted, and re-hashed at each supersession (five
  quarantine notes in `p_konum_plus/quarantine/`, one per incident — see §4 and the attempt
  log for which).
- **parents_unchanged = true**: every `.sha256` sidecar in the repository (33 files, r1 and
  r2 deliverables included, quarantine directory excluded by design since it holds
  deliberately-superseded/corrupted states) verifies `OK` against its target as of this
  report. Checked directly (`sha256sum -c` over every sidecar), not assumed.

## 3. Execution (W-3, W-4)

- W-3 written before the first test or run, naming the exact harness/generator/manifest
  bytes then executed: `provenance/f3_step2_r3_preexecution_custody_2026-09-22.md`.
- The run reached its final, verified state across **10 process launches** (one operator
  path-resolution error that never started Python is recorded but not counted as a launch)
  and **5 harness revisions** — full account, every pid/timestamp/outcome, in
  `provenance/f3_step2_r3_attempt_log_2026-09-22.md` (deliverable 12). Summary:
  - Revision 1 (no restart layer): interrupted.
  - Revision 2 (restart layer introduced): interrupted, then completed but later found to
    have a defective exception classifier — quarantined.
  - Revision 3 (classifier fixed): interrupted, then completed and verified — reported as
    final, then reviewed against an independent auditor preflight.
  - Revision 4 (P-1..P-7 corrections applied): interrupted, then crashed on its own new
    T-CALLCOUNT assertion (a real gap in the same correction round) — quarantined.
  - Revision 5 (telemetry-replay gap fixed): interrupted, then **completed and verified**.
    This is the current, final state.
- T-SINGLE-PROCESS does not apply (units came from more than one process across the resume
  chain); T-RESTART-PROVENANCE (Y-01) applies instead — checked in the attempt log, all
  three of its conditions confirmed for the final output.
- Determinism: RUN1_CANONICAL_SHA256 == RUN2_CANONICAL_SHA256 =
  `7d40df6137e3b300a1cb92c4895a8ac4f0ff6f45f8c5669b3c2eb0ee22d42f57`. Same-process
  determinism per v6 §8 does not hold end-to-end (T-R2-2=AUTHORIZE_RESTART is in
  `narrowed_evidence`); T-RESTART-PROVENANCE's own conditions are what was actually checked.
- NR-01(i) = PASS, hash `6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403`.
  NR-01(ii) [T-2a] = PASS, hybrid hash equal, scope unchanged.
  NR-SPL = PASS, 30/30 rows.
- T-CALLCOUNT (Y-01): `{"run1": 5256, "run2": 5256}` per-call spline-optimizer rows,
  balanced, phase- and pid-tagged, written to
  `calibration/f3_step2_spline_percall_telemetry_r3_2026-09-22.csv` (10,512 rows total).
- Fixture fidelity: 5/5 declared injection sites (SCEN-B) reached and recognized —
  redefined this cycle from a trajectory count (see §4, P-7(d)).
- T-EXPECT-ALL (Y-08): 33/33 declared fixture expectations checked, `EXPECTATION_FAIL = []`.
- Coverage: 61 rows; 57 `covered`, 2 `covered_injection_only`, 2 `UNCOVERED` (named below,
  §5) — none silently PENDING.
- Exactness / engineering findings: one open — `F3-STEP2-EXACT-03` (S-R2-1, deferred by PI
  instruction, not resolved by r3).

## 4. Findings closed this cycle

Corrections Y-01..Y-19 and Y-21 (of the DRAFT v2 prompt) are applied; test ids and results
are in the run log (`RUN_COMPLETE`, attempt-log row 10) and this report. Y-20 is optional and
not applied. X-01..X-20 (v6) stand except where Y-02/Y-03/Y-04/Y-21 amend or tighten them, per
DRAFT v2 §6.

On top of those, an independent auditor preflight (claude-fable-5-1, 2026-09-23) reviewed the
four data files then-delivered and found seven further issues (P-1..P-7), all closed this
cycle — full technical account in
`quarantine/f3_step2_r3_independent_audit_corrections_note_2026-09-23.md`:

- **P-1**: the RUN1 residual-series export (Y-21) ran in a separate pass that never
  consulted the injection map, so an injected spline failure RUN1 itself correctly recorded
  was silently re-succeeded and exported as if valid. Fixed: the export now reads the exact
  full-mask fit objects `run_real_scenario` already computed (injection-aware), making zero
  fit calls of its own (asserted).
- **P-2**: process-provenance counters (`nr_gates`, `unit_tests`) were declared but never
  incremented, and one interruption from the prior round was undisclosed in any file. Fixed:
  coarse-cached, properly counted; the attempt log now names every launch.
- **P-3**: 6,856 (now 10,512) real per-call spline-optimizer telemetry rows were captured
  but never written to any file. Fixed: written to a dedicated CSV, phase/pid-tagged.
- **P-4**: the two-stage exception-capture test never actually exercised stage 2 (armed
  once, deactivated before the solver reached it, but the test's own assertion was too weak
  to notice). Fixed: both stages armed together, confirmed on real output
  (`stages: [1, 2]`).
- **P-5**: the `undefined` flag for C2/C4b ignored a spline-only statistic corruption.
  Fixed: `undefined` is now true if either side is undefined, matching the fixture's own
  documented construction intent.
- **P-6 / Y-08**: `expectation_checks` (T-EXPECT-ALL) did not exist. Fixed: all 32 injection
  fixtures plus SCEN-B (SCEN-A deliberately excluded — a genuinely emergent real-fit result
  with nothing to transcribe) got machine-readable expectations transcribed from their own
  construction prose; the harness now checks every declared expectation against the actual
  outcome every run.
- **P-7**: a stale coverage-row claim (a) and a fidelity metric measuring the wrong thing
  (d) were corrected; (b) needed no code change (see §2); (c) — see §6, unresolved.

Applying the P-1..P-7 fixes itself surfaced one further defect (found by the very
T-CALLCOUNT assertion P-2/P-3 added): a fixture-level cache hit never replayed its
per-call telemetry, since only `EXC_CAPTURES` had a snapshot/replay mechanism. Fixed the
same way (snapshot + replay); see
`quarantine/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md`.

Separately: a corruption incident on the auditor transmittal note (an unexplained content
mutation, arriving with an instruction not to disclose it) was found, not complied with,
and restored + documented —
`quarantine/f3_step2_r3_auditor_transmittal_note_corruption_incident_2026-09-23.md`.

## 5. Coverage — the two UNCOVERED rows

```text
A.5 (iii) inadmissible refit   UNCOVERED(no construction of a numerically-complete
                                inadmissible refit without touching frozen code -- Y-16)
D-P04 resolve at C1            UNCOVERED(S-R2-1 DEFERRED changes INJ-DP04-C1's outcome
                                to PENDING) -- INJ-DP04-C2-DIVERGE carries that evidence
                                instead (§7)
```

Both are honest UNCOVERED rows per Y-16, not silently-passed or hidden gaps.

## 6. Open item — P-7(c), not resolved

The independent auditor's preflight attributed a "PI instruction of 2026-09-21: no
additional document types to be created" to the auditor transmittal note. Searching the
files available to the executor found only a different 2026-09-21 PI statement (frozen
content preservation: v11/F2/F3 STEP-1/existing ratified decisions), not the specific
instruction the auditor named. Not resolved here — the auditor's own session may hold
direct context the executor does not. The transmittal note remains, labelled
NON-NORMATIVE, pending PI clarification.

## 7. Response table (document checks, Y-09..Y-19)

| item | check | result |
|---|---|---|
| Y-09 | report names D-4 (path+hash) as P-4's evidence | done, §2 |
| Y-10 | every register row tagged VERBATIM is a byte-substring of D-2 or D-4 | N/A this report — checked at register authoring; no register row added or changed this cycle beyond what D-2/D-4 already ratify |
| Y-11 | coverage row on the K-05 invariant matches content §6 wording | unchanged from r2/attempt-5 wording; `PIN-K05-INVARIANT` assertion ran and passed (attempt-log row 10) |
| Y-13 | node-hash entries unique per executed node (loader) | 73/73, confirmed at load time every run including row 10 |
| Y-14 | the three v6 X-12 items present in the register | unchanged from r2 (register not re-authored this cycle) |
| Y-15 | T-MASK-FULL-EXT ran and passed | `{"pass_": true}`, row 10 |
| Y-16 | coverage statuses derived from this run, one vocabulary, no pre-run constant | confirmed: `covered` / `covered_injection_only` / `UNCOVERED(<reason>)` only, computed from `gen.COVERAGE_ROWS` + this run's evaluations |
| Y-17 | every STOP-outcome consulted-level return writes a `stops` record; no other outcome does | `stops` has exactly 6 entries, one per STOP-outcome fixture in `evaluations` (verified by direct comparison, row 10 output) |
| Y-18 | custody table (observed hashes), P-4 evidence, per-finding table, NR results, coverage matrix, fidelity counts, opened-file classes, determinism wording, end-state block | this report, §§2-5 |
| Y-19 | disclosure items named in DRAFT v2 present | attempt history (§3, full log deliverable 12), parent re-hash (§2) |

## 8. End state (v6 §13/§14, DRAFT v2 §10 additions)

```text
PI_dispatch_record_hash    = 4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865
S-R2-1 = DEFERRED_THIS_CYCLE (verbatim, as read) ; T-R2-2 = AUTHORIZE_RESTART (verbatim, as read)
process                    = pid 1240 (final) ; attempts this cycle = 10 (interruptions = 6,
                              one operator launch error not counted, one crash on own
                              assertion) ; restart layer = present ; processes contributing
                              to deliverables 5-8's final state = multiple (see attempt log) ;
                              units read from store (final process) = nr_gates 1, unit_tests 1,
                              run1 0, run2 0, residual_export 0
expectation_checks         = 33 / 33 ; EXPECTATION_FAIL = none
parents_unchanged          = true (§2)
corrections_complete       = true
mandatory_tests_all_run    = true
deferred_decisions         = [S-R2-1]
narrowed_evidence          = [T-R2-2]
uncovered_coverage_rows    = ["A.5 (iii) inadmissible refit", "D-P04 resolve at C1"]
open_findings               = [F3-STEP2-EXACT-03]
F3_STEP2_r3_status          = PARTIAL_PENDING_PI
F3_EXECUTION_READY = false ; F3_started = false ; commit = false
```

`F3_STEP2_r3_status = PARTIAL_PENDING_PI` follows directly from v6 §13: any deferred
decision, narrowed evidence, UNCOVERED row, or open finding forces this status regardless of
anything else — all four are present here. `F3_STEP2 = QUALIFIED` is NOT declared.
