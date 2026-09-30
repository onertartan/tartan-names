# p_konum_plus — F2 STEP 2 CORRECTED Full Rerun (X1–X4 / C1–C5) — Successor Report

```text
artifact_role         = F2 STEP-2 corrected full-rerun execution provenance
status                = NON-NORMATIVE
parent_execution_report = f2_step2_synthetic_analytic_feasibility_report_2026-09-01.md
correction_scope       = X1_exact_scientific_support + X2_fixture_manifest_registry_fidelity
                        + X3_family_summary_schema + X4_invalid_prediction_objective_domain_guard
                        + C1_C5_execution_clarifications
new_methodology_review = false
PI_re_ratification     = false
```

**The original STEP-2 report is retained as immutable historical provenance;
its independent-acceptance verdict is superseded by this corrected rerun for
purposes of STEP-2 gate acceptance.** The old report was not rewritten.

- **Date:** 2026-09-01
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`

---

## 1. Lineage and correction reason

Triggered by an independent artifact audit of the completed STEP-2 execution, which found two gate-specific execution gaps (X1, X4) and two cleanup items (X2, X3), plus five execution clarifications (C1–C5). No global blocker was found; no new methodology review was authorized; no ratified scientific decision changed.

## 2. Repo/hash precheck — PASS

Root ✓, branch `p_konum_plus` ✓, HEAD = expected `3e4daf47018f124e29717263e4e45fe90c8e52b8` ✓. Zero unexpected tracked modifications. Governing hashes (recomputed, all exact):

| document | SHA256 |
|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` |
| ART-F2 r2a | `2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2` |
| ART-F2 r2 (parent) | `d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4` |
| D-F2-09 exact packet | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` |
| D-F2-09 fixed-grid manifest | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` |
| STEP-2 fixture manifest | `daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b` |

No mismatch; no STOP.

## 3. Historical artifact custody hashes (pre-task, re-verified post-task)

| artifact | hash | pre/post |
|---|---|---|
| historical harness `f2_step2_feasibility_harness_2026-09-01.py` | `45b426447803ceb0cf6c029393ca606d89a5fb006d5ab34ce4b43ca4160f86db` | identical |
| historical telemetry `f2_step2_feasibility_telemetry_2026-09-01.csv` | `144a3b09776e05dff3c490725fda1bc17b07bd759a48033be338778889fa62f6` | identical |
| historical report `f2_step2_synthetic_analytic_feasibility_report_2026-09-01.md` | `9850075ea011fc0cad6740353abe138f6ed01acb2763803e72e5af5fe56a6d83` | identical |
| ART-F2 r2a | `2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2` | identical |

None of these four files were overwritten, edited, renamed, deleted, or normalized. `original_STEP2_harness_unchanged = true`, `original_STEP2_telemetry_unchanged = true`, `original_STEP2_report_unchanged = true`, `ART_F2_r2a_unchanged = true`.

## 4. Fixture manifest custody + registry fidelity

```text
pre-hash  = daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b
post-hash = daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b   (IDENTICAL)
```

The manifest was neither edited nor regenerated; the successor harness reuses the existing 21-fixture manifest verbatim.

**Registry fidelity (X2):**

```text
declared_fixture_ids (21)  == implemented_fixture_ids (21)   -> pre_execution_bijection_ok = true
executed_fixture_ids (21, excluding 3 harness self-tests)
                            == declared_fixture_ids           -> post_execution_bijection_ok = true
undeclared_executed_fixture_ids       = []
declared_but_unexecuted_fixture_ids   = []
metadata_mismatches (fixture_class, family cross-check)= []
execution_mode column status          = NOT_PRESENT_IN_MANIFEST  (not invented; honestly reported —
                                        the original manifest has no execution_mode column)
```

The three X1/C3 harness self-tests (`SELFTEST-X1-P01-ORDER`, `SELFTEST-X1-P02-SMIN`, `SELFTEST-C3-DISPLAY-PRECEDENCE`) are excluded from the bijection sets and were not added to the frozen fixture manifest, per governing-prompt §5.

## 5. X1 — exact scientific-support correction

The historical harness's Kural-T checks embedded numerical slack directly into the "exact" rule (`width_years >= 5 - 1e-9` for P-01, `s >= s_min - 1e-12` for P-02) — a silent tolerance-based scientific waiver. The successor harness:

- Keeps `FEASIBILITY_ACCEPTANCE_TOL = 1e-8` and the existing `V_P01`/`V_P02` numerical logic **unchanged**, used only for `numerically_feasible`/`POST_RETURN_CONSTRAINT_REJECTION` (a CLASS_C start-level rejection reason, never a scientific predicate).
- Adds an **independent** `scientific_domain_pass_p01`/`_p02` function using the returned float64 tuple exactly as represented — zero tolerance, no clipping, no projection, no rounding — checking the full box/order support (`-1<=c_r,c_d<=2`, `c_r<=c_d`, `K_MIN<=k_r,k_d<=K_MAX` for P-01; `-1<=m<=2`, `1<=beta<=6`, `s_l,s_r<=3`, `s_l,s_r>=s_side_min(beta)` for P-02).
- Adds `kural_t_pass_exact` (width formula, **no** `-1e-9`) and reuses the always-exact `kural_s_pass_exact` (`n_sup>=3`, unchanged formula — it never had a tolerance bug).
- Eligibility now requires **all four** — `numerically_feasible AND scientific_domain_pass AND kural_t_pass_exact AND kural_s_pass_exact` — plus finiteness and no other hard predicate. Any exact-support/Kural-T/Kural-S failure emits `MORPHOLOGY_INADMISSIBLE`, independent of and in addition to any `POST_RETURN_CONSTRAINT_REJECTION`; both are logged if both occur.

A floating-point round-trip check was performed before implementation: at the exact ratified boundary `k=K_MAX`, recomputing the width formula gives `5.000000000000001 >= 5.0` (rounds slightly above, never below), so the zero-tolerance check does not spuriously reject boundary-exact D-F2-09 grid points.

## 6. X1-P01-ORDER result

```text
theta = (0.500000005, 0.500000000, 20.0, 20.0)
V_P01 = 4.999999969612645e-09   (<= 1e-8; numerically_feasible MAY be true)
scientific_domain_pass = False   (c_r <= c_d is exactly false: 0.500000005 > 0.500000000)
MORPHOLOGY_INADMISSIBLE emitted = True
eligible = False
SELFTEST RESULT = PASS
```

## 7. X1-P02-SMIN result (`beta=sqrt(6)`)

```text
beta = 2.449489742783178  (== math.sqrt(6.0) exactly, confirmed: beta_is_sqrt6_exact = True)
m = 0.5 ; s_l = s_side_min(beta) - 5e-13 ; s_r = s_side_min(beta)
V_P02 = 5.000028169277471e-13   (<= 1e-8; numerically_feasible MAY be true)
scientific_domain_pass = False   (s_l >= s_side_min(beta) is exactly false)
MORPHOLOGY_INADMISSIBLE emitted = True
eligible = False
SELFTEST RESULT = PASS
```

Both self-tests demonstrate exactly what X1 requires: an endpoint that the numerical tolerance would accept is correctly rejected on exact scientific grounds.

## 8. X2 — manifest/registry fidelity result

```text
pre_execution_bijection_ok  = true
post_execution_bijection_ok = true
undeclared_executed_fixture_ids     = []
declared_but_unexecuted_fixture_ids = []
metadata_mismatches (fixture_class/family) = []
execution_mode_column_status = NOT_PRESENT_IN_MANIFEST
```

## 9. X3 — family-summary schema result

Canonical records now carry `predicates` (start-level hard-failure predicates only), `rejection_reasons` (CLASS_C only), `family_status` (`null` for ordinary start-level records; `"OK"` or `"FAMILY_FIT_FAILURE"` for the family-aggregation summary record), and `family_summary` (`null`, or `"NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART"` when applicable). No aggregation decision changed — `FIX-FAMILY-FIT-FAILURE` still resolves to the same family-level outcome, now expressed with `predicates=[]`, `family_status="FAMILY_FIT_FAILURE"`, `family_summary="NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART"` instead of the label living inside `predicates`.

## 10. X4 — invalid-prediction objective-domain guard result

```text
historical literal 1.0e6         = ABSENT  (confirmed by source grep: 0 occurrences as a code
                                   literal; the only 3 matches are prose/comments documenting removal)
successor guard                  = L_INVALID_PREDICTION_GUARD = 585.0  (== 4*T+1 == 4*146+1, exact)
status                            = CLASS_C_OBJECTIVE_DOMAIN_GUARD
scientific_estimand               = none
usage                             = returned ONLY from inside the numerical optimizer's internal
                                    objective wrapper when the stabilized prediction cannot be
                                    z-normalized (NONFINITE_FIT / ZERO_VARIANCE_FIT); never written
                                    to telemetry; never used in classification, eligibility, or
                                    family comparison — final endpoint classification runs
                                    independently through X1 / epsilon_model / exact scientific
                                    support / Kural T/S exactly as for any other endpoint
```

