# p_konum_plus — F3 STEP-2 r2 — Correction Execution Report

```text
artifact_role  = correction report (deliverable 10 of the STEP-2 r2 correction cycle)
status         = NON-NORMATIVE ; every result below is an EXECUTOR CLAIM,
                 independent verification pending (§15 audit, not performed here)
task           = Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
                 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
PI-ratified    = p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
                 da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
date           = 2026-09-07
F3_EXECUTION_READY = false ; real_data_access = false ; commit = false
```

---

## 1. §2 custody verification (repeated here for the record; performed at dispatch)

All §2.1 (11 items) and §2.2 (7 items, item 13's previously-undelivered hash now observed
and self-consistent with its own sidecar) matched their recorded/observed hashes exactly.
All six present §2.2 sidecars verified consistent with their target files. §2.3 record-class
items 20–23 (independent audit r4, cross-auditor reconciliation r3, ADDENDUM A r1, PIN
prompts v2–v4) were NOT_LOCATED in the repository and NOT attached at dispatch — recorded
as such per the STOP-scope rule (record-class absence is never a STOP). §2.3 dispatch-class
items 24 (PI-ratified content) and 25 (this prompt) matched. No surrogate was used for any
item. Full detail: the dispatch-turn conversation record; hashes re-stated in §9 below.

## 2. §3 dispatch preconditions

```text
P-1  PASS — every §2.1/§2.2 item present and exact; item 13 hash recorded and sidecar-consistent
P-2  PASS — PI-ratified content file present, hash recorded, all MANDATORY fields explicit
P-3  PASS — no MANDATORY field of §4.1/§4.2 remained PENDING after reading item 24
P-4  PASS — observed hash of the dispatched draft (17187d31…) equals the value recorded in
             the PI-ratified content file's source table
```

S / T values as read (verbatim): S-1=(a), S-2=alpha, T-1=AUTHORIZE, T-2=T-2a, T-3=AUTHORIZE,
T-4=T-4a, T-5=CONFIRM_WITHIN_SCOPE. Every field this cycle authorizes was AUTHORIZE/chosen —
no DEFERRED, no REFUSE, no REQUIRE_ALTERNATIVE, no narrowed (T-2b/T-4b) option was selected.
This is the full-scope combination: every §4.5 path is enabled, including the real C4a/C4b
determination (S-1) and the spline path (T-1).

## 3. Write order followed (§3, binding)

W-1 (permitted custody writes): no r1 sidecar was missing (§2.2 item 19 exception not
needed); no record-class item was attached at dispatch to import (X-15) — items 20–23 remain
NOT_LOCATED. W-2: r2 harness, r2 fixture generator, and r2 fixture manifest were prepared and
the manifest was hashed BEFORE any test or run. W-3: SHA256 of the prepared harness, generator,
and manifest were computed and the pre-execution custody record was written naming those exact
bytes, BEFORE the first test. W-4: NR-01(i) ran first, then NR-01(ii)/NR-SPL, then RUN1/RUN2.
W-5: this report and the remaining deliverables were written last.

## 4. Correction scope — finding → correction → verification (§5)

Full pin-by-pin correction ↔ test ↔ evidence detail is in
`f3_step2_class_c_pin_register_r2_2026-09-07.md` (deliverable 9), which every result below
is bound to. Summary by correction id:

```text
X-01  PIN-SPLINE-LOADER exact node-list authorization + per-node hashes         PASS
X-02  PIN-EXC-CAPTURE (S-2=alpha wiring)                                        PASS
X-03  PIN-STARTS (default full lattice; frozen validity + dedup predicate)      PASS
X-04  PIN-PROBE-SUCCESS (decoupled from full-data fit) + A.5 wiring (S-1)       PASS
X-05  PIN-ACF residual-series export + exact-rational ulp deviation             PASS
X-06  NR-01(i) assertion (not only recorded) + NR-01(ii) T-2a wrapper adapter   PASS
X-07  PIN-U-SETS rebuild (criterion-specific validity; two narrow STOP labels)  PASS
X-08  PIN-P03-STATUS (family status / mechanism outcome, two separate rules)    PASS
X-09  PIN-UNDEFINED-FLAGS (finite-valued validity)                              PASS
X-10  fixture fidelity (execution-site keys)                                   PASS (4/4)
X-11  telemetry / canonical-document enlargement / test-evidence split         PASS
X-12  register and report wording                                              applied (this pair of documents)
X-13  exact-rational deviation (no premature float rounding)                   PASS (alt 0.2465753424657534 / lin 0.2602739726027397 ulps, matches audit-independent values)
X-14  STOP_UNDEFINED_CONSULTED_SCALAR removed as a separate branch             applied (X-07's two labels only; see §6 note below)
X-15  custody imports                                                          NOT APPLICABLE (nothing attached to import this cycle)
X-16  coverage matrix evidence-class labels                                    PASS (49/49 rows labelled; see §6)
X-17  LF encoding for text deliverables                                        PASS (csv/json/md written with explicit newline="" or "\n")
X-18  opened-file list via sys.addaudithook                                    PASS (declared 12; audit-derived 3 — audit hook does not observe non-open() library loads, e.g. compiled extension dlopen; both lists reported, not reconciled beyond that)
X-19  PIN-MASKED-OBJECTIVE register wording (mechanism per T-5)                applied (register r2)
X-20  K-05 row wording (T-3=AUTHORIZE)                                         applied (register r2)
```

