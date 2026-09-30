# p_konum_plus — F2 Reconciliation-Source Provenance Check — Report

- **Report type:** non-blocking provenance check (PI decision worksheet §1) + worksheet status; NO PI field filled, NO r2 started, NO F3 content touched
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-29
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`
- **Trigger document:** `Nihai_D-F2-01_12_PI_Karar_Calisma_Sayfasi_2026-08-29.md` (NON-NORMATIVE PI decision worksheet, supplied outside the repository)
- **Subject artifact:** ART-F2 r1 `p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md` — SHA256 verified exact `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7`

---

## Reconciliation-source check (worksheet §1) — AVAILABLE AND VERIFIED

- **Repo state:** HEAD unchanged `3e4daf47…`; ART-F2 r1 hash exact `d6f4aaf1…`; only the two expected untracked F2 files (`calibration/f2_generator_specification_record_2026-08-29.md`, `provenance/f2_owner_decision_packet_report_2026-08-29.md`).
- Both v11 §0.1 reconciliation sources were found under `C:\Users\Neo\Downloads\yeni_proje\v_11\` and **hash-verified EXACT**:
  - `chatgpt_ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md` = `3bd9e7cfdbdfe9358f91792db12447594d86956cd1c1b185552cb2da4d94b787` ✓ (local filename carries a `chatgpt_` prefix vs the ledger name — cosmetic; identity is by hash)
  - `claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md` = `29c073ba5105a14299a0ea9427d8443c1a29d40960f7fed355ef49b2bae67c5a` ✓
- Result: `reconciliation_source_check = available_and_verified`; used strictly as non-normative naming/candidate-specification provenance; `v11_wins` unchanged.

## Findings from the pattern search (WC-ADL / ADL / TAD / PSAT / WC-ALC)

1. **No mathematical definition exists in either source.** Both name the candidates exactly as v11 does — "WC-ADL ve TAD/PSAT" — with no acronym expansion and no stated TAD-vs-PSAT relation. This **supports the worksheet's D-F2-01 option A** (opaque project identifier, `acronym_expansion = not_asserted`, `TAD_vs_PSAT_relation = not_asserted`) and confirms the critique of r1's "dual historical labels" phrasing: there is no evidence of a historical dual-label relation, only a compound identifier.
2. **No material contradiction** with the drafted P-01/P-02 formulas — the sources contain no formula to contradict.
3. **One non-material provenance observation, returned to the PI for D-F2-07d:** the Claude TERMINAL synthesis (§4.3) describes the morphology family as "Tek **smooth** WC-ALC". A `β = 1` cusp peak in the P-02 draft is continuous but not smooth at the peak. v11 itself is silent on smoothness, so this is *not* a contradiction — but it is a documented pre-v11 design-intent datum favoring `β_min > 1` if the PI wants strict smoothness. Flagged for the D-F2-07d choice; nothing changed.
4. **F3-relevant provenance noted but NOT used:** the same source contains pre-v11 text about a pinned tie-break and cross-fit machinery. That is P-04/P-05 territory; per the firewall it was not analyzed or applied, only its existence recorded for the future F3 gate.
5. Incidental cross-confirmation: the synthesis's "z-norm ddof=0" matches the frozen F1 convention (provenance only).

## Worksheet status

Every `PI seçimi:` field (D-F2-01…12 and the 06a–d / 07a–e sub-decisions) is **blank**, and §4's signature summary is empty — so nothing is ratified, and per worksheet §6:

```text
F2_status   = OWNER_DECISION_REQUIRED
F2_complete = false
F3_allowed  = false
```

## Next steps (per worksheet §5, once the PI fills the fields)

1. **STEP 1** — apply the PI selections plus the C1–C10 cleanup list (revision lineage, search auditability, literature provenance table, underflow-wording corrections, RNG/retry spec, pin-ID schema, D-F2-11/12 registration, next-action rewording, non-binding interface label) as **ART-F2 r1 → r2** ratification pass.
2. **STEP 2** — F2 second-pass feasibility, synthetic/analytic fixtures only (D-F2-11 scope; no real-SSA fits, no family ranking).
3. **STEP 3** — F2 freeze pass, explicit closure.
4. **STEP 4** — only then can F3 open. Until closure: P-03/P-04/P-05 work, real-SSA adequacy fitting, and generator selection remain forbidden.

## Firewall

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
generator_fit = false
generator_adequacy_comparison = false
F3_started = false
PI_fields_filled_by_executor = false
```
