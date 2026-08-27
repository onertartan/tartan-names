# SSA Application-Calibrated Clustering Benchmark
## v11 FINAL NORMATIVE — Claude Code Handoff / Decision-Freeze Candidate

**Tarih:** 2026-08-27  
**Statü:** FINAL NORMATIVE METHODOLOGY CONTRACT — henüz PI imzasıyla `frozen` durumuna geçirilmedi  
**Sonraki çalışma belgesi:** `yeni_proje_empirik_kalibrasyon_protokolu_v0.md`  
**Outcome firewall:** F12 imzası tamamlanmadan hiçbir algorithm × CVI performans sonucu okunmaz.

---

# 0. Yetki, precedence ve provenance

Bu dosya, ChatGPT v11 ile Claude v11 terminal sürümlerinin son çapraz-kontrolünden sonra oluşturulmuş **tek normatif metodoloji kaynağıdır**.

Claude Code içinde precedence:

```text
normative_methodology_source =
    "ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md"
```

Önceki ChatGPT/Claude v11 belgeleri:

- corroborative provenance,
- karar-soyağacı,
- audit/support belgesi

olarak tutulabilir; **normatif çelişki çözmek veya bu dosyadaki donmuş hükmü yeniden açmak için kullanılmaz**.

Kural:

> Wording, granularity, freeze-stage placement veya manifest-field naming bakımından eski terminal belgelerle fark varsa bu FINAL NORMATIVE dosya geçerlidir. Sırf ifade farkını uzlaştırmak için frozen metodolojik karar yeniden açılamaz.

## 0.1 Reconciliation sources

- ChatGPT v11:
  - `ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md`
  - SHA256 `3bd9e7cfdbdfe9358f91792db12447594d86956cd1c1b185552cb2da4d94b787`

- Claude v11:
  - `claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md`
  - SHA256 `29c073ba5105a14299a0ea9427d8443c1a29d40960f7fed355ef49b2bae67c5a`

## 0.2 Historical frozen project — read-only normative references

- `01_kosum_protokolu_v5_3.md`
  - SHA256 `cf8b453f0a05e2e6fed0c8b73692c2a5361fdfe60a22b3c9fe8c612e0e13db67`

- `kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md`
  - SHA256 `99c17c42711fd27dd2e55baf55f5ed41388b14a39a29e196f8eb1def34a5d0a7`

- `run_matrix_v4.csv`
  - SHA256 `34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64`

Eski benchmark:
- bit-immutable,
- read-only,
- historical comparator/provenance kaynağıdır.

Eski projedeki bilimsel seçimler yeni projeye otomatik normatif miras değildir.

---

# 1. Project identity ve claim boundary

Bu çalışma eski frozen benchmarktan **ayrı yeni bir preregistered/application-calibrated project**tir.

Primary soru:

> Sonuç-kör SSA kalibrasyonuyla kısıtlanmış ve outcome öncesi dondurulmuş finite bir application-design bank üzerinde, hangi clustering algorithm × CVI pipeline `k_true ∈ {3,4,5,6,8}` değerini en yüksek design-weighted exact-k recovery ile bulur?

Allowed claim:

> performance across the frozen calibration-constrained application design

Forbidden claim:

> performance under the true latent SSA prototype distribution

Makine-okunur:

```text
weight_semantics = "design_weight"
latent_probability_claim = false
```

---

# 2. Primary scientific estimand

Her sex `s ∈ {M,F}` ve `k ∈ {3,4,5,6,8}` için:

```text
Q_CD(k,s)
```

= calibration-constrained joint-set construction/design/provenance law.

`Q_CD`:
- latent population probability değildir;
- SSA prototype prevalence modeli değildir;
- finite scenario bank üretim sözleşmesidir.

```text
B*_{k,s}
```

= outcome öncesi üretilmiş, freeze edilmiş, hash'lenmiş finite application scenario bank.

```text
H*_s
```

= outcome öncesi freeze edilmiş empirical clean residual-supported noise bank.

Primary score:

```text
A_m(k,s)
  = Σ_b Σ_h w_b u_h P_MC(k_hat_m = k | b,h)
```

Macro primary estimand:

```text
A_m^APP
  = (1/2) Σ_s (1/5) Σ_k A_m(k,s)
```

Finite estimator:

```text
Â_m
  = Σ_c ω_c (1/S_c) Σ_r I{k_hat_mcr = k_true,c}
```

