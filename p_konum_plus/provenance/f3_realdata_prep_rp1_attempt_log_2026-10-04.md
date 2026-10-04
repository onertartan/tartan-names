# p_konum_plus — F3 real-data preparation rp1 — Attempt Log (deliverable 12)

```text
artifact_role = attempt log required by T-RP-1 = ACTIVE_FROM_START (D-10 §2; rp1
                instruction §4 C-6) and T-SINGLE-PROCESS/T-RESTART-PROVENANCE;
                carries the PI-ordered deliverable scan (§2) and the ctx-22 erratum (§7)
status        = NON-NORMATIVE (a disclosure record; the hashed results/custody files
                are authoritative)
date          = 2026-10-04 (revision opened 2026-10-03; closed 2026-10-04)
revision      = rp1 (F3 real-data preparation cycle, inside the r4 lineage)
```

Counters: **attempt** increments only on a harness byte change; **launch** is every
`python ...` invocation. R41A-02 (adopted unchanged, rp1 instruction §6) applies from
the first write of this cycle: one custody record per attempt (external writer,
refuses an existing path, `supersedes_custody_sha256` filled from attempt 2 on); one
launch-numbered log pair per launch, never overwritten; the harness is copied to
quarantine before any edit of a superseded attempt. T-RP-1 = ACTIVE_FROM_START
(D-10 §2, S-b) means the restart layer is ON from attempt 1 — unlike every prior
revision of this lineage, where attempt 1 ran with it off.

The generator `68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830` and
the manifest `5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe` are
REUSED UNCHANGED from r4-1 (rp1 instruction §4, "nothing else changes"): regenerated
in memory and verified equal by both the W-3 writer and `main()` at every launch, never
rewritten. Only the harness hash varies across attempts. Every process ran with
`REAL_DATA_MODE = False` (asserted at `main()` start) and `real_data_access = false`.

## Attempt 1 — harness `08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2`

Custody: `f3_step2_rp1_preexecution_custody_attempt1_2026-10-02.md`
(`f78966d063c9991c590ed29d14f5671d998184aa6515b8f658c0f956998183eb`),
`code_env_fingerprint = 64b35e0777fdbb52`, supersedes nothing.

| # | launch logs (sha256, quarantined) | pid | start | outcome |
|---|---|---|---|---|
| 1 | `f3_step2_rp1_launch1_stdout_2026-10-02.log` (`445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f`) / `..._stderr_...` (`c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b`) | 11116 | 2026-10-03T12:46:23.509838 | **STOPPED**: `AssertionError` at `T-NONREG-R4-2` — `s_findings=[]`, **4 U findings**, all representational: `end_state.corrections_complete`, `end_state.mandatory_tests_all_run`, `end_state.mandatory_tests_missing` (all three computed from `TESTS_RUN` BEFORE this very test records itself — a staleness bug, not a scientific one), and `solver_exceptions` (a provenance-only pid/start_iso/traceback difference, not content). Everything through RUN2 passed cleanly first: 25/25 preconditions, `T-F1-LOADER-SYNTH`/`T-CONTEXT-ID-UNIQUE`/`T-INADMISSIBLE-OBSERVABLE`/`T-STORE-READ-ACCOUNTING` all passed in-run, `DETERMINISM=True` (`556106e7…`), residual `3ee624f3…` unchanged, `T-NONREG-R4-1` 37/0. No `results.json` written. Fixed for attempt 2 — see `quarantine/f3_step2_rp1_attempt1_nonreg_bug_note_2026-10-02.md`. |

Quarantined whole: harness bytes (`...ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py`), store
(12,453 units, fingerprint `64b35e0777fdbb52`), both launch-1 logs.

## Attempt 2 — harness `0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5`

Custody: `f3_step2_rp1_preexecution_custody_attempt2_2026-10-02.md`
(`f2d33d169c161d6d004570d7aa92c8241d136bf0bb9822e76c774adce6ec1aa4`),
`code_env_fingerprint = d2ee833b4bad9138`,
`supersedes_harness_sha256 = 08d9bcc8…`.

