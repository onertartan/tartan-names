# p_konum_plus — F3 Spline Solver Qualification r2 — Artifact Inventory

```text
artifact_role = custody/provenance inventory for the r2 external audit bundle
                (Output E of the schema-safe rerun task)
status        = NON-NORMATIVE
date          = 2026-09-03
```

## r2 audit bundle (new this task)

| # | role | path | SHA256 |
|---|---|---|---|
| A | r2 schema-safe qualification manifest (38 columns × 30 rows; written, schema-validated and hashed before any solve) | `p_konum_plus/calibration/f3_spline_solver_qualification_manifest_r2_2026-09-03.csv` | `e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32` |
| B | r2 harness actually executed (enforces the 8-step write/validate/hash/custody/execute order mechanically) | `p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py` | `b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d` |
| C | r2 machine-readable case-level telemetry (30 rows = 10 fixtures × 3 configurations; each row carries manifest+harness SHA256) | `p_konum_plus/calibration/f3_spline_solver_qualification_results_r2_2026-09-03.csv` | `ffda04b01abb1dd5399e7fb6434c006616723bf6ba7d95bfc697baeb6dd40484` |
| D | r2 qualification report | `p_konum_plus/provenance/f3_spline_solver_qualification_report_r2_2026-09-03.md` | (hashed in the end-of-task response; written after this inventory's sibling artifacts) |
| E | pre-execution custody record (written by the harness AFTER manifest hash, BEFORE first solve; contains manifest+harness SHA256) | `p_konum_plus/provenance/f3_spline_solver_qualification_preexecution_custody_r2_2026-09-03.md` | (hashed in the end-of-task response) |

All r2 artifacts are untracked; nothing committed.

## Original run — historical provenance (byte-unchanged, re-verified this task)

| role | path | SHA256 | status |
|---|---|---|---|
| original manifest (schema defect: 23 headers vs 24 parsed fields) | `p_konum_plus/calibration/f3_spline_solver_qualification_manifest_2026-09-02.csv` | `522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883` | HISTORICAL_SUPERSEDED_FOR_EXTERNAL_ACCEPTANCE_ONLY |
| original executed harness | `p_konum_plus/calibration/f3_spline_solver_qualification_harness_2026-09-02.py` | `ecda07d0fee36d8988c82c31aeb8e231b812e7a4df400af9c6a80676e4cf5917` | historical provenance |
| original result/provenance record | `p_konum_plus/provenance/f3_step1_r1_corrected_ratification_candidate_2026-09-02.md` | `6e7b56348f9a1ffe144d776b48bc559baf2cbf71fb02c84ff37cba11203992c6` | historical provenance |
| original (r1-task) inventory | `p_konum_plus/provenance/f3_spline_solver_qualification_artifact_inventory_2026-09-03.md` | unchanged this task | historical provenance |

```text
scientific_result_reuse = forbidden as the accepted qualification basis
no result mixed across manifest hashes 522d3508… (original) and e71ce030… (r2)
external_independent_acceptance = PENDING
commit = false
```
