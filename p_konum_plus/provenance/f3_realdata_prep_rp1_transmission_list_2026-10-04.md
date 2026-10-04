# p_konum_plus — F3 real-data preparation rp1 — Transmission List (deliverable T)

```text
artifact_role = the complete transmission set for the rp1 cycle (instruction §8 item T);
                every hash OBSERVED (sha256, 2026-10-04). Item Z: the whole package is
                also delivered as ONE zip, for transport only — the recipient verifies
                every file inside against its own sidecar; the zip's own hash is given
                in item Z below
status        = NON-NORMATIVE
final run      = attempt 5 / launch 5 (pid 33100), exit 0 ; DETERMINISM = True
                (RUN1 == RUN2 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77,
                unchanged since r4-1) ; T-SINGLE-PROCESS holds
verdicts       = 25 preconditions EQUAL ; T-EXPECT-ALL 36/36 ; 35/35 mandatory tests
                RAN and PASSED ; T-NONREG-R4-2 s_findings=0, e_declared=39, u_findings=0 ;
                T-NONREG-R4-1 37 compared, 0 findings ; T-NONREG-R4 0 findings ;
                COVERAGE 64 rows, 0 downgrades ; rp1_status = PREPARED_PENDING_INDEPENDENT_AUDIT
                (report §4) ; end_state.F3_STEP2_r4_status (legacy field) = PARTIAL_PENDING_PI
```

Every file below has an external `.sha256` sidecar. The generator and the manifest are
the REUSED r4-1 files (rp1 instruction §4, "nothing else changes"): transmitted again
for convenience WITH their original r4-1 sidecars; no rp1 copy exists. No r3/r4/r4-1/
r4-2/pre-existing-quarantine file was modified, renamed or moved; no custody record
and no log was overwritten; real_data_access = false throughout.

