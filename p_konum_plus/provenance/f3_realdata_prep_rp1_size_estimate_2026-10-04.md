# p_konum_plus — rp1 — §7 Real-Data Run Size ESTIMATE

```text
artifact_role = deliverable H (rp1 instruction §8); rp1 instruction §7: "an engineering
                estimate of the real-data run's size from the synthetic per-call
                telemetry... with the method stated and labelled ESTIMATE. It decides
                nothing."
status        = ESTIMATE — INFORMATIONAL ONLY, NOT A REQUIREMENT, NOT A COMMITMENT,
                DECIDES NOTHING (rp1 instruction §7, verbatim)
date          = 2026-10-04
basis         = attempt-5 per-call telemetry (f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv,
                sha256 2648cb7feeba22f54c1cb27432d23c885ff3fb0d939ef28a596779b8a5390084)
                and the family telemetry (f3_step2_telemetry_rp1_2026-10-02.csv,
                sha256 836076827ae8b30d712191f5d3507dec6b721824acaa81bae491401d2e8f468f)
real_data_access = false (every number below is derived from SYNTHETIC fixtures; no
                real SSA/F1 file was read to produce this estimate)
```

## 1. Method

Two telemetry files, both from attempt 5, together cover the complete per-trajectory
fit battery:

- `f3_step2_telemetry_rp1_2026-10-02.csv` — one row per family START (fitters `P-01`,
  `P-02`), real `wall_clock_seconds`.
- `f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv` — one row per ACTUAL spline
  optimizer call (fitter `SPL`; a mode may call `trust-constr` then `SLSQP` if the
  primary stage is not accepted — the coarser `telemetry.csv`'s own `SPL` rows are
  **mode-level summaries with `wall_clock_seconds="UNAVAILABLE"`**, confirmed by
  direct inspection; the real per-call SPL timing exists only in the per-call file).

**Per-trajectory cost** = sum of `wall_clock_seconds` across every `P-01` row, every
`P-02` row, and every `SPL` per-call row belonging to that trajectory's `run1` fit
(the full battery the ratified contract names: 1 full fit + K=5 folds + LEFT/RIGHT
probes = 8 contexts, for both families and the spline, with the frozen start banks —
P-01: 731 grid points + 1 feature start; P-02: 261 + 1; SPL: 146 modes per context).

**Representative trajectory chosen: SCEN-A only.** `run1` has 4 trajectory-instances
(SCEN-A F0, SCEN-A M0, SCEN-B F0, SCEN-B M0). SCEN-B is deliberately driven to a
`STOP_BOTH_FAIL_REDESIGN` mechanism outcome by its injected fixture design — a
synthetic-test artifact, not a path a real (non-injected) trajectory takes — and its
family rows carry `NaN` wall-clock values from the injected-fault contexts, confirming
it cannot be used as a timing basis. SCEN-A resolves normally
(`RESOLVED_MECHANISM_P01`, no injected STOP) and is therefore the representative
"full battery, nothing skipped" trajectory cost.

**Scaling target: 906 trajectories (F 435 / M 471)** — the F1 freeze record's eligible
manifest size (rp1 instruction §4 C-3 cites it: "906 rows, F 435 / M 471"), the number
a real-data run would process. One sequential process is assumed (every rp1/r4
attempt of this lineage has run as one process; D-3's custody discipline does not
require parallelism and this estimate does not decide whether a future real-data run
uses it).

## 2. Per-trajectory cost (attempt 5, SCEN-A, run1)

| trajectory | family (P-01+P-02) wall (s) | SPL wall (s) | total (s) |
|---|---|---|---|
| SCEN-A, F0 | 44.155 | 304.195 | **348.350** |
| SCEN-A, M0 | 41.263 | 290.110 | **331.373** |

(SPL dominates: ~87–88% of per-trajectory wall-clock, consistent with 146 modes ×
up to 2 optimizer stages per context × 8 contexts, versus two family fits whose start
banks converge largely in a single call per start.)

## 3. Scaled estimate for 906 trajectories, one sequential process

```text
method A (sex-split): 435 × 348.350s (F) + 471 × 331.373s (M)
                     = 151,532.3s + 156,076.7s = 307,609.1s
                     ≈ 85.45 hours ≈ 3.56 days

method B (blended average, cross-check): 906 × ((348.350+331.373)/2)
                     = 906 × 339.862s = 307,914.7s
                     ≈ 85.53 hours ≈ 3.56 days
```

**ESTIMATE: ~85.4–85.5 hours (~3.56 days) of wall-clock, one sequential process,**
for the full fit battery (both families + spline, full/5-fold/2-probe) across all 906
real trajectories.

## 4. Explicitly excluded from this estimate

- `nr_gates` and `unit_tests` phase calls (388 + 1,602 calls in attempt 5) — fixed,
  one-time overhead, not per-trajectory, and already small relative to the scaled
  total (their combined run1-comparable wall-clock is on the order of single-digit
  minutes, not hours).
- A second (`RUN2`) redundant determinism-reproduction pass. rp1's own synthetic runs
  always fit RUN1 and RUN2 (to prove `DETERMINISM=True`); whether a real-data
  execution instruction also requires a reproduction pass is not decided here — if it
  does, roughly double the §3 figure.
- Any per-trajectory cost specific to real SSA data's F1 pipeline (loading, QC,
  z-normalization) — C-3's synthetic-only test (T-F1-LOADER-SYNTH) exercises this
  path on small generated files, not at real-data volume, and its own wall-clock was
  not separately telemetered; it is expected to be small relative to the fit cost but
  is not included in the number above.
- Any machine/environment difference between this estimate's host and whatever host
  eventually runs the real-data cycle.

## 5. What this estimate does NOT do

Per rp1 instruction §7, verbatim: **"It decides nothing."** It does not select a
generator, does not authorize a real-data run, does not set `F3_EXECUTION_READY`, and
is not a scheduling commitment. It is provided so the PI has an order-of-magnitude
figure (days, not hours; not weeks) when deciding how to schedule the real-data
execution cycle.

```text
commit = false
```
