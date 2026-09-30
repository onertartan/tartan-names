# p_konum_plus — F3 STEP-2 PI-ratified content

## 1. Authority, identity and scope

```text
record_date = 2026-09-07
record_revision = r2
revision_reason = synthesis of ChatGPT, Claude Chat and Manus recommendations
parent_content_sha256 = 5ca42d4a84e3f7851ea91cc376ec00f213d75288a8bfb460545aaf481355185c
status = PI_RATIFIED_CONTENT
PI = Öner
prepared_by = ChatGPT, recording the PI-authorized recommendation package
repository_target = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
S-1 = (a)
S-2 = α
T-1 = AUTHORIZE
T-2 = T-2a
T-3 = AUTHORIZE
T-4 = T-4a
T-5 = CONFIRM_WITHIN_SCOPE
mandatory_decision_fields_complete = true
```

Authority is the PI's instruction in this conversation to issue this named file following the explanation of the complete recommendation package. The PI authorizes recording the adopted package; ChatGPT supplies the operational wording. This is not a claim of a handwritten signature, independent qualification, or completed repository dispatch.

This record supplies the decision content required by §4.3 of the correction execution prompt. It supersedes the unfilled decision-content slots of the earlier DRAFT_INCOMPLETE file; it does not edit historical files. S-1 is a PI-approved operational definition, and S-2 is a narrow amendment to the SOLVER-B acceptance-error policy. The implementation executor may not invent further scientific rules.

Source hierarchy: v11 remains the sole normative methodology; the frozen F2 and ratified F3 STEP1 contracts govern except for the explicit S-1 operationalization and S-2 amendment recorded here. Audit and advisory records remain nonnormative.

| Source | SHA256 |
|---|---|
| F3 STEP1 corrected ratification candidate r4, 2026-09-05 | 5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad |
| F3 STEP1 PI ratification freeze record r1, 2026-09-05 | 7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460 |
| F3 STEP2 correction execution prompt DRAFT v6 | 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 |
| Frozen spline qualification harness r2, 2026-09-03 | b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d |

The DRAFT v6 hash identifies the decision schema and scope used here. It is NOT a PI instruction to dispatch that draft, nor a replacement for the separate P-4 dispatch hash check.

## 2. S-1 — PIN-A5-SUPPORT: data-level half-range support

**Decision: (a). The following operational definition is adopted.**

### 2.1 Reference and membership

For each trajectory i, let z_i be its existing full-data, finite, normalized reference vector on the frozen 146-point index grid G = {0, …, 145}. Use the same reference vector for P-01, P-02 and the spline benchmark. Do not derive it from a fitted curve, normalize it anew for a probe, smooth it, or recompute it after masking.

Define, in the existing float64 arithmetic:

```text
lo_i = min(z_i)
hi_i = max(z_i)
thr_i = lo_i + 0.5 * (hi_i - lo_i)
S_i = { t in G : z_i[t] >= thr_i }
```

Use the displayed evaluation order; do not algebraically substitute a different threshold formula. Equality is included. There is no epsilon, rounding band, support-size threshold or tolerance. Compute the support once from the full reference vector and reuse it for both probes and all fitters.

S_i is the union of ALL qualifying indices, including disconnected components. Do not select the largest component or replace the set by its interval hull.

### 2.2 Edge containment

Use the frozen E = 15 masks:

```text
M_LEFT  = {0, …, 14}
M_RIGHT = {131, …, 145}
O_side = G \ M_side
A5_i(side) = (S_i is a subset of M_side)
           = (S_i intersect O_side is empty)
```

Evaluate LEFT and RIGHT separately against their own masks. If even one support index remains observed, condition (i) is false for that side. The test is exact set containment; “fewer than three support points remain” is not this rule.

### 2.3 Degenerate and invalid references

For a finite constant reference (hi_i = lo_i), the formula gives S_i = G. Thus condition (i) is false for either frozen 15-point edge mask. This specifies the support predicate only: it does not make a constant trajectory eligible, override existing normalization/zero-variance rules, or declare any refit admissible. Where the upstream contract rejects such a reference, that rejection is retained; no replacement vector is manufactured.

For a nonempty finite reference and finite threshold, the maximum belongs to S_i, so S_i cannot be empty. Missing, non-finite or wrong-length reference input, a non-finite computed threshold, or an unexpectedly empty computed support is a reference/computation contract violation. Record the context and stop the affected evaluation path under the existing contract-consistency/exactness reporting protocol. Do not use vacuous containment, impute the reference, remove invalid entries, or turn this violation into a scientific C4 pass/fail observation. Unaffected paths remain governed by the existing execution protocol.

### 2.4 Relationship to the other A.5 clauses

Let F_i,side,fitter denote failure under the unchanged clauses: (ii) the observed-only feature start is rejected AND every frozen grid start fails, or (iii) the truncated refit is inadmissible. The adopted condition (i) is an additional OR condition:

```text
A5_failure = A5_i(side) OR A5_ii(side, fitter) OR A5_iii(side, fitter)
```

