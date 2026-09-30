# p_konum_plus — F3 STEP 1 — Corrected Ratification Candidate r3 (standalone)

```text
artifact_role = standalone PI ratification candidate for
                D-P03-1..7, D-P04, D-P05
status        = NON-NORMATIVE recommendation; nothing here is PI-accepted
date          = 2026-09-03
revision      = r3

parent =
f3_step1_r1_corrected_ratification_candidate_r2_2026-09-03.md

parent_sha256 =
b8ce7667200787eeda6e71b6d8ede6aebc9bb4fd1b05344dc31f62f361bc399c

revision_reason =
F3-STEP1-PROV-03 reference-only qualification-provenance correction

scientific_change = false
execution_change = false
methodology_change = false

lineage       = r1 (6e7b5634…) -> r2 (parent, remains historical provenance)
                -> r3 (this file)
governing     = v11 (d136502f…, v11_wins=true); F2 FINAL FREEZE r1 (ee2cb99d…);
                v6 prompt (418092db…); narrow-correction prompt (b0d55ba0…)
                + ADDENDUM A r1
correction_scope = F3-STEP1-EXACT-01, F3-STEP1-EXACT-02, SOLVER-B exactness
                cleanup ONLY; all other r1 content carried forward unchanged
                in substance
P03_threshold_values = NOT_COMPUTED
F2_reopening = false ; new_methodology_review = false
```

This candidate is standalone: no prior packet needs to be opened to implement
any row. Source labels: `V11_LITERAL` / `POST_V11_EXECUTION_PIN` /
`FROZEN_F2_INPUT`.

---

## 1. D-P03-2 — sex / reference population (unchanged from r1)

`sex_specific` derivation; every criterion computed and gated separately for
F (n=435) and M (n=471); a family passes a criterion only if it passes in
BOTH sexes. Rationale: separate frozen strata; pooling lets the larger stratum
mask the smaller. [POST_V11_EXECUTION_PIN; stratum sizes FROZEN_F2_INPUT/F1]
Bounded alternatives: pooled-906; single-sex pass. PI_action = ACCEPT / MODIFY.

## 2. D-P03-7 — completeness gate (Option A, unchanged from r1; binding for §3)

For every criterion computed on a subset (C2, C3, C5, C4b): define per
family/sex `family_complete_share` (share of the stratum in the criterion's
valid set) and, where a spline-relative comparison is used,
`paired_family_spline_valid_share` (share in the PAIRED set: family valid AND
benchmark valid on the same trajectories). The criterion can pass only if the
relevant share >= `c_complete = 0.90` (new owner literal, deliberately not an
alias of `c_cov`). Spline-relative statistics are always computed on the same
paired-valid set for family and benchmark. **§8.1 propagation (binding in
P03):** a statistic required by a P03 criterion that is undefined for a family
and not pre-frozen `STRUCTURALLY_NOT_APPLICABLE` (declared set: EMPTY) means
that family cannot pass that criterion and cannot enter the BOTH-PASS P04
domain; both families failing ⇒ `STOP, action = redesign`. No imputation, no
sentinel, anywhere. [POST_V11_EXECUTION_PIN]
Bounded alternatives: Option B (statistic must be defined for the full
stratum, complete share = 1, else criterion fails); c_complete as a reuse of
c_cov. PI_action = ACCEPT / MODIFY.

## 3. D-P03-1 — standalone exact criterion contracts C1–C6

Common to all six: unit_of_evaluation = one eligible trajectory fitted per
family under the unmodified FREEZE r1 contract (all frozen starts, frozen
optimizer/fallback, frozen admissibility and failure taxonomy)
[FROZEN_F2_INPUT]; adequacy order C1→C2→C3→C4→C5→C6 [V11_LITERAL, v11 §5];
first failed criterion ⇒ family FAIL, all six still measured and logged;
sex handling per D-P03-2; sex-level aggregation = `numpy.median` (even n ⇒
mean of the two central order statistics); trajectory-level medians/IQRs per
D-P03-3 conventions; undefined-statistic behavior per D-P03-7 §8.1;
equivalence tolerances live only in D-P04. All operationalizations below are
POST_V11_EXECUTION_PIN unless labelled otherwise.