Note on X-14/§10: `run_dp04`'s two remaining STOP-class subset-level results are
`STOP_CONTRACT_VIOLATION_EMPTY_U` and `STOP_CONTRACT_VIOLATION_INCONSISTENT_U`; a third,
pre-existing early-return (`scal["P01"] is None or scal["P02"] is None`, guarding an
unconsulted/structural scalar) was retained but now also reports
`STOP_CONTRACT_VIOLATION_EMPTY_U` rather than the withdrawn `STOP_UNDEFINED_CONSULTED_SCALAR`
label, since neither this cycle's fixtures nor the frozen contract define a third label for
that branch and inventing one would be a new scientific literal (§10 applies if this is ever
reached in a future run; it was NOT reached in r2 — no fixture exercises it).

## 5. Non-regression gate results (§8)

```text
NR-01 (i)   PASS — frozen-suite replay through the loaded F2 engine; canonical hash
            6f197b74e3d4224git 8393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403 ==
            expected; telemetry field equality ASSERTED true (X-06)
NR-01 (ii)  PASS — T-2a wrapper-qualification adapter: FIX-P01-BENIGN / FIX-P02-BENIGN
            replayed through fit_family (mask=FULL, start_bank=MINI_BANK, D-04)
            spliced in place of the frozen engine's native records; hybrid canonical
            document hash == 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403
            (identical to NR-01(i)'s own hash) — the wrapper reproduces the frozen engine's
            benign-fixture path exactly
NR-SPL      PASS — 30/30 rows reproduced field-for-field against the frozen r2 spline
            qualification results (ffda04b0…), executor environment
```

## 6. Coverage matrix

