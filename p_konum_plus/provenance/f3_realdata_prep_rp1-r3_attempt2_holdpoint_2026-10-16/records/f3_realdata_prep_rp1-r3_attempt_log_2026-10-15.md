# rp1-r3 attempt log

```json
{
  "time_utc": "2026-10-15T17:16:55.757120+00:00",
  "phase": "INITIALIZATION",
  "preconditions": "PASSED",
  "inventory": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_start_state_inventory_2026-10-15.json",
  "inventory_sha256": "8d1c6dbecf4ed250b853314de1a0e22f3561845e330b7876f0efc3df548f5f70",
  "preexisting_untracked_count": 69655,
  "attachments_copied_unchanged": 18,
  "tracked_changes_before_first_write": false,
  "inventory_interruption": "Streaming inventory process ended before completion; complete recorded rows retained; remaining entries hashed; only own new inventory rewritten. No protected file modified.",
  "real_data_access": false,
  "commit": false,
  "source_change": {
    "item": "R3-1",
    "path": "p_konum_plus\\calibration\\f3_rp1-r3_gate_tools_2026-10-15.py",
    "parent": "p_konum_plus\\calibration\\f3_rp1-r2_gate_tools_2026-10-10.py",
    "parent_sha256": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7",
    "sha256": "d52ff0dc61f99edd1226551c854550b6fe4420374c20a652ecc812f0c170a30b",
    "scope": "Only exception text extraction; frame/statement normalization unchanged."
  }
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_historical_execution01",
  "time_utc": "2026-10-15T17:18:13.000870+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_historical_comparison_2026-10-15.py",
  "code_sha256": "72c72f02509c62d40e7c2d0ae3414b43fe90872173a223db5606f1d999b0d2cd",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution01",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_historical_comparison_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution01"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "SOURCE_AUTHORED",
  "time_utc": "2026-10-15T17:20:09.324309+00:00",
  "items": [
    "R3-1 tests",
    "R3-2",
    "R3-3",
    "R3-5 scope guard tests"
  ],
  "path": "p_konum_plus\\calibration\\f3_rp1-r3_technical_tests_2026-10-15.py",
  "sha256": "a4ba108f778566f1df84126ff27cb406f1e311e03e54b6e07df28336513cc15d",
  "parent": "p_konum_plus\\calibration\\f3_rp1-r2_technical_tests_2026-10-10.py",
  "parent_sha256": "cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b",
  "intermediate": "Own unexecuted test-block source folded into the new technical-test module and removed; no pre-existing file touched.",
  "execution": "NOT YET EXECUTED"
}
```

```json
{
  "event": "OUTSIDE_W3_INTERRUPTED",
  "execution_id": "2026-10-15_historical_execution01",
  "time_utc": "2026-10-15T18:40:53.186116+00:00",
  "observed": "No running Python process, no execution_record.json or comparison_result.json; stdout and stderr both empty. No comparison outcome observed.",
  "disposition": "Incomplete execution retained outside every deliverable and store; will rerun unchanged code with a new execution id using an independent hidden process.",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_historical_execution02",
  "time_utc": "2026-10-15T18:40:53.606988+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_historical_comparison_2026-10-15.py",
  "code_sha256": "72c72f02509c62d40e7c2d0ae3414b43fe90872173a223db5606f1d999b0d2cd",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution02",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_historical_comparison_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution02"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "HARNESS_SOURCE_AUTHORED",
  "time_utc": "2026-10-15T18:43:47.036077+00:00",
  "path": "p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r3_2026-10-15.py",
  "sha256": "90d733a4a1fa1eb0a971838c4aa507992cf60b2aac98738bac31cacbd0993da1",
  "parent_sha256": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
  "run_real_scenario_AST_segment_byte_equal": true,
  "inherited_declarations_unchanged_except_two_R3_4_reasons": true,
  "new_declarations": {
    "results": [
      {
        "path": "rp1_r3_scope_guard.ran",
        "id": "results:rp1_r3_scope_guard.ran",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.pass_",
        "id": "results:rp1_r3_scope_guard.pass_",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].name",
        "id": "results:rp1_r3_scope_guard.cases[*].name",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].expected",
        "id": "results:rp1_r3_scope_guard.cases[*].expected",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].got",
        "id": "results:rp1_r3_scope_guard.cases[*].got",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].ok",
        "id": "results:rp1_r3_scope_guard.cases[*].ok",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "tests_run.T-RP1R3-RRS-UNCHANGED.ran",
        "id": "results:tests_run.T-RP1R3-RRS-UNCHANGED.ran",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "tests_run.T-RP1R3-RRS-UNCHANGED.passed",
        "id": "results:tests_run.T-RP1R3-RRS-UNCHANGED.passed",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "end_state.rp1_r3_status",
        "id": "results:end_state.rp1_r3_status",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "end_state.rp1_r3_open_findings",
        "id": "results:end_state.rp1_r3_open_findings",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      }
    ],
    "test_evidence": [
      {
        "path": "rp1_r3_scope_guard.ran",
        "id": "test_evidence:rp1_r3_scope_guard.ran",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.pass_",
        "id": "test_evidence:rp1_r3_scope_guard.pass_",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].name",
        "id": "test_evidence:rp1_r3_scope_guard.cases[*].name",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].expected",
        "id": "test_evidence:rp1_r3_scope_guard.cases[*].expected",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].got",
        "id": "test_evidence:rp1_r3_scope_guard.cases[*].got",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "rp1_r3_scope_guard.cases[*].ok",
        "id": "test_evidence:rp1_r3_scope_guard.cases[*].ok",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "tests_run.T-RP1R3-RRS-UNCHANGED.ran",
        "id": "test_evidence:tests_run.T-RP1R3-RRS-UNCHANGED.ran",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      },
      {
        "path": "tests_run.T-RP1R3-RRS-UNCHANGED.passed",
        "id": "test_evidence:tests_run.T-RP1R3-RRS-UNCHANGED.passed",
        "kind": "ADDITION",
        "reason": "R3-5 / section 8: new mandatory immutable-consumer scope evidence and cycle status; absent from r4-2; authored before launch 1."
      }
    ]
  },
  "dependency_pins": {
    "f3_rp1-r3_gate_tools_2026-10-15.py": "d52ff0dc61f99edd1226551c854550b6fe4420374c20a652ecc812f0c170a30b",
    "f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "f3_rp1-r3_technical_tests_2026-10-15.py": "a4ba108f778566f1df84126ff27cb406f1e311e03e54b6e07df28336513cc15d"
  },
  "execution": "NOT YET EXECUTED; no W-3 or attempt store created"
}
```

