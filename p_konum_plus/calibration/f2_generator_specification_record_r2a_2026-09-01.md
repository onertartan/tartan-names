# ART-F2 — Generator Specification Record (F2) — r2a STEP-1.5 CLASS_C + TRANSCRIPTION CORRECTION

## 0. Artifact identity / lineage

```text
artifact_id                     = ART-F2
record_revision                  = r2a_step1_5_class_c_transcription_correction_2026-09-01
parent_record                    = ART-F2 r2
parent_sha256                    = d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4
scientific_parent_ratification   = unchanged_from_r2
PI_re_ratification_required      = false
correction_scope                 = A0_A1_A2_A3_A4_A5_only

F2_STEP_1_complete   = true
F2_STEP_1_5_complete = true
F2_STEP_2            = false
F2_complete          = false
F3_allowed           = false

worktree / branch / HEAD = G:/PycharmProjects/pkp-worktree · p_konum_plus ·
                            3e4daf47018f124e29717263e4e45fe90c8e52b8
date                      = 2026-09-01
```

r2 is not overwritten and remains at its own hash. This is a new child
revision. No self-hash is stored inside this file; no `.sha256` sidecar is
created (F12-only).

**Scope discipline (binding statement):** this is a narrow STEP-1.5
transcription/CLASS_C correction pass only. It does **not** reopen or modify
D-F2-01..D-F2-07, D-F2-09.1..09.10, D-F2-10 scientific semantics, D-F2-11,
D-F2-12, Kural T, Kural S, the P-01/P-02 formulas, parameter bounds,
initialization lattices, the feature-start rule, or the candidate set. All
such content in ART-F2 r2 is incorporated here **by reference and
unchanged**; only §§4–9 below (A0–A5) modify or add text relative to r2.
Everywhere r2 is silent on an A0–A5 item, r2's content governs.

### Governing hashes (recomputed this task, all exact)

| document | SHA256 |
|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` |
| ART-F2 r2 (parent) | `d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4` |
| ART-F2 r1 (grandparent lineage, unchanged) | `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7` |
| PI ratification-ready worksheet FINAL_v2 (lineage, unchanged) | `803e9f30fa84b6c02c34a517525e6c246edf7be4db684e72a2ea8c970f9b38f5` |
| D-F2-09 exact packet (lineage, unchanged) | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` |
| D-F2-09 start-grid manifest (lineage, unchanged) | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` |
| ART-F0 | `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` |
| ART-F1 r4a (FINAL) | `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0` |
| F1 eligible manifest | `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` |
| F1 input hash table | `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac` |

`v11_wins = true`.

---

## 1. Incorporated-by-reference r2 content (unchanged)

Sections 1–8 (F2 normative constraints; evidence/search auditability +
reconciliation record; D-F2-01 name provenance; D-F2-02/D-F2-03 common
interface; D-F2-04 P-01 exact spec; D-F2-05 P-02 exact spec; D-F2-06/D-F2-07
bounds + Kural T/S), and sections 11–15 (identifiability/censoring audit;
spline registration §13/D-F2-12; D-F2-11 second-pass scope; firewall) of
ART-F2 r2 are incorporated here unchanged and are not restated. Only §9 (the
optimizer/coupled-constraint contract) and §10 (D-F2-10 failure semantics)
and §12 (pin schema) of r2 are amended below, per A0–A5.

---

## 2. A0 — Restored D-F2-08 exact fit objective

r2's pin table (§12/P-CMN.3) marked D-F2-08 `PI_RATIFIED` but the objective
definition itself was omitted from the body of r2. This is a transcription
restoration only — the objective was already ratified (worksheet D-F2-08);
no new decision is made here.

```text
D-F2-08_status = PI_RATIFIED

x            = current frozen trajectory after ART-F1 row z-normalization
ghat(theta)  = z_ddof0( g(u_grid; theta) )
T            = 146