Zorunlu sex-specific ve k-specific raporlama:
- `A_m(k,M)`
- `A_m(k,F)`
- macro pooled view.

---

# 3. k governance

Primary `k_true` support:

```text
K = {3,4,5,6,8}
v_k = 1/5
```

Sex pooling frozen ise:

```text
v_M = 1/2
v_F = 1/2
```

k=5:

```text
winner_privilege = false
```

k=5 yalnız:
- empirical mirror,
- descriptive anchor

olabilir.

`k_hat = k±1`:
- secondary partial-credit sensitivity;
- primary exact-k winner score'u değiştirmez.

Candidate selector search range:

```text
k_candidate = 2..10
```

---

# 4. Morphology ve truth identity

Primary morphology family:

```text
WC-ALC
```

Observed-window regimes:

- W-L — left-censored decline
- W-I — interior asymmetric wave
- W-R — right-censored ongoing rise

W-I için optional descriptors:
- early
- mid
- late

Regime:

```text
role = descriptor
truth_class = false
```

Primary truth cluster identity:

```text
frozen distinct generator/prototype parameter instance
```

Eski `(shape, location)` ontology:

```text
automatic_carryover = false
```

Primary morphology exclusions:
- level_shift
- cylinder
- impulse
- abrupt structures

Bunların rolü:

```text
S-NEG
```

Revival / multi-wave:

```text
R-REV
```

yalnız outcome-blind empirical eligibility gate geçerse.

DTW / elastic alignment:

```text
closed = true
```

---

# 5. Generator firewall

Primary candidate set yalnız:

1. WC-ADL
2. TAD/PSAT

Shape-constrained low-df spline:

```text
role = adequacy_benchmark
automatic_primary_fallback = false
```

Outcome-blind adequacy order:

1. morphology coverage
2. cross-fitted reconstruction / predictive fit
3. systematic residual morphology / residual structure
4. censored-case identifiability
5. parameter stability
6. parsimony

Exact equations, bounds, initialization ve fit-failure rules calibration protocolünde F2'de freeze edilir.

Tie-break:
- outcome-blind,
- pre-frozen,
- F3'te pinlenir.

Both primary candidates fail:

```text
STOP
action = redesign
```

Cross-fit:
- family/model adequacy selection audit içindir.

Family + fitting rules freeze edildikten sonra:
- seçilen generator tüm eligible calibration trajectories üzerine final-refit edilebilir;
- final-refit provenance loglanır;
- family seçimi yeniden açılamaz.

No clustering algorithm/CVI output generator selectionında kullanılamaz.

---

# 6. Geometry

Primary pairwise geometry:

```text
rho_max = max_{i<j} corr(P_i,P_j)
```

signed Pearson.

Mandatory geometry fields:
- `rho_max_pair`
- `rho_mean`
- `rho_min`
- `theta_min`
- `d_eff`
- Gram spectrum
- `hardpair_code`
- `envelope_status`
- `coverage_gap_reason`
- `unexpected_nearest_pair`

Forbidden primary substitute:

```text
max_abs_rho
```

`rho`:
- geometry descriptor,
- reporting variable,
- MC-efficiency stratum

olabilir.

`rho`:
- latent probability factor değildir.

Historical low-rho/dead-zone:

```text
historical_context_only = true
design_trigger = false
```

Natural easy domain:
- ceiling/equivalence findingdir;
- artificial difficulty yaratılmaz.

Infeasible support:

```text
coverage_gap
```

olarak raporlanır.

Artificial filler morphology:
```text
forbidden = true
```

---

# 7. A-APP class-size policy ve noise law

## 7.1 Class-size policy

A-APP primary clean core'da:

```text
class_size_policy = "equal"
```

Yani aynı scenario/cell içindeki truth clusters eşit büyüklüktedir.

Fakat ortak numeric value:

```text
n_per_cluster
```

**eski projeden miras alınmaz**.

Yeni proje için F5'te outcome öncesi bağımsız pinlenir:

```text
n_per_cluster = independently_frozen_new_project_parameter
inherit_old_n_per = false
```

Bu karar:
- equal-class-size convention'u korur,
- old C block'taki historical `n_per=10` değerini yeni projeye otomatik taşımaz.

## 7.2 Winner noise layer

Primary:

```text
A-APP = B* × H*
```

