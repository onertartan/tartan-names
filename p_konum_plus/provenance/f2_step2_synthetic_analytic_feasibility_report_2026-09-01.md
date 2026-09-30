# p_konum_plus — F2 STEP 2 Synthetic/Analytic-Only Feasibility — Report

- **Artifact role:** F2 STEP 2 execution report (executability + determinism + failure-path QC only, on predeclared synthetic/analytic fixtures). NOT a methodology review, NOT a generator adequacy study, NOT a parameter-recovery experiment, NOT a family comparison.
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-09-01
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`

---

## 1. Repository + hash precheck

Root ✓, branch `p_konum_plus` ✓, HEAD = expected `3e4daf47018f124e29717263e4e45fe90c8e52b8` ✓. Zero unexpected tracked modifications; only the fourteen known F2-era untracked artifacts present at precheck. All four STEP-2 target output paths were verified absent before creation.

Governing hashes (recomputed, all exact):

| document | SHA256 |
|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` |
| ART-F2 r2a (executable spec) | `2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2` |
| ART-F2 r2 (parent) | `d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4` |
| ART-F2 r1 | `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7` |
| PI ratification-ready worksheet FINAL_v2 | `803e9f30fa84b6c02c34a517525e6c246edf7be4db684e72a2ea8c970f9b38f5` |
| D-F2-09 exact packet | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` |
| D-F2-09 start-grid manifest | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` |
| ART-F0 | `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` |
| ART-F1 r4a | `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0` |
| F1 eligible manifest | `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` |
| F1 input hash table | `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac` |
| STEP-1.5 provenance report | `bf6fb60c2c520356ecd3321fa25a0ee15a3572522044bf8e6723196a0f2e1296` (nonnormative; recorded, not treated as authoritative over r2a/v11) |

No mismatch; no STOP.

## 2. Fixture-manifest path + pre-run/post-run SHA256

```text
path      = p_konum_plus/calibration/f2_step2_fixture_manifest_2026-09-01.csv
pre-run   = daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b
post-run  = daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b   (IDENTICAL)
```

21 predeclared fixtures across five classes (analytic benign generator ×2, stable-evaluation analytic ×5, failure-path fabricated ×8, fallback fault-injection ×1, multistart-aggregation fabricated ×3, plus manifest-reconstruction ×1 and reserved-code negative assertion ×1). The manifest was written and hashed before any fixture executed; the harness only reads it.

## 3. Environment / reproducibility

```text
python  = 3.11.7
numpy   = 1.26.4
scipy   = 1.14.1
platform = Windows-10-10.0.19045-SP0
OMP_NUM_THREADS = 1
OPENBLAS_NUM_THREADS = 1
MKL_NUM_THREADS = 1
```

Thread-pin environment variables are set at the top of the harness, before `numpy`/`scipy` are imported, and are not changed between RUN 1 and RUN 2. No BLAS/LAPACK backend identifier beyond the platform string above was available via the standard API; this is recorded as a known limitation, not fabricated.

## 4. Exact optimizer constraint-construction audit (§11A of the governing prompt)

Verified against the incorporated ART-F2 r2 scientific support (unchanged):

```text
P-01: Bounds([-1,-1,k_min,k_min],[2,2,k_max,k_max]) + LinearConstraint([[-1,1,0,0]], lb=0, ub=inf)
      exactly encodes c_r,c_d in [-1,2]; k_r,k_d in [k_min,k_max]; c_d - c_r >= 0

P-02: coarse Bounds([-1, s_side_min(1), s_side_min(1), 1], [2, 3, 3, 6])
      + NonlinearConstraint(s_l - s_side_min(beta) >= 0)
      + NonlinearConstraint(s_r - s_side_min(beta) >= 0)
      exactly encodes m in [-1,2]; beta in [1,6]; s_l,s_r <= 3; s_l,s_r >= s_side_min(beta)
      (beta-dependent lower bound represented by exact NonlinearConstraint objects,
       NOT flattened to a static lower bound, NOT using 0 as the optimizer's
       scale lower bound — s_side_min(1) is used only as the coarse box floor,
       exactly as specified)
```

Neither construction loosens, tightens, or replaces the ratified scientific support. No STOP triggered.

## 5. Exact files created

