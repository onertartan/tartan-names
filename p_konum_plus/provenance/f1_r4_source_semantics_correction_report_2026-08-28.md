# p_konum_plus — F1 r4 Source-Semantics Correction — End-of-Task Report

- **Report type:** narrow F1 correction report (OD-7 source semantics only; NO F2, NO other OD change, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `a26098a4eac480a4156d8acfa9783954f007fb26`
- **Subject artifact:** `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` (ART-F1)
  - r3 SHA256 (pre-correction): `0f0542f58cb409c4b5d02ec4efd5f9726ab83204abbe9d2ab747c0d73ee27082`
  - r4 SHA256 (post-correction): `d44075385634bdd16d76d85ddb9aa3876013c5235867d0edf4d06bc12dfa079c`
- **Companions (unchanged):** eligible manifest `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` · input hash table `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac`
- **Governing sources (verified exact this task):** v11 `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` · v0 `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` · ART-F0 `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8`

Note: the single remaining `[0,4]` occurrence in ART-F1 r4 is the deliberate negation sentence ("missingness is NOT characterized as `[0,4]` interval censoring") — the recorded prohibition itself, not a residual claim.

---

## 1. Governing/hash precheck — PASS

Root ✓, branch `p_konum_plus` ✓, HEAD `a26098a4…`. All exact before editing: v11 `d136502f…`, v0 `b6b4ed83…`, ART-F0 `56fa5093…`, ART-F1 r3 `0f0542f5…`, eligible manifest `8a6034eb…`, input hash table `aa86f1ea…`. No STOP.

## 2. OD-7 wording removed (exact)

- `OD-7_source_semantics = absent_valid_national_record_is_interval_censored_in_0_to_4` (§2 contract and §3)
- the `0 <= latent_SSA_record_count <= 4` block and `exact_missing_count = unknown_within_0_to_4` (§3)
- "`missing implies latent SSA-record count in [0,4]`" and "the `[0,4]` inference is NOT applied…" (§3)
- `latent_missing_SSA_record_count in [0,4] (information retained, never imputed at F1)` and `broader_censored_source_support` (§7)
- QC row "suppression semantics = interval-censored [0,4]…" (§10) and the register line "DATA_SOURCE_DETERMINED interval-censored [0,4]" (§11)

## 3. OD-7 replacement wording (exact)

```text
OD-7_source_semantics            = absent_valid_national_record_is_unpublished_under_SSA_disclosure_privacy_rules
observed_zero                    = false
exact_unpublished_national_count = not_identified_from_the_published_national_file
minimum_observed_published_count = 5

published => count >= 5
NOT established: unpublished => count <= 4
```

Plus, in §7: `unpublished_count_value = unknown_from_the_published_national_file` and `broader_unpublished_source_support = retained_for_later_winner_ineligible_calibration_sensitivity_governance`. No hidden count is imputed; missingness is explicitly NOT characterized as [0,4] interval censoring. Primary treatment unchanged: `exclude_via_complete_support_eligibility`, no imputation of any kind.

## 4. OD-1/2/3/4/5/6/8/9/10 unchanged — CONFIRMED

None of those register entries, contract lines, the operation order, or the z-normalization convention were touched; the only edited passages are the seven OD-7/documentation items listed above. `OD-4_time_axis = 1880..2025` intact; the pre-1937 limitation is recorded as `data_source_limitation = true, algorithm_outcome = false`, reported, not converted into truncation.

## 5. Eligible counts unchanged — CONFIRMED

F = 435, M = 471. No data recomputation was needed or performed; eligibility rule and treatment untouched.

## 6. Eligible-manifest SHA256 unchanged

```text
8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32
```

## 7. Input-hash-table SHA256 unchanged

```text
aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac
```

## 8. New ART-F1 r4 SHA256

```text
d44075385634bdd16d76d85ddb9aa3876013c5235867d0edf4d06bc12dfa079c
```

Revision lineage preserved in §0: r1 `3b0e046d…`, r2 `667801dc…`, r3 `0f0542f5…`.

## 9. Files changed (exactly one)

`p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` — seven targeted edits: §0 revision metadata (→ r4, r3 hash added), §2 OD-7 contract line, §3 rewritten source-semantics section (forward-implication-only rule + officially documented pre-1937 limitation), §4 documentation provenance (in-task 403 attempt retained honestly + PI's external verification: `current_SSA_record_vintage = March_2026`, `birth_year_2025_officially_supported = true`, `right_edge_2025_blocker = false`; bundled ReadMe preserved as older snapshot, not rewritten), §7 unpublished-count wording, §10 QC row, §11 register line. `F1_status = COMPLETE`, `F1_complete = true`, `F2_allowed = true` retained; project methodology remains `draft_pre_F12`.

## 10. Firewall confirmation

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
generator_fit = false
F2_started = false
```

No data files opened, no result content touched, no sensitivity implemented, nothing committed.

## 11. `git status --short --untracked-files=all` (at end of correction task)

```text
?? p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
?? p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv
?? p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
?? p_konum_plus/provenance/f1_execution_report_2026-08-28.md
?? p_konum_plus/provenance/f1_final_freeze_report_2026-08-28.md
?? p_konum_plus/provenance/f1_refinement_report_2026-08-28.md
```

## 12. Verdict

```text
F1_R4_SOURCE_SEMANTICS_CORRECTED_READY_FOR_INDEPENDENT_AUDIT
```
