# rp1-r2 attempt log

## Disclosure supplied by the user

rp1-r2 talimatı önce yanlışlıkla rp1-r1 denetçi oturumuna verildi; o oturum rp1r1_audit\repo içinde bir taslak yazdı; bu taslak rp1-r2'de kullanılmadı.

The excluded draft was authored by another session. No file from that draft is used, copied or modified by this preparation. Parent input is the pinned rp1-r1 harness in pkp-worktree.

## Execution status

IR1-13 remains OPEN / B. The user explicitly prohibits a run until its decision arrives. No harness, copy, or test-section excerpt has been executed in this preparation. Positive/negative tests will be authored before W-3. Runtime results, process identifiers, timing and optimizer accounting: NOT OBSERVED. Source parsing and record-generation scripts perform no harness execution.

Every future invocation must be logged with source hash, directory, start/end, outputs and disposition under instruction section 5(b). No output outside a W-3 attempt enters a deliverable or attempt store. A new launch is blocked pending an IR1-13 PI decision.

## Prelaunch source preparation

Only record-generation and source-editing scripts ran. No harness, harness copy, test-section excerpt, optimizer, or W-3 writer ran. The declaration-authoring process was stopped when its repeated schema flattening was slow; its authoring script was corrected to cache those schemas and rerun. This was an authoring-process interruption, not a scientific attempt. The source-finalization script and this record generator parse/compile source without importing or executing it. Historical execution details are not reconstructed.

Runtime launch timestamps, runtime PIDs, tests and optimizer measurements: NOT OBSERVED. The initialization timestamp and source hashes below refer to preparation only.

```json
{
  "record_preparation_started_utc": "2026-10-10T16:16:02.904757+00:00",
  "initial_inventory_created_utc": "2026-10-10T15:46:08.153574+00:00",
  "record_generator_sha256": "8d08842b3a1174f7541eb6d61de01ec258498a07dc8771f67c3bbadd7f5dd6b8",
  "record_generator_directory": "G:\\PycharmProjects\\pkp-worktree",
  "harness_sha256": "44c14e8cc512b7a56f923f1579f4f97b6e43ce3bf1326cd2703cfb395702039f",
  "launch_authorized": false,
  "harness_invocations": 0,
  "test_excerpt_invocations": 0,
  "real_data_access": false
}
```

## Prelaunch record refinement

The diff labels were refined from the actual AST assignments/calls: the replaced legacy intake guard is Q1, restored mode-summary provenance is Q8, and handoff phase save/set/restore is Q9. Generic output-wiring labels at those locations were corrected before any launch. Source/expectation changes after observed runtime failure: none (no runtime execution). The source/record generator's hash and syntax observation were refreshed. Both patches reconstruct the harness exactly; every changed line has one label. This byte/range check is preparation verification, not an independent audit or a harness test.

## Signed D-14 intake

IR1-13 = RECORDED_LIMITATION, D-14 (a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7)

The prior STOP remains historical. D-14 releases only the launch gate; IR1-13 stays OPEN / B and the executor status stays PARTIAL_PENDING_PI. Every subsequent execution is logged under section 5(b). Small-test output stays outside deliverables and the rp1-r2 attempt store. Authorization now checks the fixed signed D-14 path, message pin and unchanged sidecar directly; the old free-standing flag is not consulted. This is prelaunch PI-directed source wiring, with no observed test failure and no expectation change.

```json
{
  "created_utc": "2026-10-10T17:17:41.895601+00:00",
  "message_pin": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
  "source_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
  "placed_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
  "source_sidecar_equal_placed": true,
  "decision": "RECORDED_LIMITATION",
  "ledger_status": "OPEN / B",
  "runtime_executions": 0,
  "source_changes": {
    "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
    "p_konum_plus/calibration/f3_rp1-r2_gate_tools_2026-10-10.py": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7",
    "p_konum_plus/calibration/f3_rp1-r2_launch_attempt_2026-10-10.py": "f74423713d61604fcf53c34a5b3eb851bd79d97611c4ad2f4ffc2f2d0a3b77da",
    "p_konum_plus/calibration/f3_rp1-r2_write_custody_2026-10-10.py": "c0b9e10c2022b744b23190e81243c2713e6d7cb39859b370d9f87216de03fa0e"
  },
  "scientific_expectations_changed": false,
  "reason": "User's signed D-14 authorizes the previously blocked preparation tests and attempt-1 launch when other prerequisites hold."
}
```

## Logged outside-W3 small-input execution

```json
{
  "kind": "OUTSIDE_W3_SMALL_INPUT_TEST_EXECUTION",
  "execution_id": "2026-10-10_execution01",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_small_input_tests_2026-10-10.py",
  "code_sha256": "421be9b7283de0df43b95d59221bb40eb533ce48c139ba07fc836a821cb071a2",
  "harness_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "harness_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
  "source_hashes": {
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_small_input_tests_2026-10-10.py": "421be9b7283de0df43b95d59221bb40eb533ce48c139ba07fc836a821cb071a2",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_gate_tools_2026-10-10.py": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_technical_tests_2026-10-10.py": "cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b"
  },
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-10T17:20:43.108177+00:00",
  "end_utc": "NOT OBSERVED (running)",
  "stdout": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\stdout.log",
  "stderr": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\stderr.log",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01",
  "store_root": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\small_test_store",
  "outputs_discarded": false,
  "output_disposition": "RETAINED_IN_EXTERNAL_QUARANTINE; EXCLUDED_FROM_ALL_DELIVERABLES_AND_ATTEMPT_STORE",
  "outside_w3_attempt": true,
  "actual_optimizer_calls": 0,
  "real_data_access": false,
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_small_input_tests_2026-10-10.py"
  ],
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
}
```

