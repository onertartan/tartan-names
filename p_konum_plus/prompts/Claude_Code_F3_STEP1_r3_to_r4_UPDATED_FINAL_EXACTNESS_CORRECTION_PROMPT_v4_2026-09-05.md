# Claude Code Prompt — F3 STEP-1 r3 → r4 Updated Final Exactness Correction Package
## D-P04 Common-Support + D-P04 Failure Semantics + C3 ACF Estimator Pin + K-05 Branch Disclosure + Conditional SEPARATE-P04 Exactness Check

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Task class:** exactness / provenance closure; bounded child revision only  
**Authority:** Claude Code is execution/provenance authority only; NOT methodology authority and NOT PI authority  
**Status:** NON-NORMATIVE execution prompt

```text
prompt_revision = v4
parent_prompt = Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v3_2026-09-05.md
revision_scope =
  preserve all v3 exactness/provenance corrections;
  generalize K-05 to the exact AGG/C4b-status branch structure;
  keep c_complete symbolic except for explicitly conditional examples;
  require all new PI-owned rows to be inserted into the r4 §10 ratification table;
  add a bounded exactness check for SEPARATE-specific D-P04 C4b scalar semantics
new_methodology_review = false
F2_reopening = false
```

---

# 0. Purpose

Create a **child r4 ratification candidate** from the current r3 candidate to address the currently identified F3 STEP-1 exactness issues without reopening F2 or starting a new methodology cycle.

Active findings:

```text
D-P04-COMMON-SUPPORT-01
classification = gate-specific blocker
scope = F3 / D-P04 paired-comparison exactness

F3-STEP1-FAILBRANCH-01
classification = gate-specific blocker
scope = D-P04 common-support failure semantics

F3-STEP1-C3-ACF-01
classification = gate-specific blocker
scope = C3 exact implementation / estimator pin

K-05
classification = informational
scope = C4a/C4b interaction disclosure only

F3-STEP1-C4B-SEPARATE-P04-01
classification = conditional gate-specific blocker if AGG-L1=SEPARATE is selected
scope = SEPARATE-specific D-P04 C4b scalar exactness
```

The r4 task has five goals:

```text
1. define criterion-specific common-valid supports for D-P04
2. define CONSULTED-level semantics for the lexicographic D-P04 path
3. expose, but do NOT silently resolve, the PI-owned choice about
   D-P04 common-support floor and its associated failure branch
4. add an exact PI decision row for the C3 lag-1 residual ACF estimator
5. verify whether r3 already defines the D-P04 C4b scalar under SEPARATE;
   if absent, record the bounded under-specification without inventing a rule
```

This task must NOT ratify pending PI scientific choices.

---

# 1. Sole normative and frozen upstream custody

Before any mutation, locate and independently SHA256-verify:

```text
1. ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
   expected SHA256 =
   d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3

2. f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md
   expected SHA256 =
   ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43

3. f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md
   expected SHA256 =
   350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad
```

If any expected hash/path mismatches:

```text
STOP = true
classification = global blocker
artifact_mutation = prohibited
return observed path + observed SHA256 + expected SHA256
```

Source hierarchy:

```text
1. v11 sole normative source
2. accepted/frozen gate artifacts
3. independently accepted audits
4. latest verified status/handoff
5. historical provenance
```

Historical/superseded material must not override v11 or the accepted F2 freeze.

## 1.1 Historical r3 provenance-state quarantine

The following artifact remains valid provenance and custody evidence:

```text
f3_step1_r1_r3_provenance_correction_report_2026-09-03.md
SHA256 =
006f6c615dd1e9bfddee739fb53d8565927ef41a2c9ab76b3cba082a96839815
```

Its valid retained functions are:

```text
r2 -> r3 custody / lineage
exact r3 SHA256 provenance
F3-STEP1-PROV-03 closure
recorded spline-solver qualification provenance
```

However, its then-current gate-state statements:

```text
GATE_SPECIFIC_BLOCKER = none
CONTRACT_EXACTNESS = PASS
RATIFICATION_READY = true
```

are **historical status only**. They predate the later findings:

```text
D-P04-COMMON-SUPPORT-01
F3-STEP1-FAILBRANCH-01
F3-STEP1-C3-ACF-01
F3-STEP1-C4B-SEPARATE-P04-01
```