`H*`:
- empirical residual scale strata,
- empirical temporal dependence representation,
- common within-cell clean scale convention.

A-APP excludes:
- morphology-specific sigma
- jitter
- imbalance
- outliers
- morphology-noise coupling
- signal-scale robustness perturbation

Empirical temporal dependence:

```text
phi_primary = measured/calibrated representation
```

Automatic:

```text
phi_emp -> 0.97
```

forbidden.

Her discretization/snap:
- empirical measurement ile gerekçelendirilmiş,
- outcome-blind,
- F8'de freeze edilmiş

olmalıdır.

## 7.3 Canonical response layer

```text
sigma = 0.1 ... 1.0
noise = {white, AR(.97)}
winner_eligible = false
application_probability = none
```

Canonical block:
- response surface,
- historical comparability,
- stress characterization

içindir.

---

# 8. Hard-pair governance

A-APP:
- natural hard pair yalnız kaydedilir;
- forced counterbalancing yoktur.

A-MECH:
- matched/common-support mechanism panel.

Codes:
- HP-II
- HP-IB-L
- HP-IB-R
- HP-LL
- HP-RR

QC:

```text
|rho_intended-rho_target| <= epsilon
argmax(pairwise_rho) == intended_pair
max(non_target_rho) <= rho_target-delta
```

`epsilon`, `delta`:
- feasibility görüldükten sonra,
- outcome okunmadan önce

freeze edilir.

W-L × W-R:

```text
hardpair_code = "BB-OPP"
role = diagnostic_only
```

---

# 9. Primary uncertainty

Seeds:

```text
role = "Monte_Carlo_realization"
scientific_observation = false
```

Primary conditional MC variance:

```text
Var_MC(Â_m)
  = Σ_c ω_c^2 s^2_mc,c / S_c
```

Paired pipeline difference:

```text
D_c,r = Y_m,c,r - Y_n,c,r
```

```text
Var_MC(Â_m - Â_n)
  = Σ_c ω_c^2 s^2_D,c / S_c
```

CRN:

```text
required = true
```

Seed-level hypothesis tests:

```text
forbidden = true
```

Primary MC SE:
- frozen design'a koşulludur;
- target-population sampling uncertainty değildir.

---

# 10. BANK-SENS-S — scenario-bank sensitivity

Scientific class:

```text
BANK-SENS-S.required = true
winner_eligible = false
primary_CI = false
```

Preferred first-line candidate:

```text
scenario_id_cluster_bootstrap
```

Requirements:
- CRN/pairing preserved;
- relevant strata preserved;
- scenario unit correctly treated as resampling cluster.

Delta-method:
- optional cross-check / supplementary candidate;
- **otomatik zorunlu değildir**.

Alternative frozen-bank comparison:
- eligible sensitivity method.

Exact BANK-SENS-S procedure:

```text
freeze_stage = F11
```

F12:
- yalnız analysis-contract ratification/sign-off yapar;
- yeni sensitivity yöntemi ilk kez F12'de seçilemez.

---

# 11. BANK-SENS-L — source-trajectory influence sensitivity

Scientific class:

```text
BANK-SENS-L.required = true
winner_eligible = false
primary_CI = false
```

Preferred first-line candidate:

```text
incidence_delete_source_jackknife
```

Avantaj:

```text
new_algorithm_CVI_runs_required = 0
```

Ancak:

```text
zero_new_runs != statistical_applicability
```

## 11.1 Mandatory applicability QC

Incidence/delete-source method ancak tümü sağlanırsa uygulanır:

1. `scenario_source_ids` complete ve deterministic;
2. her delete-source operation required `(sex,k)` strata'da yorumlanabilir nonempty support bırakıyor;
3. renormalized design weights finite ve well-defined;
4. deletion, estimand support'u yorumu imkânsızlaştıracak biçimde mekanik olarak yok etmiyor;
5. required stratumda source incidence structurally universal değil;
6. deletion sonrası scenario dependency/duplication structure documented.

Pass:

```text
bank_sens_l_incidence_status = "applicable"
```

Fail:

```text
bank_sens_l_incidence_status = "not_applicable"
```

ve explicit reason zorunlu.

## 11.2 Eligible fallback methods

F11 öncesi/calibration evidence'e göre pre-frozen alternative:

- calibration-stage source-subset / bank-rebuild jackknife;
- grouped source deletion;
- alternative frozen-bank/source-influence design.

