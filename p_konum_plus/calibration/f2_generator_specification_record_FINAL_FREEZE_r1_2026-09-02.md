# p_konum_plus — ART-F2 Generator Specification Record — FINAL FREEZE r1

## 1. Identity

```text
artifact_id       = ART-F2
artifact_role     = F2_FINAL_FROZEN_OPERATIONAL_SPEC
record_revision   = FINAL_FREEZE_r1_2026-09-02
date              = 2026-09-02

parent_freeze =
f2_generator_specification_record_FINAL_FREEZE_2026-09-02.md

parent_freeze_sha256 =
2f191f0b0b24d962dfb0356be0daf201810ae9cb85d46b4164907cc43cce91f6

correction_scope = STEP3-A01_optimizer_constraint_transcription_only
scientific_change = false
execution_change = false
STEP2_rerun = false
PI_re_ratification_required = false
new_methodology_review = false

normative_authority = none
normative_source    = ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
v11_wins            = true

scientific_precursor =
f2_generator_specification_record_r2a_2026-09-01.md

accepted_execution_harness =
f2_step2_feasibility_harness_r3_2026-09-01.py

accepted_execution_telemetry =
f2_step2_feasibility_telemetry_r3_2026-09-01.csv

accepted_execution_report =
f2_step2_synthetic_analytic_feasibility_report_r3_2026-09-01.md

independent_acceptance_audit =
f2_step2_r3_independent_audit_2026-09-02.md

step3_independent_audit =
f2_step3_final_freeze_independent_audit_2026-09-02.md
```

Revision status:

```text
parent FINAL FREEZE =
SUPERSEDED_FOR_GATE_ACCEPTANCE

corrected FINAL FREEZE r1 =
ACTIVE_ACCEPTED_FREEZE_CANDIDATE_PENDING_INDEPENDENT_AUDIT
```

This child revision corrects exactly one transcription defect (STEP3-A01,
identified by the STEP-3 independent audit) in the parent's
scientific-content-by-reference block, which misbound the native
`scipy.optimize.NonlinearConstraint` pair for P-02 to the SLSQP fallback line.
All other accepted content of the parent is preserved unchanged. The parent
file itself is retained byte-unchanged as historical provenance. This record
consolidates already-ratified scientific decisions, accepted CLASS_C
implementation pins, accepted r3 operational corrections, and provenance
lineage, and records the F2 → F3 gate transition. It changes no methodology.
On any conflict, v11 wins.

## 2. Scientific content — frozen BY REFERENCE, unchanged

The full model specification is NOT rederived or rewritten here. The
following are incorporated unchanged, by reference, from ART-F2 r2
(`d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4`),
ART-F2 r2a
(`2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2`), and the
PI-ratified D-F2-09 exact initialization packet
(`8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6`) with its
fixed-grid manifest
(`c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666`):

```text
D-F2-01 .. D-F2-08
D-F2-09.1 .. D-F2-09.10
D-F2-10 scientific failure/admissibility semantics
D-F2-11
D-F2-12

P-01 exact formula (WC-ADL two-sigmoid product)
P-02 exact formula (TAD/PSAT two-piece shared-beta generalized Gaussian)

u = (t - 1880)/145
T = 146
prediction = z_ddof0(g(u_grid; theta))
no amplitude/offset parameters

D-F2-08 unweighted least squares in frozen z-space

parameter support (P-01 and P-02 bounds, exactly as ratified)
Kural T (10-90% transition width >= 5 years)
Kural S (n_sup >= 3 on the stabilized 146-grid)

initialization lattice (retained starts: P-01 = 731, P-02 = 261)
feature-start rule
dedup/order rule
tie comparator (|L_a - L_b| <= 1e-12 + 1e-9 * max)

epsilon_model            = 1e-12
feasibility_acceptance_tol = 1e-8
```

Optimizer/constraint binding (STEP3-A01 corrected wording, binding):

```text
trust-constr primary optimizer, frozen options;
for P-02, the primary trust-constr path uses Bounds plus the native
scipy.optimize.NonlinearConstraint pair.

SLSQP fallback, frozen options;
for P-02, the fallback uses the two equivalent SLSQP inequality-constraint
dicts:
  s_l - s_side_min(beta) >= 0
  s_r - s_side_min(beta) >= 0

P-01, primary trust-constr:
  Bounds + LinearConstraint(c_d - c_r >= 0)
P-01, fallback SLSQP:
  equivalent inequality dict c_d - c_r >= 0
```

No optimizer literal or option is changed by this correction; the frozen
options remain exactly those of ART-F2 r2/r2a (trust-constr: jac='2-point',
hess=BFGS(), gtol=1e-10, xtol=1e-12, barrier_tol=1e-10, maxiter=500; SLSQP:
ftol=1e-12, maxiter=500).

No scientific item is reopened. No formula, bound, objective, start rule,
tie rule, or threshold is changed by this freeze.

## 3. Accepted r3 operational corrections — FROZEN

### 3.1 X1 — numerical feasibility vs scientific support