and must NOT be propagated as the current r4 gate state.

This quarantine is provenance-only:

```text
r3 parent validity = preserved
r3 SHA256 validity = preserved
F3-STEP1-PROV-03 closure = preserved
scientific_change = false
F2_reopening = false
```

---

# 2. Current governance state

Treat current state as:

```text
F0 = COMPLETE
F1 = COMPLETE
F2 = CLOSED

F2_reopening = false
new_methodology_review = false

F3_EXECUTION_READY = false
F3_started = false

candidate_specific_fit = false
crossfit_execution = false
C4_probe_execution = false
P03_threshold_measurement = false
adequacy_measurement = false
generator_selected = false
F4_started = false
algorithm_x_CVI_outcome_access = prohibited
```

No empirical or synthetic adequacy execution is authorized by this task.

---

# 3. PI-owned scientific choices remain PENDING

Current synthesis recommendation:

```text
C4b_status = P03_GATE
AGG-L1 = WORSE
D-P03-6 = 6A
D-P03-7 = Option A
c_complete = 0.90
```

These are recommendations only.

Claude Code must NOT convert them into binding PI decisions.

Required state in r4:

```text
PI_action = ACCEPT / MODIFY
```

must remain open for the relevant owner rows.

No automatic acceptance.

---

# 4. Parent/child discipline

The r3 candidate is read-only parent provenance.

Do NOT overwrite, normalize, or silently rewrite it.

Create:

```text
p_konum_plus/calibration/
f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md
```

Create correction report:

```text
p_konum_plus/provenance/
f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md
```

Create external SHA256 provenance for r4.

Do NOT self-hash the candidate body.

Do NOT commit unless separately requested.

---

# 5. Finding 1 — D-P04-COMMON-SUPPORT-01

## 5.1 Exact defect

Under r3, P03 family-vs-spline statistics can be computed on candidate-specific paired-valid sets.

Thus D-P04 may compare:

```text
P-01 scalar on support A
versus
P-02 scalar on support B
```

even if both family-specific supports individually satisfy their P03 completeness requirements.

Therefore:

```text
P03 family-vs-spline pairing
does NOT imply
D-P04 P-01-vs-P-02 pairing
```

The minimal exactness correction is:

```text
for every subset-defined D-P04 level that is actually CONSULTED,
recompute BOTH candidate scalars on the SAME
criterion-specific common-valid support.
```

---

# 6. D-P04 lexicographic CONSULTED-level semantics

r3 D-P04 is lexicographic.

The r4 candidate must explicitly define:

```text
A D-P04 level is CONSULTED only if all earlier D-P04 levels
were equivalent within their frozen tau rule.

Once a D-P04 level resolves the comparison,
the procedure terminates.

Unconsulted later levels:
  impose no common-support requirement
  impose no floor requirement
  cannot trigger STOP
  need not be recomputed for decision purposes

The exact consulted path must be recorded in provenance/reporting.
```

Do NOT impose common-support requirements on levels that the lexicographic procedure never reaches.

---

# 7. Criterion-specific common-valid supports

The exact level membership must be verified against r3 before editing.

Do not blindly assume a criterion is subset-defined if r3 defines it on a full denominator.

For each sex stratum `s`, intended common-support semantics:

```text
C2:
  U2_s =
    trajectories for which
    P-01 has the required valid C2 statistic
    AND P-02 has the required valid C2 statistic
    AND the spline benchmark has the required valid C2 statistic.

C3:
  U3_s =
    trajectories for which
    P-01 has the required valid C3 statistic
    AND P-02 has the required valid C3 statistic
    AND the spline benchmark has the required valid C3 statistic.

C5:
  U5_s =
    trajectories for which
    P-01 has the required valid C5 statistic
    AND P-02 has the required valid C5 statistic.
```

For C4b:

