# p_konum_plus — F3 STEP-2 — CLASS_C Pin Register r1 (2026-09-06)

```text
artifact_role = CLASS_C implementation-pin register for the F3 adequacy-evaluation
                harness (deliverable 6 of the STEP-2 v5 task)
status        = NON-NORMATIVE
frozen_contract = r4 5e594136… AS RATIFIED BY freeze record r1 7055f186… ; v11 wins
harness       = f3_step2_adequacy_harness_r1_2026-09-06.py (external sidecar hash)
scientific_freedom in every row = none ; scientific literal additions = 0
```

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result | scientific_freedom |
|---|---|---|---|---|---|
| PIN-F2-LOADER | v5 §3.1/§3.3 (engine reuse; file is `__main__`-guarded) | `importlib.util.spec_from_file_location` on the frozen F2 r3 file; SHA256 verified BEFORE load (`load_f2`) | T-LOADER-F2 (hash assert + `run_all_fixtures` present) | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-F2-IMPORT-HASH | custody item 3 | `sha256_of(F2_PATH) == 01714752…` asserted before import | T-LOADER-F2 | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-SPLINE-LOADER | v5 §3.3 definition-only AST loader | `ast.parse` of the frozen r2 harness; node classes retained per §3.3 (Import/FunctionDef/ClassDef/constant Assign) PLUS the definitional-support prelude (all top-level nodes lexically before the `# ---------------- steps 1-3` orchestration marker; each verified to contain no `open(`/`print(`); every executed node's `ast.get_source_segment` is byte-identical to the frozen source; retained/prelude/excluded node lists recorded in the results JSON; correctness proof = the mandated spline non-regression (v5 §3.3 rule 5). Rationale: the retained-only namespace lacks definitional constants created by call/loop nodes (B, D1, coefficient vectors, option dicts, masks) that are NOT run-orchestration state (§3.3 rule 6 does not apply); the prelude supplies exactly those, unmodified | T-SPLINE-NR (non-regression) | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-SPLINE-IMPORT-HASH | custody item 8 | `sha256_of(SPL_PATH) == b31e5a6b…` asserted before parse | T-LOADER-SPL | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-THREADS | v5 §8 (F2 environment) | `OMP/OPENBLAS/MKL_NUM_THREADS = "1"` set before numpy import | environment block in results | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-MASKED-OBJECTIVE | r4 §8 masked objective; v5 §3.2 | wrapper-scoped rebinding of `f2.make_objective_and_x` for non-FULL masks only; the masked `fun` reuses the frozen `p01_stable`/`p02_stable` + `zero_variance_rule` + `L_INVALID_PREDICTION_GUARD` path and sums `(x[O]−ghat[O])²` directly (no correlation shortcut); mask = FULL ⇒ NO patch, frozen path verbatim | T-MASK-FULL (full-mask patched fun == frozen fun, `float.hex` bitwise) + NR-01 + per-fit assert `L_O <= L_FULL` | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-MASKS | v5 §2 literals | LEFT observed = `np.arange(15,146)`; RIGHT observed = `np.arange(0,131)`; E = 15 edges `[0,15)` / `[131,146)` | structural constants; exercised in probe fits | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-FOLDS | v5 §2 fold boundaries | `FOLD_BOUNDS = [0,29,58,87,116,146]`; training mask = `np.setdiff1d(FULL, held)`; every year predicted exactly once by the held-out fold's training fit | fold loop; C2 assembly | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-FEATURE-START-MASKED | r4 §8 / D-F2-09.5 | frozen `f2.feature_start` applied to the observed-only view (`-inf` padding outside O) ⇒ frozen min-index argmax over O and frozen constants unchanged; invalid ⇒ FEATURE_START_REJECTED, no clipping, frozen grid starts remain | T-FS-MASK (padded result == direct `min{j in O : x_j = max}` formula) | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-SPLINE-MASKED-RSS | r4 §5/§8; v5 §3.3 | `rss_of(c, x, O)` from the loaded r2 namespace (frozen function; already mask-parameterized); grid-unimodality via `amat(mode)` on the FULL grid for every fit; metric-facing prediction `z_ddof0(B c, full grid)`; 146-mode enumeration; mode equivalence `|ΔRSS| <= 1e-12 + 1e-9·max`, winner = min mode; no valid mode / zero-variance / non-finite ⇒ spline_fit_status = FAILURE | T-SPLINE-NR + fixture paths | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-ACF | D-C3-ACF-ESTIMATOR (ratified classical lag-1 ACF); v5 §4/§10 | `acf_classical(r)`: explicit sequential float64 loops in index order — `r_bar = (Σ_seq r[t])/float(T)`; `num = Σ_seq (r[t]−r_bar)(r[t+1]−r_bar)`, t=0..T−2; `den = Σ_seq (r[t]−r_bar)²`, t=0..T−1; `phi = abs(num/den)`; NO np.mean / np.sum / np.dot / BLAS / pairwise reduction / corrcoef / pearsonr / T/(T−1) variant; `den == 0.0` exact or non-finite ⇒ undefined (`None`), CL-F3-04 governance | T-ACF: bitwise (`float.hex`) equality with the independently written `acf_classical_b` (while-loop accumulation) on (a) every RUN1 full-data residual/z series and (b) closed-form vectors: alternating `(−1)^t`, linear `t`, constant (den = 0 ⇒ undefined), mixed trig; strict inequality vs `abs(np.corrcoef(r[:-1],r[1:])[0,1])` (alt (c)) and vs `phi·146/145` (alt (b)); informational `fractions.Fraction` exact-rational ulp deviation (`math.ulp`); no tolerance, no RNG | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-RHOCV | r4 §3-C2 | `numpy.corrcoef(z_i, ghat_cv_i)[0,1]` on the two 146-vectors | C2 computation; exercised on SCEN-A | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-RMSE-EDGE | r4 §3-C4b | `sqrt( Σ (probe_pred[edge]−ref_pred[edge])² / float(E) )`, both predictions full-grid z_ddof0 curves; reference = the fitter's own full-data fit | computed on real probes (validity PENDING per EXACT-01) + INJ values | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-SSTAB-W | r4 §3-C5 + frozen W widths (v5 §2) | `np.quantile(thetas, [0.25,0.75], axis=0, method="linear")`; `s_stab = max_j (IQR_j / W_j)` with W = P-01 (3, 3, 123.43902548550072, 123.43902548550072); P-02 (3, 2.9843062202305717, 2.9843062202305717, 5) | C5 computation on SCEN-A folds | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-MEDIAN | r4 §3 common fields | `numpy.median` (float64) for every sex-level aggregation | all criteria | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-IQR | r4 §3-C5 | `numpy.quantile(x, [0.25, 0.75], method="linear")` | C5 | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-TAU-COMPARE | record r1 §2 tau literals; r4 §9 | `abs(delta) <= tau_j` in float64; direction per criterion; better family per frozen direction | D-P04 fixtures (resolve at each level) | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-WORSE-SEX | v5 §5 | C1 min, C2 min, C3 max, C4a min, C4b max, C5 max over sexes; C6 = k_F | D-P04 fixtures | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-U-SETS | record r1 §3 item 4.1; v5 §5 | U2 = P01cc ∧ P02cc ∧ SPLcc ; U3 = phi-defined∧fits for all three ; U4 = both probes ×3 fitters ; U5 = P01cc ∧ P02cc ; C1/C4a/C6 not recomputed (CL-F3-01); recompute counters logged | INJ-DP04-C2-DIVERGE (same-set rule decides), INJ-DP04-C1 (counters = 0 for unconsulted) | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-CONSULTED-PATH | r4 §9.1 via record r1 | level consulted only if all earlier EQUIVALENT; terminate on RESOLVED; consulted path + per-level disclosure recorded | D-P04 fixtures | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-TERMINAL-FALLBACK | r4 §9 / record r1 | all levels EQUIVALENT ⇒ mechanism `TERMINAL_FALLBACK_MECHANISM_P01` ("P-01" < "P-02") | INJ-DP04-TERMINAL | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-UNDEFINED-FLAGS | r4 §3 (§8.1; CL-F3-04) | undefined statistic = `None` + explicit validity handling; NaN never treated as valid; undefined REQUIRED sex-level statistic ⇒ criterion not passed; undefined consulted scalar ⇒ STOP_UNDEFINED_CONSULTED_SCALAR | INJ-C3-PHI-UNDEF; T-ACF constant vector | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-K05-INVARIANT | record r1 §4 (K-05) | assert: C4b completeness share >= c_complete ⇒ ident >= c_ident (evaluator derives both from the same probe flags) | every fixture with C4 data (INJ) | PASS (RUN1/RUN2 2026-09-06; report §5) | none |
| PIN-A5-SUPPORT | r4 §3-C4a A.5(i) | **ABSENT** — no exact frozen data-level Kural-S support definition exists (ADDENDUM A r1 NOT_LOCATED in repo and, per its dispatched text, contains no operational definition; frozen F2 `n_sup`/`kural_s_pass_exact` are defined on stabilized FITTED curves only). F3-STEP2-EXACT-01 recorded; A.5 applied whole-or-not-at-all: real-fixture C4a determination returns `STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-01)`; A.5 (ii)/(iii) code written and unit-tested only (UT-A5-II / UT-A5-III), no C4 fixture outcome | — | EXACT-01 | none (gap returned to PI, not resolved) |

## TEST_CONSTANT rows (engineering; test code only — never enter any result, statistic, gate, comparator or the scientific literal registry)

| constant | where | role |
|---|---|---|
| closed-form ACF test vectors: alternating `(−1)^t`, linear `t`, constant `1.0`, mixed `sin(0.37t)+0.25·cos(1.7t)` | T-ACF | TEST_CONSTANT |
| T-MASK-FULL test theta `(0.3, 0.7, 20.0, 20.0)` and test mask `np.arange(20,120)` | T-MASK-FULL / T-FS-MASK | TEST_CONSTANT |
| UT-A5 synthetic spike vector (`x[70]=3.0`, z-scored) | UT-A5-II / UT-A5-III | TEST_CONSTANT |
| fixture construction constants (bump centers/widths, noise sigma 0.10, seeds 20260906–20260911; INJ statistic values in the generator) | fixture generator | TEST_CONSTANT (declared in the fixture manifest; PATH_COVERAGE_ONLY) |

Scientific literal registry additions = 0. Every pin's `result` column is bound to
the qualification report (deliverable 7) and the results JSON of the RUN1/RUN2
execution; `see report` resolves there.