```json
{
  "created_utc": "2026-10-15T18:44:18.251845+00:00",
  "scope": "IR2-07 named records only; no reconstruction and no outputs admitted to any attempt store",
  "authority_path": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md",
  "authority_sha256": "90b72e1f293b95758fa7fbf0cbfa40816affcd172926ece04694521ec8698f8c",
  "observed_hash_match_count": 11,
  "not_observed_count": 2262,
  "real_data_access": false,
  "contamination_inferred": false,
  "D14_extended": false,
  "event": "IR2-07_RECORDS_VERIFIED",
  "observation_record": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_IR2-07_observations_2026-10-15.json",
  "observation_record_sha256": "c355979573c434aa0288fb0891046ab30649c28d61b75a321fcc41c48d6db351"
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_synthetic_execution01",
  "time_utc": "2026-10-15T18:45:10.484162+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
  "code_sha256": "b216d013e48a1e800419630b2c6d6e4b27d612fd14d8303ddb04db0898f46a29",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution01",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution01"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-15_synthetic_execution01",
  "time_utc": "2026-10-15T18:45:14.088970+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution01\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution01\\stdout.log",
      "sha256": "a6924ec273b8f522bc3773d11fd2478b09cf9cda40f11e68ed529758f7ace4b9",
      "bytes": 206
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution01\\synthetic_result.json",
      "sha256": "4c9810a8b74c7202989853b1317fdaa240d0d50d805d2150312d50eb77b6c082",
      "bytes": 357027
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "LAUNCHER_CUSTODY_SOURCE_AUTHORED",
  "time_utc": "2026-10-15T18:46:25.887484+00:00",
  "scope": "R3-5 identity only: filenames, date tag and launch environment name. No behavior or authorization rule change. Attempt number and supersession are read from new harness constants.",
  "sources": [
    {
      "path": "p_konum_plus\\calibration\\f3_rp1-r3_launch_attempt_2026-10-15.py",
      "sha256": "e55b16569b2f1729597f95cf8d0849f08d6ce0da44f930cf5f5b568968112496",
      "parent": "p_konum_plus\\calibration\\f3_rp1-r2_launch_attempt_2026-10-10.py",
      "parent_sha256": "172e3d9bc67c0e5f8ad3406232bf77ec8c37c374a2429cee52c6491377916462"
    },
    {
      "path": "p_konum_plus\\calibration\\f3_rp1-r3_write_custody_2026-10-15.py",
      "sha256": "cf8709b364b75396f6f8fe6e252645ffc622129b724e22bd223e476a9236c5eb",
      "parent": "p_konum_plus\\calibration\\f3_rp1-r2_write_custody_2026-10-10.py",
      "parent_sha256": "c0b9e10c2022b744b23190e81243c2713e6d7cb39859b370d9f87216de03fa0e"
    }
  ],
  "execution": "NOT YET EXECUTED; W-3 and attempt store not created"
}
```

