# p_konum_plus - F3 real-data preparation rp1 - Pre-Execution Custody Record - attempt 1

```text
artifact_role = pre-execution custody record for ATTEMPT 1 of the rp1 cycle
                (deliverable 4; R41A-02(a) adopted unchanged: one record per attempt,
                never overwritten)
status        = NON-NORMATIVE
date          = 2026-10-02
written_by    = a standalone W-3 writer OUTSIDE the run process (R3A-07);
                the harness VERIFIES this record at start and never writes it

harness_path = p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py
harness_sha256 = 08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2

generator_path = p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py
generator_sha256 = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
generator_provenance = REUSED UNCHANGED from the r4-1 package (rp1 instruction,
                       nothing else changes); no rp1 copy exists and none is made

manifest_path = p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv
manifest_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
manifest_provenance = REUSED UNCHANGED from the r4-1 package; regenerated in memory
                      from the reused generator by this writer AND by main(), verified
                      equal both times; the file itself is never rewritten
manifest_regenerated_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe

dispatch_preconditions = every value below is OBSERVED (computed by this
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
D-8_path = p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md
D-8_sha256_observed = aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae
D-8_sha256_pinned = aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae
D-8_values_equal = EQUAL
A-5_path = p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md
A-5_sha256_observed = 9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575
A-5_sha256_pinned = 9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575
A-5_values_equal = EQUAL
D-9_path = p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md
D-9_sha256_observed = 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3
D-9_sha256_pinned = 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3
D-9_values_equal = EQUAL
rp1_instruction_path = p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
rp1_instruction_sha256_observed = a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5
rp1_instruction_sha256_pinned = a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5
rp1_instruction_values_equal = EQUAL
D-10_path = p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md
D-10_sha256_observed = 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34
D-10_sha256_pinned = 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34
D-10_values_equal = EQUAL
D-1_path = p_konum_plus/prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
D-1_sha256_observed = 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
D-1_sha256_pinned = 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
D-1_values_equal = EQUAL
D-2_path = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
D-2_sha256_observed = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
D-2_sha256_pinned = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
D-2_values_equal = EQUAL
F1_freeze_record_path = p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
F1_freeze_record_sha256_observed = 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0
F1_freeze_record_sha256_pinned = 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0
F1_freeze_record_values_equal = EQUAL

S1 = (a)
S2 = alpha
T1 = AUTHORIZE
T2 = T-2a
T3 = AUTHORIZE
T4 = T-4a
T5 = CONFIRM_WITHIN_SCOPE
S_R2_1 = PI_RULE (rule text in D-5 section 3, carried unchanged through D-6/D-7/D-10,
         implemented word for word; EXACT-03 closed with D-5 as source per D-5 S4(d))
T_R2_2 = AUTHORIZE_RESTART (as read from D-5, carried unchanged)
T-RP-1 = ACTIVE_FROM_START (D-10 S2, S-b: restart layer used from attempt 1,
         replacing D-3 S8.3's "attempt 1 runs without it" for rp1 only)
S-c = CHILD_HARNESS_OF_R4-2 ; S-e = SYNTHETIC_ONLY_IN_RP1 ; S-f = EXCLUDED_FROM_RP1
PI_dispatch_record_for_this_cycle = D-10 (end_state.PI_dispatch_record_hash; rp1 S9)

restart_layer_active_at_this_W3 = True (T-RP-1 = ACTIVE_FROM_START: the
         layer is active from attempt 1, unlike every prior cycle. The rp1 store is its
         own directory; the r4-2/r4-1/r4 stores stay where they are, untouched and unread.)
code_env_fingerprint = 64b35e0777fdbb52
environment = python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ; Windows-10-10.0.19045-SP0 ; OMP/OPENBLAS/MKL = 1

attempt_number = 1
launch_number_of_first_launch_under_these_bytes = env-driven (F3_RP1_LAUNCH; first launch of this attempt = 1)
supersedes_harness_sha256 = None
supersedes_custody_sha256 = None
supersedes_note_path = None
r4-2_package = historical, read-only (harness b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730,
               results f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba);
               the r4-1, r4 and r3 packages likewise. Nothing of them is overwritten,
               renamed or moved by the rp1 cycle
real_data_access = false ; REAL_DATA_MODE (harness switch) = False in every rp1 launch

declaration = this record is written AFTER the rp1 harness exists and is hashed, with the
reused generator and manifest named at their delivered hashes, and BEFORE the first test or
run of attempt 1. It names the exact bytes that are then executed. No W-4 process has
yet been started under these three hashes. Because this record is written outside the run
process, a resumed launch does NOT re-stamp it, and because its name carries the attempt
number it is never overwritten by a later attempt.

commit = false
```
