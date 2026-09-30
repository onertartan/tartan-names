# Custody supersession note — r4 attempts 5-6 -> revision 5 (cross-run mutation leak)

- Trigger: r4 attempt 6 (revision 4, harness
  `90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805`, resuming attempt 5's
  store) again STOPPED on `T-CANON`: RUN1 `777fca02...` != RUN2 `148db2d1...` (exit 1 per
  the log's own EXIT_CODE line). The hash PAIR changed versus attempts 3-4
  (`19454f65...`/`bfa626a6...`), proving the k05 fix (revision 4) removed one divergence
  source; a second, independent one remained.
- Root cause (executor's own Y-03(ii) implementation, introduced this cycle): the
  post-construction corruption for INJ-U-POST-CONSTRUCTION-INVALID wrote NaN directly into
  lists inside the GENERATOR's module-level fixture object (`fx["strata"]` is built once at
  import). RUN1's evaluation mutated it permanently; when RUN2 re-evaluated the same
  fixture, crit_stats saw the NaN at BUILD time, membership excluded the observation up
  front, the INCONSISTENT_U path never fired, and the fixture's RUN2 evaluation object
  (and stops record) differed from RUN1's -- canonical divergence by shared-state
  mutation, in any process layout. T-CANON again did exactly its job.
- Fix (revision 5): the mutation is recorded and RESTORED immediately after run_dp04
  returns (visible only to the re-validation window it exists to test). Everything else
  unchanged.
- Both prior verified properties held again in attempt 6 before the gate:
  T-EXPECT-ALL 33/33 with EXPECTATION_FAIL = [] (all four D-5-pinned PI_RULE outcomes),
  T-SCHEMA missing=[], EXC_CAPTURES_RUN1_EQ_RUN2 True, NATURAL_UNRELATED_EVENTS 0,
  FIDELITY 5/5, residual series byte-identical to the r3 verified export.
- Store handling per D-3 S8.3 (harness change => store quarantined whole, next attempt
  starts empty): 11,869 units moved to `quarantine/r4_restart_store_ATTEMPT5-6_MUTATION_LEAK/`.
- Quarantined byte-exact BEFORE any edit (sha256sum-verified):
  - harness: `f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py`
    sha256 = `90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805`
  - custody: `f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.md`
    sha256 = `cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273`
  - run logs: attempt-5 stdout, attempt-6 stdout/stderr (in this directory).
- Attempt numbering: attempts 5 (interrupted late in RUN2) and 6 (completed, T-CANON
  stop) ran revision 4; next launch is attempt 7, revision 5.
- `commit = false`.
