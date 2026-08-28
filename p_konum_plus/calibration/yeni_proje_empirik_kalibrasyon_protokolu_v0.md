# yeni_proje_empirik_kalibrasyon_protokolu_v0
## New-Project Empirical Calibration Protocol v0 — F0–F12 execution structure (DRAFT)

---

# 0. Document identity, role, and precedence

## 0.1 Identity

```text
document                 = yeni_proje_empirik_kalibrasyon_protokolu_v0.md
document_role            = normative_working_artifact
protocol_status          = DRAFT
date                     = 2026-08-28
worktree                 = G:/PycharmProjects/pkp-worktree
branch                   = p_konum_plus
drafting_context_HEAD    = cf73a83f050056949a4e9513627576ad0368c683
parent_normative_source  = p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
parent_normative_sha256  = d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3
```

## 0.2 Drafting-task class (provenance of this draft)

This v0 was produced under a governance-only construction task:

```text
protocol_construction_only   = true
calibration_execution        = false
scientific_run               = false
algorithm_CVI_outcome_access = false
legacy_continuation          = false
```

No calibration measurement was performed, no generator was fitted, no bank was
generated, no algorithm or CVI was run, and no performance outcome (legacy or
new) was read while producing this document. This document introduces **no new
methodological decision**: every closed item below is closed because v11 closed
it; every open item below is open because v11 left it open.

## 0.3 Precedence

```text
normative_methodology_source =
    "ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md"
v11_wins = true
```

- If any older document (including prior ChatGPT/Claude v11 terminal artifacts)
  differs from v11 in wording, granularity, freeze-stage placement, terminology,
  or field naming, **v11 governs** (v11 §0, §28). No methodology review cycle is
  opened merely to reconcile wording (v11 §25 item 30).
- `p_konum_plus/provenance/bootstrap_isolation_audit_2026-08-28.md` is
  **NON-NORMATIVE operational provenance** only: it establishes worktree
  isolation and firewall state; it carries no methodological authority.
- Legacy v5.3 artifacts (protocol, deviation annex, run matrix, results) are
  bit-immutable read-only historical provenance (v11 §0.2). Legacy scientific
  choices are **not** automatic normative inheritance (v11 §0.2, §17).

## 0.4 What this protocol is

This protocol translates the v11 FINAL NORMATIVE contract into an executable
F0–F12 calibration/freeze protocol. It defines, for each gate: what is already
closed, what must be pinned, with what evidence, by whom, and what stops the
line. Execution of the gates (starting with F0/F1) is **not** part of this
document and has **not started**.

## 0.5 Revision log

| rev | date | change | methodology impact |
|---|---|---|---|
| v0 initial draft | 2026-08-28 | initial F0–F12 translation of v11 (SHA256 `769ef8798d3082df192cc670175a0bee707538e0953b774273753fe31cc0a4e0`) | none — construction only |
| v0 execution-audit correction | 2026-08-28 | four corrections from the independent execution audit: (1) F10 causal order rewritten — `Delta_eq` frozen before precision preflight, paired-disagreement firewall added; (2) F6↔F10 `B*`-size cycle removed (P-11 resolvable from F6-available evidence only); (3) secondary-block governance map added (§8), F8 freeze object made explicit about the pre-outcome robustness/transfer law, P-26 evidence dependencies named; (4) F3 adequacy-threshold derivation rule frozen pre-comparison, STOP-16 contamination-recovery strengthened | none — execution/governance corrections only; no v11 closed decision reopened; §26 inventory unchanged (32) |

---

# 1. Status taxonomy

## 1.1 Item classes

```text
A = NORMATIVE_CLOSED                — fixed by v11; MUST NOT be re-selected
B = CALIBRATION_OPEN                — resolved by outcome-blind empirical
                                      calibration or scientific/practical
                                      relevance BEFORE F12 (canonical
                                      inventory: v11 §26)
C = IMPLEMENTATION_OPEN             — software / validation / file-format /
                                      executable-QC details that do not
                                      redefine the scientific estimand
D = CONDITIONAL_OR_NOT_YET_APPLICABLE — active only if its v11 condition holds
E = FORBIDDEN_OR_REJECTED           — v11 §25 explicit rejected rules
```

## 1.2 Gate status vocabulary

```text
COMPLETE | READY | OPEN | CONDITIONAL | STOP | NOT_APPLICABLE
```

A gate is COMPLETE only when its freeze object is actually frozen with
artifacts, hashes, and QC — never merely because the normative framework
exists.

## 1.3 Pin status markers

```text
UNRESOLVED
MEASUREMENT_REQUIRED
OWNER_DECISION_REQUIRED
CALIBRATION_PROTOCOL_PIN_REQUIRED
CONDITIONAL
```

No numeric value is guessed anywhere in this protocol. Absence of a value is
recorded with one of these markers.

## 1.4 No silent promotion

A B/C/D item MUST NOT be silently converted into A. Closing any open pin
requires the gate procedure of §3, the permitted evidence of §5, and a logged
pin record (source, rationale, version/hash — v11 §28 item 7).

---

# 2. NORMATIVE_CLOSED register (class A)

Fixed by v11. Re-selection at any gate is a violation. (v11 § references.)

| id | closed item | v11 |
|---|---|---|
| A-01 | New project is separate from the legacy frozen benchmark; legacy is read-only provenance | §0.2, §1 |
| A-02 | v11 file is the sole normative methodology source; `v11_wins = true` | §0, §28 |
| A-03 | Primary estimand architecture: `Q_CD(k,s)`, `B*_{k,s}`, `H*_s`, `A_m(k,s)`, macro `A_m^APP`, finite estimator `Â_m` | §2 |
| A-04 | `weight_semantics = "design_weight"`; `latent_probability_claim = false` | §1, §23.3 |
| A-05 | Claim boundary: allowed = frozen calibration-constrained application design; forbidden = true latent SSA prototype distribution | §1 |
| A-06 | `K = {3,4,5,6,8}`, `v_k = 1/5` | §3 |
| A-07 | Both sexes in scope; macro pooling `v_M = v_F = 1/2` when sex pooling is frozen | §2, §3 |
| A-08 | k=5 `winner_privilege = false` (empirical mirror / descriptive anchor only) | §3 |
| A-09 | `k_hat = k±1` is secondary partial-credit sensitivity only; primary exact-k unchanged | §3 |
| A-10 | Candidate selector range `k_candidate = 2..10` | §3 |
| A-11 | Primary morphology family WC-ALC | §4 |
| A-12 | W-L / W-I / W-R are observed-window descriptors: `role = descriptor`, `truth_class = false` | §4 |
| A-13 | Truth identity = frozen distinct generator/prototype parameter instance; old `(shape, location)` ontology `automatic_carryover = false` | §4 |
| A-14 | Primary morphology exclusions (level_shift, cylinder, impulse, abrupt) → S-NEG role | §4 |
| A-15 | Revival/multi-wave only via R-REV behind an outcome-blind empirical eligibility gate | §4 |
| A-16 | DTW / elastic alignment `closed = true` | §4, §25.15 |
| A-17 | Primary generator candidate set = {WC-ADL, TAD/PSAT} only; no third family without reopening trigger | §5, §25.14 |
| A-18 | Shape-constrained low-df spline: `role = adequacy_benchmark`, `automatic_primary_fallback = false` | §5, §25.13 |
| A-19 | Outcome-blind adequacy order frozen: coverage → cross-fit → residual structure → censored identifiability → stability → parsimony | §5 |
| A-20 | Both primary generators fail → `STOP`, `action = redesign` | §5, §22 |
| A-21 | No clustering algorithm/CVI output may participate in generator selection | §5 |
| A-22 | After family+fitting freeze: final-refit on all eligible calibration trajectories allowed with logged provenance; family selection not reopenable | §5 |
| A-23 | `rho_max = max_{i<j} corr(P_i,P_j)`, signed Pearson; `max_abs_rho` forbidden as primary | §6, §25.5 |
| A-24 | Mandatory geometry field set (rho_max_pair, rho_mean, rho_min, theta_min, d_eff, Gram spectrum, hardpair_code, envelope_status, coverage_gap_reason, unexpected_nearest_pair) | §6 |
| A-25 | rho is descriptor/reporting/MC-efficiency stratum, never latent probability factor | §6 |
| A-26 | Historical low-rho/dead-zone: `historical_context_only = true`, `design_trigger = false` | §6, §25.6 |
| A-27 | Natural easy domain = ceiling/equivalence finding; no artificial difficulty; infeasible support → `coverage_gap`; artificial filler morphology forbidden | §6, §25.7 |
| A-28 | `class_size_policy = "equal"` in A-APP primary clean core | §7.1, §17 |
| A-29 | `inherit_old_n_per = false`; `n_per_cluster` = independently frozen new-project parameter (F5); `C_NPER_STATUS = forbidden` | §7.1, §17, §25.24–25 |
| A-30 | Primary winner layer `A-APP = B* × H*` | §7.2 |
| A-31 | A-APP exclusion list: morphology-specific sigma, jitter, imbalance, outliers, morphology-noise coupling, signal-scale robustness perturbation | §7.2, §25.11 |
| A-32 | `phi_primary` = measured/calibrated representation; automatic `phi_emp -> 0.97` forbidden; any discretization/snap must be empirically justified, outcome-blind, frozen at F8 | §7.2, §25.10 |
| A-33 | Canonical response layer: `sigma = 0.1...1.0`, `noise = {white, AR(.97)}`, `winner_eligible = false`, `application_probability = none` | §7.3, §25.9 |
| A-34 | Hard-pair governance: natural pairs recorded only, no forced counterbalancing in A-APP; A-MECH matched panel; codes HP-II/HP-IB-L/HP-IB-R/HP-LL/HP-RR; W-L×W-R = `BB-OPP`, `role = diagnostic_only` | §8, §25.12 |
| A-35 | Seeds: `role = "Monte_Carlo_realization"`, `scientific_observation = false`; CRN `required = true`; seed-level hypothesis tests forbidden; primary conditional MC variance and paired-difference variance formulas | §9, §25.16 |
| A-36 | Primary MC SE is conditional on frozen design; not target-population sampling uncertainty | §9, §24.27 |
| A-37 | BANK-SENS-S: required, winner-ineligible, not a primary CI; preferred first-line candidate `scenario_id_cluster_bootstrap`; exact procedure `freeze_stage = F11`; delta-method optional cross-check, not automatically mandatory | §10 |
| A-38 | BANK-SENS-L: required, winner-ineligible; preferred candidate `incidence_delete_source_jackknife` only if the six-condition applicability QC passes; `zero_new_runs != statistical_applicability`; no silent skip — otherwise `sensitivity_class_status = "unresolved"`, `methodology_freeze_status = "STOP"`; mandatory limitation language | §11, §25.17–20 |
| A-39 | Causal direction `Delta_eq -> precision target -> scenario/seed allocation -> compute budget`; reverse (`compute_budget -> enlarge Delta_eq`) forbidden; 100 seeds neither automatically adequate nor inadequate; mandatory precision preflight; insufficiency ladder ends in `precision_insufficient`; primary A-APP never silently degraded | §12, §25.21 |
| A-40 | Scientific winner source = A-APP only; allowed terminal outcomes = {unique winner, exact/co-winner, practical-equivalence top set, precision-insufficient, coverage-limited}; forced winner forbidden | §13, §25.22 |
| A-41 | Historical Ward+CH: `role = "historical_incumbent_comparator"`, `scientific_tie_break_privilege = false`, `operational_tie_break_privilege = false`; runner-up reporting fields mandatory; equivalence set cannot be renamed "unique winner" by operational policy | §13, §25.2–4 |
| A-42 | Operational deployment tie-break: activated only if a single pipeline is operationally required; `scientific_winner_rule != operational_deployment_policy`; `legacy_neutral = true`; outcome-blind policy definition; external/exogenous criteria classes; simplicity alone is not a tie-break; incumbent continuity labeled `policy_type = "non_scientific_stakeholder_continuity"` and cannot change scientific results | §14 |
| A-43 | Transfer: default `TRANSFER-QUAL` gate with states {qualified, qualified_with_caveats, failed}; separate transfer estimand only if `distinct_transfer_source_or_law = true`; duplicating `B*×H*` as A_TRANSFER forbidden; transfer cannot change the scientific winner | §15, §25.23 |
| A-44 | E-BRIDGE umbrella with subpanels E-ACTUAL and E-MATCHED; not independent external validation; not winner-defining; every new DGP block must pass the unanswered-scientific-question test or `new_block = rejected` | §16, §24.50 |
| A-45 | Secondary registry: `frozen_v53_friedman_formulations = ["sil_euc","DB","CH","Dunn_d1_D1"]`; `sil_cos` exploratory; Friedman/Nemenyi `primary_winner_statistic = false`; amendment only under all six conditions; budget alone `valid_amendment_reason = false` | §18, §25.26–27 |
| A-46 | Venue: `venue_is_methodology_gate = false`, `venue_status = "administrative_metadata"`; venue cannot change DGP/estimand/k support/winner rule/noise law/morphology-generator decisions | §19, §25.28 |
| A-47 | Panel provenance residuals: bit-identical/identity-defective artifacts get `independent_evidence_score = N-A` until attribution resolved; unresolved non-material panel identity is not a freeze blocker; LLM consensus is not empirical evidence and not a reopening trigger | §20, §25.29 |
| A-48 | Block architecture and winner-eligibility table (A-APP the only winner-eligible block) | §21 |
| A-49 | F0–F12 freeze sequence with per-gate failure behaviors; `F11 = implementation pin`, `F12 = ratification only`; no method first chosen at F12; staged execution allowed, staged outcome reading not; accidental early exposure = logged provenance violation that cannot alter the confirmatory design and cannot be presented as pristine | §22 |
| A-50 | Outcome firewall: no algorithm × CVI performance outcome may be generated or read before F12 sign-off; canonical manifest field names of §23; 50-item mandatory QC of §24; reopening policy of §27; Claude Code execution contract of §28 | §22–§24, §27–§29 |

