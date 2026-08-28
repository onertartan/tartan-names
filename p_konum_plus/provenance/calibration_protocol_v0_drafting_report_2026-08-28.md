# p_konum_plus — Calibration Protocol v0 Drafting Task — End-of-Task Report

- **Report type:** governance-only protocol-construction task report (NO CALIBRATION / NO OUTCOME ACCESS)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **Subject artifact:** `p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md`
- **Subject SHA256:** `769ef8798d3082df192cc670175a0bee707538e0953b774273753fe31cc0a4e0`
- **Parent normative source:** `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md`
- **Parent SHA256:** `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3`

---

## 1. Precheck results — PASS

- **Repository root:** `G:/PycharmProjects/pkp-worktree` ✓
- **Branch:** `p_konum_plus` ✓
- **Working tree at precheck:** clean. HEAD had advanced from `96412ee` to `cf73a83f050056949a4e9513627576ad0368c683` via two benign commits that record exactly the expected new-project artifacts: `965577d` (adds the v11 normative source) and `cf73a83` (adds the bootstrap audit record). No legacy path was touched by either.
- **Normative source:** exists; recomputed SHA256 = `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` — **exact match, no STOP**. The source was not repaired, normalized, or rewritten. No legacy algorithm × CVI result content was inspected.

## 2. File created

`p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md` — the only file written in the drafting task.

## 3. SHA256 of the draft

```text
769ef8798d3082df192cc670175a0bee707538e0953b774273753fe31cc0a4e0
```

## 4. F0–F12 status table

| Gate | Freeze object (short) | Status |
|---|---|---|
| F0 | identity, question, boundary, estimand, k/sex scope, comparator role, ledger | **READY** |
| F1 | input files/hashes, eligibility, time axis, preprocessing, z-normalization | OPEN — requires F1 source inventory |
| F2 | WC-ADL / TAD-PSAT exact spec (formula, bounds, init, failure) | OPEN — owner decisions |
| F3 | cross-fit scheme, adequacy thresholds, tie-break, selection | OPEN |
| F4 | final-refit rule, parameter bank, descriptors, label_fuzz | OPEN |
| F5 | Q_CD, distinctness/acceptance, weights, coverage guard, `n_per_cluster` | OPEN |
| F6 | frozen B* (size, IDs, weights, incidence metadata, hashes) | OPEN |
| F7 | signed geometry, strata, `epsilon`/`delta` | OPEN (infeasibility → `coverage_gap`, never global STOP) |
| F8 | H* sigma strata, dependence representation, canonical layer | OPEN |
| F9 | algorithm/CVI registry, tie/failure policy, environment hashes, frozen four | OPEN |
| F10 | Delta_eq → precision target → allocation → budget, CRN namespace | OPEN |
| F11 | BANK-SENS-S/L exact methods + applicability/fallback, estimator, manifest/QC | OPEN (conditional sub-items) |
| F12 | ratification only: consistency review, PI sign-off, hash sidecar | OPEN |

No gate is marked COMPLETE; the normative framework existing is not gate completion.

## 5. Item counts

- **NORMATIVE_CLOSED (A): 50** (enumerated register, each with a v11 § reference)
- **CALIBRATION_OPEN (B): 25** (pins P-01…P-22, P-24…P-26; canonical inventory = all of v11 §26)
- **IMPLEMENTATION_OPEN (C): 5** (P-23 CRN namespace, P-29 environment hashes, P-30 executable manifest QC, P-31 report language, P-32 sign-off act)
- **CONDITIONAL (D): 6** (R-REV, operational deployment policy, BANK-SENS-L fallback branch, distinct transfer estimand block, delta-method cross-check, incumbent-continuity label; the first two coincide with pins P-27/P-28)
- **FORBIDDEN (E): 30** (v11 §25 reproduced verbatim)

The pin register carries all 32 items of v11 §26; no numeric value was populated anywhere — only `UNRESOLVED` / `MEASUREMENT_REQUIRED` / `OWNER_DECISION_REQUIRED` / `CONDITIONAL` markers.

## 6. Unresolved items requiring owner/PI decision before execution

F1 source inventory and eligibility confirmation; P-01/P-02 exact generator formulas, bounds, initialization, and failure rules; P-04 generator tie-break; P-05 cross-fit scheme; P-07 label_fuzz rule; P-08 final-refit rule; P-09 Q_CD composition law; P-12 design-weight rule; P-14 numeric `n_per_cluster`; P-20 `Delta_eq` justification; F9 registry composition plus tie and failure/nonfinite policies; P-24/P-25 exact BANK-SENS-S/L procedures at F11; P-26 transfer thresholds; P-27 R-REV gate assignment and eligibility rule (v11 §22 assigns R-REV no gate — flagged explicitly rather than guessed); P-28 operational policy if genuinely required; P-32 F12 sign-off. Measurement-derived pins (P-03, P-06, P-10, P-11, P-13, P-15–P-19, P-21, P-22) additionally need PI ratification at their gates.

## 7. Material conflicts

**None normative.** Two non-blocking observations: (a) the HEAD advance described in item 1 — consistent governance activity, not a contradiction; (b) the task's manifest field list is a flattened subset of v11 §23 (e.g., `stage`, `resampling_rule_id`, and several outcome/sensitivity fields appear only in v11) — resolved per `v11_wins` by mapping the full §23 canonical set, with all outcome fields marked `POST_F12_ONLY`.

## 8. GO/STOP for a separate protocol review

**GO.** Recommend an independent methodological/execution audit of v0 against v11 (completeness of the 32-pin register, gate-table fidelity, firewall-matrix semantics) before F0 execution begins.

## 9. `git status --short` (at end of drafting task)

```text
?? p_konum_plus/calibration/
```

The draft is untracked and uncommitted; nothing was staged, no commit was made, no legacy file modified.

---

## Terminal state

```text
protocol_draft_created = true
calibration_started = false
outcome_firewall = intact
next_action = independent methodological/execution audit of v0
```