L(theta)           = sum_{j=0}^{145} [x_j - ghat_j(theta)]^2
objective_direction = argmin_theta L(theta)
weighting            = unweighted
estimand_space       = frozen_z_space
```

Explanatory identity (not a separate objective; because `x` and `ghat` are
both population-z-standardized on the same 146-point grid):

```text
rho(x, ghat) = (1/T) * sum_j x_j * ghat_j
L(theta)      = 2*T*(1 - rho(x, ghat))
```

Therefore unweighted least-squares minimization is exactly equivalent to
Pearson-correlation maximization, for valid nonconstant predictions. This
identity is explanatory only — the implementation objective is, and remains,
the explicit LS formula above. No robust loss, weighted loss, cosine loss, or
any other objective is substituted; the fit estimand is unchanged from r2.

---

## 3. A1 — Corrected optimizer-feasibility semantics

### 3.1 Solver options (`constr_viol_tol` removed from trust-constr)

r2 listed `constr_viol_tol = 1e-8` among the primary `trust-constr` solver
options; this was incorrect (`trust-constr` does not accept that option
name). Corrected — the executable primary solver options are exactly:

```text
method      = trust-constr
jac         = '2-point'
hess        = BFGS()
gtol        = 1e-10
xtol        = 1e-12
barrier_tol = 1e-10
maxiter     = 500
```

`constr_viol_tol` is NOT passed as a `trust-constr` solver option anywhere in
this contract. Fallback SLSQP options are unchanged from r2: `ftol = 1e-12`,
`maxiter = 500`. No other optimizer literal is changed by this task.

### 3.2 Post-return numerical feasibility tolerance (replaces the removed option)

```text
feasibility_acceptance_tol = 1e-8
status                     = CLASS_C_POST_RETURN_ACCEPTANCE_TOLERANCE
semantics                  = numerical representation tolerance for the
                             optimizer's closed constraints only; it is NOT a
                             morphology threshold, does NOT authorize
                             clipping/projection, and does NOT replace Kural
                             T/S or any other scientific admissibility rule
```

Generic box violation:

```text
V_box(theta; lower, upper) = max_i { max(lower_i - theta_i, 0), max(theta_i - upper_i, 0) }
```

Per-family violation (evaluated manually and identically for endpoints
returned by either optimizer):

```text
V_P01(theta) = max( V_box(theta; [-1,-1,k_min,k_min], [2,2,k_max,k_max]),
                     max(c_r - c_d, 0) )

V_P02(theta) = max( V_box(theta; [-1,0,0,1], [2,3,3,6]),
                     max(s_side_min(beta) - s_l, 0),
                     max(s_side_min(beta) - s_r, 0) )
```

Numerical endpoint-feasibility rule:

```text
endpoint_numerically_feasible = finite(theta) AND V_family(theta) <= feasibility_acceptance_tol
```

The optimizer's own internal constraint-violation diagnostic may be logged
as telemetry but does not substitute for this explicit post-return
calculation. Scientific Kural T/S admissibility remains evaluated separately
under the unchanged D-F2-10 contract (r2 §10).

**Unit-verified this task (model-only, hand-written tuples, §12):** P-01
boundary point `(0.5,0.5,4.0,4.0)` → `V=0.0` (feasible); `(1.0,0.5,20,20)`
(`c_r>c_d`) → `V=0.5` (infeasible). P-02 boundary point at
`s=s_side_min(beta)` → `V=0.0` (feasible); `s_l` below `s_side_min(beta)` →
`V>0` (infeasible). Confirms boundary-exact D-F2-09 starts remain
numerically feasible under this rule, consistent with the r2 §9 rationale
for using a native constrained formulation (not a boundary-excluding
reparameterization).

---

## 4. A2 — Exact multistart aggregation

Per deterministic start in the already-ratified D-F2-09 start bank (r2 §8;
unchanged):

```text
1. run the primary optimizer;
2. apply the already-ratified per-start fallback rule (r2 §9.4) only when its
   existing pure-numerical-error trigger fires;
3. obtain at most one terminal endpoint for that start;
4. evaluate the endpoint under the full hard-failure/admissibility contract.
```

Kural S is an observed-grid endpoint admissibility rule (r2 §7.1) — it is
**not** required to hold at every intermediate optimizer iterate, only at the
terminal endpoint.

```text
eligible_endpoint =
    optimizer_returned_endpoint
    AND endpoint_numerically_feasible          (§3.2, this document)
    AND objective_finite
    AND prediction_finite
    AND NOT ZERO_VARIANCE_FIT                  (§5, this document)
    AND Kural_T_pass
    AND Kural_S_pass
    AND no_other_emittable_hard_failure_predicate_true
