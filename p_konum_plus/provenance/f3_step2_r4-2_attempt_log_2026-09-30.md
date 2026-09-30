# p_konum_plus — F3 STEP-2 r4-2 — Attempt Log (deliverable 12)

```text
artifact_role = attempt log required by T-R2-2 = AUTHORIZE_RESTART (D-3 §8.3) and
                T-RESTART-PROVENANCE; carries ERRATUM-3 (R41A-05)
status        = NON-NORMATIVE (a disclosure record; the hashed results/custody files are authoritative)
date          = 2026-09-30
revision      = r4-2 (second correction revision inside the r4 cycle)
```

Counters: **attempt** increments only on a harness byte change; **launch** is every
`python ...` invocation. R41A-02 applies from the first write of this revision:

- **(a) one custody record per attempt**, the attempt number in the file name
  (`provenance/f3_step2_r4-2_preexecution_custody_attempt<k>_2026-09-30.md`), written
  outside the run process, never overwritten — the external writer refuses an existing
  path. From attempt 2 on, `supersedes_custody_sha256` carries the superseded record's hash.
- **(b) bytes before edits**: no harness is edited in place while it is the named bytes of
  a custody record; the copy is taken to quarantine first and its hash must equal the hash
  that record names. No reconstruction is used or accepted this revision.
- **(c) one log pair per launch**, launch-numbered
  (`f3_step2_r4-2_launch<n>_stdout_2026-09-30.log` / `..._stderr_...`), never overwritten.

The generator `68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830` and the
manifest `5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe` are REUSED
UNCHANGED from r4-1 (instruction §5 items 2–3): named by path and hash in the custody
record, regenerated in memory and verified equal by both the W-3 writer and `main()`, and
never rewritten. Only the harness hash varies across attempts. Every process ran with
`real_data_access = false`.

## Attempt 1 — harness 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74 (restart layer OFF)

Custody record: `f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md`
(`ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e`),
`code_env_fingerprint = 0f32c7911cf8fccb`, `supersedes_harness_sha256 = None`,
`supersedes_custody_sha256 = None` (attempt 1 supersedes nothing within this revision).

| # | launch logs | pid | start | end/stop | outcome |
|---|---|---|---|---|---|
| 1 | launch1_stdout / launch1_stderr (5d58afbb… / d688ac98…) | 14804 | 2026-09-30 (evening) | (ctx 13) | **interrupted** externally (no error; host process exited between session turns) at `PROGRESS SPL ctx 13 SCEN-A run1:F0:fold1`. All preconditions/gates PASS in-run, incl. 15 instruments, manifest-reuse equality and T-SPL-PENDING-REALPATH 9/9. No results; NO store unit (layer off — correct §8.1 behaviour). Note: `quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md`. **R41A-02(b) applied AT the transition: bytes copied to quarantine BEFORE the edit; copy hash == custody-named hash (9e4d2803…) — preserved bytes, not a reconstruction.** |

## Attempt 2 — harness b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 (restart layer ON, store empty)

