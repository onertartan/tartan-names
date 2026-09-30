# Custody note — r4 attempt 2 interrupted -> revision 3 (restart layer introduced)

- Trigger: r4 attempt 2 (harness `20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306`,
  revision 2, one clean process, RESTART_LAYER_ACTIVE = False) was INTERRUPTED externally:
  pid 29296, started 2026-09-26T13:25:59, last output written ~13:59:38 (33.5 minutes in),
  stopped at `PROGRESS SPL ctx 34 SCEN-B run1:F0:probeR` with ZERO errors in stderr -- the
  host Claude Code process exited outside the harness's control (the same environment
  pattern recorded eight times across the r3 cycle's attempt log).
- Everything that ran before the interruption PASSED: custody VERIFY, P-1..P-4
  observed-hash checks (5 instruments), NR-01(i)/(ii), NR-SPL, T-LOADER-NODES,
  T-MASK-FULL-EXT, pins, T-A5-SUPPORT 10/10, A5 unit tests, UT-PROBE-DECOUPLE (second
  half included), UT-USET-CONSTRUCTION (case (d) under the PI_RULE architecture),
  T-COMPARATOR-NAN (real guard), T-STARTS-*, FIX-A5-TRUE, INJ-EXC-* two passes
  identical WITH the corrected context-unverifiable behavior
  (`context_unverifiable: true`, `pass_: true` -- the attempt-1 fix confirmed working),
  and RUN1 through SCEN-B F0. No results artifact exists (interrupted before
  results-writing); with the layer off, nothing was persisted -- by design (D-3 S8.1).
- This is the FIRST genuine interruption of the r4 cycle: per D-3 S8.2/S8.3 and
  T-R2-2 = AUTHORIZE_RESTART (as read from D-5), the restart layer is now introduced.
  Revision 3 = revision 2 + RESTART_LAYER_ACTIVE True + updated SUPERSEDES_*/ATTEMPT
  constants + this note's reference. No behavioral logic changes. Store
  `p_konum_plus/calibration/.r4_restart_store_2026-09-24` starts EMPTY.
- Quarantined byte-exact BEFORE any edit (sha256sum-verified pairs):
  - harness: `f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py`
    sha256 = `20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306`
  - custody: `f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT2_INTERRUPTED.md`
    sha256 = `856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78`
  - run logs: `f3_step2_r4_attempt2_stdout_2026-09-26.log`, `f3_step2_r4_attempt2_stderr_2026-09-26.log`
- A fresh W-3 custody record is written externally (same standalone writer) under the
  revision-3 hash before the relaunch.
- `commit = false`.
