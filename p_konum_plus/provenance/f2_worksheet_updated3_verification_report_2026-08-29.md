# p_konum_plus — F2 PI Worksheet (UPDATED3) — Lineage and Decision-Support Verification Report

- **Report type:** mechanical verification of the PI decision worksheet UPDATED3 (lineage hashes + Kural T / Kural S support values); NO PI field filled, NO r2 started, NO F3 content touched
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-29
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`
- **Trigger document:** `Nihai_D-F2-01_12_PI_Karar_Calisma_Sayfasi_UPDATED3_2026-08-29.md` (NON-NORMATIVE PI decision worksheet, supplied outside the repository)
- **Subject artifact:** ART-F2 r1 — SHA256 verified exact `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7`

---

## Worksheet lineage — VERIFIED

The declared revision chain reproduces exactly from the local files:

| version | file | SHA256 | claim check |
|---|---|---|---|
| pre-UPDATED2 | `…UPDATED_2026-08-29.md` | `dc499da78f858a4f0ace9761584dc8735a287152d4c5266f84b130c10553952f` | ✓ matches UPDATED2's "önceki sürüm" |
| UPDATED2 | `…UPDATED2_2026-08-29.md` | `9ed70283fca7aab7859fd737fae42b2c958a112eb06b24de5132efe20687266c` | ✓ matches UPDATED3's revision note |
| **UPDATED3 (current)** | `…UPDATED3_2026-08-29.md` | `ff5fd6bd08a4fd9fc755beaafc7f640396517896f98f3f08937bfca76449ec8f` | recorded now for custody |

(The suffix-less first draft hashes to `728d7e2d6bd9567f4885747a50a87bc31e4d082ad72ddbb41de61a1d8ae6c997` — it precedes the UPDATED chain and is unreferenced by the lineage notes; benign.) Repo unchanged: HEAD `3e4daf47…`, ART-F2 r1 exact `d6f4aaf1…`, only the three known untracked F2-era files (`calibration/f2_generator_specification_record_2026-08-29.md`, `provenance/f2_owner_decision_packet_report_2026-08-29.md`, `provenance/f2_reconciliation_source_check_report_2026-08-29.md`).

## Kural T / Kural S decision-support numbers — INDEPENDENTLY CONFIRMED

Every support value in the worksheet was re-derived from scratch (model-only, stabilized evaluation, no data, no family comparison):

- **k_max = 2·ln9·145/w_min:** 2.2 yr → 289.6 (≈290), 5 yr → 127.4 (≈127), 10 yr → 63.7 (≈64) ✓
- **s_side_min(w_min=5, β):** β=1 → 0.0157, β=1.5 → 0.0227, β=2 → 0.0289, β=4 → 0.0521, β=6 → 0.0747 ✓ — and the formula round-trips: at `s = s_side_min` the branch's 10–90 width computes to exactly **5.0000 years** for every β tested, so the R4 mechanical derivation rule is sound.
- **Kural S (n_sup, stabilized log-sum-exp/softplus evaluation):** P-02 corner (m=2, s=0.02, β=6) → **1** ✓; P-01 (c_r=c_d=2, k=290) → **1** ✓; W-R example (m=1.3, s=0.5, β=2) → **31** ✓.

No discrepancy anywhere — the worksheet's "sayısal olarak doğrulanmıştır" claim is independently reproduced; `w_min_years` / `n_min` can be pinned with the derivation mechanics double-checked.

## Gate status — unchanged, awaiting PI entries

Every scientific `PI seçimi:` field is blank, so per worksheet §6: `F2_status = OWNER_DECISION_REQUIRED`, `F2_complete = false`, `F3_allowed = false`. Nothing was filled by the executor and no r2 work was started. R1–R4 are pre-marked **APPLY** but per worksheet §5 they execute *inside* STEP 1 (the r2 pass); the reconciliation-source custody copy into `provenance/nonnormative/` was therefore deliberately NOT performed early — it lands with the r2 record that documents it.

**Needed to fire STEP 1:** the 12 main selections (D-F2-01…12), the 9 sub-selections (06a–d, 07a–e; 07d with its three-part answer), and the two primitives `w_min_years` and `n_min`. If any 06/07 sub-decision selects **Option C**, STEP 0 (outcome-blind analytic geometry audit packet) runs first; otherwise STEP 0 is skipped and rule-derived numbers are recorded as `DERIVED_FROM_RATIFIED_RULE` in r2 (R4).

Then, per worksheet §5: STEP 1 = ART-F2 r1 → r2 correction + ratification including C1–C10 + R1–R4; STEP 2 = synthetic-only feasibility (D-F2-11 scope); STEP 3 = F2 freeze pass; STEP 4 = only after `F2_complete = true` may F3 open.

## Firewall

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
generator_fit = false
generator_adequacy_comparison = false
real_SSA_fit = false
F3_started = false
PI_fields_filled_by_executor = false
repository_writes_this_pass = this report only
```