| # | launch logs (sha256, quarantined) | pid | start | outcome |
|---|---|---|---|---|
| 2 | `f3_step2_rp1_launch2_stdout_2026-10-02.log` (`d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7`) / `..._stderr_...` (`df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613`) | 13328 | 2026-10-03T14:02:04.307133 | **RAN TO CLEAN EXIT 0**: `T-NONREG-R4-2` passed (`s_findings=0, e_declared=36, u_findings=0`); all 36 declared tests ran; `DETERMINISM=True`; results `bdcfa38a9b92e56b67db1b2695d46d20d107d3c9e865d154865ec8dea0d2234f`. **Post-run defect found by the executor, not by the run**: `end_state.narrowed_evidence = ["T-R2-2"]`, missing `"T-RP-1"` (rp1 instruction C-6 names it by value, same rule as `T-R2-2`; no `T_RP_1` constant existed in code). A delivered-field defect, fixed for attempt 3 — see `quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md`. |

Quarantined whole: harness bytes (`...ATTEMPT2_NARROWED_EVIDENCE_MISSING.py`), store
(12,453 units, fingerprint `d2ee833b4bad9138`), both launch-2 logs, and the complete
9-file attempt-2 output set (prefixed `ATTEMPT2_NARROWED_EVIDENCE_MISSING_`).

## Attempt 3 — harness `d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d`

Custody: `f3_step2_rp1_preexecution_custody_attempt3_2026-10-02.md`
(`239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a`),
`code_env_fingerprint = 9cba3c77c85d5885`,
`supersedes_harness_sha256 = 0d6894c2…`.

| sub-process | pid | start | role | outcome |
|---|---|---|---|---|
| first | 23540 | 2026-10-03T15:17:22.774354 | original launch 3 | genuinely **interrupted**; wrote 4,449 store units before stopping |
| second | 26784 | 2026-10-03T15:46:53.866378 | resume of the same attempt | **STOPPED**: `AssertionError` at `T-STORE-READ-ACCOUNTING` |

Two defects, both the executor's process, disclosed here together with their evidence:

**(a) launch-log truncation.** The resume reused `F3_RP1_LAUNCH=3` and the SAME
`>`-redirected log targets as the interrupted process. `>` truncates on open, so pid
23540's partial console text (its own ctx 1 through the point of interruption) was
destroyed the instant pid 26784's redirect opened the same files — an R41A-02(c)
violation. What survives: pid 23540's 4,449 written units carry their own pid and
`start_iso` in every store payload (verified below, §7), so the computational record
is intact; only the console text is unrecoverable. The two launch-3 logs that exist
(`f3_step2_rp1_launch3_stdout_2026-10-02.log`,
`7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d`; `..._stderr_...`,
`915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45`) hold ONLY pid
26784's output (23 stdout lines, 6 stderr lines) — mirrors the r4-2 attempt-2/launch-1
precedent of disclosing lost console text while the store manifest's provenance survives.

**(b) T-STORE-READ-ACCOUNTING resume-robustness bug.** The test's original invariant
required `fit1_reads == 0` (fit1 must compute fresh). On this resume, `fit1`'s 146
`tstoreread__`-scoped units were themselves already cached by pid 23540's earlier pass
through the same early contexts, so `fit1` came back as 146 cache hits, not 0, and the
assertion failed even though the underlying accounting was correct
(`fine_counter=292` = 146+146). Fixed for attempt 4 by dropping the `fit1_reads==0`
requirement; pass_ now requires only `served_to_fit2 == T_modes` — see
`quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md`.

Quarantined whole: harness bytes (`...ATTEMPT3_STORE_READ_RESUME_BUG.py`), the merged
store (4,449 units, fingerprint `9cba3c77c85d5885`), both launch-3 logs.

## Attempt 4 — harness `47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561`

Custody: `f3_step2_rp1_preexecution_custody_attempt4_2026-10-02.md`
(`49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165`),
`code_env_fingerprint = 4cb395a7217d1d64`,
`supersedes_harness_sha256 = d57003f9…`,
`supersedes_custody_sha256 = 239adb3a…`.