No silent skip:

```text
if no interpretable BANK-SENS-L implementation exists:
    sensitivity_class_status = "unresolved"
    methodology_freeze_status = "STOP"
```

Sensitivity limitation language mandatory:

> BANK-SENS-L is a winner-ineligible source-influence sensitivity analysis; it is not a primary confidence interval and does not by itself represent target-population sampling uncertainty.

Exact method:

```text
freeze_stage = F11
```

F12:
- ratifies,
- does not newly choose the method.

---

# 12. Delta_eq, precision ve compute budget

Strict causal/governance direction:

```text
Delta_eq
-> paired MC precision target
-> scenario/seed allocation
-> compute budget
```

Forbidden:

```text
compute_budget
-> enlarge Delta_eq
```

`Delta_eq`:
- scientific/practical relevance margin;
- outcome-before;
- budget-adaptive değildir.

100 seeds:
- automatically adequate değildir;
- automatically inadequate değildir.

Mandatory precision preflight:
- analytic worst-case bounds;
- frozen design weights;
- paired-disagreement structure;
- outcome-blind simulation if necessary.

Budget insufficient ise sıra:

1. secondary scope daralt;
2. primary allocation optimize et;
3. hâlâ yetersizse:

```text
precision_insufficient
```

Primary A-APP silently degraded edilemez.

---

# 13. Winner / equivalence / runner-up

Scientific winner source:

```text
A-APP only
```

Allowed terminal outcomes:

- unique winner
- exact/co-winner
- practical-equivalence top set
- precision-insufficient
- coverage-limited

Forced winner:

```text
forbidden = true
```

Historical Ward+CH:

```text
role = "historical_incumbent_comparator"
scientific_tie_break_privilege = false
operational_tie_break_privilege = false
```

Runner-up always reported:
- primary score;
- paired difference;
- MCSE / paired CI;
- k-specific performance;
- major failure strata;
- SSA deployment `k_hat` if applicable.

Scientific equivalence set:
- operational policy tarafından “unique winner” diye yeniden adlandırılamaz.

---

# 14. Operational deployment tie-break

Yalnız tek pipeline operationally required ise aktive edilir.

```text
scientific_winner_rule != operational_deployment_policy
legacy_neutral = true
outcome_blind_policy_definition = true
```

Exact operational policy:
- F11'de gerçek deployment need ve ölçülebilir constraints biliniyorsa pinlenir;
- F12'de ratify edilir.

Binding principle:
- external/exogenous operational criteria.

Eligible examples:
1. hard runtime/resource ceiling;
2. memory ceiling;
3. dependency/licensing constraint;
4. reproducibility/platform constraint;
5. pre-measured neutral operating cost;
6. substantive distinction kalmazsa deterministic neutral fallback.

`method-class simplicity`:
- tek başına tie-break değildir;
- yalnız measurable implementation burden'a dönüştürülmüşse kullanılabilir.

Incumbent continuity istenirse:

```text
policy_type = "non_scientific_stakeholder_continuity"
```

olarak etiketlenir.

Bu policy:
- scientific winner/equivalence'i değiştiremez.

---

# 15. Transfer

Default:

```text
TRANSFER-QUAL
```

States:
- qualified
- qualified_with_caveats
- failed

Evidence:
- R-REALISTIC
- E-BRIDGE
- CAL-SENS
- genuine held-out/external evidence if available

Separate transfer estimand/DGP block yalnız:

```text
distinct_transfer_source_or_law = true
```

ise açılır.

Same `B* × H*` law'u farklı isimle A_TRANSFER olarak kopyalamak:

```text
forbidden = true
```

Transfer qualification:
- A-APP scientific winner'ı değiştiremez;
- deployment claim'i daraltabilir/veto edebilir.

---

# 16. Bridge taxonomy

Normative umbrella:

```text
E-BRIDGE
```

Subpanels:

```text
E-BRIDGE
  ├── E-ACTUAL
  └── E-MATCHED
```

- `E-ACTUAL` = actual-support / real-derived semi-synthetic bridge.
- `E-MATCHED` = common-support matched bridge.

Bunlar:
- independent external validation değildir;
- winner-defining değildir.

Yeni DGP block proposal mandatory question:

> Hangi bilimsel soru mevcut block veya sensitivity paneliyle yanıtlanamaz?

