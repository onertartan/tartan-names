# SSA Application-Calibrated Clustering Benchmark
## ChatGPT v10 ve Claude v10-r2 Son Karşılaştırması ve Sentezlenmiş v11 Freeze-Candidate

**Sürüm:** v11  
**Tarih:** 2026-08-26  
**Statü:** FINAL METHODOLOGY SYNTHESIS / FREEZE-CANDIDATE — henüz imzalanmadı  
**Sonraki adım:** `yeni_proje_empirik_kalibrasyon_protokolu_v0.md`  
**Outcome firewall:** F12 imzası tamamlanmadan hiçbir algorithm × CVI performans sonucu okunmaz.

---

# 0. Bu turun kapsamı

Bu son sentez turunda yalnız iki güncel metodoloji artefaktı bilimsel karşılaştırma nesnesidir:

1. **ChatGPT v10**
   - `ssa_application_calibrated_benchmark_v10_sentez_2026-08-26.md`
   - SHA256: `e5963a94fb4ffd3fc9574a9ee8723495784e78c99936bce9e0144ddf75429f08`

2. **Claude v10-r2**
   - `claude_p_konum_plus_iki_v9_degerlendirme_ve_sentez_v10r2_2026-08-26.md`
   - SHA256: `23e1239803c7f24c3ab0bb685382eb139337e71e0a790c0b0379645d517dd143`

Önceki ChatGPT/Claude/Kimi/Manus/Qwen/Fugu artefaktları bu turda **oy** veya bağımsız panel kanıtı değildir. Yalnız provenance, source-fidelity ve karar-soyağacı gerektiğinde tarihsel kaynak görevi görür.

---

# 1. Nihai değerlendirme

## 1.1 Rubrik

| Ölçüt | Ağırlık |
|---|---:|
| Scientific construct / estimand validity | 2.00 |
| Inference / uncertainty / sensitivity | 2.00 |
| Governance / freeze / information firewall | 1.50 |
| Provenance / source fidelity | 1.50 |
| Executability / manifest / QC | 1.50 |
| Parsimony / internal consistency / legacy leakage | 1.00 |
| Closure readiness | 0.50 |
| **Toplam** | **10.00** |

## 1.2 Puanlar

| Sıra | Belge | Construct | Inference | Governance | Provenance | Execution | Parsimony | Closure | **Toplam** |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **1** | **ChatGPT v10** | 2.00 | 1.95 | 1.50 | 1.45 | 1.45 | 0.95 | 0.50 | **9.80** |
| **2** | **Claude v10-r2** | 2.00 | 1.90 | 1.50 | 1.50 | 1.40 | 0.90 | 0.50 | **9.70** |

**Yorum:** 0.10 puanlık fark bilimsel tasarım ayrılığı değildir. İki v10'un çekirdek tasarım uyumu yaklaşık **%99** düzeyindedir. Fark, sensitivity implementation governance, operational tie-break'in ne kadar erken spesifiye edileceği, venue/panel provenance kayıtlarının freeze'e bağlanıp bağlanmaması ve belge-parsimoni tercihidir.

---

# 2. ChatGPT v10 — 9.80/10

## Güçlü yönler

1. `B* × H*` finite scientific target ile `Q_CD` design-law ayrımı çok temizdir.
2. `BANK-SENS-L` için source-influence sınıfını zorunlu tutarken incidence-jackknife'a açık **applicability QC** koyar.
3. `zero_new_algorithm_runs` ile `statistical_applicability` kavramlarını birbirinden ayırır.
4. Ward+CH için hem scientific hem operational otomatik privilege'ı açıkça sıfırlar.
5. Operational tie-break'i yalnız gerçek deployment ihtiyacı varsa, exogenous ve legacy-neutral criteria ile açar; metodoloji sentezinde keyfî sabit hiyerarşi kurmaz.
6. Venue'yu tamamen non-gating administrative/reporting metadata olarak tutar.
7. Duplicate/identity-defective panel artefaktları için attribution çözülene kadar `independent_evidence_score=N-A` kuralı temizdir.
8. New-project `n_per_cluster` ile historical C_NPER'i açık biçimde ayırır; `C_NPER_STATUS` yeni manifeste girmez.
9. Manifestte BANK-SENS-L applicability ve fallback durumlarını machine-readable alanlara bağlar.
10. Freeze sequence failure-behavior tablosu execution'a doğrudan çevrilebilir.