```text
If eventual PI-ratified C4b_status = REPORT_ONLY:

  C4b is removed from D-P04.
  No D-P04 C4b common-support requirement, common-support floor,
  or common-support failure-action rule applies.

If eventual PI-ratified C4b_status = P03_GATE:

  If eventual PI-ratified AGG-L1 = WORSE
  OR eventual PI-ratified AGG-L1 = MEAN:

    U4_s =
      trajectories for which
      P-01 LEFT and RIGHT probes are successful
      AND P-02 LEFT and RIGHT probes are successful
      AND spline LEFT and RIGHT probes are successful.

    Recompute BOTH P-01 and P-02 C4b scalars on this same U4_s
    using the eventual PI-ratified aggregation:

      WORSE -> r_i = max(RMSE_edge_LEFT_i, RMSE_edge_RIGHT_i)
      MEAN  -> r_i = (RMSE_edge_LEFT_i + RMSE_edge_RIGHT_i)/2

  If eventual PI-ratified AGG-L1 = SEPARATE:

    U4L_s =
      trajectories for which
      P-01 LEFT probe succeeds
      AND P-02 LEFT probe succeeds
      AND spline LEFT probe succeeds.

    U4R_s =
      trajectories for which
      P-01 RIGHT probe succeeds
      AND P-02 RIGHT probe succeeds
      AND spline RIGHT probe succeeds.

    Recompute BOTH P-01 and P-02 LEFT sex-level statistics on the same U4L_s
    and BOTH P-01 and P-02 RIGHT sex-level statistics on the same U4R_s.

    IMPORTANT:
      do NOT infer from this sentence how the two side-specific sex-level
      statistics are converted into the single D-P04 4b comparison level.
      That scalar-combination semantics must be verified under §10.5 below.
```

`AGG-L1-MEAN` is not a new r4 scientific option. It is an already-open
r3 D-P03-5 bounded alternative and must be preserved exactly as such.

For every CONSULTED subset-defined D-P04 level:

```text
recompute BOTH P-01 and P-02 statistics
on the SAME applicable U-set.
```

Prohibited:

```text
candidate-specific-set P-01-vs-P-02 comparison
imputation
numerical sentinel
post-hoc support substitution
```

---

# 8. Finding 2 — D-P04 common-support floor is PI-owned

The common-set requirement itself closes the paired-comparison defect.

Whether a CONSULTED D-P04 common set must also satisfy a minimum support floor is an additional scientific/governance choice.

Do NOT hard-code that choice.

The r4 candidate must expose:

```text
D-P04_COMMON_SUPPORT_FLOOR

recommended =
  apply the PI-ratified global c_complete
  to every CONSULTED subset-defined D-P04 common-valid set

bounded alternative =
  no additional D-P04 common-support floor;
  still recompute both candidate scalars on the same common-valid set;
  mandatory disclosure of |U_j,s| / n_s for every CONSULTED level

PI_action = ACCEPT / MODIFY
```

Important:

```text
Do NOT introduce any new numeric D-P04 floor literal.

Do NOT introduce 0.80, 0.85, or any other numeric value
as a candidate D-P04 threshold.

The theoretical intersection lower bound
2*c_complete - 1
may be described only as mathematics/provenance,
never as an accepted floor.
```

If the PI later accepts the recommended branch and the PI-ratified global literal is:

```text
c_complete = 0.90
```

then, conditionally:

```text
|U_j,s| / n_s >= 0.90
```

for every CONSULTED subset-defined level.

This is a conditional implication only. r4 must not pre-ratify `0.90`.

---

# 9. Finding 3 — F3-STEP1-FAILBRANCH-01

r3 contains a STOP/redesign branch for the case where no family passes P03.

Do NOT assume that this existing branch already covers a new D-P04 common-support-floor failure.

The r4 candidate must explicitly expose the action rule as PI-owned if the PI selects the recommended floor branch.

Add:

```text
D-P04_COMMON_SUPPORT_FAILURE_ACTION

Applicability =
  only if D-P04_COMMON_SUPPORT_FLOOR is ratified as
  "apply global c_complete"

recommended =
  if a CONSULTED subset-defined common-valid set fails the
  ratified common-support floor:

      D-P04 = NOT_COMPARISON_READY
      no automated winner
      STOP and return to PI governance
      no threshold relaxation
      no fallback to candidate-specific supports
      no silent skip to later D-P04 levels

bounded alternative =
  PI must provide an exact replacement action rule

PI_action = ACCEPT / MODIFY
```

Claude Code must NOT invent this branch.

Claude Code must NOT claim it was already predeclared unless it can quote exact parent text demonstrating that fact.