Yanıt yoksa:

```text
new_block = rejected
```

---

# 17. Historical C_NPER / new-project n_per

Historical provenance:

- frozen old `run_matrix_v4.csv` C block row-level record:
  - `n_per_cluster=10` in 12/12 relevant rows.

Bu:
- old-project provenance fact'tir;
- new project design value değildir.

Doğru historical characterization:
- Kimi v8-r2 `C_NPER_STATUS` taşıma-yanlısıydı ve kendi içinde bu konuda tutarlıydı;
- sonradan doğrulanan row-level artifact evidence'ı görmediği için bilgi-gecikmeli konumdaydı;
- “kendi hükmüyle manifesti çelişiyordu” karakterizasyonu kullanılmaz.

New project:

```text
class_size_policy = "equal"
inherit_old_n_per = false
n_per_cluster = independently_frozen_new_project_parameter
```

New manifest:

```text
C_NPER_STATUS = forbidden
```

---

# 18. Friedman / secondary registry

Default secondary set:

```text
frozen_v53_friedman_formulations = [
    "sil_euc",
    "DB",
    "CH",
    "Dunn_d1_D1"
]
```

`sil_cos`:

```text
exploratory_relative_to_frozen_set = true
```

Friedman/Nemenyi:

```text
primary_winner_statistic = false
```

Amendment only if all six hold:

1. before any relevant outcome reading;
2. signed deviation record;
3. genuinely new and material scientific reason;
4. exact added/removed formulation specified;
5. multiplicity/reporting consequences frozen;
6. no motivation from observed pipeline ranking.

Budget alone:

```text
valid_amendment_reason = false
```

---

# 19. Venue

```text
venue_is_methodology_gate = false
venue_status = "administrative_metadata"
```

Specific journal name:
- methodology contract'a hard-code edilmez;
- unresolved bırakılabilir;
- manuscript administration aşamasında ayrıca kaydedilebilir.

Venue:
- DGP'yi değiştiremez;
- estimand'ı değiştiremez;
- k support'u değiştiremez;
- winner rule'u değiştiremez;
- noise law'u değiştiremez;
- morphology/generator kararını değiştiremez.

EPJ-DS vs JoC gibi venue netleştirmesi:

```text
methodology_freeze_blocker = false
```

---

# 20. Panel provenance residuals

Bit-identical / identity-defective panel artifact:

```text
independent_evidence_score = N-A
```

attribution çözülene kadar.

Unresolved non-material panel identity:
- methodology freeze blocker değildir.

Panel-history:
- normative science contract gövdesinde kullanılmaz;
- provenance ledger/appendix'e gider.

Another LLM consensus:
- empirical evidence değildir;
- reopen trigger değildir.

---

# 21. Block architecture

| Block / panel | Role | Winner? |
|---|---|---:|
| **A-APP** | frozen `B*×H*`, all-k exact-k primary | **YES** |
| A-MECH | matched hard-pair mechanism | No |
| A-RESPONSE / X-CANON | canonical response surface | No |
| **E-BRIDGE** | bridge umbrella | No |
| ↳ E-ACTUAL | actual-support real-derived bridge | No |
| ↳ E-MATCHED | common-support matched bridge | No |
| R-REALISTIC | robustness perturbations | No |
| TRANSFER-QUAL | deployment qualification gate | No |
| X-LEGACY-HIST | historical frozen comparator/reference | No |
| S-NEG | negative controls | No |
| R-REV | gated revival/multi-wave | No |
| H0-XREF | prior null-work cross-reference | No |
| BANK-SENS-S | scenario-bank sensitivity | No |
| BANK-SENS-L | source-influence sensitivity | No |
| CAL-SENS | calibration sensitivity | No |
| E-WEIGHT | design-weight sensitivity | No |

---

# 22. FINAL freeze sequence

