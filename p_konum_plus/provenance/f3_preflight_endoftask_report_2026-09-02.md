# p_konum_plus — F3 PRE-FLIGHT — End-of-Task Record (verbatim)

```text
artifact_role = operational end-of-task chat responses, saved verbatim on user request
status        = NON-NORMATIVE
date          = 2026-09-02
task          = F3 PRE-FLIGHT ONLY (no adequacy execution)
structure     = Part 1: re-verification confirmation (final response, verbatim)
                Part 2: full pre-flight deliverable (prior response, verbatim)
note          = the task prompt was delivered twice (inline, then as an attached
                file); Part 2 is the original execution, Part 1 confirms identity
                of the duplicate and re-verifies custody hashes
```

---

## Part 1 — Re-verification confirmation (final response, verbatim)

Bu dosya, bir önceki mesajda tam olarak yürütülen F3 PRE-FLIGHT görevinin birebir aynısı — görev zaten tamamlandı ve depo durumu o zamandan beri değişmedi (HEAD `3e4daf4`, tracked değişiklik yok, 35 bilinen untracked dosya, beş custody hash'i yeniden doğrulandı ve birebir aynı).

Geçerli durum, önceki yanıttaki dört çıktıyla birlikte aynen ayaktadır:

1. **F3 entry/preflight contract audit** — Task A PASS (tüm hash'ler exact; F1 manifest `8a6034eb…`, 906 satır, frozen kayıtla eşleşiyor); Task B'de 18 başlıklı v11-kaynaklı F3 sözleşmesi, her madde `V11_LITERAL` / `V11_DIRECT_IMPLICATION` / `POST_V11_EXECUTION_GOVERNANCE` etiketiyle; `adequacy_threshold_derivation_rule … must_be_frozen_before_candidate_specific_adequacy_comparison` sıralamasının kaynağı açıkça **POST_V11_EXECUTION_GOVERNANCE** (v0 execution-audit düzeltmesi 2026-08-28, madde 4; v0 satır 72 ve 268–278) — yeni metodoloji kararı değil.
2. **P03/P04/P05 owner-decision packet** — P03: D-P03-1..5 (eşik biçimi, referans dağılımı, ön-deklare literaller, spline benchmark pini, kriter-4 sansür temeli); P04: T-A/T-B/T-C seçenekleri + zorunlu deterministik nötr terminal fallback; P05: X-A/X-B/X-C şema seçenekleri, deterministik hash-tabanlı fold ataması. Hiçbiri seçilmedi, hiçbiri yürütülmedi.
3. **Source/provenance table** — v11-literal kurallar ile post-v11 yürütme-yönetişim kuralları ayrıştırılmış halde.
4. **Next-task boundary** — sıradaki görev yalnızca PI'nin P03/P04/P05 paketini incelemesi/ratifikasyonu; aday-özel adequacy ölçümü ancak üç freeze'den sonra ayrı bir görevde.

Bulgular: cleanup = CL-F3-PRE-01 (spline benchmark implementasyonu henüz pinlenmedi → paket maddesi D-P03-4); informational = INF-F3-PRE-01 (F2 determinizm kapsamı aynı-süreç; F3 kendi kapsamını deklare etmeli), INF-F3-PRE-02 (kriter-4'ün F1 OD-7 semantiğiyle uyumlu yorumu owner kararına bağlandı).

```text
GLOBAL_BLOCKER        = none
GATE_SPECIFIC_BLOCKER = none
cleanup               = CL-F3-PRE-01 (spline adequacy-benchmark implementation not yet pinned; packet item D-P03-4)
informational         = INF-F3-PRE-01 (F2 determinism scope same-process only; F3 must declare its own);
                        INF-F3-PRE-02 (criterion-4 censored-identifiability basis needs owner interpretation per F1 OD-7);
                        derivation-rule-first ordering = post-v11 execution governance, correctly labelled

F3_ENTRY_READY = true

P03_derivation_rule_status = OWNER_RATIFICATION_REQUIRED
P03_threshold_values       = NOT_COMPUTED
P04_status                 = OWNER_DECISION_REQUIRED
P05_status                 = OWNER_DECISION_REQUIRED

generator_selected = false
candidate_specific_fit = false
P03_execution = false
P04_execution = false
P05_execution = false
F4_started = false

F3_started = false
commit = false
```

Sıradaki adım: PI'nin P03/P04/P05 karar paketini incelemesi/ratifikasyonu — generator adequacy execution değil.

---

## Part 2 — Full pre-flight deliverable (prior response, verbatim)

All pre-flight verification and extraction work is done. Below are the four required preflight outputs. No adequacy measurement, fit, threshold, ranking, or selection was produced.

# F3 PRE-FLIGHT — p_konum_plus

## Output 1 — F3 entry / preflight contract audit

### Task A — repository and custody preflight: PASS

| check | result |
|---|---|
| root | `G:/PycharmProjects/pkp-worktree` ✓ |
| branch | `p_konum_plus` ✓ |
| HEAD | `3e4daf47018f124e29717263e4e45fe90c8e52b8` ✓ (git diff empty; 35 known F2/F3-era untracked files, none tracked-modified) |
| v11 SHA256 | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` — exact, no STOP |
| F2 FINAL FREEZE r1 | `ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43` — exact |
| F2 acceptance audit | `8402bb68a924ccaae34d6923f6f5b8de8277a13c4af4e7478bcd94f062076dfa` — present, exact; states F2 = CLOSED, F3_allowed = true, F3_started = false |
| F1 eligible manifest | `p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv` = `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32`, 906 data rows — matches the hash frozen inside `f1_input_freeze_record_2026-08-28.md` (lines 32, 220). Only structural metadata inspected; no trajectory values read. |
| v0 protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` — exact |

Entry state confirmed: F0/F1 COMPLETE, F2 CLOSED, `generator_selected=false`, `P03/P04/P05_touched=false`, no blockers. Nothing repaired or rewritten.

### Task B — F3 contract extracted from v11

Sources: v11 §5 (lines 250–295), §25/§26 items 3–5, gate table (line 1024), §27, §28; v0 F3 gate block (lines 249–278) as execution governance only.

| item | contract | provenance |
|---|---|---|
| purpose | select one primary generator family via outcome-blind adequacy gates; double failure ⇒ redesign | **V11_LITERAL** (§5, §29) |
| active inputs | frozen F2 spec (P-01/P-02 exact formulas, bounds, init, failure rules — "freeze edilir at F2"), frozen F1 eligible trajectories, spline benchmark | **V11_LITERAL** (§5); the specific artifact identities (FREEZE r1, manifest) are **POST_V11_EXECUTION_GOVERNANCE** |
| primary generator candidate set | exactly WC-ADL and TAD/PSAT; closed | **V11_LITERAL** (§5: "Primary candidate set yalnız") |
| adequacy benchmark role | shape-constrained low-df spline: `role = adequacy_benchmark`, `automatic_primary_fallback = false` | **V11_LITERAL** (§5) |
| allowed calibration operations | outcome-blind generator fits, cross-fit adequacy, residual structure, parameter stability, written outcome-blind rationale (v0 EV-02/03/04/05/08) | **V11_DIRECT_IMPLICATION** (§5, §28.5); EV-code registry itself is **POST_V11_EXECUTION_GOVERNANCE** |
| forbidden operations/evidence | any algorithm/CVI output in generator selection; legacy performance content (v0 EV-13..17); third family | **V11_LITERAL** (§5: "No clustering algorithm/CVI output generator selectionında kullanılamaz"; §28.6) |
| adequacy evaluation order | 1 morphology coverage → 2 cross-fitted reconstruction/predictive fit → 3 systematic residual morphology/structure → 4 censored-case identifiability → 5 parameter stability → 6 parsimony | **V11_LITERAL** (§5) |
| P03 role | adequacy thresholds = calibration-only open item; measurement-derived, outcome-blind, never invented | **V11_LITERAL** (§26.3); `MEASUREMENT_REQUIRED` status label is **POST_V11_EXECUTION_GOVERNANCE** (v0 P-03) |
| P04 role | generator tie-break exact rule = calibration-only open item; outcome-blind, pre-frozen, pinned in F3 | **V11_LITERAL** (§5 "Tie-break: outcome-blind, pre-frozen, F3'te pinlenir"; §26.4) |
| P05 role | cross-fit scheme = calibration-only open item | **V11_LITERAL** (§26.5) |
| tie-break semantics | deterministic/outcome-blind/pre-frozen; Ward+CH has zero tie-break privilege; legacy-neutral | **V11_LITERAL** (§5, §13 `scientific_tie_break_privilege = false`, §29) |
| cross-fit semantics | "family/model adequacy selection audit içindir" — audit of family adequacy only, never algorithm/CVI validation | **V11_LITERAL** (§5) |
| F3/F4 boundary | F3 = adequacy + selection; final full-data refit of the selected generator happens after family+fitting freeze (F4 gate: final-refit rule, parameter banks) | **V11_LITERAL** (§5, gate table F3/F4 rows) |
| STOP behavior | both primary candidates fail ⇒ `STOP, action = redesign`; no improvisation | **V11_LITERAL** (§5, gate table) |
| family-selection irreversibility | "family seçimi yeniden açılamaz" after selection under frozen rules | **V11_LITERAL** (§5) |
| outcome firewall | no algorithm×CVI outcome generated/read before F12 | **V11_LITERAL** (§28.6, §29) |
| required provenance/QC | every pin logged with source/rationale/hash; measurement-derived pins distinguished from historical references; ART-F3 = adequacy report + selection record + tie-break pin | logging duty **V11_LITERAL** (§28.7, §28.9); ART-F3 naming **POST_V11_EXECUTION_GOVERNANCE** (v0) |
| gate-completion logic | one family selected under frozen thresholds and tie-break, or STOP | **V11_DIRECT_IMPLICATION** (§5 + gate table); exact completion criterion wording **POST_V11_EXECUTION_GOVERNANCE** (v0 F3 block) |

**Explicit provenance audit of the ordering rule** `adequacy_threshold_derivation_rule must_be_frozen_before_candidate_specific_adequacy_comparison`: this exact rule is **POST_V11_EXECUTION_GOVERNANCE** — it entered via the v0 execution-audit correction of 2026-08-28 (v0 changelog line 72, item 4; binding block at v0 lines 268–278). v11 literally requires thresholds to be outcome-blind, pre-selection, calibration-derived (§5, §26.3) and forbids outcome-influenced pin choice (§28), of which the derivation-rule-first ordering is a faithful governance tightening. It is **not** a new methodology decision and is not being reopened here.

### Task C — F2 → F3 contradiction/gap audit

F3 consumes from the accepted FREEZE r1: exact P-01/P-02 formulas and bounds, D-F2-08 objective, Kural T/S admissibility, the full D-F2-09 initialization contract (731/261 starts), the optimizer/fallback contract (STEP3-A01-corrected binding), and the frozen failure taxonomy. All are present, hash-anchored, and sufficient for candidate-specific fitting when F3 execution is later authorized. F2 STEP-2 was synthetic-only with a telemetry firewall (no L/rho/recovery/family-performance fields), so **no candidate-specific adequacy information leaked into F2** — the F3 outcome-blindness precondition holds.

Findings (none blocking):

- **global blocker:** none.
- **gate-specific blocker:** none.
- **cleanup — CL-F3-PRE-01:** the shape-constrained low-df spline `adequacy_benchmark` has a v11-frozen *role* but no frozen *implementation* anywhere in F2 artifacts (correctly so — it is not a generator). Its exact outcome-blind specification must be pinned in the next F3 task before any adequacy measurement; included as a packet item below.
- **informational — INF-F3-PRE-01:** FREEZE r1 determinism scope is same-process double-run only. F3 measurement will run in new processes; F3 must declare its own determinism/provenance scope rather than inherit F2's. No contradiction.
- **informational — INF-F3-PRE-02:** adequacy criterion 4 ("censored-case identifiability") must be interpreted against frozen F1 eligibility (FULL-support-only 906; OD-7 absence = unpublished under SSA disclosure rules, converse not established, no [0,4] interval-censoring). The evaluation basis for criterion 4 therefore needs an owner decision (packet item D-P05-4/D-P03-5 below); wording difference, not a design contradiction.

## Output 2 — P03/P04/P05 OWNER DECISION PACKET (nothing executed)

### P03 — adequacy thresholds

```text
status = MEASUREMENT_REQUIRED
numeric_thresholds = NOT_COMPUTED
threshold_derivation_rule = OWNER_RATIFICATION_REQUIRED (must be frozen first)
measurement_derived_threshold_values = deferred until after rule freeze + measurement
```

Owner decisions required to freeze the **derivation rule** (all outcome-blind; none may be chosen after seeing which candidate a rule favors):

1. **D-P03-1 — threshold form per criterion:** for each of the six frozen criteria, is adequacy judged by (a) an absolute pre-declared structural check, (b) a quantile of the calibration distribution over eligible trajectories, or (c) a margin relative to the spline `adequacy_benchmark`? (v11 gives the spline exactly this benchmark role.)
2. **D-P03-2 — reference distribution definition:** population over which calibration distributions are formed — pooled 906, or per-sex (435 F / 471 M) with a pre-declared combination rule.
3. **D-P03-3 — quantile/margin parameters as pre-declared literals** (e.g., which quantile, which margin), fixed in the rule text before measurement; the numeric *threshold values* that result remain `NOT_COMPUTED` until measurement under the frozen rule.
4. **D-P03-4 — spline benchmark specification** (CL-F3-PRE-01): exact low-df shape-constrained spline family, df, constraint set, and fitting rule — pinned outcome-blind as benchmark infrastructure, explicitly `automatic_primary_fallback = false`.
5. **D-P03-5 — criterion-4 basis:** how censored-case identifiability is evaluated consistently with F1 OD-7 semantics (e.g., window-truncated morphology classes and/or synthetic censoring probes), without introducing [0,4] interval-censoring.

### P04 — exact generator tie-break

```text
status = OWNER_DECISION_REQUIRED
required properties = deterministic · outcome_blind · pre_frozen · legacy_neutral · no algorithm/CVI information
```

Bounded PI question (no selection made here): *if both families pass all frozen adequacy gates and are not separated at the frozen thresholds, which deterministic rule decides?* v11-consistent options:

- **T-A — lexicographic in the frozen adequacy order:** compare criteria 1→6 in the v11 order using pre-frozen equivalence tolerances; first decisive criterion wins.
- **T-B — single pre-declared scalar:** one pre-named cross-fitted adequacy statistic with a pre-frozen tie tolerance, falling back to T-A ordering.
- **T-C — parsimony-first:** decisive only if effective df differ (note: both families have 4 parameters, so this likely never separates them and would need a terminal fallback).
- **Terminal deterministic neutral fallback (required under any option):** a pre-declared, measurement-independent canonical ordering of the two family IDs, invoked only if all frozen comparisons are equivalent — matching v11 §14's "deterministic neutral fallback" principle.

### P05 — cross-fit scheme

```text
status = OWNER_DECISION_REQUIRED
execution = false
role = family/model adequacy selection audit only (never algorithm/CVI validation)
```

Bounded PI question using only frozen F1 structural facts (906 trajectories, T=146, per-trajectory independent fits, no elastic alignment):

- **X-A — across-trajectory K-fold:** folds partition the eligible names; family adequacy statistics computed on held-out trajectories. Sub-decisions: K (e.g., 5 or 10); per-sex stratification; deterministic fold assignment (hash-based on frozen trajectory ID — keeps `rng_used = false`).
- **X-B — within-trajectory temporal blocking:** held-out year blocks inside each trajectory. Caveat for PI: interacts with edge-truncated morphology and Kural S support counts; must not create de-facto warping or resample the class structure.
- **X-C — hybrid:** X-A primary with X-B as a pre-declared supplementary diagnostic only.

The scheme must be fully deterministic, pre-frozen, and produce only family-level adequacy audit quantities.

## Output 3 — source/provenance table (v11-literal vs post-v11 governance)

| rule | class | source |
|---|---|---|
| Candidate set = {WC-ADL, TAD/PSAT}, closed | V11_LITERAL | v11 §5 |
| Spline = adequacy_benchmark, never automatic fallback | V11_LITERAL | v11 §5 |
| Six-step adequacy order | V11_LITERAL | v11 §5 |
| Tie-break outcome-blind, pre-frozen, pinned in F3 | V11_LITERAL | v11 §5 |
| Both-fail ⇒ STOP/redesign, no third family | V11_LITERAL | v11 §5, gate table |
| Cross-fit = family adequacy audit only | V11_LITERAL | v11 §5 |
| Family selection irreversible after freeze | V11_LITERAL | v11 §5 |
| No algorithm/CVI output in selection; no outcome read before F12 | V11_LITERAL | v11 §5, §28 |
| P-03/P-04/P-05 are calibration pins, not methodology votes | V11_LITERAL | v11 §26.3–5 |
| Derivation rule frozen BEFORE candidate-specific comparison | POST_V11_EXECUTION_GOVERNANCE | v0 execution-audit correction 2026-08-28 item 4 (v0 lines 72, 268–278) |
| P-03 MEASUREMENT_REQUIRED / P-04, P-05 OWNER_DECISION_REQUIRED status labels | POST_V11_EXECUTION_GOVERNANCE | v0 pin register P-03..P-05 |
| Permitted/forbidden evidence classes EV-02..08 / EV-13..17 | POST_V11_EXECUTION_GOVERNANCE (implementing v11 firewalls) | v0 evidence registry |
| ART-F3 artifact naming, completion-criterion wording, STOP-05/STOP-16 codes | POST_V11_EXECUTION_GOVERNANCE | v0 F3 gate block |
| Six-step future ordering, steps 1–3 and 7 sequencing | POST_V11_EXECUTION_GOVERNANCE (v0 F3 procedure); steps 5, 8, 9, 10 are V11_LITERAL | v0 line 259; v11 §5 |

## Output 4 — frozen ordering for the NEXT task and recommended boundary

Allowed future F3 ordering (constructed, not performed):

1. PI ratifies P05 cross-fit scheme — POST_V11 governance sequencing
2. PI ratifies P03 adequacy-threshold **derivation rule** (incl. spline benchmark pin D-P03-4) — POST_V11 governance sequencing
3. PI freezes P04 exact deterministic outcome-blind tie-break — pre-freeze requirement V11_LITERAL; position in sequence POST_V11
4. only then candidate-specific outcome-blind adequacy measurement may begin — POST_V11 governance (implementing v11 outcome-blindness)
5. adequacy evaluated in the v11 frozen order (coverage → cross-fit → residual structure → censored identifiability → stability → parsimony) — V11_LITERAL
6. threshold values derived only under the pre-frozen derivation rule — POST_V11 governance
7. PI ratifies measurement-derived thresholds before family selection — POST_V11 governance (v0 F3 procedure step 4)
8. apply pre-frozen tie-break only if required — V11_LITERAL
9. select generator or invoke STOP (`action = redesign`) — V11_LITERAL
10. final full-data refit remains F4, not F3 preflight — V11_LITERAL

**Recommended next-task boundary:** the next task should be *only* PI review/ratification of this P03/P04/P05 packet (analogous to the D-F2 ratification round) — producing the frozen P05 scheme, the frozen P03 derivation rule, and the frozen P04 tie-break as owner-signed pins. Candidate-specific adequacy measurement (real SSA generator fits under the FREEZE r1 contract) must be a separate, later task authorized only after those three freezes exist.

## End-of-task verdict

```text
GLOBAL_BLOCKER        = none
GATE_SPECIFIC_BLOCKER = none
cleanup               = CL-F3-PRE-01 (spline adequacy-benchmark implementation not yet pinned; owner packet item D-P03-4)
informational         = INF-F3-PRE-01 (F2 determinism scope is same-process only; F3 must declare its own);
                        INF-F3-PRE-02 (criterion-4 censored-identifiability basis needs owner interpretation consistent with F1 OD-7);
                        derivation-rule-first ordering is post-v11 execution governance, correctly labelled, not new methodology

F3_ENTRY_READY = true

P03_derivation_rule_status = OWNER_RATIFICATION_REQUIRED
P03_threshold_values       = NOT_COMPUTED
P04_status                 = OWNER_DECISION_REQUIRED
P05_status                 = OWNER_DECISION_REQUIRED

generator_selected = false
candidate_specific_fit = false
P03_execution = false
P04_execution = false
P05_execution = false
F4_started = false

F3_started = false
commit = false
```

`F3_ENTRY_READY = true` — the next action is PI review/ratification of the P03/P04/P05 decision packet above, not generator adequacy execution.
