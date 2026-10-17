# Independent auditor rerun procedure r1

This delivery record applies to the completed attempt/launch identified in rerun_overwrite_inventory_r1.json. The older attempt-1 procedure is historical. It does not authorize an independent auditor to change the frozen source.

Create a disposable checkout of commit `25c7d51a0d14e8935f464a7a52d6a49ef4383e2b` and overlay the delivered paths after verifying the transmission list and all sidecars. Keep all real SSA/F1 inputs outside that root. The ZIP is a delivery overlay, not a substitute for the pinned parent checkout.

Before running, copy every existing listed file and its sidecar, the complete synthetic fixture tree (including all negative cases and checksum directories), every runtime artifact named by the transmission list, and every store descendant to a kept-aside directory outside the disposable root. Record relative path, size and SHA256 for each original and copy, and verify equality before any removal. Keep the executor workspace unchanged. Preserve the attempt log and leave a working copy for appended auditor entries.

After verified preservation, remove only disposable copies of exclusive-create custody/writer/start/pid/end records, launch stdout/stderr pairs and sidecars, and the regenerated synthetic fixture tree. Start with an absent or empty attempt store; preserve and remove any old disposable store first. Other generated outputs may be overwritten only after preservation. Preserve the runtime fixture custody record and sidecar as well. No delivered code, prompt, baseline or scientific generator is changed.

Match the Python, NumPy, SciPy, platform and thread settings in the delivered W-3/environment records. Record every invocation. Use the unchanged launcher; it creates the external W-3 and verifies D-14 before computation. In the disposable root set:

```powershell
$env:F3_REPO_ROOT = (Get-Location).Path
$env:F3_RP1R3_LAUNCH = "1"
$env:PYTHONDONTWRITEBYTECODE = "1"
$env:OMP_NUM_THREADS = "1"
$env:OPENBLAS_NUM_THREADS = "1"
$env:MKL_NUM_THREADS = "1"
python -B p_konum_plus/calibration/f3_rp1-r3_launch_attempt_2026-10-15.py
```

All source-derived output/reserved paths follow. Preserve each sidecar too; reserved paths absent from the executor output are not fabricated.

- `p_konum_plus/calibration/.rp1-r3_attempt2_restart_store_2026-10-15`
- `p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py`
- `p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py.sha256`
- `p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1-r3_2026-10-15.md`
- `p_konum_plus/calibration/f3_step2_handoff_family_telemetry_rp1-r3_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_handoff_family_telemetry_rp1-r3_2026-10-15.csv.sha256`
- `p_konum_plus/calibration/f3_step2_handoff_timings_rp1-r3_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_handoff_timings_rp1-r3_2026-10-15.csv.sha256`
- `p_konum_plus/calibration/f3_step2_residual_series_rp1-r3_2026-10-15.json`
- `p_konum_plus/calibration/f3_step2_results_rp1-r3_2026-10-15.json`
- `p_konum_plus/calibration/f3_step2_rp1-r3_attempt2_launch1_stderr_2026-10-15.log`
- `p_konum_plus/calibration/f3_step2_rp1-r3_attempt2_launch1_stderr_2026-10-15.log.sha256`
- `p_konum_plus/calibration/f3_step2_rp1-r3_attempt2_launch1_stdout_2026-10-15.log`
- `p_konum_plus/calibration/f3_step2_rp1-r3_attempt2_launch1_stdout_2026-10-15.log.sha256`
- `p_konum_plus/calibration/f3_step2_rp1-r3_expectations_2026-10-15.json`
- `p_konum_plus/calibration/f3_step2_rp1-r3_nonregression_vs_r4-1_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_rp1-r3_nonregression_vs_r4-2_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_rp1-r3_nonregression_vs_r4_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_rp1-r3_restart_store_manifest_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_rp1-r3_store_read_log_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r3_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_telemetry_rp1-r3_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_test_evidence_rp1-r3_2026-10-15.json`
- `p_konum_plus/provenance/f3_realdata_prep_rp1-r3_attempt_log_2026-10-15.md`
- `p_konum_plus/provenance/f3_realdata_prep_rp1-r3_runtime_fixture_custody_attempt2_launch1_2026-10-15.csv`
- `p_konum_plus/provenance/f3_realdata_prep_rp1-r3_runtime_fixture_custody_attempt2_launch1_2026-10-15.csv.sha256`
- `p_konum_plus/provenance/f3_realdata_prep_rp1-r3_size_estimate_2026-10-15.json`
- `p_konum_plus/provenance/f3_realdata_prep_rp1-r3_size_estimate_2026-10-15.json.sha256`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_w3_writer_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_w3_writer_2026-10-15.json.sha256`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_end_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_end_2026-10-15.json.sha256`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_pid_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_pid_2026-10-15.json.sha256`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_start_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_start_2026-10-15.json.sha256`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_w3_writer_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_w3_writer_2026-10-15.json.sha256`
- `p_konum_plus/provenance/f3_step2_rp1-r3_preexecution_custody_attempt2_launch1_2026-10-15.md`
- `p_konum_plus/provenance/f3_step2_rp1-r3_preexecution_custody_attempt2_launch1_2026-10-15.md.sha256`

The recursive fixture file list and hashes are in rerun_overwrite_inventory_r1.json. Preserve additional files discovered in the actual rerun and transmission inventory. Compare complete result leaves, tests, negative targets, S objects/stops/RUN hashes/residual, fresh/replay accounting and input-open audit; no real SSA/F1 path may be opened or hashed. Any S difference is a failure. This procedure closes no item.
