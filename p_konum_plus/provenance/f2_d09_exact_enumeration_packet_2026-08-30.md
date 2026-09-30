# p_konum_plus — D-F2-09 Exact Deterministic Initialization/Multistart Enumeration Packet

- **Type:** NON-NORMATIVE PI decision-support packet (the D-F2-09 pre-ratification deliverable required by the MERGED worksheet)
- **Status:** DRAFT_OWNER_DECISION_PACKET — nothing here is ratified; the PI ratifies the *enumeration rules*; all counts are DERIVED
- **Date:** 2026-08-30
- **Worktree/branch/HEAD:** `G:/PycharmProjects/pkp-worktree` · `p_konum_plus` · `3e4daf47018f124e29717263e4e45fe90c8e52b8`
- **Trigger:** `Nihai_D-F2-01_12_PI_Karar_Calisma_Sayfasi_MERGED_FINAL_RECOMMENDATION_2026-08-30.md` — SHA256 `7f61eab892e7b85d9437777ffd578a04a905bb84d01103b1bfd8a6e1d94c0f0d` (explicitly NOT PI ratification)
- **Subject artifact:** ART-F2 r1 — SHA256 verified exact `d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7`

**Conditionality (binding):** every numeric filter below uses the worksheet's
RECOMMENDED — not yet ratified — pin set: location horizon `[-1, 2]`,
`k_min = 4`, Kural T primitive `w_min_years = 5` (hence
`k_max = 2*ln(9)*145/5 = 127.43902548550072`, exact continuous, repr-identical
to the worksheet's value), `s_max = 3.0`, `beta in [1, 6]`,
`s_side_min(beta) = (5/145)/(ln(10)^(1/beta) - ln(10/9)^(1/beta))`, Kural S
`n_min = 3`. If the PI changes any pin, the SAME enumeration rules re-derive
all sets and counts mechanically (`DERIVED_FROM_RATIFIED_RULE`, R4). Nothing
in this packet touched real data: all screening is model-only geometry of
start curves under stabilized evaluation.

```text
rng_used = false
CRN_namespace_use = false
algorithm_CVI_information = forbidden (none used)
governance_order = exact enumeration rule -> deterministic filtering against
                   recommended bounds + Kural T + Kural S -> deterministic
                   deduplication -> derived exact start count -> PI ratification
```

---

## Item 1 — Exact P-01 location anchor set on [-1, 2]

```text
A_loc = { -0.50, -0.25, 0.10, 0.30, 0.50, 0.70, 0.90, 1.25, 1.50 }   (9 anchors, exact literals)
```

Covers out-of-window latitude on both sides plus interior support; identical
set reused for P-02 (Item 4) to keep censored-start coverage symmetric.

## Item 2 — Exact P-01 ordered (c_r, c_d) pair enumeration

All ordered pairs `(c_r, c_d) = (A_i, A_j)` with `i <= j` (equal-location
pairs included as zero-plateau starts): **45 ordered pairs**.

## Item 3 — Exact P-01 k-base levels / asymmetry mapping

```text
k_base in { 6, 24, 96 }        c in { 0.5, 1, 2 }
(k_r, k_d) = (k_base * c, k_base / c)     # asymmetry ratio k_r/k_d in {1/4, 1, 4};
                                          # geometric mean preserved = k_base
```

9 raw combos per pair; after the bound filter `[4, 127.43902548550072]` the
surviving combos are exactly
`(6,6), (12,48), (24,24), (48,12), (96,96)` (5 combos — mechanical result).

## Item 4 — Exact P-02 m anchor set on [-1, 2]

Same `A_loc` as Item 1 (9 anchors).

## Item 5 — Exact P-02 beta anchor set

```text
beta_anchors = { 1.0, 2.0, 4.0 }
```

(Interior to the recommended `[1, 6]`; the `beta = 6` face is covered by a
boundary start, Item 9.)

## Item 6 — Exact P-02 s-base levels / asymmetry mapping

```text
s_base in { 0.05, 0.15, 0.45 }     c in { 0.5, 1, 2 }
(s_l, s_r) = (s_base * c, s_base / c)
```

Each side independently filtered against `[s_side_min(beta), 3.0]` with
`s_side_min(1) = 0.01569377976942823`, `s_side_min(2) = 0.028908255824181925`,
`s_side_min(4) = 0.05208022981671413` (exact-formula evaluation at the
optimizer's beta is the implementation rule; tabulated values are QC only).

## Item 7 — Exact feature-based start construction (per trajectory)

```text
j* = smallest index j attaining max_j x_j        (deterministic tie rule)
u* = j* / 145
P-01 feature start: (c_r, c_d, k_r, k_d) = (u* - 0.10, u* + 0.10, 24, 24)
P-02 feature start: (m, s_l, s_r, beta)  = (u*, 0.15, 0.15, 2.0)
```

Subject to the same filters as all starts. Under the recommended pins these
are always in-bounds (`u* in [0,1]`) and Kural-S-passing (verified on a demo
curve). If a future pin change ever places a feature start out of bounds, the
rule is deterministic nearest-bound projection, logged. Contributes **+1
start per family per trajectory**, outside the fixed-grid counts.

## Item 8 — Exact duplicate-start rule

After filtering: exact 4-tuple equality deduplication (tuples are constructed
from exact literals, so equality is exact); canonical ordering = ascending
lexicographic sort of the raw parameter tuple.

## Item 9 — Exact boundary-start policy

```text
B-P01 = { (-1.0, 0.5, 24, 24), (0.5, 2.0, 24, 24), (-1.0, 2.0, 24, 24),
          (0.5, 0.5, 4, 4), (0.5, 0.5, 127.43902548550072, 127.43902548550072) }
B-P02 = { (-1.0, 0.45, 0.45, 2), (2.0, 0.45, 0.45, 2), (0.5, 3.0, 3.0, 2),
          (0.5, 0.15, 0.15, 1), (0.5, 0.15, 0.15, 6) }
```

Face-representative starts (location faces, steepness/scale faces, beta
faces); degenerate corners are deliberately excluded (known
`ZERO_VARIANCE_FIT` territory). Subject to the same filters — under the
recommended pins all 10 survive (mechanical result).

## Item 10 — Exact retry policy

Triggered per trajectory per family ONLY if every primary start ends in a
hard failure. One deterministic retry round:

```text
P-01: (c_r + 0.05, c_d + 0.05, 1.5*k_r, 1.5*k_d)  applied to every primary start
P-02: (m + 0.05, 1.5*s_l, 1.5*s_r, beta)          applied to every primary start
```

Retry candidates pass the identical filter chain (bounds + Kural T + Kural S)
and are deduplicated against the primary set. After retry exhaustion:
`FAMILY_FIT_FAILURE(code)` with full logging. No further rounds; no RNG.

## Item 11 — Exact objective-tie tolerance

```text
tie iff |L_a - L_b| <= 1e-10        (CLASS_C predeclared literal)
```

## Item 12 — Exact lexicographic parameter order (tie resolution)

Lowest objective wins; within a tie (Item 11), ascending lexicographic
comparison of the RAW parameter tuple decides — order
`(c_r, c_d, k_r, k_d)` for P-01 and `(m, s_l, s_r, beta)` for P-02; first
differing component decides; the smaller tuple wins.

## Item 13 — Exact CLASS_C fallback-optimizer contract

```text
primary_optimizer   = bounded local optimizer, candidate L-BFGS-B
fallback_optimizer  = one predeclared alternative, candidate trust-constr
tolerances (CLASS_C predeclared literals): gtol = 1e-10, ftol = 1e-12, maxiter = 500
fallback trigger    = purely numerical optimizer error on a start (not fit quality)
constraints         = via the bijective transforms of ART-F2 §11.2 (log / ordered / scaled-logit)
determinism         = required; optimizer choice cannot alter family, objective, or bounds
```

If any of these class-C literals ever changes which fits are admissible, it
stops being class-C and returns to the PI (worksheet D-F2-10.6 rule).

## Item 14 — Derived exact start counts (mechanical; determinism re-run identical)

| stage | P-01 | P-02 |
|---|---|---|
| raw enumeration | 405 (45 pairs × 9 k-combos) | 243 (9 m × 3 s_base × 3 c × 3 beta) |
| after bounds + Kural T | 225 | 198 |
| after Kural S (n_sup ≥ 3, stabilized) | 219 | 178 |
| after dedup | 219 | 178 |
| boundary starts surviving | +5 (of 5) | +5 (of 5) |
| **PRIMARY fixed-grid total** | **224** | **182** |
| retry-set size (deduped vs primary) | 176 | 180 |
| feature-based starts | +1 per trajectory | +1 per trajectory |

Kural S genuinely bites at the far-out-of-window × high-steepness /
narrow-scale edges (6 P-01 and 20 P-02 raw grid combos removed) — exactly the
intended impulse/edge-spike guard. The determinism check (full re-run,
element-wise comparison) returned identical sets.

---

## What this packet is NOT

No real SSA trajectory was touched; no fit was run; no family comparison of
any kind was made; no F3 threshold, tie-break, or cross-fit content exists
here. Kural S screening of start curves is model-only geometry under
stabilized evaluation, consistent with the D-F2-11 recommended scope.

## PI action requested

Ratify or amend, as **D-F2-09 = exact-enumeration-first contract**, Items
1–14 above (Items 11 and 13 are CLASS_C predeclared literals riding along for
completeness). Together with explicit acceptance of the other recommended
selections (D-F2-01..08, 06a–d, 07a–e, 10, 11, 12 + primitives
`w_min_years = 5`, `n_min = 3`), that unlocks STEP 1 (ART-F2 r1 → r2 with
C1–C10 + R1–R4). STEP 0 is skipped (no Option C was recommended anywhere).
