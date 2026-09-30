# ART-F2 — Generator Specification Record (F2) — r2 RATIFICATION

## 0. Artifact identity / revision lineage / governing hashes

```text
artifact_id              = ART-F2
record_revision          = r2_ratification_2026-08-31
parent_record             = ART-F2 r1
parent_sha256              = d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7
record_status             = PI_RATIFIED_STEP1_COMPLETE
normative_authority       = v11_only
gate                      = F2
date                      = 2026-08-31
worktree / branch / HEAD  = G:/PycharmProjects/pkp-worktree · p_konum_plus ·
                            3e4daf47018f124e29717263e4e45fe90c8e52b8

PI_ratification           = true
F2_STEP_1_complete        = true
F2_complete               = false
F3_allowed                = false
```

r1 is not overwritten and remains at its own hash; this file is a new,
separate revision. No self-hash is stored inside this file; no `.sha256`
sidecar is created (F12-only).

### Governing hashes (recomputed this task, all exact)

| document | SHA256 |
|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` |
| ART-F2 r1 (parent) | `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7` |
| PI ratification-ready worksheet FINAL_v2 | `803e9f30fa84b6c02c34a517525e6c246edf7be4db684e72a2ea8c970f9b38f5` |
| D-F2-09 exact packet | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` |
| D-F2-09 proposed start-grid manifest | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` |
| ART-F0 | `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` |
| ART-F1 r4a (FINAL) | `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0` |
| F1 eligible manifest | `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` |
| F1 input hash table | `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac` |

`v11_wins = true`.

### PI ratification statement (source: worksheet §5, transcribed verbatim)

> I RATIFY THE F2 PI SELECTION SET AS WRITTEN IN THE PI RATIFICATION-READY
> FINAL WORKSHEET, INCLUDING D-F2-01 THROUGH D-F2-12, WITH D-F2-09.1–.7 AS
> PI-OWNED INITIALIZATION CONTRACT, D-F2-09.8–.9 AS CLASS_C IMPLEMENTATION
> PINS, AND D-F2-09.10 AS DERIVED_FROM_RATIFIED_RULE. R1–R4 SHALL APPLY IN
> ART-F2 r2. I AUTHORIZE ART-F2 r1 -> r2 CORRECTION/RATIFICATION, BUT F2
> STEP 2 MAY NOT BEGIN UNTIL THE r2 OPTIMIZER/COUPLED-CONSTRAINT CLASS_C
> CONTRACT IS EXACT AND EXECUTABLE.

Received and verified equivalent to the required form in the chat turn dated
2026-08-31 (identifies the FINAL_v2 worksheet by name; includes the D-F2-09
classification, R1–R4 clause, r1→r2 authorization, and the STEP-2 gating
condition). This ratification statement is recorded here as PROVENANCE of
authorization; it does not itself carry normative authority — v11 remains
sole normative source.

---

## 1. F2 normative constraints (unchanged from r1; v11-closed)

```text
candidate_generator_set = {WC-ADL, TAD/PSAT}     # closed; exactly 2
third_primary_generator = forbidden
shape_constrained_low_df_spline_role = adequacy_benchmark_only
automatic_spline_fallback = false
algorithm_CVI_information_in_generator_specification = forbidden
```

F2 freeze object per family: exact formula; parameter bounds; initialization
scheme; deterministic fit-failure handling — all now ratified below. F3
candidate adequacy comparison, thresholds, tie-break, and cross-fit remain
untouched. The frozen ART-F1 r4a input contract is unchanged and unreopened.

---

## 2. Evidence / search auditability + reconciliation-source check record (R2, C2, C3)

### 2.1 Search auditability (C2)

```text
pattern_search_scope   = docs/, protocol/ (legacy v5.3), p_konum_plus/
patterns_searched       = WC-ADL, WC_ADL, WC-ALC, PSAT, TAD, double logistic,
                          generalized gaussian, window-censored
files_opened_full_content = p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
                          p_konum_plus/provenance/nonnormative/ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
                          p_konum_plus/provenance/nonnormative/claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md
pattern-search-only files (matched paths, not opened for scientific content) =
                          p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md
                          p_konum_plus/provenance/calibration_protocol_v0_drafting_report_2026-08-28.md
