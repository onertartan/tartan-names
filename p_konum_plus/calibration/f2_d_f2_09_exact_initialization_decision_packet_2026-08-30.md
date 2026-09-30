# D-F2-09 — Exact Deterministic Initialization / Multistart — Owner Decision Packet

## 0. Artifact identity / hashes / task boundary

```text
artifact_role             = D-F2-09_owner_decision_packet
status                    = DRAFT_OWNER_DECISION_REQUIRED
normative_authority       = none
governing_normative_source = v11
parent_artifact           = ART-F2 r1
parent_artifact_sha256    = d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7
recommendation_context    = MERGED_FINAL_RECOMMENDATION (sha256
                            7f61eab892e7b85d9437777ffd578a04a905bb84d01103b1bfd8a6e1d94c0f0d;
                            non-normative; PI ratification absent)
PI_ratification           = absent
F2_complete               = false
F3_allowed                = false
date                      = 2026-08-30
worktree / branch / HEAD  = G:/PycharmProjects/pkp-worktree · p_konum_plus ·
                            3e4daf47018f124e29717263e4e45fe90c8e52b8
companion_manifest        = p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv
```

Governing hashes re-verified exact this task: v11 `d136502f…`, v0 `b6b4ed83…`,
ART-F0 `56fa5093…`, ART-F1 r4a `5eceb198…`, F1 manifest `8a6034eb…`, F1 hash
table `aa86f1ea…`, ART-F2 r1 `d6f4aaf1…`, MERGED worksheet `7f61eab8…`.

Task boundary: this packet does NOT ratify anything, does NOT start ART-F2 r2,
runs NO fit-feasibility, fits NO real trajectory, and touches NO F3 content.
No self-hash inside; no sidecar. Supersession note: the earlier informal
enumeration note `p_konum_plus/provenance/f2_d09_exact_enumeration_packet_2026-08-30.md`
used partly non-rule-generated anchors and an offset-based retry set; THIS
packet replaces its recommendations (that file remains untouched historical
provenance).

## 1. Conditional upstream recommendation set (NOT ratified by this task)

All content below is `CONDITIONAL_DERIVATION_FROM_PROPOSED_PI_SET` on:
P-01 = 4-parameter double-logistic product; P-02 = 4-parameter shared-beta
generalized-Gaussian form; `u = (t-1880)/145`; prediction `z_ddof0(g)`;
locations `c_r, c_d, m in [-1, 2]` with `c_r <= c_d`; `k_min = 4`; Kural T
primitive `w_min_years = 5` with derived
`k_max = 2*ln(9)*145/5 = 127.43902548550072`; `beta in [1, 6]`,
`strict_C1_required = false`; `s_max = 3.0`;
`s_side_min(beta) = (5/145)/(ln(10)^(1/beta) - ln(10/9)^(1/beta))`; Kural S
`n_sup = #{j : g_j >= g_min + 0.5*(g_max - g_min)} >= n_min = 3`; stable
evaluation mandatory; `rng_used = false`. Derived numbers become
`DERIVED_FROM_RATIFIED_RULE` only after the PI ratifies the parent rules.

## 2. Invalidation triggers

This packet must be regenerated (same rules, new derivation) if the PI later
changes any of: P-01 exact formula; P-02 exact formula; time
parameterization; prediction operator; location horizon; `k_min`;
`w_min_years`; Kural T formula; `n_min`; Kural S formula; `beta_min`;
`beta_max`; `s_max`; or strict-C1 governance if it alters admissible P-02
support.

## 3. D-F2-09 normative requirements

v0 makes the initialization scheme part of the P-01/P-02 F2 freeze object
(v11 §26 items 1–2); the worksheet fixes the structural principles:
exact-enumeration-first; hybrid deterministic initialization; feature-based
start allowed; fixed data-independent censored-start coverage;
`rng_used = false`; `CRN_namespace_use = false`; no algorithm/CVI
information; deterministic tie handling;
`start_count = derived_after_exact_enumeration_and_deduplication`. Every
element below is executable without judgment — no "log-spaced", "several",
or "approximately" remains.

## 4. P-01 WC-ADL exact start-generation specification

