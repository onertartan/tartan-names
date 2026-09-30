# p_konum_plus — ART-F2 r1 -> r2 Correction + PI Ratification — STEP 1 Report

- **Report type:** F2 STEP 1 execution report (create ART-F2 r2, apply PI-ratified decision set, apply C1–C10 + R1–R4, close the exact CLASS_C optimizer/coupled-constraint contract). NO STEP 2, NO synthetic feasibility, NO real SSA fit, NO F3, NO commit.
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-31
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `3e4daf47018f124e29717263e4e45fe90c8e52b8`

---

## 1. Repository / precheck result — PASS

Root `G:/PycharmProjects/pkp-worktree` ✓, branch `p_konum_plus` ✓, HEAD = expected `3e4daf47018f124e29717263e4e45fe90c8e52b8` ✓. Zero unexpected tracked modifications; only the eight known F2-era untracked artifacts present at precheck (list below). Both STEP-1 target output paths (`f2_generator_specification_record_r2_2026-08-31.md`, `f2_r2_correction_ratification_report_2026-08-31.md`) and the `provenance/nonnormative/` directory were verified absent before creation — no overwrite occurred. Nothing deleted/reset/stashed/checked out.

Untracked list before STEP-1 outputs:

```text
?? p_konum_plus/calibration/f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md
?? p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv
?? p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md
?? p_konum_plus/provenance/f2_d09_exact_enumeration_packet_2026-08-30.md
?? p_konum_plus/provenance/f2_d09_packet_endoftask_report_2026-08-30.md
?? p_konum_plus/provenance/f2_owner_decision_packet_report_2026-08-29.md
?? p_konum_plus/provenance/f2_reconciliation_source_check_report_2026-08-29.md
?? p_konum_plus/provenance/f2_worksheet_updated3_verification_report_2026-08-29.md
```

## 2. All governing hashes — exact (recomputed this task)

| document | SHA256 | result |
|---|---|---|
| v11 FINAL NORMATIVE | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | PASS |
| v0 execution protocol | `b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280` | PASS |
| ART-F2 r1 | `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7` | PASS |
| PI ratification-ready worksheet FINAL_v2 | `803e9f30fa84b6c02c34a517525e6c246edf7be4db684e72a2ea8c970f9b38f5` | PASS |
| D-F2-09 exact packet | `8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6` | PASS |
| D-F2-09 proposed start-grid manifest | `c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666` | PASS |
| ART-F0 | `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8` | PASS |
| ART-F1 r4a (FINAL) | `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0` | PASS |
| F1 eligible manifest | `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32` | PASS |
| F1 input hash table | `aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac` | PASS |
| R1 source 1 (chatgpt v11 sentez) | `3bd9e7cfdbdfe9358f91792db12447594d86956cd1c1b185552cb2da4d94b787` | PASS (source and repo copy both verified) |
| R1 source 2 (Claude v10→v11 TERMINAL) | `29c073ba5105a14299a0ea9427d8443c1a29d40960f7fed355ef49b2bae67c5a` | PASS (source and repo copy both verified) |

No mismatch; no file normalized or repaired.

## 3. Explicit PI-ratification check — PASS

The chat-turn statement dated 2026-08-31 was verified equivalent to the required form (worksheet §5): it names the FINAL_v2 worksheet, ratifies D-F2-01 through D-F2-12, states the D-F2-09.1–.7 (PI-owned) / D-F2-09.8–.9 (CLASS_C) / D-F2-09.10 (DERIVED) classification, invokes R1–R4, authorizes ART-F2 r1 → r2 correction/ratification, and states the STEP-2 gating condition (r2 optimizer/coupled-constraint CLASS_C contract must be exact and executable before STEP 2). Attachment of the worksheet was not treated as approval by itself — the explicit ratification sentence was required and present. `PI_ratification = true` is recorded in ART-F2 r2 §0.

## 4. ART-F2 r2 path + SHA256