D-F2-08 itself is unchanged: for every valid nonconstant prediction the sole scientific objective remains `L(theta) = sum_j [x_j - ghat_j(theta)]^2`, unweighted, in frozen z-space.

## 11. C1–C5 execution clarifications

**C1 — benign PASS criterion:** restored exactly: complete predeclared mini-bank executes without an unhandled harness exception AND every selected start yields a structured terminal record AND at least one endpoint is eligible under the corrected X1 semantics. Result: `p01_benign.c1_pass_criterion = true`, `p02_benign.c1_pass_criterion = true` (both `has_eligible_endpoint = true`).

**C2 — X1-P02-SMIN exact tuple:** used `beta = sqrt(6)`, `m = 0.5`, `s_l = s_side_min(beta) - 5e-13`, `s_r = s_side_min(beta)` exactly as specified — confirmed §7.

**C3 — display-precedence self-test:** result below (§16).

**C4 — no beta clamp in V_P02:** the historical `s_side_min(max(min(beta, BETA_MAX), BETA_MIN))` clamp was removed. Corrected `v_p02`: if `beta` is nonfinite or `<=0`, returns `float("inf")` (an infinite numerical-violation sentinel) without attempting `s_side_min`; otherwise evaluates `s_side_min(beta)` at the **returned** beta exactly, no projection. Scientific support (`1<=beta<=6`) is checked independently and exactly under `scientific_domain_pass_p02`/`kural_t_pass_exact_p02`.

**C5 — telemetry run ownership:** `telemetry_run = RUN1`. The successor telemetry CSV (`f2_step2_feasibility_telemetry_r2_2026-09-01.csv`) contains only RUN1's 10 optimizer-call rows; RUN2 exists solely for semantic determinism verification and was never appended to the CSV.

## 12. Confirmation: prior boolean-bug fix preserved, and a second instance found and fixed

The historical fix (`bool(kural_t) and bool(kural_s)` instead of `kural_t is True`/`kural_s is True`) is preserved verbatim in the corrected `classify_endpoint`. During this correction pass a **second instance of the identical bug class** was found and fixed: the harness's own X1 self-test verdict computation (`pass_=...`) initially used `cls_order["scientific_domain_pass"] is False`, which is always `False` for a `numpy.bool_(False)` (identity, not equality) — silently reporting `pass_=False` even though the underlying classification (`scientific_domain_pass=False`, `MORPHOLOGY_INADMISSIBLE` emitted, `eligible=False`) was already correct. Fixed by (a) wrapping the self-test comparisons in `bool(...)` and (b) — as the more durable fix — casting `scientific_domain_pass`/`kural_t_pass_exact`/`kural_s_pass_exact` to genuine Python `bool`/`None` at the source, inside `classify_endpoint`, so every downstream consumer (canonical records, self-tests, JSON serialization) receives clean values. Both fixes are pure Python-correctness corrections; no scientific rule, bound, or threshold was touched. The harness was re-executed in full (both runs) after this fix; all results in this report are post-fix.

## 13. Complete corrected rerun results

Full RUN1 canonical suite: 29 canonical records (21 declared fixtures fully executed — several fixtures emit more than one canonical record, e.g. per-start plus a family-aggregation record) + 3 harness self-test records, serialized separately per governing-prompt §10. All results below come from this corrected full rerun — no historical PASS output was reused or copied forward.

