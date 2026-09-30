# p_konum_plus — F3 Spline Solver Qualification r2 — Report

```text
artifact_role = r2 qualification report (Output D of the schema-safe rerun task)
status        = NON-NORMATIVE
date          = 2026-09-03
governing     = v11 (d136502f…, v11_wins = true); F2 FINAL FREEZE r1 (ee2cb99d…);
                v6 prompt (418092db…); r2 schema-safe rerun prompt
```

## 1. Why this rerun exists

External independent audit findings `F3-SPLINE-QUAL-MANIFEST-01` (original CSV
manifest: 23 header columns vs 24 parsed row fields — unescaped comma inside
`reference_construction_rule`) and `F3-SPLINE-QUAL-PREDECL-02` (exact Boolean
`expansion_trigger` not itself a frozen manifest field). Gate-specific only;
no F2 reopening, no methodology review, no real SSA execution.

## 2. Original run — historical provenance

```text
original_manifest_sha256 =
522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883

original_run_retained_unchanged = true
  (re-verified this task: manifest 522d3508…, harness ecda07d0…,
   result record 6e7b5634… all byte-unchanged)

original_manifest_external_acceptance =
superseded_due_to_schema_and_predeclaration defects

original_run_status = HISTORICAL_SUPERSEDED_FOR_EXTERNAL_ACCEPTANCE_ONLY
scientific_result_reuse = forbidden as the accepted qualification basis
historical_provenance_retained = true
no result is mixed across the original and r2 manifest hashes
```

## 3. r2 manifest — schema-safe serialization

Written with Python `csv.writer` (QUOTE_MINIMAL, ascii encoding, LF line
terminator, fixed column order); no naive join. Reopened and validated with
`csv.reader` + `csv.DictReader` before any solve.

```text
r2_manifest_schema_valid = true
r2_manifest_header_count = 38
r2_manifest_row_count = 30 (10 fixtures x 3 solver configurations)
r2_manifest_all_row_field_counts = all 30 rows have exactly 38 fields
no unnamed/extra field; no duplicate header; no empty required value

exact_expansion_trigger_predeclared = true
  manifest field expansion_trigger (SOLVER-B rows), literally:
  "NOT accept(stage1_postpolish_endpoint), where accept(c) = all coordinates
   finite AND max(0, -min(A @ c)) <= 1e-8 AND
   NNLS_KKT_existence_residual(c, active_set_tol=1e-8) <= 1e-8"

stage3 fields predeclared literally (SOLVER-B rows):
  stage3_trigger = "NOT accept(stage2_postpolish_endpoint), where accept(c) = ..."
  stage3_acceptance_rule = "SLSQP success flag AND finite endpoint AND finite
    objective AND max_linear_constraint_violation <= 1e-8;
    stage3_nnls_kkt_required = false"
  stage3_fallback_x0 = zero vector of length 8 (feasible origin)

manifest_written_before_execution = true
  (harness enforces the 8-step order mechanically; the pre-execution custody
   record Output F was written after hashing and before the first solve)

manifest_sha256 =
e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32

harness_sha256 =
b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d
```

Fixture constructions (Q01–Q10), coefficients, noise seeds, masks, and
mode_idx rules match the original executed harness exactly; no transcription
mismatch found. The stage-3 KKT asymmetry (`stage3_nnls_kkt_required = false`)
was preserved as the predeclared code-true SOLVER-B configuration per the
prompt's §6.6; not redesigned.

## 4. Firewall confirmation

```text
SSA_access = false
P01_P02_real_fit = false
candidate_comparison = false
threshold_measurement = false
generator_selection = false
```

## 5. Results

```text
qualification_case_count = 10 (x 3 configurations = 30 telemetry rows)

reference_certification = PASS
  (10/10 dual-NNLS references certified: primal feasibility <= 1e-8 AND NNLS
   KKT-existence residual <= 1e-8 at |Ac| <= 1e-8 active rows; incl. Q10 with
   145 active rows, rank 7)

SOLVER_B_qualification = PASS (10/10; endpoints POLISH except Q04/Q09
  POLISH_EXPANDED; stage-3 fallback never invoked; worst
  error-to-tolerance ratio ~0.000; worst feasibility violation 5.83e-15)

SOLVER_A_qualification = PASS (10/10; SLSQP primary succeeded everywhere;
  fallback never invoked; worst ratio 0.002)

SOLVER_C_qualification = FAIL (objective accuracy failed in
  Q03 ratio 1.55 / Q04 ratio 693 / Q07 ratio 11.9 / Q09 ratio 291 /
  Q10 ratio 74.8 with violation 6.86e-11)

semantic_repeatability = PASS (every reference and every configuration
  solved twice in-process; exact repr equality of RSS in all 30 rows)

per-case machine-readable telemetry =
p_konum_plus/calibration/f3_spline_solver_qualification_results_r2_2026-09-03.csv
(30 rows; every row carries manifest_sha256 + harness_sha256)
```

Per-case acceptance used exactly the predeclared rules: mode_tol = 1e-12 +
1e-9·|RSS_ref|; objective accuracy |RSS_solver − RSS_ref| ≤ 0.1·mode_tol;
feasibility ≤ 1e-8; case pass = reference_certified AND both; suite pass =
ALL cases, no averaging. The r2 outcome pattern reproduces the historical run
(SOLVER-A/B pass, SOLVER-C fails the same five cases); this consistency is
informational only — the r2 run stands on its own manifest hash.

## 6. Claim boundary

```text
external_independent_acceptance = PENDING
```

This rerun is solver-infrastructure qualification under a corrected
provenance contract; it is NOT an independent audit of itself, NOT PI
ratification, NOT F3 adequacy execution. Determinism claim: same code, same
environment, same inputs, same thread-pinning contract — semantic
repeatability tested in-process; cross-process/cross-platform bitwise
reproducibility not claimed.
```