## Logged outside-W3 small-input execution

```json
{
  "kind": "PREFLIGHT_PID_OBSERVED",
  "execution_id": "2026-10-10_execution01",
  "pid": 49408
}
```

## Logged outside-W3 small-input execution

```json
{
  "kind": "OUTSIDE_W3_SMALL_INPUT_TEST_EXECUTION",
  "execution_id": "2026-10-10_execution01",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_small_input_tests_2026-10-10.py",
  "code_sha256": "421be9b7283de0df43b95d59221bb40eb533ce48c139ba07fc836a821cb071a2",
  "harness_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "harness_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
  "source_hashes": {
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_small_input_tests_2026-10-10.py": "421be9b7283de0df43b95d59221bb40eb533ce48c139ba07fc836a821cb071a2",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_gate_tools_2026-10-10.py": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_technical_tests_2026-10-10.py": "cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b"
  },
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-10T17:20:43.108177+00:00",
  "end_utc": "2026-10-10T17:20:54.604294+00:00",
  "stdout": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\stdout.log",
  "stderr": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\stderr.log",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01",
  "store_root": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\small_test_store",
  "outputs_discarded": false,
  "output_disposition": "RETAINED_IN_EXTERNAL_QUARANTINE; EXCLUDED_FROM_ALL_DELIVERABLES_AND_ATTEMPT_STORE",
  "outside_w3_attempt": true,
  "actual_optimizer_calls": 0,
  "real_data_access": false,
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r2_small_input_tests_2026-10-10.py"
  ],
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "pid": 49408,
  "return_code": 0,
  "stdout_sha256": "ab9231538316b52a3fb9faf8ebe1ee43a79127bf06a479fa23ca112004a0314c",
  "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "retained_output_inventory": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\retained_output_inventory.json",
  "retained_output_inventory_sha256": "c8b275d20ecdf50f476c99263a865ac77a7f8e28b0b8bfec552e9d6542f09097",
  "attempt_store_absent": true
}
```

## Attempt-1 launch prerequisites after D-14

Native checks verified all current dispatch pins, frozen F2/SPL source pins, historical inventory hashes/sidecars, byte-equal frozen manifest regeneration, unchanged prelaunch leaf declarations, no tracked or staged changes, and an absent attempt store. The logged small execution exited 0; its outputs remain excluded and retained outside the repository. Authorization comes from signed D-14; IR1-13 remains OPEN / B, RECORDED_LIMITATION. Current code locations and source diffs are refreshed before W-3. Status remains PARTIAL_PENDING_PI.

p_konum_plus/provenance/f3_realdata_prep_rp1-r2_prelaunch_checks_after_d14_2026-10-10.json SHA256 a62060950708aa9e4b757a84bbc8a49959ece8347c4b21b5b05ef110d6cc56ad

## Launch start (machine-transferred)

```json
{
  "launch": 1,
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "code_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-10T17:23:57.871831+00:00",
  "end_utc": "NOT OBSERVED (running)",
  "stdout": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_launch1_stdout_2026-10-10.log",
  "stderr": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_launch1_stderr_2026-10-10.log",
  "output_scope": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration",
  "outputs_discarded": false,
  "outside_w3_attempt": false,
  "real_data_access": false,
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "authorization": {
    "finding": "IR1-13",
    "disposition": "RECORDED_LIMITATION",
    "ledger_status": "OPEN / B",
    "pi_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
    "pi_record_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "standalone_evidence_status": "NOT OBSERVED",
    "executor_status": "PARTIAL_PENDING_PI"
  }
}
```

## Launch end (machine-transferred)

```json
{
  "launch": 1,
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "code_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-10T17:23:57.871831+00:00",
  "end_utc": "2026-10-11T03:41:45.094519+00:00",
  "stdout": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_launch1_stdout_2026-10-10.log",
  "stderr": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_launch1_stderr_2026-10-10.log",
  "output_scope": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration",
  "outputs_discarded": false,
  "outside_w3_attempt": false,
  "real_data_access": false,
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "authorization": {
    "finding": "IR1-13",
    "disposition": "RECORDED_LIMITATION",
    "ledger_status": "OPEN / B",
    "pi_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
    "pi_record_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "standalone_evidence_status": "NOT OBSERVED",
    "executor_status": "PARTIAL_PENDING_PI"
  },
  "pid": 25084,
  "return_code": 1,
  "stdout_sha256": "aa7b1106912458f81c7ccafd2c2f55e2ea2af4b1289074e76fc61c5f56c2cfb2",
  "stderr_sha256": "53ad9c88793a4f020bddf7b56a457d57b7075a40d1edc1e1447683634de0a4cf"
}
```

## Attempt-1 observed failure and section-0 declaration-defect correction