zero-hit paths          = docs/, legacy protocol/ (no WC-ADL/TAD/PSAT/WC-ALC hits)
legacy_performance_content_access = false   # results/ never opened
```

### 2.2 Reconciliation-source check (R2) — verified this task

```text
source_check_status         = available_and_verified
hash_verification            = exact (both sources, both matched exactly this task)
mathematical_definition_found = false
acronym_expansion_found       = false
material_formula_contradiction = false
opaque_identifier_support     = yes
```

### 2.3 Literature provenance (C3)

Wikipedia consultation (generalized normal distribution; logistic function),
performed during ART-F2 r1 drafting, is recorded as **orientation/discovery
provenance only**. It supports the underlying mathematical construction
(asymmetric generalized Gaussian and logistic-function families being
recognized standard forms) and is NOT used, and must not be used, as
provenance for the TAD/PSAT naming or any acronym expansion. No
peer-reviewed/authoritative methodological source has yet been substituted;
if one is added later it must record title, author/source, URL/DOI,
access_date, and claim_supported.

---

## 3. D-F2-01 — Generator-name and definition provenance (RATIFIED)

```text
P-02_project_identifier      = "TAD/PSAT"
identifier_semantics         = opaque_project_identifier
acronym_expansion            = not_asserted
TAD_vs_PSAT_relation         = not_asserted
WC-ADL_expansion             = not_asserted
project_definition            = D-F2-05 (below) for P-02; D-F2-04 (below) for P-01
candidate_cardinality_effect  = none — exactly 2 primary families
```

(C8) The r1 phrase "one family with dual historical labels" is removed and
replaced by the opaque-identifier semantics above; no historical-label claim
is retained.

---

## 4. Common observation/preprocessing interface — D-F2-02, D-F2-03 (RATIFIED)

```text
time coordinate (D-F2-02)  : u = (t - 1880) / 145,  u in [0,1] on the grid
                              reporting transform: t_year = 1880 + 145*u ; width_year = 145*width_u

prediction operator (D-F2-03) : ghat(theta) = z_ddof0( g(u_grid; theta) )
amplitude                      : omitted
vertical_offset                : omitted
```

Rationale (unchanged from r1, ratified): for any `a > 0` and any `b`,
`z(a*g + b) = z(g)`; amplitude and vertical offset are therefore structurally
unidentifiable under the frozen F1 z-space and are omitted from both
parameter sets rather than retained as nuisance parameters.

**Downstream interface note — explicitly NON-BINDING (C10):** the residual
interface will naturally be expressed in frozen z-space; this is an
observation only and does not freeze F6/F8 noise-law or H* details, which
belong to their owning later gates.

---

## 5. P-01 WC-ADL — ratified exact specification (D-F2-04)

```text
g(u; c_r, c_d, k_r, k_d) = sigma( k_r*(u - c_r) ) * sigma( -k_d*(u - c_d) )
sigma(v) = 1 / (1 + exp(-v))

constraints: c_r <= c_d ; k_r > 0 ; k_d > 0
stable_log_domain_evaluation = required
```

Stable (class-C) evaluation form:

```text
log g       = -softplus( -k_r*(u - c_r) ) - softplus( k_d*(u - c_d) )
log g_stable = log g - max(log g)
g_stable     = exp(log g_stable)
```

This is a positive rescaling and does not change the z-space prediction
(`z(g_stable) = z(g)` under exact arithmetic). Raw `exp()` underflow is NOT a
scientific generator failure (C4; see §10).

```text
peak_location_procedure = deterministic numerical procedure (class-C; does not
                           define F4 regime thresholds)
```

Scientific role (unchanged from r1): rise and decline within one family;
W-L/W-I/W-R observed-window descriptors are generated via latent timing
(`c_r`, `c_d` may lie outside `[0,1]`), not via separate regime generators;
asymmetry via `k_r != k_d`; plateau freedom via `c_d - c_r`.

---

## 6. P-02 TAD/PSAT — ratified exact specification (D-F2-05)

```text
g(u; m, s_l, s_r, beta) =
    exp( -((m - u)/s_l)^beta )   for u <= m
    exp( -((u - m)/s_r)^beta )   for u >  m

constraints: s_l > 0 ; s_r > 0 ; beta >= 1
shared_beta = true   (4 parameters: m, s_l, s_r, beta)
stable_log_domain_evaluation = required
```

Stable (class-C) evaluation form:

```text
ell_j        = branch-specific negative power term
ell_stable_j = ell_j - max_k ell_k
g_stable_j   = exp(ell_stable_j)
```

Positive scalar rescaling: `z(g_stable) = z(g)` under exact arithmetic. Raw
`exp()` underflow is NOT scientific generator failure (C4; see §10).

---

## 7. Parameter-bound ratified tables + Kural T / Kural S (D-F2-06, D-F2-07)

### 7.1 Exact Kural T / Kural S definitions (worksheet §2, transcribed exactly)

```text
KURAL T — abrupt / level-shift guard:
each rise/decline branch's 10-90% transition width must be >= w_min_years

