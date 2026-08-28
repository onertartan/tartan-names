# ART-F0 — Project Identity and Provenance Record (F0)

## 0. Artifact identity

```text
artifact_id        = ART-F0
artifact_role      = project_identity_and_provenance_record
normative          = false
normative_authority = v11_only
gate               = F0
gate_status        = COMPLETE only if all F0 QC passes  -> see §11: COMPLETE
date               = 2026-08-28
worktree           = G:/PycharmProjects/pkp-worktree
branch             = p_konum_plus
HEAD_at_execution  = e4a09e811f9803623af7208898199026e9a71cc9
record_revision    = r2_provenance_correction_2026-08-28
r1_sha256          = cdc14bb626e295f6dab8091f12ade37e3d4d3a9738c6e346c627d6a53f6b0846
```

Revision r2 is a narrow provenance-byte-layer correction only: it restates the
legacy hash verification in explicit byte layers (§7.3) and populates the
section-7 ledger hash (§8). No scientific content — question, estimand, K, sex
scope, winner source, claim boundary, weight semantics, comparator role, open
pins, gate sequence, or firewall — was changed.

This F0 record is an **execution/freeze artifact derived from v11**. It does
NOT become an independent methodology authority. If any statement here is found
to differ from v11: `v11_wins = true`. The filename is an implementation/
provenance choice only and carries no scientific meaning.

Governing documents (both re-verified by SHA256 immediately before this record
was written; see §7.1):

- normative: `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md`
- execution protocol: `p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md`
  (operationalizes v11; cannot override it)

---

## 1. Project identity (v11 §1)

```text
project_id              = p_konum_plus
project_type            = separate preregistered/application-calibrated project
legacy_project_relation = historical_read_only_comparator
```

This project is **scientifically separate** from the legacy frozen v5.3
benchmark. The legacy project is bit-immutable, read-only, historical
comparator/provenance only (v11 §0.2). Legacy scientific choices are **not**
automatic normative inheritance for this project.

---

## 2. Primary research question (v11 §1)

v11 original (Turkish, quoted faithfully):

> Sonuç-kör SSA kalibrasyonuyla kısıtlanmış ve outcome öncesi dondurulmuş
> finite bir application-design bank üzerinde, hangi clustering algorithm × CVI
> pipeline `k_true ∈ {3,4,5,6,8}` değerini en yüksek design-weighted exact-k
> recovery ile bulur?

Faithful English rendering (no broadening into a population claim):

> On an outcome-blind SSA-calibrated and pre-outcome frozen finite
> application-design bank, which clustering algorithm × CVI pipeline recovers
> `k_true ∈ {3,4,5,6,8}` with the highest design-weighted exact-k recovery?

Preserved semantic tokens:

```text
outcome_blind
SSA_calibration_constrained
finite_design_bank
k_true = {3,4,5,6,8}
design_weighted
exact_k_recovery
```

---

## 3. Claim boundary (v11 §1)

```text
allowed_claim =
performance across the frozen calibration-constrained application design

forbidden_claim =
performance under the true latent SSA prototype distribution

weight_semantics =
design_weight

latent_probability_claim =
false
```

Design weights are **not** empirical cluster prevalence and **not** latent
population probabilities, and are never reinterpreted as such.

---

## 4. Primary estimand architecture (v11 §2) — no calibration pin filled

Architecture recorded by identity only:

```text
Q_CD(k,s)          — calibration-constrained joint-set construction/design/provenance law
B*_{k,s}           — pre-outcome frozen finite application scenario bank
H*_s               — pre-outcome frozen empirical clean residual-supported noise bank
A_m(k,s)           — per-sex, per-k design-weighted exact-k recovery score
A_m^APP            — macro primary estimand (1/2 over sexes, 1/5 over k)
Â_m                — finite estimator over frozen cells with CRN-paired MC realizations
```

Explicit semantics:

```text
Q_CD  = construction/design/provenance law
Q_CD != latent population probability
B*    = pre-outcome frozen finite application scenario bank
H*    = pre-outcome frozen empirical clean residual-supported noise bank
winner_source = A-APP only
```

No numeric Q_CD, B*, H*, weight, threshold, bank size, or `n_per_cluster`
value is defined, selected, or implied by this record. All calibration-open
pins remain exactly as registered in the v0 execution protocol (32 items,
v11 §26).

---

## 5. k and sex scope (v11 §3)

```text
K              = {3,4,5,6,8}
k_macro_weight = 1/5

sex_scope      = {M,F}
```

Where macro sex pooling is used under the frozen contract:

```text
v_M = 1/2
v_F = 1/2
```

k=5 governance:

```text
k5_winner_privilege = false
```

