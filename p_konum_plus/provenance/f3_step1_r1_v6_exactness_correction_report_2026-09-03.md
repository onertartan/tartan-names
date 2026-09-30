# p_konum_plus — F3 STEP 1 r1 (v6) Exactness Correction Report

```text
artifact_role = narrow-correction execution report (Output 1 of the 2026-09-03
                narrow exactness correction task + ADDENDUM A r1)
status        = NON-NORMATIVE
date          = 2026-09-03

scope = ONLY F3-STEP1-EXACT-01, F3-STEP1-EXACT-02, SOLVER-B exactness cleanup
scientific_change = false, EXCEPT that the C4 aggregation/gate-status
  recommendation (C4b_status, AGG-L1 rule) is a genuine PI-owned
  scientific/interpretive choice, proposed — not frozen — here
F2_change = false
F2_reopening = false
new_methodology_review = false
real_SSA_execution = false
synthetic_qualification_rerun = false
commit = false
```

Instruction precedence applied as dispatched: base prompt
(`b0d55ba036cc4a87bc10ae42cbc01ae6b6f0f5200a743c3c297e5ad4018c1c34`)
+ ADDENDUM A r1 = sole instruction source; the independent audit verdict
(`b98e85ed6b96e3d7d9e9e0ca854eaf5ef4e63fa6b09f0242748b1a5adfe309ee`)
was used as read-only provenance only.

## 1. Custody verification (base §1 + ADDENDUM A.1 / GUARD_1)

All computed on the actual files; every value exact; no STOP.

| artifact | expected | actual | result |
|---|---|---|---|
| v11 FINAL NORMATIVE | `d136502f…` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | PASS |
| F2 FINAL FREEZE r1 | `ee2cb99d…` | `ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43` | PASS |
| v6 governing prompt | `418092db…` | `418092db19773d870e5bffa888895276c2ff7e58ad78b4b4590293a684d9750a` | PASS |
| r1 corrected candidate | `6e7b5634…` | `6e7b56348f9a1ffe144d776b48bc559baf2cbf71fb02c84ff37cba11203992c6` | PASS |
| independent audit verdict | `b98e85ed…` | `b98e85ed6b96e3d7d9e9e0ca854eaf5ef4e63fa6b09f0242748b1a5adfe309ee` | PASS |
| **GUARD_1** prior STEP-1 packet `p_konum_plus/provenance/f3_step1_decision_packet_endoftask_report_2026-09-02.md` | `143651a7ee1d0bc3b738057b4e0c8aa28253ace6c1432115e64e2c190a279c17` | `143651a7ee1d0bc3b738057b4e0c8aa28253ace6c1432115e64e2c190a279c17` | PASS — line anchors 39/42/45/58 valid |
| base prompt (addendum binding) | `b0d55ba0…` | `b0d55ba036cc4a87bc10ae42cbc01ae6b6f0f5200a743c3c297e5ad4018c1c34` | PASS |

Repo state: HEAD `3e4daf47018f124e29717263e4e45fe90c8e52b8`, branch `p_konum_plus`,
no tracked modifications.

## 2. ADDENDUM A.2 — expansion literal predeclaration

```text
expansion_literal_in_hashed_manifest = true
```

Verbatim fields from the hashed manifest
(`522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883`,
present identically in every fixture row):

- column `active_set_expansion_tol` = `1e-06`
- column `tested_solver_configurations` contains, verbatim:
  `SOLVER-B(trust-constr primary; active-set equality-KKT post-polish tol 1e-8
  with single expansion to 1e-6; SLSQP fallback)`
- column `active_set_identification_tol` = `1e-08`;
  `spline_kkt_stationarity_tol` = `1e-08`;
  `spline_feasibility_acceptance_tol` = `1e-08`

The expansion tolerance AND its trigger rule (single expansion, positioned
between primary post-polish and SLSQP fallback in the declared stage sequence)
were therefore predeclared in the manifest hashed before execution.

```text
SOLVER-B_claim = REPORTED_PASS
SOLVER-A_claim = REPORTED_PASS   (expansion never used by SOLVER-A)
```

## 3. F3-STEP1-EXACT-01 — C4a/C4b closure (summary; full contract in r2 candidate)

