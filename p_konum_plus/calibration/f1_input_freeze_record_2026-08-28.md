# ART-F1 — Calibration Input Freeze Record (F1) — FINAL (r4a)

## 0. Artifact identity

```text
artifact_id         = ART-F1
artifact_role       = calibration_input_freeze_record
normative_authority = v11_only
gate                = F1
date                = 2026-08-28
worktree            = G:/PycharmProjects/pkp-worktree
branch              = p_konum_plus
HEAD_at_execution   = a26098a4eac480a4156d8acfa9783954f007fb26
record_revision     = r4a_provenance_cleanup_2026-08-28
r1_sha256           = 3b0e046da87b265f2a9100b045af4de6116c7ced362f92b0e929b32cd4fb4456
r2_sha256           = 667801dcbd93135e7e8bdfb2a14c6b191cf0244acbe4bdb06acc2c1531667b17
r3_sha256           = 0f0542f58cb409c4b5d02ec4efd5f9726ab83204abbe9d2ab747c0d73ee27082
r4_sha256           = d44075385634bdd16d76d85ddb9aa3876013c5235867d0edf4d06bc12dfa079c

F1_status           = COMPLETE
F1_complete         = true
F2_allowed          = true
```

Companion artifacts:

```text
p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
  sha256 = aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac  (unchanged since r1)

p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv
  rows = 906; sha256 = 8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32
```

r4a changes provenance/metadata only.
No scientific F1 decision or data-derived result changed.

This record is an execution artifact derived from v11 (`v11_wins = true`); it
is not an independent methodology authority. **F1 completion does NOT freeze
the project methodology** — the project-wide freeze and external `.sha256`
sidecar remain F12-only, and `methodology_contract_status = draft_pre_F12`.

## 1. Governing-source hash verification (re-verified in this freeze pass)

| document | SHA256 | result |
|---|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | PASS |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` | PASS |
| ART-F0 (r2) | `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` | PASS |
| ART-F1 r4 (pre-cleanup state) | `d44075385634bdd16d76d85ddb9aa3876013c5235867d0edf4d06bc12dfa079c` | PASS |
| f1_input_hash_table | `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac` | PASS (not modified; no inventory error found) |

Repository precheck: root/branch correct, HEAD `a26098a4…`, no unexpected
files beyond the known untracked F1-era artifacts/reports.

## 2. Frozen primary F1 contract (PI decisions, all CLOSED)

```text
OD-1_source_scope            = national_only
OD-2_source_of_record        = 146_raw_national_yob_files (yob1880.txt .. yob2025.txt)
                               names_usa_nation_parquet_role = mechanically_verified_operational_cache_only
OD-3_trajectory_value        = released_record_share_by_year_and_sex
                               released_record_share(name,sex,year) =
                                 published_count(name,sex,year)
                                 / sum_over_published_names published_count(.,sex,year)
                               semantics = share_among_published_SSA_records_for_that_year_and_sex
                               forbidden labels: true_birth_probability, true_population_share
OD-4_time_axis               = 1880..2025, T = 146
OD-5_primary_eligibility     = FULL_observed_support_on_1880_2025
                               (n_observed_years = 146, n_missing_total = 0,
                                duplicate_year = false, nonfinite_source_value = false)
OD-6_missing_year_treatment  = complete_support_restriction; primary_missing_value_imputation = none
                               (zero_fill = false; interpolation = false;
                                censor_aware_primary_input = false;
                                boundary_retention_without_imputation = false)
OD-7_source_semantics        = absent_valid_national_record_is_unpublished_under_SSA_disclosure_privacy_rules
OD-7_primary_analysis_treatment = exclude_via_complete_support_eligibility
OD-8_operation_order         = frozen 11-step chain (section 8.1)
OD-9_additional_pre_z_transform = none
                               (count -> released_record_share is the value definition itself;
                                no log/log1p/Box-Cox/rank/smoothing/interpolation)
