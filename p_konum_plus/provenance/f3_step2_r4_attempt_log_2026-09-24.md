# p_konum_plus - F3 STEP-2 r4 - Attempt Log (deliverable 12)

```text
artifact_role = attempt log required by T-R2-2 = AUTHORIZE_RESTART (D-3 S8.3) and T-RESTART-PROVENANCE
status        = NON-NORMATIVE (a disclosure record; the hashed results/custody files are authoritative)
date          = 2026-09-24 (cycle tag) ; launches span 2026-09-26 .. 2026-09-27
```

Counters, as in the r3 log: **harness revision** increments only on a byte change (each
followed by a fresh, EXTERNALLY-written W-3 record -- R3A-07); **launch** is every
`python ...` invocation. The three W-3 hashes per revision (harness / generator /
manifest -- R3A-07 asked for all three per attempt) are given in each revision block;
generator `393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c` and manifest
`c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8` are IDENTICAL across
all five revisions (never edited after the r4 fork); only the harness hash varies.
Every process ran with `real_data_access = false`.

## Revision 1 -- harness f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418 (layer OFF)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 1 | 30160 | 2026-09-26T13:04:38 | 13:23:21 (ctx 10) | **crashed on its own new assertion** (exit 1): T-EXC-UNRELATED-TYPE `context_unverifiable: false` -- the fresh-compute path never set `any_mode_unrelated`. The r4-new test caught, on its first execution, exactly the defect class the audit said the r3 test could not catch. Note: `quarantine/f3_step2_r4_attempt1_supersession_note_2026-09-24.md` (includes the disclosed reconstruction-with-hash-proof caveat for the quarantined bytes). |

## Revision 2 -- harness 20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306 (layer OFF)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 2 | 29296 | 2026-09-26T13:25:59 | 13:59:38 (ctx 34) | **interrupted** externally (no error; host process exited) -- the FIRST genuine interruption of the r4 cycle; per D-3 S8.2/S8.3 the restart layer is introduced next. Note: `quarantine/f3_step2_r4_attempt2_interruption_note_2026-09-26.md`. All pre-interruption checks PASS, including the corrected `context_unverifiable: true`. |

## Revision 3 -- harness 814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f (layer ON, store empty)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 3 | 27308 | 2026-09-26T14:55:16 | 15:29:43 (ctx 43) | **interrupted** externally; RUN1 complete, 7,421 units persisted. |
| 4 | 24680 | 2026-09-26T18:23:36 | 18:41:21 (exit 1) | **stopped by T-CANON**: RUN1 `19454f65...` != RUN2 `bfa626a6...`. Root cause 1 of 2: `k05_result` embedded the process-global cumulative counter. Note: `quarantine/f3_step2_r4_attempt34_k05_nondeterminism_note_2026-09-26.md`. Store (11,869 units) quarantined whole per D-3 S8.3. |

## Revision 4 -- harness 90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805 (layer ON, store empty)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 5 | 25924 | 2026-09-26T18:43:34 | 19:30:00 (ctx 70) | **interrupted** externally; RUN1 + 14/16 of RUN2 persisted (11,184 units). |
| 6 | 35860 | 2026-09-27T15:59:08 | 16:03:19 (exit 1) | **stopped by T-CANON again**, with a CHANGED hash pair (RUN1 `777fca02...` != RUN2 `148db2d1...`) -- proving the k05 fix effective and isolating root cause 2 of 2: the Y-03(ii) post-construction NaN mutation targeted the generator's module-level fixture object and leaked from RUN1 into RUN2. Note: `quarantine/f3_step2_r4_attempt56_mutation_leak_note_2026-09-27.md`. Store (11,869 units) quarantined whole per D-3 S8.3. |