If r3 already contains semantically identical language, record that evidence and avoid redundant duplication.

---

# 10. Finding 4 — F3-STEP1-C3-ACF-01

## 10.1 Exact defect

C3 uses a lag-1 residual autocorrelation quantity described as a sample autocorrelation.

The exact estimator convention must be pinned for an exact criterion contract.

Claude Code must first inspect:

```text
v11
accepted F2 freeze
r3
admissible current lineage/provenance referenced by r3
```

and determine whether an exact lag-1 ACF estimator is already pinned.

If an exact estimator is already pinned:

```text
F3-STEP1-C3-ACF-01 = NOT_A_DEFECT
quote exact source + section + literal
do not add duplicate methodology
```

If no exact estimator is pinned:

```text
F3-STEP1-C3-ACF-01 = CONFIRMED
classification = gate-specific blocker
```

Then insert the following PI-owned decision row into r4.

---

## 10.2 D-C3-ACF-ESTIMATOR — exact PI decision packet

```text
D-C3-ACF-ESTIMATOR

recommended =

  For each valid full-data residual series r_0,...,r_{T-1}:

    r_bar =
      (1/T) * sum_{t=0}^{T-1} r_t

    phi_i =
      abs(
        sum_{t=0}^{T-2}
          (r_t - r_bar)(r_{t+1} - r_bar)
        /
        sum_{t=0}^{T-1}
          (r_t - r_bar)^2
      )

    T = 146

  family residual:
    r_t = z_t - ghat_t

    where ghat_t is the frozen full-data best-eligible family prediction
    on the full 146-point grid, standardized by the frozen z_ddof0
    prediction rule.

  spline residual:
    defined analogously from the valid full-data
    adequacy-benchmark spline prediction.

  The identical estimator convention is used for family and spline.

  interpretation =
    classical lag-1 sample ACF convention using
    the full-series residual mean and the standard/biased
    autocovariance denominator.

bounded alternatives =

  (b) adjusted lag denominator:

      phi_adjusted =
        phi_classical * T/(T-1)

      with T = 146:

      phi_adjusted =
        phi_classical * 146/145

  (c) Pearson lagged-vector correlation:

      phi_Pearson =
        abs(
          corr(
            (r_0,...,r_{T-2}),
            (r_1,...,r_{T-1})
          )
        )

      where the two lagged subvectors are
      separately centered and separately scaled.

PI_action = ACCEPT / MODIFY
```

---

## 10.3 Exact zero-variance / undefined-statistic rule

Also pin:

```text
If:

  sum_{t=0}^{T-1}(r_t - r_bar)^2 = 0

or the resulting statistic is non-finite:

  phi_i = undefined

and the existing D-P03-7
undefined-statistic / completeness governance applies.

No new numerical zero-variance tolerance
is introduced at STEP-1.
```

Do NOT silently substitute:

```text
phi_i = 0
phi_i = NaN but treated as valid
epsilon denominator
sentinel value
```

unless separately PI-approved.

---

## 10.4 Rationale to record

Use the following scientific rationale:

```text
RATIONALE

The estimator choice is not cosmetic.

Under the frozen F2 convention, both the observed z-trajectory and the
full-grid prediction are z_ddof0 standardized on the full 146-point grid.

Therefore the full-grid residual mean is theoretically zero:

  mean(r) = mean(z) - mean(ghat) = 0 - 0 = 0

up to floating-point error.

Accordingly, the estimator choice is NOT justified by a generally
nonzero full-grid residual mean.

Nevertheless the conventions are not equivalent:

1. alternative (b) changes the classical lag-1 ACF by the fixed factor

     T/(T-1) = 146/145

2. alternative (c) separately centers and scales the two lagged
   subvectors:

     (r_0,...,r_{T-2})
     (r_1,...,r_{T-1})

   whose means and variances generally differ after the first/last
   residual is removed, even when the full residual vector has mean zero.

Therefore the three conventions can produce different C3 values
and must be pinned outcome-blind before F3 execution.

The scientific estimator formula is pinned in F3 STEP-1.

The exact library/API implementation call is a CLASS_C implementation
pin and may be fixed in the subsequent implementation step,
provided it is mathematically verified to implement the PI-ratified
formula exactly.
```