| # | launch logs (sha256, quarantined) | pid | start | outcome |
|---|---|---|---|---|
| 4 | `f3_step2_rp1_launch4_stdout_2026-10-02.log` (`c1b286fa378def03c91035199750f6243cb501768f10852996dfdc8b4d71f698`) / `..._stderr_...` (`df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613`) | 26524 | 2026-10-03T15:58:50.230844 | **RAN TO CLEAN EXIT 0**: `T-STORE-READ-ACCOUNTING` passed cold (`fit1_reads=0, served_to_fit2=146, fine_counter=146`); `T-NONREG-R4-2` passed (`s_findings=0, e_declared=39, u_findings=0`); `narrowed_evidence=["T-R2-2","T-RP-1"]` correct; `DETERMINISM=True`; results `19e06629cc54a28fb86242e3972bc51d2eb5119436b754f64fc3d958a6bd293d`. **Defect found by a PI-ordered deliverable scan performed BEFORE the register/report** (§2 below): the B' deliverable (`STORE_READ_LOG`, rp1 instruction §4 C-1 — "a new deliverable lists every read") was declared as a path constant (`STORE_READ_LOG_PATH`) and never written to a file; the accounting itself (`total_rows`, `fine_counts`) was correct throughout, only the row-level CSV was missing. Fixed for attempt 5 — see `quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md`. |

Note on the launch-2/4/5 stderr hashes being identical (`df257d12…` all three): this is
expected, not a bug — these three attempts share the identical numerical code path
(only accounting/bookkeeping changed between them), so the deterministic scipy/numpy
warning text is byte-for-byte reproducible across all three. It is independent
corroboration of `DETERMINISM=True`.

Quarantined whole: harness bytes (`...ATTEMPT4_STORE_READ_LOG_MISSING.py`), store
(12,453 units, fingerprint `4cb395a7217d1d64`, all pid 26524), both launch-4 logs, and
the complete 9-file attempt-4 output set (prefixed `ATTEMPT4_STORE_READ_LOG_MISSING_`).

## Attempt 5 — harness `39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09` (current, final)

Custody: `f3_step2_rp1_preexecution_custody_attempt5_2026-10-02.md`
(`7e2ee506a2819dc1a0f579751dbfa552d2a472d50309fef2a2e0d1731a853ae9`),
`code_env_fingerprint = a33c98202ae1591d`,
`supersedes_harness_sha256 = 47b42533…`,
`supersedes_custody_sha256 = 49cc92c9…`.

| # | launch logs (sha256) | pid | start | outcome |
|---|---|---|---|---|
| 5 | `f3_step2_rp1_launch5_stdout_2026-10-02.log` (`cbd2281e5719911a997ddf9103707d50adc74e7857616aaf443f9b0dd815f715`) / `..._stderr_...` (`df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613`) | 33100 | 2026-10-04T15:09:42.946397 | **COMPLETED, VERIFIED** — see §3–§6 |

### §3 Clean-run evidence

`T-EXPECT-ALL 36/36`; `DETERMINISM=True` (RUN1==RUN2==`556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77`,
unchanged since r4-1); residual series `3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f`
(unchanged); `T-NONREG-R4` findings=0; `T-NONREG-R4-1` compared=37, findings=0,
stops_equal=True; **`T-NONREG-R4-2` `s_findings=0, e_declared=39, u_findings=0`**;
`COVERAGE_DERIVED=64 rows, downgraded=[]`; `end_state` (refreshed) —
`corrections_complete=true, mandatory_tests_all_run=true, mandatory_tests_missing=[],
narrowed_evidence=["T-R2-2","T-RP-1"], open_findings=[]`.

### §4 B' deliverable fix verified

`STORE_READ_LOG_WRITTEN = f3_step2_rp1_store_read_log_2026-10-02.csv
sha256=6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1 rows=146`.
Cross-checked independently of the harness's own in-run assert: the file has 147
lines (1 header + 146 data rows); `results.json["store_read_accounting"]` reports
`total_rows=146` and `fine_counts={"tstoreread__|splmode|33100": 146}` (sum 146) —
CSV rows, `total_rows`, and the `fine_counts` sum all agree at 146, matching the
in-run assert the harness fix added (§4 of the attempt-4 supersession note).

### §5 Empty-store proof

The store manifest (`f3_step2_rp1_restart_store_manifest_2026-10-02.csv`,
`ca355af467f66a05b19e82fa3e2f515ce41a253718b0120e30fae6338d96a733`, 12,453 rows) was
read back independently of the harness: **every one of the 12,453 rows carries `pid
33100` and the single `start_iso` 2026-10-04T15:09:42.946397** — the exact pid/start of
this attempt's one process, and no other pid appears. This proves the store was empty
at this attempt's first launch (no unit survived from attempt 4's quarantined store)
and that **T-SINGLE-PROCESS holds**: one process computed every unit of deliverables
5–8 and every result object.

### §6 Environment match (condition (e))