```text
numerical feasibility:
V_family(theta) <= 1e-8

scientific support:
exact returned float64 tuple
with no tolerance-based scientific waiver

feasibility_acceptance_tol does not expand scientific support
```

### 3.2 A-01 / X2 / R3-P01 / R3-P03 — construction fidelity

Independently accepted facts, frozen:

```text
declared fixture IDs    = 21
implemented fixture IDs = 21
executed fixture IDs    = 21
construction fidelity   = 21/21
required frozen manifest columns present = true
```

Provenance-mapping status:

```text
manifest exact_construction prose -> implemented_construction_key
is a HUMAN-AUDITED provenance mapping.

Machine checking establishes implemented_construction_key ==
executed_construction_key; it does not constitute automated
natural-language proof of the free-text manifest prose.
```

A-01 mechanism evidence, frozen:

```text
FIX-OTHER-NUMERICAL-FAILURE:
primary tagged test fault triggered
fallback branch entered
same x0 reused
test-only non-finite fallback return exercised
OTHER_PREDECLARED_NUMERICAL_FAILURE emitted by real failure handling

FIX-INVALID-INIT:
real initialization validator called
optimizer not called
INVALID_INITIALIZATION emitted from validator path
validator wired into real run_one_start entry for every start
no outside validator rejections
```

#### CL-R3-01 — binding freeze wording

The superseded phrase "executed_construction_key is composed at
orchestration exit" is NOT frozen. The binding wording is:

For the A-01 execution-path fixtures, executed_construction_key is
deterministically derived in the audit/executor layer from evidence returned
by the real run_one_start orchestration; the underlying evidence flags
themselves are written only at their real execution sites.

```text
classification    = cleanup only
scientific_change = false
execution_change  = false
new_harness_cycle = false
```

### 3.3 X3 — schema separation

```text
predicates        = start-level hard predicates
rejection_reasons = CLASS_C start-level rejection reasons
family_status     = family-level status
family_summary    = family-level summary
```

### 3.4 X4 — invalid-prediction guard

```text
L_INVALID_PREDICTION_GUARD = 585.0 = 4*T+1
```

Rationale:

```text
valid standardized x, ghat:
L = 2*T*(1-rho)
rho >= -1
therefore L <= 4*T = 584

585 > maximum valid D-F2-08 LS value
```

This is a CLASS_C optimizer-domain guard, not a scientific observation.

### 3.5 A-03 — internal aggregation bookkeeping

```text
valid standardized prediction:
L = objective_L(x, ghat)

invalid/nonstandardizable prediction:
L = +inf for internal aggregation bookkeeping

objective_L(x, unstandardized_g) is forbidden
```

### 3.6 A-04 / R3-P04 — display precedence

```text
display precedence does not mutate the applicable predicate set
all applicable predicates remain logged
primary_display_code follows frozen precedence
display precedence changes eligibility = false
```

Independently accepted real-classifier probe, recorded:

```text
theta  = (-1.0, 1.375, 200.0, 200.0)
family = P-01

predicates =
{MORPHOLOGY_INADMISSIBLE, ZERO_VARIANCE_FIT}

primary_display_code =
ZERO_VARIANCE_FIT
```

### 3.7 C4 / C5

```text
V_P02 uses returned finite positive beta without clipping/projection

telemetry = RUN1 optimizer-call telemetry only
RUN2      = determinism verification only
```

### 3.8 R3-P05 — telemetry provenance

```text
r3 telemetry data rows = 12

+2 rows relative to r2 correspond to
FIX-OTHER-NUMERICAL-FAILURE primary fault and fabricated fallback.

Fabricated fallback optimizer-result-like fields are TEST-ONLY SYNTHETIC
values and are not optimizer measurements.
```

No scientific or performance interpretation is attached to the telemetry.

## 4. Failure-code claim

On the basis of the r3 execution plus independent audit acceptance of
construction fidelity:

```text
all 8 STEP-2-emittable failure codes were reached through their
predeclared frozen construction modes
```

Reserved non-emitted codes/warnings remain reserved and non-emitted in
STEP 2:

```text
BOUNDARY_PATHOLOGY
IDENTIFIABILITY_FAILURE
WARN_BOUNDARY
WARN_IDENTIFIABILITY
```

No emissions are invented.

## 5. Determinism scope

r3 same-process canonical hashes:

```text
RUN1 canonical SHA256 =
6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403

RUN2 canonical SHA256 =
6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403
```

Frozen scope, exactly:

```text
determinism_scope =
exact semantic double-run determinism within the same process,
same thread-pinned environment,
same code,
same inputs,
same configuration

cross-process bitwise determinism =
not tested in F2 STEP 2
not claimed

cross-platform bitwise optimizer reproducibility =
not claimed
```

The independent replay is supporting informational evidence only and does
not broaden this claim.

## 6. Nonblocking cleanups

```text
CL-F2-01 = already cleaned in r3
           (simplified C1 expression based on actual start count)
           new_harness_cycle = false

CL-F2-02 : fixture_manifest_execution_mode_column = absent
           execution-mode representation = harness-internal provenance label
           scientific_effect = none
           (frozen fixture manifest not edited)

CL-F2-03 = omitted
           (the accepted r3 artifacts record feature-start validity/dedup
            outcomes only; no feature-start identity claim beyond that is
            supported, so none is recorded)

CL-R3-01 = binding wording frozen in §3.2 of this record
```

