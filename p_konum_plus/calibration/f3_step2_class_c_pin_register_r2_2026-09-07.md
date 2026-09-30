# p_konum_plus — F3 STEP-2 — CLASS_C Pin Register r2 (2026-09-07)

```text
artifact_role = CLASS_C implementation-pin register for the F3 adequacy-evaluation
                harness (deliverable 9 of the STEP-2 r2 correction cycle)
status        = NON-NORMATIVE
parent        = f3_step2_class_c_pin_register_r1_2026-09-06.md 03486232ac62206b1eed52c2355e465364ec10fc02fb13d62dd32e2dfd50f9ca
frozen_contract = r4 5e594136… AS RATIFIED BY freeze record r1 7055f186… ; v11 wins
harness       = f3_step2_adequacy_harness_r2_2026-09-07.py (external sidecar hash)
PI-ratified content = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
                da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
S/T as read   = S-1=(a) ; S-2=alpha ; T-1=AUTHORIZE ; T-2=T-2a ; T-3=AUTHORIZE ;
                T-4=T-4a ; T-5=CONFIRM_WITHIN_SCOPE
scientific_freedom in every row = none ; new scientific literal additions by executor = 0
Every row below is re-verified and re-stated against the r2 run (RUN1 == RUN2
canonical SHA256 31686de030a5493fd2493e0b459f0b7057fbbc678c4b43bd19cd450ade3bac2d,
2026-09-07); result = executor claim, independent verification pending (§15).
```

