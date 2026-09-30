# p_konum_plus — F3 STEP 1 r1 (v6) — Corrected Ratification Candidate — End-of-Task Response (verbatim)

```text
artifact_role = operational end-of-task chat response, saved verbatim on user request
status        = NON-NORMATIVE
date          = 2026-09-02
task          = F3 STEP 1 r1 REVISED FINAL v6 — P03/P04/P05 decision-packet correction
                + synthetic-only spline solver qualification (authorized by §4.3.1)
governing_prompt = p_konum_plus_F3_STEP_1_r1_REVISED_FINAL_v6_2026-09-02.md
qualification_suite_manifest =
  p_konum_plus/calibration/f3_spline_solver_qualification_manifest_2026-09-02.csv
qualification_suite_manifest_sha256 =
  522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883
```

---

# F3 STEP 1 r1 (v6) — Corrected Final PI Ratification Candidate

**NON-NORMATIVE. No row is PI-accepted here. No real SSA fit, no cross-fit execution, no C4 probe on real data, no candidate statistic, no threshold value was computed.** The only execution was the §4.3.1-authorized synthetic-only solver qualification.

## 0. Prechecks and transcription safety

All five governing hashes exact (v11 `d136502f…`, FREEZE r1 `ee2cb99d…`, D-F2-09 packet `8ff70a64…`, r2 `d5dd001d…`, r2a `2bc141c2…`); HEAD `3e4daf4`, no tracked modifications. **Transcription-safety re-verification (source wins): all PASS, zero mismatches** —

| prompt literal | hash-linked source confirmation |
|---|---|
| min-index argmax tie | D-F2-09 packet line 114: `j_star = min{ j : x_j = max_k x_k }` |
| ±1/8 offsets, 22.577778941738334 | D-F2-09 line 83 (K₁ = lattice midpoint; Δu/2 = 1/8) |
| 0.32057672965544004, √6 | D-F2-09 line 103 (= S₁(B₁), B₁ = 2.449489742783178) |
| β ∈ [1,6]; s_side_min increasing; s_side_min(1) = 0.01569377976942823; upper bound 3 | r2 lines 451–463; recomputed s_side_min(1) = `0.01569377976942823` (exact repr match) |
| W_s = 3 − s_side_min(1) | = `2.9843062202305717` (verified; provenance r2 §bounds, incorporated by FREEZE r1 by reference) |

## 1. Solver qualification report (§4.3 / §12)

```text
synthetic_solver_qualification_performed = true
synthetic_only = true                      SSA_access = false
qualification_suite_predeclared = true
qualification_suite_manifest_path =
  p_konum_plus/calibration/f3_spline_solver_qualification_manifest_2026-09-02.csv
qualification_suite_manifest_sha256 =
  522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883
manifest_written_before_execution = true   (hash printed before first solve)
qualification_case_count = 10
qualification_case_coverage = 4 RSS scales (near-noiseless 3.9e-29 / low 0.129 /
  moderate ~39-54 / high 105-146) x modes {0, 145, interior} x contexts
  {full, interior-mask, left-edge-mask, right-edge-mask} + degenerate
  many-active case (Q10: mode_idx=10 vs natural peak near u~0.78;
  145 active rows, rank 7)
kappa_solver = 0.1
spline_feasibility_acceptance_tol = 1e-8
active_set_identification_tol = 1e-8 (+ single predeclared expansion 1e-6)
spline_kkt_stationarity_tol = 1e-8
constraint_orientation = A c >= 0 ; lambda >= 0
reference = dual-NNLS convex-QP (lambda* = NNLS(L^-1 A^T, -L^-1 b);
  c_ref = H^-1(b + A^T lambda*)), certified per case by primal feasibility
  + NNLS KKT-existence (worst residual 8.2e-14, all <= 1e-8)
reference_certification = PASS (10/10; incl. rank-deficient Q10: 145 active, rank 7)
semantic_repeatability = PASS (all references and all endpoints, exact repr equality)
```