- `p_konum_plus/calibration/f2_step2_fixture_manifest_2026-09-01.csv`
- `p_konum_plus/calibration/f2_step2_feasibility_harness_2026-09-01.py`
- `p_konum_plus/calibration/f2_step2_feasibility_telemetry_2026-09-01.csv`
- `p_konum_plus/provenance/f2_step2_synthetic_analytic_feasibility_report_2026-09-01.md` (this file)

No other project file was modified.

## 6. Confirmation no upstream file changed

Re-hashed after execution: ART-F2 r2a `2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2` — unchanged. D-F2-09 start-grid manifest `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` — unchanged (read-only reference in the harness). ART-F2 r2, r1, ART-F0, ART-F1 r4a, and both F1 manifests were not touched at all.

## 7. Harness bug found and fixed (transparency note — not a scientific change)

The first execution pass produced `has_eligible_endpoint = false` for both benign fixtures despite individual endpoints showing `kural_t_pass: True`, `kural_s_pass: True`, `predicates: []`. Root cause: `kural_t_pass_p01`/`kural_t_pass_p02` return `numpy.bool_` (because `theta` is unpacked from a NumPy array), and the eligibility check used Python's `is True` — an **identity** comparison that is always `False` for `numpy.bool_(True)` (it is not the same object as the `True` singleton), even though the value is equal to `True`. This silently forced every otherwise-admissible endpoint ineligible.

**Fix:** changed `(kural_t is True) and (kural_s is True)` to `bool(kural_t) and bool(kural_s)` in `classify_endpoint`. This is a pure Python-identity-vs-equality bug fix in the test harness's own bookkeeping. No Kural T/S formula, bound, threshold, or admissibility semantics were altered; the underlying `kural_t_pass_p01/p02` and `kural_s_pass` computations were correct both before and after the fix — only the final boolean gate was wrong. The harness was re-executed in full (both runs) after the fix; all results below are post-fix. This satisfies S2-19 (no frozen literal tuned from fixture outcomes) — nothing frozen was touched, only an internal comparison bug.

## 8. S2-01..S2-24 checklist