OD-10_z_normalization        = centering: arithmetic_mean; scale: population_standard_deviation (ddof = 0);
                               nonfinite_rule = QC_failure;
                               zero_variance_rule = ineligible_or_QC_failure_before_normalization;
                               z_t = (x_t - mean(x)) / std_ddof0(x)
```

OD-4 rationale (recorded): national support is contiguous with both sexes in
every year; national-only scope removes any state-compatibility truncation
rationale; documented historical SSA-record limitations are carried as source
limitations, not converted into a cutoff; 2025 is not removed merely because
the bundled ReadMe snapshot predates the data vintage. This period is NOT
claimed to be a complete census of all U.S. births.

OD-5 consequence (audited, not a target): `eligible_F = 435`,
`eligible_M = 471`. `primary_calibration_selection =
persistent_fully_published_SSA_trajectories`;
`generalization_to_suppressed_shorter_or_intermittent_trajectories =
not_implied_by_primary_calibration`. Eligibility was not tuned to any
historical count.

## 3. Source semantics — final rule (r4-corrected)

The local NationalReadMe documents: national scope = U.S. births where the
individual has an SSN; per-year files `name,sex,number`; names 2–15
characters; "To safeguard privacy, we restrict our list of names to those
with at least 5 occurrences."

This establishes the forward implication only:

```text
published => count >= 5

NOT established:
unpublished => count <= 4
```

Current SSA privacy/disclosure practice allows names to be omitted where
publication could reveal or permit inference of low-frequency information, so
absence does not identify the unpublished count. For a valid SSA national
name-record key `(year, sex, name)` within the documented representation
domain, the frozen semantics are:

```text
OD-7_source_semantics            = absent_valid_national_record_is_unpublished_under_SSA_disclosure_privacy_rules
observed_zero                    = false
exact_unpublished_national_count = not_identified_from_the_published_national_file
minimum_observed_published_count = 5
```

`missing != zero`; no hidden count is imputed, and missingness is NOT
characterized as `[0,4]` interval censoring. The semantic universe is the
**SSA national record system**, not the complete census of all U.S. births;
these semantics are not applied to arbitrary strings outside the documented
representation domain (2–15 characters, national file rules). Observed floor
check: minimum published count = 5 in 146/146 years — consistent with the
documented forward rule.

Early-year qualification (officially documented in current SSA
documentation; provenance in §4):

```text
pre_1937_source_limitation =
  many persons born before 1937 never obtained a Social Security card,
  so SSA records are not a complete census of all U.S. births

data_source_limitation = true
algorithm_outcome      = false
```

The `SSA_record_series` is distinct from a `complete_census_of_all_US_births`.
The project claim remains about the frozen SSA-calibrated design (v11 claim
boundary), so no time-axis truncation follows from this limitation and
`OD-4_time_axis = 1880..2025` is unchanged.

## 4. Source-documentation provenance

```text
bundled_NationalReadMe            = local_source_document_snapshot
bundled_NationalReadMe_status     = older_documentation_snapshot
  (its tabulation date 2025-03-02 predates the data vintage: yob2025.txt is
   full-year scale — 3.32M total vs 3.33M in 2024 — with the standard format
   and the standard floor of 5)

current_official_SSA_documentation = independently_verified_outside_Claude_Code
  in_task_access_attempt = https://www.ssa.gov/oact/babynames/limits.html and
                           /background.html on 2026-08-28 -> HTTP 403
                           (no content retrieved inside this environment; recorded honestly)
  external_verification  = independent external review outside Claude Code using
                           official SSA webpages; findings supplied to Claude Code
                           on 2026-08-28

current_SSA_record_vintage           = March_2026
birth_year_2025_officially_supported = true
yob2025_release_status               = officially_supported_current_national_source
                                       (also mechanically consistent: contiguous file series,
                                        identical format, per-year floor = 5,
                                        full-year-scale totals)
