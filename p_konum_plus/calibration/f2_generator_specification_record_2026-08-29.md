# ART-F2 — Generator Specification Record (F2) — DRAFT / OWNER DECISION PACKET

## 0. Artifact identity and governing hashes

```text
artifact_id         = ART-F2
artifact_role       = generator_specification_record
record_status       = DRAFT_OWNER_DECISION_PACKET
normative_authority = v11_only
gate                = F2
date                = 2026-08-29
worktree            = G:/PycharmProjects/pkp-worktree
branch              = p_konum_plus
HEAD_at_execution   = 3e4daf47018f124e29717263e4e45fe90c8e52b8

F2_status           = OWNER_DECISION_REQUIRED
F2_complete         = false
F3_allowed          = false
```

Governing hashes (recomputed this task, all exact):

| document | SHA256 |
|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` |
| ART-F0 (r2) | `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` |
| ART-F1 (r4a FINAL) | `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0` |
| F1 eligible manifest | `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` |
| F1 input hash table | `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac` |

This is a DRAFT decision packet, not a frozen record. No whole-file self-hash
is stored inside this file; no `.sha256` sidecar exists (F12-only).
`v11_wins = true`.

## 1. F2 normative constraints

```text
candidate_generator_set = {WC-ADL, TAD/PSAT}     # closed; exactly 2
third_primary_generator = forbidden
shape_constrained_low_df_spline_role = adequacy_benchmark_only
automatic_spline_fallback = false
algorithm_CVI_information_in_generator_specification = forbidden
```

F2 freeze object per family: exact formula; parameter bounds; initialization
scheme; deterministic fit-failure handling. Candidate adequacy comparison,
thresholds, tie-break, and cross-fit belong to F3 and are untouched here. The
frozen ART-F1 r4a input contract (national-only, 146 raw yob files,
1880–2025, T=146, released_record_share, FULL-support eligibility, 435 F /
471 M, no imputation, row z ddof=0, r4 disclosure semantics without any
`[0,4]` claim) is taken as fixed.

## 2. Evidence/source inventory

| item | class | status / use |
|---|---|---|
| Frozen ART-F1 structural facts (T=146 grid, z-space, 906 eligible trajectories, grid step 1/145) | EV-01 | used for geometry/identifiability rationale only; no trajectory fitted |
| Trivial mathematical/software checks (section 11.4) | EV-02 (minimal) | finiteness / nonconstancy / z-validity / transform reversibility on hand-constructed parameters; NO family comparison, NO real-data fit |
| Wikipedia, Generalized normal distribution (fetched 2026-08-29) | EV-08 | confirms symmetric generalized Gaussian `exp(-(|x-mu|/alpha)^beta)` as standard and asymmetric variants as recognized standard constructions |
| Wikipedia, Logistic function (fetched 2026-08-29) | EV-08 | confirms standard single logistic `L/(1+e^{-k(x-x0)})`; does NOT document a rise-decline double-logistic product — that composition is therefore recorded as project-defined, not literature-anchored here |
| Owner task packet 2026-08-29 (search cues: "asymmetric generalized Gaussian", "double logistic", "window-censored", "asymmetric life-cycle") | owner-supplied cue provenance | anticipates the two mathematical directions; not itself a mathematical definition |
| Repository search (docs/, protocol/, p_konum_plus/) for WC-ADL / WC-ALC / TAD / PSAT / double logistic / generalized gaussian / window-censored | discovery | names occur ONLY in v11 and v11-derived governance documents; no mathematical definition anywhere in the repository; legacy docs/protocol contain no hits; `results/` never searched or opened |
| v11 §0.1 reconciliation syntheses | absent locally | not present in the repository; not consulted |

```text
literature_access = available_limited (two pages fetched; no fabricated citations)
```

## 3. Generator-name and definition provenance

| family | name_provenance | mathematical_definition_provenance | standard_or_project_specific |
|---|---|---|---|
| WC-ADL | v11 §5 (label only; no expansion given) | none in any admissible source; drafted in this record | project-specific label; recommended definition = project-defined composition of standard logistic components; the expansion of "ADL" is NOT inferred (no source support) |
| TAD/PSAT | v11 §5 (label only; no expansion given) | none in any admissible source; drafted in this record | project-specific label; recommended definition = project parameterization of the standard asymmetric generalized Gaussian family; expansions of "TAD"/"PSAT" NOT inferred |
| WC-ALC (morphology family, context) | v11 §4 (label + W-L/W-I/W-R regime roles) | n/a (morphology umbrella, not a generator) | project-specific label; regimes remain descriptors, not truth classes |

Repository usage of the names is consistent (v11-only); no conflicting
definitions were found — the finding is absence, not inconsistency.

```text
P-02_name_definition_status = OWNER_DECISION_REQUIRED   (decision D-F2-01)
P-01_name_definition_status = OWNER_DECISION_REQUIRED   (formula ratification D-F2-04 covers it)
```

## 4. Common observation/preprocessing interface (both families)

- Input objects: the 906 frozen eligible trajectories (ART-F1 r4a pipeline:
  released_record_share -> row z-normalization, mean/population sd ddof=0),
  each a finite nonconstant vector `x in R^146` indexed by years 1880..2025.
- Time coordinate (D-F2-02): recommended internal coordinate
  `u_j = j/145, j = 0..145` (i.e. `u = (t-1880)/145 in [0,1]`). Both families
  are invariant under this affine reparameterization (location/scale
  parameters transform affinely); `u` is recommended purely for numerical
  conditioning. The raw-year form is mathematically equivalent.
- Model prediction operator (D-F2-03): for latent curve `g(u; theta)` the
  fitted prediction is `ghat(theta) = z_ddof0( g(u_grid; theta) )` — the model
  curve is z-normalized ON THE SAME 146-grid before comparison with `x`.
  Consequence: any affine transform `a*g+b (a>0)` yields identical `ghat`, so
  amplitude and vertical offset are **unidentifiable by construction** and are
  therefore **omitted from both parameter sets** (not retained as nuisance
  parameters by convention). This is scientific-contract-defining and needs
  PI ratification.
- Zero-variance guard: if `g(u_grid; theta)` is constant (analytically or by
  floating-point underflow), z-normalization is undefined ->
  `ZERO_VARIANCE_FIT` (section 9). This case is reachable at bounds-box
  corners (demonstrated in 11.4).

## 5. P-01 WC-ADL — candidate exact specification (DRAFT_RECOMMENDATION)

Latent noiseless curve (project-defined composition of two standard
logistics; rise times decline):

```text
g(u; c_r, c_d, k_r, k_d) = sigma( k_r * (u - c_r) ) * sigma( -k_d * (u - c_d) )