Attempt 1 failed at T-NONREG-R4-2, exit 1. All 22 U differences are absent-in-r4-2 Q1-Q11 test_evidence tests_run ran/passed leaves; no existing test flag changed. The defect is the omission of these declarations in the test_evidence namespace, although the results namespace already declared the new tests. Only 22 exact-path ADDITION declarations with individual reasons were appended. No prior declaration, expected value, comparison logic, scientific code, or attempt constant changed. This correction remains subject to auditor judgment under section 0.

```json
{
  "created_utc": "2026-10-11T13:13:32.993497+00:00",
  "observed_failure": "T-NONREG-R4-2; return_code=1; 22 U findings",
  "defect": "22 missing test_evidence namespace ADDITION declarations for the new Q1-Q11 ran/passed leaves",
  "old_harness_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
  "new_harness_sha256": "d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3",
  "all_22_absent_in_r4_2": true,
  "existing_test_flag_changes": [],
  "added_declarations": [
    {
      "path": "tests_run.T-RP1R2-Q1.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q1.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q1 introduces T-RP1R2-Q1; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q1.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q1.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q1 introduces T-RP1R2-Q1; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q10.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q10.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q10 introduces T-RP1R2-Q10; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q10.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q10.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q10 introduces T-RP1R2-Q10; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q11.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q11.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q11 introduces T-RP1R2-Q11; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q11.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q11.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q11 introduces T-RP1R2-Q11; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q2.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q2.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q2 introduces T-RP1R2-Q2; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q2.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q2.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q2 introduces T-RP1R2-Q2; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q3.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q3.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q3 introduces T-RP1R2-Q3; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q3.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q3.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q3 introduces T-RP1R2-Q3; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q4.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q4.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q4 introduces T-RP1R2-Q4; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q4.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q4.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q4 introduces T-RP1R2-Q4; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q5.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q5.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q5 introduces T-RP1R2-Q5; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q5.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q5.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q5 introduces T-RP1R2-Q5; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q6.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q6.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q6 introduces T-RP1R2-Q6; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q6.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q6.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q6 introduces T-RP1R2-Q6; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q7.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q7.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q7 introduces T-RP1R2-Q7; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q7.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q7.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q7 introduces T-RP1R2-Q7; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q8.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q8.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q8 introduces T-RP1R2-Q8; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q8.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q8.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q8 introduces T-RP1R2-Q8; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q9.passed",
      "id": "test_evidence:tests_run.T-RP1R2-Q9.passed",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q9 introduces T-RP1R2-Q9; its new test_evidence tests_run.passed leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    },
    {
      "path": "tests_run.T-RP1R2-Q9.ran",
      "id": "test_evidence:tests_run.T-RP1R2-Q9.ran",
      "kind": "ADDITION",
      "reason": "Section 0 declaration-defect correction after attempt 1: section 4 Q9 introduces T-RP1R2-Q9; its new test_evidence tests_run.ran leaf is absent from r4-2. This adds the missing namespace declaration; no test value or existing declaration changes."
    }
  ],
  "previous_results_declarations_unchanged": true,
  "previous_test_evidence_declarations_unchanged": true,
  "entire_source_ast_unchanged_except_22_added_declarations": true,
  "attempt1_quarantine": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\quarantine\\f3_step2_rp1-r2_attempt1_2026-10-11",
  "baseline_test_evidence_sha256": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf",
  "attempt1_test_evidence_sha256": "4147d3e9b71b0ae9d434c17bca73b1d08bff3adde593b2b24e6303d26fd9be04",
  "attempt1_nonregression_sha256": "74edfbffe1be79df185e7ed2c9915959c107354aa8c7735a6535a7e900c72cf2",
  "difference_list": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_realdata_prep_rp1-r2_attempt1_22_u_findings_2026-10-11.csv",
  "exact_diff": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_realdata_prep_rp1-r2_attempt2_declaration_only_diff_2026-10-11.diff",
  "attempt2_launch_blocker": "ATTEMPT_NUMBER remains literal 1; no environment override exists. Custody path and delivered process.attempt_number depend on it. User prohibits any other code change.",
  "attempt2_started": false,
  "real_data_access": false,
  "status": "PARTIAL_PENDING_PI"
}
```

## Section 5(b): isolated attempt-1 comparator execution

```json
{
  "kind": "OUTSIDE_W3_COMPARATOR_EXCERPT_EXECUTION",
  "execution_id": "2026-10-11_comparator_execution01",
  "code_path": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_declaration_correction_tools\\compare_attempt1.py",
  "code_sha256": "f1c52bc74e251c4089b5d40c0e6f86906d56999b8a4cf71ed342b91944bca7cf",
  "wrapper_sha256": "fab1fe9cc7383157101e9a454497fa342f76ec67445f80c0b8629c7336fa7d6f",
  "harness_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "harness_sha256": "d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-11T13:16:08.360909+00:00",
  "end_utc": "NOT OBSERVED (running)",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_declaration_correction_tools\\compare_attempt1.py"
  ],
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "stdout": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01\\stdout.log",
  "stderr": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01\\stderr.log",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01",
  "outputs_discarded": false,
  "output_disposition": "RETAINED_IN_EXTERNAL_QUARANTINE; EXCLUDED_FROM_ALL_DELIVERABLES_AND_ATTEMPT_STORES",
  "outside_w3_attempt": true,
  "actual_optimizer_calls": 0,
  "store_access": "NONE",
  "real_data_access": false,
  "scope": "Exact test_evidence and telemetry comparator excerpts only; attempt-1 results JSON is absent, so results/S recomparison cannot be executed"
}
```