| # | element | exact rule |
|---|---|---|
| 1 | location anchor-generation rule | uniform lattice `A_loc = { -1 + i/4 : i = 0..12 }` — step `Δu = 1/4` spanning the conditional horizon `[-1,2]` inclusive. Rationale: outcome-blind arithmetic rule (no hand-picked values); quarter-window resolution places ≥ 4 anchors in each censoring region (pre-window, in-window, post-window), guaranteeing censored-start coverage; endpoints give location-face coverage (§7) |
| 2 | resulting anchor set | `{-1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00}` (13) |
| 3 | ordered pair rule | `(c_r, c_d) = (A_i, A_j)` for all `i <= j` → **91 ordered pairs** |
| 4 | `c_r = c_d` allowed? | YES — equal midpoints are the zero-plateau symmetric life-cycle starts, a scientifically meaningful interior shape class |
| 5 | k-base levels | geometric 3-point lattice on the conditional `[k_min, k_max]`: `K_i = 4 * (k_max/4)^(i/2), i = 0,1,2` → `K = { 4.0, 22.577778941738334, 127.43902548550072 }` (endpoints + geometric midpoint; rule-generated) |
| 6 | asymmetry representation | independent per-side anchors: full cross product `(k_r, k_d) in K × K` (9 combos); realized asymmetry ratios `k_r/k_d in {1, 5.644…, 31.860…}` in both directions |
| 7 | mapping | direct: `(k_r, k_d) = (K_a, K_b)`, all `(a, b)` |
| 8 | filtering | bounds and Kural T are satisfied BY CONSTRUCTION (lattice endpoints = bounds; verified numerically for all 819 rows); Kural S evaluated on the stabilized curve for every start → 88 rejected (`KURAL_S_FAIL`), all logged in the manifest |
| 9 | feature-based start formula | `(c_r, c_d, k_r, k_d) = (u* - 1/8, u* + 1/8, K_1, K_1)` with `K_1 = 22.577778941738334` (the lattice midpoint — rule-tied) and half-offset `Δu/2 = 1/8` (rule-tied); `u*` per §6 |
| 10 | invalid feature start | REJECT (log `FEATURE_START_REJECTED`), continue with the fixed grid only; NO clipping, no substitution |
| 11 | boundary-start policy | none beyond the lattice — see §7 |
| 12 | duplicate rule | §9 — exact float64 tuple equality; 0 duplicates arise in the fixed grid (asserted) |
| 13 | start ordering | ascending lexicographic on canonical order `(c_r, c_d, k_r, k_d)` |
| 14 | retained grid-start count | **731** (of 819; derived, not imposed) |
| 15 | total incl. feature start | **731 + 1 per trajectory as a rule** (the feature start is trajectory-dependent; if its tuple coincides with a grid tuple for some trajectory, the per-trajectory dedup rule drops it — so the per-trajectory total is 731 or 732, mechanically determined) |

## 5. P-02 TAD/PSAT exact start-generation specification

| # | element | exact rule |
|---|---|---|
| 1 | m anchor-generation rule | identical lattice rule as P-01 item 1 |
| 2 | resulting m-anchor set | the same 13 values |
| 3 | beta anchor set | geometric 3-point lattice on `[1, 6]`: `B_i = 6^(i/2), i = 0,1,2` → `B = { 1.0, 2.449489742783178, 6.0 }` |
| 4 | scale-base rule (conditional on beta) | geometric 3-point lattice on `[s_side_min(beta), 3.0]`: `S_i(beta) = s_side_min(beta) * (3/s_side_min(beta))^(i/2)`; exact values: beta=1 → `{0.01569377976942823, 0.21698234791863757, 3.0}`; beta=2.449489742783178 → `{0.03425647986552569, 0.32057672965544004, 3.0}`; beta=6 → `{0.07465689442188805, 0.47325541018108197, 3.0}` |
| 5 | use of `s_side_min(beta)` | it IS the lower lattice endpoint (exact formula evaluated at each beta anchor), so Kural T holds by construction (bound inclusive: width exactly `w_min` is admissible, `>=`) |
| 6 | asymmetry representation | independent per-side anchors: `(s_l, s_r) in S(beta) × S(beta)` (9 combos per beta) |
| 7 | mapping | direct cross product |
| 8 | filtering | beta-dependent Kural T + `s_max` by construction (verified numerically for all 351 rows); Kural S on the stabilized curve → 90 rejected (`KURAL_S_FAIL`), all logged |
| 9 | feature-based start formula | `(m, s_l, s_r, beta) = (u*, S_1(B_1), S_1(B_1), B_1) = (u*, 0.32057672965544004, 0.32057672965544004, 2.449489742783178)` — all three non-location values are the lattice midpoints (rule-tied) |
| 10 | invalid feature start | REJECT + log, grid-only; no clipping |
| 11 | boundary-start policy | none beyond the lattice — §7 |
| 12 | duplicate rule | §9; 0 duplicates arise (asserted) |
| 13 | start ordering | ascending lexicographic on `(m, s_l, s_r, beta)` |
| 14 | retained grid-start count | **261** (of 351; derived) |
| 15 | total incl. feature start | **261 + 1 per trajectory as a rule** (same per-trajectory dedup semantics as P-01) |

