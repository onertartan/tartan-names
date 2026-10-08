# p_konum_plus — rp1-r1 — §7 Real-Data Run Size ESTIMATE (RP1A-05)

```text
artifact_role = deliverable H (rp1-r1 instruction §6 RP1A-05 + §7): the rp1 §7 estimate
                re-stated with its measurement scope LABELLED, plus a second line from
                T-F1-HANDOFF-SYNTH's measured full-lattice per-trajectory timing
status        = ESTIMATE — INFORMATIONAL ONLY, NOT A REQUIREMENT, DECIDES NOTHING
date          = 2026-10-05 (cycle tag; measurements 2026-10-04 and 2026-10-07/08)
real_data_access = false (every number below is from SYNTHETIC inputs)
```

## Line 1 — carried from rp1, scope now labelled (RP1A-05)

**ESTIMATE ~85.4–85.5 hours (~3.56 days), one sequential process, 906 trajectories.**
**Measured scope:** rp1 attempt-5 per-call telemetry, `run1` phase, **SCEN-A only** — a
smooth, well-conditioned synthetic bump trajectory (the fixture generator's `make_traj`
families), full battery (both families + spline, full/5-fold/2-probe), frozen start
banks. Method unchanged from the rp1 estimate (348.35 s/F-trajectory, 331.37 s/
M-trajectory, scaled 435 F + 471 M). This line's data is NOT from F1-shaped input; it
assumes real SSA trajectories optimize like the smooth synthetic families.

## Line 2 — NEW: measured on the F1-SHAPED synthetic trajectories (T-F1-HANDOFF-SYNTH, full lattice)

**Measured scope:** rp1-r1 attempt 2 (pid 34588), the T-F1-HANDOFF-SYNTH section —
6 trajectories built by the ACTUAL F1 pipeline from synthetic raw files
(released-record shares of random integer counts, z-normalized; near-flat, noise-like
series), full battery per trajectory with the ratified FULL_LATTICE start banks
(P-01 732 + P-02 262 starts × 8 contexts ≈ 7,952 family starts + 1,168 spline
mode-fits per trajectory).

```text
observed: handoff section ≈ 10 h of the 12 h 17 m total attempt-2 wall, 6 trajectories
          ≈ 1.5–1.8 h per trajectory (desktop under load; the same section standalone
          on an idle machine: 9 h 44 m total, file-timestamp evidence)
          of which measured SPL optimizer time: 1,524 s TOTAL (≈ 254 s/trajectory)
          => the family fits on flat-noise input are ≈ 95% of the cost (the frozen
          optimizers converge slowly there: ~1 s/start vs ~0.4-0.5 s/start on smooth
          synthetic data; 42k+ scipy warnings from flat objectives)
scaled:   906 trajectories × ~1.65 h ≈ ESTIMATE ~1,495 h ≈ 62 days, one sequential
          process, IF real SSA trajectories optimized like these flat-noise synthetics
```

## Reading the two lines together (informational)

The two lines bracket the real-data cost: real SSA trajectories are neither as smooth
as SCEN-A (line 1, ~3.6 days) nor as pathological as z-normalized random-count shares
(line 2, ~62 days) — real name-frequency series carry genuine structure (trends,
peaks) that the family models fit with far fewer iterations than pure noise. The
truthful statement is therefore an INTERVAL, dominated by family-fit convergence
behaviour on the actual data, not by the spline (whose cost is small and stable in
both measurements). Neither line is a commitment; per rp1 instruction §7, verbatim:
**"It decides nothing."** If the real-data execution cycle needs a tighter figure, a
PI-authorized timing probe on a few real trajectories would resolve the interval —
that is a PI decision, not this cycle's.

Excluded from both lines, as in rp1: nr_gates/unit-test one-time overhead; any RUN2
reproduction pass (if required, double the figure); F1 load/QC at real volume;
machine/environment differences.

```text
commit = false
```