## Retained from r1 (re-verified against the r2 run)

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result | scientific_freedom |
|---|---|---|---|---|---|
| PIN-F2-LOADER | v5 §3.1/§3.3 (engine reuse; file is `__main__`-guarded) | `importlib.util.spec_from_file_location` on the frozen F2 r3 file; SHA256 verified BEFORE load (`load_f2`) | NR-01(i) (hash assert + `run_all_fixtures` present) | PASS (RUN1/RUN2 2026-09-07; report r2 §5) | none |
| PIN-F2-IMPORT-HASH | custody item 3 | `sha256_of(F2_PATH) == 01714752…` asserted before import | NR-01(i) | PASS | none |
| PIN-SPLINE-LOADER | T-1=AUTHORIZE; X-01 | node-list authorization now EXACT (not permissive): base retain classes (Import/ImportFrom/FunctionDef/ClassDef/constant Assign, any position) PLUS exactly the 21 named prelude nodes before the orchestration marker, asserted equal (set AND order) to `AUTHORIZED_PRELUDE`; I/O-freedom checked by AST walk of `Call.func` names/attrs (`open`,`print`,`exit`,`write`,`writerow`,`writerows`,`sys.exit`), not substring; per-node SHA256 recorded; SOLVER-B function set (`run_tc,polish,accept,kkt_res,maxviol,gradf,rss_of,run_slsqp,solver_config,amat`) hashed individually | T-LOADER-NODES | PASS: 21/21 prelude nodes match authorized list exactly (order); I/O-free assertion PASS; spline NR PASS | none |
| PIN-SPLINE-IMPORT-HASH | custody item 8 | `sha256_of(SPL_PATH) == b31e5a6b…` asserted before parse | T-LOADER-NODES | PASS | none |
| PIN-THREADS | v5 §8 | `OMP/OPENBLAS/MKL_NUM_THREADS = "1"` set before numpy import | environment block in results | PASS | none |
| PIN-MASKED-OBJECTIVE | r4 §8; T-5=CONFIRM_WITHIN_SCOPE (status quo retained, X-19) | wrapper-scoped rebinding of `f2.make_objective_and_x` for non-FULL masks only; masked `fun` reuses frozen `p01_stable`/`p02_stable` + `zero_variance_rule` + `L_INVALID_PREDICTION_GUARD`; FULL mask ⇒ no rebinding, frozen path verbatim | full-mask bitwise equality (`float.hex`) + per-fit `L_O <= L_FULL` assert | PASS (bitwise match; assert never triggered) | none |
| PIN-MASKS | v5 §2 literals | LEFT observed = `np.arange(15,146)`; RIGHT observed = `np.arange(0,131)`; E=15 | probe fits, every real fixture | PASS | none |
| PIN-FOLDS | v5 §2 fold boundaries | `FOLD_BOUNDS=[0,29,58,87,116,146]`; training = `setdiff1d(FULL, held)` | SCEN-A/SCEN-B fold loops | PASS | none |
| PIN-FEATURE-START-MASKED | r4 §8 / D-F2-09.5 | frozen `f2.feature_start` on the −inf-padded observed-only view | T-STARTS-VALIDITY (below) | PASS | none |
| PIN-SPLINE-MASKED-RSS | r4 §5/§8 | `rss_of(c,x,O)` from the loaded namespace; 146-mode enumeration; mode equivalence `|ΔRSS|<=1e-12+1e-9·max`; winner=min mode; equivalent-mode set and per-mode validity now exposed (X-11) | NR-SPL + every real/acfexport spline context | PASS (30/30 NR-SPL rows; 20 real/acfexport contexts × 146 modes) | none |
| PIN-ACF | D-C3-ACF-ESTIMATOR | `acf_classical` explicit sequential float64 loops; bitwise vs `acf_classical_b` | T-ACF-RESIDUAL: every RUN1 full-data residual series (X-05) + 4 closed-form vectors | PASS: bitwise-equal(all)=true; strict-vs-(b),(c)(all)=true | none |
| PIN-RHOCV | r4 §3-C2 | `numpy.corrcoef(z_i, ghat_cv_i)[0,1]` | C2 computation, real + INJ | PASS | none |
| PIN-RMSE-EDGE | r4 §3-C4b | `sqrt(Σ(probe−ref)²/E)` on full-grid z_ddof0 curves | real C4b (now evaluated, S-1=(a)) + INJ | PASS | none |
| PIN-SSTAB-W | r4 §3-C5 | `np.quantile` IQR / frozen W widths | C5, real + INJ | PASS | none |
| PIN-MEDIAN | r4 §3 common fields | `numpy.median` float64 | all criteria | PASS | none |
| PIN-IQR | r4 §3-C5 | `numpy.quantile([0.25,0.75], method="linear")` | C5 | PASS | none |
| PIN-TAU-COMPARE | record r1 §2; r4 §9 | `abs(delta)<=tau_j` float64; direction per criterion | D-P04 fixtures | PASS | none |
| PIN-WORSE-SEX | v5 §5 | C1 min, C2 min, C3 max, C4a min, C4b max, C5 max; C6=k_F | D-P04 fixtures | PASS | none |
| PIN-CONSULTED-PATH | r4 §9.1 | level consulted only if all earlier EQUIVALENT; terminate on RESOLVED | D-P04 fixtures | PASS | none |
| PIN-TERMINAL-FALLBACK | r4 §9 | all levels EQUIVALENT ⇒ `TERMINAL_FALLBACK_MECHANISM_P01` | INJ-DP04-TERMINAL, INJ-U2-RHO-INVALID, INJ-U5-C2-INDEPENDENT, INJ-U5-SST-INVALID | PASS | none |
| PIN-K05-INVARIANT | record r1 §4; T-3=AUTHORIZE (X-20 wording) | assert: C4b completeness share `>= c_complete` ⇒ ident `>= c_ident`; row wording corrected per X-20 (INJ-C4B-FLOOR-FAIL is the legitimate excluded-combination proof, K-05 invariant reads C4b-completeness-PASS ⇒ C4a-PASS) | every fixture with C4 data | PASS (assert never triggered; INJ-C4B-FLOOR-FAIL exercises the legitimate case) | none |