### Deliverables

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1  harness (attempt 5) | calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 |
| 2  generator (REUSED r4-1) | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3  manifest (REUSED r4-1) | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4  custody, attempt 5 (final attempt's) | provenance/f3_step2_rp1_preexecution_custody_attempt5_2026-10-02.md | 7e2ee506a2819dc1a0f579751dbfa552d2a472d50309fef2a2e0d1731a853ae9 |
| 4a custody, attempt 1 (preserved, R41A-02(a)) | provenance/f3_step2_rp1_preexecution_custody_attempt1_2026-10-02.md | f78966d063c9991c590ed29d14f5671d998184aa6515b8f658c0f956998183eb |
| 4b custody, attempt 2 (preserved) | provenance/f3_step2_rp1_preexecution_custody_attempt2_2026-10-02.md | f2d33d169c161d6d004570d7aa92c8241d136bf0bb9822e76c774adce6ec1aa4 |
| 4c custody, attempt 3 (preserved) | provenance/f3_step2_rp1_preexecution_custody_attempt3_2026-10-02.md | 239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a |
| 4d custody, attempt 4 (preserved) | provenance/f3_step2_rp1_preexecution_custody_attempt4_2026-10-02.md | 49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165 |
| 5  telemetry | calibration/f3_step2_telemetry_rp1_2026-10-02.csv | 836076827ae8b30d712191f5d3507dec6b721824acaa81bae491401d2e8f468f |
| 6  results | calibration/f3_step2_results_rp1_2026-10-02.json | ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882 |
| 7  residual (byte-identical to r4-2/r4-1/r4/r3) | calibration/f3_step2_residual_series_rp1_2026-10-02.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8  test evidence | calibration/f3_step2_test_evidence_rp1_2026-10-02.json | 809e9d043d136371fafcd158d5955853f61e67490db370d1d56761b7f8e6578d |
| 9  register (child of c281e713…) | calibration/f3_step2_class_c_pin_register_rp1_2026-10-04.md | dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066 |
| 10 correction report | provenance/f3_step2_correction_report_rp1_2026-10-04.md | bf72d3e5284639972d33cb21ee87e026015fda1dc3e4eb91e85a3a038455159c |
| 11 start-state inventory | provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md | a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d |
| 12 attempt log | provenance/f3_realdata_prep_rp1_attempt_log_2026-10-04.md | d015c3cdc505cdf816764633e885605ce2b8c305fabaf4ebe9cf1406e24a458c |
| A  per-call telemetry (12,502 rows, pid 33100) | calibration/f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv | 2648cb7feeba22f54c1cb27432d23c885ff3fb0d939ef28a596779b8a5390084 |
| B  restart-store manifest (12,453 rows, pid 33100) | calibration/f3_step2_rp1_restart_store_manifest_2026-10-02.csv | ca355af467f66a05b19e82fa3e2f515ce41a253718b0120e30fae6338d96a733 |
| B' store-read log (146 rows — attempt-5 fix) | calibration/f3_step2_rp1_store_read_log_2026-10-02.csv | 6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1 |
| C  capture records | in items 6/8: solver_exceptions + exc_captures{,_unit_phase,_run2} + run1_eq_run2=true | — |
| D  non-regression vs r4-2 | calibration/f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv | 6b98e427a819f0464adf1ca100183905ae51f24de140cc4bd4c1a9bda42d5739 |
| D' non-regression vs r4-1 (retained) | calibration/f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d |
| D'' non-regression vs r4 (retained) | calibration/f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| F1 F1-synthetic fixture manifest | calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/SYNTH_FIXTURE_MANIFEST.json | 63452ff4a8f2ad99820eac509e074fb3c3a2cfb10ea765dd0f310baa6ee387b4 |
| G  C-5 observability statement | provenance/f3_realdata_prep_rp1_c5_observability_statement_2026-10-04.md | 5d36806b1036c4169870622e73a0f2c78b4c9c943c29c8902e4e83c6cd6a4d3d |
| H  §7 size estimate | provenance/f3_realdata_prep_rp1_size_estimate_2026-10-04.md | 6d8dbe067d54c50e213779e70b30c260def5ac75e516b4bfc5436cca5e9bd541 |
| T  this list | provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md | (its sidecar) |

### Item E — launch logs and quarantine artifacts of this cycle

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| launch 1 stdout (quarantined) | quarantine/f3_step2_rp1_launch1_stdout_2026-10-02.log | 445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f |
| launch 1 stderr (quarantined) | quarantine/f3_step2_rp1_launch1_stderr_2026-10-02.log | c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b |
| launch 2 stdout (quarantined) | quarantine/f3_step2_rp1_launch2_stdout_2026-10-02.log | d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7 |
| launch 2 stderr (quarantined) | quarantine/f3_step2_rp1_launch2_stderr_2026-10-02.log | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| launch 3 stdout (quarantined; resumed sub-process only — see attempt log §7) | quarantine/f3_step2_rp1_launch3_stdout_2026-10-02.log | 7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d |
| launch 3 stderr (quarantined; resumed sub-process only) | quarantine/f3_step2_rp1_launch3_stderr_2026-10-02.log | 915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45 |
| launch 4 stdout (quarantined) | quarantine/f3_step2_rp1_launch4_stdout_2026-10-02.log | c1b286fa378def03c91035199750f6243cb501768f10852996dfdc8b4d71f698 |
| launch 4 stderr (quarantined) | quarantine/f3_step2_rp1_launch4_stderr_2026-10-02.log | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| launch 5 stdout (final, live) | calibration/f3_step2_rp1_launch5_stdout_2026-10-02.log | cbd2281e5719911a997ddf9103707d50adc74e7857616aaf443f9b0dd815f715 |
| launch 5 stderr (final, live) | calibration/f3_step2_rp1_launch5_stderr_2026-10-02.log | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| attempt-1 supersession note | quarantine/f3_step2_rp1_attempt1_nonreg_bug_note_2026-10-02.md | 2357898e6d7314a5b950fc356def73a4e78ce7d27a6e67b863b6041d7784be1b |
| attempt-2 supersession note | quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md | 029fcc980513e74c142250cb9ccc51051a541af71a9dd9a85364aa705d20ca0c |
| attempt-3 supersession note (ctx-20 wording NOT corrected here by design — see attempt log §7 erratum) | quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md | 527fd2495bd4642b956ea18b760beca5a1168449cd55214bc7f6b7bb9a49a1d3 |
| attempt-4 supersession note | quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md | 73d9040bb3ed4aaf5d72dda0fd04a6189b11c38e843429e009b4641f3a79e530 |
| attempt-1 harness bytes (quarantined; == custody-named hash) | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py | 08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2 |
| attempt-2 harness bytes (quarantined) | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py | 0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5 |
| attempt-3 harness bytes (quarantined) | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py | d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d |
| attempt-4 harness bytes (quarantined) | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py | 47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561 |

Attempt-2 and attempt-4's complete superseded output sets (9 files each: results,
residual, test evidence, telemetry, per-call telemetry, store manifest, 3
non-regression CSVs), prefixed `ATTEMPT2_NARROWED_EVIDENCE_MISSING_` and
`ATTEMPT4_STORE_READ_LOG_MISSING_` respectively, are preserved whole in
`quarantine/` and are listed by directory, not individually re-hashed here — each
was the live file's own `_WRITTEN = ... sha256=...` value at the time of its own
attempt's run (attempt log §§2/4).

