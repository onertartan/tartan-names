# p_konum_plus — F3 STEP 1 — P03/P04/P05 Decision Packet — End-of-Task Response (verbatim)

```text
artifact_role = operational end-of-task chat response, saved verbatim on user request
status        = NON-NORMATIVE
date          = 2026-09-02
task          = F3 STEP 1 — exact P03/P04/P05 PI decision specification and ratification packet
              (no adequacy execution; no PI acceptance claimed; nothing frozen)
```

---

Hashes exact (v11 `d136502f…`, FREEZE r1 `ee2cb99d…`, preflight record `262f8e41…`, HEAD unchanged, no tracked modifications). No fit, cross-fit, measurement, or file write is performed in this task. The complete packet follows.

# F3 STEP 1 — Exact P03/P04/P05 PI Decision Specification and Ratification Packet

**Status: NON-NORMATIVE recommendation packet. Nothing here is self-ratified. All frozen inputs are cited from FREEZE r1 (`ee2cb99d…`) and the frozen F1 record; no candidate-specific result exists or was generated.**

Frozen structural facts used (and nothing else): 906 eligible trajectories (435 F / 471 M), full-support 1880–2025, T=146, u=(t−1880)/145; data z-space frozen in F1 (row z_ddof0); D-F2-08 unweighted LS in frozen z-space, L = 2T(1−ρ); prediction = z_ddof0(g) over the full 146-grid; P-01 and P-02 each have exactly 4 parameters; Kural T/S admissibility; D-F2-09 start grid (731/261, data-independent in θ-space); frozen failure taxonomy; `rng_used = false` convention.

## 1. Decision-completeness audit of the preflight packet (Task in §3)

Test applied to every preflight item: *could two reasonable executors implement it differently from the same text?*

| # | finding | class |
|---|---|---|
| A1 | **X-A (across-trajectory K-fold) cannot be the primary cross-fit mechanism.** Answer to the mandated question: it would not create cross-fitted reconstruction at all — both families are fitted independently per trajectory, no parameter is shared across trajectories, so a model fitted on training trajectories yields **no prediction whatsoever** for a held-out trajectory. X-A partitions IDs without producing any out-of-sample reconstruction quantity. | blocking_for_F3_execution — resolved in this packet (P05 primary = within-trajectory; X-A **rejected**, and no outer calibration role is retained for it because no recommended threshold-derivation type below needs one — retaining it would add hidden researcher degrees of freedom, §7 principle 6) |
| A2 | Preflight P03 named decision *topics* but no exact per-criterion statistics — two executors would diverge immediately. | blocking_for_F3_execution — resolved by the six criterion contracts below |
| A3 | Spline benchmark implementation unpinned (CL-F3-PRE-01). | blocking_for_F3_execution — resolved by D-P03-4 below |
| A4 | Criterion-4 probe construction unspecified. | blocking_for_F3_execution — resolved by D-P03-5 below |
| A5 | Preflight tie-break option T-C (parsimony-first) is structurally non-decisive: both families have exactly 4 parameters. | cleanup — T-C dropped from the recommendation |
| A6 | v11's literal phrase "shape-constrained low-df spline" does not itself specify the constraint; the interpretation must be a PI-ratified literal (an execution pin, not new methodology). | informational |
| A7 | F2 determinism scope (same-process only) propagates into the P05 reproducibility claim below. | informational |

None of this reopens F2; `F3_ENTRY_READY = true` is unchanged.

## 2. RECOMMENDED_P03_CONTRACT — exact derivation contract per criterion

**Common fields (apply to every criterion unless overridden).**
`unit_of_evaluation` = one eligible trajectory, fitted per family under the unmodified FREEZE r1 contract (all starts, frozen optimizer, frozen admissibility). `aggregation_unit` = trajectory-level statistic → **median** across trajectories (pre-declared; robust, no tuning) → per-sex value. `sex_handling` = **sex_specific**: every criterion is derived and gated separately for F (n=435) and M (n=471); a family passes a criterion only if it passes in **both** sexes. *Justification from frozen F1 structure only:* the two sexes are separate frozen samples of different sizes and independently frozen eligibility; pooling would let adequacy in the larger stratum mask inadequacy in the smaller, and per-sex gating requires no new data assumptions. `missing_or_failed_fit_handling` = a trajectory with no eligible full-data fit (per frozen taxonomy) counts against C1 and is excluded from the complete-case sets of C2–C5, with the exclusion share logged per sex. `family_level_aggregation_rule` = criteria evaluated in the frozen order C1→C6; first failed criterion ⇒ family FAIL (all six still measured and logged for provenance). `provenance_source` = v11 §5 order (V11_LITERAL); every operationalization below = POST_V11 execution pin for PI ratification. Equivalence tolerances live in P04, not here. `P03_threshold_values = NOT_COMPUTED` throughout — only rules and rule-literals are specified.