```json
{
  "event": "PRELAUNCH_IDENTITY_TEXT_COMPLETED",
  "time_utc": "2026-10-15T18:47:57.448569+00:00",
  "item": "R3-5",
  "scope": "Top-level module identity and launch environment help text now name rp1-r3/D-19. No declaration, expectation or scientific function changed.",
  "path": "p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r3_2026-10-15.py",
  "sha256": "96053657688ff6ba10b9e3747b4ffd8d2b9ed6632ef8708d12e7d76471969e46",
  "requires_a2_reverification_of_final_source_hash": true
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_synthetic_execution02",
  "time_utc": "2026-10-15T18:49:53.937791+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
  "code_sha256": "b216d013e48a1e800419630b2c6d6e4b27d612fd14d8303ddb04db0898f46a29",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution02",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution02"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-15_synthetic_execution02",
  "time_utc": "2026-10-15T18:49:57.316756+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution02\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution02\\stdout.log",
      "sha256": "a6924ec273b8f522bc3773d11fd2478b09cf9cda40f11e68ed529758f7ace4b9",
      "bytes": 206
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution02\\synthetic_result.json",
      "sha256": "a89a66f75ca1daa74967b9a3d1c543866e538e852d1454a4d0c5dec51071dd0a",
      "bytes": 357027
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "RECORDS_PREPARED",
  "time_utc": "2026-10-15T18:51:24.041784+00:00",
  "synthetic_prevalidation": "2026-10-15_synthetic_execution02 returned 0; Q4/Q5/Q6/RRS pass; outputs retained outside all deliverables/stores",
  "diff_record_sha256": "4b2f3c1f900dd66aabaeed71191616341f9190c5800a4d26833e833a2b1e98e3",
  "record_generator_issue": "Missing label for blank inherited separator at current harness line 4145; no harness/test/declaration changed. Native record generator assigns blank separators to nearest labelled statement; regenerated only own new diff/label files.",
  "rerun_procedure": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_auditor_rerun_procedure_r1_2026-10-15.md",
  "rerun_procedure_sha256": "f5141e15f968b7971fc40547c9e0b3263ec86df21f28346597b77948866a5d09",
  "overwrite_inventory": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_rerun_overwrite_inventory_r1_2026-10-15.json",
  "source_derived_output_path_count": 24
}
```

```json
{
  "event": "IMPLEMENTATION_EVIDENCE_RECORDED",
  "time_utc": "2026-10-15T18:53:09.277341+00:00",
  "ledger_path": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_ledger_2026-10-15.json",
  "ledger_sha256": "40469e3ddcece85e0339e7dc0e54ace4d5008fa58666fb54f47db4acc3adb9b8",
  "ledger_item_count": 38,
  "due_items_implemented_pending_verification": 12,
  "IR1-13": "OPEN / B; RECORDED_LIMITATION under D-14; not due in rp1-r3",
  "preflight_execution_metadata_records": [
    {
      "source": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution01\\execution_record.json",
      "destination": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_2026-10-15_synthetic_execution01_execution_record.json",
      "sha256": "d2ae40922df35cc95d6c83df17c3cbdb86550c8a0ef15b484b7b8f43cc680014"
    },
    {
      "source": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution02\\execution_record.json",
      "destination": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_2026-10-15_synthetic_execution02_execution_record.json",
      "sha256": "bcfda14fdec1846382bbf04ecd75802feb77eea4767128f8f56d8a645dc99173"
    }
  ],
  "outside_preflight_test_outputs_copied_to_delivery_or_store": false,
  "W3_run": "NOT STARTED"
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-15_historical_execution02",
  "time_utc": "2026-10-15T19:00:04.408899+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution02\\comparison_result.json",
      "sha256": "7d100221de3f99cf21015893b54550663379b9158d421662d29e176a15db574b",
      "bytes": 135353
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution02\\executed_source_excerpts.txt",
      "sha256": "299f83d5cc622a85708eb7f4c3d30f3a04df121921ef97d0ab1426196ed43115",
      "bytes": 1634
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution02\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution02\\stdout.log",
      "sha256": "33c969c955f1a0a25223d268dcac63a42f7f5f5b963d07c533b4c7a6c5e0f867",
      "bytes": 216
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_historical_execution03",
  "time_utc": "2026-10-15T19:00:46.920108+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_cached_historical_comparison_2026-10-15.py",
  "code_sha256": "535680c8b2d0e83d5a5eef3a19c3653719aebd8a4e7e85cd67542f7f5e0d918e",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution03",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_cached_historical_comparison_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution03"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "IR2-05_LEDGER_RECORD_COMPLETED",
  "time_utc": "2026-10-15T19:02:07.116016+00:00",
  "ledger_sha256": "90dcac7d02a74c1677db3ad535e70a98231cbce2aa2573731668b4617d152a4a",
  "item": "R42A-09",
  "current_status": "CLOSED",
  "auditor_record_sha256": "dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2",
  "removed_stale_legacy_reason_fields": [
    "historical_evidence",
    "prelaunch_evidence"
  ],
  "current_evidence_source": "Named rp1-r2 independent auditor table; closure attribution retained; initial inventory and previous packages unchanged."
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-15_historical_execution03",
  "time_utc": "2026-10-15T19:03:02.098799+00:00",
  "returncode": 4294967295,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution03\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution03\\stdout.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "R3_1_PRELAUNCH_NORMALIZATION_REFINEMENT",
  "time_utc": "2026-10-15T19:03:26.539619+00:00",
  "reason": "Preserve field text immediately preceding a harness path; normalize exact frame paths and absolute paths without consuming field= prefixes. Frame/statement normalization remains unchanged.",
  "added_tests": [
    "path_in_exception_text",
    "field_before_path_preserved"
  ],
  "dependency_pins": {
    "f3_rp1-r3_gate_tools_2026-10-15.py": "1666abcf25d54bbc0b2ea3f404e286801149c3b7fb223eb83a49c1a54a75c045",
    "f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "f3_rp1-r3_technical_tests_2026-10-15.py": "9d68989488657a8dc8f1bc3ce119ea1232415971043d0f9de799a4a014df9879"
  },
  "harness_sha256": "436eff5799998db9d74f36b4b8dbd365ced9bf96221ca42e406f3996aff9a563",
  "declarations_changed": false,
  "W3_attempt_started": false,
  "historical_execution02": "Completed successfully before refinement; not reused as final-input verification",
  "historical_execution03": "Redundant cache-capacity diagnostic intentionally stopped after execution02 success; not a comparison failure or a W3 attempt. Logged return code retained.",
  "required_reverification": "New logged a1 and a2 executions against these final input hashes before any W3 launch"
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_synthetic_execution03",
  "time_utc": "2026-10-15T19:03:48.425915+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
  "code_sha256": "b216d013e48a1e800419630b2c6d6e4b27d612fd14d8303ddb04db0898f46a29",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution03",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution03"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-15_synthetic_execution03",
  "time_utc": "2026-10-15T19:03:51.873626+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution03\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution03\\stdout.log",
      "sha256": "69804dbc8499fd2b8ca91e3125c7937013487f8dfe0846639f6d882a3ba8e373",
      "bytes": 206
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution03\\synthetic_result.json",
      "sha256": "1bc784afecde2ae2584208f680c83332a2eb086d02d86c97195682abbb421892",
      "bytes": 381794
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_historical_execution04",
  "time_utc": "2026-10-15T19:04:01.364545+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_cached_historical_comparison_2026-10-15.py",
  "code_sha256": "535680c8b2d0e83d5a5eef3a19c3653719aebd8a4e7e85cd67542f7f5e0d918e",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution04",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_cached_historical_comparison_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution04"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "R3_5_SUPERSESSION_CUSTODY_FIELDS_COMPLETED",
  "time_utc": "2026-10-15T19:05:04.605595+00:00",
  "scope": "The new W-3 writer now writes the three source-pinned SUPERSEDES fields explicitly; this is the R3-5 authorized supersession-chain wiring. No test, scientific function, declaration or expectation changed.",
  "writer_sha256": "f6f5c05f755de52db4b09016e08261126fb3d2c767f20bd3e1b61e7cc6a718e5",
  "diff_custody_sha256": "04fa407ee33afdf8e5d9bd1d0f4d329124d222663baf32e4436836c68f35b7dc",
  "ledger_sha256": "7809a46a0d1a599541f6fa359b2075735be82c2a2d898840e43a827b5abea83d",
  "historical_execution04": "Running against final core source hashes",
  "synthetic_execution03": "Returned 0 against final core source hashes; metadata copied, outputs remain external",
  "W3_run": "NOT STARTED"
}
```