## Eksikler

1. Zorunlu sensitivity sınıfının “uygun yöntem bulunamadı” gerekçesiyle sessizce düşürülemeyeceğini Claude kadar açık yazmıyordu.
2. Claude'un provenance ledger / yanlışlanabilirlik kayıt disiplini daha güçlüdür.
3. Kimi v8-r2 hakkındaki önceki ChatGPT-v9 `C_NPER` iç-çelişki karakterizasyonunun hatalı olduğu v10 metninde açık attribution-correction satırı olarak kapatılmamıştı.
4. `E-BRIDGE` tek şemsiye adı execution düzeyinde Claude'un `E-ACTUAL/E-MATCHED` ayrımından daha az granülerdir.

---

# 3. Claude v10-r2 — 9.70/10

## Güçlü yönler

1. Önceki ana farkı doğru biçimde kapatır:
   - BANK-SENS-S ve BANK-SENS-L **sınıfları** zorunlu,
   - exact implementation calibration/preflight sonrasında pinlenir.
2. Incidence-jackknife'ın yalnız deletion counterfactual ölçtüğünü ve banka yapısına bağlı dejenere olabileceğini açıkça kabul ederek önceki “tanım gereği fizibil” hükmünü geri çeker.
3. `Delta_eq` için budget-alone amendment istisnasını kapatır.
4. Runner-up koşulsuz raporlamayı açık normative kural yapar.
5. Her yeni DGP bloğu için parsimony sorusu getirir:
   > Hangi bilimsel soru mevcut blok/panelle yanıtlanamaz?
6. Provenance/source audit en güçlü katmandır.
7. Kimi v8-r2 source audit ile önceki ChatGPT-v9 T-2 karakterizasyon hatasını doğru biçimde saptar.
8. No-silent-skip koruması sensitivity coverage için değerlidir.
9. Freeze/reopening governance son derece olgundur.

## Kalan küçük kusurlar

1. Operational tie-break için önerdiği aday sıra:
   - measured compute cost
   - method-class simplicity
   - deterministic order / seeded draw

   bilimsel çatışma yaratmasa da `method-class simplicity` operasyonel olarak yeterince nesnel değildir ve exact hierarchy deployment ihtiyacı oluşmadan pinlenmemelidir.

2. Venue ana metinde non-gating F0-admin metadata olmasına rağmen açık-kalem/terminal kapanış kısmında hâlâ venue netleştirmesi imza-öncesi iş gibi görünür. Bu, kendi non-gating hükmüyle gereksiz coupling yaratır.

3. P-3 panel identity kaydının unresolved kalması bilimsel estimand veya execution contract'ı etkilemiyorsa methodology freeze'i bloke etmemelidir.

4. `E-ACTUAL/E-MATCHED` ayrımı yararlıdır, fakat bunlar ayrı yeni DGP aileleri gibi değil `E-BRIDGE` şemsiyesi altında alt-paneller olarak tutulursa parsimony daha temiz olur.

5. Panel-history ve öz-değerlendirme makinesi güçlü provenance sağlar; fakat final normative methodology document içinde fazla yer kaplaması science contract'ı gereksiz büyütebilir. v11'de bunlar provenance ledger'a ayrılır.

---

# 4. Source-fidelity düzeltmesi — C_NPER / Kimi v8-r2

v11 aşağıdaki tarihsel karakterizasyonu bağlayıcı provenance notu olarak kabul eder:

**Yanlış karakterizasyon:**
> Kimi v8-r2, “C_NPER yeni projeye taşınmamalı” derken kendi manifestinde taşıdığı için iç-çelişkilidir.