## Section 5(b): isolated attempt-1 comparator execution

```json
{
  "execution_id": "2026-10-11_comparator_execution01",
  "kind": "OUTSIDE_W3_CHILD_PID",
  "pid": 23608
}
```

## Section 5(b): isolated attempt-1 comparator execution

```json
{
  "kind": "OUTSIDE_W3_COMPARATOR_EXCERPT_EXECUTION",
  "execution_id": "2026-10-11_comparator_execution01",
  "code_path": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_declaration_correction_tools\\compare_attempt1.py",
  "code_sha256": "f1c52bc74e251c4089b5d40c0e6f86906d56999b8a4cf71ed342b91944bca7cf",
  "wrapper_sha256": "fab1fe9cc7383157101e9a454497fa342f76ec67445f80c0b8629c7336fa7d6f",
  "harness_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "harness_sha256": "d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-11T13:16:08.360909+00:00",
  "end_utc": "2026-10-11T13:23:18.965176+00:00",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_declaration_correction_tools\\compare_attempt1.py"
  ],
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "stdout": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01\\stdout.log",
  "stderr": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01\\stderr.log",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01",
  "outputs_discarded": false,
  "output_disposition": "RETAINED_IN_EXTERNAL_QUARANTINE; EXCLUDED_FROM_ALL_DELIVERABLES_AND_ATTEMPT_STORES",
  "outside_w3_attempt": true,
  "actual_optimizer_calls": 0,
  "store_access": "NONE",
  "real_data_access": false,
  "scope": "Exact test_evidence and telemetry comparator excerpts only; attempt-1 results JSON is absent, so results/S recomparison cannot be executed",
  "pid": 23608,
  "return_code": 0,
  "stdout_sha256": "da62ee58d09f7c737983d12a5b843cb7f62ad6faf706b7df8b06a0b77328d5ec",
  "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "retained_output_inventory": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01\\retained_output_inventory.json",
  "retained_output_inventory_sha256": "a17a820f51e586dedd846781eb97926ee6bb91dc6dcd1e09fc84e94531b22fc7",
  "attempt_store_absent": true,
  "executed_excerpt_sha256": "a8beed8caec46dd9749be6e624a3020f7b5a84cbf017492136565720d09f1aeb"
}
```

## Attempt-1 quarantine complete; attempt-2 identity precondition STOP

The original harness, logs, generated delivery files, synthetic runtime fixtures, and complete store are quarantined; every store unit matches its attempt-1 manifest. The active store is absent. The section-5(b) comparator execution exited 0; its outputs remain exclusively outside the repository and are excluded from all delivery files and stores. Full results-document recomparison is impossible because attempt 1 failed before that JSON was serialized.

Attempt 2 is NOT started. ATTEMPT_NUMBER is still the source literal 1 and controls both the W-3 writer and delivered process identity. The user authorized only 22 added declarations and forbids any other code change. No runtime override exists. A W-3 record purporting to authorize attempt 2 would be inconsistent with these bytes. No custody record is fabricated and no source/runtime counter is changed. Status stays PARTIAL_PENDING_PI; IR1-13 remains OPEN / B under signed D-14 RECORDED_LIMITATION.

```json
{
  "created_utc": "2026-10-11T13:23:31.371211+00:00",
  "status": "STOP_BEFORE_ATTEMPT_2",
  "harness_sha256": "d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3",
  "attempt1_harness_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
  "source_change": "22 missing ADDITION declarations only",
  "declarations_only_ast_check": true,
  "all_22_new": true,
  "existing_test_flag_changes": 0,
  "quarantine": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\quarantine\\f3_step2_rp1-r2_attempt1_2026-10-11",
  "quarantine_inventory": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\quarantine\\f3_step2_rp1-r2_attempt1_2026-10-11\\verified_quarantine_inventory_2026-10-11.csv",
  "quarantine_inventory_sha256": "934a7fba0fac5aedfa8d2d269b50e621e0e12d1bbf9b55a32edf5c02ad3f78de",
  "quarantined_file_count": 69614,
  "quarantined_store_unit_count": 67316,
  "all_store_units_match_attempt1_manifest": true,
  "dispatch_pin_checks": 42,
  "verified_d14_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
  "outside_w3_execution_record": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01\\execution_record.json",
  "outside_w3_execution_record_sha256": "b43a682456a49befee7bb03f67b9d219eb618c05687f8f6c37df1ccdfa9ff353",
  "outside_w3_outputs_disposition": "RETAINED_IN_EXTERNAL_QUARANTINE; EXCLUDED_FROM_ALL_DELIVERABLES_AND_ATTEMPT_STORES",
  "outside_w3_return_code": 0,
  "attempt2_store": "ABSENT (fresh launch would start empty)",
  "attempt2_custody": "NOT CREATED: actual harness still identifies attempt 1",
  "blocker": {
    "source": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
    "line": 101,
    "statement": "ATTEMPT_NUMBER = 1",
    "consequence": "Existing W-3 writer reads literal ATTEMPT_NUMBER from the harness; custody filename, custody attempt_number, and delivered process.attempt_number would claim attempt 1.",
    "user_constraint": "No other declaration or code may be changed; source attempt counter cannot be changed under this instruction.",
    "runtime_override": "No existing runtime configuration for the attempt counter; no AST rewrite, monkeypatch, or misleading custody record used."
  },
  "attempt2_started": false,
  "real_data_access": false,
  "executor_status": "PARTIAL_PENDING_PI",
  "commit_created": false
}
```