### C1 — morphology coverage
- scientific_role: existence of eligible admissible fits (v11 criterion 1)
  [V11_LITERAL role]. NOT a morphology-membership screen (D-P03-6A boundary).
- required-fit population: all n_s trajectories of the stratum; no valid-set
  restriction (denominator is the full stratum).
- exact trajectory statistic: Boolean — trajectory has >= 1 eligible
  admissible full-data fit under FREEZE r1.
- sex-level statistic: coverage_F,s = (# trajectories with an eligible
  admissible full-data fit) / n_s. direction: higher.
- benchmark: none. threshold_derivation_type = absolute_structural.
- literals: c_cov = 0.90 (OWNER_SCIENTIFIC_TOLERANCE; alternatives 0.85/0.95).
- measurement-derived quantity: none (floor is the rule literal).
- pass/fail: coverage_F,s >= c_cov in BOTH sexes.
- undefined behavior: impossible by construction (denominator fixed).
- D-P03-7: C1 is itself the coverage gate; failed-fit trajectories reduce the
  numerator only.
- P04 scalar (if both families pass all gates): min over sexes of
  coverage_F,s; tolerance tau_1.

### C2 — cross-fitted reconstruction / predictive fit
- scientific_role: v11 criterion 2 [V11_LITERAL role], operationalized by
  D-P05; C2 is a frozen-F1-z-space conditional reconstruction statistic —
  binding claim boundary: raw_scale_forecasting_claim = false;
  strict_preprocessing_leakage_free_forecasting_claim = false;
  temporal_dependence_leakage_free_claim = false.
- required-fit population / paired-valid rule: trajectory is
  crossfit-complete for a fitter iff all 5 P05 folds deliver an eligible
  admissible training fit; the C2 valid set V2_s = {i : family
  crossfit-complete AND spline benchmark crossfit-complete}; completeness
  requirement paired_family_spline_valid_share = |V2_s|/n_s >= c_complete.
- exact trajectory statistic: rho_cv,i = Pearson correlation between the
  frozen F1 z-trajectory z_i and the assembled out-of-sample prediction
  ghat_cv,i (every year predicted exactly once by the fold that held it out;
  per-fold predictions are the full-grid z_ddof0-standardized curves of the
  training fits, evaluated at held-out years) [FROZEN_F2_INPUT convention].
- sex-level: M_F,s = numpy.median over V2_s of rho_cv,i; direction: higher.
- benchmark: M_S,s = same statistic for the D-P03-4 spline on the same V2_s.
- threshold_derivation_type = spline_relative_margin; literal delta_2 = 0.05
  (OWNER_SCIENTIFIC_TOLERANCE; alternatives 0.03/0.10).
- measurement-derived quantity: threshold_s = M_S,s − delta_2 (NOT_COMPUTED
  until measurement under this frozen rule).
- pass/fail: M_F,s >= M_S,s − delta_2 in BOTH sexes AND
  |V2_s|/n_s >= c_complete in BOTH sexes.
- undefined behavior: V2_s empty or share below floor ⇒ criterion not passed
  (§8.1); no imputation.
- P04 scalar: min over sexes of M_F,s; tolerance tau_2.

### C3 — systematic residual morphology / structure (unchanged from r1)
- exact trajectory statistic: phi_i = |lag-1 sample autocorrelation| of the
  full-data best-eligible-fit residuals r_t = z_t − ghat_t; direction: lower.
- valid set V3_s = {i : family has an eligible full-data fit AND spline has a
  valid full-data fit}; paired_family_spline_valid_share >= c_complete.