k=5 may serve only as empirical mirror / descriptive anchor. `k_hat = k±1` is
secondary partial-credit sensitivity only and does not change the primary
exact-k score.

Candidate selector support is a later registry fact, recorded here as identity
only — **F9 is not executed by this record**:

```text
k_candidate = 2..10
```

---

## 6. Historical comparator governance (v11 §13, §17)

```text
historical_Ward_CH_role =
historical_incumbent_comparator

scientific_tie_break_privilege =
false

operational_tie_break_privilege =
false

historical_tie_break_privilege =
false
```

Legacy results MUST NOT motivate or tune any new-project calibration pin
(FIREWALL VIOLATION otherwise, per the v0 evidence firewall matrix). No legacy
winner performance number is reproduced in this record; v11 requires none for
identity/provenance, so identity/hash custody is used exclusively. The
historical `n_per=10` C-block record remains a provenance fact only and is not
a design rationale (v11 §17).

---

## 7. Provenance ledger

All hashes below are SHA256 of on-disk bytes unless a byte layer is stated.
Verification performed 2026-08-28 at HEAD `e4a09e8`, by mechanical hashing
only — no legacy scientific content was opened or interpreted.

### 7.1 Governing documents (recomputed this task)

| document | path | recomputed SHA256 | required | result |
|---|---|---|---|---|
| v11 FINAL NORMATIVE (sole normative methodology source) | `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | same | **PASS (exact)** |
| Empirical calibration protocol v0 (execution protocol; operationalizes v11, cannot override it) | `p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md` | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` | same | **PASS (exact)** |

Precedence: `v11_wins = true`.

### 7.2 Reconciliation-source identities (v11 §0.1) — history only

| artifact | SHA256 (from v11 normative ledger) |
|---|---|
| `ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md` | `3bd9e7cfdbdfe9358f91792db12447594d86956cd1c1b185552cb2da4d94b787` |
| `claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md` | `29c073ba5105a14299a0ea9427d8443c1a29d40960f7fed355ef49b2bae67c5a` |

```text
reconciliation_provenance_only = true
normative_authority            = false
local_hash_verification_status = NOT_ATTEMPTED_PER_TASK_RULE
```

Per the F0 task rule, these files were neither searched for nor read; the hash
values above are transcribed from the v11 normative ledger. Non-verification
of these history-only artifacts is not a contradiction.

### 7.3 Historical frozen project identities (v11 §0.2)

```text
legacy_status                   = bit_immutable_read_only_historical_provenance
automatic_normative_inheritance = false
canonical_verification_source   = preserved historical legacy worktree
                                  (G:/PycharmProjects/tartan-names) on-disk bytes,
                                  used for mechanical identity verification only;
                                  no content read or interpreted
new_worktree_rendering_status   = NON_CANONICAL_EOL_RENDERING
```

Per-artifact byte-layer records (all values SHA256, recomputed 2026-08-28):

`protocol/01_kosum_protokolu_v5_3.md`

```text
normative_ledger_sha256                  = cf8b453f0a05e2e6fed0c8b73692c2a5361fdfe60a22b3c9fe8c612e0e13db67
new_worktree_on_disk_sha256              = 1f5dd374fc777b4a6da7a41f2ceec0fb823b7a2308a8449fe30beda3a441c80a
canonical_legacy_worktree_on_disk_sha256 = cf8b453f0a05e2e6fed0c8b73692c2a5361fdfe60a22b3c9fe8c612e0e13db67
repo_blob_sha256                         = cf8b453f0a05e2e6fed0c8b73692c2a5361fdfe60a22b3c9fe8c612e0e13db67
canonical_verification_layer             = canonical_legacy_worktree_on_disk
verification_result                      = canonical_legacy_hash_verification = PASS_EXACT
new_worktree_on_disk_hash_match          = false
new_worktree_difference_reason           = checkout_EOL_rendering
```

`protocol/kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md`

```text
normative_ledger_sha256                  = 99c17c42711fd27dd2e55baf55f5ed41388b14a39a29e196f8eb1def34a5d0a7
new_worktree_on_disk_sha256              = e2a06560d571936361f6e5c6b39cc4ecbe6da6ab3ef5ae6ae745820158cca3db
canonical_legacy_worktree_on_disk_sha256 = 99c17c42711fd27dd2e55baf55f5ed41388b14a39a29e196f8eb1def34a5d0a7
repo_blob_sha256                         = 99c17c42711fd27dd2e55baf55f5ed41388b14a39a29e196f8eb1def34a5d0a7
canonical_verification_layer             = canonical_legacy_worktree_on_disk
verification_result                      = canonical_legacy_hash_verification = PASS_EXACT
new_worktree_on_disk_hash_match          = false
new_worktree_difference_reason           = checkout_EOL_rendering
```

`protocol/run_matrix_v4.csv`