## Attempt-2 administrative authorization and provenance patch

The PI explicitly clarified that the previous no-other-code-change restriction excludes the new attempt number and attempt-bound provenance. ATTEMPT_NUMBER is now 2. SUPERSEDES_HARNESS_SHA256 identifies the quarantined attempt-1 bytes; SUPERSEDES_CUSTODY_SHA256 identifies its verified immutable W-3 record. Logs, runtime fixture custody and the fresh store are named for attempt 2, launch 1. Launcher changes only disclose and name that identity. The custody writer and technical dependencies are unchanged. All declarations are exactly those of the previous 22-ADDITION correction; all other harness bytes are unchanged. The historical STOP record is retained unchanged and its blocker is resolved by this PI instruction. No outside-W3 outputs are imported.

```json
{
  "created_utc": "2026-10-11T14:08:38.076946+00:00",
  "authorization": "PI user message explicitly permits ATTEMPT_NUMBER=2 and attempt-bound supersession/names only",
  "previous_stop": "Historical stop record retained unchanged; current user authorization resolves the attempt-counter prohibition",
  "attempt": 2,
  "first_launch": 1,
  "prior_harness_sha256": "d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3",
  "harness_sha256": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
  "supersedes_harness_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
  "supersedes_custody_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_step2_rp1-r2_preexecution_custody_attempt1_launch1_2026-10-10.md",
  "supersedes_custody_sha256": "6384a57de7f11ab7d18920813215a3eb56c21466e24469ddf689a5fdaf791469",
  "old_launcher_sha256": "f74423713d61604fcf53c34a5b3eb851bd79d97611c4ad2f4ffc2f2d0a3b77da",
  "launcher_sha256": "172e3d9bc67c0e5f8ad3406232bf77ec8c37c374a2429cee52c6491377916462",
  "harness_exact_replacements": [
    {
      "before": "ATTEMPT_NUMBER = 1",
      "after": "ATTEMPT_NUMBER = 2"
    },
    {
      "before": "SUPERSEDES_HARNESS_SHA256 = \"cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb\"",
      "after": "SUPERSEDES_HARNESS_SHA256 = \"92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c\""
    },
    {
      "before": "SUPERSEDES_CUSTODY_SHA256 = \"162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca\"",
      "after": "SUPERSEDES_CUSTODY_SHA256 = \"6384a57de7f11ab7d18920813215a3eb56c21466e24469ddf689a5fdaf791469\""
    },
    {
      "before": "f3_step2_rp1-r2_launch{LAUNCH_NUMBER}_stdout_2026-10-10.log",
      "after": "f3_step2_rp1-r2_attempt{ATTEMPT_NUMBER}_launch{LAUNCH_NUMBER}_stdout_2026-10-10.log"
    },
    {
      "before": "f3_step2_rp1-r2_launch{LAUNCH_NUMBER}_stderr_2026-10-10.log",
      "after": "f3_step2_rp1-r2_attempt{ATTEMPT_NUMBER}_launch{LAUNCH_NUMBER}_stderr_2026-10-10.log"
    },
    {
      "before": "RESTART_STORE_DIR = \"p_konum_plus/calibration/.rp1-r2_restart_store_2026-10-10\"",
      "after": "RESTART_STORE_DIR = \"p_konum_plus/calibration/.rp1-r2_attempt2_restart_store_2026-10-10\""
    },
    {
      "before": "\"p_konum_plus/provenance/f3_realdata_prep_rp1-r2_runtime_fixture_custody_launch%d_2026-10-10.csv\" % LAUNCH_NUMBER",
      "after": "\"p_konum_plus/provenance/f3_realdata_prep_rp1-r2_runtime_fixture_custody_attempt%d_launch%d_2026-10-10.csv\" % (ATTEMPT_NUMBER, LAUNCH_NUMBER)"
    }
  ],
  "launcher_provenance_replacements": [
    {
      "before": "    prefix = \"f3_step2_rp1-r2_launch%d\" % number",
      "after": "    attempt_node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == \"ATTEMPT_NUMBER\" for t in n.targets))\n    attempt = ast.literal_eval(attempt_node.value)\n    prefix = \"f3_step2_rp1-r2_attempt%d_launch%d\" % (attempt, number)"
    },
    {
      "before": "metadata = dict(launch=number, code_path=",
      "after": "metadata = dict(attempt=attempt, launch=number, code_path="
    },
    {
      "before": "dict(pid=process.pid, launch=number)",
      "after": "dict(pid=process.pid, attempt=attempt, launch=number)"
    }
  ],
  "all_declarations_unchanged_from_22_addition_corrected_source": true,
  "all_other_harness_bytes_unchanged": true,
  "dependencies_unchanged": {
    "f3_rp1-r2_gate_tools_2026-10-10.py": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7",
    "f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "f3_rp1-r2_technical_tests_2026-10-10.py": "cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b"
  },
  "writer_unchanged_sha256": "c0b9e10c2022b744b23190e81243c2713e6d7cb39859b370d9f87216de03fa0e",
  "new_store": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\.rp1-r2_attempt2_restart_store_2026-10-10",
  "new_store_state": "ABSENT",
  "backup": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11",
  "outside_w3_comparator_outputs_imported": false,
  "real_data_access": false,
  "status": "PARTIAL_PENDING_PI"
}
```