## 6. Feature-based start rules

```text
j_star = min{ j : x_j = max_k x_k }        (smallest-index argmax; exact tie rule)
u_star = j_star / 145
```

Uses ONLY the current trajectory's own frozen z-vector — no algorithm/CVI
information, no generator-comparison information, no other trajectories, no
F3 content. Parameter mapping per §4.9 / §5.9: location(s) at `u_star` with
rule-tied half-offset (P-01) and all non-location components at the geometric
lattice midpoints — every constant is derived from the lattice rules, none is
free. Validity: the constructed start must satisfy the conditional bounds AND
Kural T AND Kural S; if not → `FEATURE_START_REJECTED` (logged), fixed grid
only. Since `u_star in [0,1]`, locations always lie inside `[-1,2]`; Kural
T/S are checked mechanically per trajectory. Demonstrated executable on a
synthetic vector (§14).

## 7. Boundary-start policy

**No separate boundary starts.** Rationale: the lattice ENDPOINTS already
provide systematic face coverage — locations reach `-1` and `2`; `k` reaches
`4` and `127.43902548550072`; `s` reaches `s_side_min(beta)` (Kural-T face)
and `3.0`; `beta` reaches `1` and `6`. Deliberately degenerate box corners
are NOT inserted; corner-adjacent lattice combinations survive only if they
mechanically pass Kural S (88 + 90 such combinations were rejected — exactly
the S-NEG-adjacent/degenerate cases the worksheet warns about). This is the
smallest policy satisfying "location-boundary coverage explicit, non-location
interior-biased, no degenerate corners by fiat".

## 8. Kural T / Kural S filtering order

```text
construction (lattices)            -> bounds + Kural T hold by construction
numerical Kural-T verification     -> transition-width check per side (all pass; belt-and-suspenders)
stabilized evaluation of the curve -> softplus / log-domain, max-shift, exp
finiteness check                   -> all finite (no NONFINITE occurrences)
Kural S (n_sup >= 3)               -> reject with KURAL_S_FAIL, keep row in manifest
```

Rejected rows are retained in the manifest with reasons — the filter is
auditable, not silent.

## 9. Deduplication and ordering

```text
canonical parameter order : (c_r, c_d, k_r, k_d) / (m, s_l, s_r, beta)
comparison rule           : exact IEEE-754 float64 tuple equality
tolerance                 : none — unnecessary, because every tuple is produced by one
                            exact formula evaluation path (identical constructions yield
                            bit-identical doubles); no near-duplicates exist by design
retained duplicate        : first in ascending canonical sort (vacuous in the fixed grid: 0 duplicates)
output ordering           : ascending lexicographic canonical sort within family; families P-01 then P-02
platform note             : ordering is by value comparison of sorted lists — no unordered sets
```

Per-trajectory rule: a feature-based start equal (exact float64 tuple) to a
retained grid start is dropped for that trajectory.

## 10. Retry / fallback separation

Scientific object = the deterministic start-generation contract above.
Optimizer brand/library is CLASS_C and never a scientific pin.