```json
{
  "event": "NATIVE_SCOPE_GUARD_CAUGHT_ENCODING_DEFECT_BEFORE_W3",
  "time_utc": "2026-10-15T19:07:44.999744+00:00",
  "cause": "One native source-pin update read our new UTF-8 harness with the Windows default encoding before writing UTF-8. The source-scope guard rejected resulting inherited docstring changes.",
  "action": "Reverse that single encoding conversion in our new harness; restore inherited text exactly. Parent files untouched; no expectation/declaration change or scientific arithmetic change.",
  "previous_own_file_sha256": "436eff5799998db9d74f36b4b8dbd365ced9bf96221ca42e406f3996aff9a563",
  "repaired_own_file_sha256": "53145cdd26e1263708a90b8dca08d0a8cab95d1fe0cdc126eb878726534a44db",
  "W3_attempt_started": false,
  "required_reverification": "Native AST and inherited-declaration checks, diff regeneration and new a2 on repaired source. a1 historical execution04 does not read this new harness: it reads the delivered parent harness and current tools, both unchanged by this repair."
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-15_synthetic_execution04",
  "time_utc": "2026-10-15T19:07:53.604365+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
  "code_sha256": "b216d013e48a1e800419630b2c6d6e4b27d612fd14d8303ddb04db0898f46a29",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution04",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution04"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-15_synthetic_execution04",
  "time_utc": "2026-10-15T19:07:57.156590+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution04\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution04\\stdout.log",
      "sha256": "69804dbc8499fd2b8ca91e3125c7937013487f8dfe0846639f6d882a3ba8e373",
      "bytes": 206
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_synthetic_execution04\\synthetic_result.json",
      "sha256": "c5382476d7fa44f1192bce7fdbaed9a2ceac6d401fd5083dcf0c72011e90df7d",
      "bytes": 381794
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "FINAL_NATIVE_SOURCE_SCOPE_CHECK_PASSED",
  "time_utc": "2026-10-15T19:08:59.385090+00:00",
  "code_path": "p_konum_plus\\calibration\\f3_rp1-r3_run_controller_2026-10-15.py",
  "code_sha256": "bf8279346e9323980e6d89d66889e09742b3e6aaf807d5f7affd0b0e79015214",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "scope": "Source AST and inherited declaration comparison only; no harness import or computation",
  "observed": {
    "unchanged_nonmain_harness_functions": 107,
    "immutable_consumer_segment_equal": true,
    "inherited_declarations_preserved_except_two_authorized_reasons": true,
    "new_addition_declarations": {
      "results": 10,
      "test_evidence": 8
    },
    "launcher_writer_identity_and_authorized_supersession_only": true
  },
  "repaired_harness_sha256": "53145cdd26e1263708a90b8dca08d0a8cab95d1fe0cdc126eb878726534a44db",
  "ledger_sha256": "266a4f7bcf5cd5a18c91f68c7857ad587a6ee051c5a1a87454348e1056770bbc",
  "real_data_access": false
}
```

