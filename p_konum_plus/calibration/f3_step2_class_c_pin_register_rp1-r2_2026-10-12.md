# rp1-r2 final implementation pin register

NON-NORMATIVE. Child of p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md (SHA256 4d5de5a776e7cd4a336b0dfc5f50aae378bdf6c3a780ff887a2a414389a5fe63). No frozen scientific rule changes.

Harness SHA256: 4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d

rp1-r2_status: PARTIAL_PENDING_PI

Key namespace and optimizer/store accounting, transferred from final results:

```json
{
  "namespace": [
    {
      "key_families": [
        "nrgates_all",
        "onestart",
        "realscen",
        "splmode",
        "unittests_all"
      ],
      "n_keys": 11431,
      "scope": "(base)"
    },
    {
      "key_families": [
        "nrgates_all",
        "realscen",
        "unittests_all"
      ],
      "n_keys": 3,
      "scope": "TEST_ONLY_Q8__"
    },
    {
      "key_families": [
        "splmode"
      ],
      "n_keys": 438,
      "scope": "excpass1__"
    },
    {
      "key_families": [
        "splmode"
      ],
      "n_keys": 438,
      "scope": "excpass2__"
    },
    {
      "key_families": [
        "onestart",
        "splmode"
      ],
      "n_keys": 54714,
      "scope": "f1handoff__"
    },
    {
      "key_families": [
        "splmode"
      ],
      "n_keys": 146,
      "scope": "tstoreread_cold__"
    },
    {
      "key_families": [
        "splmode"
      ],
      "n_keys": 146,
      "scope": "tstoreread_warm__"
    }
  ],
  "process": {
    "attempt_log_path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md",
    "attempt_number": 2,
    "command_line": "G:\\PycharmProjects\\pkp-worktree\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
    "end": "2026-10-12T03:09:23.676738",
    "executor_models": "Codex / GPT-6; current pkp-worktree executor attribution",
    "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "launch_number": 1,
    "launch_stderr_path": "p_konum_plus/calibration/f3_step2_rp1-r2_attempt2_launch1_stderr_2026-10-10.log",
    "launch_stdout_path": "p_konum_plus/calibration/f3_step2_rp1-r2_attempt2_launch1_stdout_2026-10-10.log",
    "percall_telemetry_path": "p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r2_2026-10-10.csv",
    "pid": 17884,
    "restart_layer_active": true,
    "spline_telemetry_call_total": 22217,
    "spline_telemetry_calls_by_phase": {
      "f1_handoff": 9223,
      "nr_gates": 60,
      "run1": 5256,
      "run2": 5256,
      "t_store_read_accounting": 820,
      "unit_tests": 1602
    },
    "spline_telemetry_calls_by_phase_pid": [
      {
        "count": 9223,
        "phase": "f1_handoff",
        "writer_pid": 17884
      },
      {
        "count": 60,
        "phase": "nr_gates",
        "writer_pid": 17884
      },
      {
        "count": 5256,
        "phase": "run1",
        "writer_pid": 17884
      },
      {
        "count": 5256,
        "phase": "run2",
        "writer_pid": 17884
      },
      {
        "count": 820,
        "phase": "t_store_read_accounting",
        "writer_pid": 17884
      },
      {
        "count": 1602,
        "phase": "unit_tests",
        "writer_pid": 17884
      }
    ],
    "start": "2026-10-11T17:12:37.378472",
    "store_manifest_path": "p_konum_plus/calibration/f3_step2_rp1-r2_restart_store_manifest_2026-10-10.csv",
    "store_manifest_sha256": "f6666cf24343e383a3c0a3ebbe0588a2db0575c08d20ed0156385cfe26b10bca",
    "store_rows": 67316,
    "supersedes_harness_sha256": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
    "supersedes_note_path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r2_attempt_log_2026-10-10.md",
    "units_computed_this_process": {
      "nr_gates": 1,
      "residual_export": 1,
      "run1": 2,
      "run2": 2,
      "unit_tests": 1
    },
    "units_read_from_store": {
      "nr_gates": 0,
      "residual_export": 0,
      "run1": 0,
      "run2": 0,
      "unit_tests": 0
    }
  },
  "handoff": {
    "accounting": {
      "expected_optimizer_rows": 47706,
      "expected_spline_optimizer_rows": 9223,
      "observed_family_units": 47706,
      "observed_optimizer_rows": 47706,
      "observed_spline_optimizer_rows": 9223,
      "pass_": true,
      "spline_rows_reconciled": true,
      "stored_family_units": 47706,
      "stored_spline_units": 7008
    },
    "family": {
      "path": "p_konum_plus/calibration/f3_step2_handoff_family_telemetry_rp1-r2_2026-10-10.csv",
      "rows": 47706,
      "sha256": "4fe656ccbada9b2b92618d35a384d158edc0fd54ff9d65be3238b5208157b26e"
    },
    "timing": {
      "path": "p_konum_plus/calibration/f3_step2_handoff_timings_rp1-r2_2026-10-10.csv",
      "rows": 6,
      "sha256": "587e9239ebc35d78edbd90907e8b887ed9445e366ba685d4388006bb2f81f79c"
    }
  },
  "inadmissible": {
    "family_starts": 13026,
    "spline_modes": 105
  }
}
```

Q1-Q11 observed checks:

```json
{
  "Q1": {
    "cases": [
      {
        "expected": true,
        "got": true,
        "name": "complete_intake",
        "ok": true
      },
      {
        "expected": "real_x",
        "got": "real_x",
        "name": "real_x",
        "ok": true
      },
      {
        "expected": "real_x[F,0]",
        "got": "real_x[F,0]",
        "name": "real_x[F,0]",
        "ok": true
      },
      {
        "expected": "real_mask_ids",
        "got": "real_mask_ids",
        "name": "real_mask_ids",
        "ok": true
      },
      {
        "expected": "real_mask_ids[F,0]",
        "got": "real_mask_ids[F,0]",
        "name": "real_mask_ids[F,0]",
        "ok": true
      },
      {
        "expected": 0,
        "got": 0,
        "name": "no_optimizer_reached",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q10": {
    "cases": [
      {
        "expected": true,
        "got": true,
        "name": "family_units_reconciled",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "spline_rows_reconciled",
        "ok": true
      },
      {
        "expected": false,
        "got": false,
        "name": "missing_optimizer_row_rejected",
        "ok": true
      },
      {
        "expected": 6,
        "got": 6,
        "name": "trajectory_timings",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q11": {
    "cases": [
      {
        "expected": true,
        "got": true,
        "name": "same_launch",
        "ok": true
      },
      {
        "expected": false,
        "got": false,
        "name": "different_launch",
        "ok": true
      },
      {
        "expected": false,
        "got": false,
        "name": "missing_launch",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q2": {
    "cases": [
      {
        "expected": 1,
        "got": 1,
        "name": "one_literal",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "duplicate_rejected",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "actual_equals_dry",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q3": {
    "cases": [
      {
        "expected": "PASS",
        "got": "PASS",
        "name": "complete",
        "ok": true
      },
      {
        "expected": "F1_REPRO_GATE_MISSING_FILE",
        "got": "F1_REPRO_GATE_MISSING_FILE",
        "name": "missing",
        "ok": true
      },
      {
        "expected": "F1_REPRO_GATE_EXTRA_FILE",
        "got": "F1_REPRO_GATE_EXTRA_FILE",
        "name": "extra",
        "ok": true
      },
      {
        "expected": "F1_REPRO_GATE_HASH_MISMATCH",
        "got": "F1_REPRO_GATE_HASH_MISMATCH",
        "name": "changed_raw",
        "ok": true
      },
      {
        "expected": "F1_REPRO_GATE_MANIFEST_HASH_MISMATCH",
        "got": "F1_REPRO_GATE_MANIFEST_HASH_MISMATCH",
        "name": "manifest_hash",
        "ok": true
      },
      {
        "expected": "F1_REPRO_GATE_FIELD_MISMATCH",
        "got": "F1_REPRO_GATE_FIELD_MISMATCH",
        "name": "field",
        "ok": true
      },
      {
        "expected": "F1_REPRO_GATE_ROW_COUNT",
        "got": "F1_REPRO_GATE_ROW_COUNT",
        "name": "row",
        "ok": true
      },
      {
        "expected": "F1_REPRO_GATE_ORDERING",
        "got": "F1_REPRO_GATE_ORDERING",
        "name": "ordering",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q4": {
    "cases": [
      {
        "expected": 0,
        "got": 0,
        "name": "no_constant_ok",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "constant_rejected",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q5": {
    "cases": [
      {
        "expected": true,
        "got": true,
        "name": "count_transition",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "wrong_equal_count",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "addition_in_both",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "unequal_equal",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "deep_not_hidden",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "absent_in_both",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q6": {
    "cases": [
      {
        "expected": true,
        "got": true,
        "name": "path_normalized",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "changed_raise_rejected",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q7": {
    "cases": [
      {
        "expected": true,
        "got": true,
        "name": "resumed_cold",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "stored_payload_matches",
        "ok": true
      },
      {
        "expected": false,
        "got": false,
        "name": "corrupt_payload_rejected",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q8": {
    "cases": [
      {
        "expected": "replay",
        "got": "replay",
        "name": "nrgates_all",
        "ok": true
      },
      {
        "expected": "scientific_value",
        "got": "scientific_value",
        "name": "nrgates_all_value",
        "ok": true
      },
      {
        "expected": "replay",
        "got": "replay",
        "name": "unittests_all",
        "ok": true
      },
      {
        "expected": "scientific_value",
        "got": "scientific_value",
        "name": "unittests_all_value",
        "ok": true
      },
      {
        "expected": "replay",
        "got": "replay",
        "name": "realscen",
        "ok": true
      },
      {
        "expected": "scientific_value",
        "got": "scientific_value",
        "name": "realscen_value",
        "ok": true
      },
      {
        "expected": false,
        "got": false,
        "name": "fresh_is_not_replay",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  },
  "Q9": {
    "cases": [
      {
        "expected": "onestart",
        "got": "onestart",
        "name": "onestart_scope",
        "ok": true
      },
      {
        "expected": "splmode",
        "got": "splmode",
        "name": "splmode_scope",
        "ok": true
      },
      {
        "expected": true,
        "got": true,
        "name": "phase",
        "ok": true
      },
      {
        "expected": false,
        "got": false,
        "name": "wrong_phase_rejected",
        "ok": true
      }
    ],
    "pass_": true,
    "ran": true
  }
}
```