### Restart stores (per-unit records in item B for the final attempt; quarantined
### attempts' per-unit records live inside each quarantined store directory itself)

| store | location (p_konum_plus/) | units | fingerprint |
|---|---|---|---|
| attempt 1 (quarantined) | quarantine/rp1_restart_store_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG/ | 12,453 (all pid 11116) | 64b35e0777fdbb52 |
| attempt 2 (quarantined) | quarantine/rp1_restart_store_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING/ | 12,453 (all pid 13328) | d2ee833b4bad9138 |
| attempt 3 (quarantined, merged interrupted+resumed) | quarantine/rp1_restart_store_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG/ | 4,449 (all pid 23540) | 9cba3c77c85d5885 |
| attempt 4 (quarantined) | quarantine/rp1_restart_store_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING/ | 12,453 (all pid 26524) | 4cb395a7217d1d64 |
| attempt 5 FINAL (live) | calibration/.rp1_restart_store_2026-10-02 | 12,453 (all pid 33100) | a33c98202ae1591d |

### Standing instruments (in the repository; verified by hash, not re-transmitted)

rp1 instruction `a57b6fca…`, D-10 `4c89577b…`, D-9 `1ab17e44…`, D-8 `aadf2840…`,
A-5 `9111bc71…`, r4-2 instruction `d6680338…`, D-7 `a3e70509…`, A-4 `ad222936…`,
r4-1 instruction `283ac4e2…`, D-6 `a92a0518…`, r4 instruction `e1283958…`, D-5
`0cd87ad5…`, D-3 `5b0e19ea…`, D-1 `17187d31…`, D-2 `da0c4064…`, A-1/A-2/A-3, the F1
freeze record `5eceb198…`, the r4-1 results baseline `6dd4185b…`, the r4-2 results/
telemetry/test-evidence baseline (`f2a0a4d5…`/`ac70eaf5…`/`c156b9e0…`). The r4-2
package (harness `b988e962…`, register `c281e713…`, report `7754ba02…`, …) and every
earlier package, quarantined file and audit or PI record are historical and
read-only; `parents_unchanged = true`.

### Item Z — zip

```text
f3_realdata_prep_rp1_package_2026-10-04.zip — one archive of every file listed above
(deliverables + item E + this list, each with its sidecar), for transport only;
hash given alongside the zip
```

```text
real_data_access = false ; commit = false
```