- sex-level medians; spline-relative: pass iff
  median|phi|_F,s <= median|phi|_S,s + delta_3 (= 0.05,
  OWNER_SCIENTIFIC_TOLERANCE) in BOTH sexes, plus the completeness floor.
- Explicit label: C3 measures EXCESS first-order residual structure relative
  to the same WC-ALC-shaped benchmark, not morphology membership.
- P04 scalar: max over sexes of median|phi|_F,s; tolerance tau_3.

### C4 — censored-case / window-truncation identifiability
F1-consistency (binding): nothing imputed; missing != zero; no [0,4]
semantics; all 906 inputs FULL-support; probes mask observed years only
[FROZEN_F2_INPUT / F1 OD-7].

Probe construction: two deterministic variants per trajectory — LEFT masks
year indices [0, E), RIGHT masks [146−E, 146), E = 15 (STRUCTURAL_LITERAL;
alternatives 10/20). Probe fits use the masked objective and observed-only
feature start of D-P05 §6 items (v6 §6.2/§6.3) and full-grid admissibility
(v6 §6.3A).

**C4a — probe success (exact fields):**
- unit_of_probe = one trajectory × one edge-probe (LEFT or RIGHT).
- probe_success (Boolean) = the truncated-window refit under the unmodified
  FREEZE r1 contract delivers >= 1 eligible admissible endpoint (frozen
  taxonomy: converged/finite, scientific-domain pass, Kural T pass, Kural S
  pass, morphology-admissible — all evaluated on the full stabilized
  146-grid).
- Under-mask edge cases (ADDENDUM A.5, adopted verbatim): if the masked edge
  contains the trajectory's entire Kural-S support region, or the
  observed-only feature start is rejected AND every frozen grid start fails,
  or the truncated refit is inadmissible ⇒ probe = C4a failure (numerator
  excluded, denominator retained); probe absent from the C4b paired-valid
  set; no imputation, no sentinel.
- C4a denominator = 2·n_s (every trajectory×probe pair of the stratum;
  nothing excluded from the denominator).
- C4a trajectory handling: probes enter individually; no per-trajectory
  combination in C4a.
