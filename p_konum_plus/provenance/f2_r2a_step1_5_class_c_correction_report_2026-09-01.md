# p_konum_plus — ART-F2 r2 -> r2a STEP-1.5 CLASS_C + Transcription Correction — Report

- **Artifact role:** STEP-1.5 execution report (narrow A0–A5 correction pass only). NOT a methodology review; no new PI scientific decision; no PI re-ratification required.
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-09-01
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`

---

## 1. Repository/precheck result — PASS

Root `G:/PycharmProjects/pkp-worktree` ✓, branch `p_konum_plus` ✓, HEAD = expected `3e4daf47018f124e29717263e4e45fe90c8e52b8` ✓. Zero unexpected tracked modifications; only the twelve known F2-era untracked artifacts present at precheck (list below). Both STEP-1.5 target output paths were verified absent before creation — no overwrite occurred. Nothing deleted/reset/stashed/checked out.

Untracked list before STEP-1.5 outputs:

```text
?? p_konum_plus/calibration/f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md
?? p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv
?? p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md
?? p_konum_plus/calibration/f2_generator_specification_record_r2_2026-08-31.md
?? p_konum_plus/provenance/f2_d09_exact_enumeration_packet_2026-08-30.md
?? p_konum_plus/provenance/f2_d09_packet_endoftask_report_2026-08-30.md
?? p_konum_plus/provenance/f2_owner_decision_packet_report_2026-08-29.md
?? p_konum_plus/provenance/f2_r2_correction_ratification_report_2026-08-31.md
?? p_konum_plus/provenance/f2_reconciliation_source_check_report_2026-08-29.md
?? p_konum_plus/provenance/f2_worksheet_updated3_verification_report_2026-08-29.md
?? p_konum_plus/provenance/nonnormative/claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md
?? p_konum_plus/provenance/nonnormative/ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
```

## 2. Governing-hash result — all 10 exact

| document | SHA256 |
|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` |
| ART-F2 r2 (parent) | `d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4` |
| ART-F2 r1 (lineage) | `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7` |
| PI ratification-ready worksheet FINAL_v2 (lineage) | `803e9f30fa84b6c02c34a517525e6c246edf7be4db684e72a2ea8c970f9b38f5` |
| D-F2-09 exact packet (lineage) | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` |
| D-F2-09 start-grid manifest (lineage) | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` |
| ART-F0 | `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` |
| ART-F1 r4a | `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0` |
| F1 eligible manifest / input hash table | `8a6034eb…` / `aa86f1ea…` |

No mismatch; no STOP.

## 3. r2 parent unchanged confirmation + SHA256

Re-hashed after writing r2a: `d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4` — **identical** to the pre-task value. r2 was not overwritten.

## 4. r2a path + SHA256

```text
path   = p_konum_plus/calibration/f2_generator_specification_record_r2a_2026-09-01.md
SHA256 = 2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2
```

## 5. A0 — D-F2-08 objective transcription summary

Restored (not newly decided): `x` = frozen ART-F1 z-normalized trajectory; `ghat(theta) = z_ddof0(g(u_grid;theta))`; `T=146`; `L(theta) = sum_j [x_j - ghat_j(theta)]^2`; `argmin_theta L(theta)`, unweighted, in frozen z-space. Explanatory identity retained: since both `x` and `ghat` are population-z-standardized, `L(theta) = 2T(1-rho(x,ghat))`, so unweighted LS ≡ Pearson-correlation maximization — explanatory only, the LS formula remains the implementation objective. No robust/weighted/cosine loss substituted.

## 6. A1 — corrected optimizer-feasibility semantics