w_min_years = 5

P-01: k_max = 2*ln(9)*145 / w_min_years
P-02: s_side_min(beta) = (w_min_years/145) / ( ln(10)^(1/beta) - ln(10/9)^(1/beta) )
```

```text
KURAL S — impulse / edge-spike guard:
evaluate on the stabilized curve over the observed 146-point grid

n_sup = #{ j : g_j >= g_min + 0.5*(g_max - g_min) }
require: n_sup >= 3
```

```text
Kural_T_role = F2 parameter-domain admissibility
Kural_S_role = F2 parameter-domain admissibility
not_F3_adequacy_threshold = true
not_F4_regime_threshold   = true
MORPHOLOGY_INADMISSIBLE  = violation of ratified Kural T or Kural S
```

### 7.2 P-01 WC-ADL bounds / morphology domain (RATIFIED)

```text
c_r, c_d in [-1, 2] ;  c_r <= c_d
k_min = 4
w_min_years = 5  ->  k_max = 2*ln(9)*145/5 = 127.43902548550072   (R4; see §17)
Kural S: n_min = 3
```

### 7.3 P-02 TAD/PSAT bounds / morphology domain (RATIFIED)

```text
m in [-1, 2]
beta_min = 1
beta_max = 6
strict_latent_peak_C1_required = false
s_max = 3.0
s_side_min(beta) = (5/145) / ( ln(10)^(1/beta) - ln(10/9)^(1/beta) )   (R4; see §17)
Kural T + Kural S apply jointly
```

**(C5) Corrected s_max rationale:** the r1 rationale "large s -> zero
variance demonstrated in §11.4" is removed. §11.4's degenerate case was a
**far-location + small-scale + large-beta corner** producing raw underflow,
not a consequence of a large scale value per se. The correct rationale for
`s_max = 3.0` is: z-space parameter identifiability, standardized-shape
saturation, and weak curvature / weak parameter information at large scales
— i.e. once the branch scale exceeds the observation window by a wide
margin, the in-window segment carries negligible shape information and
further increase is not scientifically distinguishable.

---

## 8. D-F2-09 — exact deterministic initialization contract (RATIFIED)

Governance classification (ratified exactly as stated):

```text
D-F2-09.1..09.7  = PI_OWNED_INITIALIZATION_REPRODUCIBILITY_CONTRACT
D-F2-09.8..09.9  = CLASS_C_IMPLEMENTATION_PINS
D-F2-09.10       = DERIVED_FROM_RATIFIED_RULE

family_definition_altering            = false
fitted_solution_altering_if_changed   = potentially_yes
```

### D-F2-09.1 — P-01 location anchors (PI-owned)

```text
A_loc = { -1 + i/4 : i = 0..12 }
      = { -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00 }

(c_r, c_d) = all ordered pairs (A_i, A_j) with A_i <= A_j
number_of_location_pairs = 91
c_r = c_d allowed = true   (zero-plateau symmetric starts)
```

### D-F2-09.2 — P-01 k starts (PI-owned)

```text
K = { 4, sqrt(4*k_max), k_max } = { 4.0, 22.577778941738334, 127.43902548550072 }
(k_r, k_d) = full K x K   (9 combinations per location pair)
raw_fixed_grid            = 819
retained_after_Kural_S    = 731
```

### D-F2-09.3 — P-02 m / beta starts (PI-owned)

```text
m anchors    = same A_loc (13 anchors)
beta anchors = { 1, sqrt(6), 6 } = { 1.0, 2.449489742783178, 6.0 }
```

### D-F2-09.4 — P-02 scale starts (PI-owned)

```text
S(beta) = { s_side_min(beta), sqrt(s_side_min(beta)*3), 3 }
(s_l, s_r) = full S(beta) x S(beta)
raw_fixed_grid          = 351
retained_after_Kural_S  = 261
```

### D-F2-09.5 — feature-based start (PI-owned)

```text
j_star = min{ j : x_j = max_k x_k }
u_star = j_star / 145

P-01: (c_r, c_d, k_r, k_d) = (u_star - 1/8, u_star + 1/8, 22.577778941738334, 22.577778941738334)
P-02: (m, s_l, s_r, beta)  = (u_star, 0.32057672965544004, 0.32057672965544004, sqrt(6))