| check | result |
|---|---|
| S2-01 repository/hash precheck | PASS |
| S2-02 fixture manifest predeclared before execution and byte-unchanged after | PASS |
| S2-03 no real SSA / results / legacy-performance access | PASS — `results/` never opened; the 906 ART-F1 trajectories never read; only the (already hash-verified, synthetic construction) D-F2-09 start-grid CSV was read |
| S2-04 D-F2-09 fixed-grid reconstruction and manifest equality | PASS — P-01 731/731, P-02 261/261, exact set equality with the existing CSV, ascending order and exact dedup confirmed |
| S2-05 feature-start validity/dedup path execution | PASS — both benign fixtures produced a valid, nonduplicate feature start; the OK branch was exercised. Note: the `FEATURE_START_REJECTED` branch exists in the implementation but was not naturally triggered by any predeclared fixture in this pass (neither benign fixture happened to produce an invalid/duplicate feature start) |
| S2-06 stable P-01 evaluation | PASS — interior and boundary tuples evaluate without exception; `FIX-P01-ZEROVAR-IN-DOMAIN` correctly reaches `ZERO_VARIANCE_FIT` (σ_g = 0.0 exactly); `FIX-P01-KURAL-S-FAIL` correctly reaches `MORPHOLOGY_INADMISSIBLE` |
| S2-07 stable P-02 evaluation | PASS — interior and `s=s_side_min(beta)` boundary tuples evaluate without exception |
| S2-08 P-01 primary optimizer mini-bank executability | PASS — all 4 selected starts (grid[0], grid[365], grid[730], feature) returned structured results with no unhandled exception; 3 of 4 eligible (grid[730] legitimately `MORPHOLOGY_INADMISSIBLE`, a real Kural-S failure at that converged endpoint, not a harness fault); ≥1 eligible endpoint exists |
| S2-09 P-02 primary optimizer mini-bank executability | PASS — all 4 selected starts (grid[0], grid[130], grid[260], feature) returned structured results, no unhandled exception; all 4 eligible |
| S2-10 post-return constraint-feasibility evaluation | PASS — `V_P01`/`V_P02` computed for every returned endpoint; `feasibility_acceptance_tol=1e-8` applied; all P-01/P-02 benign endpoints numerically feasible (`v_value=0.0`) |
| S2-11 epsilon_model / zero-variance branch | PASS — exercised on a real generator-native in-domain tuple (`FIX-P01-ZEROVAR-IN-DOMAIN`) and on fabricated vectors (nonfinite → `NONFINITE_FIT`) |
| S2-12 fallback fault-injection path | PASS — primary raised the tagged `FAULT_INJECTION_TEST_ONLY` exception; real frozen SLSQP fallback then ran on the **identical** `x0` and converged (`Optimization terminated successfully`); no new start, no perturbation, no RNG |
| S2-13 failure-code reachability for all STEP-2-emittable codes | PASS — emitted-predicate union this run: `INVALID_INITIALIZATION`, `MORPHOLOGY_INADMISSIBLE`, `NONFINITE_FIT`, `NONFINITE_INPUT`, `NONFINITE_PARAMETER`, `OPTIMIZER_NONCONVERGENCE` (fabricated), `OTHER_PREDECLARED_NUMERICAL_FAILURE`, `ZERO_VARIANCE_FIT` — all 8 STEP-2-emittable codes reached |
| S2-14 reserved boundary/identifiability codes not emitted | PASS — `BOUNDARY_PATHOLOGY`, `IDENTIFIABILITY_FAILURE` absent from the emitted-predicate union; no `WARN_BOUNDARY`/`WARN_IDENTIFIABILITY` emitted anywhere (`reserved_violation = false`) |
| S2-15 multistart aggregation orchestration | PASS — real benign mini-bank outputs aggregated correctly (`agg_status=OK` both families); fabricated cases: unique-min selected correctly, all-ineligible → `FAMILY_FIT_FAILURE`/`NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART` |
| S2-16 D-F2-09.9 tie comparator | PASS — fabricated tie case resolved to the lexicographically smallest canonical tuple exactly as specified |
| S2-17 exact semantic double-run determinism | PASS — canonical per-start JSON serialization (float64 exact-hex endpoint tuples) byte-identical across both in-process runs; `DETERMINISM_PASS=True`; `SHA256(RUN1)=SHA256(RUN2)=8eb54b282b46605de6e8629df365915f4f0c0452143529f82c22de492b458682` |
| S2-18 runtime telemetry captured without comparative inference | PASS — raw `nit`/`nfev`/`njev`/wall-clock/status per call recorded; no cross-family table or ranking computed |
| S2-19 no frozen literal tuned from fixture outcomes | PASS — only a boolean identity-vs-equality bug (§7) was fixed; no bound/threshold/formula/tolerance changed |
| S2-20 firewall/gate status preserved | PASS — see §14 below |
| S2-21 P-02 beta-dependent scale lower bound via exact NonlinearConstraint + correct coarse Bounds | PASS — verified in §4 |
| S2-22 numerical-infeasibility rejection + exact Kural-T/S semantics logged without clipping/tolerance waiver | PASS — `POST_RETURN_CONSTRAINT_REJECTION` and `MORPHOLOGY_INADMISSIBLE` are logged as distinct, separately-computed predicates; no clipping/projection anywhere in the harness |
| S2-23 thread/environment pins active for exact double-run determinism | PASS — confirmed via `ENV_INFO` output (§3) |
| S2-24 telemetry firewall: no objective L column, no family-level runtime aggregation | PASS — telemetry CSV columns are exactly `fixture_id,family,start_id,optimizer_path,status,message,success,nit,nfev,njev,wall_clock_seconds`; no `L`/objective column; no aggregated statistics computed or stored |

All 24 checks PASS. No check failure occurred; no STOP was required.

## 9. P-01 code-path results — no adequacy interpretation

`FIX-P01-BENIGN`: 4 selected starts (3 fixed-grid at lexicographic indices {0,365,730} of 731 + 1 feature start) all executed via the frozen primary `trust-constr` contract without an unhandled exception; every start returned a structured, classified record. 3 of 4 endpoints were eligible; 1 (`grid[730]`, the far out-of-window / max-steepness corner) converged to a `MORPHOLOGY_INADMISSIBLE` endpoint under the exact, unmodified Kural-S rule — a legitimate admissibility outcome, not an error. Aggregation selected a family fit among the eligible endpoints (`agg_status=OK`). `FIX-P01-ZEROVAR-IN-DOMAIN` and `FIX-P01-KURAL-S-FAIL` both reached their designated code paths on direct generator evaluation. This section makes no claim about fit quality, convergence speed, or morphology adequacy.

