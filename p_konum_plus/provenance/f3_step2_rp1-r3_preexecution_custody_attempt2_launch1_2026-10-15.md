# rp1-r3 pre-execution custody

One immutable W-3 record for this actual launch; all earlier records are preserved.

```text
harness_sha256 = 9ff48dbe6a5fdb6e4ae9d1952f1f7ecaba553eb84ef4e2a60de0be8258e8f96e
generator_sha256 = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
manifest_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
code_env_fingerprint = 75e00ea983915d67
attempt_number = 2
launch_number = 1
f3_rp1-r3_gate_tools_2026-10-15.py = 1666abcf25d54bbc0b2ea3f404e286801149c3b7fb223eb83a49c1a54a75c045
f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py = eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8
f3_rp1-r3_technical_tests_2026-10-15.py = 9d68989488657a8dc8f1bc3ce119ea1232415971043d0f9de799a4a014df9879
supersedes_harness_sha256 = 4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d
supersedes_custody_sha256 = 7d864db9c2e766ff1fc4d3ed77649e7a9a140249426d56e6d51779f7aa8efc8d
supersedes_note_path = p_konum_plus/provenance/f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md
supersedes_attempt1_writer_record_path = p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_w3_writer_2026-10-15.json
supersedes_attempt1_writer_record_sha256 = 5c9661045c6602195296689229834c4f178fb7cab03c9ad5fe3337aa2b9bf459
supersedes_attempt1_W3_record = no attempt-1 W-3 record
```

