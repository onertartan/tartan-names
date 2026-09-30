# p_konum_plus — F3 STEP 1 r3 → r4 Exactness Correction Report

```text
artifact_role = bounded child-revision correction report
status        = NON-NORMATIVE
date          = 2026-09-05

parent =
f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md

parent_sha256 =
350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad

child =
f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md

child_sha256 =
5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad

scientific_generator_change = false
F2_reopening = false
new_methodology_review = false
solver_semantic_changes = 0

findings =
  D-P04-COMMON-SUPPORT-01
  F3-STEP1-FAILBRANCH-01
  F3-STEP1-C3-ACF-01
  F3-STEP1-C4B-SEPARATE-P04-01
  K-05

prior_PI_choice_overwrites = 0

new_PI_owned_rows =
  D-P04_COMMON_SUPPORT_FLOOR
  D-P04_COMMON_SUPPORT_FAILURE_ACTION
  D-C3-ACF-ESTIMATOR   (upstream pin absent — confirmed)

conditional_PI_exactness_dependencies =
  F3-STEP1-C4B-SEPARATE-P04-01
    (upstream SEPARATE-specific P04 rule absent — confirmed)
```

## 0. Execution-prompt lineage (provenance cleanup; recorded on PI instruction)

```text
execution_prompt =
Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md

execution_prompt_sha256 (observed, computed from the dispatched file) =
b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00

parent_prompt =
Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v3_2026-09-05.md

parent_prompt_sha256 (expected per PI; independently recomputed from the
local copy and observed EQUAL) =
2af677776b892806c0d912aa437db16e66e3ce231c45b11375a8587b1ddd5c38

related read-only comparison record =
Claude_Code_F3_STEP1_r3_to_r4_correction_prompt_comparison_2026-09-05.md
observed_sha256 =
afaae1eb69ccf56b8eceb2a3d3ec9e9d0b80b5221591640d9425e986ec9199d3

This is prompt-lineage provenance cleanup only:
scientific_change = false
methodology_change = false
PI_choice_change = false
F2_reopening = false
The v4 execution prompt was not modified or renamed.
```

## 1. Custody verification — all exact, no STOP

v11 `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` PASS ·
F2 FREEZE r1 `ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43` PASS ·
r3 parent `350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad` PASS
(re-verified byte-unchanged AFTER the r4 write). Historical r3 provenance
report `006f6c61…` retained per §1.1 quarantine: its r2→r3 custody, r3 SHA256,
F3-STEP1-PROV-03 closure and qualification provenance remain valid; its
then-current `GATE_SPECIFIC_BLOCKER = none / CONTRACT_EXACTNESS = PASS /
RATIFICATION_READY = true` statements are historical status only and are NOT
propagated into r4 (r4 header states RATIFICATION_READY = false pending
independent audit).

## 2. Upstream verification results (pre-edit inspections)

- **C3 ACF pin search** (v11, F2 FREEZE r1, r3, admissible lineage): the only
  occurrence is r3 §3-C3 "phi_i = |lag-1 sample autocorrelation|" — a prose
  label with no estimator convention. **F3-STEP1-C3-ACF-01 = CONFIRMED**
  (gate-specific blocker) → D-C3-ACF-ESTIMATOR PI row inserted (r4 §3-C3
  packet + §10 table row), with the mandated recommended/classical form, the
  two bounded alternatives, the binding zero-variance/undefined rule, and the
  required rationale (the rejected "residual mean generally nonzero" rationale
  is absent; the recorded rationale states mean(r) = 0 under the frozen
  full-grid z_ddof0 convention).
- **SEPARATE-specific D-P04 4b rule search** in r3: lines 196 (per-side
  gating, P03), 201 (per-side paired-valid sets V4L_s/V4R_s), 203 (per-side
  completeness), 417 (bounded-alternative listing). The P04 scalar bullet
  defines only the single-scalar (WORSE/MEAN-compatible) quantity. No
  side-combination rule exists, and none was inferred from "both sides pass".
  **F3-STEP1-C4B-SEPARATE-P04-01 = CONFIRMED** (conditional gate-specific
  blocker) → recorded as CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED
  in r4 §3-C4b and §9.2; no rule invented; no new PI row created; WORSE path
  not blocked.
- **D-P04 failure branch search** in r3: the only STOP/redesign branch is the
  no-family-passes-P03 branch (§9); no D-P04 common-support floor/failure
  language exists. **F3-STEP1-FAILBRANCH-01** therefore required the new
  PI-owned rows (not claimed as predeclared).

## 3. Corrections applied in r4 (exact changed regions, r3 → r4 line ranges)