## 10. P-02 code-path results — no adequacy interpretation

`FIX-P02-BENIGN`: 4 selected starts (3 fixed-grid at lexicographic indices {0,130,260} of 261 + 1 feature start) all executed via the frozen primary `trust-constr` contract (with the beta-dependent `NonlinearConstraint` pair) without an unhandled exception; all 4 endpoints were eligible; aggregation selected a family fit (`agg_status=OK`). `FIX-P02-STABLE-INTERIOR` and `FIX-P02-STABLE-BOUNDARY-SMIN` both evaluated without exception. No claim is made about fit quality, convergence speed, or morphology adequacy.

## 11. Failure/fallback orchestration results

All 8 STEP-2-emittable failure codes were reached (S2-13); the two reserved codes and both reserved WARN labels were never emitted (S2-14). The fallback fault-injection fixture confirmed the exact plumbing required by r2a: a `FAULT_INJECTION_TEST_ONLY`-tagged exception on the primary path for the designated start triggers the real, unmodified SLSQP fallback on the **identical** `x0`, with no new start and no RNG; the fallback converged. All three multistart-aggregation fabricated cases (unique minimum, tie, lower-L-but-ineligible-excluded) and the all-ineligible → `FAMILY_FIT_FAILURE` case resolved exactly as specified.

## 12. Double-run determinism result

```text
DETERMINISM_CHECK = PASS
RUN1 canonical SHA256 = 8eb54b282b46605de6e8629df365915f4f0c0452143529f82c22de492b458682
RUN2 canonical SHA256 = 8eb54b282b46605de6e8629df365915f4f0c0452143529f82c22de492b458682
```

Both runs executed in the same process, same thread-pinned environment, without modifying code, inputs, fixture manifest, or configuration between runs. Canonical per-start records (fixture_id, family, start_id, optimizer_path, status class, hard-failure predicate set, CLASS_C rejection-reason set, eligibility boolean, exact IEEE-754 hex endpoint tuple) were byte-identical; no invented tolerance was used to call the runs "close" — exact string equality was required and achieved. Runtime measurements (wall-clock) were excluded from the determinism comparison as specified.

## 13. Runtime telemetry description

10 rows written to `f2_step2_feasibility_telemetry_2026-09-01.csv`, covering the 8 real optimizer calls from the two benign fixtures (4 P-01 + 4 P-02, primary path only, all converged) plus the 2 calls from the fallback fault-injection fixture (1 primary-path exception row + 1 fallback-path success row). Columns: `fixture_id, family, start_id, optimizer_path, status, message, success, nit, nfev, njev, wall_clock_seconds`. This is raw per-call computational-feasibility evidence only; no objective value, no family-level aggregation, no cross-family comparison, and no faster/slower conclusion is present or implied.

## 14. Firewall confirmation

```text
real_SSA_fit = false
real_SSA_subset_fit = false
real_SSA_trajectory_access_for_fitting = false
generator_adequacy_comparison = false
generator_selection = false
parameter_recovery_score = false
parameter_recovery_rate = false
parameter_recovery_pass_fail_threshold = false
objective_attainment_threshold = false
L_le_Ltol_rule = false
objective_success_rate = false
comparative_reconstruction_error = false
cross_family_runtime_ranking = false
family_winner_language = false
P03_derivation_or_tuning = false
P04_touched = false
P05_touched = false
algorithm_CVI_execution = false
algorithm_CVI_outcome_access = false
legacy_performance_content_access = false
F3_started = false | F4_started = false
results_directory_opened = false
rng_used = false
commit = false
```

## 15. Final gate state

```text
F2_STEP_1_complete   = true
F2_STEP_1_5_complete = true
F2_STEP_2            = true
F2_STEP2_feasibility = PASS

F2_complete = false
F3_allowed  = false

generator_selected = false
P03_touched = false | P04_touched = false | P05_touched = false

next_action = independent audit of STEP-2 artifacts before F2 STEP 3 freeze
```

STEP-2 success does not itself freeze F2. STEP 3 was not started.

## 16. Final `git status --short --untracked-files=all`

Recorded in the end-of-task response after this report is written (four new untracked STEP-2 artifacts added to the existing F2-era set).

## 17. Verdict

```text
ART_F2_STEP2_FEASIBILITY_READY_FOR_INDEPENDENT_AUDIT
```