## Attempt-2 launch-1 prerequisites

All current pins, historical inventory hashes/sidecars, environment and byte-exact frozen manifest regeneration passed. The exact permitted source delta is verified against quarantined attempt-1 bytes. The prior logged small-input tests and isolated comparator execution remain valid for the unchanged technical code and declarations. Their outputs remain excluded. The new attempt-2 store and all first-launch/custody paths are absent. Signed D-14 is verified and IR1-13 remains OPEN / B.

```json
{
  "created_utc": "2026-10-11T14:11:30.579340+00:00",
  "stage": "READY_FOR_ATTEMPT_2_LAUNCH_1",
  "attempt": 2,
  "launch": 1,
  "harness_sha256": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
  "launcher_sha256": "172e3d9bc67c0e5f8ad3406232bf77ec8c37c374a2429cee52c6491377916462",
  "writer_sha256": "c0b9e10c2022b744b23190e81243c2713e6d7cb39859b370d9f87216de03fa0e",
  "source_diff_allowed_only": [
    "22 missing ADDITION declarations",
    "attempt counter",
    "supersedes identities",
    "attempt-bound log/store/runtime custody names"
  ],
  "source_ast_matches_attempt1_after_removing_only_allowed_delta": true,
  "declarations_match_prior_22_addition_correction": true,
  "checks": [
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
      "pin": "5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5",
      "observed": "5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md",
      "pin": "e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387",
      "observed": "e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4_pi_dispatch_record_2026-09-24.md",
      "pin": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851",
      "observed": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md",
      "pin": "11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6",
      "observed": "11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_pi_ratified_content_2026-09-07.md",
      "pin": "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498",
      "observed": "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md",
      "pin": "283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330",
      "observed": "283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4-1_pi_dispatch_record_2026-09-29.md",
      "pin": "a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0",
      "observed": "a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md",
      "pin": "d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe",
      "observed": "d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4-2_pi_dispatch_record_2026-09-30.md",
      "pin": "a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb",
      "observed": "a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md",
      "pin": "ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82",
      "observed": "ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_fixture_generator_r4-1_2026-09-29.py",
      "pin": "68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830",
      "observed": "68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_fixture_manifest_r4-1_2026-09-29.csv",
      "pin": "5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe",
      "observed": "5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_results_r4-1_2026-09-29.json",
      "pin": "6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385",
      "observed": "6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md",
      "pin": "b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a",
      "observed": "b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md",
      "pin": "9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9",
      "observed": "9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md",
      "pin": "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5",
      "observed": "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md",
      "pin": "4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34",
      "observed": "4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_qualification_pi_decision_record_2026-10-02.md",
      "pin": "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3",
      "observed": "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4-2_pi_decision_record_2026-10-01.md",
      "pin": "aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae",
      "observed": "aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md",
      "pin": "9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575",
      "observed": "9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_results_r4-2_2026-09-30.json",
      "pin": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
      "observed": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_telemetry_r4-2_2026-09-30.csv",
      "pin": "ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d",
      "observed": "ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_test_evidence_r4-2_2026-09-30.json",
      "pin": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf",
      "observed": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f1_input_freeze_record_2026-08-28.md",
      "pin": "5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0",
      "observed": "5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\p_konum_plus_lightweight_review_policy_r1_2026-10-04.md",
      "pin": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
      "observed": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_realdata_prep_rp1_transmission_list_2026-10-04.md",
      "pin": "858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9",
      "observed": "858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1_2026-10-02.py",
      "pin": "39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09",
      "observed": "39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md",
      "pin": "2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d",
      "observed": "2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md",
      "pin": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364",
      "observed": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md",
      "pin": "2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989",
      "observed": "2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md",
      "pin": "aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef",
      "observed": "aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md",
      "pin": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5",
      "observed": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md",
      "pin": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f",
      "observed": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md",
      "pin": "f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913",
      "observed": "f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md",
      "pin": "82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e",
      "observed": "82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r1_2026-10-05.py",
      "pin": "cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb",
      "observed": "cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md",
      "pin": "98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956",
      "observed": "98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\p_konum_plus_lightweight_review_policy_r1_2026-10-04.md",
      "pin": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
      "observed": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md",
      "pin": "4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955",
      "observed": "4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\prompts\\f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
      "pin": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
      "observed": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f2_step2_feasibility_harness_r3_2026-09-01.py",
      "pin": "01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077",
      "observed": "01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077"
    },
    {
      "path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_spline_solver_qualification_harness_r2_2026-09-03.py",
      "pin": "b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d",
      "observed": "b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d"
    }
  ],
  "historical_inventory_checks": 43,
  "environment": {
    "python": "3.11.7",
    "numpy": "1.26.4",
    "scipy": "1.14.1",
    "platform": "Windows-10-10.0.19045-SP0",
    "OMP": "1",
    "OPENBLAS": "1",
    "MKL": "1"
  },
  "frozen_manifest_regenerated_equal": true,
  "technical_dependency_pins": {
    "f3_rp1-r2_gate_tools_2026-10-10.py": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7",
    "f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "f3_rp1-r2_technical_tests_2026-10-10.py": "cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b"
  },
  "authority": {
    "finding": "IR1-13",
    "disposition": "RECORDED_LIMITATION",
    "ledger_status": "OPEN / B",
    "pi_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
    "pi_record_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "standalone_evidence_status": "NOT OBSERVED",
    "executor_status": "PARTIAL_PENDING_PI"
  },
  "ledger_ir1_13_status": "OPEN / B",
  "small_test_execution_record": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-10_execution01\\execution_record.json",
  "small_test_record_sha256": "32c2d9c7cc72e6777d469392eed53cdbd82fbfc8ba5d004102a8c4acaa9ddb0f",
  "comparator_execution_record": "C:\\Users\\Neo\\Downloads\\rp1r2_preflight\\2026-10-11_comparator_execution01\\execution_record.json",
  "comparator_record_sha256": "b43a682456a49befee7bb03f67b9d219eb618c05687f8f6c37df1ccdfa9ff353",
  "preverification_basis": "Previously logged successful executions; technical functions/comparator/declarations unchanged by the administrative patch. No repeated execution or imported output.",
  "preverification_outputs_imported": false,
  "attempt2_store": "ABSENT; EMPTY AT FIRST LAUNCH",
  "attempt1_quarantine": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\quarantine\\f3_step2_rp1-r2_attempt1_2026-10-11",
  "supersedes_custody_sha256": "6384a57de7f11ab7d18920813215a3eb56c21466e24469ddf689a5fdaf791469",
  "real_data_access": false,
  "status": "PARTIAL_PENDING_PI",
  "commit": false
}
```