```

All applicable hard-failure predicates remain simultaneously logged
(unchanged from r2 §10). For a given trajectory and family:

```text
E = set of all eligible endpoints obtained from the full deterministic
    multistart bank (731 P-01 grid starts + feature start, or 261 P-02 grid
    starts + feature start, per r2 §8/D-F2-09.10)
```

If `E` is nonempty:

```text
family_fit = argmin_{theta in E} L(theta)
```

Objective ties use the already-frozen D-F2-09.9 comparator (unchanged):

```text
tie iff |L_a - L_b| <= 1e-12 + 1e-9*max(|L_a|,|L_b|)
winner among tied eligible endpoints = lexicographically smallest canonical
                                        parameter tuple (r2 D-F2-09.8 order)
```

If `E` is empty:

```text
family_fit             = FAMILY_FIT_FAILURE
family_failure_summary = NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART
```

`NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART` is a deterministic
family-level SUMMARY LABEL — **not a new scientific hard-failure predicate**.
Every start-level failure code / predicate / optimizer diagnostic is retained
regardless. A lower-objective endpoint that fails any hard admissibility
predicate is never chosen over an eligible one. The D-F2-09 start bank itself
is not changed by this aggregation rule.

**Unit-tested this task (fabricated endpoint records, no real data, §12):**
all-ineligible set → `FAMILY_FIT_FAILURE` /
`NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART`; one clear best among
eligible endpoints selected correctly; tie among eligible endpoints resolved
to the lexicographically smallest tuple; a lower-`L` but INELIGIBLE endpoint
correctly excluded in favor of the best eligible one.

---

## 5. A3 — Frozen `epsilon_model`

Closes the previously deferred CLASS_C literal for `ZERO_VARIANCE_FIT`. The
stabilized pre-z latent curve is positively rescaled so its maximum is 1
under the existing stable-evaluation rule (r2 §5/§6, unchanged).

```text
epsilon_model         = 1e-12
epsilon_model_status  = CLASS_C_NUMERICAL_GUARD

variance_statistic: sigma_g = std(g_stable, ddof=0)
comparison:          sigma_g <= epsilon_model
```

Exact rule:

```text
if g_stable contains any nonfinite value:
    NONFINITE_FIT
else:
    sigma_g = std(g_stable, ddof=0)
    if sigma_g <= 1e-12:
        ZERO_VARIANCE_FIT
        do not z-normalize
    else:
        ghat = (g_stable - mean(g_stable)) / sigma_g
```

This threshold is a numerical guard on an already max-normalized curve — it
is NOT a morphology threshold, NOT an F3 adequacy threshold, and NOT a new
scientific parameter-domain restriction.

A-priori numerical rationale:

```text
g_stable_max              = 1
float64_machine_epsilon    ~= 2.220446049250313e-16
epsilon_model = 1e-12       ~= 4.5e3 * machine_epsilon on the unit scale
```

Purpose: block z-normalization only when the stabilized pre-z curve has
insufficient floating-point dynamic range. This threshold is NOT increased
from raw-curve "near-flatness" arguments — the scientific prediction is
`z(g)`, so a very small pre-z amplitude can still encode a distinct
standardized shape. `epsilon_model` was NOT chosen by any morphology-margin
or Kural-S pass/fail analysis. It must not be tuned using synthetic fixture
outcomes in STEP 2; any future proposal to change it is a separate
numerical-conditioning review and may not be silently changed during STEP 2.

**Unit-verified this task (hand-written vectors, §12):** nonconstant vector
(`std ≈ 0.334`) → `OK`, z-normalized; exactly constant vector (`std = 0`) →
`ZERO_VARIANCE_FIT`; near-constant vector (`std ≈ 7.1e-15 < 1e-12`) →
`ZERO_VARIANCE_FIT`; vector containing `NaN` → `NONFINITE_FIT` (checked
before the variance statistic is computed). No STOP triggered — implementing
this literal did not require changing any ratified scientific admissibility
semantics.

---

## 6. A4 — Reserved hard-failure triggers for boundary / identifiability

No new owner-level exclusion threshold is invented in STEP 1.5 or (by this
freeze) in STEP 2. Until a separately authorized exact hard predicate exists:

```text
BOUNDARY_PATHOLOGY_status      = RESERVED_NOT_EMITTED_IN_STEP2
IDENTIFIABILITY_FAILURE_status = RESERVED_NOT_EMITTED_IN_STEP2