## 7. P-CMN.10 status-schema normalization

Normalized in this FINAL FREEZE only; r2a is not rewritten:

```text
P-CMN.10
component =
reserved BOUNDARY_PATHOLOGY / IDENTIFIABILITY_FAILURE + WARN trigger behavior

status =
CLASS_C_IMPLEMENTATION_PIN

behavior =
RESERVED_NOT_EMITTED_IN_STEP2

scientific_change = false
execution_change = false
PI_re_ratification = false
```

## 8. Final lineage table

| artifact | SHA256 | role |
|---|---|---|
| `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | normative methodology |
| `p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md` | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` | execution protocol |
| `p_konum_plus/calibration/f2_generator_specification_record_r2_2026-08-31.md` | `d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4` | scientific/operational precursor |
| `p_konum_plus/calibration/f2_generator_specification_record_r2a_2026-09-01.md` | `2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2` | scientific/operational precursor |
| `p_konum_plus/calibration/f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md` | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` | initialization custody |
| `p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv` | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` | initialization custody |
| `p_konum_plus/calibration/f2_step2_fixture_manifest_2026-09-01.csv` | `daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b` | fixture custody |
| `p_konum_plus/calibration/f2_step2_feasibility_harness_2026-09-01.py` | `45b426447803ceb0cf6c029393ca606d89a5fb006d5ab34ce4b43ca4160f86db` | historical provenance |
| `p_konum_plus/calibration/f2_step2_feasibility_telemetry_2026-09-01.csv` | `144a3b09776e05dff3c490725fda1bc17b07bd759a48033be338778889fa62f6` | historical provenance |
| `p_konum_plus/provenance/f2_step2_synthetic_analytic_feasibility_report_2026-09-01.md` | `9850075ea011fc0cad6740353abe138f6ed01acb2763803e72e5af5fe56a6d83` | historical provenance |
| `p_konum_plus/calibration/f2_step2_feasibility_harness_r2_2026-09-01.py` | `3b2555508e4b731ab3349a040a03a3d266fe068d72cd13427107a998622610bc` | superseded gate artifact |
| `p_konum_plus/calibration/f2_step2_feasibility_telemetry_r2_2026-09-01.csv` | `d688a16bfd131ee1e1cfe8715a011009b782a78a1ac897c5589cc68af3b8dabb` | superseded gate artifact |
| `p_konum_plus/provenance/f2_step2_synthetic_analytic_feasibility_report_r2_2026-09-01.md` | `9d5bf074b099cf597009218a0c16cdba68dabcdd00ee4313165c7c59c165b445` | superseded gate artifact |
| `p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py` | `01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077` | accepted execution artifact |
| `p_konum_plus/calibration/f2_step2_feasibility_telemetry_r3_2026-09-01.csv` | `cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49` | accepted execution artifact |
| `p_konum_plus/provenance/f2_step2_synthetic_analytic_feasibility_report_r3_2026-09-01.md` | `afd02531cf80fa441ad2d6e3b990583783963fc6042b87c98f0108af0629abf5` | accepted execution provenance |
| `p_konum_plus/provenance/f2_step2_r3_independent_audit_2026-09-02.md` | `f4f2cc2702efdc1e6b0eb0804c847e93420e439c2425961810304eefb9b3048c` | independent acceptance audit |
| `p_konum_plus/calibration/f2_generator_specification_record_FINAL_FREEZE_2026-09-02.md` | `2f191f0b0b24d962dfb0356be0daf201810ae9cb85d46b4164907cc43cce91f6` | superseded gate artifact (parent freeze, STEP3-A01) |
| `p_konum_plus/provenance/f2_step3_final_freeze_report_2026-09-02.md` | `41c7ce03558d8ab6cd4e8c7aa6c088cf52763288eb57029dad095a33c882f3f1` | historical provenance (parent STEP-3 report) |
| `p_konum_plus/provenance/f2_step3_final_freeze_independent_audit_2026-09-02.md` | `8bd0fb33f7c507829ec4ca253dd0a2cb2a5f7a05c65601a2c6f9f74de71e5630` | independent acceptance audit (STEP-3, identified STEP3-A01) |

Only the first row is normative. All other rows are non-normative custody,
precursor, provenance, or acceptance artifacts.

## 9. Final gate transition

```text
F2_STEP_1   = COMPLETE
F2_STEP_1_5 = COMPLETE
F2_STEP_2   = ACCEPTED
F2_STEP_3   = COMPLETE

ART_F2_FINAL_FREEZE = COMPLETE

F2_complete = true
F3_allowed  = true

generator_selected = false
P03_touched = false
P04_touched = false
P05_touched = false
F3_started  = false
```

F3_allowed means permission to begin a separately governed F3 task.
No F3 execution occurred during STEP-3 Final Freeze or its r1 correction.

Next action only:

```text
F3 — separately governed generator adequacy / selection stage
```