```json
{
  "time_utc": "2026-10-15T19:09:18.477211+00:00",
  "event": "NATIVE_CONTROLLER_STARTED",
  "controller_pid": 72424,
  "config_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_controller_custody_config_2026-10-15.json",
  "config_sha256": "64ed7a8e548e4d2cd643461a32c5b830cd58582fcc1bbfbec7bfc6dc6178133e",
  "state": "WAITING_FOR_RECORDED_HISTORICAL_COMPARISON",
  "commit": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-15_historical_execution04",
  "time_utc": "2026-10-15T19:18:56.508010+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution04\\comparison_result.json",
      "sha256": "e17b901ecfcf36fad46179f33c0f6d0caa5172e43b2e8107b300e707b3278385",
      "bytes": 135353
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution04\\executed_source_excerpts.txt",
      "sha256": "299f83d5cc622a85708eb7f4c3d30f3a04df121921ef97d0ab1426196ed43115",
      "bytes": 1634
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution04\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-15_historical_execution04\\stdout.log",
      "sha256": "33c969c955f1a0a25223d268dcac63a42f7f5f5b963d07c533b4c7a6c5e0f867",
      "bytes": 216
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "time_utc": "2026-10-15T19:19:13.183003+00:00",
  "event": "ALL_NATIVE_PRELAUNCH_CHECKS_PASSED",
  "scope_checks": {
    "unchanged_nonmain_harness_functions": 107,
    "immutable_consumer_segment_equal": true,
    "inherited_declarations_preserved_except_two_authorized_reasons": true,
    "new_addition_declarations": {
      "results": 10,
      "test_evidence": 8
    },
    "launcher_writer_identity_and_authorized_supersession_only": true
  },
  "historical_execution_record_sha256": "ff8277aadf1f9193bbf92f3f67537fbeccbec7ec63d7531992166cbf663c9c90",
  "historical_comparison_output_sha256": "e17b901ecfcf36fad46179f33c0f6d0caa5172e43b2e8107b300e707b3278385",
  "historical_further_finding_count": 0,
  "synthetic_result_output_sha256": "c5382476d7fa44f1192bce7fdbaed9a2ceac6d401fd5083dcf0c72011e90df7d",
  "parent_payloads_reverified": 2298,
  "due_implemented_items": 12,
  "store_before_launch": "EMPTY_OR_ABSENT",
  "real_data_access": false,
  "authority": "Signed D-19 plus exact D-14 authorization checked by the unchanged launcher/writer rule",
  "commit": false
}
```

```json
{
  "time_utc": "2026-10-15T19:19:15.751694+00:00",
  "event": "CONTROLLER_STOP",
  "reason": "ATTEMPT1_FAILED_NO_AUTOMATIC_CORRECTION",
  "exception_type": "AssertionError",
  "full_run_authorized_only_after_all_gates": true,
  "no_automatic_code_or_declaration_changes": true,
  "real_data_access": false,
  "commit": false
}
```

```json
{
  "event": "W3_WRITER_STOP_DIAGNOSIS_READ_ONLY",
  "observed_utc": "2026-10-16T10:02:13.884934+00:00",
  "writer_record_path": "p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_w3_writer_2026-10-15.json",
  "writer_record_sha256": "5c9661045c6602195296689229834c4f178fb7cab03c9ad5fe3337aa2b9bf459",
  "writer_return_code": 1,
  "writer_start_utc": "2026-10-15T19:19:13.446643+00:00",
  "writer_end_utc": "2026-10-15T19:19:15.686860+00:00",
  "harness_path": "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py",
  "harness_sha256": "53145cdd26e1263708a90b8dca08d0a8cab95d1fe0cdc126eb878726534a44db",
  "failure": "FileNotFoundError in W-3 writer dispatch-pin verification. Generated harness refers to incorrectly renamed historical inputs; this is our generated-path defect, not evidence that supplied historical input bytes were missing.",
  "missing_dispatch_paths": [
    {
      "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-15.md",
      "expected_sha256": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5",
      "name": "rp1-r3 incoming Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-15.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-15.md",
      "expected_sha256": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f",
      "name": "rp1-r3 incoming f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-15.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-15.md",
      "expected_sha256": "f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913",
      "name": "rp1-r3 incoming f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-15.md"
    },
    {
      "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_IR1-13_pi_decision_record_2026-10-15.md",
      "expected_sha256": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
      "name": "D-14 IR1-13 RECORDED_LIMITATION"
    }
  ],
  "correct_first_input": {
    "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md",
    "exists": true,
    "sha256": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5"
  },
  "harness_start_record_exists": false,
  "W3_record_exists": false,
  "attempt_store_exists": false,
  "code_changes_after_stop": false,
  "retry_started": false,
  "commit": false,
  "push": false
}
```

