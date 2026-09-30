# p_konum_plus - F3 Spline Solver Qualification r2 - Pre-Execution Custody Record

```text
artifact_role = pre-execution custody record (Output F)
status        = NON-NORMATIVE
date          = 2026-09-03

r2_manifest_path =
p_konum_plus/calibration/f3_spline_solver_qualification_manifest_r2_2026-09-03.csv

r2_manifest_sha256 =
e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32

r2_harness_path =
p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py

r2_harness_sha256 =
b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d

r2_manifest_schema_valid = true
r2_manifest_header_count = 38
r2_manifest_row_count = 30 (10 fixtures x 3 solver configurations)
exact_expansion_trigger_predeclared = true (manifest field expansion_trigger, SOLVER-B rows)
stage3_nnls_kkt_required = false (predeclared; code-true reproduction of the defined SOLVER-B configuration)

declaration =
this record is written by the r2 harness AFTER manifest write,
schema validation and SHA256 computation, and BEFORE the first synthetic
solver case is executed. No qualification result may edit the manifest.

original_run_status = HISTORICAL_SUPERSEDED_FOR_EXTERNAL_ACCEPTANCE_ONLY
original_manifest_sha256 =
522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883
original_harness_sha256 =
ecda07d0fee36d8988c82c31aeb8e231b812e7a4df400af9c6a80676e4cf5917

SSA_access = false
P01_P02_real_fit = false
commit = false
```