Count: **50 NORMATIVE_CLOSED items.**

---

# 3. F0–F12 gate protocol

Evidence codes `EV-xx` are defined in §5 (evidence firewall matrix). Artifact
IDs `ART-*` denote required future artifacts; their exact filenames/formats are
class-C implementation details to be fixed at the owning gate — no artifact is
created by this document. QC references are to v11 §24 item numbers.

## F0 — Project identity

| field | content |
|---|---|
| gate | F0 — project identity |
| freeze_object | project identity; primary question; old/new boundary; estimand; k/sex scope; historical comparator role; precedence/provenance ledger |
| normative_closed_inputs | A-01..A-10, A-41, A-46, A-47, A-50; reconciliation and historical source hashes of v11 §0.1–0.2 |
| open_pins_to_resolve | none scientific; C: ledger file format/naming (ART-F0) |
| permitted_evidence | v11 text; EV-11/EV-12 as provenance-ledger entries (identity+hash only); EV-18 as ledger metadata; EV-19 as administrative metadata; bootstrap isolation audit as operational provenance |
| forbidden_evidence | EV-13..EV-16 as motivation for any new-project pin; EV-17 absolutely |
| procedure | (1) instantiate the F0 identity/provenance record; (2) restate primary question, estimand architecture, claim boundary, `K`, sex scope; (3) record the old/new boundary and legacy read-only status; (4) build the provenance ledger with the v11 §0.1–0.2 hashes; (5) record literals: `weight_semantics = "design_weight"`, `latent_probability_claim = false`, `historical_Ward_CH_role = "historical_incumbent_comparator"`, `historical_tie_break_privilege = false`; (6) verify no legacy performance value is used to motivate any pin |
| required_artifacts | ART-F0: F0 identity/provenance record (under `p_konum_plus/provenance/`) |
| required_manifest_fields | `project_id`, `design_version`, `methodology_contract_status`, parent hashes, `panel_source_ledger_hash`, `question_id`, `claim_scope`, `historical_tie_break_privilege`, `venue_status`, `venue_is_methodology_gate` |
| QC | §24: 1, 2, 3, 4, 5, 33, 34, 41, 49 |
| STOP_condition | material design-relevant provenance contradiction → STOP/reconcile (STOP-02) |
| completion_criterion | F0 record written with all literals and ledger hashes; no contradiction open |
| owner_or_authority | PI (authority); Claude Code (preparation) |
| status | READY |

## F1 — Calibration inputs

| field | content |
|---|---|
| gate | F1 — inputs |
| freeze_object | raw male/female input filenames; hashes; eligibility rules; time axis; preprocessing; row z-normalization; inclusion/exclusion provenance |
| normative_closed_inputs | A-01, A-04, A-11..A-13 (what the inputs are for); F0 record |
| open_pins_to_resolve | raw source inventory: **OPEN — requires F1 source inventory** (no filename is guessed here); eligibility rule text; time-axis definition; preprocessing spec; z-normalization convention |
| permitted_evidence | EV-01 (inventory-level and structural inspection, outcome-blind); EV-08 for eligibility rationale |
| forbidden_evidence | EV-13..EV-17; selecting inputs to favor any anticipated method outcome |
| procedure | (1) enumerate candidate raw SSA trajectory files with hashes; (2) owner confirms eligibility criteria; (3) freeze time axis and preprocessing pipeline spec; (4) freeze row z-normalization convention; (5) log every inclusion/exclusion with reason; (6) hash-freeze the frozen input set |
| required_artifacts | ART-F1: input freeze record + input hash table |
| required_manifest_fields | source/input hashes (§23.1); `calibration_sex`; `stage` |
| QC | §24: 1, 2 |
| STOP_condition | unresolved inputs → calibration cannot freeze (STOP-03) |
| completion_criterion | every calibration input named, hashed, eligibility-logged; owner sign |
| owner_or_authority | PI (eligibility); Claude Code (inventory/hashing) |
| status | OPEN |

## F2 — Generator specification

| field | content |
|---|---|
| gate | F2 — generator specification |
| freeze_object | exact WC-ADL formula; exact TAD/PSAT formula; parameter bounds; initialization; fit-failure handling |
| normative_closed_inputs | A-17 (candidate set closed — no third family), A-18 (spline = adequacy benchmark only, never automatic fallback), A-21 |
| open_pins_to_resolve | P-01, P-02 — all four spec elements per family: **OWNER_DECISION_REQUIRED** / **CALIBRATION_PROTOCOL_PIN_REQUIRED**. v11 does not fully specify the equations/bounds/init/failure rules; they MUST NOT be chosen unilaterally by the executor |
| permitted_evidence | EV-01 (outcome-blind structural properties of frozen F1 inputs); EV-02 (outcome-blind fit feasibility checks); EV-08 (methodological literature and scientific argument, outcome-blind, documented) |
| forbidden_evidence | EV-13..EV-17; any adequacy-comparison result used before spec freeze; any algorithm/CVI output |
| procedure | (1) owner authors/ratifies exact WC-ADL and TAD/PSAT equations; (2) owner sets parameter bounds and initialization scheme; (3) owner sets deterministic fit-failure handling; (4) each element logged as a pin record with source and rationale; (5) spline registered as adequacy benchmark only |
| required_artifacts | ART-F2: generator specification record (both families, versioned, hashed) |
| required_manifest_fields | generator family/version/hash (§23.4) |
| QC | §24: 1, 7-preconditions n/a here; completeness of both family specs |
| STOP_condition | incomplete specification → STOP (STOP-04) |
| completion_criterion | both families fully specified (formula, bounds, init, failure), pinned, hashed |
| owner_or_authority | PI (all four spec elements); Claude Code (drafting/validation only) |
| status | OPEN |

## F3 — Generator adequacy / selection

