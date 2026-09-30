# p_konum_plus — F2 STEP-3 FINAL FREEZE r1 — Independent Acceptance Audit

```text
artifact_role = independent acceptance audit of corrected F2 STEP-3 freeze
status        = NON-NORMATIVE
date          = 2026-09-02

normative_source =
ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md

v11_wins = true
```

## 1. Audited correction artifacts

```text
correction report =
f2_step3_final_freeze_r1_correction_report_2026-09-02.md

SHA256 =
6ed8b0a263892b718fbe664143900a1af052fb9535f44740100b5d29ec6abcb7
```

```text
corrected child freeze =
f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md

SHA256 =
ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43
```

Supporting saved end-of-task response:

```text
f2_step3_r1_correction_endoftask_report_2026-09-02.md

SHA256 =
0ba7931ea8add09dede3949ffa3e68946e9af123ffae9a6b3bfeed274241dd85
```

## 2. Parent custody verification

The corrected child identifies and preserves the immutable parent:

```text
parent FINAL FREEZE =
f2_generator_specification_record_FINAL_FREEZE_2026-09-02.md

SHA256 =
2f191f0b0b24d962dfb0356be0daf201810ae9cb85d46b4164907cc43cce91f6
```

The correction report records the parent STEP-3 provenance report unchanged:

```text
f2_step3_final_freeze_report_2026-09-02.md

SHA256 =
41c7ce03558d8ab6cd4e8c7aa6c088cf52763288eb57029dad095a33c882f3f1
```

No parent overwrite is accepted.

## 3. STEP3-A01 verification

The prior blocker was:

```text
STEP3-A01 =
P-02 optimizer/coupled-constraint binding was mistranscribed in the
parent FINAL FREEZE by associating the native NonlinearConstraint pair
with the SLSQP fallback.
```

The corrected child now freezes exactly:

```text
PRIMARY trust-constr:
P-02 -> Bounds + native scipy.optimize.NonlinearConstraint pair

FALLBACK SLSQP:
P-02 -> two equivalent SLSQP inequality-constraint dicts:
  s_l - s_side_min(beta) >= 0
  s_r - s_side_min(beta) >= 0

P-01 primary:
Bounds + LinearConstraint(c_d - c_r >= 0)

P-01 fallback:
equivalent SLSQP inequality dict c_d - c_r >= 0
```

This matches the frozen ART-F2 r2/r2a optimizer contract and the accepted r3
harness implementation.

The superseded incorrect phrase:

```text
SLSQP fallback, frozen options, native NonlinearConstraint pair for P-02
```

is absent from the corrected child.

Therefore:

```text
STEP3-A01 = CLOSED
```

## 4. Parent-to-child drift audit

A full textual parent→child comparison was performed.

Observed differences are limited to:

```text
1. r1 revision identity and parent hash/lineage fields;
2. STEP3 independent-audit reference;
3. parent supersession / corrected-child candidate status wording;
4. exact STEP3-A01 optimizer/constraint correction;
5. explicit statement that frozen optimizer options are unchanged;
6. lineage rows for the parent STEP-3 freeze/provenance/audit;
7. the mechanically necessary statement that no F3 execution occurred during
   either the parent STEP-3 freeze or its r1 correction.
```

No unrelated scientific or operational drift was found.

In particular, unchanged:

```text
P-01/P-02 formulas
u=(t-1880)/145
T=146
z_ddof0 prediction rule
D-F2-08 objective
parameter supports/bounds
Kural T
Kural S
D-F2-09 initialization lattice
feature-start rule
dedup/order
tie comparator
epsilon_model=1e-12
feasibility_acceptance_tol=1e-8
A-01/A-02/A-03/A-04 accepted semantics
R3-P01..P05 accepted semantics
X1-X4/C1-C5
failure-code claim
determinism scope
P-CMN.10 normalization
```

## 5. Correction-report write-order audit

The correction report correctly records the pre-child state:

```text
correction_report_written_first = true
corrected_child_write_pending = true
F2_complete = false
F3_allowed = false
```

The end-of-task record then identifies the corrected child as written last and
reports the exact child SHA256 above.

This satisfies the intended non-self-referential write order.

## 6. Firewall / scope audit

Accepted:

```text
scientific_change = false
execution_change = false
STEP2_rerun = false
optimizer_execution = false
real_SSA_access = false
P03/P04/P05 work = false
F3_execution = false
PI_re_ratification = false
commit = false
```

No new methodology review is required.

## 7. Independent verdict

```text
GLOBAL_BLOCKER        = none
GATE_SPECIFIC_BLOCKER = none
cleanup               = nonblocking only
informational         = nonblocking only

STEP3-A01 = CLOSED

F2_STEP_1   = COMPLETE
F2_STEP_1_5 = COMPLETE
F2_STEP_2   = ACCEPTED
F2_STEP_3   = ACCEPTED

ART_F2_FINAL_FREEZE_r1 = ACCEPTED

F2_complete = true
F3_allowed  = true
F3_started  = false

F2 = CLOSED
```

The parent FINAL FREEZE remains historical/superseded-for-gate provenance.
The active accepted F2 freeze is:

```text
f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md

SHA256 =
ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43
```

## 8. Next action

```text
Custody-import this independent acceptance audit byte-for-byte into repository
provenance, then begin F3 only as a separately governed task.
```

No additional F2 correction, STEP-2 rerun, methodology review, or PI
re-ratification is required.