**C1 — morphology coverage.**
`exact_statistic`: coverage_F,s = (# trajectories of sex s with ≥1 eligible admissible full-data fit under FREEZE r1) / n_s. `direction`: higher. `reference_distribution`: none needed. `threshold_derivation_type` = **absolute_structural**. `predeclared_literals`: coverage floor **c_cov = 0.90** (alternatives 0.85 / 0.95). `pass_fail`: coverage_F,s ≥ c_cov in both sexes. `how_value_computed`: direct share; the floor is the rule literal itself (no measurement-derived component).

**C2 — cross-fitted reconstruction / predictive fit.**
`exact_statistic`: ρ_cv,i = Pearson correlation between the frozen F1 z-trajectory z_i and the assembled out-of-sample prediction ĝ_cv,i produced by the P05 primary scheme (every year predicted exactly once by a fold that did not train on it). `direction`: higher. `aggregation`: M_F,s = median_i ρ_cv,i over the complete-case set of sex s. `reference_distribution`: the same statistic computed for the spline benchmark, M_S,s, under the identical P05 scheme. `threshold_derivation_type` = **spline_relative_margin**. `predeclared_literals`: **δ₂ = 0.05** (alternatives 0.03 / 0.10). `how_value_computed`: threshold_s = M_S,s − δ₂, computed only after measurement under this frozen rule. `pass_fail`: M_F,s ≥ M_S,s − δ₂ in both sexes. `failed-fold handling`: per P05 (trajectory excluded from complete-case set if any fold invalid; share logged).

**C3 — systematic residual morphology / structure.**
`exact_statistic`: φ_i = |lag-1 sample autocorrelation of the full-data fit residual series r_t = z_t − ĝ_t| (ĝ = frozen full-grid standardized prediction of the best eligible fit); `direction`: lower. `aggregation`: median per sex. `reference_distribution`: same statistic for the spline benchmark's full-data residuals. `threshold_derivation_type` = **spline_relative_margin**. `predeclared_literals`: **δ₃ = 0.05** (alternatives 0.03 / 0.10). `pass_fail`: median|φ|_F,s ≤ median|φ|_S,s + δ₃ in both sexes. (Spline-relative because real SSA trajectories carry temporal dependence the benchmark also cannot remove; the criterion tests *excess* systematic structure, not absolute whiteness.)

**C4 — censored-case identifiability (diagnostic only).**
Mandatory F1-consistency statement: nothing is imputed; `missing ≠ zero`; no [0,4] interval semantics; all 906 inputs remain FULL-support. The probe *masks observed years*, it never fabricates censored observations.
`what is masked/truncated`: for each trajectory, two deterministic probe variants — mask the first **E** years (left truncation) and, separately, the last **E** years (right truncation), **E = 15** pre-declared (alternatives 10 / 20). `what remains observed`: the other 146−E years, unchanged frozen z-values. `what is being identified`: whether family parameters remain identifiable when window truncation hides a feature edge — the real phenomenon already frozen into the design as clipped-at-window morphology. `statistics measured`: (4a) ident_F,s = share of (trajectory × variant) probes with an eligible admissible truncated-window refit (same FREEZE r1 contract, loss masked to observed years, full-grid z_ddof0 prediction convention unchanged); (4b) agree_i = Pearson correlation, over the still-observed years, between the truncated-fit prediction and the full-data-fit prediction; median per sex. `direction`: higher for both. `threshold_derivation_type`: 4a **absolute_structural**, literal **c_ident = 0.85** (alternatives 0.80 / 0.90); 4b **spline_relative_margin**, literal **δ₄ = 0.05**, spline subjected to the identical probe. `why adequacy-diagnostic only`: probes are computed per family in isolation, feed only the C4 gate, and no cross-family quantity is formed outside the frozen P04 comparator.

**C5 — parameter stability.**
`exact_statistic`: from the K training fits of the P05 primary scheme, for trajectory i: s_stab,i = max over the family's 4 parameters of IQR_k(θ_j,k) / W_j, where W_j = frozen FREEZE-r1 bound width of parameter j (for P-02's shared β and side-scales, W_j from the frozen supports; scale parameters with β-dependent lower bound use W_j evaluated at the fitted β per fold — pinned: use the frozen *outer* support width [s_side_min(1), 3.0] for both side-scales, a constant). `direction`: lower. `aggregation`: median per sex, complete-case (all K folds eligible). `reference_distribution`: none (spline parameters are not comparable). `threshold_derivation_type` = **absolute_structural**. `predeclared_literals`: **c_stab = 0.10** (alternatives 0.05 / 0.20). `pass_fail`: median s_stab ≤ c_stab in both sexes.

