# Custody supersession note — F3 STEP-2 r3, attempt 1 -> attempt 2

- Trigger: attempt 1 (`RESTART_LAYER_ACTIVE = False`, no checkpointing, one clean process per
  S8.1) was launched as a background process. It completed RUN1 in full (SCEN-A, SCEN-B, and every
  pre-flight pin/test — NR-01(i)/(ii), spline non-regression, loader node-hash check,
  masked-objective pins, A5 unit tests, U-set construction, exception-injection fixtures,
  FIX-STARTS-*, FIX-A5-TRUE — all PASS) and reached partway into RUN2 (SCEN-A, F0, fold0) before
  the task runtime reported `status=stopped`: "No completion record was found for this background
  shell command from the previous session... may have been stopped... or may have been running
  when the previous Claude Code process exited." This is a genuine interruption external to the
  harness — not a harness defect, not a voluntary stop, and not something the harness's own code
  could have caught — the trigger condition for introducing a restart layer under
  `T_R2_2 = AUTHORIZE_RESTART` (S8.2/S8.3).
- No results/telemetry/residual-series/test-evidence artifact exists for attempt 1: `main()` never
  reached results-writing. There is therefore no partial results artifact to preserve or discard —
  only the harness bytes and the W-3 custody record they produced needed quarantining.
- Action: the attempt-1 harness bytes and its W-3 custody record were COPIED byte-exact (originals
  left in place; the live harness is then edited, and the live custody record is overwritten by the
  harness's own next run — see below) to `p_konum_plus/quarantine/` under `*_ATTEMPT1_SUPERSEDED`
  names, hash-verified equal before and after placement via `sha256sum`:
  - harness bytes: `f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py`
    sha256 = `6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31`
  - custody record: `f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT1_SUPERSEDED.md`
    sha256 = `c8d47629ea56e8228a3ac7358ca4c4cd10d339403a32e6a54ed314966f6688bd`
- Live-path change: `p_konum_plus/calibration/f3_step2_adequacy_harness_r3_2026-09-22.py` is edited
  in place — `RESTART_LAYER_ACTIVE` flips `False -> True`; three `SUPERSEDES_*` constants are added
  naming this note and the two quarantined hashes above, disclosed in the next W-3 record; no other
  behavioral code changes. Per S3's rule, a harness change after W-3 is written requires W-3 to be
  repeated with a new record. `p_konum_plus/provenance/f3_step2_r3_preexecution_custody_2026-09-22.md`
  is therefore overwritten in place by the harness's own next run, producing a fresh record under
  the new harness hash that cites this note; the pre-edit content of that path is the
  `_ATTEMPT1_SUPERSEDED` copy above, not lost.
- Restart store: `p_konum_plus/calibration/.r3_restart_store_2026-09-22/` is created empty by
  attempt 2 (the first attempt with the layer active), per S8.3.
- Generator and manifest are untouched by this change (same bytes, same hashes as attempt 1).
- `commit = false`.