## Launch start (machine-transferred)

```json
{
  "attempt": 2,
  "launch": 1,
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "code_sha256": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-11T14:12:36.798018+00:00",
  "end_utc": "NOT OBSERVED (running)",
  "stdout": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_attempt2_launch1_stdout_2026-10-10.log",
  "stderr": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_attempt2_launch1_stderr_2026-10-10.log",
  "output_scope": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration",
  "outputs_discarded": false,
  "outside_w3_attempt": false,
  "real_data_access": false,
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "authorization": {
    "finding": "IR1-13",
    "disposition": "RECORDED_LIMITATION",
    "ledger_status": "OPEN / B",
    "pi_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
    "pi_record_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "standalone_evidence_status": "NOT OBSERVED",
    "executor_status": "PARTIAL_PENDING_PI"
  }
}
```

## Attempt-2 launch-1 startup verification (native observed receipt)

{
    "observed_utc":  "2026-10-11T14:14:15.3995712Z",
    "attempt":  2,
    "launch":  1,
    "pid":  17884,
    "status":  "RUNNING",
    "harness_sha256":  "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
    "custody_path":  "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_step2_rp1-r2_preexecution_custody_attempt2_launch1_2026-10-10.md",
    "custody_sha256":  "7d864db9c2e766ff1fc4d3ed77649e7a9a140249426d56e6d51779f7aa8efc8d",
    "supersedes_custody_sha256":  "6384a57de7f11ab7d18920813215a3eb56c21466e24469ddf689a5fdaf791469",
    "full_run_exit_code":  "NOT OBSERVED (running)",
    "full_run_result":  "NOT OBSERVED (running)",
    "startup_custody_verified":  true,
    "startup_dispatch_checks":  40,
    "initial_spline_nonregression_passed":  true,
    "initial_f1_loader_synthetic_passed":  true,
    "prelaunch_store":  "ABSENT; W3 records EMPTY",
    "real_data_access":  false,
    "executor_status":  "PARTIAL_PENDING_PI",
    "ir1_13":  "OPEN / B; D-14 RECORDED_LIMITATION",
    "commit":  false
}

## Launch end (machine-transferred)

```json
{
  "attempt": 2,
  "launch": 1,
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "code_sha256": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "start_utc": "2026-10-11T14:12:36.798018+00:00",
  "end_utc": "2026-10-12T00:18:03.422231+00:00",
  "stdout": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_attempt2_launch1_stdout_2026-10-10.log",
  "stderr": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_rp1-r2_attempt2_launch1_stderr_2026-10-10.log",
  "output_scope": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration",
  "outputs_discarded": false,
  "outside_w3_attempt": false,
  "real_data_access": false,
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "authorization": {
    "finding": "IR1-13",
    "disposition": "RECORDED_LIMITATION",
    "ledger_status": "OPEN / B",
    "pi_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
    "pi_record_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "standalone_evidence_status": "NOT OBSERVED",
    "executor_status": "PARTIAL_PENDING_PI"
  },
  "pid": 17884,
  "return_code": 0,
  "stdout_sha256": "0f9466ec8c6522fc755345efe7c21e3dd54081ef7d334f8bd88cbd50491cca93",
  "stderr_sha256": "afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b"
}
```

