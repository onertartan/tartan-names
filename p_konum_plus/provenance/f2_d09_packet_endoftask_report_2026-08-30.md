# p_konum_plus — D-F2-09 Exact Initialization Decision Packet — End-of-Task Report

- **Report type:** D-F2-09 decision-packet task report (NO ratification, NO r2, NO feasibility, NO real-SSA fit, NO F3)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-30
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`
- **Created artifacts:**
  - `p_konum_plus/calibration/f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md` — SHA256 `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6`
  - `p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv` — SHA256 `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666`
- **Governing context:** ART-F2 r1 `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7` (unmodified) · MERGED_FINAL worksheet `7f61eab892e7b85d9437777ffd578a04a905bb84d01103b1bfd8a6e1d94c0f0d` (non-normative recommendation context; PI ratification absent)

---

## 1. Repository / precheck result — PASS

Root `G:/PycharmProjects/pkp-worktree` ✓, branch `p_konum_plus` ✓, HEAD = expected `3e4daf47018f124e29717263e4e45fe90c8e52b8` ✓, zero tracked modifications, log shows the expected governance chain. Both target output paths were verified **absent** before creation — no overwrite occurred. Nothing deleted/reset/stashed.

## 2. Governing hash result — all 8 exact

v11 `d136502f…` · v0 `b6b4ed83…` · ART-F0 r2 `56fa5093…` · ART-F1 r4a `5eceb198…` · F1 eligible manifest `8a6034eb…` · F1 input hash table `aa86f1ea…` · ART-F2 r1 `d6f4aaf1…` · MERGED_FINAL worksheet `7f61eab892e7b85d9437777ffd578a04a905bb84d01103b1bfd8a6e1d94c0f0d`. No STOP.

## 3. Untracked list before outputs (exact)

```text
?? p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md
?? p_konum_plus/provenance/f2_d09_exact_enumeration_packet_2026-08-30.md
?? p_konum_plus/provenance/f2_owner_decision_packet_report_2026-08-29.md
?? p_konum_plus/provenance/f2_reconciliation_source_check_report_2026-08-29.md
?? p_konum_plus/provenance/f2_worksheet_updated3_verification_report_2026-08-29.md
```

(The `f2_d09_…` provenance note is the earlier informal draft; the new packet explicitly supersedes its recommendations — it used partly non-rule-generated anchors — and it remains untouched as historical provenance.)

## 4. P-01 proposed exact enumeration (summary)

Locations: rule-generated quarter-window lattice `A_loc = {−1 + i/4 : i = 0..12}` (13 anchors, endpoints included); all ordered pairs `c_r ≤ c_d` → **91 pairs** (`c_r = c_d` allowed: zero-plateau starts). Steepness: geometric 3-point lattice `K = {4, 22.577778941738334, 127.43902548550072}` (endpoints + geometric midpoint of the conditional `[k_min, k_max]`); asymmetry via full cross product `(k_r,k_d) ∈ K×K` (9 combos; ratios {1, 5.64, 31.86} both directions). Bounds + Kural T hold **by construction** (verified numerically anyway).

## 5. P-02 proposed exact enumeration (summary)

Same 13-anchor m-lattice; β = geometric 3-point `{1.0, 2.449489742783178, 6.0}` on [1,6]; scales = β-conditional geometric 3-point on `[s_side_min(β), 3.0]` with the exact-formula lower endpoint (Kural-T face by construction) — exact lattices listed per β (e.g., β=1: {0.01569377976942823, 0.21698234791863757, 3.0}); asymmetry via `(s_l,s_r) ∈ S(β)×S(β)`.

## 6. Fixed-grid counts (derived, double-run identical)

| stage | P-01 | P-02 |
|---|---|---|
| raw | 819 | 351 |
| after bounds + Kural T | 819 (by construction) | 351 (by construction) |
| after Kural S (n_min = 3, stabilized) | **731** | **261** |
| duplicates | 0 | 0 |
| Kural-S rejections (logged with reasons) | 88 | 90 |

## 7. Feature-based start (symbolic rule)

`j* = min{j : x_j = max_k x_k}`, `u* = j*/145`; P-01 → `(u*−1/8, u*+1/8, 22.577778941738334, 22.577778941738334)`; P-02 → `(u*, 0.32057672965544004, 0.32057672965544004, 2.449489742783178)` — every constant is a lattice midpoint or half-step (rule-tied, zero free numbers). Invalid start → `FEATURE_START_REJECTED`, grid-only, **no clipping**. +1 per family per trajectory as a rule (per-trajectory dedup may reduce to +0). Executable on a synthetic vector (demo: j*=90, both constructions valid).

## 8. Retry/fallback recommendation

**Option A** — no new retry starts; one predeclared CLASS_C fallback optimizer reuses the identical deterministic start set on purely numerical errors; then `FAMILY_FIT_FAILURE(code)`. Smallest contract; no model-only argument requires Option B. Optimizer brand/tolerances remain CLASS_C, never a scientific pin. Boundary policy: **no separate boundary starts** — lattice endpoints already cover every face; degenerate corners enter only if they mechanically survive Kural S (the 88+90 rejections are precisely those corners).

## 9. Dedup / tie rules

Dedup: canonical orders `(c_r,c_d,k_r,k_d)` / `(m,s_l,s_r,β)`; exact float64 tuple equality (tolerance unnecessary — single exact construction path); first-in-sort retained; output ascending lexicographic, no unordered sets. Objective ties (CLASS_C): tie iff `|L_a−L_b| ≤ 1e−12 + 1e−9·max(|L_a|,|L_b|)`; lexicographic smallest tuple wins. Comparator determinism verified. No historical convention imported.

## 10. PI decision table

**D-F2-09.1** location lattice Δu=1/4 (alts: 1/2, 1/8) · **.2** geometric-3 K×K (alts: 5-point, base×ratio) · **.3** m-lattice × β={1,√6,6} · **.4** β-conditional geometric-3 scale lattice · **.5** feature-start rule + reject-if-invalid (alt: omit) · **.6** lattice-face-only boundary policy (alt: explicit face list) · **.7** retry Option A (alt: B) · **.8** exact-equality dedup + lexicographic order · **.9** tie comparator literals · **.10** derived-count semantics (731/261 + feature rule; regenerate on any invalidation trigger). Each carries recommendation, alternatives, consequences, family-altering flag (all "no — reproducibility contract only"), and `status = OWNER_DECISION_REQUIRED`. No PI approval filled.

## 11. Files created (exactly two)

- `p_konum_plus/calibration/f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md` (18 sections 0–17 per spec)
- `p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv` (1,170 deterministic sorted rows — retained *and* rejected with reasons; full-precision values; fixed-grid only, feature start symbolic; no real trajectory identifiers)

## 12. SHA256 of both files

```text
packet   = 8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6
manifest = c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666
```

## 13. Confirmation

```text
ART_F2_r2_started = false
PI_ratification = false
fit_feasibility_execution = false
real_SSA_fit = false
F3_started = false
```

(Also: no `results/` access, no pre-v11 tie-break text used, no recovery scores/rates, `rng_used = false`, ART-F2 r1 unmodified — hash re-verified.)

## 14. `git status --short --untracked-files=all` (at end of task)

```text
?? p_konum_plus/calibration/f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md
?? p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv
?? p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md
?? p_konum_plus/provenance/f2_d09_exact_enumeration_packet_2026-08-30.md
?? p_konum_plus/provenance/f2_owner_decision_packet_report_2026-08-29.md
?? p_konum_plus/provenance/f2_reconciliation_source_check_report_2026-08-29.md
?? p_konum_plus/provenance/f2_worksheet_updated3_verification_report_2026-08-29.md
```

Nothing staged, nothing committed.

## 15. Verdict

```text
D-F2-09_EXACT_DECISION_PACKET_READY
```

Terminal state as expected: `D-F2-09_status = OWNER_DECISION_REQUIRED`, `D-F2-09_exact_packet = READY`, `F2_status = OWNER_DECISION_REQUIRED`, `F2_complete = false`, `F3_allowed = false`. Once the PI ratifies D-F2-09.1–.10 together with the other recommended selections, STEP 1 (ART-F2 r1 → r2 with C1–C10 + R1–R4) can run.
