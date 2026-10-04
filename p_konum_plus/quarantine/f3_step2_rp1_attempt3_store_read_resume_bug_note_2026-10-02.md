# p_konum_plus — F3 real-data preparation rp1 — Attempt-3 Supersession Note (log-truncation disclosure + T-STORE-READ-ACCOUNTING resume-robustness bug)

```text
artifact_role = supersession note for rp1 attempt 3. Records TWO defects: (a) an
                executor process error that destroyed part of a launch log (a
                disclosure, not a code fix), and (b) a genuine logic bug in the
                T-STORE-READ-ACCOUNTING self-check's resume invariant, its fix, and
                the whole-store quarantine the harness change requires.
                RENAMES/MOVES nothing outside rp1's own attempt artifacts.
status        = NON-NORMATIVE
date          = 2026-10-02
revision      = rp1 (F3 real-data preparation cycle, inside the r4 lineage)
```

## 1. What attempt 3 did

rp1 attempt 3 (harness `d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d`)
began under `F3_RP1_LAUNCH=3`. The process was genuinely interrupted during the
SPL phase at ctx 20 (D-3 §8.2 interruption handling applies). The executor then
resumed the SAME attempt — correctly, per D-3 §8.2, reusing the same harness
bytes and store — but made a process error in doing so (§2), and the resumed
sub-process then hit a genuine code defect in its own self-check (§3).

## 2. Defect (a) — launch-log truncation (executor process error, disclosed)

The resume was started with the SAME `F3_RP1_LAUNCH=3` value and the SAME
`>` stdout/stderr redirect targets
(`f3_step2_rp1_launch3_stdout_2026-10-02.log` /
`..._stderr_2026-10-02.log`) as the interrupted process. `>` truncates on
open, so the interrupted process's partial console output (ctx 1-20) was
destroyed the moment the resumed process's redirect opened the same files.
Per D-3 §8.1-8.3 / R41A-02(b)-(c), each LAUNCH's console text must be
preserved and never overwritten; a resume must use a NEW launch number and
non-colliding log targets. This did not happen here.

**What survives.** The interrupted process's *computational* provenance is
not lost: every unit it wrote before the interruption is present in the
restart store with its own `pid`/`start_iso` in the store manifest, which is
how the resumed process's cache hits are provable. Only the interrupted
process's own console text for ctx 1-20 is unrecoverable. This mirrors the
r4-2 attempt-2/launch-1 precedent (lost console text disclosed, store
manifest provenance intact) and is disclosed here on that same basis — not
hidden, not minimized.

**Scope.** This is a logging/provenance-completeness defect, not a
scientific one. It does not touch any evaluation, stop, canonical document,
residual series, or determinism result.

## 3. Defect (b) — T-STORE-READ-ACCOUNTING resume-robustness bug (genuine code defect)

After the resume, the SAME sub-process raised `AssertionError` at its own
`T-STORE-READ-ACCOUNTING` self-check. The test's original invariant assumed
`fit1` (the first of two identical `fit_spline` calls under
`KEY_SCOPE="tstoreread__"`) always computes fresh (0 store reads), so that
`fit2`'s 146 reads could be attributed unambiguously to `fit1`'s writes. On
a resume, `fit1` itself became a cache hit: because `T-STORE-READ-ACCOUNTING`
runs early (before the ctx-20 interruption point), the interrupted process
had already computed and cached all 146 `tstoreread__`-scoped `splmode`
units in its own earlier pass. The resumed process's `fit1` therefore read
146 units from the store instead of writing them, and `fit2` then read the
SAME 146 — the underlying read/write accounting was completely correct
(`fine_counter = 292` = 146 + 146), but the test's pass condition required
`served_to_fit2 == T_modes and fit1_reads == 0`, which the resume
correctly fails.

**Root cause.** The test conflated two separate claims: (i) "fit2 is served
every mode from the store" (the actual property under test — resume
correctness), and (ii) "fit1 computed those modes fresh in this process"
(an artifact of attempt ordering, not a correctness requirement). Claim (ii)
is false on a legitimate resume and was never meant to gate pass/fail.

**Scope.** This is a bug in the CHECK itself, not in any computation it
checks. `s_findings` evidence from attempts 1-2 already established the
scientific content is unaffected; this defect never reached a results file
(the resumed process stopped before writing one).

## 4. Fix (attempt 4 harness)

`t_store_read_accounting` now computes `pass_` from
`served == T_modes and fine >= served and rows_ok and same_result` only —
dropping the `fit1_reads == 0` requirement entirely. `fit1_reads` and the
new field `resumed_warm_start = (fit1_reads > 0)` are still computed and
returned for diagnostic visibility, but no longer gate the pass/fail
verdict. This holds under both a cold start (fit1 writes, matching every
prior passing run) and a warm start (fit1 reads, matching attempt 3's
actual observed numbers: `fit1_reads=146`, `served_to_fit2=146`,
`fine_counter=292`) — verified by hand-tracing both arithmetic paths against
the respective passing and failing runs' logged numbers.

## 5. Whole-store quarantine (harness-change invariant)

Changing the harness changes its sha256 and therefore the
`code_env_fingerprint` that keys the restart store. Per the standing
"quarantine-whole-on-harness-change" rule, attempt 3's store and its launch
logs are quarantined in full and attempt 4 starts from an EMPTY store.

| quarantined artifact | what it is |
|---|---|
| `f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py` | attempt-3 harness bytes (sha256 `d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d`; recovered by reverting only the `t_store_read_accounting` fix above and verified byte-exact against the W-3 custody hash) |
| `rp1_restart_store_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG/` | attempt-3 restart store, 4,449 units, fingerprint `9cba3c77c85d5885` (the merged state of the interrupted-then-resumed sub-processes) |
| `f3_step2_rp1_launch3_stdout_2026-10-02.log` / `..._stderr_...log` | attempt-3's launch-3 logs; contain ONLY the resumed sub-process's console output (ctx 1-20 lost per §2 above) |

## 6. Response — attempt 4 (D-3 §8.3)

```text
harness attempt 4        = t_store_read_accounting resume-robustness fix only
RESTART_LAYER_ACTIVE     = True (unchanged; T-RP-1 = ACTIVE_FROM_START applies to
                           every attempt of this cycle)
ATTEMPT_NUMBER           = 4
supersedes_harness_sha256 = d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d
supersedes_custody_sha256 = 239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a
supersedes_note_path      = this note
```

A fresh W-3 custody record (written outside the run process) names the
attempt-4 harness/generator/manifest hashes and the new fingerprint before
attempt 4 runs. Attempt 4 MUST use a launch number not previously used in
this cycle (i.e. 4), with its own non-colliding log file targets, so that
no prior launch's console text can be overwritten. No r3, r4, r4-1, r4-2,
or pre-existing quarantine file is modified, renamed or moved.

```text
deliverable_affected = NONE (attempt 3 wrote no results.json)
real_data_access = false
commit = false
```