```text
path   = p_konum_plus/calibration/f2_generator_specification_record_r2_2026-08-31.md
SHA256 = d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4
```

r1 was not overwritten; it remains at `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7` (re-verified unchanged).

## 5. Exact optimizer/coupled-constraint CLASS_C contract — summary (ART-F2 r2 §9)

Chose **Option B — exact constrained-optimizer formulation**, not a smooth reparameterization, specifically because a large share of the ratified D-F2-09 lattice sits exactly on domain faces (`c_r=c_d`, `c_r=-1`/`c_d=2`, `k=k_min`/`k_max`, `m=-1`/`2`, `beta=1`/`6`, `s=s_side_min(beta)`/`3`); a scaled-logit transform would map such boundary values to `±infinity`, making ratified starts unrepresentable exactly. Under Option B, start conversion is the **identity map** — no forward/inverse mapping or boundary proof is needed.

- **P-01:** `Bounds` on `(c_r,c_d,k_r,k_d)` at `[-1,2]×[-1,2]×[k_min,k_max]×[k_min,k_max]`, plus a native `LinearConstraint` `c_d - c_r >= 0` (boundary-inclusive; `c_r=c_d` feasible, not merely a limit).
- **P-02:** loose box `Bounds` (`m∈[-1,2]`, `beta∈[1,6]`, `s_l,s_r∈[s_side_min(1), 3]` using the global minimum of `s_side_min` over `beta∈[1,6]` as a valid coarse region) **plus** two native `NonlinearConstraint`s carrying the exact scientific bound: `s_l - s_side_min(beta) >= 0`, `s_r - s_side_min(beta) >= 0` — because `s_side_min(beta)` is nonlinear in `beta`, a static box alone is insufficient (explicitly required by the correction prompt §8).
- **Optimizer:** primary `scipy.optimize.minimize(method='trust-constr')` (`jac='2-point'`, `hess=BFGS()`, `gtol=1e-10`, `xtol=1e-12`, `barrier_tol=1e-10`, `constr_viol_tol=1e-8`, `maxiter=500`); fallback `method='SLSQP'` (`ftol=1e-12`, `maxiter=500`) with equivalent inequality-constraint dicts, reusing the **same** deterministic start bank — no new retry starts, no RNG.
- **Success/nonconvergence/error criteria** defined without assuming shared `ftol`/`gtol` semantics: success = `OptimizeResult.success` + finite parameters + `constr_viol_tol` satisfied + finite objective; nonconvergence (e.g. `maxiter` hit, `success=False`, no exception) → `OPTIMIZER_NONCONVERGENCE`, logged, no fallback, next start tried; a genuine numerical error (exception or non-finite optimizer output) on a specific start → fallback on that same start; if the fallback also fails → `OTHER_PREDECLARED_NUMERICAL_FAILURE` for that start only, proceeding to the next start.
- **Non-alteration statement:** every bound/constraint above is exactly the ratified D-F2-06/07 domain; the post-hoc D-F2-10 admissibility re-check (Kural T/S, finiteness, zero-variance) applies uniformly to any produced solution regardless of optimizer path, so this CLASS_C design changes no scientific parameter support, morphology admissibility, or fit exclusion — **no STOP triggered**.

## 6. D-F2-09 classification

```text
09.1..09.7  = PI-owned initialization reproducibility contract
09.8..09.9  = CLASS_C implementation pins (dedup/order; objective-tie comparator)
09.10       = DERIVED_FROM_RATIFIED_RULE (P-01 = 731, P-02 = 261, feature +1/+0)
```

## 7. C1–C10 status — all APPLIED