```text
normative_ledger_sha256                  = 34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64
new_worktree_on_disk_sha256              = 34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64
canonical_legacy_worktree_on_disk_sha256 = 34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64
repo_blob_sha256                         = 56a773b72dde8e25733121e1aa020876ac7d80db94f8cb010914c44c9f58d4c1
canonical_verification_layer             = canonical_legacy_worktree_on_disk
verification_result                      = canonical_legacy_hash_verification = PASS_EXACT
new_worktree_on_disk_hash_match          = true
```

Byte-layer rules applied:

- No legacy file was altered, normalized, renamed, cleaned, or repaired.
- No normalized/CR-stripped byte stream is treated as an on-disk exact match
  anywhere in this record. The new-worktree CRLF renderings of the two `.md`
  files are recorded as `NON_CANONICAL_EOL_RENDERING` with
  `new_worktree_on_disk_hash_match = false`; they are NOT called PASS.
- Verification is carried by the canonical layer only: the preserved historical
  legacy worktree's on-disk SHA256 equals the v11 ledger value exactly for 3/3
  artifacts (`PASS_EXACT`). The `repo_blob_sha256` values are additional
  identity custody; for `run_matrix_v4.csv` the blob is the LF storage form
  and is informational only, not the canonical layer.
- Difference mechanism (informational, not a verification basis): this
  worktree checks out with `core.autocrlf=true` and no `text`/`eol` attribute
  covering `protocol/`, so LF-stored blobs render with CRLF on disk here.
- `.gitattributes` outside `p_konum_plus/` was not changed.
- STOP rule: had a canonical legacy worktree file been absent, or had its
  exact on-disk SHA256 mismatched the v11 ledger, this gate would STOP.
  Neither occurred.

### 7.4 Operational new-project chain (identity/hash/commit custody only)

| artifact | path | SHA256 (on-disk, recomputed) | introducing commit | role | status |
|---|---|---|---|---|---|
| v11 normative source | `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | `965577d` | sole normative methodology source | **NORMATIVE** |
| Bootstrap isolation audit | `p_konum_plus/provenance/bootstrap_isolation_audit_2026-08-28.md` | `ea6531e8b39fd381874ed81950983566cf2ebc52831141444c0b352362727d35` | `cf73a83` | worktree isolation / firewall audit record | non-normative operational provenance |
| Empirical calibration protocol v0 | `p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md` | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` | `edc4a38` | F0–F12 execution protocol (operationalizes v11) | normative working artifact, `draft_pre_F12` |
| Calibration protocol drafting report | `p_konum_plus/provenance/calibration_protocol_v0_drafting_report_2026-08-28.md` | `088c6590462978d71edff58465ae9179a72c3759bee334e284c953032a6c6050` | `e4a09e8` | drafting-task end report | non-normative operational provenance |
| Calibration protocol correction report | `p_konum_plus/provenance/calibration_protocol_v0_correction_report_2026-08-28.md` | `a76d2290bfca1b0c75e39a56ce5859ef5261834df13a330373c66b4e890b4b44` | `e4a09e8` | execution-audit correction report | non-normative operational provenance |
| LF line-ending policy | `p_konum_plus/.gitattributes` | `d2eb1a317920a1e2fd04a1b7352ef04bfb1f0b9f4d0594f4dc395a87ce2ccfba` | `643cc7e` | repository EOL policy for the new-project namespace | non-normative operational configuration |

Git chronology confers **no** scientific authority. The only normative
methodology authority is v11.

---

## 8. Manifest-level F0 fields (machine-readable)

```text
project_id                   = p_konum_plus
design_version               = v11_FINAL_NORMATIVE_2026-08-27
methodology_contract_status  = draft_pre_F12
parent_normative_source      = ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
parent_normative_sha256      = d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3
execution_protocol_source    = yeni_proje_empirik_kalibrasyon_protokolu_v0.md
execution_protocol_sha256    = b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280
panel_source_ledger_hash     = 761cfdda49f62cabf20d2b5dc41f3a56721314d78c3ad81f038e1a96a923a69f
panel_source_ledger_hash_scope = canonical_UTF8_LF_bytes_of_SECTION_7_only
self_hash                    = false
question_id                  = PKP-Q1
claim_scope                  = performance across the frozen calibration-constrained application design
winner_layer                 = A-APP
weight_semantics             = design_weight
latent_probability_claim     = false
historical_tie_break_privilege = false
venue_status                 = administrative_metadata
venue_is_methodology_gate    = false
```

Implementation literals (transparent, no scientific effect):