| Gate | Freeze object | Failure behavior |
|---|---|---|
| **F0** | project identity, question, old/new boundary, estimand, k/sex scope, historical comparator role, precedence/provenance ledger | material design-relevant provenance contradiction → STOP/reconcile |
| **F1** | raw hashes, eligibility, time axis, preprocessing, z-normalization | unresolved → calibration cannot freeze |
| **F2** | WC-ADL/TAD equations, bounds, init, fit-failure rules | incomplete → STOP |
| **F3** | cross-fit adequacy thresholds + generator tie-break | both primary candidates fail → STOP/redesign |
| **F4** | final-refit rule, parameter banks, source IDs, descriptors, label_fuzz | unstable/unsupported → no B* |
| **F5** | Q_CD composition/distinctness/accept-reject/weights + `class_size_policy="equal"` + new-project `n_per_cluster` numeric pin | ambiguous/collapse → revise or STOP |
| **F6** | frozen B*: size, IDs, weights, source-incidence metadata, hashes, coverage | incomplete → no run |
| **F7** | signed geometry, strata, natural hard pair, matched feasibility, epsilon/delta | secondary infeasible → coverage_gap |
| **F8** | H*, empirical dependence representation, canonical response, robustness/transfer law | unsupported → no A-APP freeze |
| **F9** | algorithm/CVI registry, candidate k=2–10, tie/failure/nonfinite policy, software/environment hashes, frozen four formulations | ambiguity → no run |
| **F10** | Delta_eq, precision target, CRN, scenario/seed allocation, compute budget | inadequate → narrow secondary / optimize / precision_insufficient |
| **F11** | **exact BANK-SENS-S/L methods + applicability/fallback**, manifest/QC, estimator, variance, equivalence, operational deployment policy if actually required | incomplete → no outcome reading |
| **F12** | **ratification only:** final analysis/reporting contract, full-text consistency review, explicit PI sign-off, external hash sidecar | unsigned → draft only |

Norm:

```text
F11 = methodological/analysis implementation pin
F12 = final ratification/sign-off
```

No method may first be chosen at F12.

**F12 kapanmadan algorithm × CVI outcome okunmaz.**

Staged execution:
```text
allowed = true
```

Staged outcome reading:
```text
allowed = false
```

Accidental early result exposure:
- provenance violation loglanır;
- confirmatory design'i değiştiremez;
- affected chain silently “pristine preregistered” diye sunulamaz.

---

# 23. Manifest — required canonical fields

## 23.1 Provenance

- `project_id`
- `design_version`
- source/input/code/registry/environment/parent hashes
- `panel_source_ledger_hash`
- `methodology_contract_status`

## 23.2 Design / scope

- `question_id`
- `design_block`
- `claim_scope`
- `winner_layer`
- `stage`
- `calibration_sex`
- `k_true`
- `class_size_policy`
- `n_per_cluster`
- `class_sizes`
- `composition_id`

Norm:

```text
class_size_policy = "equal"
```

Forbidden:

```text
C_NPER_STATUS
```

## 23.3 Bank / design measure

- `parameter_bank_id`
- `parameter_bank_hash`
- `q_cd_rule_id`
- `q_cd_rule_hash`
- `bank_id`
- `bank_hash`
- `scenario_id`
- `scenario_source_ids`
- `resampling_rule_id`
- `weight_source`
- `weight_hash`
- `weight_semantics`
- `latent_probability_claim`

Norms:

```text
weight_semantics = "design_weight"
latent_probability_claim = false
```

## 23.4 Morphology / geometry

- generator family/version/hash
- shape family/regime/subtype
- `prototype_instance_id`
- `prototype_instance_hash`
- observed descriptors
- `label_fuzz`
- signed rho fields
- `d_eff`
- Gram spectrum
- `hardpair_code`
- `epsilon`
- `delta`
- `unexpected_nearest_pair`
- `envelope_status`
- `coverage_gap_reason`

## 23.5 Noise / randomness

- sigma
- sigma source
- noise type
- phi
- phi source
- seed namespace/key
- CRN id

## 23.6 Outcomes

- `k_hat`
- `correct`
- `bias`
- `k_hat_tie`
- `cvi_failure`
- `algorithm_failure`
- `converged`

## 23.7 Uncertainty / sensitivity

- `mcse`
- `bank_sens_s_method`
- `bank_sens_s_status`
- `bank_sens_l_method`
- `bank_sens_l_applicability_status`
- `bank_sens_l_not_applicable_reason`
- `bank_sens_l_source_count`
- `calibration_sensitivity_role`

## 23.8 Transfer / operational

- `distinct_transfer_source_or_law`
- `historical_tie_break_privilege`
- `operational_tie_break_policy_id`
- `operational_tie_break_scientific`
- `venue_status`
- `venue_is_methodology_gate`

Norms:

