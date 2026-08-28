# p_konum_plus — Calibration Protocol v0 Execution-Audit Correction — Report

- **Report type:** execution/governance correction task report (NO CALIBRATION / NO OUTCOME ACCESS / NOT a methodology-review cycle)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **Subject artifact:** `p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md`
- **Old SHA256 (pre-correction):** `769ef8798d3082df192cc670175a0bee707538e0953b774273753fe31cc0a4e0`
- **New SHA256 (post-correction):** `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280`
- **Parent normative source:** `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md`
- **Parent SHA256 (re-verified before editing):** `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3`

---

## 1. Exact changes made

**Correction 1 — F10 causal order (MUST FIX):**
- The F10 `procedure` cell was rewritten to the exact mandated order: relevance argument → PI freezes `Delta_eq` → derive paired MC precision target → analytic worst-case bounds → frozen design weights → paired-disagreement characterization without algorithm × CVI outcome access → outcome-blind precision simulation if necessary → scenario/seed allocation → compute-budget consequence. The preflight no longer precedes the `Delta_eq` pin.
- A binding block was added immediately after the F10 table stating literally `paired_disagreement_information_pre_F12 / must_not_be_estimated_from_algorithm_x_CVI_benchmark_outcomes`, with the rule that disagreement inputs must be outcome-blind bounds, declared assumptions, or dedicated outcome-blind precision constructs.
- F10 `permitted_evidence`, pin P-21 ("derived from the frozen Delta_eq"), and pin P-22 (post-`Delta_eq` preflight, outcome-blind disagreement inputs) were aligned. "Budget may never enlarge `Delta_eq`" is stated in the procedure itself.

**Correction 2 — F6 ↔ F10 cycle removed (MUST FIX):**
- P-11 (both in the F6 gate table and the pin register) now reads `UNRESOLVED / OWNER_DECISION_REQUIRED / MEASUREMENT_REQUIRED`, justified **only** by outcome-blind bank-construction / design-coverage adequacy evidence available by F6, with explicit "MUST NOT depend on the later F10 precision calculation" and "no exact resolution rule invented beyond v11". The old "coverage guard + precision preflight" resolution rule and the EV-09 permission at F6 were deleted; "F10 precision outputs" was added to P-11's forbidden evidence.
- F10's `normative_closed_inputs` and the new post-table block state that `B*`, `Q_CD`, geometry, and `H*` are already frozen at F10 and allocation cannot change them or their semantics.
- The DAG section gained an explicit bullet: no `F10 -> F6` edge exists.

**Correction 3 — secondary-block governance map (MUST FIX):**
- New dedicated **§8 "Secondary-block governance map"** covering all 16 v11 §21 blocks/panels (A-APP … E-WEIGHT), each with the seven required fields (`role`, `winner_eligible`, `activation_status`, `specification_gate`, `required_pre_outcome_artifact`, `open_pin_if_any`, `failure_status`), the v11 §16 new-block rejection rule verbatim, and an explicit statement that the map creates no new DGP detail, numeric value, or calibration pin (§26 stays at 32). Gates v11 §22 does not assign (E-BRIDGE, S-NEG, R-REV) are marked `OWNER_DECISION_REQUIRED` rather than guessed.
- F8's `freeze_object` now explicitly includes "the pre-outcome robustness/transfer law (v11 §22 F8 freeze object), kept separate from H*", and F8 procedure step 6 freezes that law.
- P-26 (gate table and register) now names its eligible evidence dependencies — R-REALISTIC, E-BRIDGE, CAL-SENS, genuine held-out/external evidence if available — with "none winner-defining" and dependence on the F8-frozen law.
- Downstream sections renumbered (STOP → §9, Reopening → §10, E-register → §11, counts → §12, status block → §13) with both internal cross-references fixed.

**Correction 4a — F3 threshold derivation:**
- The permissive "set thresholds from calibration distributions + owner sign" wording was replaced: the threshold **derivation rule** must be frozen (owner-signed) before any candidate-specific adequacy comparison used for generator selection, and may not be selected or adjusted after inspecting which candidate it favors. The literal three-line rule block was added after the F3 table; P-03's constraints and resolution method were updated accordingly. No threshold value was chosen.

**Correction 4b — STOP-16 recovery:**
- STOP-16 now covers "legacy **or premature outcome** information contaminates a calibration pin", classifies as `provenance_violation + gate_STOP for affected chain`, and a binding recovery block was added reproducing the mandated sequence — including "do not claim that simple re-derivation restores pristine preregistration", permanent contamination annotation, no silent erasure/overwrite of history, and explicit PI governance for any disposition.

Additionally, a **§0.5 revision log** records both the initial draft (with its old SHA256) and this correction pass — provenance only, no methodological content.

## 2. Old SHA256

```text
769ef8798d3082df192cc670175a0bee707538e0953b774273753fe31cc0a4e0
```

## 3. New SHA256

```text
b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280
```

## 4. Four corrections closed

**Confirmed** — all four items (F10 causal order; F6↔F10 cycle removal; secondary-block governance map incl. F8 law and P-26 dependencies; F3 derivation rule + STOP-16 recovery) are implemented as specified above.

## 5. No other methodological decision changed

**Confirmed.** The 32-item §26 inventory, F0–F12 gate order, signed-rho governance, class-size policy, `n_per_cluster` non-inheritance, A-APP winner role, canonical winner-ineligible role, BANK-SENS required status, F11/F12 separation, outcome firewall, 30 rejected rules, and reopening policy are all untouched. No v11 closed decision was reopened; no numeric value was introduced anywhere. The v11 source hash was re-verified before editing (`d136502f…` — exact match).

## 6. No calibration or outcome access

**Confirmed.** No calibration was run, no generator fitted, no bank created, no algorithm/CVI executed, no legacy or new performance result opened. Only the draft file was edited (plus a pre-edit snapshot copied to `G:/temp/`, outside the repository, solely to produce the diff below).

## 7. `git diff -- p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md`

Output: **empty** — the draft has never been committed (untracked), so git has no baseline to diff against. As substitute evidence, `git diff --no-index` against the pre-edit snapshot shows:

```text
1 file changed, 109 insertions(+), 23 deletions(-)   (25 hunks, 132 lines touched)
```

The full 37KB unified diff was displayed in-session and persisted to
`C:\Users\Neo\.claude\projects\G--PycharmProjects-pkp-worktree\b800288b-637c-4206-9aff-fe894d0b09e7\tool-results\bwc04rfsc.txt`; every hunk corresponds to one of the changes enumerated in item 1.

## 8. `git status --short` (at end of correction task)

```text
?? p_konum_plus/calibration/
?? p_konum_plus/provenance/calibration_protocol_v0_drafting_report_2026-08-28.md
```

Nothing staged, nothing committed, no freeze sidecar created, no legacy file touched.

## 9. Final verdict

```text
READY_FOR_F0_EXECUTION_AUDIT
```