Attempt 5's `environment` field: `python 3.11.7, numpy 1.26.4, scipy 1.14.1,
Windows-10-10.0.19045-SP0, OMP/OPENBLAS/MKL=1` — read back from both attempt 4's
quarantined `results.json` and attempt 5's `results.json` independently of the
harness: **identical field-by-field**, no difference to report.

### §6b E-declaration timing proof (condition (d))

`EXPECTATIONS_E` is an inline dict literal in `main()` (no separate declaration
file; `EXPECTATIONS_E_PATH` is a vestigial, unused constant — see §2 below). The
"declaration file" is therefore the harness source file itself. Its hash
(`39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09`) and filesystem
mtime (`2026-10-04 15:07:39.66`, read with `ls -la --time-style=full-iso`
immediately before the launch 5 invocation) were recorded BEFORE attempt 5 started
(`PID=33100, START=2026-10-04T15:09:42.946397`) — the declaration predates the run by
2 minutes 3 seconds. The dict's shape (prefixes, not per-run values) is otherwise
unchanged from attempt 4: the only new sub-fields it must cover
(`store_read_accounting.store_read_log_path/_sha256/_rows`) fall under the already
fully-declared `"store_read_accounting"` prefix, so no new entry was needed.

## §7 Erratum — attempt-3 interruption context (ctx 20 → ctx 22)

Both the attempt-3 quarantine note (`f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md`,
left unmodified — correcting it would not change any hash-pinned artifact, but the
PI's instruction (f) directed the correction into this attempt log instead) and the
attempt-4/attempt-5 harness comment text (as it stood through attempt 4) state that
the attempt-3 interruption landed at "SPL ctx 20". This is **incorrect** — the actual
interruption point, established by direct forensic inspection of the quarantined
attempt-3 store (`rp1_restart_store_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG/`, 4,449
files, all pid 23540, all `start_iso` 2026-10-03T15:17:22.774354) this session, is
**SPL ctx 22** (`SCEN-A run1:M0:fold0`). Evidence:

```text
SCEN-A_P-01_run1_M0_full    4/4 files present  (ctx 21, complete, both fitters)
SCEN-A_P-01_run1_M0_fold0   4/4 files present  (ctx 22, P-01 fitter complete)
SCEN-A_P-02_run1_M0_fold0   2/4 files present  (ctx 22, P-02 fitter: only
                             grid_0 and grid_130 written; "feature" and
                             grid_260 missing — the exact write in progress
                             when the process stopped)
