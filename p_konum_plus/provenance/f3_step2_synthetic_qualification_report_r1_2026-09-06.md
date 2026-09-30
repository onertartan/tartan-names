# p_konum_plus — F3 STEP-2 — Synthetic Qualification Report r1 (2026-09-06)

```text
artifact_role = STEP-2 synthetic path-coverage qualification report
                (deliverable 7 of the v5 task)
status        = NON-NORMATIVE ; interpretation = PATH_COVERAGE_ONLY
frozen_contract = r4 5e594136… AS RATIFIED BY freeze record r1 7055f186… ; v11 wins
execution_prompt = Claude_Code_F3_STEP2_CLASS_C_IMPLEMENTATION_PIN_PROMPT_v5_2026-09-06.md
                   (dispatched download variant ..._v5_20260906.md; observed SHA256 =
                    1532a5e481946d7c64d2ac5025ef16372b1f6530ab4fbc8aa5567392f18cf0af)
```

## 1. Custody (§1) — verified from scratch this run

STOP-class items 1–11: ALL EXACT — v11 `d136502f…`; F2 FREEZE r1 `ee2cb99d…`;
F2 engine `01714752…`; F2 fixture manifest `daa5fd08…`; start lattice
`c39fb519…`; D-F2-09 packet `8ff70a64…`; F2 telemetry `cd7218b1…`; spline r2
bundle `e71ce030…` / `b31e5a6b…` / `ffda04b0…`; r4 `5e594136…`; record r1
`7055f186…`; parent record `bef216e3…`. Record-class: item 12 `99b615d2…`
EXACT; 13 `7cc4843f…` EXACT; 14 `a48c516b…` EXACT; 15 `84c24165…` EXACT;
16 = observed `1532a5e4…`; **17 ADDENDUM A r1 = NOT_LOCATED in the
repository** (its dispatched text, read during the r3→r4 task, contains no
operational data-level Kural-S support definition — §7 below); 18 `f4d8e800…`
EXACT; 19 `0a43dad7…` EXACT; 20 NOT_LOCATED; 21 `afc49ca8…` EXACT;
22 NOT_LOCATED; 23 `00784bda…` EXACT; 24 NOT_LOCATED.

## 2. §1.1 pre-dispatch state — aborted v1 run