Closed in the r2 candidate with: exact C4a probe-success Boolean, fixed
denominator `2*n_s`, sex-level formula and `c_ident` inequality; the full C4b
chain LEFT/RIGHT -> trajectory -> paired-valid set -> sex-level median ->
spline-relative pass/fail inequality -> P04 scalars; the ADDENDUM A.5
under-mask rule adopted verbatim (probe = C4a failure, numerator excluded,
denominator retained; absent from the C4b paired-valid set; no imputation, no
sentinel); C4b gate status pinned as a bounded PI recommendation
(`C4b_status = P03_GATE` recommended; `REPORT_ONLY` bounded alternative); the
L/R combination drawn ONLY from the ADDENDUM A.4 enumerated set
(recommended `AGG-L1-WORSE`; bounded alternatives `AGG-L1-SEPARATE`,
`AGG-L1-MEAN`; `AGG-L1-POOL` not carried forward as one of the two allowed
alternatives). Per GUARD_2 these are execution-audit scaffolding plus a
PI-owned interpretive choice; nothing is self-ratified; `PI_action` left
unfilled. The ambiguous phrase "C4b's paired-valid set, which is always
reported" is replaced by the exact reporting rule in the r2 candidate.

## 4. F3-STEP1-EXACT-02 — line-anchored C1/C2/C6 restatement (ADDENDUM A.6)

Quotations verified against the byte-identical file `143651a7…` (anchor line =
bold header; contract text on the following line).

**Common fields (lines 39–40), quoted:** "**Common fields (apply to every
criterion unless overridden).** `unit_of_evaluation` = one eligible trajectory,
fitted per family under the unmodified FREEZE r1 contract (all starts, frozen
optimizer, frozen admissibility). `aggregation_unit` = trajectory-level
statistic → **median** across trajectories (pre-declared; robust, no tuning) →
per-sex value. `sex_handling` = **sex_specific**: every criterion is derived
and gated separately for F (n=435) and M (n=471); a family passes a criterion
only if it passes in **both** sexes. […] `missing_or_failed_fit_handling` = a
trajectory with no eligible full-data fit (per frozen taxonomy) counts against
C1 and is excluded from the complete-case sets of C2–C5, with the exclusion
share logged per sex. `family_level_aggregation_rule` = criteria evaluated in
the frozen order C1→C6; first failed criterion ⇒ family FAIL (all six still
measured and logged for provenance). […]"

Superseded elements → replacements:
- "excluded from the complete-case sets … exclusion share logged per sex" →
  **D-P03-7 Option A** (completeness sub-gate `c_complete` + paired-valid
  sets) + **§8.1 failure propagation** (undefined required statistic ⇒
  criterion not passed). Logging alone no longer suffices.
- All other Common-fields elements retained unchanged.

**C1 (lines 42–43), quoted:** "**C1 — morphology coverage.**
`exact_statistic`: coverage_F,s = (# trajectories of sex s with ≥1 eligible
admissible full-data fit under FREEZE r1) / n_s. `direction`: higher.
`reference_distribution`: none needed. `threshold_derivation_type` =
**absolute_structural**. `predeclared_literals`: coverage floor **c_cov =
0.90** (alternatives 0.85 / 0.95). `pass_fail`: coverage_F,s ≥ c_cov in both
sexes. `how_value_computed`: direct share; the floor is the rule literal
itself (no measurement-derived component)."

Superseded elements: none of C1's own content; additions only — explicit
D-P03-7 relationship, explicit non-reinterpretation as a morphology-membership
screen (D-P03-6A boundary), and the P04 scalar. Full standalone restatement in
the r2 candidate.

**C2 (lines 45–46), quoted:** "**C2 — cross-fitted reconstruction / predictive
fit.** `exact_statistic`: ρ_cv,i = Pearson correlation between the frozen F1
z-trajectory z_i and the assembled out-of-sample prediction ĝ_cv,i produced by
the P05 primary scheme (every year predicted exactly once by a fold that did
not train on it). `direction`: higher. `aggregation`: M_F,s = median_i ρ_cv,i
over the complete-case set of sex s. `reference_distribution`: the same
statistic computed for the spline benchmark, M_S,s, under the identical P05
scheme. […] `pass_fail`: M_F,s ≥ M_S,s − δ₂ in both sexes. `failed-fold
handling`: per P05 (trajectory excluded from complete-case set if any fold
invalid; share logged)."