if invalid: FEATURE_START_REJECTED ; no clipping ; no substitution ; fixed grid only
```

Uses only the current trajectory's own frozen z-vector; no algorithm/CVI
information, no generator-comparison information, no other trajectories, no
F3 content.

### D-F2-09.6 — boundary starts (PI-owned)

```text
separate_boundary_start_bank = none
```

The A_loc / K / S(beta) / beta-anchor lattices already reach every face
(`-1`, `2`, `k_min`, `k_max`, `s_side_min(beta)`, `3`, `1`, `6`); no
additional degenerate-corner bank is inserted.

### D-F2-09.7 — retry starts (PI-owned)

```text
second_retry_start_bank = none
fallback_optimizer_may_reuse_same_start_bank = true
rng_used = false
```

### D-F2-09.8 — dedup / order (CLASS_C)

```text
P-01 canonical order = (c_r, c_d, k_r, k_d)
P-02 canonical order = (m, s_l, s_r, beta)
fixed-grid order      = ascending lexicographic

feature-start non-location constants = reference canonical cached lattice nodes
                                       (22.577778941738334; 0.32057672965544004; sqrt(6))
equivalent constants                  = do not recompute independently

comparison_rule = exact IEEE-754 float64 tuple equality
tolerance        = none — unnecessary; every tuple arises from one exact
                   construction path, so identical constructions yield
                   bit-identical doubles; no near-duplicates exist by design
retained_duplicate = first in ascending canonical sort (vacuous in the fixed
                     grid: 0 duplicates arise)