Per-case results (final delivered endpoint of each complete configuration; A-pass = objective accuracy `|RSS_solver−RSS_ref| ≤ 0.1·(1e-12+1e-9·|RSS_ref|)`, B-pass = feasibility ≤ 1e-8):

| case | RSS_ref | SOLVER-A (SLSQP→tc) | SOLVER-B (tc→polish→SLSQP) | SOLVER-C (tc only) |
|---|---|---|---|---|
| Q01 near-noiseless | 3.908e-29 | PRIMARY, err 2.8e-18, ratio 0.000 PASS | POLISH, err 5.1e-29 PASS | err 1.45e-14, ratio 0.145 PASS |
| Q02 low | 1.290e-01 | PASS | PASS | PASS |
| Q03 moderate/full | 5.379e+01 | PASS (ratio 0.002) | PASS | **FAIL ratio 1.55** |
| Q04 high/full | 1.049e+02 | PASS | POLISH_EXPANDED PASS | **FAIL ratio 693** |
| Q05 mode 0 | 6.549e-01 | PASS | PASS | PASS |
| Q06 mode 145 | 6.090e-01 | PASS | PASS | PASS |
| Q07 interior mask | 3.893e+01 | PASS | PASS | **FAIL ratio 11.9** |
| Q08 left-edge mask | 4.461e+01 | PASS | PASS | PASS (ratio 0.151) |
| Q09 right-edge mask | 4.801e+01 | PASS | POLISH_EXPANDED PASS | **FAIL ratio 291** |
| Q10 degenerate | 1.460e+02 | PASS | POLISH PASS | **FAIL ratio 74.8, viol 6.9e-11** |

```text
qualification_pass[SOLVER-A] = true   (SLSQP primary succeeded in all 10 cases;
                                       fallback never invoked; reported property:
                                       a fallback endpoint would face identical criteria)
qualification_pass[SOLVER-B] = true   (all endpoints KKT-certified; L3 satisfied;
                                       expansion step used only in Q04/Q09)
qualification_pass[SOLVER-C] = false  (fails objective accuracy in Q03/Q04/Q07/Q09/Q10)
SOLVER-C = eliminated                  SOLVER-D = not needed (no comparator widening)

recommended_solver_option = SOLVER-B
  (every delivered endpoint carries its own primal-feasibility + NNLS KKT-existence
   certificate; smallest error-to-tolerance margins incl. the degenerate case)
bounded_alternative = SOLVER-A (also fully qualified; simpler; endpoints not
  self-certified)
spline_solver_qualification = PASS
```

These are solver-qualification diagnostics, not scientific adequacy outcomes.

## 2. Corrected D-P03-4 — shape-constrained low-df spline benchmark

Supersedes (cleanup): `shape_constraint = low_df_only`, the multi-wave-contradiction rationale, and the "closed-form normal equations" wording. Corrected pin:

- **Role:** `adequacy_benchmark_only`; `automatic_primary_fallback = false`; `third_primary_generator = false`; `winner_eligible = false`. `R_REV_consumed = false`, `R_REV_resolved = false`; no P-27 resolution.
- **Representation:** degree-3 clamped B-spline, knot vector `[0,0,0,0, 0.2,0.4,0.6,0.8, 1,1,1,1]`, 8 basis functions (nominal df 8), evaluated on the frozen 146-point u-grid.
- **Shape constraint (the v11-required property):** grid-unimodality per §4.1 — for mode `mode_idx ∈ {0..145}`: `q[t+1]−q[t] ≥ 0` for `t < mode_idx`, `≤ 0` for `t ≥ mode_idx`; mode 0 = monotone non-increasing (W-L-compatible), mode 145 = monotone non-decreasing (W-R), interior = single turning point (W-I). Constraints imposed on the **full 146-grid for every fit, including masked fits**. No multi-wave spline.
- **Objective:** `RSS_spline_O(c) = Σ_{t∈O} (z_t − (Bc)_t)²` — a convex inequality-constrained least-squares problem (not closed-form). Metric-facing prediction = `z_ddof0(Bc over full grid)`. Zero-variance/non-finite full-grid fit ⇒ `spline_fit_status = FAILURE` → D-P03-7.
- **Solver pin (recommended, qualified):** SOLVER-B — trust-constr primary (`gtol=1e-10, xtol=1e-14, barrier_tol=1e-12, maxiter=1000`; success = status ∈ {1,2} and finite endpoint/objective) → active-set equality-KKT post-polish (identification `|A c| ≤ 1e-8`, single predeclared expansion to `1e-6` if the polished point is unacceptable) — a polished endpoint is accepted only with primal feasibility ≤ 1e-8 **and** NNLS KKT-existence residual ≤ 1e-8 → SLSQP fallback (`ftol=1e-12, maxiter=500`) if still required; fallback endpoint faces the identical acceptance rule; if it also fails, that mode is numerically invalid.
- **Mode selection (order-independent):** solve all 146 modes; `RSS_min` = global minimum over numerically valid modes; `equivalent_mode_set = {mode : |RSS_mode − RSS_min| ≤ 1e-12 + 1e-9·max(|RSS_mode|,|RSS_min|)}`; `winner_mode_idx = min(equivalent_mode_set)`. No running-best chain. No valid mode ⇒ `spline_fit_status = FAILURE`. Qualification showed solver accuracy well inside the comparator (worst ratio 0.000–0.15 of the κ-scaled tolerance), so the provisional comparator needs no PI widening.
- **Determinism claim:** deterministic algorithm and semantic decision rule within the frozen code/environment; cross-process/cross-platform bitwise equality not claimed.

## 3. D-P03-6 — WC-ALC scope consequence (genuine PI decision)

The stated consequence is not hidden: F1 eligibility is support-based, so the 906 can include non-WC-ALC (multi-wave/revival) trajectories, while both families **and** the benchmark are unimodal — a purely spline-relative C2/C3 can be insensitive to that mismatch in common mode.

**Recommended: D-P03-6A — within-WC-ALC adequacy interpretation.**
`F3_generator_adequacy_claim` = adequacy of the two primary families relative to the frozen WC-ALC/shape-constrained benchmark architecture; `F3_is_not` a test that every eligible trajectory is WC-ALC. **All 906 trajectories remain in C1–C6 aggregation without exception**: every trajectory enters C1 coverage, contributes to C2/C3/C5 medians and C4 probes whenever its fits are valid, and is governed by the D-P03-7 completeness gate otherwise; no morphology screen exists or is implied, and `silent_multiwave_exclusion = forbidden`. Claims that may be made: relative and benchmark-anchored adequacy of P-01/P-02 on the full frozen sample. Claims that may not: universal WC-ALC membership, R-REV resolution, multi-wave sensitivity of C2/C3. `R_REV_handling` stays outside this ratification; its outcome-blind P-27 gate must be governed later before any R-REV use.

**Bounded alternative D-P03-6B (fully specified, not recommended):** add to C3 a second, explicitly diagnostic **unconstrained** low-df spline reference (identical basis, knots, objective and solver contract, no shape constraints — a linear LS solve) with statistic `Δ_shape,i = RSS_constrained,i − RSS_unconstrained,i ≥ 0` on the full-data fit, reported per sex as `median Δ_shape` and the share of trajectories with `Δ_shape > d_shape` (owner literal, e.g. 5.0 in RSS units). Role = morphology-mismatch **diagnosis only**: report-only, no pass/fail participation, no position in the frozen six-step order, never a fallback or selector. Rejected because it adds one solver family and two literals with no consuming gate; 6A states the claim boundary honestly without them. If the PI wants multi-wave sensitivity to gate F3, that is an additional PI scientific decision beyond both options.

## 4. Corrected D-P05 — exact within-trajectory cross-fit

Architecture retained (K=5, g=0, edge blocks retained, all-5-folds completeness, rng_used=false). Corrections and binding pins:

- **Fold arithmetic (cleanup — supersedes any `29/29/30/29/29` wording):** `[floor(b·146/5), floor((b+1)·146/5))` ⇒ boundaries `[0, 29, 58, 87, 116, 146]`, sizes **29/29/29/29/30**, literal ranges `fold 0 = [0,29)`, `fold 1 = [29,58)`, `fold 2 = [58,87)`, `fold 3 = [87,116)`, `fold 4 = [116,146)`.
- **`g = 0` binding rationale (§6.0A adopted verbatim):** classification(g) = STRUCTURAL_LITERAL; four-parameter global parametric curves limit—but do not eliminate—adjacent-year-dependence optimism; identical folds for families and benchmark improve comparability **without** any claim that leakage cancels (`common_mode_leakage_cancellation_claim = false`, `dependence_free_reconstruction_claim = false`); a positive gap would mix dependence separation with boundary-information loss; residual dependence is assessed by C3. `g_sens > 0` = PI_OPTION_ONLY, default NOT_INCLUDED, strictly report-only if ever authorized.
- **Masked generator objective (exact, no shortcut):** `ghat(θ) = z_ddof0(g(u_grid; θ))` always on the full 146-grid; `L_O(θ) = Σ_{t∈O} (z_t − ghat_t(θ))²`. The identity `L = 2T(1−ρ)` is full-grid-only and is not reused on subsets. **X4 guard retained** `L_INVALID_PREDICTION_GUARD = 585` with the corrected rationale: `L_O ≤ full_grid_L ≤ 584` because the masked objective sums a subset of the nonnegative full-grid terms (not via any `L_O ≤ 4|O|` claim).
- **Feature start under masking (mandatory pin; source-verified):** `j_star_O = min{ j ∈ O : x_j = max_{k∈O} x_k }`, `u_star_O = j_star_O/145`; then the frozen D-F2-09.5 formulas unchanged — P-01 `(u_star_O − 1/8, u_star_O + 1/8, 22.577778941738334, 22.577778941738334)`; P-02 `(u_star_O, 0.32057672965544004, 0.32057672965544004, √6)` (m = P-02 location, never the spline mode_idx). If invalid ⇒ `FEATURE_START_REJECTED`, no clipping, no substitution; the frozen fixed grid remains. Same observed-only principle in C4 probes. This is an F3 masked-fit pin; the accepted full-data D-F2-09 rule is unaltered.
- **§6.3A:** mask changes the objective only — prediction standardization, Kural T, Kural S, scientific support, and the frozen failure semantics stay on the full stabilized 146-grid exactly as in F2; no fold-specific admissibility domain.
- **C2 claim boundary (binding):** C2 = cross-fitted reconstruction conditional on the frozen F1 z-space; `raw_scale_forecasting_claim = false`; `strict_preprocessing_leakage_free_forecasting_claim = false`; `temporal_dependence_leakage_free_claim = false` (contiguous g=0 blocks do not isolate held-out years from adjacent-year dependence); F1 is not re-normalized within folds. C2 statistic: ρ_cv,i = corr(z_i, ĝ_cv,i) with every year predicted exactly once out-of-sample.
- **Determinism:** fold identity = pure function of the year index; semantic reproducibility claimed under the frozen contract; cross-process/cross-platform bitwise equality not claimed.

## 5. Corrected D-P03-5 — window-truncation identifiability

Retained: E=15, left+right probes, FULL-support inputs, missing ≠ zero, no [0,4] semantics, no imputation; probe fits use §6.3 observed-only feature start and §6.2 direct masked `L_O`. **C4a** = probe-fit/admissibility success share (also feeds D-P03-7). **C4b replaced** (correlation-on-observed-region superseded): for each successful trajectory × probe, `RMSE_edge = sqrt((1/E)·Σ_{t∈masked edge}(probe_prediction_t − reference_prediction_t)²)` on the **masked** E indices, reference = the family's own full-data frozen-contract fit prediction; lower = better; spline-relative — the benchmark undergoes the identical truncation and masked-edge comparison. Binding disclosure adopted verbatim: C4b measures functional identifiability of edge behaviour under simulated window censoring; it does **not** measure edge accuracy against observed data (C2's first/last folds provide that), morphology fit/WC-ALC membership (C1–C3, D-P03-6), or parameter-space instability (C5); `common_mode_misspecification_blindness = true` — C4b can be small even when both fits are wrong at the edge in the same way.

