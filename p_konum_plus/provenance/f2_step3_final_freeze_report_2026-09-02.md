# p_konum_plus — F2 STEP-3 Final Freeze — Provenance Report

## 1. Artifact role

- **Report type:** F2 STEP-3 Final Freeze execution provenance (static document/hash audit + accepted-lineage consolidation + gate transition preparation). NO new methodology, NO STEP-2 rerun, NO real SSA, NO F3 execution, NO commit.
- **Status:** NON-NORMATIVE
- **Date:** 2026-09-02 · **Worktree:** `G:/PycharmProjects/pkp-worktree` · **Branch:** `p_konum_plus` · **HEAD:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`
- **Write-order note (governing prompt §7):** this report is written BEFORE the FINAL FREEZE record; therefore `final_freeze_file_write_pending = true` and this report deliberately contains no final-freeze hash (that hash appears only in the end-of-task response).

## 2. Repository precheck — PASS

Root ✓, branch `p_konum_plus` ✓, HEAD = expected `3e4daf47018f124e29717263e4e45fe90c8e52b8` ✓, zero unexpected tracked modifications; 26 known F2-era untracked files recorded pre-task; both STEP-3 target paths verified absent before any write.

## 3. Governing/frozen hash verification — all 17 exact

| artifact | SHA256 | result |
|---|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | PASS |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` | PASS |
| ART-F2 r2a | `2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2` | PASS |
| ART-F2 r2 | `d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4` | PASS |
| D-F2-09 exact packet | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` | PASS |
| D-F2-09 fixed-grid manifest | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` | PASS |
| STEP-2 fixture manifest | `daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b` | PASS |
| historical STEP-2 harness | `45b426447803ceb0cf6c029393ca606d89a5fb006d5ab34ce4b43ca4160f86db` | PASS |
| historical STEP-2 telemetry | `144a3b09776e05dff3c490725fda1bc17b07bd759a48033be338778889fa62f6` | PASS |
| historical STEP-2 report | `9850075ea011fc0cad6740353abe138f6ed01acb2763803e72e5af5fe56a6d83` | PASS |
| r2 successor harness | `3b2555508e4b731ab3349a040a03a3d266fe068d72cd13427107a998622610bc` | PASS |
| r2 successor telemetry | `d688a16bfd131ee1e1cfe8715a011009b782a78a1ac897c5589cc68af3b8dabb` | PASS |
| r2 successor report | `9d5bf074b099cf597009218a0c16cdba68dabcdd00ee4313165c7c59c165b445` | PASS |
| r3 successor harness | `01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077` | PASS |
| r3 successor telemetry | `cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49` | PASS |
| r3 successor report | `afd02531cf80fa441ad2d6e3b990583783963fc6042b87c98f0108af0629abf5` | PASS |
| r3 independent audit (custody) | `f4f2cc2702efdc1e6b0eb0804c847e93420e439c2425961810304eefb9b3048c` | PASS |

No upstream artifact was rewritten; no STOP.

## 4. F2F-00 — independent r3 audit verification — PASS

`p_konum_plus/provenance/f2_step2_r3_independent_audit_2026-09-02.md` (hash exact above) identifies the exact three r3 artifact hashes of §5 below and states verbatim: `GLOBAL_BLOCKER = none`, `GATE_SPECIFIC_BLOCKER = none`, `F2_STEP_2_r3 = ACCEPTED`, `STEP3_allowed = true` (with `F2_complete = false`, `F3_allowed = false`, `F3_started = false`). It independently addresses every required item: A-01/R3-P01 evidence provenance (incl. the falsifiable benign negative control), the FIX-OTHER-NUMERICAL-FAILURE real orchestration path, the FIX-INVALID-INIT real validator path (zero outside rejections), the R3-P03 human-audited prose→key distinction, A-02, A-03, A-04/R3-P04 (exact multi-predicate probe result), R3-P05 telemetry semantics (12 rows, synthetic fields), X1–X4/C1–C5 preservation, firewall, and determinism scope (same-process only; independent replay recorded as supporting informational evidence). It records one nonblocking cleanup (CL-R3-01, wording only) and one informational note. Acceptance is taken from this audit, not inferred from the r3 execution report alone.