| field | content |
|---|---|
| gate | F3 — adequacy and selection |
| freeze_object | cross-fit adequacy thresholds; generator tie-break; selected generator family |
| normative_closed_inputs | A-19 (adequacy order frozen: 1 morphology coverage; 2 cross-fitted reconstruction/predictive fit; 3 systematic residual morphology/structure; 4 censored-case identifiability; 5 parameter stability; 6 parsimony), A-20, A-21, A-22 |
| open_pins_to_resolve | P-03 adequacy thresholds (**MEASUREMENT_REQUIRED** — no value invented here; the threshold **derivation rule** must itself be frozen before any candidate-specific adequacy comparison used for generator selection); P-04 exact deterministic tie-break (**OWNER_DECISION_REQUIRED**, pre-frozen, outcome-blind); P-05 cross-fit scheme (**OWNER_DECISION_REQUIRED**) |
| permitted_evidence | EV-02, EV-03, EV-04, EV-05 (all outcome-blind); EV-08 for threshold/tie-break rationale |
| forbidden_evidence | EV-13..EV-17; **any clustering algorithm/CVI output** (A-21); any peek at downstream performance |
| procedure | (1) freeze cross-fit scheme; (2) freeze the adequacy-threshold **derivation rule** (owner-signed) BEFORE any candidate-specific adequacy comparison used for generator selection — the rule may not be selected or adjusted after inspecting which candidate it favors; (3) run outcome-blind adequacy evaluation in the frozen order; (4) compute thresholds from calibration distributions strictly under the pre-frozen derivation rule; PI ratifies before selection; (5) apply pre-frozen deterministic tie-break if needed; (6) log selection with full evidence trail; (7) if both candidates fail → STOP, `action = redesign` |
| required_artifacts | ART-F3: adequacy report + selection record + tie-break pin |
| required_manifest_fields | generator family/version/hash (selected) |
| QC | §24: 1; selection evidence contains zero algorithm/CVI content |
| STOP_condition | both primary candidates fail → STOP / redesign (STOP-05) |
| completion_criterion | one family selected under frozen thresholds and tie-break; family selection thereafter not reopenable |
| owner_or_authority | PI (thresholds ratification, tie-break); Claude Code (measurement execution) |
| status | OPEN |

Threshold-derivation governance (binding):

```text
adequacy_threshold_derivation_rule
must_be_frozen_before_candidate_specific_adequacy_comparison
is_used_for_generator_selection
```

Measurement-derived thresholds remain allowed; the derivation rule itself must
not be selected after inspecting which candidate it favors. No algorithm/CVI
outcome may be used at any point in F3.

## F4 — Final refit / parameter bank

| field | content |
|---|---|
| gate | F4 — final refit and parameter bank |
| freeze_object | final-refit rule; parameter vectors; source IDs; observed-window descriptors; label_fuzz; sex-specific calibration provenance |
| normative_closed_inputs | A-12 (`observed_window_regime = descriptor`, `truth_class = false`), A-13 (truth identity = frozen distinct generator/prototype parameter instance), A-22 |
| open_pins_to_resolve | P-06 descriptor thresholds (**MEASUREMENT_REQUIRED**); P-07 label_fuzz rule (**OWNER_DECISION_REQUIRED**); P-08 full-data final-refit rule (**OWNER_DECISION_REQUIRED** within A-22 constraints) |
| permitted_evidence | EV-01, EV-02, EV-04, EV-05 |
| forbidden_evidence | EV-13..EV-17 |
| procedure | (1) freeze final-refit rule; (2) refit selected family on all eligible calibration trajectories with logged provenance; (3) build parameter vectors with `scenario_source_ids`-compatible source IDs; (4) compute observed-window descriptors (W-L/W-I/W-R, optional early/mid/late) as descriptors only; (5) freeze label_fuzz rule; (6) record sex-specific calibration provenance; (7) hash the parameter bank |
| required_artifacts | ART-F4: parameter bank + provenance record (`parameter_bank_id`, `parameter_bank_hash`) |
| required_manifest_fields | `parameter_bank_id`, `parameter_bank_hash`, `prototype_instance_id`, `prototype_instance_hash`, shape family/regime/subtype, observed descriptors, `label_fuzz` |
| QC | §24: 1, 10 (no old `(shape,location)` truth carry-over) |
| STOP_condition | unstable/unsupported parameter bank → no B* (STOP-06) |
| completion_criterion | hashed parameter bank with complete source IDs and descriptors; stability evidence on file |
| owner_or_authority | PI (rules); Claude Code (refit execution, bank build) |
| status | OPEN |

## F5 — Q_CD and class size

| field | content |
|---|---|
| gate | F5 — Q_CD and class size |
| freeze_object | Q_CD whole-vector sampling/composition; distinctness rule; acceptance/rejection rule; design weights; coverage guard; new-project numeric `n_per_cluster` |
| normative_closed_inputs | fixed literals: `class_size_policy = "equal"`, `inherit_old_n_per = false`, `C_NPER_STATUS = forbidden` (A-28, A-29); `Q_CD` is a construction/provenance law, not a latent probability (A-03, A-04) |
| open_pins_to_resolve | P-09 Q_CD composition (**OWNER_DECISION_REQUIRED** + MEASUREMENT); P-10 distinctness/acceptance thresholds (**MEASUREMENT_REQUIRED**); P-12 design-weight rule (**OWNER_DECISION_REQUIRED**); P-13 coverage guard (**MEASUREMENT_REQUIRED**); P-14 numeric `n_per_cluster` (**OWNER_DECISION_REQUIRED**, outcome-blind justification). Historical `n_per=10` (12/12 C-block rows) is provenance fact only and MUST NOT be a calibration rationale (v11 §17) |
| permitted_evidence | EV-01 (calibrated parameter distributions via F4), EV-06 (feasibility), EV-08, EV-09 (outcome-blind precision considerations feeding F10) |
| forbidden_evidence | EV-13..EV-17; historical `n_per=10` as rationale; any weight semantics implying latent probability |
| procedure | (1) freeze Q_CD whole-vector composition law per (k,s); (2) freeze distinctness and acceptance/rejection thresholds from calibrated distributions; (3) freeze design-weight rule with `weight_semantics = "design_weight"`; (4) freeze coverage guard; (5) owner pins numeric `n_per_cluster` with an outcome-blind written justification; (6) hash `q_cd_rule_id`/`q_cd_rule_hash` |
| required_artifacts | ART-F5: Q_CD rule record + n_per_cluster pin record |
| required_manifest_fields | `q_cd_rule_id`, `q_cd_rule_hash`, `class_size_policy`, `n_per_cluster`, `class_sizes`, `composition_id`, `weight_source`, `weight_semantics`, `latent_probability_claim` |
| QC | §24: 5, 6, 7, 8, 9, 15, 16, 17 |
| STOP_condition | ambiguous/collapsed Q_CD or design support → revise or STOP (STOP-07) |
| completion_criterion | Q_CD law + thresholds + weights + coverage guard + numeric `n_per_cluster` frozen and hashed |
| owner_or_authority | PI (`n_per_cluster`, composition, weights); Claude Code (measurement, construction) |
| status | OPEN |

## F6 — B* scenario bank

| field | content |
|---|---|
| gate | F6 — B* freeze |
| freeze_object | frozen finite scenario bank per (k,s): bank size; bank IDs; scenario IDs; scenario source IDs; design weights; source-incidence metadata; acceptance/rejection logging; coverage; hashes |
| normative_closed_inputs | A-03 (B* definition), A-30; Q_CD law from F5 |
| open_pins_to_resolve | P-11 B* size: **UNRESOLVED / OWNER_DECISION_REQUIRED / MEASUREMENT_REQUIRED** — justified only by outcome-blind bank-construction / design-coverage adequacy evidence available by F6; never convenience-only; MUST NOT depend on the later F10 precision calculation; no exact resolution rule is invented here beyond v11 |
| permitted_evidence | F4/F5 artifacts; EV-06; EV-08 (outcome-blind bank-construction / design-coverage adequacy rationale available by F6) |
| forbidden_evidence | EV-13..EV-17; tuning bank contents toward any anticipated method behavior |
| procedure | (1) generate bank under frozen Q_CD; (2) log every acceptance/rejection with reason; (3) attach `scenario_source_ids` and source-incidence metadata (BANK-SENS-L precondition); (4) verify design weights sum correctly; (5) verify coverage vs guard; (6) hash-freeze bank (`bank_id`, `bank_hash`) |
| required_artifacts | ART-F6: frozen B* + acceptance/rejection log + incidence metadata |
| required_manifest_fields | `bank_id`, `bank_hash`, `scenario_id`, `scenario_source_ids`, `weight_source`, `weight_hash`, `k_true`, `calibration_sex` |
| QC | §24: 14, 15 |
| STOP_condition | incomplete B* → no run (STOP-08) |
| completion_criterion | hashed bank with complete IDs, weights, incidence metadata, and logged construction |
| owner_or_authority | Claude Code (construction); PI (ratify size/coverage) |
| status | OPEN |

## F7 — Geometry

| field | content |
|---|---|
| gate | F7 — geometry freeze |
| freeze_object | signed geometry records; geometry strata; natural hard-pair records; matched-panel (A-MECH) feasibility; `epsilon`; `delta` |
| normative_closed_inputs | A-23 (`rho_max = max_{i<j} corr(P_i,P_j)`, signed Pearson; `max_abs_rho` forbidden); A-24 mandatory fields: `rho_max_pair`, `rho_mean`, `rho_min`, `theta_min`, `d_eff`, Gram spectrum, `hardpair_code`, `envelope_status`, `coverage_gap_reason`, `unexpected_nearest_pair`; A-26 (`historical_context_only = true`, `design_trigger = false`); A-27 (no artificial filler; infeasible support → `coverage_gap`); A-34 (hard-pair codes; BB-OPP diagnostic only) |
| open_pins_to_resolve | P-15 geometry strata (**MEASUREMENT_REQUIRED**); P-16 `epsilon`/`delta` (**MEASUREMENT_REQUIRED** — frozen only after feasibility is observed and before any outcome) |
| permitted_evidence | EV-06 (geometry feasibility on frozen B*/prototypes); EV-08 |
| forbidden_evidence | EV-13..EV-17; historical rho bands as design triggers or application-probability support |
| procedure | (1) compute all mandatory signed geometry fields per scenario; (2) record natural hard pairs (no counterbalancing); (3) audit matched-panel QC feasibility: `|rho_intended-rho_target| <= epsilon`, `argmax(pairwise_rho) == intended_pair`, `max(non_target_rho) <= rho_target-delta`; (4) freeze strata and `epsilon`/`delta` from observed feasibility; (5) report infeasible support as `coverage_gap` with `coverage_gap_reason` — never manufacture difficulty |
| required_artifacts | ART-F7: geometry record + strata/epsilon/delta pin record |
| required_manifest_fields | signed rho fields, `theta_min`, `d_eff`, Gram spectrum, `hardpair_code`, `epsilon`, `delta`, `unexpected_nearest_pair`, `envelope_status`, `coverage_gap_reason` |
| QC | §24: 12, 13 |
| STOP_condition | secondary matched support infeasible → `coverage_gap` (conditional_panel_NO_GO — explicitly NOT a global STOP) |
| completion_criterion | geometry fields complete for all scenarios; strata + epsilon/delta frozen pre-outcome |
| owner_or_authority | Claude Code (measurement); PI (ratify strata/epsilon/delta) |
| status | OPEN |