**C6 — parsimony.**
`exact_statistic`: parameter count k_F (= 4 for both families, frozen). `direction`: lower. `threshold_derivation_type` = **absolute_structural**: pass iff k_F ≤ df_spline (the D-P03-4 literal). `pass_fail`: structural; both candidates pass by construction (4 ≤ 8). C6 remains in the hierarchy for the P04 comparator, where it is decisive only if the families' parameter counts ever differ (they do not, under the closed candidate set — recorded transparently).

**Reference population decision (D-P03-2):** `sex_specific` derivation with both-sexes-must-pass gating, as specified above; rejected alternative = pooled-906 (masks stratum-specific inadequacy; no compensating benefit given both strata are large).

### D-P03-4 — spline adequacy benchmark, exact pin (closes CL-F3-PRE-01)

```text
representation      = cubic B-spline (degree 3) in u on [0,1], fitted in frozen z-space
df / knot rule      = df_spline = 8: 4 interior knots equally spaced at u = {0.2, 0.4, 0.6, 0.8}
                      (alternatives df = 6 or 10 with the same equal-spacing rule)
shape constraints   = realized as the hard low-df cap + fixed deterministic knots
                      (the v11 phrase "shape-constrained" is interpreted as
                      complexity/shape restriction via df, an explicit PI literal decision;
                      no monotonicity/unimodality constraint is imposed — those would
                      contradict the frozen multi-wave morphology classes)
boundary behavior   = natural evaluation on [0,1] only; no extrapolation, no periodicity
fit objective       = unweighted least squares against the frozen z-trajectory
                      restricted to the same observation set as the family fit being
                      benchmarked (full grid for C1/C3; P05 training mask for C2;
                      probe mask for C4)
normalization       = fitted curve then standardized by full-grid z_ddof0, identical to
                      the frozen F2 prediction convention, before any rho statistic
initialization      = none needed (linear LS; closed-form normal equations)
failure handling    = zero-variance fitted curve or non-finite solution => spline-fit
                      failure, logged, trajectory excluded from that spline statistic
determinism rule    = fully deterministic; rng_used = false
role                = adequacy_benchmark only; automatic_primary_fallback = false;
                      never a third candidate
```

### D-P03-5 — criterion-4 probe literals

E = 15 years; two variants (left, right) per trajectory; same FREEZE r1 fitting contract with loss masked to observed years; full-grid z_ddof0 unchanged; Kural T/S evaluated unchanged on the full stabilized grid (admissibility is a property of θ). All literals PI-modifiable.

## 3. RECOMMENDED_P05_SCHEME — primary cross-fit contract