sigma(v) = 1 / (1 + exp(-v))
constraint: c_r <= c_d ; k_r > 0 ; k_d > 0
```

| element | specification |
|---|---|
| input time coordinate | `u` per section 4 (D-F2-02) |
| parameters | `c_r` rise midpoint (u-units, may lie outside [0,1]); `c_d` decline midpoint (u-units, may lie outside [0,1]); `k_r` rise steepness; `k_d` decline steepness |
| amplitude/baseline | none — removed by the z-invariance of the prediction operator (section 4) |
| rise mechanism | rising logistic with midpoint `c_r`, 10–90% width `2*ln(9)/k_r` u-units |
| decline mechanism | falling logistic with midpoint `c_d`, width `2*ln(9)/k_d` |
| asymmetry mechanism | `k_r != k_d` (rise/decline speed asymmetry) and plateau length `c_d - c_r` |
| peak/location mechanism | latent maximum lies between `c_r` and `c_d`; located numerically (no closed form needed for fitting) |
| window censoring mechanism | the window [0,1] observes only a segment of the latent life cycle: both midpoints left of 0 -> observed decline tail (W-L-like); interior midpoints -> interior rise-peak-decline (W-I-like); midpoints right of 1 -> observed rise (W-R-like) — regimes remain descriptors, not truth classes; no separate generators per regime |
| output before z-normalization | `g(u_grid; theta) in (0,1)^146` |
| output after frozen row z-normalization | `ghat = z_ddof0(g(u_grid; theta))` |

## 6. P-02 TAD/PSAT — candidate exact specification (DRAFT_RECOMMENDATION)

Latent noiseless curve (project parameterization of the standard asymmetric
generalized Gaussian: two-piece, shared shape exponent, distinct side
scales):

```text
g(u; m, s_l, s_r, beta) =
    exp( -((m - u)/s_l)^beta )    for u <= m
    exp( -((u - m)/s_r)^beta )    for u >  m