## F8 — H* / noise

| field | content |
|---|---|
| gate | F8 — H* freeze |
| freeze_object | empirical residual sigma strata; empirical temporal-dependence representation; common clean within-cell scale convention; white-noise ceiling diagnostic; canonical response definitions; **the pre-outcome robustness/transfer law** (v11 §22 F8 freeze object), kept separate from H* |
| normative_closed_inputs | `A_APP = B_star × H_star` (A-30); `automatic_phi_to_0.97 = forbidden` (A-32); A-APP exclusion list (A-31); canonical layer literal: `sigma = 0.1...1.0`, `noise = {white, AR(.97)}`, `winner_eligible = false`, `application_probability = none` (A-33) |
| open_pins_to_resolve | P-17 H* sigma strata (**MEASUREMENT_REQUIRED**); P-18 empirical temporal-dependence representation (**MEASUREMENT_REQUIRED**; any discretization/snap must be empirically justified, outcome-blind, frozen here); P-19 white-noise ceiling diagnostic (**MEASUREMENT_REQUIRED** + spec) |
| permitted_evidence | EV-07 (residual noise measurement from calibrated fits), EV-01, EV-08 |
| forbidden_evidence | EV-13..EV-17; automatic phi snap; any morphology-noise coupling in A-APP |
| procedure | (1) measure clean residual scale distribution; freeze sigma strata; (2) measure temporal dependence; freeze empirical representation (`phi` + `phi_source`); (3) freeze common within-cell clean scale convention; (4) freeze white-noise ceiling diagnostic; (5) define canonical response layer per A-33 (winner-ineligible); (6) freeze the pre-outcome robustness/transfer perturbation law (evidence basis for R-REALISTIC and TRANSFER-QUAL), kept separate from H* |
| required_artifacts | ART-F8: H* freeze record (hashed) |
| required_manifest_fields | `sigma`, `sigma_source`, `noise_type`, `phi`, `phi_source` |
| QC | §24: 11 |
| STOP_condition | unsupported H* → no A-APP freeze (STOP-09) |
| completion_criterion | H* strata + dependence representation + conventions frozen with measurement provenance |
| owner_or_authority | Claude Code (measurement); PI (ratify representation) |
| status | OPEN |

## F9 — Method registry

| field | content |
|---|---|
| gate | F9 — method/environment registry |
| freeze_object | algorithm registry; CVI registry; `k_candidate = 2..10`; tie policy; failure/nonfinite policy; software/environment hashes; frozen four secondary Friedman formulations |
| normative_closed_inputs | A-10; A-45: `frozen_v53_friedman_formulations = ["sil_euc","DB","CH","Dunn_d1_D1"]`, `sil_cos` exploratory, Friedman/Nemenyi not primary; amendment only under the six conditions (pre-outcome, signed deviation, genuinely new material reason, exact formulation change specified, multiplicity consequences frozen, no motivation from observed ranking); budget alone is not an amendment reason |
| open_pins_to_resolve | registry composition (algorithm list, CVI list) — **OWNER_DECISION_REQUIRED**, outcome-blind; tie and failure/nonfinite policies — **OWNER_DECISION_REQUIRED**; P-29 software/environment hashes (**IMPLEMENTATION_OPEN**, pinned here) |
| permitted_evidence | EV-08 (scope rationale); software/environment facts |
| forbidden_evidence | EV-13..EV-17 — in particular, legacy winner/performance content MUST NOT influence registry composition; observed pipeline rankings (none may exist) |
| procedure | (1) owner fixes algorithm and CVI registries; (2) fix `k_candidate = 2..10`; (3) fix deterministic tie policy and failure/nonfinite policy; (4) hash software/environment; (5) record frozen four secondary formulations |
| required_artifacts | ART-F9: registry + environment freeze record |
| required_manifest_fields | code/registry/environment hashes (§23.1), `frozen_v53_friedman_formulations` |
| QC | §24: 42, 43 |
| STOP_condition | registry/failure-rule ambiguity → no run (STOP-10) |
| completion_criterion | registries, policies, and environment hashed and frozen |
| owner_or_authority | PI (registry composition); Claude Code (environment freeze) |
| status | OPEN |

## F10 — Delta_eq / precision / allocation

| field | content |
|---|---|
| gate | F10 — Delta_eq, precision target, allocation |
| freeze_object | `Delta_eq`; paired MC precision target; CRN seed namespace; scenario/seed allocation; compute budget consequence |
| normative_closed_inputs | A-39 causal direction: `Delta_eq -> paired_MC_precision_target -> scenario_seed_allocation -> compute_budget`; forbidden reverse: `compute_budget -> enlarge_Delta_eq`; 100 seeds neither automatically adequate nor inadequate (**no 100-seed assumption**); A-35 (CRN required; seeds are MC realizations); at F10 `B*`, `Q_CD`, geometry, and `H*` are already frozen — F10 resolves Monte Carlo scenario/seed allocation over the frozen design and cannot change them or their frozen design semantics |
| open_pins_to_resolve | P-20 `Delta_eq` numeric scientific justification (**OWNER_DECISION_REQUIRED** — scientific/practical relevance, outcome-before, never budget-adaptive); P-21 paired precision target (**MEASUREMENT_REQUIRED**, derived from the frozen Delta_eq); P-22 scenario/seed allocation (**MEASUREMENT_REQUIRED** via post-`Delta_eq` outcome-blind preflight); P-23 CRN seed namespace (**IMPLEMENTATION_OPEN**) |
| permitted_evidence | EV-08 (Delta_eq relevance argument); EV-09 (analytic worst-case bounds); EV-10 (outcome-blind simulation if necessary); frozen design weights; paired-disagreement inputs only as outcome-blind bounds, explicitly declared assumptions, or dedicated outcome-blind precision constructs |
| forbidden_evidence | EV-13..EV-17; budget pressure as a reason to enlarge Delta_eq; convenience defaults |
| procedure | exact order: (1) scientific/practical relevance argument (EV-08); (2) PI freezes `Delta_eq`; (3) derive the paired MC precision target from the frozen `Delta_eq`; (4) analytic worst-case bounds; (5) use frozen design weights; (6) characterize paired-disagreement structure WITHOUT algorithm × CVI outcome access — only outcome-blind bounds, explicitly declared assumptions, or dedicated outcome-blind precision constructs; (7) outcome-blind precision simulation if necessary; (8) scenario/seed allocation and CRN namespace; (9) compute-budget consequence; (10) if budget insufficient: first narrow secondary scope, then optimize primary allocation, and if still insufficient declare `precision_insufficient` — budget may never enlarge `Delta_eq`, and the primary A-APP is never silently degraded |
| required_artifacts | ART-F10: Delta_eq pin record + preflight report + allocation record |
| required_manifest_fields | `seed_namespace`, `CRN_id` |
| QC | §24: 28, 29, 30, 31 |
| STOP_condition | inadequate precision after permitted adjustments → `precision_insufficient` (STOP-11; defined terminal outcome, not silent degradation) |
| completion_criterion | Delta_eq justified and pinned pre-outcome; target + allocation + CRN namespace frozen |
| owner_or_authority | PI (Delta_eq); Claude Code (preflight computation, allocation derivation) |
| status | OPEN |

Paired-disagreement firewall (binding):

```text
paired_disagreement_information_pre_F12
must_not_be_estimated_from_algorithm_x_CVI_benchmark_outcomes
```

Any disagreement input used for precision planning must be an outcome-blind
bound, an explicitly declared assumption, or a dedicated outcome-blind
precision construct. `B*` is already frozen when F10 runs: allocation cannot
resize, reweight, or otherwise alter `B*`, `Q_CD`, geometry, or `H*`.

## F11 — Analysis / sensitivity implementation freeze