Superseded elements → replacements:
- "failed-fold handling: per P05 (… share logged)" → **D-P03-7 Option A**:
  paired-valid set + completeness floor + §8.1 propagation.
- "complete-case set" (family-specific) → **paired-valid set** (family AND
  spline crossfit-complete on the same trajectories) for the spline-relative
  comparison.
- Added from the audited candidate §4: the binding C2 claim-boundary flags
  (`raw_scale_forecasting_claim = false`,
  `strict_preprocessing_leakage_free_forecasting_claim = false`,
  `temporal_dependence_leakage_free_claim = false`, frozen-F1-z-space
  conditional reconstruction role).

**C6 (lines 58–59), quoted:** "**C6 — parsimony.** `exact_statistic`:
parameter count k_F (= 4 for both families, frozen). `direction`: lower.
`threshold_derivation_type` = **absolute_structural**: pass iff k_F ≤
df_spline (the D-P03-4 literal). `pass_fail`: structural; both candidates pass
by construction (4 ≤ 8). C6 remains in the hierarchy for the P04 comparator,
where it is decisive only if the families' parameter counts ever differ (they
do not, under the closed candidate set — recorded transparently)."

Superseded elements → replacements: exact form pinned as
`pass iff (k_F = 4) <= df_spline = 8` where 8 = the nominal 8-basis count of
the clamped knot vector; P04 scalar = k_F with τ₆ = 0. No other change.

Other supersessions identified (beyond the A.6 known list): prior C3's
spline-relative comparison set and prior C5's "complete-case (all K folds
eligible)" are likewise now governed by D-P03-7 Option A (paired-valid where
spline-relative, completeness-gated where absolute); prior C4 block (lines
51–53: correlation-unit 4b on still-observed years, δ₄ = 0.05 ρ-units) was
already superseded by v6 §7 (RMSE_edge on the masked edge, new RMSE-unit
literals) — recorded, no new finding.

**Prior-packet vs audited-candidate inconsistencies that are NOT already v6
corrections: none found.**

## 5. SOLVER-B exactness cleanup — implemented semantics (from the executed artifacts)

Determined by static inspection of the custody-imported executed harness
(`f3_spline_solver_qualification_harness_2026-09-02.py`,
`ecda07d0fee36d8988c82c31aeb8e231b812e7a4df400af9c6a80676e4cf5917`) and the
hashed manifest; nothing rerun, nothing modified.

Distinct tolerance roles (code-true):

```text
reference_active_set_identification_tol = 1e-8
  (reference() uses ACT_TOL only; the 1e-6 expansion NEVER touches
   reference certification)
postpolish_primary_active_set_tol = 1e-8   (stage-1 polish)
postpolish_expansion_tol          = 1e-6   (stage-2 polish only)
spline_kkt_stationarity_tol       = 1e-8
spline_feasibility_acceptance_tol = 1e-8
```

Exact implemented SOLVER-B stage order (ADDENDUM A.7 template, code wins):

```text
stage 0  c_tc = trust-constr endpoint (gtol=1e-10, xtol=1e-14,
         barrier_tol=1e-12, maxiter=1000); the polish stages consume c_tc
         only through active-set identification, so stage 1 executes
         unconditionally on the delivered endpoint
stage 1  polish(c_tc, postpolish_primary_active_set_tol = 1e-8)
stage 2  polish(c_tc, postpolish_expansion_tol = 1e-6)
         # active set re-identified from the SAME c_tc, not from the
         # stage-1 point
stage 3  SLSQP(ftol=1e-12, maxiter=500) from x0 = the 8-dim zero vector
         (the feasible origin; NOT c_tc, NOT the stage-2 point)

accept(c) :=    max(0, -min(A @ c)) <= 1e-8        # primal feasibility
            AND nnls_kkt_residual(c) <= 1e-8       # NNLS existence at |Ac|<=1e-8 rows
            AND all coordinates finite

expansion_trigger  = NOT accept(stage-1 polished point)
stage-3 trigger    = NOT accept(stage-2 polished point)
stage-3 acceptance = SLSQP success flag AND finite endpoint/objective
                     AND max_violation <= 1e-8
                     (the KKT-existence term is NOT applied to the stage-3
                      fallback endpoint in the executed code)
reject             = stage-3 acceptance also fails => mode_idx numerically
                     invalid; excluded from equivalent_mode_set; no valid
                     mode => spline_fit_status = FAILURE
```