- **P-01 benign mini-bank** (`grid[0]`, `grid[365]`, `grid[730]`, `feature`): all 4 starts executed via the frozen primary `trust-constr` contract without unhandled exception; 3 of 4 eligible under the corrected exact rule (`grid[730]` legitimately `MORPHOLOGY_INADMISSIBLE` — a real Kural-S failure at that converged endpoint); aggregation `OK`.
- **P-02 benign mini-bank** (`grid[0]`, `grid[130]`, `grid[260]`, `feature`): all 4 starts executed without unhandled exception; all 4 eligible; aggregation `OK`.
- **Stable-evaluation fixtures** (P-01 interior/boundary, P-02 interior/`s=s_side_min(beta)` boundary): all evaluate without exception.
- **`FIX-P01-ZEROVAR-IN-DOMAIN`**: `ZERO_VARIANCE_FIT`, `sigma_g = 0.0` exactly.
- **`FIX-P01-KURAL-S-FAIL`**: `MORPHOLOGY_INADMISSIBLE` (both exact-support and exact-Kural-S evaluated).
- **Failure-path fabricated fixtures**: `NONFINITE_INPUT`, `INVALID_INITIALIZATION`, `NONFINITE_PARAMETER`, `NONFINITE_FIT`, `OPTIMIZER_NONCONVERGENCE`, `OTHER_PREDECLARED_NUMERICAL_FAILURE`, `FAMILY_FIT_FAILURE`/`NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART` — all reached.
- **`FIX-FALLBACK-FAULT-INJECTION`**: primary raised the tagged exception; real SLSQP fallback ran on the identical `x0` and converged (`Optimization terminated successfully`).
- **Multistart aggregation fabricated cases**: unique-minimum, tie (lexicographically smallest), lower-L-but-ineligible-excluded — all correct.
- **`FIX-D0F209-MANIFEST-QC`**: P-01 731/731, P-02 261/261, exact set equality with the existing CSV, ascending order, exact dedup — all PASS.
- **Reserved-code negative assertion**: `reserved_violation = false` — `BOUNDARY_PATHOLOGY`, `IDENTIFIABILITY_FAILURE`, `WARN_BOUNDARY`, `WARN_IDENTIFIABILITY` never emitted.

No parameter-recovery, objective-attainment, or family-comparison claim is made anywhere in this section.

## 14. R2-01..R2-36 table

| check | result |
|---|---|
| R2-01 repository/root/branch/HEAD precheck | PASS |
| R2-02 all governing hashes exact | PASS |
| R2-03 historical STEP-2 artifacts preserved byte-unchanged | PASS |
| R2-04 fixture manifest pre-hash exact | PASS |
| R2-05 fixture manifest declared↔implemented ID + metadata/execution-mode fidelity | PASS |
| R2-06 D-F2-09 reconstruction exact: 731 / 261 | PASS |
| R2-07 feature-start +1/+0 semantics preserved | PASS — both benign fixtures produced valid, nonduplicate feature starts (+1); rejection branch exists but not naturally triggered this rerun (same as historical run) |
| R2-08 P-01 optimizer/constraint construction preserved | PASS — `Bounds` + `LinearConstraint(c_d-c_r>=0)`, unchanged |
| R2-09 P-02 beta-dependent NonlinearConstraint construction preserved | PASS — two `NonlinearConstraint` objects, unchanged |
| R2-10 numerical V_P01/V_P02 feasibility semantics preserved | PASS (except the required C4 beta-clamp removal in V_P02) |
| R2-11 exact scientific-domain predicate implemented independently | PASS — `scientific_domain_pass_p01`/`_p02`, zero tolerance |
| R2-12 X1-P01-ORDER adversarial self-test | PASS (§6) |
| R2-13 X1-P02-SMIN adversarial self-test | PASS (§7) |
| R2-14 exact Kural T has no numerical waiver | PASS — `-1e-9`/`-1e-12` removed |
| R2-15 exact Kural S preserved | PASS — `n_sup>=3`, unchanged formula |
| R2-16 ZERO_VARIANCE_FIT behavior preserved | PASS — `epsilon_model=1e-12` unchanged |
| R2-17 primary optimizer mini-bank full rerun P-01 | PASS |
| R2-18 primary optimizer mini-bank full rerun P-02 | PASS |
| R2-19 fallback fault-injection full rerun | PASS |
| R2-20 all STEP-2-emittable failure paths rerun | PASS — 8/8 codes reached |
| R2-21 reserved boundary/identifiability labels remain non-emittable | PASS |
| R2-22 multistart aggregation behavior preserved | PASS |
| R2-23 family status/summary separated from hard-predicate schema | PASS (§9) |
| R2-24 exact D-F2-09.9 tie behavior preserved | PASS |
| R2-25 exact semantic RUN1/RUN2 determinism | PASS (§15) |
| R2-26 executed fixture IDs exactly equal declared manifest IDs; no undeclared/unexecuted IDs | PASS |
| R2-27 fixture manifest post-hash equals pre-hash | PASS |
| R2-28 telemetry firewall preserved | PASS |
| R2-29 no frozen scientific/class-C literal tuned from outcomes | PASS — only two Python identity-vs-equality bugs fixed, zero scientific content touched |
| R2-30 real-SSA / adequacy / recovery / P03/P04/P05 / F3 firewall preserved | PASS |
| R2-31 X4 historical `1.0e6` absent; exact `585.0` CLASS_C objective-domain guard active | PASS (§10) |
| R2-32 benign P-01/P-02 PASS criterion explicitly satisfied | PASS (§11 C1) |
| R2-33 X1-P02-SMIN uses beta=sqrt(6) exactly | PASS (§7) |
| R2-34 C3 multiple-predicate display-precedence self-test PASS | PASS (§16) |
| R2-35 V_P02 uses returned beta without clipping/projection | PASS (§11 C4) |
| R2-36 successor telemetry contains RUN1 calls only | PASS (§11 C5) |