| field | content |
|---|---|
| gate | F11 — analysis and sensitivity implementation pin |
| freeze_object | exact BANK-SENS-S implementation; BANK-SENS-L applicability audit + exact implementation or fallback; executable manifest/QC; primary estimator; MC variance; paired-difference variance; practical-equivalence implementation (using the already-justified Delta_eq); reporting rules; operational deployment policy only if actually required |
| normative_closed_inputs | A-37, A-38, A-35, A-36, A-40..A-43; `F11 = methodological/analysis implementation pin`; no method may first be chosen at F12 |
| open_pins_to_resolve | P-24 BANK-SENS-S exact implementation — preferred first-line candidate `scenario_id_cluster_bootstrap`; requirements: CRN/pairing preserved, relevant strata preserved, scenario unit treated as the resampling cluster; delta-method = optional cross-check only, not automatically mandatory (**UNRESOLVED until F11**). P-25 BANK-SENS-L — preferred first-line candidate `incidence_delete_source_jackknife` ONLY if all six applicability conditions pass (below); else pre-frozen eligible fallback (**CONDITIONAL**). P-26 transfer qualification thresholds (**MEASUREMENT_REQUIRED**/**OWNER_DECISION_REQUIRED**; eligible evidence sources = R-REALISTIC, E-BRIDGE, CAL-SENS, genuine held-out/external evidence if available — none winner-defining). P-28 operational deployment policy (**CONDITIONAL** — only if a single pipeline is truly required; external/exogenous measurable criteria; pinned here, ratified F12). P-30 executable manifest QC; P-31 report language (**IMPLEMENTATION_OPEN**) |
| permitted_evidence | calibration-structure checks on frozen F4–F10 artifacts (EV-03..EV-07 class evidence); EV-08; EV-09; EV-10 |
| forbidden_evidence | EV-13..EV-17; any new algorithm × CVI outcome; choosing sensitivity methods by anticipated results |
| procedure | (1) pin exact BANK-SENS-S procedure. (2) Run the BANK-SENS-L applicability audit — the incidence/delete-source method applies ONLY if ALL six hold: [1] `scenario_source_ids` complete and deterministic; [2] every delete-source operation leaves interpretable nonempty support in every required `(sex,k)` stratum; [3] renormalized design weights remain finite and well-defined; [4] deletion does not mechanically destroy estimand support so that interpretation becomes impossible; [5] source incidence in required strata is not structurally universal; [6] post-deletion scenario dependency/duplication structure is documented. Pass → `bank_sens_l_incidence_status = "applicable"`; fail → `"not_applicable"` with explicit reason and decision path to a pre-frozen eligible fallback (calibration-stage source-subset/bank-rebuild jackknife; grouped source deletion; alternative frozen-bank/source-influence design). `zero_new_runs != statistical_applicability`. (3) If no interpretable BANK-SENS-L implementation exists: `sensitivity_class_status = "unresolved"`, `methodology_freeze_status = "STOP"` — no mandatory sensitivity class may be silently skipped. (4) Freeze estimator, MC variance, paired-difference variance, practical-equivalence implementation with the F10 Delta_eq. (5) Freeze reporting rules incl. runner-up fields and the mandatory limitation language: "BANK-SENS-L is a winner-ineligible source-influence sensitivity analysis; it is not a primary confidence interval and does not by itself represent target-population sampling uncertainty." (6) Pin operational deployment policy only if genuinely required. (7) Freeze executable manifest/QC |
| required_artifacts | ART-F11: analysis/sensitivity implementation contract + applicability audit record |
| required_manifest_fields | `bank_sens_s_method`, `bank_sens_s_status`, `bank_sens_l_method`, `bank_sens_l_applicability_status`, `bank_sens_l_not_applicable_reason`, `bank_sens_l_source_count`, `resampling_rule_id`, `calibration_sensitivity_role`, `distinct_transfer_source_or_law`, `operational_tie_break_policy_id`, `operational_tie_break_scientific` |
| QC | §24: 18–27, 32, 35, 36, 37, 38, 44 |
| STOP_condition | unresolved mandatory BANK-SENS-L → methodology freeze STOP (STOP-12); incomplete F11 contract → no outcome reading (STOP-13) |
| completion_criterion | every analysis/sensitivity implementation choice pinned pre-outcome; manifest/QC executable |
| owner_or_authority | PI (method pins, policy); Claude Code (audit execution, contract drafting) |
| status | OPEN (contains CONDITIONAL sub-items P-25 fallback, P-28) |

## F12 — Ratification only

| field | content |
|---|---|
| gate | F12 — ratification |
| freeze_object | final analysis/reporting-contract ratification; full-text consistency review; explicit PI sign-off; external hash sidecar/freeze |
| normative_closed_inputs | `F12 = final ratification/sign-off` — F12 MUST NOT introduce any new scientific or sensitivity method (A-49); lifecycle: `draft -> calibration_pins_complete -> manifest_analysis_contract_complete -> explicit_signoff -> frozen`; unsigned → `draft_only` |
| open_pins_to_resolve | P-32 explicit F12 sign-off (governance act) |
| permitted_evidence | completed F0–F11 artifacts only (consistency review) |
| forbidden_evidence | EV-17 (still absolutely prohibited until sign-off completes); any new method proposal |
| procedure | (1) verify all calibration pins closed (`calibration_pins_complete`); (2) verify manifest/analysis contract complete; (3) full-text consistency review; (4) explicit PI sign-off; (5) external hash sidecar/freeze of the complete contract |
| required_artifacts | ART-F12: ratification record + external hash sidecar (NOT created before F12) |
| required_manifest_fields | `methodology_contract_status` (terminal value), all §23 provenance hashes complete |
| QC | §24: 45, 46, 47, 48 |
| STOP_condition | unsigned → `draft_only` (STOP-14); any early outcome exposure logged as provenance violation (STOP-15) |
| completion_criterion | signed, hash-frozen contract. Absolute firewall: `F12_not_complete -> algorithm_x_CVI_outcome_reading = PROHIBITED` |
| owner_or_authority | PI (sign-off authority) |
| status | OPEN |

---

# 4. Calibration-open pin register

Canonical inventory = v11 §26 (all 32 items; v11: "these are measurement and
implementation pins, not new methodology votes"). Evidence codes per §5.
Classes: B = CALIBRATION_OPEN, C = IMPLEMENTATION_OPEN, D = CONDITIONAL.
Owner tokens: PI = decision authority; CC = Claude Code executor.
No numeric value is populated anywhere in this register.

| pin_id | pin_name | class | freeze_gate | current_status | normative_constraints | permitted_evidence | forbidden_evidence | resolution_method | required_artifact | source_provenance | owner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P-01 | WC-ADL exact formula/bounds/init/failure handling | B | F2 | UNRESOLVED — OWNER_DECISION_REQUIRED, CALIBRATION_PROTOCOL_PIN_REQUIRED | candidate set closed (A-17); no 3rd family; outcome-blind | EV-01,02,08 | EV-13..17 | owner-authored spec + outcome-blind fit-feasibility validation | ART-F2 | v11 §26.1, §5 | PI |
| P-02 | TAD/PSAT exact formula/bounds/init/failure handling | B | F2 | UNRESOLVED — OWNER_DECISION_REQUIRED, CALIBRATION_PROTOCOL_PIN_REQUIRED | as P-01 | EV-01,02,08 | EV-13..17 | as P-01 | ART-F2 | v11 §26.2, §5 | PI |
| P-03 | Adequacy thresholds | B | F3 | UNRESOLVED — MEASUREMENT_REQUIRED | adequacy order frozen (A-19); thresholds set pre-selection, outcome-blind; no invented values; derivation rule frozen before any candidate-specific adequacy comparison and never selected for the candidate it favors | EV-02,03,04,05,08 | EV-13..17; any algorithm/CVI output | freeze derivation rule first, then derive thresholds from calibration distributions under that rule; PI ratifies before selection | ART-F3 | v11 §26.3, §5 | PI + CC |
| P-04 | Generator tie-break exact rule | B | F3 | UNRESOLVED — OWNER_DECISION_REQUIRED | deterministic, outcome-blind, pre-frozen | EV-08 | EV-13..17 | owner pins deterministic rule before adequacy comparison completes | ART-F3 | v11 §26.4, §5 | PI |
| P-05 | Cross-fit scheme | B | F3 | UNRESOLVED — OWNER_DECISION_REQUIRED | cross-fit serves family/adequacy audit only (A-22) | EV-01,08 | EV-13..17 | owner selects scheme from data structure, documented | ART-F3 | v11 §26.5, §5 | PI |
| P-06 | Descriptor thresholds (W-L/W-I/W-R) | B | F4 | UNRESOLVED — MEASUREMENT_REQUIRED | descriptors only; `truth_class = false` (A-12) | EV-01,02 | EV-13..17 | thresholds measured from calibrated fits | ART-F4 | v11 §26.6, §4 | CC + PI |
| P-07 | label_fuzz rule | B | F4 | UNRESOLVED — OWNER_DECISION_REQUIRED | truth identity remains frozen parameter instance (A-13) | EV-01,08 | EV-13..17 | owner pins rule; logged | ART-F4 | v11 §26.7 | PI |
| P-08 | Full-data final-refit rule | B | F4 | UNRESOLVED — OWNER_DECISION_REQUIRED | family not reopenable; provenance logged (A-22) | EV-01,05,08 | EV-13..17 | owner pins rule within A-22 constraints | ART-F4 | v11 §26.8, §5 | PI |
| P-09 | Q_CD whole-vector sampling/composition | B | F5 | UNRESOLVED — OWNER_DECISION_REQUIRED + MEASUREMENT_REQUIRED | Q_CD = construction/provenance law, not latent probability (A-03/A-04) | EV-01,06,08 | EV-13..17 | owner + measurement define composition law per (k,s) | ART-F5 | v11 §26.9, §2 | PI + CC |
| P-10 | Distinctness/acceptance thresholds | B | F5 | UNRESOLVED — MEASUREMENT_REQUIRED | truth clusters = distinct parameter instances | EV-01,06 | EV-13..17 | thresholds from calibrated parameter distributions | ART-F5 | v11 §26.10 | CC + PI |
| P-11 | B* size | B | F6 | UNRESOLVED / OWNER_DECISION_REQUIRED / MEASUREMENT_REQUIRED | justified only by outcome-blind bank-construction / design-coverage adequacy evidence available by F6; never convenience-only; no dependence on the later F10 precision calculation; no exact resolution rule invented beyond v11 | EV-06,08 | EV-13..17; F10 precision outputs | owner decision + measurement from F6-available design-coverage adequacy evidence; PI ratifies | ART-F6 | v11 §26.11 | PI + CC |
| P-12 | Design weights | B | F5→F6 | UNRESOLVED — OWNER_DECISION_REQUIRED | `weight_semantics = "design_weight"`; `latent_probability_claim = false`; weights must sum correctly | EV-08 | EV-13..17 | rule pinned at F5; frozen values hashed at F6 | ART-F5/F6 | v11 §26.12, §23.3 | PI |
| P-13 | Coverage guard | B | F5 | UNRESOLVED — MEASUREMENT_REQUIRED | infeasible support → `coverage_gap`, no filler (A-27) | EV-06 | EV-13..17 | guard defined from feasibility measurement | ART-F5 | v11 §26.13 | CC + PI |
| P-14 | New-project numeric `n_per_cluster` | B | F5 | UNRESOLVED — OWNER_DECISION_REQUIRED | `class_size_policy="equal"`; `inherit_old_n_per=false`; `C_NPER_STATUS=forbidden`; historical `n_per=10` = provenance only, never rationale | EV-08,09 | EV-13..17; historical n_per as rationale | owner pins numeric value with outcome-blind written justification | ART-F5 | v11 §26.14, §7.1, §17 | PI |
| P-15 | Geometry strata | B | F7 | UNRESOLVED — MEASUREMENT_REQUIRED | signed rho only; strata after feasibility, before outcomes | EV-06 | EV-13..17; historical rho bands as triggers | strata from observed feasibility; PI ratifies | ART-F7 | v11 §26.15, §6 | CC + PI |
| P-16 | `epsilon` / `delta` | B | F7 | UNRESOLVED — MEASUREMENT_REQUIRED | frozen after feasibility observed, before outcome reading (v11 §8) | EV-06 | EV-13..17 | from matched-panel QC feasibility measurement | ART-F7 | v11 §26.16, §8 | CC + PI |
| P-17 | H* sigma strata | B | F8 | UNRESOLVED — MEASUREMENT_REQUIRED | clean residual-supported; A-APP exclusions apply | EV-07 | EV-13..17 | measured residual-scale distribution → strata | ART-F8 | v11 §26.17, §7.2 | CC + PI |
| P-18 | Empirical temporal-dependence representation | B | F8 | UNRESOLVED — MEASUREMENT_REQUIRED | no automatic phi→0.97; snaps need empirical justification, outcome-blind, F8-frozen | EV-07 | EV-13..17; automatic snap | measured dependence → representation + `phi_source` | ART-F8 | v11 §26.18, §7.2 | CC + PI |
| P-19 | White-noise ceiling diagnostic | B | F8 | UNRESOLVED — MEASUREMENT_REQUIRED | diagnostic role; part of H* support evidence | EV-07 | EV-13..17 | diagnostic spec + measurement | ART-F8 | v11 §26.19 | CC + PI |
| P-20 | `Delta_eq` numeric justification | B | F10 | UNRESOLVED — OWNER_DECISION_REQUIRED | scientific/practical relevance; outcome-before; budget-adaptive forbidden | EV-08 | EV-13..17; budget pressure | owner writes scientific relevance justification; pinned pre-outcome | ART-F10 | v11 §26.20, §12 | PI |
| P-21 | Paired precision target | B | F10 | UNRESOLVED — MEASUREMENT_REQUIRED | strictly derived from Delta_eq (causal chain A-39) | EV-08,09 | EV-13..17; reverse causation | derived from pinned Delta_eq | ART-F10 | v11 §26.21, §12 | CC + PI |
| P-22 | Scenario/seed allocation | B | F10 | UNRESOLVED — MEASUREMENT_REQUIRED | no 100-seed assumption; resolved only after `Delta_eq` and the precision target are frozen; disagreement inputs outcome-blind (bounds/assumptions/dedicated constructs only); allocation cannot change frozen `B*` or design semantics | EV-09,10 | EV-13..17; convenience | post-`Delta_eq` preflight (analytic bounds → frozen weights → outcome-blind disagreement characterization → simulation if needed) → allocation | ART-F10 | v11 §26.22, §12 | CC + PI |
| P-23 | CRN seed namespace | C | F10 | UNRESOLVED | CRN required (A-35); namespace must guarantee valid pairing | EV-09 | EV-13..17 | implementation spec; PI ratifies | ART-F10 | v11 §26.23, §9 | CC → PI |
| P-24 | BANK-SENS-S exact implementation | B | F11 | UNRESOLVED (preferred candidate `scenario_id_cluster_bootstrap`) | winner-ineligible; not primary CI; CRN/pairing + strata preserved; scenario = resampling cluster; delta-method optional only | EV-03..07 class checks, EV-08,09,10 | EV-13..17; result-anticipation | exact procedure pinned at F11 after calibration-structure checks | ART-F11 | v11 §26.24, §10 | PI + CC |
| P-25 | BANK-SENS-L applicability audit + exact implementation/fallback | B (fallback branch D) | F11 | UNRESOLVED — CONDITIONAL fallback | six-condition applicability QC (see F11); `zero_new_runs != statistical_applicability`; no silent skip → freeze STOP | EV-03..07 class checks on F6 incidence metadata, EV-08 | EV-13..17 | audit → applicable/not_applicable → exact method or pre-frozen fallback | ART-F11 | v11 §26.25, §11 | PI + CC |
| P-26 | Transfer qualification thresholds | B | F11 | UNRESOLVED — MEASUREMENT_REQUIRED / OWNER_DECISION_REQUIRED | TRANSFER-QUAL states fixed; eligible evidence sources = R-REALISTIC, E-BRIDGE, CAL-SENS, genuine held-out/external evidence if available (v11 §15) — none winner-defining; depends on the F8-frozen robustness/transfer law and the ≤F11 bridge/CAL-SENS panel specs; cannot change scientific winner | EV-03..08 | EV-13..17 | thresholds pinned pre-outcome against the frozen eligible evidence sources | ART-F11 | v11 §26.26, §15 | PI |
| P-27 | R-REV eligibility gate | D | UNRESOLVED (pre-F12, outcome-blind; exact gate assignment OWNER_DECISION_REQUIRED — v11 §22 does not assign R-REV a gate) | CONDITIONAL | R-REV activates only if outcome-blind empirical eligibility passes (A-15) | EV-01,02,04 | EV-13..17 | owner assigns gate + pins eligibility rule before any outcome | ART at owning gate | v11 §26.27, §4 | PI |
| P-28 | Operational deployment policy | D | F11 (ratified F12) | CONDITIONAL — only if a single pipeline is truly required | external/exogenous measurable criteria; simplicity alone insufficient; continuity labeled non-scientific; cannot change scientific results (A-42) | EV-08 + measured operational constraints | EV-13..17; scientific results | pinned at F11 iff genuine deployment need + measurable constraints exist | ART-F11 | v11 §26.28, §14 | PI |
| P-29 | Software/environment hashes | C | F9 | UNRESOLVED | reproducibility requirement (§23.1) | environment facts | EV-13..17 | freeze + hash environment at F9 | ART-F9 | v11 §26.29 | CC |
| P-30 | Executable manifest QC | C | F11 | UNRESOLVED | canonical field names of §23; §24 checks executable | F0–F10 artifacts | EV-13..17 | implement QC harness against §23/§24; PI ratifies | ART-F11 | v11 §26.30, §23–24 | CC → PI |
| P-31 | Final report language | C | F11→F12 | UNRESOLVED | mandatory limitation language; runner-up fields; claim boundary (A-05) | F0–F11 artifacts | EV-13..17 | reporting rules frozen F11, ratified F12 | ART-F11/F12 | v11 §26.31 | PI |
| P-32 | Explicit F12 sign-off | C (governance act, not a scientific choice) | F12 | UNRESOLVED | ratification only; no new methods at F12; unsigned → draft_only | completed F0–F11 | EV-17 until signed | PI performs sign-off + external hash sidecar | ART-F12 | v11 §26.32, §22 | PI |

Register notes:

- Venue choice is **not** in this register (v11 §26: not a methodological
  calibration pin). Unresolved non-material panel identity is not a blocker.
- Particularly protected pins (no guessing, no convenience defaults, no legacy
  outcome influence): P-01..P-05 (generator/adequacy/tie-break/cross-fit),
  P-09..P-14 (Q_CD/B*/weights/n_per_cluster), P-15..P-16 (geometry strata,
  epsilon/delta), P-17..P-19 (H*), P-20..P-23 (Delta_eq/precision/allocation/
  CRN), P-24..P-25 (BANK-SENS-S/L), P-26 (transfer), P-27 (R-REV), P-28
  (operational policy).