Custody record: `f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md`
(`766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1`),
`code_env_fingerprint = 4ced291f15fb5afd`,
`supersedes_harness_sha256 = 9e4d2803…`,
**`supersedes_custody_sha256 = ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e`**
(R41A-02(a): the field r4-1 could never fill, filled here because per-attempt names
preserved the superseded record). The attempt-1 record stays on disk, untouched.
Engineering refinement at this attempt, disclosed: LAUNCH_NUMBER moved from a source
constant to the environment variable `F3_R42_LAUNCH`, because a resumed launch of one
attempt must not change the harness bytes (a source constant would have changed the
fingerprint and orphaned the attempt's own store units); `main()` refuses to run without it.

| # | launch logs | pid | start | end | outcome |
|---|---|---|---|---|---|
| 2 | launch2_stdout / launch2_stderr (3af46762… / df257d12…) | 10412 | 2026-09-30T20:38:58 | 21:36:01, **exit 0** | **COMPLETED, VERIFIED**: `DETERMINISM = True` (RUN1 == RUN2 == `556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77` — exactly the r4-1 value, as the instruction expected); residual series `3ee624f3…` byte-identical to r4-1/r4/r3; `T-EXPECT-ALL 36/36`; **30/30 recorded tests passed**, incl. the two new mandatory ones — `T-SPL-PENDING-REALPATH` (9/9 cases, stubs restored, no routed cell carries a verdict) and `T-NONREG-R4-1` (**37 objects compared, 0 findings, stops equal, no whitelist**); `T-NONREG-R4` findings=0; NATURAL_UNRELATED_EVENTS = 0; COVERAGE_DERIVED 64 rows, downgraded = []; `end_state.PI_dispatch_record_hash = a3e70509…` (D-7 as observed; D-5 in its own field — R41A-03). Results `f2a0a4d5…`. **This is the current, final state of the r4-2 revision.** |

## Single-process statement and T-RESTART-PROVENANCE (D-3 §8.3)

Although the restart layer was ACTIVE for attempt 2, launch 2 ran uninterrupted and
**one process (pid 10412) computed every object of deliverables 5–8**: the store manifest's
11,869 rows all carry pid 10412, and the per-call telemetry's phase/pid split is entirely
`nr_gates/10412 = 60, unit_tests/10412 = 1602, run1/10412 = 5256, run2/10412 = 5256`
(launch 1 wrote no store unit — the layer was off — and no result object). Launch 2 read
zero units from the store (`units_read_from_store` all 0). **T-SINGLE-PROCESS therefore
applies and holds**; T-RESTART-PROVENANCE is not needed in its place, and its three
conditions hold anyway (fingerprint-keyed store `4ced291f…`, disjoint RUN1/RUN2 namespaces,
every contributing process in this table). Progress rule (§8.3): launches 1 → 2 both
completed new work; the STOP condition never arose.

## ERRATUM-3 (R41A-05) — the r3 attempt log's rows 6–8 versus the revision-4 custody record

This erratum adds point (d) that ERRATUM-2 (r4-1 attempt log) did not state, and names the
two references A-4 asks for. **The r3, r4 and r4-1 logs are historical and are NOT
modified**; this is the record of the correction.

### References

1. **The record corrected**: the r3 attempt log
   `p_konum_plus/provenance/f3_step2_r3_attempt_log_2026-09-22.md`, sha256
   `253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5` (re-verified on the
   repository copy, 2026-09-30).
2. **The statement corrected**: item 3 of the erratum in the r4 attempt log
   (`f3_step2_r4_attempt_log_2026-09-24.md`, `8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69`),
   which says the r3 final store's foreign entries stand under prefix `548ae790f6ac756a`,
   **"matching no combination named in any r3 file"**. That is incorrect: the prefix is
   exactly the fingerprint of a triple an r3 file does name (see (d) below). ERRATUM-2 of
   the r4-1 attempt log already identified `548ae790…` as the ATTEMPT8 custody triple's
   fingerprint but did not state the row-6–8 conflict or correct this wording.

### (d) The conflict, stated

```text
the r3 attempt log, rows 6, 7, 8   : "revision 4 (f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5,
                                      P-1..P-7 corrections)" -- rows 7 and 8 read "same bytes as #6"
the custody record filed under the ATTEMPT8 quarantine label
  (f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md,
   sha256 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657) states:
     attempt_number       = 4
     harness_sha256       = 390f42b72971030033c6964731d699358a1547bf9093b8e949c0e338e6bc0336
     generator_sha256     = cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8
     manifest_sha256      = 9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a
     code_env_fingerprint = 548ae790f6ac756a
```

Both records describe **revision 4** and they name **different harness bytes**
(`f882b922…` vs `390f42b7…`). Exactly one of them can be right about the bytes that ran.

### What the records support about the bytes that ran attempts 6–8

Three observations, computed on the delivered files on 2026-09-30, then the inferences they
license — **each inference is marked as an inference, not as a finding**.

**Observation 1 (recomputed here).** With the r3 environment the custody records state
(python 3.11.7, numpy 1.26.4, scipy 1.14.1, Windows-10-10.0.19045-SP0, threads = 1), the
fingerprint of each candidate triple is:

| harness | generator / manifest | fingerprint |
|---|---|---|
| 5fea165c… (r3 FINAL) | cc23c9b5… / 9c944543… | **1ba561daefb48b2e** |
| 390f42b7… (ATTEMPT8 custody) | cc23c9b5… / 9c944543… | **548ae790f6ac756a** |
| f882b922… (rows 6–8) | cc23c9b5… / 9c944543… | e3ccc7d133c9ff2f |
| f882b922… (rows 6–8) | e35c2bf0… / 4544ff75… | 9bb07bae05cdeb5e |
| 390f42b7… | e35c2bf0… / 4544ff75… | e965ecee77046155 |
| 5fea165c… | e35c2bf0… / 4544ff75… | f399c3d0b0398816 |

**Observation 2 (counted here).** The quarantined r3 FINAL store
(`quarantine/r3_restart_store_2026-09-22_FINAL_T-R3-2/`) holds units under **exactly two**
prefixes, and no others: `1ba561daefb48b2e` (11,723 units) and `548ae790f6ac756a`
(11,723 units). No unit stands under `e3ccc7d1…` or `9bb07bae…` — that is, under **no**
fingerprint that pairs `f882b922…` with either generator/manifest pair any r3 file names.

**Observation 3 (quoted).** The attempt-8 quarantine note
(`f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md`) states that attempt 8
"resumed from the restart store" and that "RUN1's real-scenario fixtures were already cached
from attempt 6".

**Inference A (inference, not a finding).** Since attempt 8 resumed from units attempt 6 had
cached, attempts 6 and 8 must have read the same fingerprint, hence the same
(harness, generator, manifest, environment) identity. Combined with Observation 2, the only
non-final identity with units in the store is `548ae790…` = the `390f42b7…` triple.
It follows — *as an inference from the store keys and the note, not from a preserved
execution record* — that the bytes that computed the non-final units, and therefore ran
attempts 6 and 8, were **`390f42b7…`**, and that the r3 attempt log's rows 6–8 name the
wrong harness.

**Inference B (inference, not a finding).** The r4 erratum's item 3 wording ("matching no
combination named in any r3 file") is **incorrect as written**: `548ae790…` matches the
triple named by the ATTEMPT8-labelled custody record `2e55e150…`. The correct statement is
that the prefix matches no combination named **in the r3 attempt log**, which is the record
that conflicts with it.

**What remains unprovable.** `390f42b7…` is NOT_PRESERVED (r4-1 ERRATUM-2 point 1; searched
again 2026-09-30 with the same result), so no byte-level check can confirm Inference A; it
rests on the store keys, the custody record and the attempt-8 note. `f882b922…` IS preserved
(it is the file under the ATTEMPT5 harness label) but has no units in any store, which is
consistent with it never having computed a stored unit — and also with it having run only
phases that write no store unit. Both readings are left open; neither is asserted.

**Scope of impact — none on any delivered output.** The r3 FINAL run executed under
`1ba561da…` (harness `5fea165c…`), r4 under `5ef61a41…`, r4-1 under `dc228827…` and r4-2
under `0f32c7911cf8fccb`; no unit under `548ae790…` was ever readable by any of them
(prefix mismatch by construction). This is a labelling/disclosure defect only, in records,
not in results.

```text
renames_or_moves of any r3 / r4 / r4-1 / quarantined file = NONE
real_data_access = false ; commit = false
```