```text
historical_tie_break_privilege = false
operational_tie_break_scientific = false
venue_is_methodology_gate = false
```

## 23.9 Secondary registry

```text
frozen_v53_friedman_formulations
```

canonical value:

```text
["sil_euc","DB","CH","Dunn_d1_D1"]
```

---

# 24. Mandatory QC

1. provenance hashes complete;
2. old frozen artifacts unchanged;
3. no unverified third-party numeric claim labeled verified;
4. duplicate panel artifacts not counted independently;
5. historical C_NPER attribution correction retained;
6. `class_size_policy="equal"` in A-APP;
7. new-project numeric `n_per_cluster` frozen at F5;
8. old `n_per=10` not automatically inherited;
9. no `C_NPER_STATUS`;
10. no old `(shape,location)` truth carry-over;
11. no automatic phi snap;
12. signed rho definitions used;
13. max-absolute rho not substituted;
14. B* acceptance/rejection rates logged;
15. design weights sum correctly;
16. `weight_semantics="design_weight"`;
17. `latent_probability_claim=false`;
18. BANK-SENS-S class present;
19. BANK-SENS-S exact method pinned at F11;
20. delta-method not silently treated as mandatory unless explicitly frozen;
21. BANK-SENS-L class present;
22. BANK-SENS-L incidence applicability QC completed;
23. `zero_new_runs` not used as sole validity claim;
24. BANK-SENS-L fallback frozen if incidence method not applicable;
25. no mandatory sensitivity class silently skipped;
26. sensitivity layers winner-ineligible;
27. sensitivity intervals not called target-population CIs;
28. CRN pairing valid;
29. no seed-level hypothesis testing;
30. Delta_eq precedes precision/budget;
31. budget does not alter Delta_eq;
32. runner-up report fields complete;
33. Ward+CH no scientific automatic privilege;
34. Ward+CH no operational automatic privilege;
35. operational policy separately labeled if present;
36. transfer gate cannot change scientific winner;
37. `distinct_transfer_source_or_law` canonical field used;
38. no duplicate A_TRANSFER with same law;
39. E-BRIDGE umbrella used for E-ACTUAL/E-MATCHED;
40. venue non-gating;
41. no specific venue hard-coded as methodology requirement;
42. frozen four Friedman formulations correct;
43. amendment has six required conditions if used;
44. exact sensitivity implementation pinned at F11, not first chosen at F12;
45. F12 full-text consistency review completed;
46. F12 explicit PI sign-off present;
47. no outcome reading before F12;
48. reopening trigger, if invoked, has evidence class;
49. unresolved non-material panel provenance does not become design blocker;
50. every new DGP block passes the unanswered-scientific-question test.

---

# 25. Explicit rejected rules

Forbidden/rejected:

1. rewrite old frozen project;
2. treat old Ward+CH as new scientific prior/winner;
3. use Ward+CH as automatic scientific tie-break;
4. use Ward+CH as automatic operational tie-break;
5. use `max|rho|` as primary geometry;
6. treat rho historical bands as target-probability law;
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
20. `zero new runs ⇒ statistical validity`;
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

---

# 26. Calibration-only open items

Bunlar yeni metodoloji oylaması değil, ölçüm ve implementation pinleridir:

1. WC-ADL exact formula/bounds/init/failure handling;
2. TAD/PSAT exact formula/bounds/init/failure handling;
3. adequacy thresholds;
4. generator tie-break exact rule;
5. cross-fit scheme;
6. descriptor thresholds;
7. label_fuzz rule;
8. full-data final refit rule;
9. Q_CD whole-vector sampling/composition;
10. distinctness/acceptance thresholds;
11. B* size;
12. design weights;
13. coverage guard;
14. **new-project numeric n_per_cluster**;
15. geometry strata;
16. epsilon/delta;
17. H* sigma strata;
18. empirical temporal-dependence representation;
19. white-noise ceiling diagnostic;
20. Delta_eq numeric justification;
21. paired precision target;
22. scenario/seed allocation;
23. CRN seed namespace;
24. BANK-SENS-S exact implementation;
25. BANK-SENS-L applicability audit + exact implementation/fallback;
26. transfer qualification thresholds;
27. R-REV eligibility gate;
28. operational deployment policy only if a single pipeline is truly required;
29. software/environment hashes;
30. executable manifest QC;
31. final report language;
32. explicit F12 sign-off.

