# p_konum_plus — F2 STEP-2 r3 Independent Artifact Audit

```text
artifact_role    = independent acceptance audit
status           = NON-NORMATIVE
date             = 2026-09-02
gate             = F2 · STEP 2 r3
normative_source = ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
v11_wins         = true
new_methodology_review = false
PI_re_ratification     = false
```

## 0. Audited artifacts

```text
f2_step2_feasibility_harness_r3_2026-09-01.py
SHA256 =
01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077

f2_step2_feasibility_telemetry_r3_2026-09-01.csv
SHA256 =
cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49

f2_step2_synthetic_analytic_feasibility_report_r3_2026-09-01.md
SHA256 =
afd02531cf80fa441ad2d6e3b990583783963fc6042b87c98f0108af0629abf5
```

Frozen STEP-2 fixture manifest independently re-hashed:

```text
f2_step2_fixture_manifest_2026-09-01.csv
SHA256 =
daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b
```

## 1. Independent-audit verdict

```text
GLOBAL_BLOCKER        = none
GATE_SPECIFIC_BLOCKER = none

cleanup       = 1
informational = 1

F2_STEP_2_r3 = ACCEPTED

F2_complete = false
F3_allowed  = false
F3_started  = false

STEP3_allowed = true
```

The r3 successor artifacts are accepted for F2 STEP-2 gate purposes.
This audit does not itself complete F2 and does not authorize F3 execution
before STEP-3 Final Freeze.

## 2. A-01 / R3-P01 — exact-construction evidence provenance

PASS.

The r3 harness initializes construction-evidence flags to false and writes
them at real validation/orchestration/optimizer/fallback execution sites.
The evidence is returned upward from the real start orchestration and is not
supplied as fixture-level expected truth.

The independently checked evidence contract includes:

```text
validator_called
optimizer_called
primary_fault_injection_triggered
fallback_branch_entered
same_x0_reused
fallback_nonfinite_injection_triggered
```

The benign negative control produces:

```text
primary_fault_injection_triggered      = false
fallback_branch_entered                = false
fallback_nonfinite_injection_triggered = false
validator_called                       = true
optimizer_called                       = true
```

Thus the instrumentation is falsifiable and not a constant/declarative PASS
mechanism.

## 3. A-01A — FIX-OTHER-NUMERICAL-FAILURE

PASS.

The fixture enters the real start orchestration:

```text
primary tagged FAULT_INJECTION_TEST_ONLY fault triggered
-> fallback branch entered
-> same x0 reused
-> test-only fabricated non-finite fallback endpoint exercised
-> real post-fallback handling emits OTHER_PREDECLARED_NUMERICAL_FAILURE
```

No direct hard-coded final canonical failure record is used to establish the
fixture PASS.

Observed terminal predicate set includes:

```text
NONFINITE_PARAMETER
OTHER_PREDECLARED_NUMERICAL_FAILURE
```

which is consistent with the genuinely non-finite fabricated fallback
endpoint.

## 4. A-01B / R3-P02 — FIX-INVALID-INIT

PASS.

`validate_initialization` is wired into the real `run_one_start` entry path
for every start and is called before any optimizer call. Its semantics remain
narrow: the already-supported non-finite initialization check only.

For FIX-INVALID-INIT:

```text
validator_called       = true
optimizer_called       = false
INVALID_INITIALIZATION = emitted from validator path
```

No validator rejection was observed outside the predeclared invalid-init
fixture.

## 5. R3-P03 — manifest prose to construction-key provenance

PASS.

The distinction is accepted as:

```text
machine checked:
implemented_construction_key == executed_construction_key

human audited:
manifest exact_construction prose -> implemented_construction_key
```

The prose-to-key mapping is provenance review, not automated natural-language
semantic proof. The r3 report contains the 21-row mapping table and does not
overclaim machine verification of the free-text prose.

## 6. A-02

PASS.

All seven frozen manifest columns are required before execution and absence is
a loud failure; missing-column conditions are not filtered out of the audit
result.

## 7. A-03

PASS.

Internal aggregation bookkeeping uses:

```text
valid standardized prediction:
L = objective_L(x, ghat)

otherwise:
L = +inf
```