**Doğru karakterizasyon:**
> Kimi v8-r2, `C_NPER_STATUS` taşıma-yanlısı ve kendi içinde bu konuda tutarlıdır; fakat frozen `run_matrix_v4.csv` üzerindeki daha sonra doğrulanan 12/12 row-level `n_per_cluster=10` kanıtını görmediği için bilgi-gecikmeli bir konum taşır.

Sonuç:
- source-fidelity düzeltmesi yapılır;
- design decision değişmez;
- historical old-project C_NPER provenance ledger'da tutulur;
- new project yine kendi `n_per_cluster` değerini bağımsız freeze eder;
- `C_NPER_STATUS` yeni projecte taşınmaz.

---

# 5. İki v10 arasında artık kapalı olan bilimsel kararlar

Aşağıdaki konularda substantive disagreement **yoktur**:

1. project = old frozen benchmarktan ayrı yeni çalışma;
2. primary target = frozen finite application design;
3. `Q_CD` latent probability law değildir;
4. `B* × H*` primary scientific target;
5. `k={3,4,5,6,8}`, all-k;
6. k=5 winner privilege yok;
7. WC-ALC primary morphology;
8. W-L/W-I/W-R = descriptor regimes, truth classes değil;
9. truth identity = frozen distinct prototype/generator instance;
10. old `(shape,location)` ontology automatic carry-over yok;
11. WC-ADL ve TAD/PSAT tek primary generator candidates;
12. spline automatic primary fallback değil;
13. double generator failure = STOP/redesign;
14. signed Pearson `rho_max`;
15. historical rho dead-zone = context only;
16. empirical residual-supported clean noise winner layer;
17. automatic `.97` phi snap yok;
18. canonical sigma/AR(.97) block winner-ineligible;
19. A-APP natural hard pair only;
20. A-MECH matched/counterbalanced mechanism panel;
21. primary uncertainty = conditional paired MC;
22. seeds = MC realizations;
23. no seed-level hypothesis testing;
24. BANK-SENS-S mandatory winner-ineligible sensitivity class;
25. BANK-SENS-L mandatory winner-ineligible source-influence class;
26. sensitivity classes primary CI değildir;
27. `Delta_eq -> precision -> allocation -> budget`;
28. budget alone cannot enlarge Delta_eq;
29. no forced unique winner;
30. Ward+CH historical comparator only;
31. no automatic Ward scientific tie-break;
32. no automatic Ward operational tie-break;
33. runner-up always reported;
34. transfer default = qualification gate;
35. separate transfer DGP only distinct source/law exists;
36. historical C_NPER does not define new-project n_per;
37. no `C_NPER_STATUS` in new manifest;
38. frozen four Friedman formulations default;
39. Friedman/Nemenyi primary winner statistic değil;
40. pre-outcome signed amendment requires genuinely new material scientific reason;
41. venue methodology gate değil;
42. no algorithm×CVI outcome before full freeze/sign-off;
43. explicit reopening triggers only.

Bu nedenle v11 bir “yeni tasarım” değildir; iki v10'un kalan governance/granularity farklarını kapatan terminal synthesis'tir.

---

# 6. v11 yeni/rafine kararları

## V11-R1 — Mandatory sensitivity class, calibrated implementation

Her iki sınıf zorunludur:

```text
BANK-SENS-S.required = true
BANK-SENS-L.required = true
winner_eligible = false
primary_CI = false
```

Exact estimator **bank/calibration structure görülmeden normatif olarak tek yönteme kilitlenmez**.

### BANK-SENS-S

Preferred first-line candidate:

```text
scenario_id_cluster_bootstrap
```

CRN/pairing/strata korunur.

Delta-method veya deterministic alternative-bank comparison:
- cross-check / supplementary candidate.

Exact method F11'de pinlenir.

### BANK-SENS-L

Preferred first-line candidate:

```text
incidence_delete_source_jackknife
```

yalnız applicability QC geçerse.

Applicability QC:

1. `scenario_source_ids` complete/deterministic;
2. required `(sex,k)` support delete-source sonrası anlamlı kalıyor;
3. weight renormalization finite/well-defined;
4. deletion estimand support'u mekanik olarak yok etmiyor;
5. source incidence required stratumda universal değil;
6. dependency/duplication structure documented;
7. deletion counterfactual bilimsel olarak yorumlanabilir.

Fail:

```text
bank_sens_l_incidence_status = "not_applicable"
```

ve pre-frozen alternative source-influence method seçilir:

- calibration-stage bank rebuild/subset jackknife;
- grouped source deletion;
- alternative frozen-bank/source influence design.

**No-silent-skip protection:**

Zorunlu sensitivity sınıfı sessizce düşürülemez.

Eğer hiçbir yorumlanabilir implementasyon bulunamazsa:

```text
sensitivity_class_status = "unresolved"
methodology_freeze_status = "STOP"
```

ve gerekçe imzalı provenance kaydıyla görünür tutulur.

---

## V11-R2 — Operational deployment tie-break

Yalnız tek pipeline deployment açısından gerçekten gerekiyorsa açılır.

Rules:

```text
scientific_winner_rule != operational_deployment_policy
legacy_neutral = true
outcome_blind_policy_definition = true
```

Tie-break exact hierarchy F0'da otomatik hard-code edilmez.

F11/F12'de gerçek deployment requirement biliniyorsa şu sıra kullanılır:

1. **hard exogenous constraints**
   - runtime ceiling
   - memory/resource ceiling
   - dependency/licensing
   - reproducibility/platform requirement

2. **pre-measured neutral operating cost**
   - calibration-stage compute/runtime/resource measurements

3. **deterministic neutral fallback**
   - yalnız substantive operational distinction yoksa.

`method-class simplicity` tek başına tie-break değildir; yalnız ölçülebilir implementation burden'a dönüştürülmüşse kullanılabilir.

Incumbent continuity istenirse:

```text
policy_type = "non_scientific_stakeholder_continuity"
```

olarak etiketlenir ve scientific equivalence set'i değiştiremez.

---

## V11-R3 — Bridge taxonomy

Parsimony + granularity birlikte korunur:

```text
E-BRIDGE
  ├── E-ACTUAL
  └── E-MATCHED
```

- `E-BRIDGE` = umbrella scientific role.
- `E-ACTUAL` = real-derived/semi-synthetic actual-support bridge.
- `E-MATCHED` = common-support matched bridge.

Bunlar independent external validation değildir.

Yeni ayrı DGP bloğu önerisi için mandatory test:

> Hangi bilimsel soru mevcut blok veya sensitivity paneliyle yanıtlanamaz?

Yanıt yoksa yeni blok açılmaz.

---

## V11-R4 — Venue

```text
venue_is_methodology_gate = false
venue_status = "administrative_metadata"
```

Current venue conflict / uncertainty scientific freeze blocker değildir.

Venue:
- boş veya unresolved bırakılabilir;
- kullanıcı daha sonra manuscript administration için kaydedebilir;
- DGP/estimand/winner/noise/k/morphology değiştiremez.

Dolayısıyla:
- “EPJ-DS mi JoC mu?” netleştirmesi v11 methodology sign-off için prerequisite değildir.

---

## V11-R5 — Panel provenance residuals

Bit-identical / identity-defective artefact:

```text
independent_evidence_score = N-A
```

attribution çözülene kadar.

Unresolved panel identity:
- design-relevant material contradiction oluşturmuyorsa
- methodology freeze blocker değildir.

Panel history:
- normative methodology gövdesine değil,
- provenance ledger / appendix'e taşınır.

---

# 7. v11 primary estimand

For sex `s ∈ {M,F}` and `k ∈ {3,4,5,6,8}`:

```text
Q_CD(k,s)
```

= calibration-constrained joint-set construction/design law.

```text
B*_{k,s}
```

= outcome-before frozen finite scenario bank.

```text
H*_s
```

= outcome-before frozen empirical clean residual-supported noise bank.

Primary pipeline score:

```text
A_m(k,s)
  = Σ_b Σ_h w_b u_h P_MC(k_hat_m = k | b,h)
```