Venue choice:
- bu listeye metodolojik calibration pin olarak girmez.

Unresolved old panel identity:
- design-relevant contradiction yaratmadıkça blocker değildir.

---

# 27. Reopening policy

Lifecycle:

```text
draft
-> calibration_pins_complete
-> manifest_analysis_contract_complete
-> explicit_signoff
-> frozen
```

After `frozen`, reopening only if:

1. calibration materially falsifies a frozen design assumption;
2. provenance/source audit reveals a **material design-relevant contradiction**;
3. genuinely new objection class appears.

Not reopening triggers:

- another LLM gives a different score;
- another LLM rewrites same objection;
- model consensus changes;
- historical Ward+CH is absent from top results;
- venue changes;
- secondary ranking differs;
- unresolved non-material panel identity remains unresolved;
- wording/granularity difference between prior v11 artifacts.

---

# 28. Claude Code execution contract

Claude Code must:

1. treat this file as the sole normative methodology source;
2. keep old v5.3 project read-only;
3. not reopen closed design decisions;
4. create `yeni_proje_empirik_kalibrasyon_protokolu_v0.md` as the next normative working artifact;
5. perform only calibration/pre-freeze measurements in that protocol;
6. not generate/read algorithm × CVI performance outcomes before F12;
7. log every pin with source, rationale, version/hash where applicable;
8. preserve explicit STOP behavior;
9. distinguish measurement-derived pins from historical references;
10. produce manifest/QC fields in canonical names from this file.

If Claude Code finds a discrepancy between this file and an older terminal document:

```text
this_FINAL_NORMATIVE_file_wins = true
```

unless the discrepancy satisfies an explicit reopening trigger.

---

# 29. Terminal methodology statement

> This benchmark is a separate preregistered SSA application-calibrated clustering study. Its primary scientific target is design-weighted exact recovery of `k_true` over an outcome-blind, pre-frozen finite `B*×H*` application design for `k={3,4,5,6,8}` and both sexes. `Q_CD` is the calibration-constrained construction/provenance law used to generate that bank and is not a latent SSA prototype-probability distribution. Primary morphology is WC-ALC; W-L/W-I/W-R are observed-window descriptors, while truth is defined by frozen distinct generator/prototype parameter instances. WC-ADL and TAD/PSAT are the only primary generator candidates and are selected through outcome-blind adequacy gates; double failure triggers redesign. Signed prototype geometry is recorded without using historical rho thresholds as design triggers. A-APP uses equal truth-cluster sizes, but the common numeric `n_per_cluster` is a new-project parameter pinned independently at F5 and is not inherited from the historical C block. The winner layer uses empirically calibrated clean residual-supported noise without automatic AR(.97) snapping; canonical sigma/AR(.97) conditions are winner-ineligible. Primary uncertainty is CRN-paired Monte Carlo uncertainty conditional on the frozen bank. BANK-SENS-S and BANK-SENS-L are mandatory winner-ineligible sensitivity classes; their exact procedures are pinned at F11 after calibration-structure checks, with incidence/delete-source jackknife as the preferred BANK-SENS-L candidate only when its applicability QC passes. `Delta_eq` is fixed from scientific relevance before outcomes and determines precision and compute requirements, never the reverse. No unique winner is forced. Historical Ward+CH has no automatic scientific or operational tie-break privilege. Transfer is a deployment-qualification gate unless a genuinely distinct transfer source or law defines a separate estimand. E-BRIDGE is the umbrella for E-ACTUAL and E-MATCHED bridge panels. Secondary Friedman/Nemenyi uses the frozen four formulations by default; any amendment requires a signed pre-outcome deviation supported by a genuinely new material scientific reason and the full six-condition amendment rule. Venue and unresolved non-material panel identity are non-gating metadata. F11 pins all analysis/sensitivity implementation choices; F12 only ratifies the completed contract through consistency review, PI sign-off and hash freeze. No algorithm×CVI outcome may be read before F12.

---

# 30. Final decision

**Methodology-panel phase: CLOSED.**

**GO:**

```text
yeni_proje_empirik_kalibrasyon_protokolu_v0.md
```

**NO-GO before F12:**

```text
algorithm × CVI performance outcome reading
```

Bu FINAL NORMATIVE dosya + explicit PI sign-off:

```text
p_konum_plus_decision_freeze_v0
```

için normatif temeldir.