WARN_BOUNDARY_status       = RESERVED_NOT_EMITTED_IN_STEP2_UNTIL_TRIGGER_PINNED
WARN_IDENTIFIABILITY_status = RESERVED_NOT_EMITTED_IN_STEP2_UNTIL_TRIGGER_PINNED
```

STEP 2 may record raw, threshold-free diagnostics already implied by the
optimizer/domain contract — e.g. `minimum_box_or_constraint_slack`,
`optimizer_reported_constraint_violation`, optimizer termination/status
diagnostics — but no Hessian-condition-number threshold, boundary-distance
threshold, or any other new identifiability/boundary cutoff may be
introduced in STEP 2. These raw diagnostics never make an otherwise
admissible endpoint fail. All other existing hard-failure predicates
(`NONFINITE_INPUT`, `INVALID_INITIALIZATION`, `NONFINITE_PARAMETER`,
`NONFINITE_FIT`, `ZERO_VARIANCE_FIT`, `MORPHOLOGY_INADMISSIBLE`,
`OPTIMIZER_NONCONVERGENCE`, `OTHER_PREDECLARED_NUMERICAL_FAILURE`) are
unchanged. This is not a deletion of taxonomy or warning labels — it
prevents unowned hard-failure/warning thresholds from being invented during
feasibility execution while preserving raw audit telemetry.

---

## 7. A5 — Repaired single-valued pin status + reporting precedence

r2's `P-CMN.7` pin record mixed a `PI_RATIFIED` scientific-semantics status
with a `CLASS_C` precedence status under one entry. Split into two
single-valued records:

```text
P-CMN.7a
  component = failure taxonomy + scientific admissibility semantics
  status    = PI_RATIFIED

P-CMN.7b
  component = primary hard-failure display precedence
  status    = CLASS_C_IMPLEMENTATION_PIN