Do NOT use the rejected rationale:

```text
"residual mean is generally nonzero because the families lack
offset/amplitude parameters"
```

That statement is not valid under the frozen full-grid `z_ddof0`
prediction convention.

---

## 10.5 New bounded exactness check — F3-STEP1-C4B-SEPARATE-P04-01

Search r3 for an **exact** rule defining the D-P04 C4b 4b comparison under:

```text
C4b_status = P03_GATE
AGG-L1 = SEPARATE
```

In particular, determine whether r3 explicitly defines how the two side-specific
statistics:

```text
LEFT C4b statistic
RIGHT C4b statistic
```

become the D-P04 4b comparison quantity/rule.

Do not infer the answer from the P03 statement:

```text
SEPARATE passes iff both sides pass
```

because P03 pass/fail semantics and P04 scalar-comparison semantics are distinct.

If r3 contains an exact SEPARATE-specific P04 rule:

```text
F3-STEP1-C4B-SEPARATE-P04-01 = NOT_A_DEFECT
quote exact source + section + literal
preserve it exactly
```

If r3 does NOT contain such a rule:

```text
F3-STEP1-C4B-SEPARATE-P04-01 = CONFIRMED

classification =
  conditional gate-specific blocker

condition =
  AGG-L1 = SEPARATE is selected for ratification/execution
```

Then:

```text
do NOT invent:
  max-over-sides
  mean-over-sides
  LEFT-then-RIGHT lexicographic order
  RIGHT-then-LEFT lexicographic order
  both-sides-must-be-equivalent rule
  any other scalar-combination rule
```

Record in r4:

```text
AGG-L1-SEPARATE remains an existing bounded PI alternative.

However, if its D-P04 C4b scalar-comparison rule is absent upstream,
SEPARATE cannot be treated as execution-exact until the PI supplies
an exact D-P04 4b rule.

status =
  CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED
```

Do NOT turn this into a current blocker for the preferred WORSE path.

Do NOT force a new PI row now unless the PI selects SEPARATE.

The purpose is to prevent silent rule invention or a later hidden r5 regression.

---

# 11. K-05 — informational disclosure only

K-05 is not a blocker.

The exact implication depends on the eventual C4b-status / AGG branch.

Use the following canonical branch structure:

```text
If eventual PI-ratified C4b_status = P03_GATE:

  If eventual PI-ratified AGG-L1 = WORSE
  OR eventual PI-ratified AGG-L1 = MEAN:

    the applicable C4b paired-valid set V4_s/U4_s contains only
    trajectories for which the family has successful LEFT and RIGHT probes.

    Therefore:

      C4b completeness share >= c_complete
      =>
      family C4a successful-probe share >= c_complete.

  If eventual PI-ratified AGG-L1 = SEPARATE:

    if BOTH side-specific C4b completeness requirements satisfy:

      LEFT common/paired-valid share >= c_complete
      AND
      RIGHT common/paired-valid share >= c_complete

    then family LEFT success count >= c_complete*n_s
    and family RIGHT success count >= c_complete*n_s.

    Hence over the full 2*n_s probe denominator:

      family C4a successful-probe share >= c_complete.

Thus, under P03_GATE:

  if the applicable C4b completeness condition passes
  AND the PI-ratified c_complete > c_ident,

  then c_ident is structurally non-binding on that path.

If eventual PI-ratified C4b_status = REPORT_ONLY:

  C4b completeness is not a P03/P04 gate.
  The implication above does NOT make c_ident non-binding.
  c_ident remains independently binding through C4a.
```

Conditional current-recommendation example only:

```text
IF the PI later ratifies:

  C4b_status = P03_GATE
  c_complete = 0.90
  c_ident = 0.85

THEN, for WORSE / MEAN, and for SEPARATE when both side-specific
completeness conditions pass:

  C4a successful-probe share >= 0.90 > 0.85,

so C4a is structurally non-binding after the applicable C4b
completeness condition passes.
```

The numeric `0.90` above is a **conditional example tied to a future PI ratification**.
Do NOT write it as a presently ratified literal.

Do NOT change:

```text
c_ident
c_complete
C4a
C4b
```

because of K-05.

Record K-05 in the correction report as:

```text
classification = informational
scientific_change = false
```

The final PI ratification/freeze record, after r4 independent audit and explicit
PI closure, must contain a canonical exact K-05 disclosure matching the
actually ratified C4b-status / AGG / c_complete branch.

Do NOT import reviewer prose as normative text.

---

# 12. AGG-L1 branch discipline

r4 must preserve all three currently permitted r3 branches:

```text
AGG-L1-WORSE
AGG-L1-SEPARATE
AGG-L1-MEAN
```

Do not ratify any branch.

Do not remove any branch.

`AGG-L1-MEAN` remains a bounded alternative only; its restoration here is an
exactness correction against r3, not a new recommendation and not a new
scientific choice.

`AGG-L1-SEPARATE` also remains a bounded alternative. If §10.5 confirms that
its D-P04 4b scalar-comparison rule is absent, preserve the alternative but
mark the conditional exactness dependency; do not invent the missing rule.

Do not choose based on:

```text
F1 morphology composition
W-L/W-I/W-R prevalence
candidate-specific performance
F3 outcomes
```

The PI will decide after independent r4 audit.

---

# 13. Scientific content that must NOT change

Unless required by the explicitly declared findings above, do NOT alter:

```text
C1-C6 scientific roles
C1-C6 ordering
P03 family-vs-spline gates
D-P03-1
D-P03-2
D-P03-3
D-P03-4
D-P03-5 scientific alternatives
D-P03-6 scientific alternatives
D-P03-7 scientific alternatives
D-P05 cross-fit scheme
delta literals
tau literals
c_cov
c_ident
c_stab
E
K
g
spline basis / knots / df
solver semantics
F2 generator specifications
primary generator set
R-REV governance
```

No new primary generator.

No 6B companion.

No DTW/elastic alignment.

No empirical tuning.

---

# 14. Firewall

This task prohibits:

```text
real SSA generator fit
P05 empirical cross-fit
C4 empirical probe execution
P03 measurement-derived threshold computation
generator comparison
generator selection
F4 full-data refit
algorithm × CVI outcome access
new pilot execution
synthetic adequacy execution
```

No data-derived choice.

No threshold retuning.

---

# 15. Required semantic diff constraints

After producing r4, compare r3 → r4 and explicitly report:

```text
changed_F2_content = 0
changed_solver_semantics = 0
new_generator_count = 0
new_diagnostic_count = 0

D-P04_common_support_exactness_added = true
D-P04_consulted_level_semantics_added = true
AGG_L1_MEAN_existing_bounded_alternative_preserved = true
AGG_L1_SEPARATE_existing_bounded_alternative_preserved = true
C4b_REPORT_ONLY_removes_D-P04_4b_level = true
historical_r3_gate_state_not_propagated = true

D-P04_common_support_floor_PI_row_added = true
D-P04_failure_action_PI_row_added = true

C3_ACF_exactness_status =
  PIN_ALREADY_EXISTS
  OR
  D_C3_ACF_ESTIMATOR_ROW_ADDED

C4B_SEPARATE_P04_exactness_status =
  PIN_ALREADY_EXISTS
  OR
  CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED

K05_branch_complete_informational_recorded = true

parent_r3_preserved = true
```

Do NOT assert:

```text
changed_PI_choices = 0
```

merely because no prior PI choice was overwritten.

Instead distinguish:

```text
prior_PI_choice_overwrites = 0

new_PI_owned_rows_added =
  D-P04_COMMON_SUPPORT_FLOOR
  D-P04_COMMON_SUPPORT_FAILURE_ACTION
  D-C3-ACF-ESTIMATOR
```

if the C3 row is confirmed necessary.

`F3-STEP1-C4B-SEPARATE-P04-01` does NOT create a new owner row unless
SEPARATE is actually selected and the upstream rule is absent.

---

## 15.1 Mandatory r4 §10 ratification-table integration

Do not leave new owner rows only in narrative sections.

If the corresponding row is required, add it explicitly to the r4 §10
ratification table / owner-decision register using the same row style as r3.

At minimum, the r4 table must include or cross-reference:

```text
D-P04_COMMON_SUPPORT_FLOOR
D-P04_COMMON_SUPPORT_FAILURE_ACTION

D-C3-ACF-ESTIMATOR
  only if no admissible upstream exact ACF pin exists
```