```text
question_id = "PKP-Q1":
  implementation_literal_only = true
  scientific_effect = none

design_version = "v11_FINAL_NORMATIVE_2026-08-27":
  implementation_literal_only = true
  scientific_effect = none  (names the parent contract version)

panel_source_ledger_hash:
  implementation_literal_only = true   (the hash-scope definition is operational)
  scientific_effect = none
  self_hash = false
  scope = canonical_UTF8_LF_bytes_of_SECTION_7_only
  payload definition: every line of this file from the section heading line
  that opens section 7 ("7. Provenance ledger", inclusive) up to but not
  including the section heading line that opens section 8; CR bytes stripped;
  every line LF-terminated. The value is stored here in section 8, OUTSIDE
  the hashed payload, so no self-reference exists.
  reproduction:
    awk '/^## 8\. Manifest-level F0 fields/{exit} p{print} /^## 7\. Provenance ledger/{p=1; print}' <this_file> | tr -d '\r' | sha256sum
  No F0 .sha256 sidecar is created; the project-wide external freeze sidecar
  remains an F12-only artifact.
```

`methodology_contract_status` is deliberately **not** `frozen`: F12 explicit
PI sign-off has not occurred.

---

## 9. Panel / LLM provenance rule (v11 §20)

```text
LLM_opinion_is_empirical_evidence = false
```

The §7.2 reconciliation artifacts are LLM-panel syntheses retained as
decision-lineage history only. If any panel artifact is found bit-identical or
attribution-defective:

```text
independent_evidence_score = N-A
```

until attribution is resolved. No attribution adjudication was performed at F0
and none is required; unresolved non-material panel identity is not a freeze
blocker. No old LLM synthesis was inspected to create any methodology
argument in this record.

---

## 10. Information and outcome firewall

```text
legacy_information_firewall  = ACTIVE
algorithm_CVI_outcome_access = PROHIBITED
calibration_execution_status = NOT_STARTED
F12_explicit_PI_signoff      = false
frozen                       = false
```

Not performed in this task (and prohibited until their gates / F12):
legacy winner/result content reading; legacy S-06 result reading; legacy
robustness result reading; legacy SSA deployment result reading; new-project
algorithm×CVI result reading; algorithm×CVI execution; SSA calibration data
analysis; generator fitting; threshold selection; `n_per_cluster` selection;
Q_CD construction; B* construction; H* construction.

---

## 11. F0 QC

| # | check | result | evidence |
|---|---|---|---|
| 1 | normative v11 hash exact | PASS | §7.1 |
| 2 | v0 execution-protocol hash exact | PASS | §7.1 |
| 3 | project old/new boundary explicit | PASS | §1 |
| 4 | sole normative-source precedence explicit | PASS | §0, §7.1 |
| 5 | claim boundary explicit | PASS | §3 |
| 6 | `weight_semantics = design_weight` | PASS | §3, §8 |
| 7 | `latent_probability_claim = false` | PASS | §3, §8 |
| 8 | K exactly `{3,4,5,6,8}` | PASS | §5 |
| 9 | both sexes in scope | PASS | §5 |
| 10 | k=5 no winner privilege | PASS | §5 |
| 11 | A-APP is the only scientific winner source | PASS | §4, §8 |
| 12 | Ward+CH zero scientific/operational automatic tie-break privilege | PASS | §6 |
| 13 | legacy artifacts read-only provenance only | PASS | §1, §7.3 |
| 14 | legacy scientific decisions not automatically inherited | PASS | §1, §7.3 |
| 15 | venue administrative metadata only | PASS | §8 |
| 16 | no LLM consensus treated as empirical evidence | PASS | §9 |
| 17 | no calibration pin filled | PASS | §4 (all 32 v0 pins untouched) |
| 18 | no F1 activity occurred | PASS | §10 (no SSA data touched) |
| 19 | no algorithm×CVI outcome read/generated | PASS | §10 |
| 20 | provenance ledger deterministic identity/hash records | PASS | §7 |
| 21 | filename/internal metadata/date consistent | PASS | §0 (2026-08-28 throughout) |
| 22 | F0 artifact not labeled as independent normative source | PASS | §0 (`normative = false`, `normative_authority = v11_only`) |
| 23 | legacy_hash_QC — canonical legacy worktree on-disk SHA256 equals the v11 pin exactly for all three frozen artifacts (`PASS_EXACT` 3/3); no normalized stream counted as an on-disk match | PASS | §7.3 |
| 24 | panel_source_ledger_hash_QC — actual section-7 canonical hash populated in §8 and independently recomputed exactly after all edits | PASS | §8; r2 end-of-task report |

All 24 checks PASS (r2).

---

## 12. Gate closure

```text
F0_status            = COMPLETE
next_gate            = F1
F1_execution_started = false
```

F1 (raw input inventory, hashes, eligibility, time axis, preprocessing,
z-normalization) is NOT executed by this record and requires its own task
under the v0 execution protocol.
