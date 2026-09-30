# p_konum_plus — F3 STEP-2 r4-2 — Transmission List (deliverable F)

```text
artifact_role = the complete transmission set for the r4-2 revision (instruction §5 F);
                every hash OBSERVED (sha256sum, 2026-09-30). Item G: the whole auditor
                folder is also delivered as ONE zip, for transport only — the auditor
                verifies every file inside against its own sidecar; the zip's hash is
                given in the delivery message
status        = NON-NORMATIVE
final run      = attempt 2 / launch 2 (pid 10412), exit 0 ; DETERMINISM = True
                (RUN1 == RUN2 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77,
                equal to r4-1's, as T-NONREG-R4-1 requires) ; T-SINGLE-PROCESS holds
verdicts       = 15 preconditions EQUAL ; T-EXPECT-ALL 36/36 ; 30/30 recorded tests passed
                (incl. T-SPL-PENDING-REALPATH 9/9 and T-NONREG-R4-1: 37 compared,
                0 findings, stops equal) ; T-NONREG-R4 0 findings ; COVERAGE 64 rows,
                0 downgrades ; NATURAL_UNRELATED_EVENTS 0 ; end state PARTIAL_PENDING_PI
                with PI_dispatch_record_hash = D-7 observed (R41A-03)
```

Every file below has an external `.sha256` sidecar. The generator and the manifest are the
REUSED r4-1 files (instruction §5 items 2–3): transmitted again for convenience WITH their
original r4-1 sidecars; no r4-2 copy exists. No r3/r4/r4-1/quarantine file was modified,
renamed or moved; no custody record and no log was overwritten.

### Deliverables

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1  harness (attempt 2) | calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py | b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 |
| 2  generator (REUSED r4-1) | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3  manifest (REUSED r4-1) | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4  custody, attempt 2 (final attempt's) | provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md | 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1 |
| 4' custody, attempt 1 (preserved, R41A-02(a)) | provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md | ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e |
| 5  telemetry | calibration/f3_step2_telemetry_r4-2_2026-09-30.csv | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d |
| 6  results | calibration/f3_step2_results_r4-2_2026-09-30.json | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba |
| 7  residual (byte-identical to r4-1/r4/r3) | calibration/f3_step2_residual_series_r4-2_2026-09-30.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8  test evidence | calibration/f3_step2_test_evidence_r4-2_2026-09-30.json | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf |
| 9  register (child of 45a10494…) | calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md | c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c |
| 10 correction report | provenance/f3_step2_correction_report_r4-2_2026-09-30.md | 7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6 |
| 11 start-state inventory | provenance/f3_step2_r4-2_start_state_inventory_2026-09-30.md | 66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5 |
| 12 attempt log (incl. ERRATUM-3) | provenance/f3_step2_r4-2_attempt_log_2026-09-30.md | b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65 |
| A  per-call telemetry (12,174 rows, one pid) | calibration/f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv | 7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c |
| B  restart-store manifest (11,869 rows, pid 10412) | calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv | 1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95 |
| C  capture records | in items 6/8: solver_exceptions + exc_captures{,_unit_phase,_run2} + run1_eq_run2=true | — |
| D  non-regression vs r4-1 | calibration/f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d |
| D' non-regression vs r4 (retained) | calibration/f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| F  this list | provenance/f3_step2_r4-2_transmission_list_2026-09-30.md | (its sidecar) |

### Item E — launch logs and quarantine artifacts of this revision

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| launch 1 stdout | calibration/f3_step2_r4-2_launch1_stdout_2026-09-30.log | 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 |
| launch 1 stderr | calibration/f3_step2_r4-2_launch1_stderr_2026-09-30.log | d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 |
| launch 2 stdout (final) | calibration/f3_step2_r4-2_launch2_stdout_2026-09-30.log | 3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7 |
| launch 2 stderr (final) | calibration/f3_step2_r4-2_launch2_stderr_2026-09-30.log | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| attempt-1 interruption note | quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md | (sidecar) |
| attempt-1 harness bytes (copied BEFORE the edit; == custody-named hash) | quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py | 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74 |
| launch-1 log pair, quarantine copies | quarantine/f3_step2_r4-2_launch1_{stdout,stderr}_2026-09-30.log | 5d58afbb… / d688ac98… |

### Restart store (fingerprint 4ced291f15fb5afd; per-unit records in item B)

| store | location (p_konum_plus/) | units |
|---|---|---|
| attempt-2 FINAL (live) | calibration/.r4-2_restart_store_2026-09-30 | 11,869 (all pid 10412) |

### Standing instruments (in the repository; verified by hash, not re-transmitted)

r4-2 instruction `d6680338…`, D-7 `a3e70509…`, A-4 `ad222936…`, r4-1 instruction
`283ac4e2…`, D-6 `a92a0518…`, r4 instruction `e1283958…`, D-5 `0cd87ad5…`, D-3
`5b0e19ea…`, D-1 `17187d31…`, D-2 `da0c4064…`, A-1/A-2/A-3; the r4-1 results baseline
`6dd4185b…`. parents_unchanged = true (start-state inventory §2).

```text
real_data_access = false ; commit = false (within the package; the PI's separate
post-completion repository instruction is recorded in the report §8)
```
