# p_konum_plus - F3 STEP-2 r4 Pre-Execution Custody Record

```text
artifact_role = pre-execution custody record (deliverable 4, r4)
status        = NON-NORMATIVE
date          = 2026-09-24
written_by    = a standalone W-3 writer OUTSIDE the run process (R3A-07);
                the harness VERIFIES this record at start and never writes it

harness_path = p_konum_plus/calibration/f3_step2_adequacy_harness_r4_2026-09-24.py
harness_sha256 = 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c

generator_path = p_konum_plus/calibration/f3_step2_fixture_generator_r4_2026-09-24.py
generator_sha256 = 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c

manifest_path = p_konum_plus/calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv
manifest_sha256 = c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8
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
A-1_path = p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md
A-1_sha256_observed = 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6
A-1_sha256_pinned = 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6
A-1_values_equal = EQUAL
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
S_R2_1 = PI_RULE (rule text in D-5 S3, implemented word for word; EXACT-03
         closed with D-5 as source per D-5 S4(d))
T_R2_2 = AUTHORIZE_RESTART (as read from D-5; exercised from revision 3 on,
         after the first genuine interruption -- D-3 S8.2/S8.3)

restart_layer_active_at_this_W3 = True (layer retained; store QUARANTINED whole on the revision-4->5 harness change per D-3 S8.3 and starts EMPTY at this revision)
code_env_fingerprint = 5ef61a412c6bd76c
environment = python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ; Windows-10-10.0.19045-SP0 ; OMP/OPENBLAS/MKL = 1

attempt_number = 7 (revision 5)
supersedes_harness_sha256 = 90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805
supersedes_custody_sha256 = cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273
supersedes_note_path = p_konum_plus/quarantine/f3_step2_r4_attempt56_mutation_leak_note_2026-09-27.md
r3_package = historical, read-only (r3 harness 5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77);
             nothing of r3 is overwritten by the r4 cycle

declaration = this record is written AFTER the r4 harness, generator and
manifest exist and are hashed, and BEFORE the first test or run of the r4
cycle. It names the exact bytes that are then executed. No W-4 process has
yet been started under these three hashes. Because this record is written
outside the run process, a resumed launch does NOT re-stamp it and this
declaration stays true for the revision as a whole.

real_data_access = false
commit = false
```
