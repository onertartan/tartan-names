# p_konum_plus - F3 STEP-2 r4-1 Pre-Execution Custody Record

```text
artifact_role = pre-execution custody record (deliverable 4, r4-1 revision)
status        = NON-NORMATIVE
date          = 2026-09-29
written_by    = a standalone W-3 writer OUTSIDE the run process (R3A-07);
                the harness VERIFIES this record at start and never writes it

harness_path = p_konum_plus/calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py
harness_sha256 = 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f

generator_path = p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py
generator_sha256 = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830

manifest_path = p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv
manifest_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
manifest_written_by = this W-3 writer, with the harness's own csv writer
                      (LF, ascii); main() regenerates it and verifies equality

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
S_R2_1 = PI_RULE (rule text in D-5 S3, carried unchanged by D-6 S2, implemented
         word for word; EXACT-03 closed with D-5 as source per D-5 S4(d))
T_R2_2 = AUTHORIZE_RESTART (as read from D-5, carried unchanged by D-6 S2)

restart_layer_active_at_this_W3 = True (retained; attempt 3 follows the
         attempt-2 non-regression-check fix -- D-3 S8.3 harness-change. The
         attempt-2 store is quarantined whole and the r4-1 store is EMPTY at
         attempt 3's first launch. The r4 store is left in place, untouched.)
code_env_fingerprint = dc228827920a9633
environment = python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ; Windows-10-10.0.19045-SP0 ; OMP/OPENBLAS/MKL = 1

attempt_number = 3 (r4-1 revision, third attempt; restart layer active)
supersedes_harness_sha256 = 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2
supersedes_custody_sha256 = None
supersedes_note_path = p_konum_plus/quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md
r4_package = historical, read-only (r4 harness 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c);
             nothing of r4 or r3 is overwritten, renamed or moved by the r4-1 revision

declaration = this record is written AFTER the r4-1 harness, generator and
manifest exist and are hashed, and BEFORE the first test or run of the r4-1
revision. It names the exact bytes that are then executed. No W-4 process has
yet been started under these three hashes. Because this record is written
outside the run process, a resumed launch does NOT re-stamp it and this
declaration stays true for the revision as a whole.

real_data_access = false
commit = false
```