The forbidden `objective_L(x, unstandardized_g)` bookkeeping path is absent.

## 8. A-04 / R3-P04

PASS.

The C3 display-precedence self-test is non-tautological and verifies that the
predicate set is not mutated.

The real classifier multi-predicate probe independently checks:

```text
classify_endpoint((-1.0, 1.375, 200.0, 200.0), "P-01")

predicates =
{MORPHOLOGY_INADMISSIBLE, ZERO_VARIANCE_FIT}

primary_display_code =
ZERO_VARIANCE_FIT
```

No classifier rule is changed to obtain the result.

## 9. R3-P05 — telemetry semantics

PASS.

The accepted telemetry contains exactly 12 data rows:

```text
8 benign primary rows
2 FIX-OTHER-NUMERICAL-FAILURE rows
2 FIX-FALLBACK-FAULT-INJECTION rows
```

The two new FIX-OTHER rows are the real-orchestration correction footprint.

The fabricated fallback row's optimizer-result-like fields are explicitly
test-only synthetic values, not optimizer measurements.

Telemetry firewall remains intact: no L/rho/recovery/family-performance
fields are added.

## 10. X1–X4 / C1–C5 preservation

PASS.

Independently checked/replayed items include:

```text
X1 exact scientific support separated from numerical feasibility tolerance
X2 registry/manifest fidelity
X3 status/predicate/rejection/family-summary schema separation
X4 L_INVALID_PREDICTION_GUARD = 585.0

C1 benign execution criterion
C2 beta=sqrt(6) adversarial check
C3 display precedence
C4 no beta clamp
C5 RUN1 telemetry / RUN2 determinism role

D-F2-09 retained counts:
P-01 = 731
P-02 = 261

reserved STEP-2 labels remain non-emitted
aggregation/tie semantics preserved
RNG_USED = false
```

## 11. Independent replay

A separate local audit replay reconstructed the frozen D-F2-09 grids from the
frozen rules and reproduced:

```text
P-01 raw      = 819
P-01 retained = 731

P-02 raw      = 351
P-02 retained = 261

DETERMINISM_PASS = true
telemetry rows    = 12
construction fidelity = 21/21
post-execution fixture bijection = true
R3-P04 exact multi-predicate probe = PASS
8 STEP-2-emittable failure codes reached
validator rejections outside FIX-INVALID-INIT = 0
```

The separate replay environment is not used to claim cross-platform or
cross-process bitwise equality of optimizer endpoints. F2 evidence supports
exact same-process double-run semantic determinism only.

## 12. Nonblocking cleanup CL-R3-01

```text
classification = cleanup
rerun_required  = false
```

The r3 report wording says `executed_construction_key` is composed at
orchestration exit. More precisely, for the A-01 execution-path fixtures the
underlying evidence flags are written only at their real execution sites and
returned by `run_one_start`; the audit/executor layer then deterministically
derives the executed construction key from that returned evidence.

Required freeze wording:

```text
For the A-01 execution-path fixtures, executed_construction_key is
deterministically derived in the audit/executor layer from evidence returned
by the real run_one_start orchestration; the underlying evidence flags
themselves are written only at their real execution sites.
```

This is provenance wording cleanup only:

```text
scientific_change = false
execution_change  = false
new_harness_cycle = false
```

## 13. Informational note

The independent replay did not claim process-independent or
platform-independent bitwise optimizer reproducibility. This is not an open
blocker and does not alter the accepted F2 STEP-2 determinism scope.

## 14. Final gate decision

```text
A-01 = CLOSED
A-02 = CLOSED
A-03 = CLOSED
A-04 = CLOSED

R3-P01 = CLOSED
R3-P02 = CLOSED
R3-P03 = CLOSED
R3-P04 = CLOSED
R3-P05 = CLOSED

GLOBAL_BLOCKER        = none
GATE_SPECIFIC_BLOCKER = none

F2_STEP_2_r3 = ACCEPTED
STEP3_allowed = true

F2_complete = false
F3_allowed  = false
F3_started  = false
```

Next action:

```text
F2 STEP-3 Final Freeze
```

No F3 execution is authorized by this audit artifact alone.