All 36 checks PASS. No check failure occurred; no STOP was required.

## 15. Double-run determinism hashes

```text
DETERMINISM_CHECK = PASS
RUN1 canonical SHA256 = 80830b4473b43731a2bf7d54b9b742a4415b573a53ac374b5ea325bdd00cb2cf
RUN2 canonical SHA256 = 80830b4473b43731a2bf7d54b9b742a4415b573a53ac374b5ea325bdd00cb2cf
```

Canonical serialization includes, per start: `fixture_id, family, start_id, optimizer_path, status_class, predicates, rejection_reasons, scientific_domain_pass, kural_t_pass_exact, kural_s_pass_exact, eligible, terminal_endpoint_hex (exact IEEE-754 hex), family_status, family_summary` — plus the three harness self-test records serialized alongside (same canonical document). Both in-process runs, same thread-pinned environment, no code/input/manifest/configuration change between runs. No invented closeness tolerance; exact string equality achieved. Runtime excluded from the comparison.

## 16. Telemetry firewall + `telemetry_run=RUN1`

```text
telemetry_run = RUN1
```

Successor telemetry file `f2_step2_feasibility_telemetry_r2_2026-09-01.csv` — 10 rows, columns exactly `fixture_id,family,start_id,optimizer_path,status,message,success,nit,nfev,njev,wall_clock_seconds`. No `L`/objective/`rho`/`theta_true`/parameter-error/recovery column; no family-level aggregate; no cross-family runtime summary; no faster/slower conclusion.

**C3 display-precedence self-test:**

```text
input predicates = {NONFINITE_FIT, MORPHOLOGY_INADMISSIBLE}
all predicates remain present = true
primary_display_code = NONFINITE_FIT   (matches DISPLAY_PRECEDENCE: NONFINITE_FIT ranks above MORPHOLOGY_INADMISSIBLE)
display precedence changes eligibility/admissibility = false (by construction; precedence is display-only)
SELFTEST RESULT = PASS
```

## 17. Firewall/gate state

```text
real_SSA_fit = false | real_SSA_subset_fit = false | real_SSA_trajectory_access_for_fitting = false
parameter_recovery_analysis = false | objective_attainment_analysis = false
generator_adequacy_comparison = false | generator_selection = false
cross_family_runtime_ranking = false | family_winner_language = false
P03_touched = false | P04_touched = false | P05_touched = false
algorithm_CVI_execution = false | algorithm_CVI_outcome_access = false
legacy_performance_content_access = false | results_directory_opened = false
F3_started = false | F4_started = false | rng_used = false | commit = false

ART_F2_r2a_unchanged = true
original_STEP2_harness_unchanged = true
original_STEP2_telemetry_unchanged = true
original_STEP2_report_unchanged = true
STEP2_fixture_manifest_unchanged = true

X1_closed = true | X2_closed = true | X3_closed = true | X4_closed = true | C1_C5_closed = true

F2_STEP_2_corrected_rerun = PASS

PI_re_ratification = false
F2_complete = false
F3_allowed = false

next_action = independent audit of corrected STEP-2 successor artifacts
```

STEP 3 was not started.

## 18. Exact successor file hashes

```text
f2_step2_feasibility_harness_r2_2026-09-01.py    = 3b2555508e4b731ab3349a040a03a3d266fe068d72cd13427107a998622610bc
f2_step2_feasibility_telemetry_r2_2026-09-01.csv = d688a16bfd131ee1e1cfe8715a011009b782a78a1ac897c5589cc68af3b8dabb
```

(This report's own hash is reported in the end-of-task response, computed after this file is written.)

## 19. Final `git status --short --untracked-files=all`

Recorded in the end-of-task response after this report is written (three new untracked successor artifacts added to the existing F2-era set).

## 20. Verdict

```text
ART_F2_STEP2_R2_FEASIBILITY_READY_FOR_INDEPENDENT_AUDIT
```