---

# 5. Evidence firewall matrix

Semantics (binding):

- legacy references may serve as provenance/context;
- legacy outcome results may NOT justify or tune any calibration pin — doing so
  is a **FIREWALL VIOLATION**;
- new-project algorithm × CVI outcomes are PROHIBITED before F12 sign-off;
- LLM opinion/consensus is not empirical evidence;
- venue is non-gating administrative metadata.

| ev_id | evidence_class | allowed_for_calibration_pin? | allowed_as_provenance? | allowed_before_F12? | notes |
|---|---|---|---|---|---|
| EV-01 | raw_SSA_trajectory_data | yes | yes | yes | only via the frozen F1 inventory; outcome-blind use |
| EV-02 | outcome_blind_generator_fit | yes | yes | yes | F2/F3/F4 evidence; no algorithm/CVI content |
| EV-03 | cross_fit_adequacy | yes | yes | yes | F3 evidence under frozen scheme |
| EV-04 | residual_structure | yes | yes | yes | F3/F4/F8 evidence |
| EV-05 | parameter_stability | yes | yes | yes | F3/F4 evidence |
| EV-06 | geometry_feasibility | yes | yes | yes | F5/F6/F7 evidence; signed rho only |
| EV-07 | residual_noise_measurement | yes | yes | yes | F8 evidence; no automatic snap |
| EV-08 | scientific_practical_relevance_argument | yes | yes | yes | must be outcome-blind, written, owner-signed (e.g. Delta_eq, n_per_cluster); includes methodological literature |
| EV-09 | analytic_precision_bound | yes | yes | yes | F10 preflight element |
| EV-10 | outcome_blind_simulation | yes | yes | yes | only as v11 §12 preflight; outputs restricted to variance/allocation statistics; no pipeline ranking may be extracted; accidental exposure logged as provenance violation |
| EV-11 | legacy_protocol_text | no (context only) | yes | yes (read-only) | wording differences resolved by `v11_wins`; never normative inheritance |
| EV-12 | legacy_run_manifest | no (context only) | yes | yes (read-only) | e.g. historical `n_per=10` = provenance fact, never rationale |
| EV-13 | legacy_winner_results | no — FIREWALL VIOLATION if used | yes (identity/hash custody) | no (content reading) | historical comparator content enters only post-F12 via X-LEGACY-HIST |
| EV-14 | legacy_S06_diagnostics | no — FIREWALL VIOLATION if used | yes (identity/hash custody) | no (content reading) | as EV-13 |
| EV-15 | legacy_robustness_results | no — FIREWALL VIOLATION if used | yes (identity/hash custody) | no (content reading) | as EV-13 |
| EV-16 | legacy_SSA_deployment_results | no — FIREWALL VIOLATION if used | yes (identity/hash custody) | no (content reading) | as EV-13 |
| EV-17 | algorithm_CVI_outcomes_new_project | no | no (must not exist pre-F12) | no — PROHIBITED | absolute outcome firewall; exposure = logged provenance violation |
| EV-18 | LLM_opinion_or_consensus | no | yes (panel ledger) | yes (as ledger metadata) | not empirical evidence; not a reopening trigger (v11 §20) |
| EV-19 | venue_choice | no | yes (administrative metadata) | yes | `venue_is_methodology_gate = false`; cannot alter any design element |