- C4a sex-level statistic: ident_F,s = (# successful probes of sex s)/(2·n_s);
  direction: higher.
- C4a pass/fail: ident_F,s >= c_ident (= 0.85, OWNER_SCIENTIFIC_TOLERANCE;
  alternatives 0.80/0.90) in BOTH sexes.
- D-P03-7 relationship: C4a is the probe-completeness component of C4; failed
  probes propagate to C4b's paired-valid set; ident_F,s is always defined.

**C4b — masked-edge functional identifiability (exact chain):**
- per successful trajectory×probe:
  `RMSE_edge = sqrt((1/E) * sum_{t in masked_edge}
  (probe_prediction_t − full_data_reference_prediction_t)^2)`;
  direction lower; predictions are the frozen full-grid z_ddof0-standardized
  curves; reference = the family's own full-data FREEZE-r1 fit (for the
  spline: the spline's own full-data fit).
- **Gate status (PI decision, recommended): `C4b_status = P03_GATE`** — C4b
  participates in P03 pass/fail with delta_4_RMSE and in P04 with
  tau_4b_RMSE. Rationale: v11 criterion 4 is part of the frozen adequacy
  order; gating on C4a alone would reduce it to fit-success only. Bounded
  alternative: `REPORT_ONLY` — then delta_4_RMSE is deleted from P03,
  tau_4b_RMSE is deleted from P04, C4 gates on C4a alone, and C4b is a
  disclosed diagnostic. PI_action = ACCEPT / MODIFY.
- **LEFT/RIGHT combination (PI-owned interpretive choice; enumerated set of
  ADDENDUM A.4 only; recommended): `AGG-L1-WORSE`** —
  `r_i = max(RMSE_edge_LEFT_i, RMSE_edge_RIGHT_i)`.
  Structural rationale (no candidate result exists): W-L and W-R morphology
  classes are edge-anchored, so a family must remain identifiable under BOTH
  left and right truncation; the worse edge is the binding constraint; a mean
  can mask a one-sided identifiability failure. Bounded alternatives:
  `AGG-L1-SEPARATE` (LEFT and RIGHT aggregated and gated separately; C4b
  passes iff both sides satisfy the spline-relative inequality);
  `AGG-L1-MEAN` (`r_i = (LEFT_i + RIGHT_i)/2`). PI_action = ACCEPT / MODIFY.
- paired-valid set (under WORSE): V4_s = {i : family LEFT and RIGHT probes
  both successful AND spline LEFT and RIGHT probes both successful}. (Under
  SEPARATE: per-side paired-valid sets V4L_s, V4R_s.)
- completeness: |V4_s|/n_s >= c_complete in BOTH sexes (per side under
  SEPARATE).
- sex-level aggregation: C4b_F,s = numpy.median over V4_s of r_i^F; same for
  the spline, C4b_S,s, on the same V4_s.
- exact pass/fail (under P03_GATE + WORSE):
  `C4b_F,s <= C4b_S,s + delta_4_RMSE` in BOTH sexes, AND the completeness
  floor, AND C4a passes. delta_4_RMSE = 0.10 standardized-prediction RMSE
  units (OWNER_SCIENTIFIC_TOLERANCE; alternatives 0.05/0.20; fresh RMSE-unit
  choice, not recycled from rho units).
- C4b reporting rule (replaces the ambiguous r1 phrase): C4b_F,s, C4b_S,s,
  |V4_s|/n_s, and the per-side probe-failure shares are ALWAYS reported for
  provenance, under both P03_GATE and REPORT_ONLY.
- binding disclosure [carried from v6 §7.2]: C4b measures functional
  identifiability under simulated window censoring (probe fit vs the family's
  own full-data fit on the masked edge); it does NOT measure edge accuracy
  against observed data, morphology fit / WC-ALC membership, or
  parameter-space instability; common_mode_misspecification_blindness = true.
- P04 scalars: c4a scalar = min over sexes of ident_F,s (tau_4a); c4b scalar
  = max over sexes of C4b_F,s (tau_4b_RMSE = 0.02,
  OWNER_SCIENTIFIC_TOLERANCE; alternatives 0.01/0.05); sub-level order 4a
  before 4b; under REPORT_ONLY the 4b sub-level is removed.

### C5 — parameter stability (unchanged from r1)
- statistic: from the 5 P05 training fits, s_stab,i = max over the family's 4
  parameters of IQR_folds(theta_j)/W_j; direction lower.
- frozen marginal outer widths [FROZEN_F2_INPUT, source-verified]: P-01
  c_r,c_d: W=3; k_r,k_d: W=123.43902548550072; P-02 m: W=3; beta: W=5;
  s_l,s_r: W_s = 3 − s_side_min(1) = 2.9843062202305717 (normalization
  constant only; the beta-dependent feasibility constraint stays active in
  fitting).
- valid set: crossfit-complete trajectories of the family;
  family_complete_share >= c_complete (absolute criterion — no pairing).
- sex-level: median s_stab <= c_stab (= 0.10, OWNER_SCIENTIFIC_TOLERANCE;
  alternatives 0.05/0.20) in BOTH sexes, plus the completeness floor.
- IQR pin: numpy.quantile(., 0.25/0.75, method="linear"); median pin:
  numpy.median. Linear-width rationale: all supports are ratified linear
  intervals; linear width adds no transform choice (owner interpretive
  choice).
- P04 scalar: max over sexes of median s_stab; tolerance tau_5.

### C6 — parsimony
- scientific_role: v11 criterion 6 [V11_LITERAL role]; structural under the
  closed candidate set.
- exact statistic: parameter count k_F = 4 for both families
  [FROZEN_F2_INPUT]; direction lower.
- benchmark reference: df_spline = 8 = the nominal 8-basis count of the
  D-P03-4 clamped knot vector.
- threshold_derivation_type = absolute_structural; no owner literal beyond
  the D-P03-4 df; no measurement-derived quantity.
- exact pass/fail: pass iff (k_F = 4) <= (df_spline = 8); both candidates
  pass by construction.
- undefined behavior: impossible (counts frozen).
- D-P03-7: not applicable (no valid-set restriction) — recorded explicitly.
- P04 scalar: k_F with tau_6 = 0 (exact); decisive only if the counts ever
  differ, which they do not under the closed set — C6 therefore cannot select
  a winner and is retained transparently as the last lexicographic level.

## 4. D-P03-3 — literal inventory (updated for r2)

As in r1 §9 with these additions/changes (classifications per v6 §12):
`c_complete = 0.90` OWNER_SCIENTIFIC_TOLERANCE; `delta_4_RMSE = 0.10`,
`tau_4b_RMSE = 0.02` OWNER_SCIENTIFIC_TOLERANCE (RMSE units);
`reference_active_set_identification_tol = 1e-8`,
`postpolish_primary_active_set_tol = 1e-8`, `postpolish_expansion_tol = 1e-6`,
`spline_kkt_stationarity_tol = 1e-8`,
`spline_feasibility_acceptance_tol = 1e-8`, `kappa_solver = 0.1`
IMPLEMENTATION_TOLERANCE; C4 aggregation rule (AGG-L1-WORSE recommended) =
PI-owned interpretive choice; E = 15, K = 5, g = 0, fold rule, spline
degree/knots/basis/mode set STRUCTURAL_LITERAL; spline-relative threshold
values MEASUREMENT_DERIVED_THRESHOLD = NOT_COMPUTED. All r1 rationales carry
forward; no candidate measurement justified any literal.

## 5. D-P03-4 — spline benchmark + solver pin (r1 content + SOLVER-B exactness cleanup)

All of r1 §2 carries forward unchanged: role adequacy_benchmark_only (never a
generator, winner_eligible = false, R-REV/P-27 untouched); degree-3 clamped
B-spline, knots [0,0,0,0, 0.2,0.4,0.6,0.8, 1,1,1,1], 8 basis functions,
frozen 146-point u-grid; grid-unimodality over mode_idx in {0..145} imposed
on the FULL grid for every fit (masked fits included); objective
RSS_spline_O(c) = sum_{t in O}(z_t − (Bc)_t)^2 (convex inequality-constrained
LS); metric-facing prediction z_ddof0(Bc, full grid); zero-variance/non-finite
⇒ spline_fit_status = FAILURE → D-P03-7; order-independent mode selection
(global RSS_min, equivalent set by |ΔRSS| <= 1e-12 + 1e-9·max, winner = min
mode_idx); determinism claim semantic-only.

**Exact solver pin (code-true; matches the accepted schema-safe r2
qualification bundle — harness `b31e5a6b…`, manifest `e71ce030…`):**

```text
SOLVER-B, per mode_idx:
stage 0  trust-constr primary: gtol=1e-10, xtol=1e-14, barrier_tol=1e-12,
         maxiter=1000; endpoint c_tc delivered to stage 1 unconditionally
         (the polish consumes c_tc only through active-set identification)
stage 1  equality-KKT polish on rows {i : |(A c_tc)_i| <=
         postpolish_primary_active_set_tol = 1e-8}
stage 2  equality-KKT polish on rows {i : |(A c_tc)_i| <=
         postpolish_expansion_tol = 1e-6}   # re-identified from c_tc
stage 3  SLSQP (ftol=1e-12, maxiter=500) from x0 = the 8-dim zero vector
         (feasible origin)

accept(c) := max(0, -min(A c)) <= spline_feasibility_acceptance_tol (1e-8)
             AND min_{lambda>=0} ||A_active(c)^T lambda − grad f(c)||_2
                 <= spline_kkt_stationarity_tol (1e-8),
                 A_active(c) = rows with |A c| <= 1e-8
             AND all coordinates finite

expansion_trigger = NOT accept(stage-1 point) AND expansion not yet attempted
stage-3 trigger   = NOT accept(stage-2 point)
stage-3 acceptance = SLSQP success flag AND finite endpoint/objective AND
                     max_violation <= 1e-8   (KKT term not applied to the
                     fallback endpoint — implementation pin, code-true)
mode invalid      = stage-3 acceptance fails; excluded from
                    equivalent_mode_set; no valid mode =>
                    spline_fit_status = FAILURE

reference_active_set_identification_tol = 1e-8 (reference certification only;
the 1e-6 expansion never applies to reference certification)
```

Label (ADDENDUM A.9): spline trust-constr options (gtol=1e-10, xtol=1e-14,
barrier_tol=1e-12, maxiter=1000) are a spline-only F3 pin; they are not
inherited from and do not alter the frozen F2 P-01/P-02 optimizer literals.

Qualification provenance (reference-only r3 update):

```text
qualification_basis =
schema-safe r2 synthetic solver qualification bundle

r2_manifest_sha256 =
e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32

r2_harness_sha256 =
b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d

r2_results_sha256 =
ffda04b01abb1dd5399e7fb6434c006616723bf6ba7d95bfc697baeb6dd40484

SOLVER_A_EXTERNAL_ACCEPTANCE = PASS
SOLVER_B_EXTERNAL_ACCEPTANCE = PASS
SOLVER_C_EXTERNAL_ACCEPTANCE = FAIL

synthetic_solver_qualification_external_independent_acceptance = PASS

original qualification bundle =
HISTORICAL_SUPERSEDED_FOR_EXTERNAL_ACCEPTANCE_ONLY
(manifest 522d3508... ; harness ecda07d0... — retained as provenance,
 not deleted)
```

SOLVER-A remains the qualified bounded alternative; SOLVER-C remains
eliminated; SOLVER-D not needed. PI_action = ACCEPT / MODIFY.

## 6. D-P03-5 — consolidated C4 row

The complete C4 contract is §3-C4 above (probe construction, C4a exact
fields, A.5 edge rule, C4b chain, gate-status and AGG-L1 PI choices,
disclosure). PI_action = ACCEPT / MODIFY.

## 7. D-P03-6 — WC-ALC scope (unchanged from r1)

Recommended 6A: F3 adequacy claim is relative to the frozen
WC-ALC/shape-constrained benchmark architecture; NOT a universal WC-ALC
membership test; ALL 906 trajectories remain represented in C1–C6 aggregation
(C1 full denominator; valid sets + completeness gates elsewhere; no
morphology screen exists); silent_multiwave_exclusion = forbidden;
R-REV/P-27 untouched. Bounded alternative 6B: diagnostic unconstrained
low-df spline reference, report-only (fully specified in r1 §3, carried
forward). Genuine PI scientific choice. PI_action = ACCEPT / MODIFY.

## 8. D-P05 — cross-fit scheme (unchanged from r1, incl. v6 corrections)

Within-trajectory contiguous folds; K=5; fold boundaries [0,29,58,87,116,146]
⇒ sizes 29/29/29/29/30, folds [0,29) [29,58) [58,87) [87,116) [116,146);
g=0 STRUCTURAL_LITERAL with the v6 §6.0A binding rationale (no
leakage-cancellation claim; no dependence-free claim; g_sens = PI option,
report-only, default NOT_INCLUDED); masked objective
L_O(theta) = sum_{t in O}(z_t − ghat_t(theta))^2 with ghat always full-grid
z_ddof0 (no correlation shortcut; L = 2T(1−rho) is full-grid-only);
L_INVALID_PREDICTION_GUARD = 585 justified by L_O <= full_grid_L <= 584;
observed-only feature start j_star_O = min{j in O : x_j = max_{k in O} x_k},
u_star_O = j_star_O/145, frozen D-F2-09.5 constants unchanged
(22.577778941738334; 0.32057672965544004; sqrt(6); ±1/8), invalid ⇒
FEATURE_START_REJECTED, no clipping [FROZEN_F2_INPUT]; masks change the
objective only — Kural T/S and admissibility on the full stabilized grid
(v6 §6.3A); crossfit-complete = 5/5 folds; rng_used = false; semantic
determinism only. C2 claim boundary per §3-C2. PI_action = ACCEPT / MODIFY.

## 9. D-P04 — deterministic tie-break (r1 + exactness corrections)

Invocation only when BOTH families pass every required P03 gate (per §3, incl.
completeness floors); exactly one passes ⇒ selected without tie-break; none ⇒
STOP, action = redesign [V11_LITERAL]. Lexicographic in the frozen order
C1 → C2 → C3 → C4a → C4b → C5 → C6 with worse-sex scalars as pinned per
criterion in §3; equivalence tolerances tau_1 = 0.01, tau_2 = 0.005,
tau_3 = 0.01, tau_4a = 0.01, tau_4b_RMSE = 0.02, tau_5 = 0.01, tau_6 = 0;
|delta| <= tau ⇒ next criterion, else the better family wins and the
procedure terminates. NONCOMPARABLE-skip does not exist: an undefined
required quantity means the family did not pass P03 (§8.1) and the BOTH-PASS
domain was never entered; only pre-frozen STRUCTURALLY_NOT_APPLICABLE
sub-statistics (declared set: EMPTY; plus the 4b sub-level if the PI selects
C4b_status = REPORT_ONLY — a pre-frozen structural removal, not an outcome
decision) are omitted. Terminal deterministic neutral fallback: ascending
family-ID order "P-01" < "P-02", only after all scientific comparisons remain
equivalent; legacy-neutral; no Ward+CH privilege [V11_LITERAL constraints].
PI_action = ACCEPT / MODIFY.

## 10. Ratification table

| decision_id | final_exact_recommendation | bounded_alternative_set | PI_action |
|---|---|---|---|
| D-P03-1 | §3 six standalone contracts | per-criterion substitutions | ACCEPT / MODIFY |
| D-P03-2 | sex_specific, both-pass | pooled-906; single-sex | ACCEPT / MODIFY |
| D-P03-3 | §4 inventory | per-literal alternatives | ACCEPT / MODIFY |
| D-P03-4 | §5 spline + SOLVER-B pin | SOLVER-A; df 6/10 | ACCEPT / MODIFY |
| D-P03-5 | §3-C4: C4b_status = P03_GATE; AGG-L1-WORSE; A.5 edge rule | REPORT_ONLY; AGG-L1-SEPARATE / AGG-L1-MEAN | ACCEPT / MODIFY |
| D-P03-6 | 6A within-WC-ALC claim | 6B diagnostic reference | ACCEPT / MODIFY |
| D-P03-7 | Option A + c_complete = 0.90 (new owner literal) | Option B; reuse c_cov | ACCEPT / MODIFY |
| D-P04 | §9 lexicographic rule | T-B composite (rejected); tau alternatives | ACCEPT / MODIFY |
| D-P05 | §8 scheme | K = 10; g_sens PI option | ACCEPT / MODIFY |

main_risk (D-P03-5 row, binding wording): C4b = functional identifiability
under simulated censoring (probe fit vs the family's own full-data fit on the
masked edge). It does not measure edge accuracy, morphology fit / WC-ALC
membership, or parameter-space instability, and it is blind by design to
common-mode misspecification.

No PI acceptance is claimed. P03_threshold_values = NOT_COMPUTED. No
candidate-specific result exists.
