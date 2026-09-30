# Custody supersession note — r4 attempt 1 -> revision 2 (2026-09-24)

- Trigger: r4 attempt 1 (harness `f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418`,
  one clean process, RESTART_LAYER_ACTIVE = False per D-3 S8.1) STOPPED on its own new
  assertion: `T-EXC-UNRELATED-TYPE` failed with `context_unverifiable: false` -- the injected
  ValueError was caught and recorded as an UNRELATED capture (`caught_not_crashed: true`,
  `exception_type_recorded: "ValueError"`), but the fit_spline context still returned VALID.
  Python exit code 1 (captured in the log itself; the task runner's "exit 0" summary reflects
  the shell chain, not Python -- the log's own `EXIT_CODE=1` line is authoritative).
- Root cause: the context-level `any_mode_unrelated` flag was set only on the CACHED-mode
  replay path (and there wrongly exempted TEST_ONLY messages); the FRESH-compute path's
  `except` block set the per-mode `mode_unrelated` but never propagated it to
  `any_mode_unrelated`, so the context-level `STOP_EXACTNESS_PENDING(...)` return never
  fired and the remaining 145 valid modes carried the context. The r4 assertion (new this
  cycle, R3A-03) caught it -- exactly the class of defect the audit said the r3 test could
  not catch ("passes by propagated_uncaught").
- Fix (revision 2): `any_mode_unrelated = True` set in the fresh-compute except block;
  the cached-path TEST_ONLY exemption removed (ANY kind=UNRELATED capture stops the
  context; TEST_ONLY only changes the finding TAG per Y-04(b), never the stop).
- No results/telemetry/residual/test-evidence artifact exists for attempt 1 (crashed in
  the unit_tests phase, long before results-writing). No store existed (layer off).
- Quarantined:
  - harness bytes: `f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py`
    sha256 = `f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418`.
    Provenance caveat, disclosed rather than hidden: the live file was edited BEFORE a
    quarantine copy was taken (executor ordering mistake). The quarantined file is a
    RECONSTRUCTION obtained by inverting the exact two post-crash edits; its SHA256 equals
    the W-3-recorded attempt-1 hash, which makes it bit-for-bit the executed bytes -- the
    equality is the proof, not the executor's word.
  - W-3 custody record (untouched original): `f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.md`
    sha256 = `307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441`
  - attempt-1 stdout/stderr logs: `f3_step2_r4_attempt1_stdout_2026-09-24.log`,
    `f3_step2_r4_attempt1_stderr_2026-09-24.log` (the stdout log shows every pre-crash
    check PASS: custody VERIFY, P-1..P-4 observed-hash check, NR gates, T-A5-SUPPORT
    10/10, UT-PROBE-DECOUPLE second half, UT-USET case (d) under the PI_RULE
    architecture).
- Revision 2: ATTEMPT_NUMBER = 2; RESTART_LAYER_ACTIVE stays False (this was a defect
  crash, not an interruption -- D-3 S8's restart layer remains un-introduced); a fresh W-3
  custody record is written externally (same writer script) under the revision-2 hash
  before the relaunch.
- `commit = false`.