If tolerance-based dedup is ever needed for backend portability, it must be
predeclared before STEP 2, its rationale documented, and it must not change
scientific grid content.
```

### D-F2-09.9 — objective tie (CLASS_C)

```text
tie iff |L_a - L_b| <= 1e-12 + 1e-9 * max(|L_a|, |L_b|)
winner = lexicographically smallest canonical parameter tuple (per D-F2-09.8 order)
```

### D-F2-09.10 — derived start counts (DERIVED_FROM_RATIFIED_RULE)

```text
P-01 fixed retained starts = 731
P-02 fixed retained starts = 261
feature-start contribution  = +1 if valid and nonduplicate; +0 otherwise
status                      = DERIVED_FROM_RATIFIED_RULE
parent_decisions            = D-F2-09.1..09.4 (lattice rules) + D-F2-06/07 (Kural T/S)
```

---

## 9. Exact CLASS_C optimizer / coupled-constraint contract — STEP-1 exit condition

This section is the mandatory STEP-1 exit condition (worksheet §4 /
correction prompt §8). It fixes an **exact constrained-optimizer
formulation** (worksheet §8 Option B) rather than a smooth reparameterization
for both families, precisely because a large share of the D-F2-09.1–.7
lattice is anchored exactly ON the domain faces (`c_r=c_d`, `c_r=-1`,
`c_d=2`, `k=k_min`, `k=k_max`, `m=-1`, `m=2`, `beta=1`, `beta=6`,
`s=s_side_min(beta)`, `s=3`). A smooth unconstrained reparameterization via
scaled-logit/log transforms maps open intervals bijectively but sends exact
boundary values to `±infinity` (`logit(0)=-inf`, `logit(1)=+inf`), which
would make many ratified D-F2-09 starts unrepresentable exactly. The native
constrained-optimizer route below has no such gap: every ratified start
value is passed to the optimizer unchanged (identity start conversion), so
no forward/inverse mapping and no boundary proof is required — the identity
map trivially and exactly carries every feasible scientific point to itself.

### 9.1 Optimized coordinates

```text
P-01 optimized coordinates = (c_r, c_d, k_r, k_d)   — raw, no transform
P-02 optimized coordinates = (m, s_l, s_r, beta)     — raw, no transform
start conversion            = identity (D-F2-09 grid tuples passed to the
                              optimizer's x0 unchanged)
```

### 9.2 P-01 exact constraint enforcement

```text
Bounds:            c_r in [-1,2] ; c_d in [-1,2] ; k_r in [k_min,k_max] ; k_d in [k_min,k_max]
Linear constraint: c_d - c_r >= 0   (i.e. A = [-1, 1, 0, 0], lb = 0, ub = +inf)
```

Both are passed natively (scipy.optimize `Bounds` and `LinearConstraint`
objects) to a constrained solver (§9.4) — inclusive of the boundary (`c_r =
c_d` and box faces are feasible, not merely approached in the limit).

### 9.3 P-02 exact constraint enforcement

```text
m in [-1,2] ; beta in [1,6]
s_l >= s_side_min(beta) ; s_r >= s_side_min(beta) ; s_l <= 3 ; s_r <= 3
```

A static independent box is insufficient because `s_side_min(beta)` is a
nonlinear function of `beta` (see §7.1). Exact coupled formulation, two
layers:

```text
Bounds (loose, box-only, necessary but not sufficient on their own):
  m in [-1,2] ; beta in [1,6] ; s_l in [s_side_min(1), 3] ; s_r in [s_side_min(1), 3]
  where s_side_min(1) = 0.01569377976942823 is the GLOBAL minimum of
  s_side_min(beta) over beta in [1,6] (s_side_min is increasing in beta on
  this domain), giving the optimizer a valid coarse trust region.

Nonlinear constraints (exact, sufficient; scipy.optimize `NonlinearConstraint`):
  g1(x) = s_l - s_side_min(beta) >= 0
  g2(x) = s_r - s_side_min(beta) >= 0
```

The nonlinear constraints, not the box, carry the exact scientific bound;
the box only bounds the search region. Post-fit, EVERY produced solution
(regardless of which optimizer stage produced it) is re-checked against
Kural T/S and all bounds under the same D-F2-10 admissibility evaluation
applied to any candidate fit — so a solution is never accepted as scientific
merely because the optimizer's internal `constr_viol_tol` says so; the
optimizer's constraint satisfaction and the post-hoc admissibility check are
independent and consistent, not circular.

### 9.4 Optimizer contract

```text
primary_optimizer   = scipy.optimize.minimize(method='trust-constr')
                       Bounds + LinearConstraint (P-01) or Bounds + NonlinearConstraint (P-02)
                       jac = '2-point' (finite-difference)
                       hess = scipy.optimize.BFGS()  (quasi-Newton Hessian approximation)

primary tolerances (CLASS_C predeclared literals):
  gtol = 1e-10
  xtol = 1e-12
  barrier_tol = 1e-10
  constr_viol_tol (internal feasibility tolerance for the check in 9.3) = 1e-8
  maxiter = 500

fallback_optimizer   = scipy.optimize.minimize(method='SLSQP')
                       bounds = same Bounds
                       constraints expressed as SLSQP inequality-constraint
                       dicts equivalent to 9.2/9.3:
                         P-01: {'type':'ineq','fun': lambda x: x[1]-x[0]}
                         P-02: {'type':'ineq','fun': lambda x: x[1]-s_side_min(x[3])},
                               {'type':'ineq','fun': lambda x: x[2]-s_side_min(x[3])}
  fallback tolerances (CLASS_C predeclared literals):
    ftol = 1e-12
    maxiter = 500

success criterion         = OptimizeResult.success == True
                             AND all returned parameters finite
                             AND constraint violation <= constr_viol_tol (1e-8)
                             AND objective value finite
nonconvergence criterion  = no exception raised, optimizer terminates normally
                             (e.g. hits maxiter) but success == False
                             -> logged as OPTIMIZER_NONCONVERGENCE for that
                             start; NOT a numerical error; NO fallback
                             triggered; proceed to next start in the bank
pure numerical-error criterion = any exception raised during objective/
                             gradient/constraint evaluation (e.g. FloatingPointError,
                             numpy.linalg.LinAlgError, ValueError from a
                             non-finite function value) OR non-finite entries
                             in the optimizer's returned x or objective value

fallback trigger list      = exactly the "pure numerical-error criterion" above,
                             evaluated PER START (not per family/trajectory)
fallback scope              = same single start that triggered the error, using
                             the identical deterministic start bank (D-F2-09.1..09.7);
                             NO new retry starts are introduced (worksheet D-F2-09.7)
fallback outcome if it also errors = OTHER_PREDECLARED_NUMERICAL_FAILURE for
                             that start; proceed to the next start in the bank
rng_used                    = false (no randomness anywhere in this contract)
```

### 9.5 Non-alteration statement

The bounds and constraints in §9.2/9.3 are exactly the ratified D-F2-06/07
domain — nothing added, loosened, or tightened. The two-layer (box +
nonlinear) formulation for P-02 is a numerical device to give the solver a
valid search region; the SCIENTIFIC constraint is carried entirely by the
nonlinear constraint and by the post-hoc D-F2-10 admissibility re-check that
applies uniformly regardless of optimizer path. This CLASS_C design changes
no scientific parameter support, no morphology admissibility, and no fit
exclusion/admissibility rule — therefore no STOP is triggered under worksheet
§8/§4.

---

## 10. D-F2-10 — fit-success / failure policy (RATIFIED, corrected)

```text
stable_evaluation_required          = true
raw_underflow_is_ZERO_VARIANCE_FIT  = false        # (C4)

ZERO_VARIANCE_FIT = stabilized pre-z fitted trajectory effectively constant
                     under predeclared CLASS_C epsilon_model
                     (epsilon_model to be predeclared before STEP 2; see §14)

MORPHOLOGY_INADMISSIBLE = violation of ratified Kural T or Kural S (§7.1)

all_applicable_hard_failure_predicates = evaluated_and_logged_simultaneously
inadmissible_if_any_hard_failure_predicate_true = true

primary_failure_code_precedence      = CLASS_C reporting only
primary_code_is_display_convention_only = true
precedence_changes_admissibility     = false

WARN_BOUNDARY       = success_with_warning unless another hard failure holds
WARN_IDENTIFIABILITY = warning only unless a separately PI-owned exclusion rule exists

no silent clipping
no silent deletion
no manual per-trajectory tuning
no automatic spline fallback
no per-trajectory family switching
```

Failure-code taxonomy (unchanged from r1, reused): `NONFINITE_INPUT`,
`INVALID_INITIALIZATION`, `OPTIMIZER_NONCONVERGENCE`, `BOUNDARY_PATHOLOGY`,
`NONFINITE_PARAMETER`, `NONFINITE_FIT`, `ZERO_VARIANCE_FIT`,
`MORPHOLOGY_INADMISSIBLE`, `IDENTIFIABILITY_FAILURE`,
`OTHER_PREDECLARED_NUMERICAL_FAILURE`. If `epsilon_model` or any other
tolerance is later found to change admissibility rather than merely report
it, that changes its status from CLASS_C and returns to the PI — it is not
silently redefined.

---

## 11. Identifiability and censoring audit (carried from r1, referenced against Kural T/S)

| axis | P-01 WC-ADL | P-02 TAD/PSAT |
|---|---|---|
| amplitude / baseline | removed by construction (§4) | same |
| location vs rates | plateau length `c_d-c_r` partially confounded with `k` when far out-of-window; governed by Kural T/S admissibility, not silently accepted | `m` out-of-window leaves the unobserved-side scale weakly identified — flagged `WARN_IDENTIFIABILITY`, governed by Kural T/S |
| asymmetry | identifiable when both transitions intersect the window | identifiable for interior `m` |
| out-of-window timing | finite box `[-1,2]` (identifiability-horizon rationale) | same |
| excluded-morphology adjacency | `k` bounds via Kural T keep transitions off step-like (level_shift) forms; Kural S keeps off impulse-like forms | `beta`/`s` bounds via Kural T keep peak off flat-top (cylinder) forms; Kural S off impulse-like forms |

This audit is now anchored to the exact, ratified Kural T/S admissibility
rule rather than descriptive language alone.

---

## 12. Numerical implementation vs scientific-specification separation (pin schema per C7)

```text
Pin ID schema = P-01.x / P-02.x / P-CMN.x
status        = single-valued (one of: NORMATIVELY_FIXED, PI_RATIFIED,
                CLASS_C_IMPLEMENTATION_PIN, DERIVED_FROM_RATIFIED_RULE)
```

`P-CMN.x` pins are shared sub-components of P-01 and P-02 (e.g. time
coordinate, prediction operator, objective) — they are NOT a new top-level
pin category, and the v0 §26 calibration-open pin inventory (32 items)
remains unchanged; this note is recorded here per C7/C8.

| pin_id | component | status |
|---|---|---|
| P-CMN.1 | time coordinate (D-F2-02) | PI_RATIFIED |
| P-CMN.2 | prediction operator, no amplitude/offset (D-F2-03) | PI_RATIFIED |
| P-CMN.3 | fit objective (D-F2-08) | PI_RATIFIED |
| P-01.1 | exact formula (D-F2-04) | PI_RATIFIED |
| P-01.2 | bounds + Kural T/S (D-F2-06) | PI_RATIFIED |
| P-01.3 | initialization D-F2-09.1/.2/.5/.6/.7 | PI_RATIFIED |
| P-01.4 | constraint parameterization / optimizer (§9) | CLASS_C_IMPLEMENTATION_PIN |
| P-02.1 | exact formula (D-F2-05) | PI_RATIFIED |
| P-02.2 | bounds + Kural T/S (D-F2-07) | PI_RATIFIED |
| P-02.3 | initialization D-F2-09.3/.4/.5/.6/.7 | PI_RATIFIED |
| P-02.4 | constraint parameterization / optimizer (§9) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.4 | dedup/order (D-F2-09.8) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.5 | objective tie (D-F2-09.9) | CLASS_C_IMPLEMENTATION_PIN |
| P-CMN.6 | k_max, s_side_min(beta), start counts | DERIVED_FROM_RATIFIED_RULE |
| P-CMN.7 | failure taxonomy / precedence (D-F2-10) | PI_RATIFIED (precedence itself CLASS_C) |

---

## 13. Spline benchmark registration (D-F2-12, RATIFIED)

```text
shape_constrained_low_df_spline_role = adequacy_benchmark_only
winner_candidate                     = false
automatic_primary_fallback           = false

spline_exact_specification = outcome-blind pre-F3 implementation pin
deadline                    = before any candidate-specific F3 adequacy computation
```

Does not expand the P-01/P-02 scientific freeze object and does not create a
third primary generator.

---

## 14. D-F2-11 — F2 second-pass scope (RATIFIED)

```text
F2_second_pass_feasibility = synthetic_and_analytic_fixtures_only
```

Allowed: executability; deterministic repeatability; stable generator
evaluation; constraint-transform QC; initialization-path QC; failure-code
exercise; CLASS_C implementation validation; runtime telemetry (as
computational evidence only).

Forbidden: real SSA fit; real SSA subset fit; parameter-recovery score;
parameter-recovery pass/fail threshold; parameter-recovery rate; family
comparison; comparative reconstruction error; P-03 derivation/tuning;
generator selection; and explicitly — an objective-attainment threshold such
as `L <= L_tol`; self-generated-fixture pass/fail based on objective
attainment; any recovery-style success rate. Synthetic fixtures may test
code-path execution, deterministic repeatability, constraint handling,
stable evaluation, initialization-path execution, and failure-code
reachability only.

**STEP-2 precondition (per this ratification):** STEP 2 may not begin until
the `epsilon_model` CLASS_C literal (§10) and any remaining CLASS_C runtime
literal needed to execute the optimizer contract (§9) are predeclared and
this record (or a documented STEP-1.5 addendum) is confirmed exact and
executable by independent audit.

---

## 15. Forbidden F3 items / firewall confirmation

Untouched in this pass: P-03 adequacy thresholds; P-04 generator tie-break;
P-05 cross-fit scheme; any family comparison or selection statement.

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access      = false
algorithm_CVI_execution           = false
generator_adequacy_comparison     = false
generator_selection               = false
cross_fit_adequacy                = false
P03_touched = false | P04_touched = false | P05_touched = false
F3_started = false | F4_started = false
Q_CD_created = false | B_star_created = false | H_star_created = false
real_SSA_fit = false | real_SSA_subset_fit = false
```

---

## 16. F2 completion checklist (STEP 1)

| check | state |
|---|---|
| candidate count = exactly 2 | PASS |
| P-01/P-02 exact formulas ratified | PASS |
| all bounds ratified with Kural T/S exact definitions | PASS |
| D-F2-09.1–.7 initialization contract frozen exactly (no vague phrases) | PASS |
| exact CLASS_C optimizer/coupled-constraint contract closed (§9) | PASS |
| D-F2-09.8–.9 CLASS_C pins recorded | PASS |
| D-F2-09.10 counts recorded as DERIVED_FROM_RATIFIED_RULE | PASS |
| D-F2-10 failure semantics corrected (raw underflow != ZERO_VARIANCE_FIT) | PASS |
| D-F2-11 second-pass scope frozen, STEP-2 prohibitions explicit | PASS |
| D-F2-12 spline deadline frozen | PASS |
| R1 exact-byte custody complete and hash-verified | PASS |
| R2/R3/R4 recorded | PASS |
| C1–C10 applied | PASS (§17) |
| no F3 threshold selected / no cross-fit run / no generator selected | PASS |
| no real SSA trajectory touched | PASS |
| PI ratification recorded | PASS |
| STEP 2 executed | NO — deliberately not run in this task |

---

## 17. C1–C10 application status

| item | status | note |
|---|---|---|
| C1 revision lineage | APPLIED | §0 |
| C2 search auditability | APPLIED | §2.1 |
| C3 literature provenance | APPLIED | §2.3 |
| C4 underflow correction | APPLIED | §5, §6, §10 |
| C5 P-02 s_max rationale | APPLIED | §7.3 |
| C6 initialization/retry exactness, rng_used=false | APPLIED | §8 (D-F2-09.5/.7) |
| C7 pin schema P-01.x/P-02.x/P-CMN.x, single-valued status | APPLIED | §12 |
| C8 decision register: opaque identifier, D-F2-11/12 formal | APPLIED | §3, §13, §14 |
| C9 next_action: no frozen-trajectory feasibility language | APPLIED | §14 (synthetic-only; STEP-2 precondition explicit) |
| C10 downstream interface NON-BINDING label | APPLIED | §4 |

## R1–R4 application status

```text
R1 = APPLIED
  ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
    ledger_filename        = ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
    actual_local_filename  = chatgpt_ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
                             (cosmetic prefix difference; hash identity governs)
    original_path          = C:/Users/Neo/Downloads/yeni_proje/v_11/chatgpt_ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
    repository_copy_path   = p_konum_plus/provenance/nonnormative/ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
    SHA256                 = 3bd9e7cfdbdfe9358f91792db12447594d86956cd1c1b185552cb2da4d94b787  (verified exact, both source and copy)
    copy_date              = 2026-08-31
    provenance_role        = nonnormative
    methodology_authority  = none

  claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md
    ledger_filename        = claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md
    actual_local_filename  = claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md  (identical)
    original_path          = C:/Users/Neo/Downloads/yeni_proje/v_11/claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md
    repository_copy_path   = p_konum_plus/provenance/nonnormative/claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md
    SHA256                 = 29c073ba5105a14299a0ea9427d8443c1a29d40960f7fed355ef49b2bae67c5a  (verified exact, both source and copy)
    copy_date              = 2026-08-31
    provenance_role        = nonnormative
    methodology_authority  = none

  copy_only = true | normalize = false | delete_original = false

R2 = APPLIED (§2.2)
  available_and_verified; no mathematical definitions found; no acronym
  expansions found; no TAD-vs-PSAT historical relation established; no
  material P-01/P-02 formula contradiction.

R3 = APPLIED
  Pre-v11 tie-break/cross-fit text present in the R1-custodied sources
  (identified during the 2026-08-29 reconciliation check):
    methodology_authority = none
    historical_provenance = true
    superseded_by = v11
    P04_derivation_use = prohibited
    P05_derivation_use = prohibited
    F3_scientific_evidence_use = prohibited

R4 = APPLIED — mechanical derivations
  [1] k_max
      status = DERIVED_FROM_RATIFIED_RULE
      parent_decision_id = D-F2-06 (Kural T, w_min_years)
      derivation_formula = 2*ln(9)*145 / w_min_years
      input_values        = w_min_years = 5
      rounding_policy      = none — exact continuous float64 value used as the
                             optimizer bound; no rounding
      derived_value        = 127.43902548550072

  [2] s_side_min(beta)
      status = DERIVED_FROM_RATIFIED_RULE
      parent_decision_id = D-F2-07 (Kural T, w_min_years)
      derivation_formula = (5/145) / ( ln(10)^(1/beta) - ln(10/9)^(1/beta) )
      input_values        = w_min_years = 5 ; beta = optimizer's current beta
      rounding_policy      = none — exact formula evaluated at the beta in use
      derived_value        = function of beta (not a single number); example
                             evaluations: beta=1 -> 0.01569377976942823,
                             beta=sqrt(6) -> 0.03425647986552569 (matches the
                             worksheet §D-F2-09.3/.4 example), beta=6 -> 0.07465689442188805

  [3] D-F2-09.10 derived start counts
      status = DERIVED_FROM_RATIFIED_RULE
      parent_decision_id = D-F2-09.1..09.4 lattice rules + D-F2-06/07 (Kural T/S)
      derivation_formula = enumerate lattice -> filter bounds+Kural T (by
                           construction) -> filter Kural S (n_sup>=3, stabilized
                           evaluation) -> dedup (exact tuple equality)
      input_values        = A_loc (13), K (3), S(beta) (3 per beta), beta anchors (3)
      rounding_policy      = none
      derived_value        = P-01 = 731 ; P-02 = 261
```

---

## 18. Firewall / gate status

```text
ART_F2_r2_created       = true
PI_ratification_recorded = true
F2_STEP_1_complete      = true

F2_STEP_2   = false
F2_complete = false
F3_allowed  = false

real_SSA_fit          = false
real_SSA_subset_fit   = false
algorithm_CVI_execution = false
algorithm_CVI_outcome_access = false
legacy_performance_content_access = false

next_action = independent audit of ART-F2 r2
STEP 2 may begin only after that independent audit passes AND the STEP-2
precondition in §14 (epsilon_model + any remaining runtime CLASS_C literal)
is predeclared exact and executable.
```