```text
crossfit_unit           = contiguous year-blocks WITHIN each trajectory
number_of_folds         = K = 5 (alternative: 10)
fold_construction       = deterministic index blocks: fold b (b = 0..4) holds out year
                          indices [floor(b*146/5), floor((b+1)*146/5)) on the frozen
                          1880-2025 grid; sizes 29/29/30/29/29; identical for every
                          trajectory, sex, and family
temporal_block_definition = the contiguous index ranges above; no wrapping
edge_block_handling     = first/last blocks include the window edges and are retained
                          (edge truncation is a frozen design feature, never wrapped)
gap_rule                = no guard gap (g = 0); alternative g = 2 years, not recommended:
                          the frozen D-F2-08 objective models no serial dependence, and
                          gaps shrink training support, interacting with Kural S
training_year_definition = all 146 - |block| years outside the held-out block
heldout_year_definition  = the block
fit_objective_on_training = frozen D-F2-08 unweighted LS in frozen z-space, with the sum
                          restricted to training indices; NOTHING else changes:
                          prediction remains z_ddof0 over the FULL 146-grid (frozen F2
                          convention explicitly unchanged), starts = the frozen
                          data-independent D-F2-09 grid, optimizer/fallback/admissibility
                          = FREEZE r1 verbatim
prediction_on_heldout    = the training-fitted, full-grid-standardized curve evaluated at
                          held-out years; assembled over the 5 folds so every year is
                          predicted exactly once out-of-sample -> ghat_cv (146 values)
statistic                = rho_cv = corr(z, ghat_cv) per trajectory (consumed by C2)
aggregation              = within trajectory: single rho_cv; across trajectories: median;
                          sex: per-sex, both-must-pass (C2 rule)
failed_fold_handling     = any fold with no eligible training fit -> trajectory marked
                          crossfit-incomplete, excluded from C2/C5 complete-case sets,
                          share logged per sex and family
minimum_valid_folds      = 5 of 5 for inclusion
deterministic_fold_identity = pure function of year index; identical everywhere
rng_used                 = false
cross_process_reproducibility_claim = semantic determinism under the frozen contract;
                          bitwise cross-process/cross-platform equality NOT claimed
                          (consistent with the frozen F2 determinism scope)
```

**Decision principle satisfied:** every held-out year receives a genuine out-of-sample reconstruction from parameters that never saw it — this *is* cross-fitted reconstruction/predictive fit. **X-A rejected** (audit item A1): no shared parameters ⇒ no held-out-trajectory prediction ⇒ not cross-fit; and no outer-calibration role for X-A is retained, because no recommended derivation type requires a held-out threshold-estimation sample (spline-relative margins and structural floors are computed on the same complete-case sets, symmetrically for family and benchmark). X-B-as-primary is exactly what is specified above; X-C (hybrid) rejected as complexity without a consuming criterion.

## 4. RECOMMENDED_P04_RULE — exact deterministic tie-break (T-A, fully specified)

```text
invocation            = only if BOTH families PASS all six P03 gates (both sexes);
                        if exactly one passes, it is selected without tie-break;
                        if none passes: STOP, action = redesign
comparison_quantities = per criterion, one pre-declared scalar, worse-sex convention
                        (min over sexes for higher-better, max over sexes for lower-better):
                        c1 coverage share | c2 median rho_cv | c3 median |phi|
                        | c4a ident share, then c4b median agree (sub-levels, in order)
                        | c5 median s_stab | c6 parameter count
equivalence_tolerances = tau1 = 0.01 (share) ; tau2 = 0.005 (rho) ; tau3 = 0.01 ;
                        tau4a = 0.01, tau4b = 0.005 ; tau5 = 0.01 ; tau6 = 0 (exact)
lexicographic_transition = compare criteria strictly in the frozen order 1 -> 6
                        (with 4a before 4b); if |delta_c| <= tau_c the criterion is
                        EQUIVALENT and evaluation moves to the next; otherwise the
                        family better in the frozen direction is selected and the
                        procedure terminates
non_comparable_rule   = if a criterion's scalar is undefined for at least one family
                        (e.g., empty complete-case set), the criterion is logged
                        NONCOMPARABLE and skipped deterministically
all_equivalent        = terminal deterministic neutral fallback
terminal_fallback     = ascending lexicographic order of the frozen family IDs:
                        "P-01" < "P-02"  =>  P-01 selected.
                        Outcome-blind and measurement-independent (IDs were assigned by
                        specification order in F2, before any measurement existed),
                        legacy-neutral (no historical pipeline involved), deterministic.
historical_privilege  = none; Ward+CH and every legacy pipeline have zero tie-break role
```

All tolerances are rule literals for PI ratification, fixed before any measurement; they are also reused nowhere else (no double-use).

## 5. Why-recommended / rejected-alternative summary (§7 requirements)

