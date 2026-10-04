# p_konum_plus — rp1 — C-5 (D-8 PI-2 (iii)/(iv)) Observability Statement

```text
artifact_role = deliverable G (rp1 instruction §8): the statement rp1 instruction
                §4 C-5 requires -- whether a refit that completes numerically but
                is inadmissible under the frozen taxonomy is visible in the output
                or telemetry the harness already receives, with line citations into
                the frozen F2 engine and the frozen spline harness
status        = NON-NORMATIVE (report-only; introduces no new classification, no
                frozen-code change, no scientific object)
date          = 2026-10-04
revision      = rp1 (F3 real-data preparation cycle, inside the r4 lineage)
frozen engines cited = f2_step2_feasibility_harness_r3_2026-09-01.py
                       (01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077)
                       f3_spline_solver_qualification_harness_r2_2026-09-03.py
                       (b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d)
```

## 1. The question (D-8 PI-2 (iii))

Is a refit that **completes numerically** (the optimizer returns a finite,
well-formed endpoint) but is **inadmissible under the frozen taxonomy**
(the endpoint fails the frozen morphology/acceptance rule, not a numerical
failure) visible in the output or telemetry the harness already receives —
on both the family side (F2 engine) and the spline side (spline harness) —
without changing any frozen code or adding a new classification?

**Answer: yes on both sides.** The event is already fully determined by
existing fields; nothing frozen needs to change to observe it.

## 2. Family side — f2_step2_feasibility_harness_r3_2026-09-01.py

The frozen `classify_endpoint` path computes, in order:

| step | field | line(s) |
|---|---|---|
| numerical feasibility | `num_feasible` (→ returned as `numerically_feasible`) | L265, L268, L310 |
| morphology rule, part 1 | `kural_t` (`kural_t_pass_exact_p01`/`_p02`) | L277 |
| morphology rule, part 2 | `kural_s` (`kural_s_pass_exact`) | L286–288 |
| morphology predicate | `"MORPHOLOGY_INADMISSIBLE"` added to `predicates` iff `theta_finite` and NOT (domain_pass AND kural_t AND kural_s) | L290–291 |
| aggregate admissibility | `eligible` — conjoins `theta_finite`, `num_feasible`, `domain_pass`, `kural_t`, `kural_s`, finiteness, and `len(predicates) == 0` | L299–305 |

A **numerically completed but inadmissible** family start is exactly the
case `eligible is False`, `predicates == ["MORPHOLOGY_INADMISSIBLE"]` (no
other predicate — in particular not `OPTIMIZER_NONCONVERGENCE`, L293–294,
which would mean the numerical side itself failed), `numerically_feasible
is True`, and `theta_finite is True`. Every one of these four fields is
already returned by the frozen `classify_endpoint` in its result dict
(L307–…); no frozen line is touched to observe the conjunction.