When any A.5 failure condition holds: the probe fails C4a (numerator excluded, denominator retained) and is absent from the C4b paired-valid set. No imputation or sentinel is introduced. Otherwise the frozen eligible-admissible-endpoint rule determines probe_success. A false condition (i) alone never establishes probe success.

Record condition (i) separately. If fitting is skipped because condition (i) already establishes failure, unexecuted conditions (ii)/(iii) must be marked not evaluated, not fabricated as false or pass. Existing full-data reference eligibility requirements for C4b pairing remain unchanged; they are not newly imposed on C4a probe_success.

This is an operational support definition for the observed reference trajectory, not a claim of recovering latent noise-free support. Its sensitivity to noise/extremes is acknowledged. No empirical SSA outcome was used in drafting it in this session.

### 2.5 Synthesis rationale and scientific limitations

The PI retains option (a) after considering the Manus recommendation of option (b) and the Claude Chat recommendation of option (a). This revision does not change support membership, masks, edge-case behavior, acceptance policy or any T decision adopted above.

The two objects must be distinguished: F2 defines support on a stabilized fitted curve; this S-1 decision applies the half-range construction to the observed full-data reference z-trajectory. Transferring the construction to that reference is an explicit PI-approved operationalization, not an identity already established by the frozen F2 definition.

Option (a) is retained because it supplies one fitter-independent support set for each trajectory. Its threshold depends on the observed minimum and maximum; extreme observations and noise can move the threshold and alter which indices belong to the set. This can affect whether an edge mask contains the entire support. The decision makes no claim of estimating latent noise-free support or of empirical superiority over a fit-based definition.

Option (b) remains a scientifically defensible alternative in principle. A common designated spline reference could preserve a common region across candidates, while introducing dependence on that model, its fit validity and its stability. Candidate-specific references could produce different regions. Merely using a stabilized fitted curve does not prove robustness to data perturbations. The Manus note does not fully designate the reference fit and its invalid-fit behavior; it therefore does not supply a complete replacement specification. No alternative fit-based rule is authorized by this record.

No smoothing, robust-range substitute, threshold search or empirical comparison was performed or authorized in this synthesis. The selected data-level definition is justified by its common-reference design and explicit semantics; its statistical performance remains unverified. The constant-reference and invalid-reference handling in §2.3 is explicit adopted operational content and must not be described as a verbatim quotation of an upstream frozen rule.

Document drafting and scientific authorization are distinct: ChatGPT prepared the complete wording at the PI's request; the PI authorized the package in this conversation. Claude Chat's incomplete definition slot and Manus's alternative recommendation are advisory inputs, not competing ratifications. Review scores compare document quality and are not evidence of scientific validity or qualification.

## 3. S-2 — PIN-SOLVER-B-UNVERIFIABLE: α

**Decision: α. The following narrow acceptance-error policy is adopted.**

### 3.1 Covered event

The covered event is a `RuntimeError` raised by the `nnls(A[act].T, g)` invocation in frozen `kkt_res(c, z, O, A)` while that invocation is being used by `accept(c, z, O, A)` to compute the KKT-existence certificate for a SOLVER-B stage-1 or stage-2 acceptance check.

Identify the call context and exception origin, not merely the exception class or message. An NNLS call in `polish()` is a different site and is NOT covered. Errors in optimization, objective evaluation, polishing, loading, unrelated runtime code, or non-RuntimeError exceptions are not converted into acceptance failure by this amendment; retain the existing error/exactness protocol for them.

### 3.2 Effect and stage progression

On the covered event, record the evidence and return NOT ACCEPTED for that acceptance check. Treat the result exactly as the existing `accept()` false branch at that stage:

- Stage 1 acceptance error: enter the existing stage-2 expansion/polish branch, using its existing input and settings.
- Stage 2 acceptance error: enter the existing stage-3 SLSQP branch, using its existing input and settings.
- Stage 3 retains its existing acceptance rule; no new KKT requirement or exemption is created there.

Do not restart the chain, skip an eligible stage, label the whole mode invalid solely because of the certificate exception, or fail the whole trajectory solely because of that event. Subsequent acceptance is NOT guaranteed. When later stages fail or produce an ineligible endpoint, the existing terminal and admissibility rules govern.

### 3.3 Implementation boundary and evidence

Use the disclosed runtime wrapper approach around the loaded acceptance path. Keep frozen source files byte-unchanged. Preserve all existing feasibility, KKT and optimizer literals; no retries, tolerance relaxation, alternative certificate solver or approximate acceptance is authorized.

Capture fixture, sex, trajectory, mask, mode, acceptance stage, exception type, message and full traceback. Restore any temporary runtime instrumentation after its intended scope. Test-only injection must target the covered call context and be manifest-declared. Unrelated exceptions must remain distinguishable and must not be swallowed by a broad mode-level catch.

T-1 AUTHORIZE enables the loaded spline path. This decision closes the missing policy definition; implementation correctness and synthetic qualification still require the prescribed future tests.

## 4. T-1 — AUTHORIZE the bounded spline loader extension

For the frozen spline harness identified in §1 only, authorize the base retain classes from the correction prompt (Import, ImportFrom, FunctionDef, ClassDef, constant Assign) plus the explicitly listed definitional-support nodes before the orchestration marker `# ---------------- steps 1-3`:

```text
U, KNOTS, TC_OPTS, SLSQP_OPTS, B, the two asserts on B,
D1 and its for-loop, C_INT, C_DEC, C_INC, C_RIGHT, MASKS,
COEF_MAP, CFG_FIELDS, the docstring Expr, the thread-env loop,
and the three path strings
```

This is the bounded 21-prelude-node extension stated in prompt v6 §4.2. No orchestration block is authorized. Record exact retained-node identities, order and source hashes; enforce the existing execution-list and I/O-free checks. Source mismatch or inability to satisfy those checks is reported under the existing protocol, not resolved by expanding this authorization. Spline non-regression remains mandatory.

## 5. T-2 — T-2a wrapper qualification

Authorize a fixture-type-dispatching qualification adapter. Replay FIX-P01-BENIGN and FIX-P02-BENIGN through `fit_family(mask=FULL)`; run other F2 fixtures through their frozen constructions. Preserve each fixture's own start-bank composition, order and feature-start behavior through explicit parameters. Do not apply the F3 FULL_LATTICE default implicitly to F2 replay fixtures.

Require the existing complete canonical equality and telemetry/endpoint comparisons specified in the correction prompt. Similar output under a different bank does not qualify as exact replay. NR-01(i) remains mandatory independently of NR-01(ii).

If the adapter cannot meet the contract without prohibited modification, record ENG-03 and stop the affected qualification path. Do not switch automatically to T-2b or claim its narrower evidence meets T-2a. This authorization is not a prediction of test success.

## 6. T-3 — AUTHORIZE K-05 wording correction

Adopt the corrected coverage-row wording:

```text
K-05 invariant: C4b completeness PASS implies C4a PASS.
The excluded combination is C4b-completeness-PASS + C4a-FAIL.
C4b-completeness-FAIL + C4a-PASS is a legitimate case (INJ-C4B-FLOOR-FAIL).
```

This is the specified wording correction; it changes no criterion, threshold or outcome rule.

## 7. T-4 — T-4a per-optimizer-call telemetry

Authorize a disclosed recording wrapper around `scipy.optimize.minimize` in the loaded spline namespace. Produce one row per trust-constr and SLSQP call with status, message, nit, nfev, njev, wall time and objective, associated with its fit/mode/stage context.

Preserve inputs, return values, exceptions, optimizer settings and numerical behavior. Behavior neutrality must be demonstrated under the existing verification contract; it is not assumed proven by this record. Missing metrics are labelled unavailable with their reason, not fabricated as measured values. Do not silently substitute T-4b. Timing observations are not scientific thresholds or deterministic-output equality targets.

## 8. T-5 — CONFIRM_WITHIN_SCOPE

Confirm the disclosed masked-objective runtime rebinding mechanism: FULL uses the frozen path without rebinding; non-FULL temporarily rebinds `f2.make_objective_and_x` to the masked factory and restores it afterwards. Frozen run_one_start, primary/fallback chain, classification and aggregation execute unmodified. The existing masked objective and its guards remain binding. No alternate optimizer chain is authorized.

This records the existing permitted status quo explicitly; T-5's optional nature is unchanged.

## 9. Literal and verification boundaries

The half-range coefficient 0.5 and inclusive membership operator are PI-ratified S-1 content in this data-level application, not executor-created scientific literals. Grid length 146 and edge length 15 are inherited frozen structural values. No new optimizer tolerances or statistical thresholds are introduced. Record PI_RATIFIED attribution to this file's externally computed hash in the implementation register.

Future verification must distinguish threshold equality, disconnected support, support partly observed versus fully masked, finite constant reference behavior, invalid-reference contract failure, stage-1 versus stage-2 covered exceptions and unrelated exceptions. These are test obligations, not results from this document-preparation task.

Corrected criterion-specific U2/U3/U4/U5 common-valid supports and P03/D-P04 rules remain governed by the ratified contract. This record does not restore the withdrawn completion-only interpretation.

## 10. Dispatch and end state

```text
PI_decision_content = COMPLETE
S_T_values = RATIFIED_AS_RECORDED
implementation_executed_by_this_task = false
qualification_executed_by_this_task = false
custody_P1 = NOT_VERIFIED_BY_THIS_RECORD
dispatch_prompt_hash_P4 = TO_BE_RECORDED_AND_CHECKED_AT_DISPATCH
F2 = CLOSED
F3_STEP1 = FROZEN (S-1 operationalization and S-2 amendment explicitly recorded above)
F3_STEP2_qualification = NOT_DECLARED
F3_EXECUTION_READY = false
commit = false
```

P-4 does not require its record to be embedded in this file. The PI's dispatch instruction/record must identify the actual execution prompt and its hash; verify equality there. The schema-reference hash in §1 is not dispatch approval.

All remaining execution-prompt custody and dispatch conditions still apply. Nothing here asserts that required repository files are present or hash-exact, that a DRAFT prompt has become dispatchable, or that synthetic qualification has passed. No real SSA/F1 fit, empirical threshold computation, generator selection, F4 or algorithm×CVI execution is authorized by this file alone.