**Recommendation: Option A — no new retry starts.** One predeclared CLASS_C
fallback optimizer re-runs the exact same deterministic start set when the
primary optimizer raises a purely numerical error. Rationale: smallest
contract; the 731/261-start coverage already spans the admissible domain
faces and interior; no model-only numerical argument requires a second start
set. (Option B — an exact second deterministic start set — remains the listed
alternative; if ever chosen, every offset must be enumerated exactly.) After
primary + fallback exhaustion on all starts: `FAMILY_FIT_FAILURE(code)`,
logged. No RNG anywhere.

CLASS_C implementation candidates (predeclared, non-scientific): primary
bounded local optimizer candidate L-BFGS-B; fallback candidate trust-constr;
tolerance literals `gtol = 1e-10`, `ftol = 1e-12`, `maxiter = 500`. If any
class-C literal starts changing which fits are admissible, it stops being
class-C and returns to the PI (worksheet D-F2-10.6 rule).

## 11. Objective-tie determinism (CLASS_C comparator)

```text
tie iff |L_a - L_b| <= atol + rtol * max(|L_a|, |L_b|)
atol = 1e-12        rtol = 1e-9
winner among tied starts = ascending lexicographic smallest canonical parameter tuple
```

Implementation determinism only — not family science. No historical selector
tie rule was imported.

## 12. Exact start-count derivation

| stage | P-01 | P-02 |
|---|---|---|
| raw rule-generated grid | 819 (91 pairs × 9 k-combos) | 351 (13 m × 3 beta × 9 scale-combos) |
| bounds + Kural T | 819 (by construction; verified) | 351 (by construction; verified) |
| after Kural S (stabilized, n_min = 3) | **731** | **261** |
| duplicates removed | 0 (none arise) | 0 |
| separate boundary starts | 0 (policy §7) | 0 |
| feature-based start | +1 per trajectory (rule; per-trajectory dedup may reduce to +0) | same |

Counts are DERIVED from the ratifiable rules — never imposed. Any
invalidation trigger (§2) regenerates them mechanically.

## 13. Machine-readable manifest summary

`f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv` — 1,170 data rows
(819 P-01 + 351 P-02; retained AND rejected, with reasons), columns exactly:
`family, start_id, start_type, parameter_order, parameter_values,
source_rule, conditional_upstream_decisions, Kural_T_pass, Kural_S_pass,
retained, rejection_reason`. Rows deterministic, ascending-sorted within
family; `parameter_values` at full float64 repr precision (grid exactly
reproducible); `start_type = fixed_grid` only — the feature-based start is
symbolic (this packet §6) and is NOT expanded with real SSA data; no real
trajectory identifiers appear.

## 14. Model-only enumeration QC (executed this task)

```text
double-run reproducibility (full rebuild, element-wise)   = identical
all retained start curves finite                          = yes (0 NONFINITE)
all starts inside conditional bounds                      = yes (by construction + verified)
Kural T numerical verification per side                   = pass for all 1,170 rows
Kural S evaluated with stabilized (softplus/log-domain)   = yes; 88 + 90 rejections logged
duplicate count                                            = 0 (assertion passed)
sort order reproducible                                    = yes
feature-start symbolic rule executed on a synthetic vector = yes (j* = 90, u* = 0.6206896551724138;
                                                             P-01 and P-02 constructions valid, Kural-S-passing)
objective-tie comparator determinism                       = verified (equal -> tie; 5e-10 -> tie; 1e-6 -> distinct)
parameter-recovery scores / rates / family comparison      = NOT computed (prohibited)
real trajectories touched                                  = none
```

## 15. PI decision table (smallest closing set — status all OWNER_DECISION_REQUIRED)