For each row preserve:

```text
recommended
bounded alternative(s)
PI_action = ACCEPT / MODIFY
status = pending until explicit PI action after independent audit
```

For `F3-STEP1-C4B-SEPARATE-P04-01`:

```text
if upstream SEPARATE-specific P04 rule exists:
  no new PI row

if absent:
  do NOT invent a recommendation row merely to make the table look complete;
  record:
    CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED
```

The PI will supply a new exact row only if SEPARATE is actually chosen.

---

# 16. Required deliverables

Minimum:

```text
1. p_konum_plus/calibration/
   f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md

2. p_konum_plus/provenance/
   f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md

3. r3_to_r4 semantic diff
   machine-readable or plain-text exact diff summary

4. external SHA256 for r4 child

5. current-state end-of-task report
```

Do not self-hash the candidate.

---

# 17. Required correction report fields

Include:

```text
parent =
f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md

parent_sha256 =
350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad

child =
f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md

child_sha256 =
<computed>

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
  D-C3-ACF-ESTIMATOR
    if upstream pin is absent

conditional_PI_exactness_dependencies =
  F3-STEP1-C4B-SEPARATE-P04-01
    only if upstream SEPARATE P04 rule is absent
```

List exact changed sections/line ranges.

---

# 18. Required end-state logic

If all unconditional exactness issues are fully represented in r4:

```text
F0 = COMPLETE
F1 = COMPLETE
F2 = CLOSED

D-P04-COMMON-SUPPORT-01 =
CORRECTED_IN_r4_PENDING_INDEPENDENT_AUDIT

F3-STEP1-FAILBRANCH-01 =
EXPOSED_AS_PI_OWNED_IN_r4_PENDING_INDEPENDENT_AUDIT

F3-STEP1-C3-ACF-01 =
PIN_ALREADY_EXISTS
OR
EXPOSED_AS_D_C3_ACF_ESTIMATOR_IN_r4_PENDING_INDEPENDENT_AUDIT

F3-STEP1-C4B-SEPARATE-P04-01 =
PIN_ALREADY_EXISTS
OR
CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED

K-05 =
INFORMATIONAL_RECORDED_WITH_BRANCH_SEMANTICS

F3_STEP1_r4_candidate_created = true
F3_STEP1_r4_independent_audit = PENDING

PI_ratification = PENDING
RATIFICATION_READY = false
F3_EXECUTION_READY = false
F3_started = false
```

Do NOT mark any finding CLOSED until independent audit confirms the child correction.

The conditional SEPARATE finding does not block r4 creation or the preferred
WORSE path. It blocks only future ratification/execution of SEPARATE if its
P04 4b rule remains undefined.

---

# 19. Independent audit requirements after Claude Code returns

Do NOT perform the independent audit yourself unless explicitly asked in a separate task.

The next audit must verify:

```text
1. r3 parent hash exact
2. r4 child hash exact
3. consulted-level lexicographic semantics exact
4. same-set scalar recomputation exact
5. unconsulted levels cannot trigger floor/failure logic
6. AGG-L1-MEAN remains preserved as the existing r3 bounded alternative
7. AGG-L1-SEPARATE remains preserved as the existing r3 bounded alternative
8. C4b REPORT_ONLY correctly removes the C4b D-P04 sub-level
9. superseded r3 RATIFICATION_READY=true is not propagated as current state
10. no numeric D-P04 floor literal invented
11. D-P04 floor is correctly represented as PI-owned
12. D-P04 failure action is correctly represented as PI-owned
13. C3 ACF estimator:
      a) exact upstream pin proven,
      OR
      b) D-C3-ACF-ESTIMATOR row exactly inserted
14. zero-residual-variance / non-finite C3 behavior exact
15. rejected residual-mean rationale absent
16. CLASS_C library-call deferral does not alter scientific estimator semantics
17. SEPARATE-specific P04 C4b rule:
      a) exact upstream rule quoted,
      OR
      b) conditional under-specification correctly recorded without rule invention
18. K-05 branch semantics cover WORSE, MEAN, SEPARATE, and REPORT_ONLY correctly
19. every newly required PI row is present/cross-referenced in r4 §10 ratification table
20. no F2/scientific generator drift
21. no forbidden execution
```

