# p_konum_plus - F3 STEP-2 r4-2 Pre-Execution Custody Record - attempt 1

```text
artifact_role = pre-execution custody record for ATTEMPT 1 of the r4-2 revision
                (deliverable 4; R41A-02(a): one record per attempt, never overwritten)
status        = NON-NORMATIVE
date          = 2026-09-30
written_by    = a standalone W-3 writer OUTSIDE the run process (R3A-07);
                the harness VERIFIES this record at start and never writes it

harness_path = p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py
harness_sha256 = 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74

generator_path = p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py
generator_sha256 = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
generator_provenance = REUSED UNCHANGED from the r4-1 package (r4-2 instruction section 5
                       item 2); no r4-2 copy exists and none is made

manifest_path = p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv
manifest_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
manifest_provenance = REUSED UNCHANGED from the r4-1 package (section 5 item 3); regenerated
                      in memory from the reused generator by this writer AND by main(),
                      verified equal both times; the file itself is never rewritten
manifest_regenerated_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe

dispatch_preconditions_P1_P4 = every value below is OBSERVED (computed by this
                               writer on the repository files), not a stamped literal
D-3_path = p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
D-3_sha256_observed = 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
D-3_sha256_pinned = 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
D-3_values_equal = EQUAL
r4_instruction_path = p_konum_plus/prompts/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md
r4_instruction_sha256_observed = e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387
r4_instruction_sha256_pinned = e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387
r4_instruction_values_equal = EQUAL
D-5_path = p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md
D-5_sha256_observed = 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
D-5_sha256_pinned = 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
D-5_values_equal = EQUAL
r4-1_instruction_path = p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md
r4-1_instruction_sha256_observed = 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330
r4-1_instruction_sha256_pinned = 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330
r4-1_instruction_values_equal = EQUAL
D-6_path = p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md
D-6_sha256_observed = a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0
D-6_sha256_pinned = a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0
D-6_values_equal = EQUAL
r4-2_instruction_path = p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
r4-2_instruction_sha256_observed = d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe
r4-2_instruction_sha256_pinned = d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe
r4-2_instruction_values_equal = EQUAL
D-7_path = p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md
D-7_sha256_observed = a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb
D-7_sha256_pinned = a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb
D-7_values_equal = EQUAL
A-1_path = p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md
A-1_sha256_observed = 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6
A-1_sha256_pinned = 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6
A-1_values_equal = EQUAL
A-2_path = p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md
A-2_sha256_observed = b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a
A-2_sha256_pinned = b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a
A-2_values_equal = EQUAL
A-3_path = p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md
A-3_sha256_observed = 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9
A-3_sha256_pinned = 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9
A-3_values_equal = EQUAL
A-4_path = p_konum_plus/prompts/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md
A-4_sha256_observed = ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82
A-4_sha256_pinned = ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82
A-4_values_equal = EQUAL
D-1_path = p_konum_plus/prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
D-1_sha256_observed = 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
D-1_sha256_pinned = 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
D-1_values_equal = EQUAL
D-2_path = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
D-2_sha256_observed = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
D-2_sha256_pinned = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
D-2_values_equal = EQUAL

S1 = (a)
S2 = alpha
T1 = AUTHORIZE
T2 = T-2a
T3 = AUTHORIZE
T4 = T-4a
T5 = CONFIRM_WITHIN_SCOPE
S_R2_1 = PI_RULE (rule text in D-5 section 3, carried unchanged by D-6 and D-7,
         implemented word for word; EXACT-03 closed with D-5 as source per D-5 S4(d))
T_R2_2 = AUTHORIZE_RESTART (as read from D-5, carried unchanged by D-6 and D-7)
PI_dispatch_record_for_this_revision = D-7 (end_state.PI_dispatch_record_hash; R41A-03)

restart_layer_active_at_this_W3 = False (r4-2 attempt 1 is ONE process from the
         beginning; a restart layer is introduced only after a recorded interruption of
         THIS revision - D-3 S8.1/S8.2/S8.3. The r4-2 store is its own directory; the r4-1
         and r4 stores stay where they are, untouched and unread.)
code_env_fingerprint = 0f32c7911cf8fccb
environment = python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ; Windows-10-10.0.19045-SP0 ; OMP/OPENBLAS/MKL = 1

attempt_number = 1
launch_number_of_first_launch_under_these_bytes = 1
supersedes_harness_sha256 = None
supersedes_custody_sha256 = None      # R41A-02(a): filled from attempt 2 on
supersedes_note_path = None
r4-1_package = historical, read-only (harness 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f,
               results 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385);
               the r4 and r3 packages likewise. Nothing of them is overwritten, renamed or
               moved by the r4-2 revision

declaration = this record is written AFTER the r4-2 harness exists and is hashed, with the
reused generator and manifest named at their delivered hashes, and BEFORE the first test or
run of attempt 1. It names the exact bytes that are then executed. No W-4 process has
yet been started under these three hashes. Because this record is written outside the run
process, a resumed launch does NOT re-stamp it, and because its name carries the attempt
number it is never overwritten by a later attempt.

real_data_access = false
commit = false
```