```json
{
  "created_utc": "2026-10-16T16:49:09.727471+00:00",
  "authority": "D-20 C-4",
  "quarantine_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\quarantine\\f3_step2_rp1-r3_attempt1_2026-10-16",
  "copied_file_count": 149,
  "inventory_sha256": "f0a4cf8cf2b4d84138a05c8a5f873fb8247aa64546e46c4a3cc8dbd1639bcd10",
  "attempt1_harness_sha256": "53145cdd26e1263708a90b8dca08d0a8cab95d1fe0cdc126eb878726534a44db",
  "attempt1_writer_record_sha256": "5c9661045c6602195296689229834c4f178fb7cab03c9ad5fe3337aa2b9bf459",
  "originals_moved_or_modified": false,
  "active_attempt1_W3_record_exists": false,
  "real_data_access": false,
  "event": "D20_C4_ATTEMPT1_QUARANTINE_BEFORE_FIRST_EDIT",
  "D20_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_2026-10-16.md",
  "D20_sha256": "778d8aff874991591cf45ae37e4fc0c698fb066304e16b6503e29868f693eff2",
  "decision": "B; HOLD BEFORE ATTEMPT2 LAUNCH",
  "observed_failure": "Attempt-1 W-3 writer stopped on a substituted historical input path; no W-3 record, harness execution or attempt store. No classification or ledger closure inferred."
}
```

```json
{
  "event": "D20_C1_C4_BOUNDED_SOURCE_CHANGES",
  "time_utc": "2026-10-16T16:51:29.226341+00:00",
  "D20_sha256": "778d8aff874991591cf45ae37e4fc0c698fb066304e16b6503e29868f693eff2",
  "incoming_count": 10,
  "carried_count": 11,
  "harness_sha256": "a49d72496ce381572d23f21ba8611f9e123e52a07383eb6aef1045f38d0f3192",
  "writer_sha256": "822560025b80920431998005b647076348f4e3026546e42a852718ea1f082891",
  "changes": [
    "C-1: exact incoming and carried named groups, joined for existing dispatch iteration; every hash read from bytes and matched D-20 printed values",
    "C-1: writer resolves only that specific two-group concatenation",
    "C-4: ATTEMPT_NUMBER=2, isolated attempt-2 store, attempt-1 writer-record supersession and explicit no attempt-1 W-3 record; parent rp1-r2 supersession chain retained",
    "C-4: writer reports those attempt-1 supersession fields"
  ],
  "harness_functions_including_main_unchanged": 108,
  "expectations_and_declarations_unchanged": true,
  "Q4_Q5_Q6_tests_and_behaviour_changed": false,
  "launch_started": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-16_attempt2_C3_execution01",
  "time_utc": "2026-10-16T16:52:55.294482+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_literal_listing_2026-10-16.py",
  "code_sha256": "f13d0f9b11a53388ad5963a461ee4dec04312986fc89ef7a0661b26222015966",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution01",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_literal_listing_2026-10-16.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution01"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-16_attempt2_C3_execution01",
  "time_utc": "2026-10-16T16:52:58.211120+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution01\\C3_literal_listing.csv",
      "sha256": "9cf65d726941ceeb4a8f1881b1d4ee02fd3a67a3b7054ea1b5e6bda6ffcc07e4",
      "bytes": 81316
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution01\\C3_literal_listing.json",
      "sha256": "6cce838d89fe324c9f534237cdacd7c51c932f50f71efd482857ef2afbd9e799",
      "bytes": 156815
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution01\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution01\\stdout.log",
      "sha256": "e41028577b5ba4eb49bd0c24cff041c6e321c363304fd2c4476c96da07cd69cb",
      "bytes": 6564
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "D20_C3_TEXT_PRESERVATION_DURING_PREPARATION",
  "time_utc": "2026-10-16T16:54:17.364412+00:00",
  "detail": "C-3 showed that initial C-1 assembly had copied parent descriptive labels. Carried descriptive labels are kept byte-identical to attempt 1; only C-1 paths/hashes are restored. Wrong-looking TEXT is reported without repair.",
  "preserved_attempt1_label_count": 8,
  "harness_sha256": "9ff48dbe6a5fdb6e4ae9d1952f1f7ecaba553eb84ef4e2a60de0be8258e8f96e",
  "expectations_or_declarations_changed": false,
  "launch_started": false
}
```