Per A.7's "code wins" rule, the r2 candidate corrects the r1 phrase "fallback
endpoint faces the identical acceptance rule" to the code-true stage-3
acceptance above (**cleanup**, listed below). The stage-3 path was never
exercised in the qualification run (all SOLVER-B endpoints were POLISH or
POLISH_EXPANDED; Q04/Q09 used stage 2), so the delivered qualification results
are fully consistent with one exact interpretation, which the r2 candidate
incorporates as an **implementation pin**:

```text
QUALIFICATION_TEXT_IMPLEMENTATION_MISMATCH = false
```

## 6. Qualification provenance handoff (base §5) — summary

Full inventory in Output 3. Manifest custody verified
(`522d3508…` exact). Manifest-before-execution classification:

```text
SUPPORTED_BUT_NOT_INDEPENDENTLY_PROVABLE_FROM_REPO_ARTIFACTS
```

(the executed harness's control flow writes and hashes the manifest before any
solve, and the hash appears before the case table in the recorded stdout
inside `6e7b5634…`; repository artifacts alone cannot independently prove the
historical temporal ordering). Claim boundary:

```text
spline_solver_qualification_claim = REPORTED_PASS
external_independent_acceptance   = PENDING
```

This report's inspection is NOT an independent acceptance audit.

## 7. v6 §16 audit re-run on the r2 candidate (+ ADDENDUM A.8 V/W)

A NO · B NO · C NO · D NO · E NO · F NO · G NO · H NO · I NO · J NO
(A–J all as expected = NO)
K YES · L YES · L2 YES · L3 YES · M YES · N YES · O YES · P YES · Q YES ·
R YES · S YES · T YES · U YES (K–U all as expected = YES)
V NO (C4b LEFT/RIGHT -> trajectory -> sex chain and gate status are exact in
the r2 candidate; two executors cannot diverge) · W YES (the r2 candidate is
standalone; no unstated contract requires opening `143651a7…`).

## 8. Findings

- **global blocker:** none. **gate-specific blocker:** none remaining
  (F3-STEP1-EXACT-01 and -02 closed by the r2 candidate; SOLVER-B cleanup
  closed).
- **cleanup:** r1 phrase "fallback endpoint faces the identical acceptance
  rule" superseded by the code-true stage-3 acceptance; ambiguous "C4b's
  paired-valid set, which is always reported" phrase replaced; tolerance roles
  split into named literals.
- **informational:** stage-3 SLSQP fallback never exercised in the
  qualification run; no standalone machine-readable case-level telemetry file
  exists (case-level results are hash-anchored inside `6e7b5634…` §1 and were
  not regenerated — rerun forbidden); external independent acceptance of the
  qualification remains PENDING; the executed harness was custody-imported
  byte-identically from its execution location into
  `p_konum_plus/calibration/` (source SHA256 = destination SHA256 =
  `ecda07d0…`) solely to make the audit bundle repository-resident.

## 9. RATIFICATION_READY logic (base §7, 12 conditions)

1 exact ✓ · 2 exact ✓ · 3 standalone C1/C2/C6 (indeed all six) ✓ ·
4 D-P03-7 propagation consistent across C1–C6 ✓ · 5 P04 consumes only defined
scalars ✓ · 6 distinct tolerance roles ✓ · 7 exact Boolean expansion trigger ✓ ·
8 text matches executed implementation ✓ · 9 no real SSA/candidate execution ✓ ·
10 no qualification rerun ✓ · 11 no F2/v11 change ✓ · 12 all PI-owned choices
labelled PI-owned ✓ → `RATIFICATION_READY = true` (candidate-text exactness
only; external independent solver-qualification acceptance remains PENDING and
is not claimed).