Only after independent audit PASS may the unconditional findings be CLOSED,
provided no PI-owned row remains unratified.

---

# 20. PI ratification sequence after independent audit

After audit PASS, the PI must review the single audited r4 artifact/hash and explicitly close all remaining owner rows.

At minimum:

```text
C4b_status = ACCEPT / MODIFY
AGG-L1 = ACCEPT / MODIFY
D-P03-6 = ACCEPT / MODIFY
D-P03-7 = ACCEPT / MODIFY
c_complete = ACCEPT / MODIFY

D-P04_COMMON_SUPPORT_FLOOR = ACCEPT / MODIFY
D-P04_COMMON_SUPPORT_FAILURE_ACTION = ACCEPT / MODIFY

D-C3-ACF-ESTIMATOR = ACCEPT / MODIFY
if that row exists
```

If the PI selects:

```text
AGG-L1 = SEPARATE
```

and §10.5 found no exact upstream D-P04 4b rule, then BEFORE SEPARATE can be
ratified/executed:

```text
STOP
return F3-STEP1-C4B-SEPARATE-P04-01 to PI
PI must supply an exact SEPARATE-specific D-P04 C4b comparison rule
```

No such rule is needed if the PI does not select SEPARATE.

The final ratification/freeze record must also include a canonical exact K-05
informational disclosure matching the actually ratified branch.

Only after this owner closure and final provenance audit may F3 execution readiness be considered.

---

# 21. Required Claude Code response format

Return:

| Check | PASS/FAIL | Evidence |
|---|---|---|
| v11 hash | | |
| F2 freeze hash | | |
| r3 parent hash | | |
| parent preserved | | |
| D-P04 consulted-level semantics exact | | |
| D-P04 common-valid sets exact | | |
| unconsulted levels cannot trigger floor/STOP | | |
| AGG-L1-MEAN existing bounded alternative preserved | | |
| AGG-L1-SEPARATE existing bounded alternative preserved | | |
| C4b REPORT_ONLY removes D-P04 C4b sub-level | | |
| historical r3 RATIFICATION_READY=true not propagated | | |
| D-P04 floor represented as PI-owned | | |
| no numeric new D-P04 floor literal | | |
| D-P04 failure branch represented as PI-owned | | |
| C3 ACF upstream pin found? | | |
| D-C3-ACF-ESTIMATOR row exact if required | | |
| C3 zero-variance/non-finite rule exact | | |
| rejected residual-mean rationale absent | | |
| CLASS_C implementation deferred correctly | | |
| SEPARATE-specific P04 C4b rule found? | | |
| conditional SEPARATE under-specification recorded if needed | | |
| K-05 branch semantics exact | | |
| new PI rows integrated into r4 §10 ratification table | | |
| prior PI choices not overwritten | | |
| no forbidden execution | | |
| r4 child created | | |
| correction report created | | |
| semantic diff created | | |
| external child SHA256 recorded | | |
| F3_EXECUTION_READY remains false | | |

Then:

```text
r4 path =
r4 status =
r4 SHA256 =

correction report path =
correction report SHA256 =

semantic diff path =

open PI-owned rows =
conditional exactness dependencies =
```

Final classification vocabulary only:

```text
global blocker
gate-specific blocker
cleanup
informational
```

---

# 22. Final instruction

Execute only the bounded F3 STEP-1 exactness/provenance task defined above.

Do not reopen F2.

Do not make PI-owned scientific choices.

Do not run F3.

Do not introduce a D-P04 numeric floor.

Do not invent a D-P04 failure branch beyond the explicit PI-owned row.

Do not change the C3 estimator recommendation.

Do not choose among the C3 bounded alternatives.

Do not drop, silently narrow, or reclassify the existing r3 `AGG-L1-MEAN`
bounded alternative.

Do not drop or silently redefine the existing r3 `AGG-L1-SEPARATE`
bounded alternative.

Do not invent a SEPARATE-specific D-P04 4b scalar-combination rule.

Do not use the rejected “residual mean generally nonzero” rationale.

If any additional scientific choice is required:

```text
STOP and return bounded ambiguity to Öner.
```