## Revision 5 -- harness 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c (layer ON, store empty)
| # | pid | start | end/stop | outcome |
|---|---|---|---|---|
| 7 | 31388 | 2026-09-27T16:05:40 | 16:36:33 (ctx 33) | **interrupted** externally; 6,086 units persisted. |
| 8 | 29564 | 2026-09-27T17:44:22 | 18:06:15, **exit 0** | **COMPLETED, VERIFIED**: `DETERMINISM = True` (RUN1 == RUN2 == `777fca02e1f514038e04cb3b5aac5365fa4dd851b03174820ef4692f8c73c2d8` -- equal to revision 4's RUN1 value, confirming both determinism fixes independently); T-EXPECT-ALL 33/33, EXPECTATION_FAIL = []; captures RUN1==RUN2; NATURAL_UNRELATED_EVENTS = 0; FIDELITY 5/5; 27/27 mandatory tests ran and passed; all output hashes verified on disk against the printed values. **This is the current, final state of the r4 cycle.** |

## T-RESTART-PROVENANCE (D-3 S8.3), checked for launch 8's output
1. Store keys carry the code+input+environment fingerprint computed fresh by the reading
   process (`5ef61a412c6bd76c` for revision 5) -- cross-revision reads impossible by
   construction; each defect fix ALSO quarantined the store whole, so no unit computed
   under superseded bytes existed to read.
2. RUN1/RUN2 unit namespaces disjoint (`realscen_run1_*` / `realscen_run2_*`); no test
   read another test's unit (per-key naming).
3. Every process contributing units to the final output is in this table (launches 7-8,
   both revision 5); the per-call telemetry's phase/pid split shows exactly those two
   pids: `run1/29564 = 1300, run1/31388 = 3956, run2/29564 = 5256, nr_gates/31388 = 60,
   unit_tests/31388 = 1602` -- and the store manifest (11,869 rows) records pid/start_iso
   per unit.
T-SINGLE-PROCESS is NOT_RUN(units from 2 processes) per D-3 S4.4/S8.3; T-RESTART-PROVENANCE
takes its place. Progress rule (S8.3): no two consecutive launches completed zero new
units (ctx/store counts above); the STOP condition never arose.

## ERRATUM to the r3 attempt log (R3A-07; the r3 file is historical and NOT modified)
Target: `p_konum_plus/provenance/f3_step2_r3_attempt_log_2026-09-22.md`, sha256
`253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5` (hash re-verified
against the repository copy on 2026-09-24 before this erratum was written; it equals the
value the independent audit received).
1. **Rows 9-10, "harness rev" column**: the log says revision 5 = `99f895c1...`. WRONG:
   `99f895c1...` is the SUPERSEDED revision quarantined by the attempt-8 note; the bytes
   rows 9-10 actually executed are `5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77`
   -- as proven by three independent sources the audit named (the r3 custody record, the
   harness constant SUPERSEDES_HARNESS_SHA256, and the restart-store fingerprint
   `1ba561daefb48b2e` which the auditor recomputed from the delivered triple), and
   re-verified by this executor directly (`sha256sum` of the r3 harness = `5fea165c...`).
   Root cause of the error: the log's hash column was filled from the pre-launch
   quarantine chain rather than from a post-edit re-hash of the live file.
2. **Three W-3 hashes per attempt**: the r3 log recorded only the harness hash per row.
   The r3 generator/manifest pairs per revision are recoverable from the r3 custody
   records (live + quarantined copies) and are given per-revision in the r3 section of
   the r4 correction report; this log records all three per revision natively.
3. **Foreign store entries (T-R3-2)**: the r3 final store held 11,723 entries under
   prefix `548ae790f6ac756a`, matching no combination named in any r3 file. On 2026-09-27
   the ENTIRE final r3 store (23,446 entries) was moved to
   `quarantine/r3_restart_store_2026-09-22_FINAL_T-R3-2/` and the 11,723 foreign entries
   were individually listed (path, size, sha256) in
   `quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv`.
   Origin of the prefix: consistent with launches under intermediate byte-states of the
   r3 editing sequence whose exact bytes were not separately preserved; nothing under it
   was ever readable by the delivered r3 harness (prefix mismatch by construction, as the
   audit itself established).

`commit = false`.