---

# 6. Artifact DAG (pre-outcome)

```text
v11 normative source
    ->
F0 identity/provenance
    ->
F1 frozen calibration inputs
    ->
F2 generator specifications
    ->
F3 adequacy + selected generator
    ->
F4 parameter/source bank
    ->
F5 Q_CD + n_per_cluster
    ->
F6 B*
    ->
F7 geometry freeze
    ->
F8 H*
    ->
F9 method registry/environment
    ->
F10 Delta_eq/precision/allocation
    ->
F11 manifest + analysis/sensitivity implementation
    ->
F12 PI ratification + external freeze hash
    ->
algorithm × CVI outcome access
```

- **No reverse arrows.** No outcome node feeds any calibration node.
- In particular there is no `F10 -> F6` edge: `B*` size and contents are frozen at F6; F10 allocation cannot resize, reweight, or otherwise alter `B*`, `Q_CD`, geometry, `H*`, or their frozen design semantics.
- Staged execution of gates is allowed; staged outcome reading is not (v11 §22).
- `coverage_gap` at F7 is a lateral annotation, not a back-edge.

---

# 7. Manifest governance — canonical fields by freeze gate

Canonical field names from v11 §23 — never renamed for convenience.
`population_time` values: `F-gate` (fixed/populated during calibration) or
`POST_F12_ONLY` (outcome-bearing; populated only after F12 sign-off).

## 7.1 Provenance (v11 §23.1)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `project_id` | F0 | F0 | |
| `design_version` | F0 | F0 | |
| source/input/code/registry/environment/parent hashes | F1 (input), F9 (code/registry/env), F0 (parent) | respective gates | |
| `panel_source_ledger_hash` | F0 | F0 | |
| `methodology_contract_status` | F0 (field) | updated per lifecycle; terminal at F12 | lifecycle §10 |

## 7.2 Design / scope (v11 §23.2)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `question_id` | F0 | F0 | |
| `design_block` | F0 (architecture A-48) | per-run manifest | |
| `claim_scope` | F0 | F0 | A-05 boundary |
| `winner_layer` | F0 (A-APP only) | per-run manifest | |
| `stage` | F0 (schema) | per-stage | |
| `calibration_sex` | F1 | F1+ | |
| `k_true` | F5/F6 (per scenario) | F6 | |
| `class_size_policy` | value normative now (`"equal"`) | F5 manifests | A-28 |
| `n_per_cluster` | F5 | F5 | P-14; UNRESOLVED |
| `class_sizes` | F5/F6 | F6 | equal by policy |
| `composition_id` | F5 | F5/F6 | |
| `C_NPER_STATUS` | — | FORBIDDEN FIELD | must not appear (A-29) |

## 7.3 Bank / design measure (v11 §23.3)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `parameter_bank_id`, `parameter_bank_hash` | F4 | F4 | |
| `q_cd_rule_id`, `q_cd_rule_hash` | F5 | F5 | |
| `bank_id`, `bank_hash` | F6 | F6 | |
| `scenario_id`, `scenario_source_ids` | F6 | F6 | BANK-SENS-L precondition |
| `resampling_rule_id` | F11 | F11 | BANK-SENS resampling |
| `weight_source`, `weight_hash` | F5 (rule) / F6 (values) | F6 | |
| `weight_semantics` | value normative now (`"design_weight"`) | all manifests | A-04 |
| `latent_probability_claim` | value normative now (`false`) | all manifests | A-04 |

## 7.4 Morphology / geometry (v11 §23.4)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| generator family/version/hash | F3 | F3+ | |
| shape family/regime/subtype | F4 | F4 | descriptors |
| `prototype_instance_id`, `prototype_instance_hash` | F4 | F4 | truth identity |
| observed descriptors | F4 | F4 | P-06 thresholds |
| `label_fuzz` | F4 | F4 | P-07 |
| signed rho fields (`rho_max_pair`, `rho_mean`, `rho_min`), `theta_min`, `d_eff`, Gram spectrum, `hardpair_code`, `unexpected_nearest_pair`, `envelope_status`, `coverage_gap_reason` | F7 | F6/F7 | signed Pearson only |
| `epsilon`, `delta` | F7 | F7 | P-16; UNRESOLVED |

## 7.5 Noise / randomness (v11 §23.5)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `sigma`, `sigma_source` | F8 | F8 | |
| `noise_type` | F8 | F8 | |
| `phi`, `phi_source` | F8 | F8 | no automatic snap |
| `seed_namespace`, `CRN_id` | F10 | F10 | P-23 |

## 7.6 Outcomes (v11 §23.6) — schema listed, values firewalled

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `k_hat` | F9 (schema) | **POST_F12_ONLY** | |
| `correct` | F9 (schema) | **POST_F12_ONLY** | |
| `bias` | F9 (schema) | **POST_F12_ONLY** | |
| `k_hat_tie` | F9 (schema) | **POST_F12_ONLY** | |
| `cvi_failure` | F9 (schema) | **POST_F12_ONLY** | |
| `algorithm_failure` | F9 (schema) | **POST_F12_ONLY** | |
| `converged` | F9 (schema) | **POST_F12_ONLY** | |

## 7.7 Uncertainty / sensitivity (v11 §23.7)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `mcse` | F11 (estimator) | **POST_F12_ONLY** | |
| `bank_sens_s_method` | F11 | F11 | P-24 |
| `bank_sens_s_status` | F11 | F11 / POST_F12 results | |
| `bank_sens_l_method` | F11 | F11 | P-25 |
| `bank_sens_l_applicability_status` | F11 | F11 | six-condition audit |
| `bank_sens_l_not_applicable_reason` | F11 | F11 | mandatory if not applicable |
| `bank_sens_l_source_count` | F11 | F11 | |
| `calibration_sensitivity_role` | F11 | F11 | CAL-SENS |

## 7.8 Transfer / operational (v11 §23.8)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `distinct_transfer_source_or_law` | F0 default `false`; changed only at F11 with evidence | F11 | D-4 |
| `historical_tie_break_privilege` | value normative now (`false`) | F0 | A-41 |
| `operational_tie_break_policy_id` | F11 (conditional) | F11 | P-28 |
| `operational_tie_break_scientific` | value normative now (`false`) | F11 | |
| `venue_status` | value normative now (`"administrative_metadata"`) | F0 | |
| `venue_is_methodology_gate` | value normative now (`false`) | F0 | |

## 7.9 Secondary registry (v11 §23.9)

| field | freeze gate | population_time | notes |
|---|---|---|---|
| `frozen_v53_friedman_formulations` | F9 | F9 | canonical value `["sil_euc","DB","CH","Dunn_d1_D1"]` (A-45) |

---

# 8. Secondary-block governance map

Every v11 §21 block/panel, mapped for execution governance. This map creates
**no new DGP detail, no numeric value, and no new calibration pin** — the v11
§26 inventory remains exactly 32 items. Gate assignments not fixed by v11 §22
are marked honestly as owner decisions rather than guessed. Winner
eligibility is exactly the v11 §21 column: A-APP only.

New-DGP-block rule (v11 §16, binding for any proposed new block):

```text
What scientific question cannot be answered by an existing
block or sensitivity panel?

If no such question exists:
    new_block = rejected
```

| block | role | winner_eligible | activation_status | specification_gate | required_pre_outcome_artifact | open_pin_if_any | failure_status |
|---|---|---|---|---|---|---|---|
| A-APP | frozen `B*×H*` all-k exact-k primary winner layer | **YES** (only winner-eligible block) | ACTIVE (mandatory primary) | F5–F8 (design), F10 (allocation), F11 (analysis) | ART-F5..ART-F11 chain | P-09..P-25 chain | gate STOPs (STOP-07..09, STOP-11); terminal outcomes `precision_insufficient` / `coverage-limited` |
| A-MECH | matched/common-support hard-pair mechanism panel | no | CONDITIONAL on matched feasibility observed at F7 | F7 | matched-panel QC record (in ART-F7) | P-16 (`epsilon`/`delta`) | infeasible → `coverage_gap` = conditional_panel_NO_GO (never global) |
| A-RESPONSE / X-CANON | canonical response surface; historical comparability; stress characterization | no (`winner_eligible = false`, `application_probability = none`) | ACTIVE (secondary; grid closed by v11 §7.3) | F8 | canonical response definitions (in ART-F8) | none (sigma/noise grid closed by A-33) | descriptive only; cannot affect winner |
| E-BRIDGE | bridge umbrella (E-ACTUAL + E-MATCHED) | no | ACTIVE as umbrella taxonomy | ≤F11 pre-outcome (v11 §22 assigns no gate; exact placement OWNER_DECISION_REQUIRED) | bridge panel specification record | panel spec = pre-outcome implementation item, not a §26 pin | not independent external validation; informs TRANSFER-QUAL only |
| E-ACTUAL | actual-support / real-derived semi-synthetic bridge | no | CONDITIONAL subpanel of E-BRIDGE | ≤F11 (with E-BRIDGE) | subpanel spec under E-BRIDGE record | panel spec (not a §26 pin) | not winner-defining |
| E-MATCHED | common-support matched bridge | no | CONDITIONAL subpanel of E-BRIDGE | ≤F11 (with E-BRIDGE) | subpanel spec under E-BRIDGE record | panel spec (not a §26 pin) | not winner-defining |
| R-REALISTIC | robustness perturbations | no | ACTIVE (secondary) | F8 (pre-outcome robustness/transfer law) + F11 (analysis role) | robustness/transfer law record (in ART-F8) | law = F8 gate freeze object (v11 §22), not a §26 pin | narrows claims only; cannot affect winner |
| TRANSFER-QUAL | deployment qualification gate | no | ACTIVE (default, v11 §15) | F11 (P-26 thresholds) | qualification thresholds + evidence mapping to R-REALISTIC / E-BRIDGE / CAL-SENS / genuine held-out-external (in ART-F11) | P-26 | states {qualified, qualified_with_caveats, failed}; can narrow/veto deployment claim; cannot change scientific winner |
| X-LEGACY-HIST | historical frozen comparator/reference | no | content ACTIVE post-F12 only; pre-F12 identity/hash custody only (EV-13..EV-16 firewall) | F0 (provenance ledger) | F0 provenance ledger (ART-F0) | none | read-only; pre-F12 content reading falls under STOP-15/STOP-16 |
| S-NEG | negative controls (excluded morphologies: level_shift, cylinder, impulse, abrupt) | no | ACTIVE (secondary control) | ≤F11 pre-outcome (v11 §22 assigns no gate; placement OWNER_DECISION_REQUIRED) | negative-control panel spec | panel spec (not a §26 pin) | control-only; cannot affect winner |
| R-REV | gated revival/multi-wave | no | CONDITIONAL (D-1) — only if the outcome-blind empirical eligibility gate passes | UNRESOLVED (= P-27; owner assigns gate pre-F12, outcome-blind) | eligibility gate record | P-27 | gate fails → NOT_APPLICABLE |
| H0-XREF | prior null-work cross-reference | no | ACTIVE (reference panel) | F0 (ledger entry); reporting role at F11 | ledger entry (in ART-F0) | none | reference-only |
| BANK-SENS-S | scenario-bank sensitivity | no (winner-ineligible, not primary CI) | ACTIVE (mandatory) | F11 | exact procedure pin (in ART-F11) | P-24 | unresolved → F11 incomplete → no outcome reading (STOP-13) |
| BANK-SENS-L | source-influence sensitivity | no (winner-ineligible, not primary CI) | ACTIVE (mandatory) | F11 (applicability audit + method/fallback) | applicability audit + method pin (in ART-F11) | P-25 | no interpretable implementation → `sensitivity_class_status = "unresolved"`, `methodology_freeze_status = "STOP"` (STOP-12, global) |
| CAL-SENS | calibration sensitivity | no | ACTIVE (secondary; `calibration_sensitivity_role` fixed at F11) | F11 | calibration-sensitivity scope record (in ART-F11) | scope = owner item at F11, not a §26 pin | winner-ineligible; informs TRANSFER-QUAL |
| E-WEIGHT | design-weight sensitivity | no | ACTIVE (secondary) | F11 | weight-sensitivity scope record (in ART-F11) | scope = owner item at F11, not a §26 pin | winner-ineligible |