`constr_viol_tol` removed from the `trust-constr` solver-option list (it is not a valid option for that method); the primary option set is now exactly `jac='2-point'`, `hess=BFGS()`, `gtol=1e-10`, `xtol=1e-12`, `barrier_tol=1e-10`, `maxiter=500`; fallback SLSQP unchanged (`ftol=1e-12`, `maxiter=500`). In its place: an explicit **post-return** `feasibility_acceptance_tol = 1e-8` (`CLASS_C_POST_RETURN_ACCEPTANCE_TOLERANCE`) with generic box-violation `V_box` and exact per-family violation formulas `V_P01`, `V_P02` (P-02's uses `s_side_min(beta)`, the nonlinear Kural-T bound). `endpoint_numerically_feasible = finite(theta) AND V_family(theta) <= 1e-8`. Explicitly not a morphology threshold and does not authorize clipping/projection; Kural T/S remain the separate scientific admissibility check.

## 7. A2 — exact multistart aggregation summary

Per start: run primary optimizer → apply existing per-start fallback only on its existing pure-numerical-error trigger → one terminal endpoint → evaluate under the full hard-failure/admissibility contract (Kural S applies only at the terminal endpoint, not intermediate iterates). `eligible_endpoint` requires numerical feasibility (§A1) + finite objective/prediction + not `ZERO_VARIANCE_FIT` + Kural-T pass + Kural-S pass + no other hard-failure predicate. `E` = set of eligible endpoints across the full deterministic bank (731+1 / 261+1 per family, per r2 D-F2-09.10). Nonempty `E` → `argmin_{theta in E} L(theta)`, ties via the existing D-F2-09.9 comparator + lexicographic tiebreak. Empty `E` → `family_fit = FAMILY_FIT_FAILURE`, `family_failure_summary = NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART` — explicitly a **summary label**, not a new hard-failure predicate; every start-level code is still retained. The D-F2-09 start bank itself is untouched.

## 8. A3 — exact `epsilon_model` definition

```text
epsilon_model = 1e-12   (CLASS_C_NUMERICAL_GUARD)
rule: nonfinite g_stable -> NONFINITE_FIT
      else sigma_g = std(g_stable, ddof=0)
      sigma_g <= 1e-12 -> ZERO_VARIANCE_FIT (no z-normalization)
      else               -> ghat = (g_stable - mean)/sigma_g
```

Rationale: `g_stable` is max-normalized to 1 by construction; `1e-12 ≈ 4.5e3 × machine_epsilon` on the unit scale — a pure floating-point dynamic-range guard, not a morphology/adequacy threshold, and explicitly not derived from raw-curve near-flatness or any Kural-S pass/fail analysis (small pre-z amplitude can still encode a distinct standardized shape). Must not be tuned from STEP-2 fixture outcomes; any future change is a separate numerical-conditioning review.

## 9. A4 — reserved hard-failure-code status

```text
BOUNDARY_PATHOLOGY_status      = RESERVED_NOT_EMITTED_IN_STEP2
IDENTIFIABILITY_FAILURE_status = RESERVED_NOT_EMITTED_IN_STEP2
WARN_BOUNDARY_status           = RESERVED_NOT_EMITTED_IN_STEP2_UNTIL_TRIGGER_PINNED
WARN_IDENTIFIABILITY_status    = RESERVED_NOT_EMITTED_IN_STEP2_UNTIL_TRIGGER_PINNED
```

STEP 2 may record raw threshold-free diagnostics (constraint slack, optimizer-reported violation, termination status) but may not introduce any new boundary/identifiability cutoff; these diagnostics never fail an otherwise-admissible endpoint. All other hard-failure predicates unchanged. No new owner-level threshold was invented.

## 10. A5 — split pin records + display precedence

`P-CMN.7` (mixed-status) replaced by `P-CMN.7a` (`failure taxonomy + scientific admissibility semantics`, `PI_RATIFIED`) and `P-CMN.7b` (`primary hard-failure display precedence`, `CLASS_C_IMPLEMENTATION_PIN`). Fixed 10-code display ordering recorded (NONFINITE_INPUT → INVALID_INITIALIZATION → NONFINITE_PARAMETER → NONFINITE_FIT → ZERO_VARIANCE_FIT → MORPHOLOGY_INADMISSIBLE → OPTIMIZER_NONCONVERGENCE → OTHER_PREDECLARED_NUMERICAL_FAILURE → BOUNDARY_PATHOLOGY → IDENTIFIABILITY_FAILURE); all applicable predicates still logged simultaneously; `precedence_changes_admissibility = false`. Full updated pin table (19 rows, every row single-valued) recorded in ART-F2 r2a §7.

## 11. Static/unit-level check results — all PASS

Executed model-only, hand-written/fabricated fixtures, no real trajectory data:

- `constr_viol_tol` confirmed absent from the trust-constr option text.
- Document-search confirmed D-F2-08 exact objective now present.
- `V_P01`: feasible interior `0.0`, feasible boundary `(0.5,0.5,4,4)` `0.0`, `c_r>c_d` violation `0.5`, out-of-box violation `1.0`.
- `V_P02`: feasible boundary at `s=s_side_min(beta)` `0.0`, feasible interior `0.0`, `s_l` below `s_side_min(beta)` violation `≈0.0171`, `beta` out of range violation `1.0`.
- `epsilon_model` rule: nonconstant vector → `OK` (`std≈0.334`); exactly-constant vector → `ZERO_VARIANCE_FIT`; near-constant vector (`std≈7.1e-15`) → `ZERO_VARIANCE_FIT`; vector with `NaN` → `NONFINITE_FIT`.
- Multistart aggregation: all-ineligible → `FAMILY_FIT_FAILURE`/`NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART`; one clear best selected correctly; tie resolved to lexicographically smallest tuple; lower-`L`-but-ineligible endpoint correctly excluded in favor of the eligible one.
- Pin-table schema check: every row in the updated table carries exactly one status value.

No fixture result was used to tune `epsilon_model`, `feasibility_acceptance_tol`, or any scientific parameter — constants were fixed before the checks ran. Forbidden actions (synthetic feasibility suite, real/subset SSA fit, P-01 vs P-02 comparison, recovery scores/rates, P-03 work, generator selection, F3) were **not** performed.

## 12. Exact files created

- `p_konum_plus/calibration/f2_generator_specification_record_r2a_2026-09-01.md`
- `p_konum_plus/provenance/f2_r2a_step1_5_class_c_correction_report_2026-09-01.md` (this file)

No other file touched; r2, r1, and all upstream artifacts re-verified byte-unchanged.

## 13. Provenance report path + SHA256

```text
path = p_konum_plus/provenance/f2_r2a_step1_5_class_c_correction_report_2026-09-01.md
```

(Its own SHA256 is reported in the end-of-task response, computed after this file is written — a file cannot contain its own hash. No sidecar created.)

## 14. Confirmation

```text
PI_re_ratification = false
F2_STEP_2 = false
F2_complete = false
F3_allowed = false
```

Also: no algorithm/CVI execution or outcome access, no legacy performance content access, no `results/` opened, no real SSA fit of any kind, no P-03/P-04/P-05 touched, no generator selected.

## 15. Final `git status --short --untracked-files=all`

Recorded in the end-of-task response after this report is written (two new untracked paths added: ART-F2 r2a and this report).

## 16. Verdict

```text
ART_F2_R2A_STEP1_5_READY_FOR_INDEPENDENT_AUDIT
```

End state: `ART_F2_r2_unchanged = true`, `ART_F2_r2a_created = true`, `A0_closed .. A5_closed = true`, `PI_re_ratification = false`, `F2_STEP_1_complete = true`, `F2_STEP_1_5_complete = true`, `F2_STEP_2 = false`, `F2_complete = false`, `F3_allowed = false`. Next action: independent narrow audit of ART-F2 r2a.