Macro:

```text
A_m^APP
  = (1/2) Σ_s (1/5) Σ_k A_m(k,s)
```

Finite estimator:

```text
Â_m
  = Σ_c ω_c (1/S_c) Σ_r I{k_hat_mcr = k_true,c}
```

Machine-readable:

```text
weight_semantics = "design_weight"
latent_probability_claim = false
```

Allowed claim:

> performance across the frozen calibration-constrained application design

Forbidden claim:

> performance under the true latent SSA prototype distribution

---

# 8. k governance

```text
K = {3,4,5,6,8}
v_k = 1/5
```

If macro sex pooling frozen:

```text
v_M = 1/2
v_F = 1/2
```

Mandatory:
- sex-specific results;
- k-specific results.

k=5:

```text
winner_privilege = false
```

`k_hat = k±1`:
- secondary partial-credit sensitivity only.

---

# 9. Morphology and truth identity

Primary:

```text
WC-ALC
```

Observed-window regimes:
- W-L
- W-I
- W-R

Optional W-I descriptors:
- early
- mid
- late

Regime:
```text
role = descriptor
```

Truth cluster identity:

```text
frozen distinct generator/prototype parameter instance
```

Old benchmark identity:

```text
(shape, location)
automatic_carryover = false
```

Primary exclusions:
- level_shift
- cylinder
- impulse
- abrupt structures

Role:
```text
S-NEG
```

Revival/multi-wave:
```text
R-REV
```
only if pre-frozen empirical eligibility gate passes.

DTW/elastic alignment:
```text
closed = true
```

---

# 10. Generator firewall

Primary candidate set:

1. WC-ADL
2. TAD/PSAT

Shape-constrained low-df spline:

```text
role = adequacy_benchmark
automatic_primary_fallback = false
```

Outcome-blind lexicographic adequacy order:

1. morphology coverage;
2. cross-fitted reconstruction/predictive fit;
3. residual morphology/structure;
4. censored-case identifiability;
5. parameter stability;
6. parsimony.

Tie-break:
- frozen before outcome;
- exact rule in calibration protocol.

Both candidates fail:

```text
STOP / redesign
```

After family/form/rules frozen:
- selected generator may be final-refit on all eligible calibration trajectories;
- provenance logged;
- final refit cannot reopen generator-family choice.

---

# 11. Geometry

Primary:

```text
rho_max = max_{i<j} corr(P_i,P_j)
```

signed Pearson.

Required:
- rho_max_pair
- rho_mean
- rho_min
- theta_min
- d_eff
- Gram spectrum
- hardpair_code
- envelope_status
- coverage_gap_reason
- unexpected_nearest_pair

Forbidden primary substitute:

```text
max_abs_rho
```

rho:
- geometry descriptor;
- reporting variable;
- MC-efficiency stratum;
- not target probability factor.

Historical dead-zone:
```text
historical_context_only = true
```

Natural easy domain:
- ceiling/equivalence finding.

Infeasible geometry:
- `coverage_gap`,
- no artificial filler.

---

# 12. Noise

## A-APP winner layer

```text
B* × H*
```

H*:
- empirical residual scale strata;
- empirical temporal dependence representation;
- common within-cell clean scale convention;
- equal class size if explicitly frozen.

A-APP excludes:
- morphology-specific sigma;
- jitter;
- imbalance;
- outliers;
- morphology-noise coupling;
- signal-scale robustness perturbation.

Empirical phi:

```text
phi_primary = measured/calibrated representation
```

Automatic:
```text
phi_emp -> 0.97
```
is forbidden.

Any discretization:
- empirical calibration justified;
- outcome-blind;
- frozen before run.

## A-RESPONSE / X-CANON

```text
sigma = 0.1 ... 1.0
noise = {white, AR(.97)}
winner_eligible = false
application_probability = none
```

---

# 13. Hard-pair

A-APP:
- natural hard pair recorded;
- no counterbalancing.

A-MECH:
- matched/counterbalanced common-support mechanism.

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

epsilon/delta:
- feasibility-after;
- outcome-before freeze.

