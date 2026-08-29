# p_konum_plus — F1 Owner-Decision Refinement Audit — End-of-Task Report

- **Report type:** F1 refinement report (national-only scope fixed; missingness/suppression/eligibility refinement; NO F2, NO generator fit, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `a26098a4eac480a4156d8acfa9783954f007fb26`
- **Subject artifact:** `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` (ART-F1)
  - r1 SHA256: `3b0e046da87b265f2a9100b045af4de6116c7ced362f92b0e929b32cd4fb4456`
  - r2 SHA256: `667801dcbd93135e7e8bdfb2a14c6b191cf0244acbe4bdb06acc2c1531667b17`
- **Companion CSV (unchanged):** `p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv` — `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac`
- **Governing sources (verified exact this task):** v11 `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` · v0 `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` · ART-F0 `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8`

---

## 1. Governing-hash / repository precheck — PASS

Root ✓, branch `p_konum_plus` ✓, HEAD `a26098a4eac480a4156d8acfa9783954f007fb26` (unchanged, accounted for), only the three known F1-era untracked files present. Hashes exact: v11 `d136502f…`, v0 `b6b4ed83…`, ART-F0 `56fa5093…`, ART-F1 r1 `3b0e046d…`, CSV `aa86f1ea…`.

## 2. OD-1 confirmed

`OD-1 = national_only`, recorded as **RESOLVED_BY_PI (CLOSED)**. State/territory files are `excluded_from_primary_F1_scope` (provenance only) and no longer influence the time axis, eligibility, missingness, representation, or counts. The former "1910–2024 state-compatible" axis variant is removed as an independent justification.

## 3. NationalReadMe source semantics

Scope = U.S. births with an SSN, tabulated "as of March 2, 2025"; format `name,sex,number`, names 2–15 chars; **documented privacy rule: only names with ≥5 occurrences are published**. Therefore absent `(year,sex,name)` = **below-publication-rule censoring (true value 0–4, or non-representable name), NOT observed zero**. No early-year completeness caveat exists in the local ReadMe. Source semantics vs analysis treatment are recorded separately.

## 4. National missingness topology (1880–2025, T=146)

| category | F | M |
|---|---|---|
| FULL | 435 | 471 |
| BOUNDARY_ONLY_LEFT_MISSING | 2,968 | 2,135 |
| BOUNDARY_ONLY_RIGHT_MISSING | 2 | 1 |
| BOUNDARY_BOTH_MISSING | 2,862 | 1,424 |
| INTERNAL_GAPS_PRESENT | 50,309 | 31,695 |
| SINGLETON_OR_TOO_SHORT (n_obs = 1) | 15,746 | 9,740 |

DATA-QC categories only — explicitly not W-L/W-I/W-R.

## 5. Eligibility-family structural consequences (no rule chosen)

E1 (full support): F=435, M=471, clean. E2 (no internal gaps): F=22,013, M=13,771 — but median observed years = 1 (dominated by singletons: 15,746 F / 9,740 M) and ~98% boundary-missing, a key structural fact. E4 ladders: ≥0.95 → 663 F / 675 M; ≥0.90 → 810 / 806; ≥0.80 → 1,197 / 1,229, with boundary/internal-gap fractions and max-gap distributions recorded. E3 diagnostics among gap-bearing trajectories: ladders at max_gap ≤1/2/3/5 and runs ≤1/2 (e.g., F: 8,163 / 15,955 / 22,198 / 31,156), limits not chosen.

## 6. Released-record-share QC — PASS

292/292 (year,sex) groups: minimum denominator 90,994 (>0); **max |Σshares − 1| = 0.0** (tolerance 1e-9); zero negative, zero nonfinite. Semantics recorded as `share_among_published_SSA_records_for_that_year_and_sex`; `true_birth_probability` / `true_population_share` labels forbidden.

## 7. Final-representation zero-variance counts

On FULL trajectories under the share transform (raw-count constancy not used as substitute): **F: 435 full, 0 zero-variance, 0 nonfinite; M: 471 full, 0 zero-variance, 0 nonfinite.** The proposed OD-10 zero-variance rule is currently vacuous on E1 — uncontradicted.

## 8. Early-year / edge qualification

Local official documentation contains **no early-year limitation** — no documented basis for left truncation (none imported from external sources). One flagged `data_source_limitation`: the ReadMe's 2025-03-02 tabulation date is inconsistent with the full-year-scale `yob2025` (3.32M vs 3.33M in 2024) — the bundled ReadMe predates the data vintage, raising a right-edge (final-year accrual) question for OD-4. Not a STOP; data files are internally consistent and hash-stable. No automatic truncation performed.

## 9. Reduced owner-decision register

OD-1 **RESOLVED_BY_PI** · OD-2, OD-3, OD-9, OD-10 **PROPOSED_BY_PI, uncontradicted by audit** · OD-4 **OPEN** (default full 1880–2025; right-edge question documented) · OD-5 **OPEN** · OD-6 **OPEN** · OD-7_source_semantics **DATA_SOURCE_DETERMINED** · OD-7_analysis_treatment **OPEN** (T1–T5 characterized; T3 zero-fill noted as contradicting documented censoring semantics — descriptive fact) · OD-8 **OPEN** (canonical chain recorded). No new OD numbers.

## 10. Exact ART-F1 changes

Full r2 revision of `f1_input_freeze_record_2026-08-28.md`: §0 revision block (r1 hash preserved); §2/§4/§9.2 scope+role updates (state/territory excluded, parquet = `mechanically_verified_operational_cache_only`); new §3.4 NationalReadMe semantics incl. vintage observation; §3.1 adds per-year floor check (146/146 = 5) and right-edge totals 2021–2025; §5 rebuilt (topology + E1–E4 + E3 ladders); §6 rewritten national-only (state-compat justification removed, OD-4 restated); §7 adds T1–T5 table and OD-8 chain; §8 adds the zero-variance audit; §9.1 share QC; §11 QC re-run (12 PASS + gate OPEN); §12 reduced register; §13 status. F1 **not** marked COMPLETE.

## 11. Revised ART-F1 SHA256 (r2)

```text
667801dcbd93135e7e8bdfb2a14c6b191cf0244acbe4bdb06acc2c1531667b17
```

## 12. Companion CSV SHA256 — unchanged

```text
aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac
```

No inventory/hash error was found, so the CSV was not touched.

## 13. Firewall confirmation

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
generator_fit = false
generator_adequacy = false
Q_CD_created = false
B_star_created = false
H_star_created = false
F2_started = false
```

## 14. `git status --short --untracked-files=all` (at end of refinement task)

```text
?? p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
?? p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
?? p_konum_plus/provenance/f1_execution_report_2026-08-28.md
```

Same three untracked F1-era files; nothing staged or committed.

## 15. Verdict

```text
F1_OWNER_DECISION_PACKET_REFINED
```

No provenance/source contradiction rose to STOP; the single flagged item (ReadMe vintage vs `yob2025`) is recorded as a `data_source_limitation` feeding OD-4. Remaining for the PI: OD-4, OD-5, OD-6, OD-7_analysis_treatment, OD-8 — then a short F1 freeze pass can close the gate.
