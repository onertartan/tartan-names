# p_konum_plus — F3 STEP-2 r4-1 — Attempt Log (deliverable 12)

```text
artifact_role = attempt log required by T-R2-2 = AUTHORIZE_RESTART (D-3 S8.3) and T-RESTART-PROVENANCE
status        = NON-NORMATIVE (a disclosure record; the hashed results/custody files are authoritative)
date          = 2026-09-29 (revision tag) ; launches span 2026-09-29 .. 2026-09-30
revision      = r4-1 (correction revision inside the r4 cycle; child of the r4 package)
```

Counters, as in the r3/r4 logs: **harness attempt** increments only on a byte change (each
followed by a fresh, EXTERNALLY-written W-3 record — R3A-07); **launch** is every
`python ...` invocation. The three W-3 hashes per attempt (harness / generator / manifest)
are given per attempt; generator `68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830`
and manifest `5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe` are IDENTICAL
across all three attempts (never edited after the r4-1 fork); only the harness hash varies.
Every process ran with `real_data_access = false`.

## Attempt 1 — harness b22708d2fd7e1a68c5c471285d58d5398992bcde36690e5b04dc94321f6d9841 (layer OFF)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 1 | 19528 | 2026-09-29T20:24:03 | ~20:35 (ctx 41) | **interrupted** externally (no error; host process exited outside the harness's control) while progressing through RUN1 (last line `PROGRESS SPL ctx 41 SCEN-B run1:M0:probeL`). All preconditions/gates PASS (9 instruments; W-3 verified; NR-01(i)/(ii), NR-SPL, T-LOADER-NODES, T_MASK_FULL_EXT). This is the FIRST genuine interruption of the r4-1 revision; per D-3 S8.2/S8.3 the restart layer is introduced next. No results written. Note: `quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md`. |

## Attempt 2 — harness 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2 (layer ON, store empty)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 2 | 3348 | 2026-09-29T21:15:37 | ~22:06 (exit 1) | **ran the ENTIRE computation** (RUN1+RUN2, 11,869 units) — `EXC_CAPTURES_RUN1_EQ_RUN2 = True`, `T_EXPECT_ALL 36/36`, eval-level PENDING all pass (the 3 new INJ-SPL-PENDING fixtures) — then **stopped at the T-NONREG-R4 SELF-CHECK** (exit 1). Root cause: a representation bug in the CHECK, not a regression — it compared this run's in-memory `evals1` (native floats) against the canon()-ized (hex-string) r4 results, so 33/34 shared fixtures were spuriously flagged on `criteria`/`disc`/`dp04`. Applying `canon()` to both sides collapses all 33 to zero. Fixed in attempt 3. Note: `quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md`. Store (11,869 units) quarantined whole per D-3 S8.3. Attempt-2 harness bytes recovered byte-exact (reverting the single non-regression-block edit; hash re-verified = 280869892d…) and quarantined. |

## Attempt 3 — harness 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f (layer ON, store empty)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 3 | 22616 | 2026-09-29T22:14:16 | (ctx 42) | **interrupted** externally; NR gates + unit tests + RUN1 complete, 7,271 units persisted. |
| 4 | 7972 | 2026-09-30T12:44:02 | 13:03:07, **exit 0** | **COMPLETED, VERIFIED** (resumed from the 7,271-unit store): `DETERMINISM = True` (RUN1 == RUN2 == `556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77`); `T-EXPECT-ALL 36/36`, EXPECTATION_FAIL = []; captures RUN1==RUN2; NATURAL_UNRELATED_EVENTS = 0; **NONREGRESSION_VS_R4 shared=34 new=3 dropped=0 findings=0 real_path_spline_pending=0**; eval-level spline-pending PENDING (FULL→C3/C4b, FOLD→C2, PROBE→C4b; C4a stays PASS); COVERAGE_DERIVED = 64 rows, downgraded = []; all mandatory tests ran and passed; all output hashes verified on disk against the printed values. **This is the current, final state of the r4-1 revision.** |

## T-RESTART-PROVENANCE (D-3 S8.3), checked for launch 4's output
1. Store keys carry the code+input+environment fingerprint computed fresh by the reading
   process (`dc228827920a9633` for attempt 3) — cross-attempt reads impossible by
   construction; each interruption/fix ALSO started from an empty store (attempts 2 and 3
   after a whole-store quarantine), so no unit computed under superseded bytes existed to read.
2. RUN1/RUN2 unit namespaces disjoint (`realscen_run1_*` / `realscen_run2_*`); no test
   read another test's unit (per-key naming).
3. Every process contributing units to the final output is in this table (launches 3-4,
   both attempt 3); the per-call telemetry's phase/pid split shows exactly those two pids:
   `nr_gates/22616 = 60, unit_tests/22616 = 1602, run1/22616 = 5256, run2/7972 = 5256` —
   and the store manifest (11,869 rows) records pid/start_iso per unit (7,271 under pid
   22616, 4,598 under pid 7972).
T-SINGLE-PROCESS is NOT_RUN (units from 2 processes) per D-3 S4.4/S8.3; T-RESTART-PROVENANCE
takes its place. Progress rule (S8.3): no two consecutive launches completed zero new units
(7,271 then 4,598); the STOP condition never arose.

## ERRATUM-2 (R4A-10) — r3 custody-vs-quarantine labelling and the r4 report §8(c)
This erratum records the R4A-10 finding. The r3 and r4 files it concerns are historical and
are **NOT modified**; the reconciliation lives in the r4-1 quarantine annotation note
(`quarantine/f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md`) and the r4-1
start-state inventory §3/§4, and the corrected statement is carried in the r4-1 correction
report §8.

1. **Three named-but-unfiled r3 bytes are NOT_PRESERVED.** The r3 custody records name a
   harness `d67e097d…` (ATTEMPT5), a generator `e35c2bf0…` (attempts 1–5) and a harness
   `390f42b7…` (ATTEMPT8). A repository + quarantine search on 2026-09-29 (the two restart-
   store directories excluded — they hold pickled units, not source) found **none** of them.
2. **The ATTEMPT5/ATTEMPT8 quarantine labels do not hold the bytes their attempt custody
   record names.** The file filed under the ATTEMPT5 harness label is `f882b922…` (not
   `d67e097d…`); the file under the ATTEMPT8 harness label is `99f895c1…` (not `390f42b7…`);
   the generator filed under the ATTEMPT5 label is `cc23c9b5…` (the r3 FINAL/ATTEMPT8
   generator, not `e35c2bf0…`). ATTEMPT1/ATTEMPT2-3 harness and the ATTEMPT5 manifest do
   match. Full table in the annotation note §2/§3.
3. **The r4 report §8(c) statement is corrected.** The r4 correction report
   (`provenance/f3_step2_correction_report_r4_2026-09-27.md`, historical, NOT modified)
   states that `d67e097d…` is "present in quarantine". It is not; the ATTEMPT5 harness label
   holds `f882b922…`. The corrected statement is carried in the r4-1 correction report §8.
4. **Scope of impact — none on any delivered output.** The r3 FINAL run executed under
   harness `5fea165c…`/generator `cc23c9b5…` (fingerprint `1ba561da…`) and the r4 run under
   harness `5ef61a41…`; no unit under the r3 store's foreign prefix `548ae790…` (the
   recomputed fingerprint of the ATTEMPT8 custody triple, harness `390f42b7…`) was ever
   readable by either. This is a labelling/disclosure defect only.

`commit = false`.