```text
region 1  header/title: 1 ; 7-8 ; 11 ; 14 ; 17-24 -> 1 ; 7-8 ; 11 ; 14 ;
          17-39 (revision r4, parent r3 + sha, revision_reason findings,
          current_gate_state block incl. RATIFICATION_READY = false, lineage)
region 2  138 -> 154-212  §3-C3: estimator cross-reference bullet +
          D-C3-ACF-ESTIMATOR PI packet (recommended classical ACF, bounded
          alternatives (b)/(c), zero-variance/undefined rule, rationale,
          CLASS_C library-call deferral)
region 3  222 -> 297-307  §3-C4b: SEPARATE-specific P04 status bullet
          (conditional exactness dependency; no rule invention)
region 4  408 -> 494-648  §9 additions: 9.1 consulted-level semantics;
          9.2 criterion-specific common-valid supports (C1/C6 excluded as
          full-denominator/structural — verified against r3 before editing;
          U2/U3/U5; C4b branch structure incl. REPORT_ONLY removal and
          SEPARATE non-inference note; prohibitions); 9.3 floor PI row
          (no numeric literal; 2*c_complete-1 as mathematics only);
          9.4 failure-action PI row; 9.5 K-05 branch-complete informational
          disclosure (WORSE/MEAN/SEPARATE/REPORT_ONLY; conditional 0.90
          example tied to future PI ratification)
region 5  420 ; 422 -> 660-663 ; 666-671  §10 table: D-P04 row cross-
          references §9.1/§9.2; three new PI rows added
          (D-P04_COMMON_SUPPORT_FLOOR, D-P04_COMMON_SUPPORT_FAILURE_ACTION,
          D-C3-ACF-ESTIMATOR); conditional SEPARATE dependency note
          (explicitly not a PI row)
```

Machine-readable exact diff:
`p_konum_plus/provenance/f3_step1_r3_to_r4_semantic_diff_2026-09-05.txt`
(SHA256 `a8ba561e6ff61f0d2d401c9b58598205a7c3a9282786e5892527d48e26c6a043`).

## 4. Semantic diff constraints (§15)

```text
changed_F2_content = 0
changed_solver_semantics = 0
new_generator_count = 0
new_diagnostic_count = 0

D-P04_common_support_exactness_added = true
D-P04_consulted_level_semantics_added = true
AGG_L1_MEAN_existing_bounded_alternative_preserved = true   (r3 §3-C4b and
  §10 table listing unchanged; §9.2 references it as the existing r3
  bounded alternative)
AGG_L1_SEPARATE_existing_bounded_alternative_preserved = true
C4b_REPORT_ONLY_removes_D-P04_4b_level = true (r3 text retained + §9.2)
historical_r3_gate_state_not_propagated = true

D-P04_common_support_floor_PI_row_added = true
D-P04_failure_action_PI_row_added = true

C3_ACF_exactness_status = D_C3_ACF_ESTIMATOR_ROW_ADDED
C4B_SEPARATE_P04_exactness_status =
  CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED

K05_branch_complete_informational_recorded = true

parent_r3_preserved = true (350bc15e… re-verified after write)

prior_PI_choice_overwrites = 0
new_PI_owned_rows_added =
  D-P04_COMMON_SUPPORT_FLOOR
  D-P04_COMMON_SUPPORT_FAILURE_ACTION
  D-C3-ACF-ESTIMATOR
```

## 5. Finding classifications

- gate-specific blockers, corrected/exposed in r4 pending independent audit:
  D-P04-COMMON-SUPPORT-01; F3-STEP1-FAILBRANCH-01; F3-STEP1-C3-ACF-01.
- conditional gate-specific blocker (only if SEPARATE selected):
  F3-STEP1-C4B-SEPARATE-P04-01.
- informational: K-05 (recorded with full branch semantics;
  scientific_change = false; c_ident/c_complete/C4a/C4b unchanged).
- cleanup: prompt-lineage provenance block (§0 above).
- No finding is marked CLOSED; closure requires independent r4 audit and
  explicit PI owner closure.

## 6. End state (§18)

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED

D-P04-COMMON-SUPPORT-01 = CORRECTED_IN_r4_PENDING_INDEPENDENT_AUDIT
F3-STEP1-FAILBRANCH-01 = EXPOSED_AS_PI_OWNED_IN_r4_PENDING_INDEPENDENT_AUDIT
F3-STEP1-C3-ACF-01 = EXPOSED_AS_D_C3_ACF_ESTIMATOR_IN_r4_PENDING_INDEPENDENT_AUDIT
F3-STEP1-C4B-SEPARATE-P04-01 =
  CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED
K-05 = INFORMATIONAL_RECORDED_WITH_BRANCH_SEMANTICS

F3_STEP1_r4_candidate_created = true
F3_STEP1_r4_independent_audit = PENDING

PI_ratification = PENDING
RATIFICATION_READY = false
F3_EXECUTION_READY = false
F3_started = false
commit = false
```

Open PI-owned rows after r4: C4b_status; AGG-L1; D-P03-6; D-P03-7;
c_complete; D-P04_COMMON_SUPPORT_FLOOR; D-P04_COMMON_SUPPORT_FAILURE_ACTION;
D-C3-ACF-ESTIMATOR (all PI_action = ACCEPT / MODIFY, pending after
independent audit).