constraint: s_l > 0 ; s_r > 0 ; beta >= 1 ; m may lie outside [0,1]
```

| element | specification |
|---|---|
| input time coordinate | `u` per section 4 (D-F2-02) |
| parameters | `m` latent peak location (u-units); `s_l` left (rise-side) scale; `s_r` right (decline-side) scale; `beta` shared shape exponent |
| amplitude/baseline | none — removed by z-invariance (section 4) |
| rise mechanism | left branch, approach to peak with scale `s_l` |
| decline mechanism | right branch with scale `s_r` |
| asymmetry mechanism | `s_l != s_r` (side-scale asymmetry); optional owner alternative: side-specific exponents `beta_l, beta_r` (5-parameter variant, D-F2-05) |
| peak/location mechanism | `m` (value 1 at `u = m`; continuous; C1 for `beta > 1`, corner peak at `beta = 1`) |
| window censoring mechanism | as P-01: `m < 0` -> observed decline branch only (W-L-like); interior `m` -> W-I-like; `m > 1` -> observed rise branch only (W-R-like); descriptors only |
| output before z-normalization | `g(u_grid; theta) in (0,1]^146` |
| output after frozen row z-normalization | `ghat = z_ddof0(g(u_grid; theta))` |

## 7. Parameter-bound decision tables

All numeric bounds below are DRAFT_RECOMMENDATIONs requiring PI ratification
(D-F2-06/07). None derives from legacy ranges, candidate preference, or any
algorithm/CVI information. Constants used: window length 1, grid step
`1/145 ≈ 0.0069`; logistic 10–90% width `= 2*ln(9)/k` (k=4 -> 1.10 windows;
k=290 -> 0.0152 ≈ 2.2 grid steps).

### 7.1 P-01 WC-ADL

| parameter | lower | upper | bound_type | rationale | source/evidence | scientific_or_numerical | OWNER_DECISION_REQUIRED? |
|---|---|---|---|---|---|---|---|
| `c_r` | −1.0 | 2.0 | box (with `c_r <= c_d`) | one full window length of out-of-window latitude per side; beyond that the in-window segment of a logistic transition is indistinguishable from flat/linear (identifiability horizon on T=146 geometry) | EV-01 geometry | scientific | YES |
| `c_d` | −1.0 | 2.0 | box (ordered) | same | EV-01 geometry | scientific | YES |
| `delta = c_d − c_r` | 0 | 3.0 | derived box | permits monotone-through-window plateaus while keeping both transitions within the identifiability horizon | EV-01 geometry | scientific | YES |
| `k_r`, `k_d` | 4 | 290 | box | lower: 10–90% width ≈ 1.10 windows — flatter is indistinguishable from a linear trend; upper: width ≈ 2.2 grid steps — steeper approaches a step (level_shift-adjacent, an excluded morphology) and is unresolvable on the grid | EV-01 geometry + v11 §4 exclusions | scientific + numerical | YES |

### 7.2 P-02 TAD/PSAT

| parameter | lower | upper | bound_type | rationale | source/evidence | scientific_or_numerical | OWNER_DECISION_REQUIRED? |
|---|---|---|---|---|---|---|---|
| `m` | −1.0 | 2.0 | box | same out-of-window identifiability horizon as P-01 locations | EV-01 geometry | scientific | YES |
| `s_l`, `s_r` | 0.02 | 3.0 | box | lower: half-width ≈ 3 grid steps at `beta = 2` — narrower approaches impulse-adjacent unresolvable peaks; upper: 3 window lengths — the in-window segment becomes numerically flat (zero-variance risk, demonstrated in 11.4) | EV-01 geometry + v11 §4 exclusions | scientific + numerical | YES |
| `beta` | 1.0 | 6.0 | box | lower: corner (Laplace-like) peak still width-controlled; below 1 the cusp sharpens toward impulse-adjacent forms; upper: flat-top plateau approaches cylinder-adjacent (excluded morphology) | EV-08 (GG family standard) + v11 §4 exclusions | scientific | YES |

If the PI prefers empirically informed refinements of any numeric bound:
`OWNER_DECISION_REQUIRED / MEASUREMENT_NOT_RUN_IN_THIS_PASS` — no F1-empirical
bound measurement was executed in this pass.

## 8. Initialization decision tables (D-F2-09)

Deterministic initialization contract (draft; identical structure for both
families, family-specific start values):

| element | draft rule |
|---|---|
| initial parameter construction | hybrid: (a) one feature-based start per trajectory — location start at the in-window argmax of `x` (deterministic function of the frozen data), moderate steepness/scales, symmetric asymmetry; plus (b) a fixed data-independent grid |
| deterministic start grid | locations `{−0.5, −0.25, 0.1, 0.3, 0.5, 0.7, 0.9, 1.25, 1.5}` (out-of-window starts included on both sides); steepness/scale at 3 log-spaced levels spanning the bound box interior; asymmetry ratios `{0.5, 1, 2}` |
| boundary starts | one start at each identifiable bounds-box face midpoint (not corners — corners are degenerate, 11.4) |
| number/type of starts | grid size above is a DRAFT_RECOMMENDATION; the exact count is OWNER_DECISION_REQUIRED |
| tie between equally good starts | deterministic: lowest objective wins; exact objective tie broken by lexicographic order of the transformed parameter vector under a fixed parameter ordering (`c_r,c_d,k_r,k_d` / `m,s_l,s_r,beta`) |
| dependence | none on any algorithm/CVI information; fully reproducible from frozen data + fixed grid |

## 9. Fit-success and failure-policy tables (D-F2-10)

### 9.1 Fit-success predicate (operational complement of the failure policy)

A fit is successful iff ALL hold: optimizer termination = converged (or
gradient/step tolerance met); all parameters finite and inside bounds
(boundary contact allowed but flagged); fitted curve finite; pre-z variance
of the fitted curve > 0; z-normalization valid; objective finite. Boundary
contact -> `WARN_BOUNDARY` (success with diagnostic warning) unless at a
predeclared degenerate configuration (below) -> failure. Singularity /
near-flat curvature -> `WARN_IDENTIFIABILITY` diagnostic. **No F3 adequacy
threshold participates in fit success.**

### 9.2 Failure-code taxonomy

```text
NONFINITE_INPUT | INVALID_INITIALIZATION | OPTIMIZER_NONCONVERGENCE |
BOUNDARY_PATHOLOGY | NONFINITE_PARAMETER | NONFINITE_FIT |
ZERO_VARIANCE_FIT | IDENTIFIABILITY_FAILURE |
OTHER_PREDECLARED_NUMERICAL_FAILURE
```

Predeclared degenerate configurations (draft): all location parameters at the
same out-of-window bound with maximal flatness (P-01: `c_r = c_d` at a far
bound with `k` at lower bound; P-02: `m` at a far bound with observed-side
scale at a bound) -> `IDENTIFIABILITY_FAILURE`; constant/underflowed curve ->
`ZERO_VARIANCE_FIT` (reachable — demonstrated at a P-02 bounds corner, 11.4).

### 9.3 Deterministic failure-handling sequence (draft)

```text
primary deterministic multistart set (section 8)
-> one predeclared deterministic retry set (fixed perturbed grid)
-> predeclared numerical fallback optimizer (class-C; purely numerical)
-> FAMILY_FIT_FAILURE(code) with logged trajectory_id + code + diagnostics
```

Principles (binding): no automatic spline fallback; no silent parameter
clipping; no silent data deletion; no manual per-trajectory tuning; no family
switching for individual trajectories; no dropping a failed trajectory
without logged reason.

## 10. Identifiability and censoring audit

| axis | P-01 WC-ADL | P-02 TAD/PSAT |
|---|---|---|
| amplitude / baseline | removed by construction (section 4) — unnecessary, not nuisance | same |
| location vs rates | plateau length `c_d−c_r` partially confounded with `k` when the peak is far out-of-window; both-midpoints-out-same-side leaves only one effective transition identifiable | `m` out-of-window leaves the unobserved-side scale (`s_l` for `m<0`, `s_r` for `m>1`) weakly/un-identified — flagged `WARN_IDENTIFIABILITY`, not silently fixed |
| asymmetry | `k_r/k_d` identifiable only when both transitions intersect the window | side-scale asymmetry identifiable only for interior `m` |
| out-of-window timing | `c_r`, `c_d` control latent timing; out-of-window values allowed within finite box [−1, 2] (identifiability horizon rationale, section 7) | `m` same |
| excluded-morphology adjacency | `k` upper bound keeps transitions off step-like (level_shift) forms | `beta` upper bound keeps peak off flat-top (cylinder) forms; `s` lower bound off impulse-like forms |
| W-L / W-I / W-R generation | reachable via latent timing (verified finite/nonconstant in 11.4) | same |

Latent-timing governance: out-of-window latent maxima are mathematically
required for W-L/W-R and are allowed; all optimization domains are finite
boxes (no unbounded domain); the finiteness rationale is the T=146
identifiability horizon, not convenience. No observed-window regime
thresholds are defined here (later gates).

## 11. Numerical implementation vs scientific specification separation

### 11.1 Scientific specification (PI-owned contract)

Family formulas (sections 5–6); parameter sets and meanings; bounds
(section 7); fit objective (D-F2-08: recommended unweighted least squares in
frozen z-space, `sum_t (x_t − ghat_t)^2`); determinism requirements of
initialization and failure handling; failure taxonomy and admissibility
conditions (finite, in-bounds, nonzero variance).

### 11.2 Class-C implementation candidates (no scientific effect if predeclared)

Constraint transforms (log for positive parameters; ordered `(a, log delta)`
for `c_r <= c_d`; scaled-logit for boxed locations — all bijective onto the
allowed set, hence family-preserving; reversibility verified in 11.4);
optimizer library/algorithm choice (e.g. bounded quasi-Newton vs
trust-region) and internal tolerances; retry mechanics; floating-point
guards. Per the task rule these are recorded as
`CLASS_C_IMPLEMENTATION_CANDIDATE`, not silently promoted to scientific pins.

### 11.3 Classification of the four flagged items

| item | classification |
|---|---|
| fit objective | scientific-contract-defining -> PI (D-F2-08) |
| constraint parameterization | CLASS_C (bijective, family-preserving; equivalence noted) |
| optimizer/fallback policy | CLASS_C, except its determinism/predeclaration requirement, which is part of the scientific failure policy (D-F2-10) |
| fit-success predicate | operational complement of the frozen fit-failure policy (inside D-F2-10); its admissibility conditions mirror the failure taxonomy and do not add a new scientific pin |

### 11.4 Trivial feasibility checks executed (EV-02, permitted set only)

Hand-constructed parameters on the 146-grid (no real trajectory touched, no
family comparison): P-01 finite/nonconstant/z-valid in W-I-, W-L-, W-R-style
and bounds-corner configurations (4/4); P-02 finite/nonconstant/z-valid in
W-I/W-L/W-R/sharp-peak configurations (4/4) and **constant-zero by underflow
at one bounds-box corner** (`m = 2.0, s_l = 0.02, beta = 6`) — documented as
the reachable `ZERO_VARIANCE_FIT` case and the reason corners are excluded
from boundary starts; constraint transforms round-trip exactly (log, ordered
`a + exp(b)`, scaled-logit). Resolvability constants verified
(`2 ln 9 / k`, grid step `1/145`).

## 12. Spline benchmark registration

```text
shape_constrained_low_df_spline_role = adequacy_benchmark_only
winner_candidate                     = false
automatic_primary_fallback           = false
spline_exact_implementation          = deferred_to_owning_pre_F3_implementation_pin
```

If an exact spline implementation is required for F3 adequacy benchmarking,
it must be pinned outcome-blind BEFORE any candidate-specific F3 adequacy
comparison begins. No spline specification is selected in this record.

## 13. Forbidden F3 items / firewall confirmation

Untouched in this pass: P-03 adequacy thresholds; P-04 generator tie-break;
P-05 cross-fit scheme; every adequacy threshold class; any family comparison
or selection statement. No "WC-ADL is better", no "TAD/PSAT is better", no
`selected_generator`.

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
algorithm_CVI_execution = false
generator_adequacy_comparison = false
generator_selection = false
cross_fit_adequacy = false
P03_touched = false | P04_touched = false | P05_touched = false
F3_started = false | F4_started = false
Q_CD_created = false | B_star_created = false | H_star_created = false
```

