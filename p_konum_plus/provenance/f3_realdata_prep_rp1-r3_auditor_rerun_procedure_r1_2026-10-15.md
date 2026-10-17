# rp1-r3 independent auditor rerun procedure r1

Use a disposable copy of the complete delivered package. Keep the executor workspace, historical packages and all real F1/SSA files outside the auditor run. This procedure performs no audit and closes no finding.

Before execution, create a kept-aside directory outside the disposable run root. Record its absolute path. Make a recursive preservation inventory with original relative path, byte count and SHA256 for every file below the synthetic fixture tree, the attempt store and every listed output and sidecar. Copy these files to the kept-aside directory and verify each copy against that inventory before removing anything from the disposable run root. Also preserve every rp1-r3 runtime file in the final transmission/output audit not already listed below. Preserve the delivered attempt log and its sidecar; place byte-identical copies in the kept-aside directory, and leave a working copy for the auditor's new appended execution entries.

The following paths are source-derived for attempt 1, launch 1. Preserve each existing path and its `.sha256` sidecar. Entries reserved but never created require no fabricated file.

- `p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1-r3_2026-10-15.md`
- `p_konum_plus/calibration/f3_step2_handoff_family_telemetry_rp1-r3_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_handoff_timings_rp1-r3_2026-10-15.csv`
- `p_konum_plus/calibration/f3_step2_residual_series_rp1-r3_2026-10-15.json`
- `p_konum_plus/calibration/f3_step2_results_rp1-r3_2026-10-15.json`
- `p_konum_plus/calibration/f3_step2_rp1-r3_attempt1_launch1_stderr_2026-10-15.log`
- `p_konum_plus/calibration/f3_step2_rp1-r3_attempt1_launch1_stdout_2026-10-15.log`
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
- `p_konum_plus/provenance/f3_realdata_prep_rp1-r3_runtime_fixture_custody_attempt1_launch1_2026-10-15.csv`
- `p_konum_plus/provenance/f3_realdata_prep_rp1-r3_size_estimate_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_end_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_pid_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_start_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_w3_writer_2026-10-15.json`
- `p_konum_plus/provenance/f3_step2_rp1-r3_preexecution_custody_attempt1_launch1_2026-10-15.md`

Regenerated synthetic fixture tree: `p_konum_plus/calibration/f3_step2_rp1-r3_f1_synth_fixtures_2026-10-15`. Preserve **every descendant**, including `q3_complete`, all negative fixture directories and checksum subdirectories. The unchanged harness regenerates this tree. Preserve and remove it only in the disposable copy after verified custody.

Attempt store: `p_konum_plus/calibration/.rp1-r3_attempt1_restart_store_2026-10-15`. Preserve its complete recursive contents and manifest in the kept-aside directory; the auditor copy starts with an absent or empty store. Never import any executor store unit into it.

After custody preservation, remove only the disposable copy's W-3 file, launch writer/start/pid/end records and their sidecars, stdout/stderr pairs and sidecars, and generated synthetic tree so exclusive-create checks can pass. Generated output files above may be removed after preservation or overwritten by the unchanged harness; keep their original verified copies. Source files, incoming prompts, dependency pins, baseline results and frozen generator/manifest stay byte-identical.

Match the binding Python/NumPy/SciPy/platform and thread settings recorded by the executor W-3 and results. Set F3_REPO_ROOT to this disposable root, F3_RP1R3_LAUNCH=1, PYTHONDONTWRITEBYTECODE=1 and OMP_NUM_THREADS/OPENBLAS_NUM_THREADS/MKL_NUM_THREADS=1. Run `python -B p_konum_plus/calibration/f3_rp1-r3_launch_attempt_2026-10-15.py`. Log every invocation. The launcher writes the new external W-3 before starting the unchanged harness; its fixed D-14 verification must succeed. Keep every record and log pair. Plan an uninterrupted run using the instruction's estimate; measured time is recorded by the actual process.

The independent auditor verifies all mandatory inherited and RRS tests, the Q4/Q5/Q6 target assertions, the byte-identical run_real_scenario segment, S objects and canonical RUN1/RUN2 equality, complete leaf-level E/U comparison, Q10 fresh/replay accounting, input-open audit and every checksum. Any S difference fails. Do not close any finding without the independent audit or an explicit named PI decision. Do not read, hash or import real SSA/F1 files or real eligible/hash tables. Prior packages remain untouched.