## Final section-8 delivery preparation

Native record generation only; no harness, copy, test excerpt, optimizer or real-data execution. Attempt 1 failed with missing ADDITION declarations; the logged section-0 correction and PI-authorized attempt-2 provenance patch are retained. Attempt 2 completed with exit code 0. No outside-W3 execution output is imported. Restart stores, pickle payloads and ZIPs are excluded from Git delivery.

```json
{
  "created_utc": "2026-10-12T10:49:59.111030+00:00",
  "rp1_r2_status": "PARTIAL_PENDING_PI",
  "final_attempt": 2,
  "final_launch": 1,
  "pid": 17884,
  "exit_code": 0,
  "start_utc": "2026-10-11T14:12:36.798018+00:00",
  "end_utc": "2026-10-12T00:18:03.422231+00:00",
  "elapsed_seconds": 36326.624213,
  "recorded_tests": 50,
  "passed_tests": 50,
  "technical_cases": 48,
  "technical_q3_cases": 8,
  "nonregression_rows": 219434,
  "e_declared": 219433,
  "s_findings": 0,
  "u_findings": 0,
  "telemetry_rows": 12298,
  "percall_rows": 22217,
  "family_rows": 47706,
  "timing_rows": 6,
  "store_manifest_rows": 67316,
  "store_read_rows": 733,
  "fixture_input_files": 2204,
  "run1_canonical_sha256": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
  "run2_canonical_sha256": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
  "result_sha256": "81e1b523cc41561edabbea9098696646355b811d4b1ce86493bf10fae7e63818",
  "harness_sha256": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
  "ledger_status_counts": {
    "IMPLEMENTED_PENDING_VERIFICATION": 24,
    "CLOSED (prior auditor decision only)": 2,
    "OPEN": 5
  },
  "result_end_state": {
    "F3_STEP2_r4_status": "PARTIAL_PENDING_PI",
    "PI_dispatch_record_hash": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f",
    "PI_dispatch_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md",
    "S_R2_1_source_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851",
    "S_R2_1_source_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md",
    "corrections_complete": true,
    "deferred_decisions": [],
    "mandatory_tests_all_run": true,
    "mandatory_tests_missing": [],
    "narrowed_evidence": [
      "T-R2-2",
      "T-RP-1"
    ],
    "open_findings": [],
    "rp1_r2_open_findings": [
      "RP1A-01",
      "RP1A-02",
      "RP1A-03",
      "RP1A-04",
      "RP1A-05",
      "RP1A-06",
      "R42A-03 (b)",
      "R42A-09",
      "D-9 \u00a72(a) binding of rp1/rp1-r1 bytes",
      "A.5 (iii) inadmissible refit",
      "IR1-04",
      "IR1-13",
      "F1 input-hash-table sidecar"
    ],
    "rp1_r2_status": "PARTIAL_PENDING_PI",
    "standalone_evidence_status": "NOT OBSERVED",
    "uncovered_coverage_rows": [
      "A.5 (iii) inadmissible refit"
    ]
  },
  "real_data_access": false,
  "environment": {
    "MKL": "1",
    "OMP": "1",
    "OPENBLAS": "1",
    "numpy": "1.26.4",
    "platform": "Windows-10-10.0.19045-SP0",
    "python": "3.11.7",
    "scipy": "1.14.1"
  },
  "historical_errata": {
    "handoff_spline_rows": {
      "historical_narrative": 8895,
      "observed": 9223,
      "path": "p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv",
      "sha256": "d9d1c2564c9a24cddf55f31f662f09a40d453308536d5fcbbfa0dcfdfe1f000a"
    },
    "warning_records": {
      "historical_narrative": "42k+",
      "observed": 33013,
      "lines": 66026,
      "runtime_warnings": 28,
      "path": "p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log",
      "sha256": "afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b"
    },
    "external_writer_pins": {
      "historical_narrative": 31,
      "observed": 20,
      "path": "p_konum_plus/calibration/_w3_writer_rp1-r1_tmp.py",
      "sha256": "30badd450c236b650614b38767d3ce83ecf13a36b0a8043beda4265dfd4eced0"
    },
    "upstream_inventory_count": {
      "historical_narrative": 11,
      "audit_corrected": 12,
      "status": "Audit attribution; no historical document modified."
    },
    "scen_a_estimate_scope": "Historical SCEN-A family telemetry is MINI_BANK; a full-bank description is unsupported. New size estimate requires measured Q10 bytes; NOT OBSERVED.",
    "missing_historical_custody": "Deleted dry-copy custody and historical ZIP associations: X / NOT OBSERVED. Existing untracked ZIPs are not used to reconstruct historical identity."
  },
  "final_ledger_open_findings": [
    "R42A-09",
    "D-9 \u00a72(a) binding of rp1/rp1-r1 bytes",
    "A.5 (iii) inadmissible refit",
    "IR1-13",
    "F1 input-hash-table sidecar"
  ]
}
```
