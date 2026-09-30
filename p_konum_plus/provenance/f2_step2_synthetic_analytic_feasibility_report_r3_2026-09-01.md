# p_konum_plus — F2 STEP 2 r3 Exact-Construction Fidelity Corrected Full Rerun — Successor Report

```text
artifact_role = F2 STEP-2 r3 exact-construction-fidelity corrected full-rerun provenance
status        = NON-NORMATIVE
parent_execution_report = f2_step2_synthetic_analytic_feasibility_report_r2_2026-09-01.md
parent_report_sha256    = 9d5bf074b099cf597009218a0c16cdba68dabcdd00ee4313165c7c59c165b445
correction_scope = A01_exact_construction_fidelity + A02_required_manifest_column_fail_loudly
                 + A03_standardized_L_bookkeeping + A04_display_precedence_selftest_repair
                 + R3P01_evidence_provenance + R3P02_validator_wiring
                 + R3P03_construction_mapping_disclosure + R3P04_multipredicate_selftest
                 + R3P05_telemetry_synthesis_disclosure
new_methodology_review = false
PI_re_ratification     = false
```

**The r2 report is retained as immutable historical provenance; its final
STEP-2 acceptance claim is superseded by r3 for gate purposes.**

- **Date:** 2026-09-01 · **Worktree:** `G:/PycharmProjects/pkp-worktree` · **Branch:** `p_konum_plus` · **HEAD:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`

---

## 1. Lineage / correction reason

Independent audit of the r2 successor artifacts found one remaining gate-specific blocker (A-01: exact-construction fidelity not enforced — FIX-OTHER-NUMERICAL-FAILURE hard-coded its final record; FIX-INVALID-INIT used an inline check instead of a validator path) plus cleanups A-02/A-03/A-04; the advisory audit of the r3 prompt added R3-P01..P05 (evidence provenance, validator wiring, mapping disclosure, multi-predicate probe, telemetry synthesis disclosure). No global blocker; no ratified scientific decision changed.

## 2. Repository + hash precheck — PASS

Root ✓, branch ✓, HEAD = expected ✓, zero unexpected tracked modifications, 22 known F2-era untracked files recorded pre-task. All ten §0 hashes recomputed exact: v11 `d136502f…`, v0 `b6b4ed83…`, r2a `2bc141c2…`, r2 `d5dd001d…`, D-F2-09 packet `8ff70a64…`, D-F2-09 manifest `c39fb519…`, STEP-2 fixture manifest `daa5fd08…`, r2 harness `3b255550…`, r2 telemetry `d688a16b…`, r2 report `9d5bf074…`. No STOP.

## 3. r2 artifact custody

Re-hashed after the full r3 run: r2 harness `3b2555508e4b731ab3349a040a03a3d266fe068d72cd13427107a998622610bc`, r2 telemetry `d688a16bfd131ee1e1cfe8715a011009b782a78a1ac897c5589cc68af3b8dabb`, r2 report `9d5bf074b099cf597009218a0c16cdba68dabcdd00ee4313165c7c59c165b445` — all byte-identical. ART-F2 r2a also unchanged (`2bc141c2…`).

## 4. Fixture manifest custody

```text
pre-hash  = daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b
post-hash = daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b   (IDENTICAL)
```

Not edited, not regenerated; reused verbatim.

## 5. Required manifest-column audit (A-02)

All seven frozen columns verified present before any fixture execution: `fixture_id, fixture_class, family, purpose, exact_construction, start_selection_rule, forbidden_interpretation`. `missing_manifest_columns = []`. The check is a loud assertion — absence would abort with `F2_STEP2_R3_FEASIBILITY_NOT_READY`; nothing is filtered from the audit result. `execution_mode` remains a harness-internal registry label only (not required in, and not added to, the manifest).

## 6. Full 21-fixture registry and construction-fidelity audit (A-01)

```text
declared_fixture_ids = implemented_fixture_ids = executed_fixture_ids = 21/21 (exact set equality)
metadata mismatches (fixture_class, family) = 0
construction_fidelity_pass = 21/21
```

For every fixture the harness keeps a deterministic construction-evidence record `{fixture_id, manifest_exact_construction, implemented_construction_key, executed_construction_key, construction_fidelity_pass}`. The `executed_construction_key` is composed at orchestration exit from **observed** evidence only (§8); it never comes from the fixture definition or dispatch table.

## 7. Manifest `exact_construction` → `implemented_construction_key` mapping table

**This prose-to-key mapping is a HUMAN-AUDITED provenance step. `construction_fidelity_pass` proves `implemented == executed`, not machine agreement with the manifest prose.** All 21 rows (prose abridged to its operative clause where long; full prose is in the byte-frozen manifest):

| fixture_id | manifest exact_construction (operative clause) | implemented_construction_key | fidelity |
|---|---|---|---|
| FIX-P01-BENIGN | θ=(u0−1/8, u0+1/8, K_mid, K_mid); x=z(stabilized P01 curve); mini-bank {0,365,730}+feature | minibank_3grid+cond_feature_via_run_one_start | PASS |
| FIX-P02-BENIGN | θ=(u0, s_feature, s_feature, √6); x=z(stabilized P02 curve); mini-bank {0,130,260}+feature | minibank_3grid+cond_feature_via_run_one_start | PASS |
| FIX-P01-STABLE-INTERIOR | θ=(0.3,0.7,20,20) hand-declared interior; evaluation only | stable_eval_only_no_optimizer | PASS |
| FIX-P01-STABLE-BOUNDARY | θ=(−1,−1,4,4) exact boundary; evaluation only | stable_eval_only_no_optimizer | PASS |
| FIX-P02-STABLE-INTERIOR | θ=(0.5,0.5,0.5,2) interior; evaluation only | stable_eval_only_no_optimizer | PASS |
| FIX-P02-STABLE-BOUNDARY-SMIN | θ=(0.5, s_side_min(2), s_side_min(2), 2); evaluation only | stable_eval_only_no_optimizer | PASS |
| FIX-P01-ZEROVAR-IN-DOMAIN | θ=(−1.0, 1.375, 40.0, k_max) in-domain; real generator → ε_model path | stable_eval_only_no_optimizer | PASS |
| FIX-NONFINITE-INPUT | fabricated 146-vector with one NaN at index 10 | fabricated_unit_check | PASS |
| FIX-INVALID-INIT | fabricated start (nan,0.5,20,20) fed to the initialization validator | validator_reject_no_optimizer | PASS |
| FIX-NONFINITE-PARAMETER | fabricated final endpoint (nan,0.5,20,20) presented post-fallback | fabricated_unit_check | PASS |
| FIX-NONFINITE-FIT | fabricated g_stable with one +inf at index 50 | fabricated_unit_check | PASS |
| FIX-P01-KURAL-S-FAIL | θ=(2.0,2.0,k_max,k_max) real generator evaluation known to fail Kural S | real_generator_classify_eval_only | PASS |
| FIX-OPTIMIZER-NONCONVERGENCE | fabricated OptimizeResult-like record success=False, finite x | fabricated_unit_check | PASS |
| FIX-OTHER-NUMERICAL-FAILURE | primary raises FAULT_INJECTION_TEST_ONLY; fabricated fallback stage ALSO returns non-finite x=(nan,nan,nan,nan) | orchestrated_primary_fault_fallback_nonfinite | PASS |
| FIX-FAMILY-FIT-FAILURE | fabricated 3-endpoint set, each with a distinct hard-failure predicate | aggregation_unit_all_ineligible | PASS |
| FIX-RESERVED-CODES-NEGATIVE | post-hoc scan of union of all emitted predicate/warning sets | post_hoc_negative_assertion | PASS |
| FIX-FALLBACK-FAULT-INJECTION | designated P-01 idx0 start; injected primary fault; REAL frozen SLSQP fallback on identical x0 | orchestrated_primary_fault_real_slsqp_fallback | PASS |
| FIX-AGG-UNIQUE-MIN | fabricated 3-endpoint set with unique eligible minimum | aggregation_unit_fabricated_records | PASS |
| FIX-AGG-TIE | fabricated set with two eligible endpoints tied within D-F2-09.9 | aggregation_unit_fabricated_records | PASS |
| FIX-AGG-LOWERL-INELIGIBLE | fabricated (L=0.001 ineligible, L=3.0 eligible) | aggregation_unit_fabricated_records | PASS |
| FIX-D0F209-MANIFEST-QC | full 819/731 + 351/261 lattice regeneration vs frozen CSV | grid_reconstruction_set_equality | PASS |

## 8. Evidence provenance (§4A) — write sites + falsifiability

Every flag defaults to `False` and is written only at its permitted site:

| flag | writing function / code site |
|---|---|
| `validator_called` | `validate_initialization` entry (first statement) |
| `primary_fault_injection_triggered` | `run_primary`, immediately before the tagged raise |
| `optimizer_called` | `run_primary` / `run_fallback`, immediately before the real `minimize()` call |
| `fallback_branch_entered` | `run_one_start` fallback dispatch site |
| `same_x0_reused` | `run_one_start` fallback dispatch site (computed by comparing the x0 passed onward against the original tuple) |
| `fallback_nonfinite_injection_triggered` | `run_fallback`, at the test-only injection |
| `executed_construction_key` | orchestration/executor exit, composed from observed flags/counters only |

No flag is assigned in a fixture definition, dispatch table, canonical-record assembly outside orchestration, or the report writer; none is conditioned on `fixture_id` or derived from manifest text. Evidence propagates upward in the `run_one_start` return value and is consumed read-only.

**§4A.4 falsifiability control — PASS.** Observed evidence of the already-executed benign start `FIX-P01-BENIGN grid[0]` (primary path succeeds): `primary_fault_injection_triggered=false`, `fallback_branch_entered=false`, `fallback_nonfinite_injection_triggered=false`, `validator_called=true`, `optimizer_called=true` — the same flags take both values across code paths, so the instrumentation is falsifiable.

## 9. A-01A — FIX-OTHER-NUMERICAL-FAILURE execution-path evidence

Routed through the real `run_one_start` orchestration with `fault_inject_primary=true, fault_inject_fallback_nonfinite=true` on the deterministic designated start (`ret01[0]`); no hard-coded canonical record exists for this fixture. Observed evidence (identical RUN1/RUN2):

```text
primary_fault_injection_triggered      = true    (raised and caught; telemetry row: EXCEPTION:RuntimeError:FAULT_INJECTION_TEST_ONLY)
fallback_branch_entered                = true
same_x0_reused                         = true
fallback_nonfinite_injection_triggered = true    (test-only _FabricatedFallbackResult, x=(nan,nan,nan,nan))
OTHER_PREDECLARED_NUMERICAL_FAILURE    = emitted by the real post-fallback non-finite handling branch
```

Observed predicate set for the terminal record (all logged simultaneously per D-F2-10): `{NONFINITE_PARAMETER, OTHER_PREDECLARED_NUMERICAL_FAILURE}` — the additional `NONFINITE_PARAMETER` arises correctly because the fabricated non-finite endpoint genuinely is a non-finite parameter tuple; r2's single-predicate hard-coded record was exactly the A-01 defect. The separate `FIX-FALLBACK-FAULT-INJECTION` (real SLSQP fallback) is preserved unchanged and not merged. Classification note: the endpoint is non-finite, so classification is family-independent (domain checks are skipped for non-finite tuples); the canonical record and telemetry carry the manifest family label `P-CMN`.

## 10. A-01B — FIX-INVALID-INIT validator-path evidence (+ §6.1 wiring)

`validate_initialization(theta, family, evidence)` implements ONLY the already-supported non-finite check (no broadened criterion) and is wired into `run_one_start` for **every** start, before any optimizer call. Fixture evidence (identical RUN1/RUN2):

```text
validator_called              = true
optimizer_called              = false
INVALID_INITIALIZATION        = emitted from the validator path
construction_fidelity_pass    = true
```

§6.1 equivalence evidence: `rejections_outside_FIX-INVALID-INIT = 0` (the validator fired for all 8 benign starts + both fault-injection starts and rejected none — behaviour-neutral as expected; the rejection counter contains exactly `["FIX-INVALID-INIT"]`). Per §6.1, r3-vs-r2 canonical hash equality is NOT claimed as equivalence evidence (r3 canonical output carries additional construction-audit fields by design); the zero-rejection count is the required evidence.

## 11. A-02 closure

Closed per §5 above: loud, unfiltered required-column check active before execution; verified passing on the frozen manifest.

## 12. A-03 closure

`internal_L(x_fixture, theta, family)` now computes the aggregation-bookkeeping objective for **every** terminal endpoint, eligible or not: stable generator → `zero_variance_rule` → if `OK`, `L = objective_L(x_fixture, ghat)` (standardized); otherwise `L = +inf`. The forbidden `objective_L(x, g_stable)` path does not exist in the r3 harness. Aggregation still filters `eligible == true` first, so no family-fit result changed. L is not written to telemetry.

## 13. A-04 closure (+ §9.1 real-classifier multi-predicate probe)

**C3 repaired (non-tautological):** `before = sorted(copy(input))`; `primary_display_code(input)` called; `after = sorted(input)`; required `after == before` AND `primary == NONFINITE_FIT`. Observed: `before == after == [MORPHOLOGY_INADMISSIBLE, NONFINITE_FIT]`, `primary = NONFINITE_FIT` — **PASS** (precedence neither deletes nor mutates predicates; display precedence changes admissibility = false).

**§9.1 real-classifier probe — PASS.** `classify_endpoint((-1.0, 1.375, 200.0, 200.0), "P-01")` observed verbatim: `predicates = [MORPHOLOGY_INADMISSIBLE, ZERO_VARIANCE_FIT]` (exactly the required set), `primary_display_code = ZERO_VARIANCE_FIT`, consistent with `primary_display_code(predicates)`. No classifier rule was adjusted. This probe is not a fixture, not in the 21-fixture set, not telemetered, and introduces no new threshold/class/claim.

## 14. Preservation of X1–X4 / C1–C5

X1 exact scientific support fully separate from the 1e-8 numerical tolerance (both adversarial self-tests re-PASS: P-01 order violation `V=5.0e-9` numerically tolerable yet `scientific_domain_pass=false`; P-02 s_min violation with `beta=sqrt(6)` exactly, `V≈5.0e-13` yet `scientific_domain_pass=false`); X3 family-status/summary schema preserved; X4 guard `585.0` preserved (the only `1.0e6` text in the file is the comment "historical 1.0e6 absent" on the guard-definition line — no code literal); C1 benign criterion PASS both families; C2 `beta=sqrt(6)` exact; C3 per §13; C4 no beta clamp (`v_p02` returns an infinite sentinel for nonfinite/≤0 beta); C5 telemetry = RUN1 only. Thread pins before NumPy/SciPy import; `RNG_USED=false`; D-F2-09 reconstruction 731/261 exact vs frozen CSV; mini-banks `{0,365,730}`/`{0,130,260}` + conditional feature (+1 valid-nonduplicate both); P-02 beta-dependent `NonlinearConstraint` pair; exact `trust-constr`/SLSQP options; reserved labels not emitted; D-F2-09.9 tie behavior verified.

## 15. Complete full-rerun results

Complete frozen 21-fixture suite rerun from scratch (no r2 PASS record reused, no r2 telemetry copied): P-01 benign — 4/4 starts structured, 3/4 eligible (`grid[730]` legitimately `MORPHOLOGY_INADMISSIBLE`), aggregation `OK`; P-02 benign — 4/4 structured, 4/4 eligible, aggregation `OK`; all stable-evaluation fixtures exception-free; `FIX-P01-ZEROVAR-IN-DOMAIN` → `ZERO_VARIANCE_FIT` (σ_g = 0.0); `FIX-P01-KURAL-S-FAIL` → `MORPHOLOGY_INADMISSIBLE`; all 8 STEP-2-emittable failure codes reached through their predeclared construction modes; fallback real-SLSQP fixture converged on the identical x0; all aggregation/tie fabricated cases correct; `FIX-D0F209-MANIFEST-QC` PASS; reserved-code negative assertion `CONFIRMED_ABSENT`. No family-performance or adequacy interpretation is made.

## 16. R3-01..R3-42 table

| check | result | check | result |
|---|---|---|---|
| R3-01 root/branch/HEAD | PASS | R3-22 X1 semantics preserved | PASS |
| R3-02 governing hashes exact | PASS | R3-23 X3 schema preserved | PASS |
| R3-03 r2 artifacts unchanged | PASS | R3-24 X4=585.0; no 1.0e6 literal | PASS |
| R3-04 manifest pre/post identical | PASS | R3-25 C1 P-01 PASS | PASS |
| R3-05 required columns present | PASS | R3-26 C1 P-02 PASS | PASS |
| R3-06 21==21==21 IDs | PASS | R3-27 731/261 exact | PASS |
| R3-07 class/family fidelity | PASS | R3-28 real-SLSQP fallback fixture PASS | PASS |
| R3-08 exact_construction loaded ×21 | PASS | R3-29 8/8 codes via predeclared modes | PASS |
| R3-09 fidelity 21/21 | PASS | R3-30 reserved labels non-emittable | PASS |
| R3-10 primary fault triggered | PASS | R3-31 aggregation+tie preserved | PASS |
| R3-11 fallback branch entered | PASS | R3-32 RUN1==RUN2 exact | PASS |
| R3-12 same x0 reused | PASS | R3-33 telemetry firewall; RUN1 | PASS |
| R3-13 fallback nonfinite injection exercised | PASS | R3-34 no literal tuned | PASS |
| R3-14 OTHER_… emitted by real branch | PASS | R3-35 firewall preserved | PASS |
| R3-15 no hard-coded record for FIX-OTHER | PASS | R3-36 no upstream modified | PASS |
| R3-16 validator actually called | PASS | R3-37 §4A write-site provenance | PASS |
| R3-17 optimizer not called (invalid init) | PASS | R3-38 §4A.4 falsifiability | PASS |
| R3-18 INVALID_INITIALIZATION from validator path | PASS | R3-39 validator every start; 0 outside rejections | PASS |
| R3-19 no silenced column absence | PASS | R3-40 21-row mapping table, human-audited label | PASS |
| R3-20 no unstandardized-L path remains | PASS | R3-41 §9.1 probe exact match | PASS |
| R3-21 C3 before/after mutation test | PASS | R3-42 telemetry 12 rows, reconciled vs 10 | PASS |

All 42 PASS. No STOP condition arose.

## 17. Determinism hashes

```text
RUN1 canonical SHA256 = 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403
RUN2 canonical SHA256 = 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403   (IDENTICAL)
```

Canonical document includes all r2 fields plus `scientific_domain_pass`, exact Kural-T/S flags, `family_status`/`family_summary`, the 21-entry construction audit (with manifest prose verbatim), the special-evidence dicts for FIX-OTHER-NUMERICAL-FAILURE / FIX-INVALID-INIT / FIX-FALLBACK-FAULT-INJECTION, the falsifiability record, and the outside-rejection list. All fields originate under §4A rules. Runtime excluded; exact string equality required and achieved; no new closeness tolerance.

## 18. Telemetry firewall (§13.1)

```text
telemetry_run                  = RUN1
expected_r3_telemetry_row_count = 12
actual_r3_telemetry_row_count   = 12
```

Row-by-row reconciliation vs r2 (10 rows): the 8 benign-fixture primary rows and the 2 FIX-FALLBACK-FAULT-INJECTION rows are structurally identical to r2's 10; the **+2 new rows** are `FIX-OTHER-NUMERICAL-FAILURE` primary (`EXCEPTION:RuntimeError:FAULT_INJECTION_TEST_ONLY`) and its fabricated fallback row — exactly the rows the real-orchestration correction mandates. Fabricated-fallback synthetic-field declaration (test-only values, not optimizer measurements): `optimizer_path=fallback`, `status=-1`, `success=False`, `message=FABRICATED_FALLBACK:FAULT_INJECTION_TEST_ONLY:nonfinite_return`, `nit/nfev/njev=-1`, `wall_clock_seconds=nan`. Columns unchanged; no `L`/`rho`/recovery/aggregate columns; no cross-family ranking.

## 19. Firewall / gate state

```text
real_SSA_fit = false | real_SSA_subset_fit = false
parameter_recovery_analysis = false | objective_attainment_analysis = false
generator_adequacy_comparison = false | generator_selection = false
P03_touched = false | P04_touched = false | P05_touched = false
algorithm_CVI_execution = false | algorithm_CVI_outcome_access = false
legacy_performance_content_access = false | results_directory_opened = false
F3_started = false | F4_started = false | rng_used = false | commit = false