right_edge_2025_blocker              = false
```

This is a documentation-vintage difference, NOT a data contradiction: the raw
files are internally consistent and hash-stable; the bundled ReadMe was not
rewritten.

## 5. Inventory, lineage, and scope (final)

- Source of record: the 146 national `yob*.txt` files (SHA256 per file in
  `f1_input_hash_table_2026-08-28.csv`, unchanged since r1; stability
  sentinels re-verified in r1).
- `names_usa_nation.parquet`: operational cache only; verified
  content-identical to the raw concatenation at full key level after
  reversing its documented recode (`sex→gender`, `F→female`, `M→male`).
- State/territory files (53) and their parquet: `excluded_from_primary_F1_scope`
  (OD-1); retained as discovered SSA provenance only; they influence no
  primary determination.
- StateReadMe/TerritoryReadMe: hash custody only. Türkiye files, geo parquet:
  not candidates.

## 6. Structural audit summary (national, frozen axis)

1880–2025 contiguous (T=146); 2,180,704 rows; both sexes present in all 146
years; 0 duplicate `(year,sex,name)` keys; 0 missing; 0 nonfinite; count
range 5..99,693 with per-year floor exactly 5 in all years; name lengths
observed 2..15 (matches documented format); per-year-sex denominators
90,994..1,748,237 (all > 0). Missingness topology and eligibility-family
diagnostics (decision support for the now-closed OD-5/OD-6) are preserved in
revision r2 (`r2_sha256` above) and summarized: FULL = 435 F / 471 M;
boundary-only = 5,832 F / 3,560 M; internal-gaps = 50,309 F / 31,695 M;
singletons = 15,746 F / 9,740 M.

## 7. Eligible-trajectory manifest (frozen)

```text
path            = p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv
manifest_scope  = eligible_trajectories_only        (explicit choice; the excluded
                  complement is reproducible from the frozen rule + hashed inputs)
ordering_rule   = ascending (sex, name), ASCII
rows            = 906  (F = 435, M = 471)
sha256          = 8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32
fields          = trajectory_id, sex, name, year_min, year_max, T, source_scope,
                  eligibility_rule_id, trajectory_value_id, source_record_status,
                  n_observed_years, n_missing_total, eligible, exclusion_reason
trajectory_id   = "<sex>_<name>" (natural key; deterministic)
eligibility_rule_id  = OD5_FULL_observed_support_1880_2025
trajectory_value_id  = OD3_released_record_share_by_year_and_sex
no algorithm/CVI fields
```

Non-full trajectories (all remaining `(sex,name)` pairs):

```text
primary_eligible = false
reason           = incomplete_published_support
unpublished_count_value = unknown_from_the_published_national_file  (never imputed at F1)
broader_unpublished_source_support =
  retained_for_later_winner_ineligible_calibration_sensitivity_governance
```

No censor-aware likelihood was chosen; no sensitivity analysis was
implemented (F11 territory).

## 8. Frozen preprocessing pipeline and QC results

### 8.1 Frozen operation order (OD-8)

```text
1.  source-format validation
2.  source-semantics validation
3.  enforce national-only source scope
4.  construct 1880-2025 annual trajectory index
5.  evaluate FULL-support eligibility using published-record presence
6.  retain only fully eligible trajectories
7.  compute released-record-share by year x sex
    (denominator = sum over ALL published names for that year & sex)