## Corrected in r2 (X-07/X-08/X-09)

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result | scientific_freedom |
|---|---|---|---|---|---|
| PIN-U-SETS | r4 §9.2 VERBATIM as ratified by record r1 §3 item 4.1; X-07 | U2/U3/U4 as r1 (criterion-specific validity of P-01∧P-02∧SPL, or probe-success for U4); **U5 corrected to P-01∧P-02 validity only, NO spline term, NO completion-only shortcut** (`valid(rho)=notNone∧isfinite`); construction-time exclusion of an invalid observation is the frozen construction, never a STOP; two narrow STOP labels kept distinct: `CONTRACT_VIOLATION_EMPTY_U` (empty consulted set) and `CONTRACT_VIOLATION_INCONSISTENT_U` (member found invalid AFTER construction, new in r2) | T-U2-RHO-INVALID-EXCLUDE, T-U5-INDEPENDENT-OF-C2, T-U5-SST-INVALID-EXCLUDE, T-U-POST-CONSTRUCTION-INVALID, T-U-EMPTY | PASS: INJ-U2-RHO-INVALID `\|U2\|=9` both sexes; INJ-U5-C2-INDEPENDENT `\|U5\|=10` (C2-invalid did not shrink U5); INJ-U5-SST-INVALID `\|U5\|=9` in F; INJ-U-POST-CONSTRUCTION-INVALID → `CONTRACT_VIOLATION_INCONSISTENT_U`; INJ-DP04-EMPTY-U → `CONTRACT_VIOLATION_EMPTY_U` (unchanged) | none |
| PIN-UNDEFINED-FLAGS | r4 §3 (§8.1); X-09 | `valid(v) ⇔ v is not None ∧ math.isfinite(v)`; P03-direct: `cc[i] ∧ valid(stat[i])`; D-P04 U-set construction: `valid(stat[i])` directly (X-07); NaN never silently treated as valid or RESOLVED | T-FINITE-P03 (INJ-NAN-STAT), T-FINITE-DP04 | PASS: INJ-NAN-STAT → `RESOLVED_MECHANISM_P01` (NaN excluded at P03 layer via §8.1, not a failed comparison) | none |
| PIN-P03-STATUS | r4 §3; X-08 (AUD-19) | two separate rules: (i) family P03 status = FAIL iff >=1 criterion definitely fails in either sex regardless of any earlier PENDING (fixes the r1 bug where an earlier PENDING masked a later definite FAIL); PASS iff all definite-pass; PENDING iff neither; (ii) mechanism outcome is a function of the two family statuses ONLY — any PENDING (incl. FAIL+PENDING) ⇒ `MECHANISM_UNDETERMINED_PENDING_EXACTNESS`, never resolved by the other family's status | T-P03-STATUS-A/B/C | PASS: INJ-P03-C4PENDING-C5FAIL → P-01 `p03=FAIL` (definite_failures=[C5]) despite pending C4, mechanism `MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING)`; INJ-P03-BOTHFAIL-C4PENDING → `STOP_BOTH_FAIL_REDESIGN` (a definite FAIL+FAIL leaves no PENDING in the combination) | none |

