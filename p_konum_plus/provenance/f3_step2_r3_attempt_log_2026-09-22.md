# p_konum_plus - F3 STEP-2 r3 - Attempt Log (deliverable 12)

```text
artifact_role = attempt log required by T-R2-2 = AUTHORIZE_RESTART (S8.3) and T-RESTART-PROVENANCE
status        = NON-NORMATIVE (a disclosure record; the hashed results/custody files are authoritative)
date          = 2026-09-22 (cycle) ; log covers process launches through 2026-09-24
```

Two counters appear below and are NOT the same thing:
- **harness revision** — increments only when the harness's own bytes change (a real code
  edit, always followed by a fresh W-3 custody record per S3's rule).
- **process launch** (this log's row order) — every `python ...` invocation, whether it
  completed, was interrupted, or crashed. Several launches can share one revision (a
  resumed process reruns byte-identical code so the restart store's fingerprint still
  matches).

Every process below ran with `real_data_access = false`.

| # | harness rev | pid | start | end / stopped at | outcome |
|---|---|---|---|---|---|
| 1 | 1 (`6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31`, `RESTART_LAYER_ACTIVE=False`) | 4220 | 2026-09-22T12:22:28.806647 | stopped at RUN2 SCEN-A:F0:fold0 (ctx 41) | **interrupted** — host process exited outside harness control; no partial results existed (main() had not reached results-writing). Trigger for introducing the restart layer. See `quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md`. |
| 2 | 2 (`891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd`, restart layer introduced) | 5232 | 2026-09-22T14:43:48.833968 | stopped at RUN2 SCEN-A:F0:fold4 (ctx 45) | **interrupted**, same external pattern. Restart store began accumulating (7,943 entries by this point). |
| 3 | 2 (same bytes as #2, resumed) | 8740 | 2026-09-23T13:37:05.516474 | `RUN_COMPLETE 8740`, exit 0 | **completed**, but later found defective: the post-hoc exception classifier (`_classify_call_site()` called from inside `wrapped_accept`'s `except` block) could never see the covered call site, because `inspect.stack()` from inside an except handler only sees the ALREADY-UNWOUND stack. Found and fixed before being reported as final. Harness + custody + all 4 outputs quarantined. See `quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md`. |
| 4 | 3 (`d67e097dc158c4909276b026ce66533f33dfab7a94d800e57342eb86e76f58ff`, classifier fixed) | 21380 | 2026-09-23T13:56:21.156411 | stopped at RUN2 SCEN-A:F0:fold1 (ctx 42) | **interrupted**, same external pattern. |
| 5 | 3 (same bytes as #4, resumed) | 24220 | 2026-09-23T19:32:32.616091 | end 2026-09-23T19:50:36.580655, exit 0 | **completed**, verified: RUN1==RUN2 (`943d14ab...`), natural exception correctly `COVERED`, all non-regression gates PASS. Reported as final; independent auditor preflight (claude-fable-5-1, 2026-09-23) then found P-1..P-7 on the delivered package. |
| 6 | 4 (`f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5`, P-1..P-7 corrections) | 18036 | 2026-09-23T21:51:13.308056 | stopped at RUN2 SCEN-A:F0:full (ctx 40) | **interrupted**, same external pattern. Restart store had been reset empty at the start of this revision (23,738 pre-revision-4 entries quarantined whole to `quarantine/r3_restart_store_2026-09-22_ATTEMPT1-5_PRE_AUDIT_P1-P7_CORRECTIONS/`). |
| 7 | 4 (same bytes as #6) | — (never started) | 2026-09-24 | Python never opened the script | **operator error, not a harness or environment event**: a `cd` from an unrelated verification command in the same shell session persisted into this invocation, so the relative path to the harness resolved to a nonexistent doubled path (`.../provenance/p_konum_plus/calibration/...`). No process was created. Corrected by using an absolute path for every launch from here on. |
| 8 | 4 (same bytes as #6, resumed via absolute path) | 15252 | 2026-09-24T11:37:01.875876 | reached results-writing, then `AssertionError: T-CALLCOUNT: RUN1 per-call total must equal RUN2 per-call total` (`{"run2": 5256}`, no `"run1"` key) | **crashed on its own new assertion** — a real gap in this cycle's own P-2/P-3 fix: a fixture-level cache HIT never re-enters `run_real_scenario`/`fit_spline`, so the phase-tagged per-call telemetry those calls append live was never replayed from the cached payload (unlike `EXC_CAPTURES`, which already had snapshot+replay). No results/telemetry/residual/test-evidence artifact exists for this launch — crashed before that stage. See `quarantine/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md`. |
| 9 | 5 (`99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a`, telemetry-replay fixed) | 10920 | 2026-09-24T12:02:04.573394 | stopped at RUN1 SCEN-A:M0:probeR (ctx 23) | **interrupted**, same external pattern. |
| 10 | 5 (same bytes as #9, resumed via absolute path) | 1240 | 2026-09-24T14:27:44.558016 | end 2026-09-24T14:51:59.765920, exit 0 | **completed, verified**: RUN1==RUN2 (`7d40df61...`), `T_CALLCOUNT` `{"run1": 5256, "run2": 5256}` (balanced), `T_EXPECT_ALL` 33/33 declared with `EXPECTATION_FAIL=[]`, S2 exception test shows both stages `[1, 2]`, `FIDELITY = 5/5` (declared injection sites), determinism and all non-regression gates confirmed against on-disk file hashes, not just printed values. **This is the current, final state.** |

## T-RESTART-PROVENANCE (Y-01), checked against row 10 (the only process whose output is live)

1. Every unit row 10 read from the store carries the identity (code+input+environment
   fingerprint) that row 10 itself computed at start — enforced structurally: `ckpt_load`
   prefixes every key with `_CODE_ENV_FINGERPRINT[0]`, computed fresh each process from the
   live harness/generator/manifest hashes, so a key collision across different bytes is not
   possible by construction, not by convention.
2. No RUN2 unit was read from a unit computed for RUN1: `one_run("run1")` and
   `one_run("run2")` key their per-fixture cache as `"realscen_run1_<fixture_id>"` /
   `"realscen_run2_<fixture_id>"` — disjoint namespaces.
3. Every process that computed a unit surviving into row 10's output is in this table (rows
   1-10) and ran under harness bytes that are either row 10's own
   (`99f895c1...`) or an ancestor superseded through a disclosed chain of hash-verified
   quarantine notes (rows 1-9 above) -- no undisclosed process boundary remains.

T-SINGLE-PROCESS does not apply to row 10's own output (units came from more than one
process across the resume chain; `units_read_from_store` in `results.json`'s `process` block
for row 10 is non-empty for `nr_gates` and `unit_tests`, confirming a store read actually
occurred). T-RESTART-PROVENANCE takes its place, per S8.3.

## Progress rule (S8.3 "progress")

No two consecutive processes in this table completed with zero new units computed — every
interrupted or crashed launch nonetheless persisted real forward progress to the store
(confirmed by growing `PROGRESS SPL ctx` counts and, for row 8, by reaching results-writing
before crashing). The two-in-a-row STOP condition was never reached.

`commit = false`.