## 14. PI owner-decision register (decision packet)

Pin records (format: pin_id | family | component | candidate | status |
owner | evidence | provenance | rationale | alternatives | unresolved-reason
| downstream effect) are given compactly; statuses use only
DRAFT_RECOMMENDATION / OWNER_DECISION_REQUIRED / NORMATIVELY_FIXED /
CLASS_C_IMPLEMENTATION_CANDIDATE.

| pin_id | family | spec_component | candidate_value_or_definition | status | owner | evidence_class | source_provenance | scientific_rationale | alternatives_considered | reason_not_selected_or_unresolved | downstream_effect |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P-00-SET | both | candidate set | {WC-ADL, TAD/PSAT}; spline benchmark-only | NORMATIVELY_FIXED | v11 | — | v11 §5 | closed | — | — | F3 operates on exactly these two |
| P-01-A | WC-ADL | exact formula | double-logistic product (section 5) | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01,08 | project-defined; single logistic standard (fetched); product composition project-defined | life-cycle rise×decline with censorable latent timing | 5-param variants; logistic×exponential hybrids | PI ratification absent | defines P-01 family (family-altering) |
| P-01-B | WC-ADL | bounds | table 7.1 | OWNER_DECISION_REQUIRED | PI | EV-01 | T=146 geometry | identifiability horizon + excluded-morphology adjacency | empirically refined bounds (MEASUREMENT_NOT_RUN_IN_THIS_PASS) | numeric ratification absent | feasible parameter space |
| P-01-C | WC-ADL | initialization | section 8 contract | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01 | project-defined | determinism + censored-start coverage | pure data-independent grid; pure feature-based | start count unratified | reproducibility of fits |
| P-01-D | WC-ADL | fit-failure policy | section 9 | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01 | project-defined | no-fallback/no-silent-repair principles | — | ratification absent | F3 inputs' integrity |
| P-02-A | TAD/PSAT | exact formula | two-piece asymmetric generalized Gaussian, shared beta (section 6) | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01,08 | asymmetric GG = recognized standard construction (fetched); two-piece dual-scale = project parameterization | single-peak asymmetric life cycle with censorable peak | 5-param `beta_l != beta_r`; kappa-skew GG parameterization | PI ratification absent | defines P-02 family (family-altering) |
| P-02-B | TAD/PSAT | bounds | table 7.2 | OWNER_DECISION_REQUIRED | PI | EV-01,08 | T=146 geometry | as P-01-B | empirical refinement (not run) | numeric ratification absent | feasible parameter space |
| P-02-C | TAD/PSAT | initialization | section 8 contract | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01 | project-defined | as P-01-C | as P-01-C | start count unratified | reproducibility |
| P-02-D | TAD/PSAT | fit-failure policy | section 9 | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01 | project-defined | as P-01-D | — | ratification absent | F3 inputs' integrity |
| P-CMN-1 | both | time parameterization | `u = (t−1880)/145` | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01 | project-defined | conditioning; affine-invariant | raw calendar year | trivial but contract-recorded | parameter units |
| P-CMN-2 | both | prediction operator / no amplitude-offset | `ghat = z_ddof0(g)` | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-01 | project-defined | z-invariance removes unidentifiable parameters | amplitude+offset nuisance fit in share space | contract-defining | identifiability of both families |
| P-CMN-3 | both | fit objective | unweighted LS in frozen z-space | DRAFT_RECOMMENDATION -> OWNER_DECISION_REQUIRED | PI | EV-08 | project-defined | matches frozen z-metric; no clustering-relevance weighting | robust loss (changes the fitted estimand; would need explicit justification) | contract-defining | meaning of "best fit" |
| P-CMN-4 | both | constraint parameterization | log / ordered / scaled-logit transforms | CLASS_C_IMPLEMENTATION_CANDIDATE | executor (predeclared) | EV-02 | project-defined | bijective, family-preserving (verified) | direct boxed optimization | class-C by rule | none scientific |
| P-CMN-5 | both | optimizer + numerical fallback | bounded local optimizer + one predeclared fallback | CLASS_C_IMPLEMENTATION_CANDIDATE (determinism requirement inside P-0x-D) | executor (predeclared) | EV-02 | project-defined | numerical only | alternatives equivalent | class-C by rule | none scientific |
| P-CMN-6 | both | fit-success predicate | section 9.1 | operational complement of P-0x-D (no separate scientific pin) | PI via P-0x-D | EV-01 | project-defined | admissibility mirrors failure taxonomy | stricter predicates = F3 territory | — | which fits enter F3 |