**New RMSE-unit literals (not recycled from ρ units):** `delta_4_RMSE = 0.10` (alternatives 0.05 / 0.20) and `tau_4b_RMSE = 0.02` (alternatives 0.01 / 0.05), both OWNER_SCIENTIFIC_TOLERANCE. Outcome-blind rationale: predictions live on the frozen unit-variance z-scale, so RMSE_edge is expressed in trajectory-standard-deviation units; a 0.10-sd margin permits edge-behaviour drift an order of magnitude below the trajectory's own scale, and the equivalence tolerance is one-fifth of the margin so that tie declaration is strictly finer than the pass margin.

## 6. D-P03-7 — completeness gate (genuine PI decision)

The log-only exclusion rule is superseded. **Recommended: Option A — completeness sub-gate + paired-valid sets.** For every complete-case criterion (C2, C3, C5; C4 via C4a plus C4b's paired-valid set, which is always reported): define per family/sex `family_complete_share` and, where spline-relative comparison is used, `paired_family_spline_valid_share`; the criterion can pass only if the relevant share ≥ `c_complete`; every spline-relative statistic is computed on the **same paired-valid trajectory set** for family and benchmark. **Floor recommendation: a new owner literal `c_complete = 0.90`** rather than reusing `c_cov` — numerically equal today, but independently owned: reusing `c_cov` would silently couple morphology coverage (a scientific adequacy claim about fit existence) with statistical-population sufficiency (a validity condition on medians), so a future PI modification of one would invisibly move the other. Consequence: with both at 0.90, a family cannot pass any criterion computed on fewer than 90% of the stratum, and paired-valid restriction removes family-asymmetric subset advantages. **Option B (fully specified alternative):** a family passes a complete-case criterion only if the statistic is defined for every trajectory in the stratum (complete share = 1) and the statistic passes; undefined values are never numerically imputed and no finite sentinel exists — rejected as brittle (a single numerical failure fails a criterion outright). **§8.1 binding P03 propagation:** a statistic required by a P03 criterion that is undefined for a family and not pre-frozen `STRUCTURALLY_NOT_APPLICABLE` ⇒ that family cannot pass that criterion ⇒ cannot enter the BOTH-PASS P04 domain; both families failing ⇒ `STOP, action = redesign`. The pre-frozen `STRUCTURALLY_NOT_APPLICABLE` set is declared **empty**.

## 7. C3 and C5 conventions

**C3** retained: per-sex median of |lag-1 residual autocorrelation| of the full-data fit residuals, spline-relative (`δ₃ = 0.05`). Explicit label: C3 measures **excess first-order residual structure relative to the same WC-ALC-shaped benchmark**, not general morphology membership (that boundary is D-P03-6A's). Under recommended 6A, no absolute component is added; 6B's diagnostic addition is specified in §3 above. No post-measurement change permitted.

**C5** exact conventions: `stability_component_j = IQR_across_folds(θ_j)/W_j`; `s_stab,i = max_j` over the family's 4 parameters; per-sex median ≤ `c_stab = 0.10`. Frozen marginal outer widths (source-verified, FREEZE r1 by reference): P-01 `c_r, c_d`: W = 3 (support [−1,2]); `k_r, k_d`: W = 123.43902548550072 (support [4, 127.43902548550072]); P-02 `m`: W = 3; `β`: W = 5 ([1,6]); `s_l, s_r`: **W_s = 3 − s_side_min(1) = 2.9843062202305717** — a normalization constant only; the β-dependent feasibility constraint remains fully active during fitting. **IQR pin:** `numpy.quantile(values, 0.25/0.75, method="linear")`, IQR = Q75 − Q25, over the five fold estimates. **Median pin:** `numpy.median` (even n ⇒ mean of the two central order statistics), used everywhere a median appears. **Linear-width rationale (owner interpretive choice, not measurement-derived):** all eight parameters were ratified in F2 as linear intervals; linear width is the only convention requiring no additional transform decision (a log scale would need per-parameter base and zero-handling choices — new researcher degrees of freedom), and it makes one unit of the stability statistic mean the same fraction of the ratified support for every parameter.

## 8. Corrected D-P04

Retained: invocation only when both families pass every required P03 gate; lexicographic C1→C6 (4a before 4b); worse-sex scalar convention; no historical privilege; terminal deterministic family-ID fallback (`"P-01" < "P-02"`) only after all scientific comparisons remain equivalent. **NONCOMPARABLE-skip deleted:** an undefined required quantity means the family did not pass that P03 criterion and is not in the BOTH-PASS domain; only pre-frozen `STRUCTURALLY_NOT_APPLICABLE` sub-statistics (declared set: empty) may be omitted; applicability is never decided post hoc. **Tolerances:** τ₁ = 0.01, τ₂ = 0.005, τ₃ = 0.01, τ₄ₐ = 0.01, **τ₄ᵦ_RMSE = 0.02** (replaces the ρ-unit value), τ₅ = 0.01, τ₆ = 0.

## 9. Literal inventory (§12) — all with classification and outcome-blind rationale

| literal | value | class | rationale (compressed) |
|---|---|---|---|
| c_cov | 0.90 | OWNER_SCIENTIFIC_TOLERANCE | a family unable to admissibly fit ≥90% of a stratum fails coverage as a scientific matter |
| δ₂, δ₃ | 0.05, 0.05 | OWNER_SCIENTIFIC_TOLERANCE | benchmark-relative slack of 0.05 in ρ / |φ| units ≈ 5% of the frozen unit scale |
| c_ident | 0.85 | OWNER_SCIENTIFIC_TOLERANCE | truncated-window refits are strictly harder; floor set below c_cov by one nominal step |
| E | 15 | STRUCTURAL_LITERAL | ≈10% of the 146-year window; large enough to hide a feature edge, small enough to keep Kural-S-viable interiors |
| δ₄_RMSE / τ₄ᵦ_RMSE | 0.10 / 0.02 | OWNER_SCIENTIFIC_TOLERANCE | §5 above; fresh RMSE-unit choices, not recycled ρ values |
| c_stab | 0.10 | OWNER_SCIENTIFIC_TOLERANCE | fold-to-fold IQR above 10% of the ratified support width signals instability |
| c_complete | 0.90 | OWNER_SCIENTIFIC_TOLERANCE | §6 above; independently owned, not a c_cov alias |
| K / g / fold rule | 5 / 0 / floor-formula | STRUCTURAL_LITERAL | K=5 keeps ≥116 training years per fold (Kural-S-safe); g=0 per §6.0A binding wording |
| spline degree/knots/basis/mode set | 3 / {0.2,0.4,0.6,0.8} / 8 / {0..145} | STRUCTURAL_LITERAL | fixed clamped low-df design; full-grid mode enumeration |
| mode tie comparator | 1e-12 + 1e-9·max | IMPLEMENTATION_TOLERANCE | F2-form numerical-equivalence pattern; qualification shows solver error ≪ comparator |
| spline_feasibility_acceptance_tol | 1e-8 | IMPLEMENTATION_TOLERANCE | spline-only pin patterned after (not inherited from) F2 |
| active_set_identification_tol / expansion / spline_kkt_stationarity_tol | 1e-8 / 1e-6 / 1e-8 | IMPLEMENTATION_TOLERANCE | required for deterministic reference certification and SOLVER-B acceptance |
| kappa_solver | 0.1 | IMPLEMENTATION_TOLERANCE | solver error must sit an order below the mode comparator |
| solver options (tc/SLSQP as §2) | — | IMPLEMENTATION_TOLERANCE | qualified configuration literals |
| P04 τ₁..τ₆ | §8 values | OWNER_SCIENTIFIC_TOLERANCE | pre-frozen equivalence scales per criterion unit |
| transcribed F2 literals (feature start, W_j) | §0 table | (frozen F2; re-verified) | source-wins confirmed, zero mismatches |
| spline-relative threshold **values** | — | MEASUREMENT_DERIVED_THRESHOLD | `NOT_COMPUTED`; computable only under the frozen rule after ratification |

No candidate measurement justified any literal.

## 10. §13 structural planning note (informational)

`906 × 146 × 8 = 1,058,208` spline subproblems — an operation-count planning quantity, not a runtime; nothing executed. If optimization is wanted later, only mathematically exact reuse is permitted (e.g., per-mask Gram-matrix factorizations shared across the 146 modes — identical solutions by construction).

## 11. §14 overlap note (informational)

C2's first/last folds already contain edge-extrapolation difficulty; C4's E=15 probes are a targeted edge-identifiability diagnostic. `partial overlap = true, contradiction = false`; both retained.

## 12. Corrected PI ratification table (§15)

| decision_id | previous_packet_status | correction_applied | final_exact_recommendation | bounded_alternative_set | why_recommended | main_risk | source | PI_action |
|---|---|---|---|---|---|---|---|---|
| D-P03-1 | exact statistics, some conventions loose | C4b→RMSE_edge; §8.1 failure propagation; median/IQR pins | six criterion contracts as corrected (§§4–7) | substitute statistics per criterion | computable from frozen machinery, candidate-blind | margin literals are judgment calls, PI-modifiable | v11 §5 order (literal); operationalization = post-v11 pin | ACCEPT / MODIFY |
| D-P03-2 | sex_specific, both-pass | none | sex_specific; both sexes must pass | pooled-906; single-sex pass | prevents stratum masking; no new assumptions | smaller stratum drives outcomes | post-v11 pin | ACCEPT / MODIFY |
| D-P03-3 | ρ-unit τ₄ᵦ; no classifications | full §9 inventory with 4-way classification + rationale | literals per inventory table | listed per literal | every literal pre-frozen, classified, outcome-blind | tolerance choices decide edge cases; frozen pre-measurement | post-v11 pins | ACCEPT / MODIFY |
| D-P03-4 | df-cap called "shape constraint"; "normal equations"; unqualified solver | grid-unimodal constraint; mode enumeration; qualified SOLVER-B; certified reference; order-independent mode selection | §2 pin verbatim | SOLVER-A (qualified); df 6/10 knot variants | v11 shape-constraint honored; solver PASS with KKT-certified endpoints incl. degenerate case | 146-mode enumeration cost (planning note §10); benchmark stays unimodal by design (see D-P03-6) | v11 §5 role (literal); implementation = post-v11 pin | ACCEPT / MODIFY |
| D-P03-5 | correlation-unit C4b on observed region | C4b = RMSE_edge on masked edge vs own full-data reference; new RMSE literals; binding disclosure | §5 pin verbatim | E ∈ {10, 20}; δ/τ alternatives | measures exactly the identifiability question without touching OD-7 semantics | **C4b = functional identifiability under simulated censoring (probe fit vs the family's own full-data fit on the masked edge). It does not measure edge accuracy, morphology fit / WC-ALC membership, or parameter-space instability, and it is blind by design to common-mode misspecification.** | post-v11 pin; F1 OD-7 respected | ACCEPT / MODIFY |
| D-P03-6 | consequence not surfaced | explicit scope decision with claim boundaries | **6A** — within-WC-ALC adequacy claim; all 906 remain in aggregation; R-REV/P-27 untouched | **6B** — diagnostic unconstrained-spline Δ_shape report-only addition (fully specified §3) | honest claim boundary without new machinery | genuine PI scientific choice: accepting 6A accepts that F3 does not gate multi-wave mismatch | v11 §4/§5 morphology + post-v11 pin | ACCEPT / MODIFY |
| D-P03-7 | log-only exclusion | completeness sub-gate + paired-valid sets + §8.1 propagation | **Option A** with new owner literal c_complete = 0.90 | Option B (all-defined-or-fail, fully specified); c_complete reuse of c_cov | blocks family-asymmetric subset advantages; keeps comparisons paired | genuine PI choice: floor value and new-literal-vs-reuse have scientific consequences (§6) | post-v11 pin | ACCEPT / MODIFY |
| D-P04 | NONCOMPARABLE-skip; ρ-unit τ₄ᵦ | skip deleted (undefined ⇒ not passed); τ₄ᵦ_RMSE; empty STRUCTURALLY_NOT_APPLICABLE set | §8 rule verbatim | T-B composite (rejected: re-weights frozen hierarchy); τ alternatives | preserves frozen six-level hierarchy deterministically | tolerances could decide the winner; all pre-frozen, PI-owned | v11 §5 tie-break (literal); exactness = post-v11 pin | ACCEPT / MODIFY |
| D-P05 | 29/29/30/29/29 error; ρ-shortcut risk; no masked feature-start pin | fold literals corrected; direct masked L_O; §6.0A g-rationale; feature-start pin; §6.3A; C2 claim boundary; corrected X4 rationale | §4 pin verbatim | K = 10; g_sens report-only PI option | genuine out-of-sample reconstruction per year; nothing but the objective mask changes | blocked-CV optimism not fully eliminated (disclosed; C3 assesses residual dependence) | v11 §5 cross-fit (literal); scheme = post-v11 pin | ACCEPT / MODIFY |

## 13. Findings (§17)

- **global blocker:** none. **gate-specific blocker:** none.
- **cleanup (all corrected in this packet):** fold-size wording 29/29/30/29/29 superseded; `shape_constraint = low_df_only` superseded; multi-wave-contradiction spline rationale superseded; "closed-form normal equations" superseded; NONCOMPARABLE-skip superseded; ρ-unit τ₄ᵦ superseded; log-only exclusion superseded; X4 rationale restated for masked objectives.
- **informational:** C2/C4 partial overlap (§11); structural count 1,058,208 (§10); SOLVER-A fallback never invoked in qualification; the 6A-vs-6B and Option-A-vs-B rows are genuine PI scientific choices, marked as such.

## 14. Ratification-ready audit (§16)

A NO · B NO · C NO · D NO · E NO · F NO · G NO · H NO · I NO · J NO — (A–J all as expected).
K YES (10/10 cases, κ pre-frozen) · L YES · L2 YES (10/10 certified, worst residual 8.2e-14) · L3 YES (SOLVER-B endpoints self-certified) · M YES · N YES (§0 table, source-wins) · O YES (§6.3A) · P YES (`522d3508…` printed pre-execution) · Q YES (final-endpoint semantics throughout) · R YES (Q01/Q02 spline-representable; Q10 degenerate, 145 active/rank 7) · S YES (§4, §6.0A adopted) · T YES (§12 D-P03-5 row) · U YES (|Ac| ≤ tol, A c ≥ 0 / λ ≥ 0, rank-deficiency handled by NNLS existence).

`spline_solver_qualification = PASS`; no reference failed certification; no case failed. Smallest correction still required: none.

---

```text
GLOBAL_BLOCKER = none
GATE_SPECIFIC_BLOCKER = none
cleanup = fold-size wording; shape-constraint wording; normal-equations wording;
          NONCOMPARABLE-skip; rho-unit tau_4b; log-only exclusion; X4 rationale
          (all superseded/corrected in this packet)
informational = C2/C4 partial overlap; structural count 1,058,208;
                SOLVER-A fallback never invoked in qualification;
                D-P03-6 and D-P03-7 are genuine PI scientific choices

F3_ENTRY_READY = true
F3_EXECUTION_READY = false

P03_derivation_rule_status = OWNER_RATIFICATION_REQUIRED
P03_threshold_values       = NOT_COMPUTED
P04_status                 = OWNER_DECISION_REQUIRED
P05_status                 = OWNER_DECISION_REQUIRED

D_P03_6_status = OWNER_DECISION_REQUIRED
D_P03_7_status = OWNER_DECISION_REQUIRED

RATIFICATION_READY = true

spline_solver_qualification = PASS

qualification_suite_manifest_sha256 =
  522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883

reference_certification = PASS

candidate_specific_fit = false
crossfit_execution = false
C4_probe_execution = false
adequacy_measurement = false
generator_selected = false

F3_started = false
F4_started = false
commit = false

NEXT_ACTION =
PI review and explicit acceptance/modification of the corrected
D-P03-1..7, D-P04 and D-P05 final ratification candidate
```