W-L × W-R:
```text
BB-OPP
role = diagnostic_only
```

---

# 14. Primary uncertainty

Seeds:

```text
role = Monte_Carlo_realization
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

BANK-SENS-S/L:
- robustness/influence layers;
- winner-ineligible;
- not target-population CIs.

---

# 15. Delta_eq / precision / budget

Strict direction:

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
- not budget-adaptive.

100 seeds:
- neither automatically adequate nor automatically inadequate.

Mandatory precision preflight:
- analytic worst-case bounds;
- actual frozen weights;
- paired disagreement structure;
- outcome-blind simulation if needed.

Budget insufficient:

1. narrow secondary scope;
2. optimize primary allocation;
3. if still insufficient:
   ```text
   precision_insufficient
   ```

No forced winner.

---

# 16. Winner / equivalence / runner-up

Scientific winner source:

```text
A-APP only
```

Allowed terminal scientific states:
- unique winner;
- exact/co-winner;
- practical-equivalence top set;
- precision-insufficient;
- coverage-limited.

Historical Ward+CH:

```text
role = historical_incumbent_comparator
scientific_tie_break_privilege = false
operational_tie_break_privilege = false
```

Runner-up mandatory:
- score;
- paired difference;
- MCSE / paired CI;
- k-specific performance;
- important failure strata;
- SSA deployment `k_hat` if applicable.

Scientific equivalence set cannot be renamed unique winner by operational policy.

---

# 17. Transfer

Default:

```text
TRANSFER-QUAL
```

States:
- qualified
- qualified_with_caveats
- failed

Evidence:
- R-REALISTIC;
- E-BRIDGE/E-ACTUAL/E-MATCHED;
- CAL-SENS;
- genuine external/held-out evidence if available.

Separate transfer DGP only if:

```text
distinct_transfer_source_or_law = true
```

Same `B* × H*` law duplicated as A_TRANSFER:
```text
RED
```

Transfer qualification:
- cannot change A-APP scientific winner;
- may restrict deployment claim.

---

# 18. Historical C_NPER / new n_per

Historical old project:
- row-level frozen record belongs to provenance ledger;
- old C block may be documented as historical `n_per_cluster=10`.

New project:

```text
inherit_old_n_per = false
```

If class size used:

```text
n_per_cluster = independently_frozen_new_project_parameter
```

New manifest:

```text
C_NPER_STATUS = forbidden
```

---

# 19. Friedman / secondary registry

Default:

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

Amendment only if all:
1. before relevant outcome read;
2. signed deviation;
3. independent, genuinely new, material scientific reason;
4. exact formulation change stated;
5. multiplicity/reporting implications frozen;
6. not motivated by observed ranking.

Budget alone:
```text
valid_amendment_reason = false
```

---

# 20. Block architecture

| Block / panel | Role | Winner? |
|---|---|---:|
| **A-APP** | frozen `B*×H*`, all-k primary exact-k | **YES** |
| A-MECH | matched hard-pair mechanism | No |
| A-RESPONSE / X-CANON | canonical response surface | No |
| **E-BRIDGE** | bridge umbrella | No |
| ↳ E-ACTUAL | actual-support real-derived bridge | No |
| ↳ E-MATCHED | common-support matched bridge | No |
| R-REALISTIC | robustness perturbations | No |
| TRANSFER-QUAL | deployment qualification gate | No |
| X-LEGACY-HIST | old frozen comparator/reference | No |
| S-NEG | negative controls | No |
| R-REV | gated revival | No |
| H0-XREF | prior null-work cross-reference | No |
| BANK-SENS-S | scenario-bank sensitivity | No |
| BANK-SENS-L | source-influence sensitivity | No |
| CAL-SENS | calibration sensitivity | No |
| E-WEIGHT | design-weight sensitivity | No |

New block admissibility question:

> Hangi bilimsel soru mevcut blok veya sensitivity paneliyle yanıtlanamaz?

No answer:
```text
new_block = rejected
```

---

# 21. Freeze sequence — final

| Gate | Freeze object | Failure behavior |
|---|---|---|
| **F0** | project identity, question, old/new boundary, estimand, k/sex scope, historical comparator role, provenance ledger | material design provenance contradiction -> STOP/reconcile |
| **F1** | raw hashes, eligibility, time axis, preprocessing, z-norm, new n_per if used | unresolved -> calibration cannot freeze |
| **F2** | WC-ADL/TAD definitions, bounds, init, fit-failure rules | incomplete -> STOP |
| **F3** | cross-fit adequacy thresholds + generator tie-break | both fail -> STOP/redesign |
| **F4** | final-refit rule, parameter banks, source IDs, descriptors, label_fuzz | unstable support -> no B* |
| **F5** | Q_CD composition/distinctness/accept/reject/weights | ambiguous/collapse -> revise or STOP |
| **F6** | frozen B*: size, IDs, weights, source incidence, hashes, coverage | incomplete -> no run |
| **F7** | signed geometry, strata, natural hard pair, matched feasibility, epsilon/delta | secondary infeasible -> coverage_gap |
| **F8** | H*, empirical dependence, canonical response, robustness/transfer law | unsupported -> no A-APP freeze |
| **F9** | algorithm/CVI registry, candidate k=2–10, failure/tie/nonfinite policy, software/environment hashes, frozen four formulations | ambiguity -> no run |
| **F10** | Delta_eq, precision target, CRN, scenario/seed allocation, budget | inadequate -> secondary narrowing / allocation optimization / precision_insufficient |
| **F11** | BANK-SENS-S/L exact methods + applicability; manifest/QC; estimator; variance; equivalence; operational policy if required | incomplete -> no outcome reading |
| **F12** | final analysis/reporting contract + explicit PI sign-off + external hash sidecar | unsigned -> draft only |

**F12 kapanmadan algorithm × CVI outcome okunmaz.**

Staged execution:
- allowed.

Staged result reading:
- forbidden.

Accidental early reading:
- provenance violation logged;
- cannot alter confirmatory design;
- affected chain cannot be silently treated as pristine preregistration.

---

# 22. Final manifest additions / standardization

Required core additions:

```text
weight_semantics = "design_weight"
latent_probability_claim = false

