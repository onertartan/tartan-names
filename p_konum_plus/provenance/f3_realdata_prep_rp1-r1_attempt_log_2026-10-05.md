# p_konum_plus — F3 real-data preparation rp1-r1 — Attempt Log (deliverable 12)

```text
artifact_role = attempt log for the rp1-r1 B-correction cycle; carries the pre-§1 process-error
                disclosure (§0) and, below it, one section per attempt
status        = NON-NORMATIVE (a disclosure record; the hashed results/custody files are authoritative)
date          = 2026-10-05 (opened before attempt 1; extended as attempts run)
revision      = rp1-r1 (B-correction cycle of rp1, inside the r4 lineage; D-11 r1 governs)
```

## 0. Process-error disclosure (before §1 was fully verified)

Before the rp1-r1 instruction §1 preconditions were completely re-verified — specifically, before
the PI delivered the two "input, not directive" files §1 item 2 requires (the rp1 independent audit,
GPT Codex, `2fa28e2a…`, and the review of the rp1-r1 DRAFT, GPT Codex, `aa9fcaa9…`) — the executor
copied `p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py` to
`p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py` (created 2026-10-05, local
machine time ~19:54; content byte-identical to the rp1 harness,
sha256 `39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09` — no R-1…R-5 edit had yet
been made to it). This preceded a completed §1 and was a precondition-discipline error. Per the PI's
explicit instruction, the copy was deleted before any further action; nothing was computed, keyed,
pickled, or derived from it while it existed, and no other file was touched. The full §1
re-verification that followed (after the two input files arrived) is recorded in the start-state
inventory §1; it passed with no mismatch. See also
`provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md` §0.

Counters: **attempt** increments only on a harness byte change; **launch** is every `python ...`
invocation. R41A-02 (adopted by rp1, carried unchanged into rp1-r1 per D-11 r1 §9) applies from the
first write: one custody record per attempt, external writer, never overwritten; one launch-numbered
log pair per launch; harness copied to quarantine before any edit of a superseded attempt. T-RP-1 =
ACTIVE_FROM_START (carried from D-10) applies again: the restart layer is ON from attempt 1 of this
cycle too.

The generator `68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830` and the manifest
`5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe` are REUSED UNCHANGED from r4-1
(regenerated in memory and verified equal by the W-3 writer AND by `main()` at every launch). Only
the harness hash varies across attempts. Every process ran with `REAL_DATA_MODE = False` (asserted
at `main()` start) and `real_data_access = false`.

## Attempt 1 — harness `4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d`

Custody: `f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md`
(`dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d`), supersedes nothing
(first attempt of this cycle).

| # | launch logs (sha256, quarantined) | pid | start | outcome |
|---|---|---|---|---|
| 1 | `f3_step2_rp1-r1_launch1_stdout_2026-10-05.log` (`f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7`, 204 lines) / `..._stderr_...` (`fdf8c410faa5ff104eb1519e4a831b113000490ed51ae980550ecff2181308ff`) | 34228 | 2026-10-06T10:55:39.541069 | **STOPPED at `T-NONREG-R4-2`** with `s_findings=[]` (scientific content already byte-identical to r4-2) and **6 U findings, all three bugs in the R-3 comparison logic ITSELF**, none in any computation: (a) COUNT-kind double-canonicalization; (b) an `exc_injection_fixtures` EQUAL declaration colliding between the two compared files; (c) three capture-record fields declared EQUAL instead of provenance-stripped. Everything before that passed: 31/31 preconditions; `T-F1-LOADER-SYNTH` 21/21 cases (the 8 new R-2 branches included); `T-F1-HANDOFF-SYNTH` 144/144 with loader x-hashes matched; `T-CONTEXT-ID-UNIQUE` (replacement) on the actually-passed ids; `T-F1-CONTRACT-GAP` 4/4; `T-F1-REPRO-GATE-SYNTH` 5/5; cold+warm `T-STORE-READ-ACCOUNTING`; `T-EXPECT-ALL` 36/36; `DETERMINISM=True` (`556106e7…`); residual `3ee624f3…` unchanged; `T-NONREG-R4-1` 37/0. No `results.json` written. Fix note: `quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md`. |

Quarantined whole: harness bytes (`...ATTEMPT1_NONREG_E_DECLARATION_BUGS.py`, hash verified equal
to the custody-pinned value), store (67,313 units, all pid 34228), both launch-1 logs, and the
9-file written-output set (prefixed `ATTEMPT1_NONREG_E_DECLARATION_BUGS_`).

## Attempt 2 — harness `cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb` (current, final)

Custody: `f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md`
(`162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca`),
`code_env_fingerprint = 29de608948a06cf2`,
`supersedes_harness_sha256 = 4bffb33a…`, `supersedes_custody_sha256 = dc10e08c…`.