C1 revision lineage (r2 tag + r1 parent hash) · C2 search auditability (scope, opened-vs-pattern-search split, zero-hit paths) · C3 literature provenance (Wikipedia = orientation-only, not naming provenance) · C4 underflow correction (raw underflow ≠ `ZERO_VARIANCE_FIT`, applied in §5/§6/§10 of r2) · C5 P-02 `s_max` rationale corrected (z-space saturation/weak-identifiability, not "zero-variance") · C6 initialization/retry made exact, `rng_used=false`, no second retry bank · C7 pin schema `P-01.x`/`P-02.x`/`P-CMN.x` with single-valued status; v0 §26 inventory (32) unchanged · C8 decision register: "dual historical labels" replaced by opaque-identifier semantics; D-F2-11/12 formally recorded · C9 `next_action` scrubbed of frozen-trajectory feasibility language; explicit STEP-2 precondition (predeclare `epsilon_model` etc.) added · C10 downstream residual-interface note labeled NON-BINDING.

## 8. R1–R4 status — all APPLIED

**R1:** both reconciliation sources copied byte-exact into `p_konum_plus/provenance/nonnormative/`; source and repository-copy hashes verified identical both before and after copy (`3bd9e7cf…`, `29c073ba…`); `copy_only=true`, `normalize=false`, `delete_original=false`; full custody record (ledger/actual filenames, original path, repo copy path, hash, copy date) in ART-F2 r2 §17. **R2:** reconciliation-check findings recorded in ART-F2 r2 §2.2 — available_and_verified, no math definitions, no acronym expansions, no TAD-vs-PSAT relation, no formula contradiction. **R3:** pre-v11 tie-break/cross-fit text in the custodied sources marked `methodology_authority=none`, `superseded_by=v11`, `P04_derivation_use=prohibited`, `P05_derivation_use=prohibited`, `F3_scientific_evidence_use=prohibited`. **R4:** three mechanical derivations recorded with parent decision, formula, inputs, rounding policy, and value — `k_max=127.43902548550072`, `s_side_min(beta)` (function, example values shown), and D-F2-09.10 counts (731/261); none re-decided, none rounded on implementation bounds.

**D-F2-09 manifest wording (§15A compliance):** this report and ART-F2 r2 state only that the D-F2-09 task recorded deterministic double-run reproduction; no claim is made that all 1,170 manifest rows were independently recomputed in this STEP-1 pass.

## 9. Exact files created/copied

**Created:**
- `p_konum_plus/calibration/f2_generator_specification_record_r2_2026-08-31.md`
- `p_konum_plus/provenance/f2_r2_correction_ratification_report_2026-08-31.md` (this file)

**Copied (R1 custody, byte-exact):**
- `p_konum_plus/provenance/nonnormative/ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md`
- `p_konum_plus/provenance/nonnormative/claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md`

ART-F2 r1 was not modified (hash re-verified unchanged). No other file touched.

## 10. Provenance report path + SHA256

```text
path = p_konum_plus/provenance/f2_r2_correction_ratification_report_2026-08-31.md
```

(Its own SHA256 is reported in the end-of-task response, computed after this file is written — a file cannot contain its own hash. No sidecar is created.)

## 11. Confirmation

```text
real_SSA_fit = false
F2_STEP_2    = false
F2_complete  = false
F3_allowed   = false
```

Also: no algorithm/CVI execution or outcome access, no legacy performance content access, no P-03/P-04/P-05 touched, no generator selected, no F3/F4 started, no `results/` opened, `rng_used = false` throughout.

## 12. Final `git status --short --untracked-files=all`

Recorded in the end-of-task response after this report is written (five new untracked paths added: ART-F2 r2, this report, and the two R1 custody copies plus the new `provenance/nonnormative/` directory entries).

## 13. Verdict

```text
ART_F2_R2_RATIFICATION_READY_FOR_INDEPENDENT_AUDIT
```

End state: `ART_F2_r2_created = true`, `PI_ratification_recorded = true`, `F2_STEP_1_complete = true`; `F2_STEP_2 = false`, `F2_complete = false`, `F3_allowed = false`. Next action: independent audit of ART-F2 r2. STEP 2 may begin only after that audit passes and the STEP-2 precondition (predeclaration of `epsilon_model` and any remaining runtime CLASS_C literal) is satisfied.