```json
{
  "writer_sha256": "822560025b80920431998005b647076348f4e3026546e42a852718ea1f082891",
  "created_utc": "2026-10-16T18:55:56.559339+00:00",
  "repo_root": "G:\\PycharmProjects\\pkp-worktree",
  "environment": {
    "python": "3.11.7",
    "numpy": "1.26.4",
    "scipy": "1.14.1",
    "platform": "Windows-10-10.0.19045-SP0",
    "OMP": "1",
    "OPENBLAS": "1",
    "MKL": "1"
  },
  "pin_checks": [
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
      "expected": "5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5",
      "observed": "5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5",
      "source": "D-3"
    },
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md",
      "expected": "e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387",
      "observed": "e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387",
      "source": "r4 instruction"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md",
      "expected": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851",
      "observed": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851",
      "source": "D-5"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md",
      "expected": "11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6",
      "observed": "11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6",
      "source": "A-1"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md",
      "expected": "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498",
      "observed": "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498",
      "source": "D-2"
    },
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md",
      "expected": "283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330",
      "observed": "283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330",
      "source": "r4-1 instruction"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md",
      "expected": "a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0",
      "observed": "a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0",
      "source": "D-6"
    },
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md",
      "expected": "d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe",
      "observed": "d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe",
      "source": "r4-2 instruction"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md",
      "expected": "a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb",
      "observed": "a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb",
      "source": "D-7"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md",
      "expected": "ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82",
      "observed": "ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82",
      "source": "A-4 (input)"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py",
      "expected": "68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830",
      "observed": "68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830",
      "source": "generator (reused r4-1)"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv",
      "expected": "5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe",
      "observed": "5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe",
      "source": "manifest (reused r4-1)"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json",
      "expected": "6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385",
      "observed": "6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385",
      "source": "r4-1 results (baseline)"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md",
      "expected": "b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a",
      "observed": "b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a",
      "source": "A-2 (input)"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md",
      "expected": "9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9",
      "observed": "9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9",
      "source": "A-3 (input)"
    },
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md",
      "expected": "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5",
      "observed": "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5",
      "source": "rp1 instruction"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md",
      "expected": "4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34",
      "observed": "4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34",
      "source": "D-10"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md",
      "expected": "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3",
      "observed": "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3",
      "source": "D-9 (QUALIFIED)"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md",
      "expected": "aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae",
      "observed": "aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae",
      "source": "D-8"
    },
    {
      "path": "p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md",
      "expected": "9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575",
      "observed": "9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575",
      "source": "A-5 (input)"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json",
      "expected": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
      "observed": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
      "source": "r4-2 results (non-regression baseline)"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv",
      "expected": "ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d",
      "observed": "ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d",
      "source": "r4-2 telemetry"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json",
      "expected": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf",
      "observed": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf",
      "source": "r4-2 test evidence"
    },
    {
      "path": "p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md",
      "expected": "5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0",
      "observed": "5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0",
      "source": "F1 freeze record"
    },
    {
      "path": "p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md",
      "expected": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
      "observed": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
      "source": "D-11 r1"
    },
    {
      "path": "p_konum_plus/provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md",
      "expected": "858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9",
      "observed": "858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9",
      "source": "rp1 transmission list"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py",
      "expected": "39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09",
      "observed": "39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09",
      "source": "rp1 harness"
    },
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md",
      "expected": "2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d",
      "observed": "2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d",
      "source": "rp1-r1 instruction"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md",
      "expected": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364",
      "observed": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364",
      "source": "D-12"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md",
      "expected": "2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989",
      "observed": "2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989",
      "source": "rp1 audit (input)"
    },
    {
      "path": "p_konum_plus/prompts/RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md",
      "expected": "aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef",
      "observed": "aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef",
      "source": "rp1-r1 DRAFT review (input)"
    },
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md",
      "expected": "f84069a060c806355676a259bd07b437a7f81ae0600b90fef5ab9baa6f73881a",
      "observed": "f84069a060c806355676a259bd07b437a7f81ae0600b90fef5ab9baa6f73881a",
      "source": "rp1-r3 incoming Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md",
      "expected": "10b3543344bd9ebf9df3319cfdc0d3540888328fde8bf4e5d6e05764bb675b1a",
      "observed": "10b3543344bd9ebf9df3319cfdc0d3540888328fde8bf4e5d6e05764bb675b1a",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md",
      "expected": "278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93",
      "observed": "278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md",
      "expected": "3e2a5fe3373ae08fc91831d7312c5f994ff332efdf3bae50818cced98d608e45",
      "observed": "3e2a5fe3373ae08fc91831d7312c5f994ff332efdf3bae50818cced98d608e45",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md",
      "expected": "25023f450dc443a8d248fc8ed662812947f098f1532042a6858f159cee39deb9",
      "observed": "25023f450dc443a8d248fc8ed662812947f098f1532042a6858f159cee39deb9",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md",
      "expected": "fe9b2b539f55efeda94d61c77ad30bd146de2ebcbbbf4d7a203fb13a8c0dcfa0",
      "observed": "fe9b2b539f55efeda94d61c77ad30bd146de2ebcbbbf4d7a203fb13a8c0dcfa0",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md",
      "expected": "f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72",
      "observed": "f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md",
      "expected": "dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2",
      "observed": "dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md"
    },
    {
      "path": "p_konum_plus/prompts/F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md",
      "expected": "25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2",
      "observed": "25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2",
      "source": "rp1-r3 incoming F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_2026-10-16.md",
      "expected": "778d8aff874991591cf45ae37e4fc0c698fb066304e16b6503e29868f693eff2",
      "observed": "778d8aff874991591cf45ae37e4fc0c698fb066304e16b6503e29868f693eff2",
      "source": "D-20 signed attempt-2 bounded correction and hold point"
    },
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md",
      "expected": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5",
      "observed": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5",
      "source": "rp1-r3 incoming Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-15.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md",
      "expected": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f",
      "observed": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-15.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md",
      "expected": "f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913",
      "observed": "f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913",
      "source": "rp1-r3 incoming f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-15.md"
    },
    {
      "path": "p_konum_plus/prompts/F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md",
      "expected": "82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e",
      "observed": "82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e",
      "source": "rp1-r3 incoming F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py",
      "expected": "cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb",
      "observed": "cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb",
      "source": "rp1-r3 carried p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py"
    },
    {
      "path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md",
      "expected": "98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956",
      "observed": "98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956",
      "source": "rp1-r3 carried p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md"
    },
    {
      "path": "p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md",
      "expected": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
      "observed": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
      "source": "rp1-r3 carried p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md"
    },
    {
      "path": "p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md",
      "expected": "4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955",
      "observed": "4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955",
      "source": "rp1-r3 carried p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
      "expected": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
      "observed": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
      "source": "D-14 IR1-13 RECORDED_LIMITATION"
    },
    {
      "path": "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
      "expected": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
      "observed": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
      "source": "rp1-r3 carried p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    },
    {
      "path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv",
      "expected": "e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75",
      "observed": "e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75",
      "source": "rp1-r3 carried p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv"
    }
  ],
  "launch_authorization": {
    "finding": "IR1-13",
    "disposition": "RECORDED_LIMITATION",
    "ledger_status": "OPEN / B",
    "pi_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
    "pi_record_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "standalone_evidence_status": "NOT OBSERVED",
    "executor_status": "PARTIAL_PENDING_PI"
  },
  "launch_authorization_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
  "current_launch_started": false,
  "real_data_access": false,
  "store_at_first_launch": "EMPTY"
}
```