### Decisions requested from the PI (smallest closing set)

| DECISION ID | recommended option | alternatives | scientific consequence | numerical consequence | why recommended | family-altering if changed later? |
|---|---|---|---|---|---|---|
| D-F2-01 | Declare TAD/PSAT ONE family with dual historical labels, defined by P-02-A | (b) PSAT = named parameterization of TAD (same formula, both names mapped); (c) escalate as genuinely ambiguous | fixes candidate-set semantics at exactly 2 families | none | no admissible source distinguishes the two names; option (a) is the smallest consistent closure | no (label semantics only) |
| D-F2-02 | internal coordinate `u=(t−1880)/145` | raw year `t` | none (affine-invariant family) | better conditioning | conditioning | no |
| D-F2-03 | z-normalized prediction operator; omit amplitude/offset | fit amplitude+offset in share space | changes fitted estimand & identifiability if altered | avoids 2 unidentifiable parameters | matches frozen F1 z-metric exactly | yes (contract) |
| D-F2-04 | P-01 formula = double-logistic product (section 5) | 5-parameter variants; other rise-decline compositions | defines the WC-ADL family | 4-parameter, well-conditioned | minimal complete censorable life-cycle form | yes |
| D-F2-05 | P-02 formula = 4-param two-piece generalized Gaussian (section 6) | 5-param `beta_l != beta_r`; kappa-skew form | defines the TAD/PSAT family | 4-parameter, standard-family anchored | parsimonious; asymmetric GG standard | yes |
| D-F2-06 | ratify P-01 bounds (table 7.1) | adjust numbers; request empirical refinement (measurement not run) | feasible-space definition | box constraints | geometry-tied rationale | partially (reachable shapes) |
| D-F2-07 | ratify P-02 bounds (table 7.2) | same | same | same | same | partially |
| D-F2-08 | unweighted least squares in frozen z-space | robust loss | defines fit estimand | standard smooth objective | consistency with frozen metric | yes (contract) |
| D-F2-09 | initialization contract (section 8) incl. exact start count | smaller/larger deterministic grids | none if deterministic | multistart robustness | covers censored starts deterministically | no (if deterministic) |
| D-F2-10 | fit-failure policy + taxonomy + success predicate (section 9) | stricter/looser predeclared sequences | admissibility of fitted objects | deterministic failure handling | no-silent-repair principles | yes (policy is contract) |