```json
{
  "event": "D20_C5_CHECKS_START_SOURCE_BINDING",
  "binding_path": "p_konum_plus\\provenance\\f3_realdata_prep_rp1-r3_attempt2_C5_source_binding_2026-10-16.json",
  "binding_sha256": "e3f71f7c41a4963a6eedd7d0afb5aff7be297ffff090ae3ec5b5ecf537236f5d",
  "record": {
    "created_utc": "2026-10-16T16:54:50.519439+00:00",
    "authority": "D-20 C-5; pre-launch checks only; hold point B",
    "core_source_hashes": {
      "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py": "9ff48dbe6a5fdb6e4ae9d1952f1f7ecaba553eb84ef4e2a60de0be8258e8f96e",
      "p_konum_plus/calibration/f3_rp1-r3_gate_tools_2026-10-15.py": "1666abcf25d54bbc0b2ea3f404e286801149c3b7fb223eb83a49c1a54a75c045",
      "p_konum_plus/calibration/f3_rp1-r3_technical_tests_2026-10-15.py": "9d68989488657a8dc8f1bc3ce119ea1232415971043d0f9de799a4a014df9879",
      "p_konum_plus/calibration/f3_rp1-r3_launch_attempt_2026-10-15.py": "e55b16569b2f1729597f95cf8d0849f08d6ce0da44f930cf5f5b568968112496",
      "p_konum_plus/calibration/f3_rp1-r3_write_custody_2026-10-15.py": "822560025b80920431998005b647076348f4e3026546e42a852718ea1f082891"
    },
    "historical_check_code_hashes": {
      "p_konum_plus/calibration/f3_rp1-r3_cached_historical_comparison_2026-10-15.py": "535680c8b2d0e83d5a5eef3a19c3653719aebd8a4e7e85cd67542f7f5e0d918e",
      "p_konum_plus/calibration/f3_rp1-r3_historical_comparison_2026-10-15.py": "72c72f02509c62d40e7c2d0ae3414b43fe90872173a223db5606f1d999b0d2cd",
      "p_konum_plus/calibration/f3_rp1-r3_logged_preflight_2026-10-15.py": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617"
    },
    "no_harness_computation": true,
    "no_optimizer": true,
    "full_launch_authorized": false
  }
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-16_attempt2_C5_a1_execution01",
  "time_utc": "2026-10-16T16:54:50.915382+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_cached_historical_comparison_2026-10-15.py",
  "code_sha256": "535680c8b2d0e83d5a5eef3a19c3653719aebd8a4e7e85cd67542f7f5e0d918e",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a1_execution01",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_cached_historical_comparison_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a1_execution01"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-16_attempt2_C5_w3_execution01",
  "time_utc": "2026-10-16T16:56:12.767910+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_w3_check_2026-10-16.py",
  "code_sha256": "b72b2607fb262494460060f7483b7756460af98fa3858811eb41970ea93cf589",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_w3_execution01",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_w3_check_2026-10-16.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_w3_execution01"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-16_attempt2_C5_w3_execution01",
  "time_utc": "2026-10-16T16:56:20.844308+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_w3_execution01\\actual_writer_stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_w3_execution01\\actual_writer_stdout.log",
      "sha256": "c20a26d82d8e10a2e01a4b6dc19990659cd661b8168f15de82adc7072309eafd",
      "bytes": 325
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_w3_execution01\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_w3_execution01\\stdout.log",
      "sha256": "02617a6396618f1f86b97e99655257abbfd3042bbd56b414e5efa2e8f24ac75f",
      "bytes": 121
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_w3_execution01\\W3_check_result.json",
      "sha256": "1f4e8ae48374b64bda4b0c5b31db291e23fa82b7d08acbdb418d3adcc1af3940",
      "bytes": 30413
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-16_attempt2_C5_rrs_execution01",
  "time_utc": "2026-10-16T16:56:21.033802+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_rrs_check_2026-10-16.py",
  "code_sha256": "e9ba0e66c7900c36ee70cef88ec9701cdb62232db1e1863173848e784c96fa70",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_rrs_execution01",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_rrs_check_2026-10-16.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_rrs_execution01"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-16_attempt2_C5_rrs_execution01",
  "time_utc": "2026-10-16T16:56:22.326877+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_rrs_execution01\\RRS_result.json",
      "sha256": "7f83ea58720d7bb839ca1a8739b5b1bbc38d6f37b2fddbe7475522e98f1b195b",
      "bytes": 1103
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_rrs_execution01\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_rrs_execution01\\stdout.log",
      "sha256": "2adbbc7622c6de31d196e1a45700c10d806bbc2b87a7131bd0352ecc45a5a3c4",
      "bytes": 66
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-16_attempt2_C5_a2_execution01",
  "time_utc": "2026-10-16T16:56:22.551278+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
  "code_sha256": "b216d013e48a1e800419630b2c6d6e4b27d612fd14d8303ddb04db0898f46a29",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a2_execution01",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_synthetic_prevalidation_2026-10-15.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a2_execution01"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-16_attempt2_C5_a2_execution01",
  "time_utc": "2026-10-16T16:56:26.419321+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a2_execution01\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a2_execution01\\stdout.log",
      "sha256": "69804dbc8499fd2b8ca91e3125c7937013487f8dfe0846639f6d882a3ba8e373",
      "bytes": 206
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a2_execution01\\synthetic_result.json",
      "sha256": "633d671927576bfd03bcdd1cc1d11493096e2a918f0e094394c9eb7b59e61005",
      "bytes": 381794
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-16_attempt2_C3_execution02",
  "time_utc": "2026-10-16T16:56:40.871868+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_literal_listing_2026-10-16.py",
  "code_sha256": "83450a131cc9a264ddc010720dd186fd83dba5d16cdc7198b8df464251b046d6",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution02",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_literal_listing_2026-10-16.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution02"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-16_attempt2_C3_execution02",
  "time_utc": "2026-10-16T16:56:42.896398+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution02\\C3_literal_listing.csv",
      "sha256": "a15db5c42c247041e8581a043610d4dfb684718b9c2bca96a302ff0a808b1c65",
      "bytes": 81324
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution02\\C3_literal_listing.json",
      "sha256": "5c18b221a7832d1a6c3eee8d3069e35edb9b64bd7c3080db992ddd4ac8b57851",
      "bytes": 162387
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution02\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution02\\stdout.log",
      "sha256": "f1754faeecffcf6c4c0dfc3a93e4f9ac6f7b1d99056240a329221eec343b4ff5",
      "bytes": 11239
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_START",
  "execution_id": "2026-10-16_attempt2_C3_execution03",
  "time_utc": "2026-10-16T16:58:43.658012+00:00",
  "code_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_literal_listing_2026-10-16.py",
  "code_sha256": "4b1ab26e5b6e31542a90ff86ce0ee1940dcfdd67fe957d58193a5499a439d38a",
  "wrapper_path": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_logged_preflight_2026-10-15.py",
  "wrapper_sha256": "329cedc5ec7eedc12533c69f3f3c8afa6453d9619f5921ffbc38e80d97364617",
  "directory": "G:\\PycharmProjects\\pkp-worktree",
  "output_root": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution03",
  "command": [
    "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "-B",
    "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_rp1-r3_attempt2_literal_listing_2026-10-16.py",
    "G:\\PycharmProjects\\pkp-worktree",
    "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution03"
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "inputs_scope": "Pinned historical synthetic deliveries and gate source only; exact hashes recorded by comparator",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-16_attempt2_C3_execution03",
  "time_utc": "2026-10-16T16:58:50.263816+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution03\\C3_literal_listing.csv",
      "sha256": "fad840c4cd83faefd62bcc0ee5f7df07c6cc772894fca9c608e84c0e08d28089",
      "bytes": 81822
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution03\\C3_literal_listing.json",
      "sha256": "b9b05d86cdcc41ee82aed7e88214c817fca8eee75c23eaedaf230dce7313c46b",
      "bytes": 163130
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution03\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C3_execution03\\stdout.log",
      "sha256": "3f32bd6afa8e10597c5324d81333346fe55963922e6e19d2e1e0a5ee90bec524",
      "bytes": 11596
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "OUTSIDE_W3_END",
  "execution_id": "2026-10-16_attempt2_C5_a1_execution01",
  "time_utc": "2026-10-16T17:11:56.733297+00:00",
  "returncode": 0,
  "retained_outputs": [
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a1_execution01\\comparison_result.json",
      "sha256": "e17b901ecfcf36fad46179f33c0f6d0caa5172e43b2e8107b300e707b3278385",
      "bytes": 135353
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a1_execution01\\executed_source_excerpts.txt",
      "sha256": "299f83d5cc622a85708eb7f4c3d30f3a04df121921ef97d0ab1426196ed43115",
      "bytes": 1634
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a1_execution01\\stderr.log",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "path": "C:\\Users\\Neo\\Downloads\\rp1r3_preflight\\2026-10-16_attempt2_C5_a1_execution01\\stdout.log",
      "sha256": "33c969c955f1a0a25223d268dcac63a42f7f5f5b963d07c533b4c7a6c5e0f867",
      "bytes": 216
    }
  ],
  "output_disposition": "RETAINED_OUTSIDE_EVERY_DELIVERABLE_AND_STORE",
  "actual_optimizer_calls": 0,
  "store_access": false,
  "real_data_access": false
}
```