| # | launch logs (sha256) | pid | start | end | outcome |
|---|---|---|---|---|---|
| 2 | `f3_step2_rp1-r1_launch2_stdout_2026-10-05.log` (`d26b2898c580aae762af8a824851e9ea5c1e9cd8bd9c72424052d58ec83c6630`) / `..._stderr_...` (`afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b`) | 34588 | 2026-10-07T14:51:58.715047 | 2026-10-08T03:08:36.537570, **exit 0** | **COMPLETED, VERIFIED**: `T-NONREG-R4-2` `s_findings=0, e_declared=2114, u_findings=0` (full-depth R-3: results.json every leaf + test_evidence.json every leaf + telemetry row-by-row/column-by-column); 39/39 recorded tests `ran=true, passed=true` (38 mandatory + T-NONREG-R4); `DETERMINISM=True` (RUN1==RUN2==`556106e7…`, unchanged since r4-1); residual `3ee624f3…` byte-identical; `end_state` refreshed: `corrections_complete=true`, `mandatory_tests_missing=[]`, `narrowed_evidence=["T-R2-2","T-RP-1"]`, `open_findings=[]`, `PI_dispatch_record_hash` = D-12 observed; environment field-by-field equal to the binding one. Results `e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb`. |

### Single-process statement (D-3 §8.3) and R-5 accounting

One process (pid 34588, 14:51:58 → 03:08:36, **12 h 16 m 38 s**) computed **all 67,313 store
units and every result object — T-SINGLE-PROCESS applies and holds** (store manifest: one pid;
`units_read_from_store` coarse counters 0 outside the declaring test's own namespaces). The
per-call telemetry `source` column (R-5): 21,725 `fresh` / 492 `replay`, the 492 exactly the
three deliberate T-STORE-READ-ACCOUNTING re-reads (cold fit2 164 + warm fit1 164 + warm fit2
164); the B' store-read log: 730 rows = cold scope 292 (146 fit2 + 146 verification re-reads)
+ warm scope 438 (146 fit1 + 146 fit2 + 146 verification), arithmetic exact, every row
scoped/attributed to pid 34588.

### Run-time note (feeds RP1A-05)

Of the 12.28 h, the `T-F1-HANDOFF-SYNTH` section dominates (~10 h): per trajectory it runs the
FULL family battery (P-01 732-start + P-02 262-start banks × 8 contexts ≈ 7,952 family optimizer
starts) on flat-noise synthetic z-series where the frozen optimizers converge slowly — measured
SPL (spline) optimizer time is only 1,524 s TOTAL (≈ 254 s/trajectory), so the family fits, which
the delivered telemetry does not row-log for this section (the handoff's local telemetry list is
discarded by design; only spline per-call rows are global), account for ≈ 95 % of the section's
wall time. ≈ 1.5–1.8 h per trajectory on the binding machine under desktop load. The same section
took 9 h 44 m in the executor's standalone pre-verification on an otherwise idle machine
(2026-10-05 21:41 → 2026-10-06 07:25, file-timestamp evidence) — the primary-run figure is
consistent with that baseline plus contention, and nothing about it is anomalous.

### R-4 executor dry check (2026-10-08, after attempt 2; procedure §4)

Performed once in `G:\rp1r1_dry_check\pkp-copy` (robocopy of the tree, `.git`/quarantined
stores/live store/zip excluded): (1) the delivered W-3 writer with `F3_REPO_ROOT` at the copy
REFUSED while the executor's attempt-2 custody was present — then, custody records moved to a
kept-aside folder outside `p_konum_plus`, it wrote the copy's own record (same harness hash
`cac93ac6…`, same fingerprint `29de6089…`, own sha256 `892076fc696e583feaff312e1b330ede888ff1fd149bd11139bc4591ba680f51`,
differing from the executor's only through the `F3_REPO_ROOT` line); (2) the UNCHANGED harness,
launched in the copy, printed `PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = true` and
`DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS (… 31 verified …)`, passed NR-01(i)/(ii) and NR-SPL,
and wrote store units and logs ONLY inside the copy; the real repository was untouched. The
dry-check process was then STOPPED deliberately (SIGTERM) — the full-length computation was
intentionally not repeated (it is the auditor's step; a second ~12 h run by the same executor on
the same machine adds no audit evidence). The copy and kept-aside folder were deleted afterwards
(disposable, procedure §1). An earlier buffered launch of the same dry check (launch 1 in the
copy, ~110 s) was killed before Python flushed stdout, leaving an empty log in the copy; the
quoted evidence comes from the unbuffered launch-3 re-run in the same copy — both launches lived
only inside the now-deleted copy and touched nothing delivered.

```text
real_data_access = false throughout every attempt and the dry check
commit = false (separate PI instruction required)
```
