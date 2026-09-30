# Custody supersession note — r4 attempts 3-4 -> revision 4 (k05_result nondeterminism)

- Trigger: r4 attempt 4 (revision 3, harness
  `814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f`, restart layer active,
  resuming attempt 3's store) ran RUN2 to completion and STOPPED on
  `assert record_test("T-CANON", h1 == h2)`: RUN1 canonical `19454f65...` != RUN2 canonical
  `bfa626a6...`. Python exit 1 (log's own `EXIT_CODE=1` line; the task summary's "exit 0"
  again reflects the shell chain only).
- Everything BEFORE the determinism gate passed, including every r4-specific outcome:
  T-EXPECT-ALL 33/33 with `EXPECTATION_FAIL = []` (all four D-5-pinned S-R2-1 = PI_RULE
  expectations hold: INJ-DP04-C1 -> RESOLVED_MECHANISM_P01 at C1; INJ-C4B-NOREF ->
  TERMINAL_FALLBACK_MECHANISM_P01; SCEN-B -> STOP_BOTH_FAIL_REDESIGN with V4 empty in M;
  INJ-C1-FAIL -> ONLY_P02_PASSES), T-SCHEMA missing=[], EXC_CAPTURES_RUN1_EQ_RUN2 True
  (1 natural COVERED capture in each run), NATURAL_UNRELATED_EVENTS = 0, FIDELITY 5/5,
  and the residual-series file byte-identical to r3's verified export (`3ee624f3...`).
- Root cause (executor's own new field, introduced this cycle for R3A-11): `k05_result`
  embedded the PROCESS-GLOBAL cumulative `K05_CHECK_COUNT` into each fixture's canonical
  evaluation object. The counter keeps growing across the run, so the same fixture's
  RUN2 object always carries a larger count than its RUN1 object -- canonical-document
  determinism was broken BY CONSTRUCTION, in any process layout, interrupted or not.
  T-CANON did exactly its job.
- Fix (revision 4): `evaluate_fixture` snapshots the counter at entry and embeds the
  PER-FIXTURE delta ("%d checks this fixture"), which is a pure function of the fixture's
  own data -- still computed from the real assertion counter (R3A-11), now deterministic.
- Store handling per D-3 S8.3 ("if the harness changes later (a defect fixed), the store
  goes into the quarantine folder of that attempt and the next attempt starts with an
  empty store"): the ENTIRE store (11,869 units, attempts 3-4) moved whole to
  `quarantine/r4_restart_store_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM/`. Revision 4
  starts with an empty store (full recompute, ~60 min machine time, accepted -- the rule
  exists precisely so no unit computed under superseded bytes can leak forward).
- Quarantined byte-exact BEFORE any edit (sha256sum-verified):
  - harness: `f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py`
    sha256 = `814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f`
  - custody: `f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.md`
    sha256 = `51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f`
  - run logs: `f3_step2_r4_attempt3_stdout_2026-09-26.log`,
    `f3_step2_r4_attempt4_stdout_2026-09-26.log`, `f3_step2_r4_attempt4_stderr_2026-09-26.log`
- No results/telemetry/test-evidence artifact was written by attempts 3-4 (T-CANON stops
  before results-writing). The residual-series file WAS written (its writer precedes the
  gate); it is byte-identical to the r3 verified export and is superseded by revision 4's
  own rewrite rather than separately quarantined (disclosed here).
- Attempt numbering: attempts 3 (interrupted mid-RUN2) and 4 (completed, T-CANON stop)
  ran revision 3; the next launch is attempt 5, revision 4.
- `commit = false`.