```json
{
  "event": "D20_ATTEMPT2_HOLD_POINT_READY_NO_LAUNCH",
  "created_utc": "2026-10-16T17:14:00.317770+00:00",
  "packager_code_sha256": "9e30b78525ff90124ef97d7b91bc09fd972118b6382972ab105c7b44c7a1eca1",
  "authority_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_2026-10-16.md",
  "authority_sha256": "778d8aff874991591cf45ae37e4fc0c698fb066304e16b6503e29868f693eff2",
  "decision": "B",
  "harness_sha256": "9ff48dbe6a5fdb6e4ae9d1952f1f7ecaba553eb84ef4e2a60de0be8258e8f96e",
  "writer_sha256": "822560025b80920431998005b647076348f4e3026546e42a852718ea1f082891",
  "source_proof": {
    "harness_function_segments_unchanged": 108,
    "main_unchanged": true,
    "run_real_scenario_unchanged": true,
    "all_other_harness_globals_unchanged": true,
    "writer_changed_functions": [
      "literal_constants",
      "main"
    ],
    "ledger_unchanged_sha256": "266a4f7bcf5cd5a18c91f68c7857ad587a6ee051c5a1a87454348e1056770bbc",
    "expectations_and_declarations_unchanged": true,
    "unchanged_gate_tests_launcher": {
      "p_konum_plus/calibration/f3_rp1-r3_gate_tools_2026-10-15.py": "1666abcf25d54bbc0b2ea3f404e286801149c3b7fb223eb83a49c1a54a75c045",
      "p_konum_plus/calibration/f3_rp1-r3_technical_tests_2026-10-15.py": "9d68989488657a8dc8f1bc3ce119ea1232415971043d0f9de799a4a014df9879",
      "p_konum_plus/calibration/f3_rp1-r3_launch_attempt_2026-10-15.py": "e55b16569b2f1729597f95cf8d0849f08d6ce0da44f930cf5f5b568968112496"
    },
    "parent_chain_unchanged": true,
    "C2_D19_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md",
    "C2_D19_observed_sha256": "10b3543344bd9ebf9df3319cfdc0d3540888328fde8bf4e5d6e05764bb675b1a"
  },
  "C3_counts": {
    "NEW": 39,
    "PIN": 23,
    "HISTPATH": 43,
    "TEXT": 73
  },
  "C3_real_input_hashes_NOT_OBSERVED": [
    "p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv",
    "p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv"
  ],
  "C3_TEXT_review_count": 15,
  "C5_all_passed": true,
  "active_W3_record_created": false,
  "harness_launched": false,
  "active_attempt_store_created": false,
  "actual_optimizer_calls": 0,
  "full_launch_authorized": false,
  "commit": false,
  "push": false,
  "instruction": "Stop here; require separate PI approval naming this harness and all changed-file hashes. Any byte change requires a new hold point."
}
```