```

against attempt-5's clean `PROGRESS` numbering (ctx 21 = `SCEN-A run1:M0:full`, ctx 22
= `SCEN-A run1:M0:fold0`). The interruption is therefore pinned to ctx 22, mid-write on
the P-02 fitter's grid search, not ctx 20. This is a provenance-narrative correction
only: it does not change any computation, test result, store unit, or delivered field
from any attempt — `s_findings` was `[]` in every attempt that reached a comparison.
The attempt-5 harness comment carries the corrected figure going forward.

## §2 Deliverable/field scan (PI-ordered, performed before writing the register/report)

Every rp1 instruction §8 deliverable and every §4–§9 named result field, checked
against the harness code with the line that writes or computes it (line numbers as of
the attempt-5 harness, `39c733a3…`):

| item | status | evidence (line / file) |
|---|---|---|
| 1 harness (diff vs r4-2) | present | diff computed, 1,087 differing lines; "contains only C-1…C-6" is the AUDITOR's check (rp1 instruction §10), not re-verified exhaustively here; spot-checked: no `6B` marker anywhere in the file |
| 2–3 generator / manifest reused | present | named by path+hash, regenerated in memory and verified equal every launch (`MANIFEST_REUSED_UNCHANGED_FROM_R4_1 = true`) |
| 9 register | written this session | `f3_step2_class_c_pin_register_rp1_2026-10-04.md` |
| 10 report | written this session | `f3_step2_correction_report_rp1_2026-10-04.md` |
| 11 start-state inventory | present (prior session) | `provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md` |
| 12 attempt log | this file | — |
| A per-call telemetry | present | `csv.DictWriter` write, harness ~L4581 |
| B store manifest | present | `csv.writer` write, harness ~L4593 |
| **B' store-read log** | **was MISSING in attempts 1–4; fixed for attempt 5** | `STORE_READ_LOG_PATH` defined L410, write+assert added ~L4604–4627 this session |
| C capture records + RUN1/RUN2 comparison | present | `EXC_CAPTURES_RUN1_EQ_RUN2`, printed; captures carried in `test_evidence.json` |
| D T-NONREG-R4-2 CSV | present | `csv.DictWriter` write, harness ~L5080 |
| E quarantine copies, notes, launch log pairs | present | `p_konum_plus/quarantine/` (5 attempts' worth) |
| F1 T-F1-LOADER-SYNTH fixtures | present | `f3_step2_rp1_f1_synth_fixtures_2026-10-02/`, written ~L3824 |
| G C-5 statement | written this session | `provenance/f3_realdata_prep_rp1_c5_observability_statement_2026-10-04.md` |
| H §7 size estimate | written this session | `provenance/f3_realdata_prep_rp1_size_estimate_2026-10-04.md` |
| T transmission list | written this session | `provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md` |
| Z zip | assembled this session | `f3_realdata_prep_rp1_package_2026-10-04.zip` |
| C-1 `units_read_from_store` (coarse) | present | dict `UNITS_READ_FROM_STORE`, defined L331, assigned L4624-area (per-phase, inherited from r4-2, declared E) |
| C-1 fine-grained read log | **fixed this session** | see B' above |
| C-2(i) `passes_identical`, `pass_key_namespaces_disjoint` | present | ~L3212–3213 |
| C-2(ii) T-KEY-NAMESPACE test + register table | present | `record_test("T-KEY-NAMESPACE", ...)`, `key_namespace_table` in results ~L4806 |
| C-3 `REAL_DATA_MODE=False` + assert | present | module constant L440; assert ~L3650 |
| C-3 opened-file audit (X-18/Y-12) | present | `sys.addaudithook`, L117; `opened_files_declared`/`opened_files_audit_derived` in results, both E-declared as "rp1's own file paths" — confirmed no F1/SSA path appears in either list |
| C-3 test T-F1-LOADER-SYNTH | present, PASSED | ~L3821 |
| C-4 test T-CONTEXT-ID-UNIQUE | present, PASSED | ~L3837 |
| C-5 counters + test | present, PASSED | `INADMISSIBLE_COMPLETED` L3056; test ~L3841 |
| C-5 statement (G) | written this session | see G above |
| C-6 restart layer / narrowed_evidence | present, correct since attempt 3 | `T_RP_1` constant, `narrowed_evidence` computation |
| C-6 T-SINGLE-PROCESS / T-RESTART-PROVENANCE | narrative determination, not a coded field | holds for attempts 2, 4, 5 (one pid each, proven §5 above for attempt 5); would have been T-RESTART-PROVENANCE for attempt 3 had it completed (it did not) |
| C-7 no 6B code | confirmed | no `6B` marker in the file |
| §5 T-NONREG-R4-2 | present, PASSED (attempts 2, 4, 5) | ~L5080 |
| §7 estimate | written this session | see H above |
| §9 end_state fields | present, correct | refreshed block, confirmed §3 above |
| §9 `rp1_status` | **not a coded field** — computed in the report (§9 of the instruction defines it from the mandatory-test/non-regression/open-findings criteria; the harness's `F3_STEP2_r4_status` is a different, legacy field inherited from the r4 lineage, not this cycle's own status) | see the correction report |

**One additional observation, not a missing deliverable**: `EXPECTATIONS_E_PATH`
(L414, comment: "the expectations manifest, WRITTEN BEFORE THE RUN (external file;
the harness only READS it)") is defined and never referenced again —
`EXPECTATIONS_E` is an inline dict instead. rp1 instruction §8 names no separate
"expectations manifest" deliverable letter, so nothing is omitted; this is dead code,
left untouched per the PI's narrow-fix instruction for attempt 5, and reported here
only for completeness.

## Single-process statement (D-3 §8.3)

Attempts 2, 4 and 5 each ran as ONE process, start to finish, computing every unit of
that attempt's store and every result object — **T-SINGLE-PROCESS applies and holds**
for all three (store manifests: one pid each; `units_read_from_store` all 0 for each).
Attempt 1 ran as one process that stopped at the non-regression check before writing a
store-dependent result; no store-read ever occurred within it either. Attempt 3 is the
only T-RESTART-PROVENANCE case of this cycle: two processes (pid 23540, pid 26784)
jointly produced its (truncated) partial record before it, too, stopped on a defect —
it never reached exit 0, so no deliverable depends on it.

```text
real_data_access = false throughout every attempt
commit = false
```
