# Custody supersession note — attempt 8 crashed before results-writing

- Trigger: attempt 8 (revision 4, the P-1..P-7 corrections) resumed from the restart store
  and ran to the point of writing `results.json`, then hit
  `AssertionError: T-CALLCOUNT: RUN1 per-call total must equal RUN2 per-call total` --
  `percall_by_phase = {"run2": 5256}`, zero `"run1"` entries. `main()` never reached
  results-writing, so (as with the very first interruption) there is no partial
  results/telemetry/residual-series/test-evidence artifact to preserve or discard --
  only the harness bytes and the W-3 custody record needed quarantining.
- Root cause: RUN1's real-scenario fixtures were already cached from attempt 6 (which had
  fully computed them before an external interruption). On this attempt, every
  `ckpt_load(ckey)` for RUN1 HIT, so `run_real_scenario`/`fit_spline` never re-executed --
  meaning the phase-tagged rows those calls append live to `SPLINE_TELEMETRY_CALLS` were
  never produced, and nothing replayed them from the cached payload either (unlike
  `EXC_CAPTURES`, which already had an `exc_snapshot`-based replay). A correctness gap in
  this cycle's OWN P-2/P-3 fix, caught by the very T-CALLCOUNT assertion that fix added --
  the assertion did its job.
- Fix: `one_run`'s per-fixture cache payload gained a 7th element,
  `tel_calls_snapshot = SPLINE_TELEMETRY_CALLS[n_tel_before:]` (the slice appended during
  that fixture's fresh computation), replayed via `SPLINE_TELEMETRY_CALLS.extend(...)` on a
  cache hit -- the same snapshot/replay shape already proven correct for `EXC_CAPTURES`.
- Quarantined, byte-verified:
  - harness: `f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py`
    sha256 = `99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a`
  - custody: `f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md`
    sha256 = `2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657`
- Note on the live-path results/telemetry/residual_series/test_evidence files: these are
  unchanged leftovers from the already-quarantined attempt-5 run (the earlier quarantine
  step copied rather than moved them, so the live path still holds attempt 5's bytes,
  verified identical to their own quarantined copies). Not attempt 8's output -- attempt 8
  produced none. Superseded by whatever this revision's own successful run writes and
  prints its own hashes for; verify against THOSE hashes, not file-existence alone.
- `commit = false`.