scenario_source_ids

bank_sens_s_method
bank_sens_s_status

bank_sens_l_method
bank_sens_l_applicability_status
bank_sens_l_not_applicable_reason
bank_sens_l_source_count

distinct_transfer_source_or_law

frozen_v53_friedman_formulations

historical_tie_break_privilege = false
operational_tie_break_policy_id
operational_tie_break_scientific = false

venue_status
venue_is_methodology_gate = false

methodology_contract_status
```

Do not include:

```text
C_NPER_STATUS
```

---

# 23. Final QC additions

In addition to inherited QC:

1. source/input/code/registry/environment hashes present;
2. panel-derived numerical assertions not labeled verified without source evidence;
3. duplicate panel artefacts not counted as independent evidence;
4. historical C_NPER attribution correction recorded;
5. no old truth ontology automatic carry-over;
6. no automatic phi snap;
7. signed rho fields complete;
8. B* acceptance/rejection rates logged;
9. design weights sum correctly;
10. `latent_probability_claim=false`;
11. BANK-SENS-S class present;
12. BANK-SENS-L class present;
13. exact sensitivity methods pinned before outcome;
14. BANK-SENS-L incidence applicability explicitly evaluated;
15. no mandatory sensitivity class silently skipped;
16. sensitivity layers winner-ineligible;
17. sensitivity intervals not called population CIs;
18. CRN pairing valid;
19. seed-level hypothesis testing absent;
20. Delta_eq precedes precision/budget;
21. budget does not modify Delta_eq;
22. runner-up fields complete;
23. Ward+CH has no automatic scientific privilege;
24. Ward+CH has no automatic operational privilege;
25. operational policy, if present, is separately labeled;
26. transfer gate cannot change scientific winner;
27. no duplicate A_TRANSFER without distinct law/source;
28. new-project n_per directly frozen if used;
29. no `C_NPER_STATUS`;
30. venue non-gating;
31. venue uncertainty does not alter DGP/estimand;
32. frozen four Friedman formulations correct;
33. any amendment has signed new-material-science justification;
34. no result reading before F12;
35. reopening trigger, if invoked, has evidence class;
36. unresolved non-material panel provenance does not silently become design blocker;
37. every new block passes the “unanswered scientific question” parsimony test.

---

# 24. Remaining calibration-only items

These are measurements / implementation pins, not topics for another LLM methodology vote:

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
14. new n_per if used;
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
25. BANK-SENS-L applicability audit + exact implementation;
26. transfer qualification thresholds;
27. R-REV gate;
28. deployment operational policy only if a single pipeline is actually required;
29. software/environment hashes;
30. executable manifest QC;
31. final report language;
32. explicit F12 sign-off.

Venue choice and unresolved historical panel identity are **administrative/provenance notes**, not calibration design measurements and not methodology freeze blockers unless they reveal a new material design contradiction.

---

# 25. Reopening policy

Status progression:

```text
draft
-> calibration_pins_complete
-> manifest_analysis_contract_complete
-> explicit_signoff
-> frozen
```

After `frozen`, reopening only if:

1. calibration materially falsifies a frozen design assumption;
2. provenance/source audit reveals a **material design-relevant** contradiction;
3. genuinely new objection class appears.

Not reopening triggers:

- another LLM gives different score;
- same argument is rephrased;
- another model claims higher consensus;
- historical incumbent performs poorly;
- venue changes;
- non-primary panel ranking changes;
- unresolved non-material panel identity remains unresolved.

---

# 26. Terminal methodology statement

> This benchmark is a separate preregistered SSA application-calibrated clustering study. Its primary scientific target is design-weighted exact recovery of `k_true` over an outcome-blind, pre-frozen finite `B*×H*` design for `k={3,4,5,6,8}` and both sexes. `Q_CD` is the calibration-constrained construction/provenance law used to generate the bank, not a latent SSA prototype probability distribution. Primary morphology is WC-ALC; W-L/W-I/W-R are observed-window descriptors, while truth is defined by frozen distinct generator/prototype parameter instances. WC-ADL and TAD/PSAT are the only primary generator candidates and are selected using outcome-blind adequacy gates; double failure triggers redesign. Signed prototype geometry is recorded without using historical rho thresholds as design triggers. The winner layer uses empirically calibrated clean residual-supported noise without automatic AR(.97) snapping; canonical sigma/AR(.97) conditions are winner-ineligible. Primary uncertainty is CRN-paired Monte Carlo uncertainty conditional on the frozen bank. Scenario-bank and source-trajectory sensitivity classes are mandatory but winner-ineligible; their exact estimators are frozen after calibration-structure applicability checks, with incidence/delete-source jackknife as the preferred source-influence candidate when interpretable and a visible STOP/fallback rule when it is not. `Delta_eq` is fixed from scientific relevance before outcomes and determines precision and compute requirements, never the reverse. No unique winner is forced. Historical Ward+CH has no automatic scientific or operational tie-break privilege. Transfer is a deployment qualification gate unless a genuinely distinct transfer source/law defines a separate estimand. Secondary Friedman/Nemenyi uses the frozen four formulations by default; any amendment requires a signed pre-outcome deviation supported by a genuinely new material scientific reason. Venue and unresolved non-material panel identity are non-gating metadata. No algorithm×CVI outcome may be read until the complete methodology, sensitivity, precision, manifest, analysis and reporting contract is explicitly signed and frozen.

---

# 27. Final decision

**Methodological panel phase: CLOSE.**

**GO:**
```text
yeni_proje_empirik_kalibrasyon_protokolu_v0.md
```

**NO-GO:**
```text
algorithm × CVI performance outcome reading
```

No additional numbered LLM synthesis round is scientifically warranted unless one of the explicit reopening triggers is met.

**v11 + explicit PI sign-off** is the appropriate basis for `p_konum_plus_decision_freeze_v0`.

