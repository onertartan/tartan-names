# p_konum_plus — F1 Final Owner Freeze Pass — End-of-Task Report

- **Report type:** F1 closure report (source-semantics finalization + PI decisions + gate closure; NO F2, NO generator fit, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `a26098a4eac480a4156d8acfa9783954f007fb26`
- **Subject artifacts:**
  - `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` (ART-F1 r3 FINAL) — SHA256 `0f0542f58cb409c4b5d02ec4efd5f9726ab83204abbe9d2ab747c0d73ee27082` (r1 `3b0e046d…`, r2 `667801dc…` preserved in lineage)
  - `p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv` — SHA256 `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` (906 rows)
  - `p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv` — unchanged, SHA256 `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac`
- **Governing sources (verified exact this task):** v11 `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` · v0 `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` · ART-F0 `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8`

---

## 1. Repository / governing-hash precheck — PASS

Root ✓, branch `p_konum_plus` ✓, HEAD `a26098a4eac480a4156d8acfa9783954f007fb26`, only known F1-era untracked files. All five hashes exact: v11 `d136502f…`, v0 `b6b4ed83…`, ART-F0 `56fa5093…`, ART-F1 r2 `667801dc…`, input hash table `aa86f1ea…`. Nothing normalized or rewritten.

## 2. Documentation / source-semantic findings

- `bundled_NationalReadMe = local_source_document_snapshot`, status `older_documentation_snapshot` (its 2025-03-02 tabulation date predates the data vintage; `yob2025` is full-year scale, format-identical, floor = 5).
- Current official SSA documentation: **access attempted 2026-08-28** (`limits.html`, `background.html`) — both returned **HTTP 403**, so `current_official_SSA_documentation = NOT_AVAILABLE`. Per the task rule, no alternative cutoff was invented; the vintage issue is recorded explicitly. `yob2025_release_status = mechanically_consistent_with_official_national_series`; `right_edge_2025_blocker = false` (PI decision + mechanical consistency). Vintage difference recorded as distinct from a data contradiction.
- Early-year limitation carried as `data_source_limitation = true, algorithm_outcome = false`, with `SSA_record_series` explicitly distinguished from a `complete_census_of_all_US_births`; no claim broadening, no truncation derived from it.

## 3. Suppression semantics confirmed

```text
absent valid national record -> exact latent SSA-record count unknown in {0,1,2,3,4}
```

`observed_zero = false`, `minimum_published_count = 5` (documented rule, observed in 146/146 years). Semantic universe = the SSA national record system; the [0,4] inference is not applied outside the documented representation domain (names 2–15 chars — observed range exactly 2..15).

## 4. OD-1..OD-10 final table — all CLOSED

OD-1 national_only · OD-2 146 raw yob files (parquet = verified operational cache only) · OD-3 released_record_share (published-records semantics; stronger labels forbidden) · OD-4 axis 1880–2025, T=146 · OD-5 FULL observed support · OD-6 complete_support_restriction, no imputation · OD-7 interval-censored [0,4] semantics + exclude-via-eligibility treatment · OD-8 frozen 11-step operation order · OD-9 no additional pre-z transform · OD-10 mean / population sd ddof=0 / nonfinite = QC_failure / zero-variance = ineligible-or-QC-failure, post-z tolerance 1e-8 (class-C literal, cannot alter eligibility).

## 5. Eligible counts (audited consequences, not targets)

**F = 435, M = 471** — recomputed this pass and identical to the prior audit (no STOP, no silent eligibility change).

## 6. Eligible manifest

`p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv` — **906 rows** (eligible-only scope, explicit; ordering rule: ascending (sex, name), ASCII; `trajectory_id = <sex>_<name>`), SHA256:

```text
8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32
```

## 7. Released-record-share QC — PASS

Denominators over all published names per (year,sex): all > 0 (min 90,994); shares finite, non-negative; no duplicate keys; exact sums (max |Σ−1| = 0.0 ≤ 1e-9); zero-variance occurrences: 0.

## 8. Z-normalization QC — PASS

Row-wise ddof=0 on all 906 eligible trajectories: every check zero-failure for both sexes; observed extremes max |mean(z)| = 3.1e-15, max |std(z)−1| = 1.0e-15, max |‖z‖₂−√146| = 1.2e-14 — six orders inside the 1e-8 tolerance. Full per-sex QC table (all 11 metrics, all 0 failures) embedded in ART-F1 §8.3. `ALL_QC_PASS = true`.

## 9. Source/data limitations retained in the record

(a) SSA-record-series vs complete-census distinction (early-year qualification, no truncation); (b) documentation-vintage lag of the bundled ReadMe with the 2025 right-edge accrual note (`right_edge_2025_blocker = false`); (c) suppression censoring [0,4] with non-full trajectories retained as `broader_censored_source_support = retained_for_later_winner_ineligible_calibration_sensitivity_governance` — no censor-aware likelihood chosen at F1.

## 10. Revised ART-F1 SHA256 (r3 final)

```text
0f0542f58cb409c4b5d02ec4efd5f9726ab83204abbe9d2ab747c0d73ee27082
```

(r1 `3b0e046d…` and r2 `667801dc…` preserved in the revision lineage.)

## 11. Input hash table — unchanged

```text
aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac
```

## 12. Files changed/created

Changed: `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` (→ r3 final). Created: `p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv`. Nothing else touched; no `.sha256` sidecar created (F12-only). Pipeline scripts ran from the OS temp directory outside the repo.

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

No result-directory content opened; the only external access was the two blocked SSA documentation URLs.

## 14. `git status --short --untracked-files=all` (at end of freeze pass)

```text
?? p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
?? p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv
?? p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
?? p_konum_plus/provenance/f1_execution_report_2026-08-28.md
?? p_konum_plus/provenance/f1_refinement_report_2026-08-28.md
```

Nothing staged, nothing committed.

## 15. Verdict

```text
F1_COMPLETE_READY_FOR_INDEPENDENT_AUDIT
```

`F1_status = COMPLETE`, `F2_allowed = true` — while the project methodology remains `draft_pre_F12` (no project-wide freeze; F12 PI sign-off still pending). Next gate: F2 generator specification, as a separate task.
