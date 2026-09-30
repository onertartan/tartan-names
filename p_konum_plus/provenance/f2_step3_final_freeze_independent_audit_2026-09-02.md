# p_konum_plus — F2 STEP-3 Final Freeze Independent Audit

```text
artifact_role = independent audit of F2 STEP-3 freeze artifacts
status        = NON-NORMATIVE
date          = 2026-09-02
normative_source = ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
v11_wins = true
```

## 0. Audited STEP-3 artifacts

```text
f2_generator_specification_record_FINAL_FREEZE_2026-09-02.md
SHA256 =
2f191f0b0b24d962dfb0356be0daf201810ae9cb85d46b4164907cc43cce91f6

f2_step3_final_freeze_report_2026-09-02.md
SHA256 =
41c7ce03558d8ab6cd4e8c7aa6c088cf52763288eb57029dad095a33c882f3f1

f2_step3_final_freeze_endoftask_report_2026-09-02.md
SHA256 =
132271e3e90f925b37808d1adad52ccd59a5adac61fb5e015199649fd10e00ed
```

Upstream F2 STEP-2 r3 acceptance remains valid and is not reopened.

## 1. Independent audit result

```text
GLOBAL_BLOCKER        = none
GATE_SPECIFIC_BLOCKER = 1

STEP3-A01 =
P-02 optimizer/coupled-constraint transcription is misbound in the
FINAL FREEZE record.

classification =
F2 STEP-3 gate-specific blocker
```

The FINAL FREEZE scientific-content-by-reference block states:

```text
trust-constr primary optimizer, frozen options
SLSQP fallback, frozen options, native NonlinearConstraint pair for P-02
```

The second line is incorrect as written.

Frozen ART-F2 r2/r2a and the accepted r3 harness establish instead:

```text
PRIMARY:
trust-constr
P-01: Bounds + LinearConstraint
P-02: Bounds + native scipy.optimize.NonlinearConstraint pair

FALLBACK:
SLSQP
same bounds
P-01: equivalent SLSQP inequality dict
P-02: two equivalent SLSQP inequality dicts
```

Thus `native NonlinearConstraint pair for P-02` belongs to the PRIMARY
trust-constr path, not the SLSQP fallback path.

## 2. Why this blocks STEP-3 final acceptance

The affected record is the artifact whose role is:

```text
F2_FINAL_FROZEN_OPERATIONAL_SPEC
```

Therefore an incorrect optimizer/constraint binding in that record cannot be
left as the accepted operational freeze, even though:

```text
scientific_methodology_change = false
STEP2_execution_change = false
accepted_r3_execution = unchanged
```

This is a transcription/operational-freeze defect, not a scientific-methodology
defect.

## 3. Required correction

Do NOT overwrite or edit the existing FINAL FREEZE artifact.

Preserve it as historical, superseded-for-gate provenance and create a child
correction revision.

Required corrected wording:

```text
trust-constr primary optimizer, frozen options;
for P-02, the primary trust-constr path uses Bounds plus the native
scipy.optimize.NonlinearConstraint pair.

SLSQP fallback, frozen options;
for P-02, the fallback uses the two equivalent SLSQP inequality-constraint
dicts for s_l - s_side_min(beta) >= 0 and
s_r - s_side_min(beta) >= 0.
```

No other scientific/operational content may change except any mechanically
necessary lineage/status wording identifying the superseded parent and
corrected child.

## 4. Nonblocking informational item

The saved end-of-task response contains one malformed first rendering of HEAD
and immediately follows it with the correct HEAD plus an explicit transparency
note. The repository/provenance report and FINAL FREEZE use the correct HEAD.

```text
classification = informational
project_artifact_correction_required = false
```

## 5. Gate state after this audit

```text
F2_STEP_1   = COMPLETE
F2_STEP_1_5 = COMPLETE
F2_STEP_2   = ACCEPTED

F2_STEP_3 = CORRECTION_REQUIRED

F2_complete = false
F3_allowed  = false
F3_started  = false

STEP2_rerun_required = false
new_methodology_review = false
PI_re_ratification_required = false
```

The existing FINAL FREEZE's internal `F2_complete=true` / `F3_allowed=true`
claims are superseded for gate purposes by this independent audit until the
narrow STEP-3 transcription correction is independently accepted.

## 6. Required next action

```text
F2 STEP-3 Final Freeze r1 transcription correction
```

Only STEP3-A01 may be corrected. Do not reopen STEP-2 or scientific decisions.
