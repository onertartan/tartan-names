# p_konum_plus — F3 STEP-2 r4-1 — Transmission List (deliverable F)

```text
artifact_role = the complete transmission set for the r4-1 revision (r4-1 instruction S2:
                "the full list, including the stdout and stderr logs"). Every hash is
                OBSERVED (sha256sum on the delivered files, 2026-09-30).
status        = NON-NORMATIVE
date          = 2026-09-29 (revision tag) ; run completed 2026-09-30
final run      = attempt 3, launch 4 (pid 7972), exit 0 ; DETERMINISM = True
                (RUN1 == RUN2 canonical = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77)
```

Every file below except the two restart-store directories has an external `.sha256` sidecar
verifying its listed hash. The r4-1 revision modifies, renames or moves NO r3, r4 or
pre-existing quarantine file; every item here is a NEW r4-1 file. Verification verdicts
(from the delivered results and stdout): 9 instruments PASS; W-3 verified at every launch;
T-EXPECT-ALL 36/36; DETERMINISM True; T-NONREG-R4 findings 0; eval-level spline-pending PASS;
COVERAGE_DERIVED 64 rows, 0 downgrades; 28/28 tests_run passed; NATURAL_UNRELATED_EVENTS 0;
end state PARTIAL_PENDING_PI.

### Deliverables 1-12 + A/B/C (each with a .sha256 sidecar)

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1  harness | calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py | 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f |
| 2  generator | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3  manifest | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4  W-3 custody | provenance/f3_step2_r4-1_preexecution_custody_2026-09-29.md | 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d |
| 5  telemetry | calibration/f3_step2_telemetry_r4-1_2026-09-29.csv | 85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167 |
| 6  results | calibration/f3_step2_results_r4-1_2026-09-29.json | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 |
| 7  residual | calibration/f3_step2_residual_series_r4-1_2026-09-29.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8  test-evidence | calibration/f3_step2_test_evidence_r4-1_2026-09-29.json | f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd |
| 9  register (child of r4 register 0eed314c) | calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md | 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 |
| 10 correction report | provenance/f3_step2_correction_report_r4-1_2026-09-29.md | e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e |
| 11 start-state inventory (R4A-04) | provenance/f3_step2_r4-1_start_state_inventory_2026-09-29.md | fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 |
| 12 attempt log (incl. ERRATUM-2, R4A-10) | provenance/f3_step2_r4-1_attempt_log_2026-09-29.md | ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 |
| A  per-call telemetry (12,174 rows) | calibration/f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv | 22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88 |
| B  restart-store manifest, final store (11,869 rows) | calibration/f3_step2_r4-1_restart_store_manifest_2026-09-29.csv | cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1 |
| C  non-regression vs r4 (R4A-01(f); 37 rows) | calibration/f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |

### Run logs — the final attempt-3 launch (pid 7972); stdout AND stderr (r4-1 instruction S2)

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| stdout | calibration/f3_step2_r4-1_run_stdout_2026-09-29.log | 77120f5be87da8dada1cdad47f7840427922ba212464499950b1263f0747ecf4 |
| stderr | calibration/f3_step2_r4-1_run_stderr_2026-09-29.log | 9b678df6d6be6c0b9b5d96d0c358da4ec24debd5a7114a02e60a2f26a4608aa1 |

### Quarantine artifacts (all NEW r4-1 files; nothing renamed or moved from r3/r4)

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| attempt-1 interruption note | quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md | 7ff79add1a72219a64a64f73cb5f14160148a120582715e400435ba4434dcab4 |
| attempt-2 nonreg-canon-bug note | quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md | e27b29b2ae8746aa7dce2700aa11d942b8ed1f1db429a482845623fee7e9f6e2 |
| annotation note (R4A-10) | quarantine/f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md | 3adbd089c03c8212e56f9c275b5785562a3289e2bf2b4977b71ee1b34473e2aa |
| attempt-2 harness snapshot (byte-exact 280869892d) | quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py | 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2 |
| attempt-1 stdout | quarantine/f3_step2_r4-1_attempt1_stdout_2026-09-29.log | f0398c8e7350e5eb7a5d6f7168decdeea88da5bdf12be06c9654bb4813c8d546 |
| attempt-1 stderr | quarantine/f3_step2_r4-1_attempt1_stderr_2026-09-29.log | 8fa1cab46ecfc0f92cb2df6301c4cab9a8e4b2079ce1a7fed4e1fb323e171b94 |
| attempt-2 stdout | quarantine/f3_step2_r4-1_attempt2_stdout_2026-09-29.log | 9381d124f61d1435e6d107320e127246798ae23f34d5b01dabadcb48c34fd7cf |
| attempt-2 stderr | quarantine/f3_step2_r4-1_attempt2_stderr_2026-09-29.log | 83c1e4a49778cdd973fa40838a7997317cea45e687afeadebba89d22a1a9b253 |

### Restart stores (transmitted whole; per-unit path/size/sha256/pid/start_iso in deliverable B)

| store | location (p_konum_plus/) | units |
|---|---|---|
| attempt-3 FINAL (live; fingerprint dc228827920a9633) | calibration/.r4-1_restart_store_2026-09-29 | 11,869 |
| attempt-2 QUARANTINED whole (fingerprint b6fc376b049c20e1) | quarantine/r4-1_restart_store_2026-09-29_ATTEMPT2_NONREG_CANON_BUG | 11,869 |

### Standing instruments (already in the repository; verified by hash, not re-transmitted)

D-1 v6 `17187d31…`, D-2 `da0c4064…`, D-3 `5b0e19ea…`, r4 instruction `e1283958…`,
D-5 `0cd87ad5…`, r4-1 instruction `283ac4e2…`, D-6 `a92a0518…`, A-1 `11cfa591…`,
A-2 `b7217027…`, A-3 `9c16abb5…`. The r4 package (parents_unchanged = true) is at the
non-retroactivity hashes re-verified in the start-state inventory §2.

```text
real_data_access = false ; commit = false
```