## New in r2

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result | scientific_freedom |
|---|---|---|---|---|---|
| PIN-A5-SUPPORT | S-1=(a); PI-ratified §2, da0c4064… | **PI_RATIFIED, VERBATIM.** `lo=min(z)`, `hi=max(z)`, `thr=lo+0.5(hi-lo)`, `S={t: z[t]>=thr}` on the existing full-data finite reference (shared across P-01/P-02/spline, never a fitted curve); `A5_i(side)=(S subset of M_side)`; `M_LEFT={0..14}`, `M_RIGHT={131..145}`; contract-violation guard (missing/nonfinite/wrong-length/empty-support) raises rather than silently proceeding | real C4a/C4b determination on SCEN-A/SCEN-B/FIX-STARTS-* (4 trajectories) | PASS: A.5(i) false on all 4 real trajectories (support never fully inside either 15-point edge mask; sizes 32-54); real C4a/C4b now evaluated (no longer STOP_EXACTNESS_PENDING) | none — transcribed verbatim, tagged PI_RATIFIED |
| PIN-SOLVER-B-UNVERIFIABLE | S-2=alpha; PI-ratified §3, da0c4064… | **PI_RATIFIED, VERBATIM.** Covered event = RuntimeError from `nnls(A[act].T,g)` inside `kkt_res` via `accept()` for a SOLVER-B stage-1/stage-2 acceptance check; disclosed runtime wrapper around the loaded `accept()` (namespace rebinding only, frozen file bytes untouched); on the event: record evidence, return NOT ACCEPTED at that stage; existing stage-2-expansion / stage-3-SLSQP control flow continues unmodified | T-EXC-CAPTURE (X-02) | PASS: 1 injected capture (stage 1, `TEST_ONLY_INJECTION` tag) + 2 natural captures (stage 2, "Maximum number of iterations reached", genuinely occurring at SCEN-A run1:F0:full mode 113 — reported as a real finding, not asserted away); chain correctly continued past every captured stage to a valid or FAILURE terminal state in all cases | none — transcribed verbatim, tagged PI_RATIFIED |
| PIN-STARTS | X-03 (AUD-05) | `fit_family` takes an explicit `start_bank` parameter; DEFAULT (unspecified) = full retained lattice (`range(len(retained))`); `"MINI_BANK"` = frozen `mini_bank_indices` (declared per-fixture, D-04); feature start accepted iff finite ∧ numerically feasible ∧ `zero_variance_rule=="OK"` ∧ `scientific_domain_pass_*` ∧ `kural_t_pass_exact_*` ∧ `kural_s_pass_exact` ∧ not an exact-tuple duplicate of a bank start; rejection reason recorded | T-STARTS-DEFAULT (FIX-STARTS-FULL), T-STARTS-VALIDITY, T-STARTS-DUP (FIX-STARTS-DUP) | PASS: FIX-STARTS-FULL start_bank_size = 732 (P-01, 731 retained+feature) / 262 (P-02, 261 retained+feature); FIX-STARTS-DUP `FEATURE_START_REJECTED(DUPLICATE)` at u_star∈{0.0,1.0} on the real path, both sides | none |
| PIN-PROBE-SUCCESS | X-04 (AUD-06) | `probe_success` = the truncated refit's own eligibility (`fit_family(...).eligible`), decoupled from the full-data fit's eligibility; A.5 failure (PIN-A5-SUPPORT) additionally excludes a probe from the C4a numerator and the C4b paired-valid set; C4b's RMSE_edge still requires the full-data reference (pre-existing, not newly imposed on probe_success) | UT-PROBE-DECOUPLE | PASS: full-data fit forced ineligible while the probe fit remained eligible ⇒ `probe_success_c4a=true` (C4a numerator counted), `rmse_computable=false` (absent from C4b paired set, no reference available) | none |
| PIN-LOADER-NODE-HASHES | X-01 | per-node SHA256 recorded for every retained/prelude node (`node_hashes` in test evidence) plus the explicit SOLVER-B function-set hash table (`solver_b_function_hashes`) | T-LOADER-NODES | PASS: 52 retained + 21 prelude nodes hashed; 10/10 SOLVER-B functions found and hashed | none |
| PIN-TELEMETRY | T-4=T-4a; X-11a | disclosed wrapper around `scipy.optimize.minimize` in the loaded spline namespace; one row per trust-constr/SLSQP call: status, message, nit, nfev, njev, wall time, objective | T-4a scope (v5 §8 unchanged) | PASS (scope unchanged, not narrowed — T-4b not chosen) | none |
| PIN-CANON-DOC | X-11d | canonical RUN1/RUN2 document = `evals`+`stops`+`a5`+`ut_probe_decouple`+`pins` (ACF/A5-detail/unit-test objects excluded, moved to the separate test-evidence document, X-11d); per-fit theta/L/start-bank-size/FEATURE_START_REJECTED and per-spline-fit mode/RSS/equivalent-mode-set/per-mode-validity now present in the evaluation-layer records | T-CANON | PASS: RUN1 canonical SHA256 == RUN2 canonical SHA256 = `31686de0…` | none |

## TEST_CONSTANT rows (engineering; test code only — never enter any result, statistic, gate, comparator, or the scientific literal registry)

| constant | where | role |
|---|---|---|
| closed-form ACF test vectors: alternating `(-1)^t`, linear `t`, constant `1.0`, mixed `sin(0.37t)+0.25cos(1.7t)` | acf_verify (main) | TEST_CONSTANT |
| T-MASK-FULL test theta `(0.3,0.7,20.0,20.0)` and test mask `np.arange(20,120)` | PIN-MASKED-OBJECTIVE check | TEST_CONSTANT |
| UT-A5 synthetic spike vector (`x[70]=3.0`, z-scored) | UT-A5-II / UT-A5-III | TEST_CONSTANT |
| monotone TEST_CONSTANT vectors (`T-t` and `t`, z-scored, unique argmax at index 0 / 145) | FIX-STARTS-DUP | TEST_CONSTANT |
| fixture construction constants (bump centers/widths, noise sigma 0.10, seeds 20260906-20260912; INJ statistic values in the generator) | fixture generator r2 | TEST_CONSTANT (declared in the r2 fixture manifest; PATH_COVERAGE_ONLY) |

```text
new_scientific_literal_by_executor = 0
PI_RATIFIED content transcribed verbatim: PIN-A5-SUPPORT, PIN-SOLVER-B-UNVERIFIABLE
  (both tagged PI_RATIFIED with the content file's hash da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498)
Every pin's result is bound to f3_step2_correction_report_r2_2026-09-07.md and
f3_step2_results_r2_2026-09-07.json; "see report" resolves there.
commit = false
```