rp1 implements the read-only predicate as `family_start_inadmissible_completed`
(`f3_step2_adequacy_harness_rp1_2026-10-02.py` L3059–3066), called at both
of `run_one_start`'s cache paths (cached: L1095; freshly computed: L1104),
incrementing the report-only counter `INADMISSIBLE_COMPLETED["family_starts"]`
(L3056 for the counter's definition).

## 3. Spline side — f3_spline_solver_qualification_harness_r2_2026-09-03.py

The frozen per-mode driver (`accept`, L308; stage sequence L340–405, SOLVER-B
config L139–151) populates a `tel` dict with, among others:

| field | meaning | line(s) |
|---|---|---|
| `primary_status` | the primary (trust-constr) solver's own success flag, as a string `"True"`/`"False"` | L370, L379, L383 |
| `stage1_accept` | stage-1 post-polish acceptance, or `"NOT_APPLICABLE"`/`"NOT_REACHED"` | L365, L386 |
| `stage2_accept` | stage-2 post-polish acceptance (re-identified from the same `c_tc`) | L365, L394, L405 |
| `fallback_status` | stage-3 fallback solver's acceptance, or `"NOT_INVOKED"` | L365–367, L375, L401 |
| `final_endpoint_source` | which stage's endpoint was actually delivered: `PRIMARY`/`POLISH`/`POLISH_EXPANDED`/`FALLBACK` | L372, L380, L388, L396, L402 |

The acceptance rule itself (`SOLVER-B`'s `primary_success_rule`,
`stage1_postpolish_rule`, `stage2_postpolish_rule`, `stage3_acceptance_rule`)
is declared at L139–151 and is the frozen taxonomy: trust-constr status in
`{1,2}` AND finite endpoint AND finite objective (plus, from stage 2
onward, the KKT/residual conditions named there).

A **numerically completed but inadmissible** spline mode is exactly the
case where the primary solver itself returned cleanly (`primary_status ==
"True"` — the optimizer *completed*) but **no stage's acceptance rule
accepted the result** — i.e. `stage1_accept` and `stage2_accept` are never
`"True"`, `final_endpoint_source` is never `"PRIMARY"`, and `fallback_status`
is never `"True"`. Every one of these fields is already in the `tel` dict
the frozen stage drivers return; no frozen line is touched to observe the
conjunction.

rp1 implements the read-only predicate as `spline_mode_completed_not_accepted`
(`f3_step2_adequacy_harness_rp1_2026-10-02.py` L3069–3081), called at both
of `fit_spline`'s paths — the cached path reads the flag back from the 8th
tuple element stored alongside the mode at L1245–1247 (so a resumed process
counts identically to the one that originally computed the unit — the same
discipline T-STORE-READ-ACCOUNTING's own resume-robustness fix relies on);
the fresh path computes it directly at L1299–1304 (guarded by `not
mode_unrelated`, since an `UNRELATED` exception capture is a different,
already-handled event class, not a clean-but-inadmissible completion),
incrementing `INADMISSIBLE_COMPLETED["spline_modes"]`.

## 4. The counter is report-only (no frozen change, no new classification)

`INADMISSIBLE_COMPLETED = {"family_starts": 0, "spline_modes": 0}`
(L3056) is read ONLY from fields the frozen engines already return. It:

- changes no frozen line in either engine (both stay at their pinned
  hashes, verified every launch — `PIN-F2-IMPORT-HASH`, `PIN-SPLINE-IMPORT-HASH`);
- adds no new predicate, status code, or eligibility rule to either engine;
- enters no scientific object (`evaluations`, `stops`, the canonical
  document, the residual series are all untouched by it);
- is carried into `results["inadmissible_completed_counts"]`
  (`f3_step2_adequacy_harness_rp1_2026-10-02.py` L4858, post attempt-5 edit)
  as a report-only
  block, declared `E` in its entirety under `EXPECTATIONS_E` ("C-5
  ADDITION (not in r4-2)").

## 5. Verification — T-INADMISSIBLE-OBSERVABLE (mandatory test)

`t_inadmissible_observable` (L3084–…) exercises both predicates against
synthetic inputs built from the frozen engines' own vocabulary, with
expected outcomes written before the calls:

- **family**: seeks a WITNESS endpoint on the frozen P-01/P-02 start
  lattices by calling `classify_endpoint` directly (no optimizer run, no
  frozen code change); asserts the predicate does NOT fire on a synthetic
  `eligible=True` record nor on a synthetic nonconverged
  (`OPTIMIZER_NONCONVERGENCE`) record.
- **spline**: asserts the predicate is `True` on a synthetic
  clean-return-not-accepted `tel` dict and `False` on synthetic
  accepted-stage and dirty-return `tel` dicts.

Observed in every clean rp1 run (attempts 2 and 4; not reached by attempts
1/3, which stopped earlier): `witness_on_frozen_lattice = false` (no P-01/P-02
start-bank lattice point happens to land in the morphology-inadmissible-only
region for these fixtures — a negative result the test reports, not fails,
per §(a) above: "If no lattice point classifies as morphology-only-
inadmissible, that is reported (not failed)"), `eligible_not_counted = true`,
`nonconverged_not_counted = true`, `infeasible_not_counted = true`,
`clean_not_accepted_counted = true`, `accepted_stage1_not_counted = true`,
`accepted_primary_not_counted = true`, `dirty_return_not_counted = true`,
`pass_ = true`.

## 6. Carried forward (D-8 PI-2 (iv))

Both counters and the predicates behind them are carried into the real-data
execution instruction unchanged. Any family-start or spline-mode event in
**real data** that the predicates above classify as numerically-completed-
but-inadmissible goes to the PI (D-8 PI-2 (iv)) — this statement does not
decide what happens to such an event, only that it is observable.

```text
real_data_access = false throughout this statement's derivation (every line
cited above was read from the frozen, already-delivered engine files and the
rp1 harness; no SSA/F1 file was opened)
commit = false
```
