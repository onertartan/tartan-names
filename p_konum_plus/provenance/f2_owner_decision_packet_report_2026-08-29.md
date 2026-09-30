# p_konum_plus — F2 Generator Specification Draft + PI Decision Packet — End-of-Task Report

- **Report type:** F2 first-pass report (specification drafting + owner-decision packet; NO F3, NO adequacy comparison, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-29
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`
- **Subject artifact:** `p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md` (ART-F2, DRAFT_OWNER_DECISION_PACKET) — SHA256 `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7`
- **Governing sources (verified exact this task):** v11 `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` · v0 `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` · ART-F0 `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` · ART-F1 r4a `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0` · eligible manifest `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` · input hash table `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac`

---

## 1. Repository / precheck results — PASS

Root `G:/PycharmProjects/pkp-worktree` ✓, branch `p_konum_plus` ✓, working tree **clean** at start, actual HEAD recorded: `3e4daf47018f124e29717263e4e45fe90c8e52b8` ("record F1 execution and audit provenance"). `git ls-files` confirms all F0/F1 governance artifacts (ART-F1 r4a, both manifests, v11, v0, ART-F0, all provenance reports — 17 files) are **tracked**. Log shows the expected governance commit chain.

## 2. Governing / F1 hash results — all exact

v11 `d136502f…` · v0 `b6b4ed83…` · ART-F0 `56fa5093…` · **ART-F1 r4a `5eceb198…`** · eligible manifest `8a6034eb…` · input hash table `aa86f1ea…`. Re-verified byte-identical again after the pass. No STOP.

## 3. Admissible source/provenance inventory

Repository discovery (docs/, legacy protocol/, p_konum_plus/; `results/` never searched or opened): the names WC-ADL / TAD/PSAT / WC-ALC occur **only in v11 and v11-derived governance documents — no mathematical definition exists in the repository**; the v11 §0.1 reconciliation syntheses are absent locally; usage is consistent (absence, not inconsistency). Literature access **available (limited)**: two pages fetched 2026-08-29 — asymmetric generalized Gaussian confirmed as a recognized standard construction (formula quoted); single logistic standard, but the rise-decline double-logistic product is *not* documented there, so it is recorded as a project-defined composition (no fabricated citations). Owner task search cues recorded as owner-supplied provenance. Frozen ART-F1 facts used as EV-01.

## 4. WC-ADL draft specification (summary)

`g(u; c_r, c_d, k_r, k_d) = σ(k_r(u−c_r)) · σ(−k_d(u−c_d))`, `c_r ≤ c_d`, on `u=(t−1880)/145`; prediction = model curve **z-normalized on the same 146-grid** (amplitude/offset removed as unidentifiable by construction); latent timing may lie outside the window (finite box `[−1, 2]`, identifiability-horizon rationale) generating W-L/W-I/W-R as descriptors; steepness bounds `[4, 290]` tied to grid resolvability and excluded-morphology (step-like) adjacency; deterministic hybrid multistart; 9-code failure taxonomy with no-fallback/no-silent-repair principles. All numeric values are DRAFT_RECOMMENDATIONs.

## 5. TAD/PSAT draft specification (summary)

Two-piece asymmetric generalized Gaussian: `g(u; m, s_l, s_r, β) = exp(−((m−u)/s_l)^β)` for `u≤m`, right branch with `s_r`; shared `β ∈ [1,6]` (5-param `β_l≠β_r` = owner alternative); `m ∈ [−1,2]`, scales `[0.02, 3.0]` with impulse-/cylinder-adjacency and flatness rationales; same interface, initialization, and failure policy structure. Trivial checks: both families finite/nonconstant/z-valid across W-L/W-I/W-R-style configurations; one P-02 bounds-box **corner underflows to constant zero** — documented as the reachable `ZERO_VARIANCE_FIT` case (and why corners are excluded from boundary starts).

## 6. Naming/definition ambiguity found

Both labels are **project-specific with no repository mathematical definition**; "ADL"/"TAD"/"PSAT" expansions were **not** inferred (no source support). `P-02_name_definition_status = OWNER_DECISION_REQUIRED` (D-F2-01): recommended = one family with dual historical labels bound to the P-02 formula; alternatives = PSAT-as-parameterization, or escalate as genuinely ambiguous. Candidate cardinality stays exactly 2.

## 7. PI owner-decision register

**D-F2-01** TAD/PSAT naming semantics · **D-F2-02** time coordinate (recommend `u`) · **D-F2-03** z-normalized prediction operator, no amplitude/offset (contract-defining) · **D-F2-04** P-01 exact formula · **D-F2-05** P-02 exact formula · **D-F2-06/07** bounds-table ratifications (empirical refinement = MEASUREMENT_NOT_RUN_IN_THIS_PASS) · **D-F2-08** fit objective (recommend unweighted LS in frozen z-space; robust loss changes the estimand) · **D-F2-09** initialization/multistart incl. exact start count · **D-F2-10** fit-failure policy + taxonomy (+ success predicate as its operational complement). Classified per the task rule: constraint parameterization and optimizer choice = `CLASS_C_IMPLEMENTATION_CANDIDATE` (not promoted to scientific pins); each decision carries recommendation, alternatives, consequences, and a family-altering flag. Full 16-record pin table in ART-F2 §14.

## 8. Artifact created

`p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md` (ART-F2, `record_status = DRAFT_OWNER_DECISION_PACKET`, all 16 required sections; not FINAL; no self-hash inside; no sidecar).

## 9. ART-F2 draft SHA256

```text
d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7
```

## 10. No empirical family adequacy comparison was run — CONFIRMED

No trajectory was fitted; no reconstruction/predictive/residual/stability/coverage/parsimony comparison of any kind; only hand-constructed-parameter finiteness/transform checks (EV-02 permitted set).

## 11. P-03 / P-04 / P-05 untouched — CONFIRMED

No adequacy threshold, no tie-break, no cross-fit scheme defined or discussed beyond declaring them F3-owned.

## 12. Firewall confirmation

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
algorithm_CVI_execution = false
generator_adequacy_comparison = false
generator_selection = false
cross_fit_adequacy = false
P03_touched = false
P04_touched = false
P05_touched = false
F3_started = false
F4_started = false
Q_CD_created = false
B_star_created = false
H_star_created = false
```

## 13. `git status --short --untracked-files=all` (at end of F2 pass)

```text
?? p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md
```

Exactly the one new draft, untracked and uncommitted; F1 artifacts byte-identical.

## 14. Verdict

```text
F2_OWNER_DECISION_PACKET_READY
```

Expected terminal state holds: `F2_status = OWNER_DECISION_REQUIRED`, `F2_complete = false`, `F3_allowed = false` — awaiting PI resolution of D-F2-01..D-F2-10, after which in-F2 fit-feasibility validation of the ratified specs (still no family comparison) and the F2 freeze pass can follow.