## 5. Accepted r3 artifact hashes

```text
f2_step2_feasibility_harness_r3_2026-09-01.py    = 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077
f2_step2_feasibility_telemetry_r3_2026-09-01.csv = cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49
f2_step2_synthetic_analytic_feasibility_report_r3_2026-09-01.md = afd02531cf80fa441ad2d6e3b990583783963fc6042b87c98f0108af0629abf5
```

The r3 report supports: A01–A04 closed; R3-P01..P05 closed; X1–X4/C1–C5 closed; R3-01..R3-42 all PASS; telemetry 12/12; RUN1 = RUN2 canonical SHA256 `6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403`; `F2_STEP_2_r3_corrected_rerun = PASS` with `F2_complete=false`, `F3_allowed=false`.

## 6. Authority / v11 precedence

The FINAL FREEZE artifact to be written is `F2_FINAL_FROZEN_OPERATIONAL_SPEC` with `normative_authority = none`; v11 remains the sole normative methodology source (`v11_wins = true`). It consolidates already-ratified science, accepted CLASS_C pins, accepted r3 operational corrections, and lineage — it changes nothing.

## 7. Scientific-content non-reopening confirmation

No item in the forbidden list was touched: v11 methodology, P-01/P-02 formulas, D-F2-08, D-F2-09.1..09.10, parameter bounds, Kural T/S, `epsilon_model=1e-12`, `feasibility_acceptance_tol=1e-8`, optimizer options, start rules, tie rule, and all scientific thresholds are frozen BY REFERENCE to ART-F2 r2/r2a and the ratified D-F2-09 packet — unchanged, not rederived, not rewritten.

## 8. A-01/A-02/A-03/A-04 + R3-P01..P05 closure lineage

A-01 (construction fidelity 21/21, real orchestration for FIX-OTHER-NUMERICAL-FAILURE, real validator path for FIX-INVALID-INIT) — closed in r3, independently accepted. A-02 (loud required-column check) — closed. A-03 (standardized-only internal L; `objective_L(x, unstandardized_g)` absent) — closed. A-04 (non-tautological C3 + R3-P04 real-classifier probe `{MORPHOLOGY_INADMISSIBLE, ZERO_VARIANCE_FIT}` / `ZERO_VARIANCE_FIT`) — closed. R3-P01 (evidence flags observed at real write sites; falsifiability control PASS), R3-P02 (validator wired to every start; 0 outside rejections), R3-P03 (human-audited mapping disclosed), R3-P04, R3-P05 (12-row telemetry with declared synthetic fallback fields) — all closed. The freeze will adopt the CL-R3-01 binding wording (below), not the superseded phrase.

## 9. X1–X4 / C1–C5 consolidation

X1 numerical-vs-scientific separation; X2 registry/manifest fidelity; X3 predicates/rejection/family-status/summary schema; X4 guard 585.0 (= 4·T+1 > 4·T = 584 = max valid standardized LS, since L = 2T(1−ρ), ρ ≥ −1); C1 benign execution criterion; C2 β=√6 adversarial check; C3 display precedence; C4 no beta clamp; C5 RUN1 telemetry / RUN2 determinism role — all preserved through r3 and independently accepted; frozen as accepted operational corrections in the FINAL FREEZE.

## 10. Telemetry 12-row provenance

r3 telemetry = exactly 12 data rows: 8 benign primary rows + 2 FIX-OTHER-NUMERICAL-FAILURE rows (the real-orchestration correction footprint) + 2 FIX-FALLBACK-FAULT-INJECTION rows. The fabricated-fallback optimizer-result-like fields are TEST-ONLY SYNTHETIC values, declared and tagged, not optimizer measurements. Telemetry firewall intact (no L/ρ/recovery/family-performance fields).

## 11. Determinism scope