---

# 9. STOP register

Classes: `global_STOP` (project halts), `gate_STOP` (gate cannot close;
downstream blocked), `conditional_panel_NO_GO` (panel-only), `provenance_violation`
(logged; taints affected chain).

| stop_id | trigger | class | gate | mandated behavior |
|---|---|---|---|---|
| STOP-01 | normative v11 hash mismatch | global_STOP + provenance_violation | any | halt; do not repair/replace/normalize the normative source |
| STOP-02 | material design-relevant provenance contradiction | global_STOP | F0 | STOP/reconcile per v11 §22; reopening class 2 evidence required |
| STOP-03 | unresolved F1 inputs | gate_STOP | F1 | calibration cannot freeze |
| STOP-04 | incomplete F2 generator specification | gate_STOP | F2 | STOP until owner completes spec |
| STOP-05 | both primary generators fail F3 adequacy | global_STOP | F3 | `action = redesign`; no third family improvisation |
| STOP-06 | unstable/unsupported F4 parameter bank | gate_STOP | F4 | no B* |
| STOP-07 | ambiguous/collapsed F5 Q_CD / design support | gate_STOP | F5 | revise or STOP |
| STOP-08 | incomplete B* | gate_STOP | F6 | no run |
| STOP-09 | unsupported H* | gate_STOP | F8 | no A-APP freeze |
| STOP-10 | ambiguous F9 registry / failure rules | gate_STOP | F9 | no run |
| STOP-11 | inadequate F10 precision after permitted adjustments | gate_STOP (defined terminal outcome) | F10 | narrow secondary → optimize primary → `precision_insufficient`; primary never silently degraded |
| STOP-12 | unresolved mandatory BANK-SENS-L | global_STOP | F11 | `sensitivity_class_status="unresolved"`, `methodology_freeze_status="STOP"` |
| STOP-13 | incomplete F11 analysis/sensitivity contract | gate_STOP | F11 | no outcome reading |
| STOP-14 | unsigned F12 | gate_STOP | F12 | `draft_only`; outcome access remains PROHIBITED |
| STOP-15 | early algorithm × CVI outcome exposure | provenance_violation | any | log; cannot alter confirmatory design; affected chain never presented as pristine preregistered |
| STOP-16 | information-firewall violation (legacy or premature outcome information contaminates a calibration pin) | provenance_violation + gate_STOP for affected chain | any | recovery sequence below; contamination is never silently erased or overwritten, and re-derivation does NOT restore pristine preregistration status |

Boundary rule: secondary-panel geometry infeasibility is `coverage_gap` =
`conditional_panel_NO_GO` (v11 §22 F7) — it is never escalated to global STOP.

Firewall-violation recovery (STOP-16 detail, binding):

```text
record provenance violation
-> gate STOP for affected chain
-> do not claim that simple re-derivation restores pristine preregistration
-> affected chain cannot be presented as pristine preregistered
-> any recovery/disposition requires explicit PI governance consistent with v11
```

The contaminated history is preserved in the provenance log and must not be
silently erased or overwritten. Any re-derived pin carries a permanent
contamination annotation in its pin record and in reporting; the affected
chain is never presented as "pristine preregistered" (v11 §22).

---

# 10. Reopening register

Lifecycle (v11 §27):

```text
draft
-> calibration_pins_complete
-> manifest_analysis_contract_complete
-> explicit_signoff
-> frozen
```

After `frozen`, reopening only if one of the three valid classes holds:

1. calibration materially falsifies a frozen design assumption;
2. provenance/source audit reveals a material design-relevant contradiction;
3. a genuinely new objection class appears.

Explicit NON-triggers (v11 §27):

- another LLM gives a different score/opinion;
- the same objection reworded;
- LLM consensus change;
- historical Ward+CH absent from top results;
- venue change;
- secondary ranking difference;
- unresolved non-material panel identity;
- wording/granularity difference between prior v11 artifacts.

---

# 11. FORBIDDEN_OR_REJECTED register (class E) — v11 §25

1. rewrite old frozen project;
2. treat old Ward+CH as new scientific prior/winner;
3. use Ward+CH as automatic scientific tie-break;
4. use Ward+CH as automatic operational tie-break;
5. use `max|rho|` as primary geometry;
6. treat historical rho bands as target-probability law;
7. force artificial geometry filler;
8. k=5-only primary estimand;
9. canonical sigma/AR(.97) as application-probability winner layer;
10. automatic phi→.97 snap without empirical justification;
11. morphology-specific sigma in A-APP;
12. A-APP forced hard-pair counterbalancing;
13. automatic spline fallback;
14. additional primary generator family without reopening trigger;
15. DTW/elastic alignment;
16. seed-level hypothesis tests;
17. BANK-SENS-S/L as target-population confidence intervals;
18. mandatory incidence-jackknife irrespective of support structure;
19. silently dropping BANK-SENS-L;
20. `zero new runs => statistical validity`;
21. budget-driven Delta_eq coarsening;
22. forced unique winner;
23. duplicate A_TRANSFER using same source/law;
24. carry old `C_NPER_STATUS` into new project;
25. inherit historical n_per automatically;
26. unfreeze Friedman set by preference;
27. Friedman/Nemenyi as primary scientific winner statistic;
28. hard-code venue into DGP/estimand freeze;
29. count LLM consensus as independent empirical evidence;
30. open a new numbered methodology round solely for wording reconciliation.

Count: **30 FORBIDDEN_OR_REJECTED items.**

---

# 12. Class-count summary and conditional register

| class | count | basis |
|---|---|---|
| A — NORMATIVE_CLOSED | 50 | §2 register |
| B — CALIBRATION_OPEN | 25 | pin register: P-01..P-22 (22) + P-24, P-25, P-26 (3) |
| C — IMPLEMENTATION_OPEN | 5 | P-23, P-29, P-30, P-31, P-32 |
| D — CONDITIONAL_OR_NOT_YET_APPLICABLE | 6 | register below (D-1/D-2 coincide with P-27/P-28) |
| E — FORBIDDEN_OR_REJECTED | 30 | §11 register |

Conditional register (class D):

| d_id | item | activation condition | v11 |
|---|---|---|---|
| D-1 | R-REV revival/multi-wave panel (= P-27) | outcome-blind empirical eligibility gate passes | §4, §26.27 |
| D-2 | Operational deployment policy (= P-28) | a single pipeline is genuinely operationally required, with measurable external constraints | §14, §26.28 |
| D-3 | BANK-SENS-L fallback path (branch of P-25) | incidence applicability audit returns `not_applicable` | §11.2 |
| D-4 | Distinct transfer estimand/DGP block | `distinct_transfer_source_or_law = true` with genuinely distinct source/law | §15 |
| D-5 | Delta-method BANK-SENS-S cross-check | optional supplement; only if explicitly frozen at F11 | §10 |
| D-6 | Incumbent-continuity operational label | stakeholder continuity requested; labeled `policy_type = "non_scientific_stakeholder_continuity"` | §14 |

---

# 13. Machine-readable status block

```text
document =
  yeni_proje_empirik_kalibrasyon_protokolu_v0.md

document_role =
  normative_working_artifact

parent_normative_source =
  ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md

parent_normative_sha256 =
  d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3

methodology_panel_status =
  CLOSED

protocol_status =
  DRAFT

calibration_execution_status =
  NOT_STARTED

calibration_pins_complete =
  false

manifest_analysis_contract_complete =
  false

F12_explicit_PI_signoff =
  false

frozen =
  false

algorithm_CVI_outcome_access =
  PROHIBITED

legacy_information_firewall =
  ACTIVE
```

No freeze sidecar accompanies this draft; the external hash sidecar is an F12
artifact and is not created before F12.
