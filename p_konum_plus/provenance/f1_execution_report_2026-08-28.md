# p_konum_plus — F1 Calibration Inputs Execution — End-of-Task Report

- **Report type:** F1 execution report (inventory + structural audit + owner-decision gate; NO F2, NO generator fit, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `a26098a4eac480a4156d8acfa9783954f007fb26`
- **Subject artifacts:**
  - `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` (ART-F1) — SHA256 `3b0e046da87b265f2a9100b045af4de6116c7ced362f92b0e929b32cd4fb4456`
  - `p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv` — SHA256 `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac`
- **Governing sources (verified exact this task):** v11 `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` · v0 `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` · ART-F0 `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8`

---

## 1. Repository/hash precheck — PASS

Root `G:/PycharmProjects/pkp-worktree` ✓ · branch `p_konum_plus` ✓ · HEAD `a26098a4eac480a4156d8acfa9783954f007fb26` (expected prefix `a26098a` ✓) · tree clean at start. Governing hashes recomputed, all exact: v11 `d136502f…`, v0 `b6b4ed83…`, ART-F0 `56fa5093…`.

## 2. Candidate SSA sources discovered

- **Primary:** `data/raw/names-usa/national-data/yob1880.txt … yob2025.txt` — 146 SSA national per-year raw files.
- **Secondary (scope = owner):** 51 state + 2 territory files under `data/raw/names-usa/`.
- **Derived:** `data/preprocessed/usa/names_usa_nation.parquet` and `names_usa_states.parquet`.
- **Documentation:** 3 SSA ReadMe PDFs — hashed, never opened.
- **Out of scope:** 12 Türkiye (TUIK) name files (non-SSA), `usa_states_geo.parquet` (not name data).

## 3. Structural facts (credible candidates)

**National set:** years **1880–2025 contiguous (T=146)**, 2,180,704 rows, sexes {F, M} present in all 146 years, 0 duplicate keys, 0 missing, 0 nonfinite, `count_min = 5` (SSA suppression floor observed), `count_max = 99,693`; unique names F=72,322, M=45,466; per-year-sex totals derivable in-file (1880: F=90,994/M=110,490 → 2025: F=1,607,267/M=1,708,076). Coverage over the full axis — F: 435 full, 663 ≥95%, 810 ≥90%, 1,197 ≥80%, 3,484 ≥50%; M: 471 / 675 / 806 / 1,229 / 2,977. Constant trajectories (≥2 observed years): F=4,160, M=2,609.
**State/territory:** 53 files, 6.72M rows, support starts 1910+ (max 2024/2025).
**Nation parquet:** shape (2,180,704×4); after reversing its documented recode (`sex→gender`, `F→female`, `M→male`) it equals the raw concatenation **exactly at full key level** (0 unmapped values). Builder identified: `notebooks/data-preprocessing-usa.ipynb` (`to_parquet` + `names_usa_nation`); consumer: `modules/usa/baby_names_usa_nation.py`. States parquet adds derived `total_count`/`rank` — verification deferred.

## 4. Files created (exactly two)

- `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` (ART-F1, sections 0–13)
- `p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv` (217 rows, required fields, no outcome fields)

## 5. Artifact SHA256

```text
f1_input_freeze_record_2026-08-28.md  = 3b0e046da87b265f2a9100b045af4de6116c7ced362f92b0e929b32cd4fb4456
f1_input_hash_table_2026-08-28.csv    = aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac
```

## 6. Provisional input set — NON-FROZEN

The 146 national `yob*.txt` files are the provisional primary candidate (all hashed); the nation parquet is a lineage-resolved alternative input-of-record; state/territory files are provisional secondary pending scope. **Nothing is frozen** — owner decisions remain.

## 7. Owner decisions required

**OD-1** source scope (national vs +state/territory) · **OD-2** input-of-record form (146 raw files vs verified parquet) · **OD-3** trajectory value (count vs per-year-sex share vs other) · **OD-4** time axis (A: 1880–2025 vs B: 1910–2024 vs justified truncation) · **OD-5** eligibility rule · **OD-6** missing-year handling · **OD-7** suppression interpretation (absence = censored <5 vs zero) · **OD-8** operation order · **OD-9** pre-normalization transform · **OD-10** z-normalization convention (centering, ddof, zero-variance, nonfinite, order).

## 8. Options with structural consequences (outcome-blind only)

Recorded per decision in ART-F1 §5–§8 and §12. Key numbers: axis A (T=146): full-coverage F=435/M=471; axis B (T=115): full-coverage F=785/M=874, ≥90% F=1,371/M=1,584. Coverage-threshold ladders per sex as in item 3. Suppression floor = 5 makes absence censored, which couples OD-5/6/7. Constant trajectories exist (4,160 F / 2,609 M), so the zero-variance z-norm rule is not vacuous. No clustering/CVI consequence was computed for any option.

## 9. Excluded/ambiguous files

Excluded from content inspection: everything under `results/` (rule; nothing there was needed), 3 ReadMe PDFs (hash custody only), 12 Türkiye files (non-SSA), geo parquet (not name data). **No file needed `AMBIGUOUS_FIREWALL_RISK / DO_NOT_OPEN`.** One notebook (`data-processing-usa-nationwide-missing-names.ipynb`) is recorded reference-only, role not established — moot since parquet lineage was proven by direct content comparison.

## 10. Firewall confirmation

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
generator_fit = false
F2_started = false
```

Also: no eligibility threshold chosen, no historical count (39/57) used as target, no legacy preprocessing inherited — every open choice routed to the owner.

## 11. F1 QC

13-row QC table in ART-F1 §11: rows 1–12 all **PASS** (hashes, precheck, outcome-blind discovery, 217 hashed rows, 3/3 hash-stability sentinels, clean national structure, lineage resolved, no silent selections, exactly two artifacts, firewall intact); row 13 gate closure = **OPEN** pending OD-1..OD-10.

## 12. `git status --short --untracked-files=all` (at end of F1 task)

```text
?? p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
?? p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
```

Exactly the two F1 artifacts, untracked and uncommitted. (Audit scripts ran from the OS temp directory, outside the repository.)

## 13. Verdict

```text
F1_OWNER_DECISION_REQUIRED
```

This is the expected outcome, not a failure: the raw inventory, hashing, structural audit, and lineage audit are complete; v11 genuinely leaves OD-1..OD-10 to the PI. `F1_complete = false`, `F2_allowed = false`, outcome firewall intact.