Frozen exactly as: exact semantic double-run determinism within the same process, same thread-pinned environment, same code, same inputs, same configuration (RUN1 = RUN2 = `6f197b74…`). Cross-process bitwise determinism: not tested in F2 STEP 2, not claimed. Cross-platform bitwise optimizer reproducibility: not claimed. The independent replay is supporting informational evidence only and does not broaden this claim.

## 12. CL-F2-01/02/03 + CL-R3-01 cleanup status

CL-F2-01: already cleaned in r3 (actual-start-count C1 expression); `new_harness_cycle = false`. CL-F2-02: `fixture_manifest_execution_mode_column = absent`; execution-mode representation = harness-internal provenance label; `scientific_effect = none`; manifest untouched. CL-F2-03: omitted — the accepted r3 artifacts record feature-start validity/dedup outcomes only; no feature-start identity claim beyond that is supported, so none is recorded. CL-R3-01: the freeze adopts the exact binding wording — "For the A-01 execution-path fixtures, executed_construction_key is deterministically derived in the audit/executor layer from evidence returned by the real run_one_start orchestration; the underlying evidence flags themselves are written only at their real execution sites." — replacing the overstrong "composed at orchestration exit" phrase (cleanup only; `scientific_change = false`, `execution_change = false`, `new_harness_cycle = false`).

## 13. P-CMN.10 normalization

Normalized in the FINAL FREEZE only (r2a not rewritten): `P-CMN.10` — component = reserved `BOUNDARY_PATHOLOGY`/`IDENTIFIABILITY_FAILURE` + WARN trigger behavior; `status = CLASS_C_IMPLEMENTATION_PIN` (single-valued); `behavior = RESERVED_NOT_EMITTED_IN_STEP2`; `scientific_change = false`, `execution_change = false`, `PI_re_ratification = false`.

## 14. Firewall confirmation

```text
STEP2_rerun = false | trust_constr_executed = false | SLSQP_executed = false
new_fixture = false | fixture_manifest_edited = false
real_SSA_fit = false | real_SSA_subset_fit = false
generator_adequacy_evaluation = false | generator_comparison = false | generator_selection = false
parameter_recovery = false | objective_attainment_analysis = false
P03_work = false | P04_work = false | P05_work = false | F3_execution = false
algorithm_CVI_execution = false | algorithm_CVI_outcome_access = false
legacy_performance_content_access = false | results_directory_opened = false
new_scientific_decision = false | new_numerical_threshold = false
new_optimizer_literal = false | new_objective = false | new_start_rule = false | new_tie_rule = false
commit = false
```

## 15. Final gate-transition readiness

Entry state verified: F0 COMPLETE, F1 COMPLETE, F2 STEP-1 COMPLETE, STEP-1.5 COMPLETE, STEP-2 r3 execution PASS + independent audit PASS ⇒ STEP-2 ACCEPTED; no open global or gate-specific blocker. All F2F prerequisite checks preceding the freeze write PASS (full table in the end-of-task response). The gate transition (`F2_complete = true`, `F3_allowed = true`) is therefore authorized and will be recorded exclusively in the FINAL FREEZE artifact written after this report. `F3_allowed` means permission to begin a separately governed F3 task; no F3 execution occurs in STEP-3.

## 16. Files to be created (in order)

1. This report (`p_konum_plus/provenance/f2_step3_final_freeze_report_2026-09-02.md`) — written first.
2. `p_konum_plus/calibration/f2_generator_specification_record_FINAL_FREEZE_2026-09-02.md` — written last, only after this report's write is verified.

```text
final_freeze_file_write_pending = true
```

## 17. Git status before final freeze write

26 known F2-era untracked files at precheck (nothing staged/committed); this report adds one more untracked path. The full final listing is captured in the end-of-task response after both writes.

## 18. Verdict (report-stage)

All prerequisite F2F checks preceding the freeze write are PASS; proceeding to write the FINAL FREEZE record as the last project artifact of this task. Expected task verdict: `ART_F2_FINAL_FREEZE_COMPLETE_F3_ALLOWED`.