```

Deterministic display ordering (reporting only):

```text
1  NONFINITE_INPUT
2  INVALID_INITIALIZATION
3  NONFINITE_PARAMETER
4  NONFINITE_FIT
5  ZERO_VARIANCE_FIT
6  MORPHOLOGY_INADMISSIBLE
7  OPTIMIZER_NONCONVERGENCE
8  OTHER_PREDECLARED_NUMERICAL_FAILURE
9  BOUNDARY_PATHOLOGY
10 IDENTIFIABILITY_FAILURE
```

```text
all applicable hard predicates are still logged simultaneously
primary_display_code            = first emitted code in the fixed ordering above
display precedence changes admissibility = false
BOUNDARY_PATHOLOGY and IDENTIFIABILITY_FAILURE = not emitted in STEP 2 under A4
```

The ordering is reporting-only and never changes endpoint eligibility (§4
governs eligibility exclusively).

### Updated pin table (r2 §12, corrected; all other rows unchanged from r2)

| pin_id | component | status |
|---|---|---|
| P-CMN.1 | time coordinate (D-F2-02) | PI_RATIFIED |
| P-CMN.2 | prediction operator, no amplitude/offset (D-F2-03) | PI_RATIFIED |
| P-CMN.3 | fit objective (D-F2-08; now restored in full, §2) | PI_RATIFIED |
| P-01.1 | exact formula (D-F2-04) | PI_RATIFIED |
| P-01.2 | bounds + Kural T/S (D-F2-06) | PI_RATIFIED |
| P-01.3 | initialization D-F2-09.1/.2/.5/.6/.7 | PI_RATIFIED |
| P-01.4 | constraint parameterization / optimizer (r2 §9, corrected §3 this doc) | CLASS_C_IMPLEMENTATION_PIN |
| P-02.1 | exact formula (D-F2-05) | PI_RATIFIED |
| P-02.2 | bounds + Kural T/S (D-F2-07) | PI_RATIFIED |
| P-02.3 | initialization D-F2-09.3/.4/.5/.6/.7 | PI_RATIFIED |
| P-02.4 | constraint parameterization / optimizer (r2 §9, corrected §3 this doc) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.4 | dedup/order (D-F2-09.8) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.5 | objective tie (D-F2-09.9) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.6 | k_max, s_side_min(beta), start counts | DERIVED_FROM_RATIFIED_RULE |
| P-CMN.7a | failure taxonomy + scientific admissibility semantics | PI_RATIFIED |
| P-CMN.7b | primary hard-failure display precedence | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.8 | multistart aggregation rule (§4, this doc) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.9 | epsilon_model (§5, this doc) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.10 | reserved BOUNDARY_PATHOLOGY / IDENTIFIABILITY_FAILURE status (§6, this doc) | RESERVED_NOT_EMITTED_IN_STEP2 |

Every status field above is single-valued; no row carries two statuses.

---

## 8. Intentionally excluded items (unchanged from correction-prompt §9A)

The following are intentionally NOT added in STEP 1.5: `[-1,2]`
location-horizon counterexample re-justification; D-F2-09 grid-coverage
adequacy testing; historical custody-path timeline cleanup. Closed scientific
decisions are not reopened without a material contradiction; grid adequacy is
not a STEP-2 objective-attainment question; custody-path chronology is
non-blocking provenance cleanup. No A6/A7/A8 are created.

---

## 9. STEP-1.5 internal consistency checks (executed this task; static/unit-level only)

```text
parse/document-search check: `constr_viol_tol` absent from the trust-constr
  option list in §3.1 of this document                              -> CONFIRMED ABSENT
document-search check: D-F2-08 exact objective now present (§2)      -> CONFIRMED PRESENT
unit evaluation of V_P01 on hand-written tuples (feasible interior,
  feasible boundary, c_r>c_d violation, out-of-box violation)        -> PASS (§3.2)
unit evaluation of V_P02 on hand-written tuples (feasible boundary at
  s_side_min(beta), interior feasible, s_l below s_side_min(beta)
  violation, beta-out-of-range violation)                            -> PASS (§3.2)
unit evaluation of epsilon_model rule on hand-written vectors
  (nonconstant / exactly-constant / near-constant / nonfinite)        -> PASS (§5)
unit test of multistart aggregation on fabricated endpoint records
  (all-ineligible, one-clear-best, tie, lower-L-but-ineligible)       -> PASS (§4)
unit test of D-F2-09.9 tie comparator (embedded in aggregation test)  -> PASS (§4)
pin-table schema check for single-valued statuses (§7 table)          -> PASS — every
  row has exactly one status value
```

No fixture result was used to tune `epsilon_model`, `feasibility_acceptance_tol`,
or any scientific parameter — all constants above were fixed BEFORE the unit
checks were run, and the checks only confirm the predeclared rules classify
the hand-written fixtures as expected.

**Forbidden and NOT performed:** synthetic feasibility suite execution; any
fit to a real SSA trajectory or subset; P-01 vs P-02 comparison; any
recovery score/rate/pass-fail; any objective-attainment success rate; P-03
derivation/tuning; generator selection; F3 execution.

---

## 10. Firewall / gate status

```text
ART_F2_r2_unchanged   = true
ART_F2_r2a_created    = true

A0_closed = true
A1_closed = true
A2_closed = true
A3_closed = true
A4_closed = true
A5_closed = true

PI_re_ratification = false

F2_STEP_1_complete   = true
F2_STEP_1_5_complete = true
F2_STEP_2            = false
F2_complete          = false
F3_allowed           = false

real_SSA_fit = false | real_SSA_subset_fit = false
generator_adequacy_comparison = false | generator_selection = false
algorithm_CVI_execution = false | algorithm_CVI_outcome_access = false
legacy_performance_content_access = false
P03_touched = false | P04_touched = false | P05_touched = false
F3_started = false | F4_started = false

next_action = independent narrow audit of ART-F2 r2a
```