Inventory of files created by the aborted v1 dispatch: **EMPTY** — the v1 run
was stopped during read-only custody/inspection; no `f3_step2_*` file and no
other file was created or modified (verified twice: at the PI's revert request
and again at this run's start; `git diff` empty both times). Nothing to
quarantine; the quarantine directory was not created (nothing to move);
nothing was reused. No tracked repository file was modified.

## 3. Engine loading

```text
PIN-F2-LOADER     : importlib by path; SHA256 verified BEFORE load =
                    01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077
                    (file is __main__-guarded; the F2 suite does not run at import)
PIN-SPLINE-LOADER : definition-only AST loader; SHA256 verified BEFORE parse =
                    b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d
                    retained nodes (§3.3 classes) = 52 ; definitional-support
                    prelude nodes (lexically before the phase-1 orchestration
                    marker; no open()/print(); byte-identical source segments)
                    = 21 ; excluded orchestration/I-O nodes = 31
                    node lists recorded in the results JSON
                    correctness proof = the spline non-regression (§4)
```

Loader note (informational): the literal §3.3 retained-node classes leave the
retained functions without their definitional constants (B, D1, coefficient
vectors, option dicts, masks), which are created by call/loop nodes that are
NOT run-orchestration state; §3.3 rule 6 therefore does not apply, and the
loader executes those prelude nodes unmodified. Disclosed in PIN-SPLINE-LOADER.

## 4. Non-regression gates — both PASS

```text
NR-01                 = PASS ; the F2 r3 suite executed through the loaded
                        engine reproduced the accepted RUN1 canonical SHA256
                        6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403
                        and all 12 telemetry rows equal the frozen CSV on every
                        non-wall-clock field ; wrapper equivalence: with mask =
                        FULL the wrapper applies NO patch (frozen path verbatim)
spline non-regression = PASS ; all 30 r2 qualification result rows rebuilt via
                        the loaded SOLVER-B functions equal the frozen
                        ffda04b0… CSV field-for-field
```

## 5. Pin verification results (register: deliverable 6; all scientific_freedom = none)

```text
PIN-MASKED-OBJECTIVE : full-mask patched fun == frozen fun bitwise (float.hex) ;
                       L_O <= L_FULL asserted on every masked eligible fit
                       (zero violations across 4645 telemetry rows)
PIN-FEATURE-START-MASKED : -inf-padded frozen feature_start == direct
                       min{j in O : x_j = max} formula
PIN-ACF              : 8 verification vectors (4 closed-form TEST_CONSTANTs +
                       4 RUN1 fixture z-series): bitwise equality of the two
                       independently written sequential implementations on ALL ;
                       strict inequality vs alternative (b) (x146/145) and
                       alternative (c) (corrcoef on lagged vectors) on ALL
                       defined vectors ; constant vector => den == 0 => undefined
                       (no substitution) ; exact-rational Fraction cross-check:
                       ulp deviation 0.0 on the closed forms (informational)
PIN-K05-INVARIANT    : asserted on every fixture with C4 data; zero violations
PIN-U-SETS / PIN-CONSULTED-PATH : INJ-DP04-C1 recompute counters all zero for
                       unconsulted levels (evidence logged); INJ-DP04-C2-DIVERGE
                       demonstrates the ratified same-set rule deciding against
                       the candidate-specific ordering (P03 candidate-specific
                       C2 medians favour P-02 by 0.02; common-set U2 medians
                       favour P-01 by 0.01 > tau_2; RESOLVED for P-01;
                       |U2|/n_s = 0.8 disclosed with NO floor)
mechanism labelling  : outputs contain mechanism_outcome only; the harness
                       asserts no winner/selected/generator_selected key
A.5 (ii)/(iii)       : code written and unit-tested only (UT-A5-II PASS,
                       UT-A5-III PASS); A.5 not applied; no C4 fixture outcome
```

## 6. Fixture fidelity and coverage

```text
fixtures declared = 22 (manifest d9fb75f8c643f53a67032e4b65a5bec1af85ccbdf1cb47c58577c1d3f23b565b,
                    written and hashed BEFORE execution)
implemented = 22/22 ; executed = 22/22 (fidelity 100 %)
mechanism outcomes (all as predeclared; PATH_COVERAGE_ONLY):
  SCEN-A  PENDING_EXACTNESS(F3-STEP2-EXACT-01)   [real; C4 gate pending]
  SCEN-B  STOP_BOTH_FAIL_REDESIGN                [real path: P-01 fold-failure
          injection fails C2 completeness; P-02 fails C2 completeness via the
          injected spline FAILURE — BOTH_FAIL reached before C4]
  INJ-C1..C5/SEX fixtures -> ONLY_P02_PASSES ; INJ-ONLY-P01 -> ONLY_P01_PASSES ;
  INJ-BOTH-FAIL -> STOP_BOTH_FAIL_REDESIGN ;
  INJ-DP04-{C1,C2-DIVERGE,C3,4A,4B,C5} -> RESOLVED_MECHANISM_P01 at the
  targeted level ; INJ-DP04-TERMINAL -> TERMINAL_FALLBACK_MECHANISM_P01 ;
  INJ-DP04-EMPTY-U -> STOP_CONTRACT_VIOLATION_EMPTY_U (TEST_ONLY_INJECTION)
STOP branches exercised: BOTH_FAIL_REDESIGN (real + injected) ;
  CONTRACT_VIOLATION_EMPTY_U (injected, level C2)

coverage_complete = false — PENDING rows (all due to F3-STEP2-EXACT-01):
  C4a pass/fail (real probe computation) ; A.5(i) condition ;
  C4b pass/fail (real) — the C4a/C4b/D-P04-4a/4b DECISION-LAYER logic is
  covered via TEST_ONLY_INJECTION fixtures (does not qualify the real C4 path)
  and A.5 (ii)/(iii) are unit-tested pending; every other coverage row of the
  §7 matrix is covered (full matrix in the results JSON)
```

## 7. Exactness findings (§12) — none resolved by Claude Code

```text
F3-STEP2-EXACT-01  (gate-specific blocker)
  rule    : r4 §3-C4a A.5 condition (i) via record r1
  gap     : no exact frozen data-level definition of a trajectory's Kural-S
            support region exists. Resolution order applied: (1) ADDENDUM A r1
            NOT_LOCATED in the repository (and its dispatched text states the
            A.5 outcome rule only, no operational support definition);
            (2) frozen F2 Kural-S semantics (n_sup / kural_s_pass_exact,
            engine lines 115-121) are defined on stabilized FITTED curves and
            do not determine the support REGION of a data trajectory
  options observed (not chosen): (a) PI supplies an operational data-level
            definition; (b) PI designates a fitted curve on which A.5(i) is
            evaluated; (c) PI removes condition (i)
  wiring  : A.5 applied whole-or-not-at-all — the C4a determination on real
            fixtures returns STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-01);
            C4a/C4b and D-P04 4a/4b real paths PENDING; C4 cannot be declared
            qualified until the PI closes the gap
```

Engineering note ENG-NOTE-01 (informational; no frozen code modified): during
full 146-mode enumeration on synthetic fixture vectors, the frozen SOLVER-B
acceptance evaluation can raise (scipy NNLS "maximum number of iterations
reached" inside the KKT-existence certificate) on a degenerate mode — a case
never reached by the 10 tame r2 qualification fixtures. The ratified rule
states an endpoint is "acceptable ONLY if all of the following hold"; when the
conditions cannot be shown to hold, the endpoint is not accepted, so the
wrapper records that mode as numerically invalid (`ACCEPTANCE_UNVERIFIABLE`)
and continues. Observed exactly once in RUN1+RUN2 (telemetry row count 1;
winner modes unaffected — the affected mode is a poorly aligned one). The
frozen r2 file is byte-unchanged. Flag for the PI: production F3 execution on
real data will traverse the same 146-mode enumeration; if the PI prefers an
explicit written rule for unverifiable-acceptance modes, it can be added as a
CLASS_C pin at the F3 execution gate.

## 8. Determinism, telemetry, environment

```text
RUN1 canonical SHA256 = e7fbb85f9db9d63ca44be61f7862529f4fddc5ca2375ef0a95594f754282f22c
RUN2 canonical SHA256 = e7fbb85f9db9d63ca44be61f7862529f4fddc5ca2375ef0a95594f754282f22c
DETERMINISM = true (same process, thread-pinned OMP/OPENBLAS/MKL = 1;
              cross-process / cross-platform bitwise reproducibility NOT claimed)
telemetry (RUN1 only) = 4645 optimizer-call rows
              (incl. 1 ACCEPTANCE_UNVERIFIABLE, 2 TEST_ONLY_INJECTION rows)
environment = Python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ;
              Windows-10-10.0.19045-SP0 ; OMP=OPENBLAS=MKL=1
runtime notes (recorded, non-scientific): one full-grid 146-mode SOLVER-B
              spline fit ~90 s; SCEN-A n_s = 1 per sex chosen for runtime
              (harness is n-agnostic; declared in the manifest)
rng_used    = fixture generation only (recorded seeds); no RNG in any fit or
              verification test
real_data_access = false ; files opened by the harness (complete list, also in
the results JSON): the frozen F2 engine + its fixture manifest + telemetry +
start-lattice manifest; the frozen spline r2 harness + results CSV; the
STEP-2 fixture generator + fixture manifest. No F1/SSA path.
```

## 9. End state (§13)

```text
F3_STEP2_harness_created = true
F3_STEP2_NR01 = PASS ; F3_STEP2_spline_nonregression = PASS
F3_STEP2_fixture_fidelity = 22/22 implemented ; 22/22 executed
F3_STEP2_coverage_complete = false (C4-real rows PENDING per F3-STEP2-EXACT-01)
F3_STEP2_exactness_findings = [F3-STEP2-EXACT-01]
F3_STEP2_determinism = true (RUN1 == RUN2)
F3_STEP2_status = PARTIAL_PENDING_PI
  (NR-01 PASS, spline non-regression PASS, fidelity 100 %, determinism true;
   status is PARTIAL solely because F3-STEP2-EXACT-01 is open — a PI-owned
   gap, returned, not resolved)
real_data_access = false ; generator_selected = false
P03_threshold_values = NOT_COMPUTED
F3_EXECUTION_READY = false ; F3_started = false ; commit = false
```

Next action: independent audit of this STEP-2 package (v5 §14), and PI closure
of F3-STEP2-EXACT-01 (bounded options in §7); after both, a narrow rerun of
the C4 paths can complete the coverage matrix.
