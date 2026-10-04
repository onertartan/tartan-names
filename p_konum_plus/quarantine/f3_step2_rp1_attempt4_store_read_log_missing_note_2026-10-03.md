# p_konum_plus — F3 real-data preparation rp1 — Attempt-4 Supersession Note (B' deliverable missing: STORE_READ_LOG never written)

```text
artifact_role = supersession note for rp1 attempt 4. Records a missing-deliverable
                defect found by the executor's own deliverable-by-deliverable scan
                against rp1 instruction §8 (performed before writing the register/
                report, at the PI's instruction), its fix, and the whole-store
                quarantine the harness change requires. RENAMES/MOVES nothing
                outside rp1's own attempt artifacts.
status        = NON-NORMATIVE
date          = 2026-10-03
revision      = rp1 (F3 real-data preparation cycle, inside the r4 lineage)
```

## 1. What attempt 4 did

rp1 attempt 4 (pid 26524, harness
`47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561`) ran to a
**clean exit 0**: 25/25 preconditions EQUAL; `T_STORE_READ_ACCOUNTING`
passed cold (`fit1_reads=0, served_to_fit2=146, fine_counter=146,
pass_=true` — the attempt-3 resume-robustness fix held under the ordinary,
non-resumed case); `T-NONREG-R4-2` passed (`s_findings=0, e_declared=39,
u_findings=0`); `DETERMINISM = True` (RUN1==RUN2==`556106e7...`, unchanged);
`end_state.narrowed_evidence = ["T-R2-2", "T-RP-1"]` (the attempt-2 fix
held); all 36 declared tests ran. `results.json` (sha256
`19e06629cc54a28fb86242e3972bc51d2eb5119436b754f64fc3d958a6bd293d`) and
every other deliverable of attempts 1-4's scope were written.

## 2. The defect found in the PI-ordered pre-register deliverable scan

Before writing the register and report, the PI instructed a scan of every
rp1 instruction §8 deliverable and every §4-9 named result field against
the harness code, naming the line that writes each one. That scan found:

`STORE_READ_LOG_PATH` (harness line 410, defined as
`f3_step2_rp1_store_read_log_{DATE_TAG}.csv`) is the path rp1 instruction
§4 C-1 names: *"A new deliverable lists every read (key family, key,
writer pid, reader pid)."* `grep` across the whole harness file showed
exactly one occurrence of this constant — its own definition. `STORE_READ_LOG`
(the in-process list every `ckpt_load` HIT appends to, harness line 226) is
populated and counted (`total_rows=len(STORE_READ_LOG)`, feeding
`results["store_read_accounting"]["total_rows"]`), but no code ever opens
`STORE_READ_LOG_PATH` for writing. The B' deliverable was declared by path
and never produced.

**Scope of the defect.** `results.json`'s `store_read_accounting` field
already carried the correct `total_rows` (146) and `fine_counts`
(`{"tstoreread__|splmode|26524": 146}`) — the underlying accounting was
correct, consistent across attempts 1-4, and is not in question. What was
missing is the row-level CSV deliverable itself (scope_or_phase, key
family, key, writer pid, writer start, reader pid, reader start — one row
per read), which the instruction requires as a standalone file, not merely
as a results.json summary.

**Why fixed by rerun, not by an erratum note.** This is a required
deliverable FILE that the code never produces, not a narrative description
of bytes. The precedent inside this same cycle is attempt 2's
`narrowed_evidence` omission (a delivered-field defect, fixed by a harness
change and a full rerun) — the same treatment applies here, one level up
(a delivered FILE rather than a delivered field).

A second, unrelated observation from the same scan: `EXPECTATIONS_E_PATH`
(harness line 414, with a comment describing it as "the expectations
manifest, WRITTEN BEFORE THE RUN (external file; the harness only READS
it)") is likewise defined and never referenced again — `EXPECTATIONS_E` is
instead an inline dict literal inside `main()`. This is dead code, not a
missing deliverable: rp1 instruction §8 lists no separate "expectations
manifest" file among A/B/B'/C/D/E/F1/G/H/T/Z, so nothing is omitted by
keeping the declaration inline. The PI's fix instruction for attempt 5 was
scoped narrowly to the B' write; this dead constant is left untouched and
is reported here only as an observation, carried into the attempt log's
scan table.

## 3. Fix (attempt 5 harness)

Immediately after the existing `STORE_MANIFEST_WRITTEN` block, the harness
now writes `STORE_READ_LOG_PATH` as a CSV (header
`scope_or_phase,key_family,key,writer_pid,writer_start,reader_pid,reader_start`,
one row per `STORE_READ_LOG` entry), then re-reads the file and asserts
that the CSV's data-row count, `len(STORE_READ_LOG)`, and
`sum(READS_FINE.values())` are all equal before printing
`STORE_READ_LOG_WRITTEN`. The file's path and sha256 are also folded into
`results["store_read_accounting"]` (`store_read_log_path`,
`store_read_log_sha256`, `store_read_log_rows`) for traceability; this adds
sub-fields under a key already declared `E` in its entirety
(`"store_read_accounting": "C-1 ADDITION (not in r4-2)"`), so no new
`EXPECTATIONS_E` entry is needed.

## 4. Whole-store quarantine (harness-change invariant)

Changing the harness changes its sha256 and therefore the
`code_env_fingerprint` that keys the restart store. Per the standing
"quarantine-whole-on-harness-change" rule, attempt 4's store and its launch
logs are quarantined in full and attempt 5 starts from an EMPTY store.

| quarantined artifact | what it is |
|---|---|
| `f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py` | attempt-4 harness bytes (sha256 `47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561`; copied before the fix above was applied) |
| `rp1_restart_store_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING/` | attempt-4 restart store, 12,453 units, fingerprint `4cb395a7217d1d64`, all pid 26524 |
| `f3_step2_rp1_launch4_stdout_2026-10-02.log` / `..._stderr_...log` | attempt-4's launch-4 logs (the clean exit-0 run) |

## 5. Response — attempt 5 (D-3 §8.3)

```text
harness attempt 5        = STORE_READ_LOG CSV write + row-count assert only
RESTART_LAYER_ACTIVE     = True (unchanged; T-RP-1 = ACTIVE_FROM_START applies to
                           every attempt of this cycle)
ATTEMPT_NUMBER           = 5
supersedes_harness_sha256 = 47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561
supersedes_custody_sha256 = 49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165
supersedes_note_path      = this note
```

A fresh W-3 custody record (written outside the run process) names the
attempt-5 harness/generator/manifest hashes and the new fingerprint before
attempt 5 runs, with a launch number (5) not previously used in this
cycle and its own non-colliding log file targets. No r3, r4, r4-1, r4-2,
or pre-existing quarantine file is modified, renamed or moved.

```text
deliverable_affected = store_read_accounting (new store_read_log_* sub-fields,
                        additive only) plus the new B' CSV file itself; all
                        other fields expected unchanged (scientific content
                        proven unchanged by attempt 4's s_findings=0 before
                        this rerun)
real_data_access = false
commit = false
```