| ID | item | recommended | alternative(s) | why recommended | scientific consequence | numerical consequence | family-altering if changed later? |
|---|---|---|---|---|---|---|---|
| D-F2-09.1 | P-01 location-anchor rule/set | quarter-window lattice, 13 anchors (§4.1–2) | Δu = 1/2 (7 anchors, 28 pairs) or Δu = 1/8 (25 anchors, 325 pairs), same rule | smallest rule-generated set with ≥4 anchors per censoring region | censored-start coverage | grid size driver | no (reproducibility contract only) |
| D-F2-09.2 | P-01 k/asymmetry rule | geometric 3-point `K` × `K` cross product (§4.5–7) | geometric 5-point (25 combos); base×ratio scheme | endpoints+midpoint rule; asymmetry emerges from cross product; zero filter waste | slow/moderate/fast transition coverage | 9 combos/pair | no |
| D-F2-09.3 | P-02 m/beta anchor rule/set | same lattice ×  `B = {1, 6^(1/2), 6}` (§5.1–3) | finer beta lattice `6^(i/4)` (5 anchors) | same rule family as P-01/beta endpoints incl. cusp and flat-top faces | shape-exponent coverage | 39 (m, beta) cells | no |
| D-F2-09.4 | P-02 scale/asymmetry rule | beta-conditional geometric 3-point on `[s_side_min(beta), 3]`, cross product (§5.4–7) | 5-point variant | lower endpoint = exact Kural-T face; rule-tied | Kural-T-consistent scale coverage | 9 combos per (m, beta) | no |
| D-F2-09.5 | feature-based-start rules | min-index argmax; midpoint mapping; reject-if-invalid (§6) | omit feature start entirely | one data-adapted start with zero free constants; no silent clipping | per-trajectory local start | +1 start/trajectory | no |
| D-F2-09.6 | boundary-start policy | none beyond lattice faces (§7) | explicit face-midpoint list | lattice endpoints already cover faces; corners only via mechanical Kural-S survival | avoids degenerate-corner starts by fiat | 0 extra rows | no |
| D-F2-09.7 | retry-start policy | Option A — same set, class-C fallback optimizer (§10) | Option B — exact second deterministic set | smallest contract; no model-only argument requires B | none | one extra optimizer pass on failure | no |
| D-F2-09.8 | dedup/order rule | exact float64 equality; ascending lexicographic (§9) | tolerance-based dedup | tuples are exact-construction; tolerance unnecessary | none | deterministic manifest | no |
| D-F2-09.9 | objective-tie comparator | atol 1e-12 / rtol 1e-9 + lexicographic smallest (§11) | other predeclared literals | conventional strict literals; class-C | none | deterministic winner | no |
| D-F2-09.10 | start-count semantics | counts DERIVED after enumeration+filter+dedup: 731 / 261 (+1 rule); regenerate on any §2 trigger | — (semantics, not a number) | worksheet governance: counts never imposed | none | compute-cost visibility (731×906 and 261×906 optimizer runs upper bound per family) | no |

## 16. D-F2-09 completion checklist

| check | state |
|---|---|
| every §8/§9 requirement item (15 + 15) specified exactly | PASS |
| no vague phrases (log-spaced / several / approximately / moderate) remain as operational elements | PASS |
| anchors rule-generated (no arbitrary nice numbers) | PASS |
| feature start symbolic, deterministic, reject-if-invalid | PASS |
| boundary policy explicit, no degenerate corners by fiat | PASS |
| retry decided (Option A recommended), no RNG | PASS |
| dedup/tie rules exact | PASS |
| counts derived + reproducible (double-run identical) | PASS |
| manifest CSV deterministic, all rows incl. rejections | PASS |
| smallest PI set returned (10 decisions) | PASS |
| PI approval filled | NO — deliberately absent |

## 17. Firewall / gate status

```text
ART_F2_r2_started = false          PI_ratification = false
fit_feasibility_execution = false  real_SSA_fit = false
real_SSA_subset_fit = false        generator_adequacy_comparison = false
generator_selection = false        F3_execution = false
algorithm_CVI_execution = false    algorithm_CVI_outcome_access = false
legacy_performance_content_access = false
results_directory_opened = false   pre_v11_tie_break_text_used = false
rng_used = false                   CRN_namespace_use = false

D-F2-09_status       = OWNER_DECISION_REQUIRED
D-F2-09_exact_packet = READY
F2_status            = OWNER_DECISION_REQUIRED
F2_complete          = false
F3_allowed           = false
```