8.  denominator / duplicate / finite / nonnegative QC
9.  zero-variance QC
10. row-wise z-normalization (mean, std ddof=0)
11. post-normalization QC
```

The primary eligible set has `n_missing_total = 0`, so no imputation stage
exists.

### 8.2 QC tolerance (class-C implementation literal)

```text
post_z_tolerance = 1e-8
implementation_literal_only = true; scientific_effect = none
checks: finite(z); |mean(z)| <= tol; |std_ddof0(z) - 1| <= tol; | ||z||_2 - sqrt(146) | <= tol
The tolerance cannot alter scientific eligibility (a violation is a QC failure/STOP, never a re-tune).
```

### 8.3 QC results on the frozen eligible set (executed this pass)

| metric | F | M |
|---|---|---|
| n_eligible | 435 | 471 |
| n_failed_support_QC | 0 | 0 |
| n_failed_duplicate_QC | 0 | 0 |
| n_failed_denominator_QC | 0 | 0 |
| n_nonfinite_pre_z | 0 | 0 |
| n_negative_share | 0 | 0 |
| n_zero_variance | 0 | 0 |
| n_failed_z_mean_QC | 0 | 0 |
| n_failed_z_std_QC | 0 | 0 |
| n_failed_z_norm_QC | 0 | 0 |
| n_nonfinite_post_z | 0 | 0 |

Observed extremes vs tolerance: max |mean(z)| = 3.1e-15; max |std(z)−1| =
1.0e-15; max deviation of ‖z‖₂ from √146 = 1.2e-14 — all ≤ 1e-8.
Share QC over all 292 (year,sex) groups (r2, re-confirmed by construction
here): denominators > 0 (min 90,994), exact share sums (max |Σ−1| = 0.0),
no negative, no nonfinite. `ALL_QC_PASS = true`. Eligible counts recomputed
identically to the prior audit (435/471) — no silent eligibility change.

## 9. Firewall audit

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access      = false
generator_fit                     = false
generator_adequacy                = false
Q_CD_created                      = false
B_star_created                    = false
H_star_created                    = false
F2_started                        = false
results_directory_content_opened  = false
external_access                   = two SSA documentation URLs attempted (HTTP 403; no content);
                                    no performance/result source touched
```

## 10. F1 final QC checklist

| check | result |
|---|---|
| OD-1..OD-10 all resolved | PASS |
| source scope = national only | PASS |
| source of record = 146 raw national yob files | PASS |
| axis = 1880..2025, T = 146 | PASS |
| trajectory value = released_record_share | PASS |
| primary eligibility = FULL support; imputation = none | PASS |
| suppression semantics = absence unpublished under SSA disclosure rules; count not identified from the published file; not observed zero | PASS |
| z-normalization = mean + std ddof=0, frozen QC | PASS |
| eligible manifest deterministic (ordering rule recorded) and hashed | PASS |
| input hashes stable (hash table unchanged) | PASS |
| share QC passes | PASS |
| z-normalization QC passes | PASS |
| legacy outcome access = false; new outcome access = false | PASS |
| F2 not started | PASS |

## 11. Final owner-decision register

```text
OD-1  = CLOSED (PI)   national_only
OD-2  = CLOSED (PI)   146 raw national yob files; parquet = operational cache only
OD-3  = CLOSED (PI)   released_record_share_by_year_and_sex (published-records semantics)
OD-4  = CLOSED (PI)   1880..2025, T = 146
OD-5  = CLOSED (PI)   FULL observed support on 1880-2025 (consequence: 435 F / 471 M)
OD-6  = CLOSED (PI)   complete_support_restriction; no imputation
OD-7  = CLOSED        source semantics: absence = unpublished under SSA disclosure/privacy
                      rules (published => count >= 5; converse NOT established; count not
                      identified from the published file);
                      primary treatment (PI): exclude via complete-support eligibility
OD-8  = CLOSED (PI)   11-step operation order (8.1)
OD-9  = CLOSED (PI)   no additional pre-z transform
OD-10 = CLOSED (PI)   mean / population sd ddof=0 / nonfinite = QC_failure /
                      zero-variance = ineligible-or-QC-failure; post-z tolerance 1e-8 (class C)
```

Alternative treatments (T2–T5) are not declared scientifically invalid; they
are outside the primary F1 contract and may only enter later as
winner-ineligible sensitivity governance under F11 rules.

## 12. Gate closure

```text
F1_status                    = COMPLETE
F1_complete                  = true
F2_allowed                   = true
methodology_contract_status  = draft_pre_F12   (project-wide freeze requires F12 PI sign-off;
                                                no .sha256 sidecar created — F12-only)
outcome_firewall             = intact
next_gate                    = F2 (generator specification; separate task)
```

F1 scientific/governance artifact set: this record, the input hash table, and
the eligible-trajectory manifest. The F1 execution/refinement reports under
`p_konum_plus/provenance/` remain NON-NORMATIVE operational provenance.