| recommendation | why_recommended | main_alternative_rejected | reason_for_rejection | remaining_risk |
|---|---|---|---|---|
| P03 contract (six exact criteria, sex-specific, spline-relative + structural floors) | every statistic is computable from frozen machinery, candidate-blind, benchmark-anchored exactly where v11 gives the spline that role | pooled-sex derivation; family-self-quantile thresholds | pooling masks stratum inadequacy; self-quantiles are circular (threshold would move with the candidate it judges) | margin/floor literals are judgment calls — mitigated by PI MODIFY authority and pre-measurement freezing |
| D-P03-4 spline pin (cubic B-spline, df=8, fixed knots, LS in frozen z-space) | deterministic, initialization-free, convex, reproducible; benchmark strictly more flexible than 4-param families yet low-df | penalized/monotone/unimodal spline variants | penalty weight = extra researcher dof; monotone/unimodal constraints contradict frozen multi-wave morphology classes | "shape-constrained" interpreted as df-cap — flagged (A6) as explicit PI literal |
| P05 within-trajectory 5-fold blocked scheme | produces a true out-of-sample reconstruction for every year; only frozen-objective masking, nothing else altered | X-A across-trajectory K-fold | produces no prediction for held-out trajectories (no shared parameters) — fails the v11 phrase it claims to implement | block truncation interacts with Kural S on some morphologies — visible in logged fold-failure shares, gated by complete-case handling |
| P04 T-A lexicographic + neutral terminal fallback | preserves the already-frozen six-level hierarchy verbatim; every step deterministic and pre-frozen | T-B single-scalar composite | collapsing six frozen criteria into one scalar re-weights the hierarchy v11 froze | tolerance literals could in principle decide the winner — they are frozen pre-measurement and PI-owned, which is the designed mitigation |

Special attentions (§7): thresholds never depend on which candidate they favor (spline-relative/structural only); P05 genuinely measures prediction; the spline is benchmark-only, never fallback (double-use avoided — it appears in thresholds, not in selection); the six-level hierarchy is untouched; C4 respects OD-7 exactly (masking observed data only); every rule uses the minimum machinery needed (X-A dropped, T-C dropped, no hybrid).

## 6. Ratification-ready table

| decision_id | exact decision needed | Claude recommendation | alternatives | PI action |
|---|---|---|---|---|
| D-P03-1 | per-criterion exact statistics C1–C6 as specified in §2 | adopt the six contracts verbatim | substitute statistics (e.g., mean for median; run-length for lag-1 autocorr) | ACCEPT / MODIFY |
| D-P03-2 | reference population | sex_specific; both sexes must pass every gate | pooled-906; sex-specific with single-sex pass | ACCEPT / MODIFY |
| D-P03-3 | rule literals | c_cov=0.90; δ₂=0.05; δ₃=0.05; c_ident=0.85; δ₄=0.05; c_stab=0.10 | listed per criterion in §2 | ACCEPT / MODIFY |
| D-P03-4 | spline benchmark pin | cubic B-spline, df=8, knots u={0.2,0.4,0.6,0.8}, LS in frozen z-space, z_ddof0, deterministic, benchmark-only | df=6 or 10; penalized variant | ACCEPT / MODIFY |
| D-P03-5 | criterion-4 probe | E=15, left+right variants, masked-loss refit, 4a/4b statistics | E=10 or 20 | ACCEPT / MODIFY |
| D-P04 | exact tie-break | T-A lexicographic, worse-sex scalars, tolerances τ=(0.01, 0.005, 0.01, 0.01/0.005, 0.01, 0), NONCOMPARABLE-skip, terminal fallback "P-01"<"P-02" | T-B composite scalar; different τ literals | ACCEPT / MODIFY |
| D-P05 | primary cross-fit scheme | within-trajectory contiguous 5-fold, no gap, masked frozen objective, full-grid z_ddof0 unchanged, frozen starts/optimizer, 5/5-fold completeness, rng_used=false; X-A rejected outright | K=10; g=2-year guard gap | ACCEPT / MODIFY |

Every row carries its complete operational definition in §§2–4; PI acceptance of a row creates a frozen pin with no further interpretation round.

```text
RATIFICATION_READY = true
```

No PI acceptance is claimed; nothing is frozen; no candidate result exists.

---

## End-of-task schema

```text
GLOBAL_BLOCKER = none

F3_ENTRY_READY = true

F3_EXECUTION_READY = false

P03_derivation_rule_status = OWNER_RATIFICATION_REQUIRED
P03_threshold_values       = NOT_COMPUTED
P04_status                 = OWNER_DECISION_REQUIRED
P05_status                 = OWNER_DECISION_REQUIRED

RATIFICATION_READY = true

candidate_specific_fit = false
crossfit_execution = false
adequacy_measurement = false
generator_selected = false

F3_started = false
commit = false

NEXT_ACTION =
PI review and explicit ratification/modification of the exact
P03/P04/P05 decision packet
```