A01_closed = true | A02_closed = true | A03_closed = true | A04_closed = true
R3P01_evidence_provenance_verified = true
R3P02_validator_wired_to_real_path = true
R3P03_construction_mapping_disclosed = true
R3P04_multipredicate_selftest_pass = true
R3P05_telemetry_synthesis_disclosed = true
X1_closed = true | X2_closed = true | X3_closed = true | X4_closed = true | C1_C5_closed = true

F2_STEP_2_r3_corrected_rerun = PASS
F2_complete = false
F3_allowed = false
STEP3_started = false

next_action = independent audit of r3 STEP-2 successor artifacts
```

No scientific adequacy is claimed; the manifest prose was not machine-verified (§7 note).

## 20. Successor file hashes

```text
f2_step2_feasibility_harness_r3_2026-09-01.py    = 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077
f2_step2_feasibility_telemetry_r3_2026-09-01.csv = cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49
```

(This report's own hash is given in the end-of-task response; no self-hash, no sidecar.)

## 21. Final git status

Recorded in the end-of-task response after this report is written (three new untracked r3 artifacts added to the existing F2-era set). Nothing staged, nothing committed.

## 22. Verdict

```text
ART_F2_STEP2_R3_FEASIBILITY_READY_FOR_INDEPENDENT_AUDIT
```