49/49 rows from the r2 fixture generator's `COVERAGE_ROWS` report `covered` or
`covered_injection_only` (X-16 evidence-class labels: `real_fit`, `decision_layer_injection`,
`unit_test`, `assertion`, or a `;`-joined combination) — none `PENDING` or `UNCOVERED`, since
every S/T field this cycle authorizes was enabled. Full table: `results` JSON `coverage` array
(also reproduced in the r2 fixture manifest's `expected_outcome` / `evidence_class` columns).
Notable rows: "C4a pass (real probe computation)" and "C4b pass/fail (real)" are now
`real_fit`-covered (previously `PENDING(F3-STEP2-EXACT-01)` in r1, resolved by S-1=(a)).

## 7. Fixture fidelity (X-10)

```text
implemented = 4/4 ; executed = 4/4
```
Scope: the 4 real-fit fixture/context pairs with an execution-site construction-evidence
record (SCEN-A, SCEN-B, FIX-STARTS-FULL, FIX-STARTS-DUP), audited via `construction_audit`
(A.5 support size and condition per real trajectory: SCEN-A F0 size=42, M0 size=54; SCEN-B F0
size=41, M0 size=32 — A.5(i) false on all four, i.e. no trajectory's support falls wholly
inside either 15-point edge mask). INJ fixtures are constructed directly (no execution site to
diverge from); their fidelity is definitional, not audited by this mechanism.

## 8. Exactness / engineering findings

None open. `exactness_findings = []`, `engineering_findings = []` in the r2 results JSON — no
implementation choice this cycle required a PI decision the frozen contract and §4.3 did not
already determine, and no required computation was impossible without modifying a frozen
artifact. (F3-STEP2-EXACT-01 and -02, open in r1, are CLOSED by S-1/S-2 respectively; neither
number is reused.)

## 9. Determinism, hashes, environment

```text
RUN1 canonical SHA256 = 31686de030a5493fd2493e0b459f0b7057fbbc678c4b43bd19cd450ade3bac2d
RUN2 canonical SHA256 = 31686de030a5493fd2493e0b459f0b7057fbbc678c4b43bd19cd450ade3bac2d
determinism            = true
python = 3.11.7 ; numpy = 1.26.4 ; scipy = 1.14.1 ; platform = Windows-10-10.0.19045-SP0
OMP_NUM_THREADS = OPENBLAS_NUM_THREADS = MKL_NUM_THREADS = 1
cross-process / cross-platform bitwise reproducibility: NOT claimed and NOT to be claimed
```

Deliverable hashes (path — SHA256):
```text
1. f3_step2_adequacy_harness_r2_2026-09-07.py
   78b6210ace605fe9b43a3b15716535df28b8a25a11a072f68484e9cb7ad12776
2. f3_step2_fixture_generator_r2_2026-09-07.py
   a1e6068c0868e7594242fcc6d588cc255f3b0f4bdf21d1e93851e5bafcf98e25
3. f3_step2_fixture_manifest_r2_2026-09-07.csv
   807f49b30ac453e95259d39b546515acff8f93c2d6b7bebf81cd4a44621e3beb
4. f3_step2_r2_preexecution_custody_2026-09-07.md
   afddfb590b78caea08dcde0ca28141e31835a8b3857af973b30a6a5eeff8a743
5. f3_step2_telemetry_r2_2026-09-07.csv
   0459344f2b518531d5732577b98f031684ca29e3815c0e51af75b857be60155a
6. f3_step2_results_r2_2026-09-07.json
   7b78b7ba64ded891fdd5098d3a35556938d1314c5d712a7dc6ee6046b7a26ed2
7. f3_step2_residual_series_r2_2026-09-07.json
   f28bd6a02978154d1ba71d83a8ffe42cdc5e95d12a26c43b886439cca19b94f5
8. f3_step2_test_evidence_r2_2026-09-07.json
   109ca273fbaf2e47800c048a87e72e9064c576642ecbe2a7e9e1331cf9426c0b
9. f3_step2_class_c_pin_register_r2_2026-09-07.md
   (computed and sidecar-written alongside this report; see item 9 sidecar)
10. f3_step2_correction_report_r2_2026-09-07.md (this file)
   (self-hash not applicable per §12; external sidecar only)
```

## 10. Opened-file list (X-18)

Declared (manually tracked, `OPENED_FILES`) — 12 files: the r2 harness itself, the two frozen
custody-critical inputs (D-F2-09 start-grid manifest, F2 engine), the F2 fixture manifest and
frozen telemetry, the frozen spline harness and its frozen results CSV, the r2 fixture
generator, the r2 fixture manifest, and the three r2 outputs opened for their own post-write
hash (residual series, telemetry, test evidence).

Machine-derived (`sys.addaudithook`, filtered to paths under this repository) — 3 entries: two
`.pyc` cache files (F2 engine, r2 fixture generator) and the r2 harness source file itself. The
audit hook observes only the `open` event; it does not observe compiled-extension `dlopen`
(numpy/scipy's own `.pyd` loads), which is why the machine-derived list is sparser than the
declared list — this is a known, accepted limitation of the "optional but recommended" X-18
mechanism, not a discrepancy in file access.

## 11. Solver exception evidence (S-2/X-02) — a real, non-injected finding

Three `PIN-EXC-CAPTURE` records total: one is the deliberate `T-EXC-CAPTURE` injection (stage
1, tagged `TEST_ONLY_INJECTION` in its message, fired on the first live `nnls` call reached for
the declared fixture SCEN-A). The other two are **genuine, non-injected** SOLVER-B
unverifiable-acceptance events: `nnls` raised `RuntimeError("Maximum number of iterations
reached.")` at SCEN-A, trajectory F0, full-data context, spline mode 113, stage 2 — reproduced
identically across the two independent full-data spline fits that touch that trajectory (the
RUN1 real-scenario pass and the separate ACF-residual-export pass). In every one of the three
cases, S-2=alpha's policy (record and treat as NOT ACCEPTED at that stage; let the existing
stage-2-expansion/stage-3-SLSQP control flow continue unmodified) was applied correctly and the
fit reached a valid terminal state. This is reported as a genuine finding, not suppressed: it
demonstrates the S-2 gap this cycle's PI decision closed was not hypothetical — the frozen
SOLVER-B chain does encounter this condition on ordinary synthetic data.

## 12. Required end-state (§14)

```text
F3_STEP2_r2_harness_created = true
dispatch_preconditions      = P-1..P-4 ALL PASS
PI_ratified_content_hash    = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
S-1=(a) ; S-2=alpha ; T-1=AUTHORIZE ; T-2=T-2a ; T-3=AUTHORIZE ; T-4=T-4a ;
T-5=CONFIRM_WITHIN_SCOPE (explicit, not blank)
work_plan_applied           = every §4.5 path enabled (full-scope combination); no path stopped
NR-01 (i)                   = PASS, hash 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403
NR-01 (ii)                  = PASS, T-2a, hybrid hash == NR-01(i) hash, scope unchanged (not narrowed)
NR-SPL                      = PASS, 30/30 rows
corrections X-01..X-20      = all applied; X-15 NOT APPLICABLE (nothing to import); test ids and
                              results in §4 above and in the pin register r2
fixture fidelity            = 4/4 implemented ; 4/4 executed
coverage_complete           = true (49/49 rows covered; none PENDING/UNCOVERED)
exactness / engineering findings = none open
determinism                 = true (RUN1 == RUN2 canonical SHA256)
real_data_access = false ; opened-file list = §10 above ; generator_selected = false
P03_threshold_values = NOT_COMPUTED ; new_scientific_literal_by_executor = 0
status fields (§13, reported separately, none implying another):
  corrections_complete = true
  mandatory_tests_all_run = true
  deferred_decisions = []
  narrowed_evidence = []
  uncovered_coverage_rows = []
  open_findings = []
F3_STEP2_r2_status          = CORRECTED_PENDING_INDEPENDENT_AUDIT
F3_EXECUTION_READY = false ; F3_started = false ; commit = false
```

No wording in this report or the pin register asserts "verified", "QUALIFIED", or
"audit PASS" about the executor's own output. `F3_STEP2 = QUALIFIED` can be declared only by
the PI after the independent audit of §15, which this task does not perform.