## 15. F2 completion checklist

| check | state |
|---|---|
| candidate count = exactly 2 | PASS |
| WC-ADL draft formula mathematically complete | PASS (section 5; ratification pending) |
| TAD/PSAT draft formula mathematically complete | PASS (section 6; ratification pending) |
| all parameters defined | PASS |
| all proposed bounds explicitly listed | PASS (tables 7.1/7.2) |
| initialization contract drafted for both | PASS |
| fit-failure contract drafted for both | PASS |
| no automatic spline fallback | PASS |
| no third family | PASS |
| no F3 threshold selected / no cross-fit run / no generator selected | PASS |
| no algorithm/CVI content accessed | PASS |
| F1 contract unchanged; manifests byte-identical | PASS |
| PI ratification present | NO — expected: OWNER_DECISION_REQUIRED |

## 16. Gate status

```text
F2_status    = OWNER_DECISION_REQUIRED
F2_complete  = false
F3_allowed   = false
P-01         = OWNER_DECISION_REQUIRED (D-F2-02..04, 06, 08..10)
P-02         = OWNER_DECISION_REQUIRED (D-F2-01..03, 05, 07..10)
next_action  = PI resolution of D-F2-01..D-F2-10; then in-F2 fit-feasibility
               validation of the ratified specifications on the frozen
               trajectory set (no family comparison), then F2 freeze pass
outcome_firewall = intact
```
