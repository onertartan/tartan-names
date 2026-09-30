# p_konum_plus - F3 STEP-2 r3 Pre-Execution Custody Record

```text
artifact_role = pre-execution custody record (deliverable 4)
status        = NON-NORMATIVE
date          = 2026-09-22

harness_path = p_konum_plus/calibration/f3_step2_adequacy_harness_r3_2026-09-22.py
harness_sha256 = 5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77

generator_path = p_konum_plus/calibration/f3_step2_fixture_generator_r3_2026-09-22.py
generator_sha256 = cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8

manifest_path = p_konum_plus/calibration/f3_step2_fixture_manifest_r3_2026-09-22.csv
manifest_sha256 = 9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a

dispatch_preconditions_P1_P4 = ALL PASS
S1 = (a)
S2 = alpha
T1 = AUTHORIZE
T2 = T-2a
T3 = AUTHORIZE
T4 = T-4a
T5 = CONFIRM_WITHIN_SCOPE
S_R2_1 = DEFERRED_THIS_CYCLE
T_R2_2 = AUTHORIZE_RESTART
pi_ratified_content_path = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
pi_ratified_content_sha256 = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
dispatch_record_path = p_konum_plus/prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md
dispatch_record_sha256 = 4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865

restart_layer_active_at_this_W3 = True
code_env_fingerprint = 1ba561daefb48b2e

attempt_number = 5
supersedes_harness_sha256 = 99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a
supersedes_custody_sha256 = 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657
supersedes_note_path = p_konum_plus/quarantine/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md

declaration = this record is written AFTER the r3 harness, generator and manifest exist and are hashed, and BEFORE the first test or run. It names the exact bytes that are then executed. No W-4 process has yet been started under these three hashes.

real_data_access = false
commit = false
```
