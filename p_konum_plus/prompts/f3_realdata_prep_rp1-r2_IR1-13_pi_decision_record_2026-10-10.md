# p_konum_plus — rp1-r2 — PI decision record on IR1-13 (D-14) — 2026-10-10

> Child of D-13. Governed by D-11 r1 §5–§6 and Ek-1 r1. Prepared by Claude (Claude Code cloud session) at the
> PI's request. The record is the PI's. It carries no hash of itself.
> **Signed by the PI's approval of 2026-10-10 (§5).**

```text
record                = f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md   (D-14)
draft                 = f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_DRAFT_2026-10-10.md
                        fb9eb58885d6c25a1ab9de7f86f15e7c08ec09b69893aecbb2db4b36fa9595c2
status                = SIGNED (PI approval, 2026-10-10; §5)
parent                = D-13 f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md  6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f
subject               = IR1-13 (rp1-r1 independent audit f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913): the 9 h 44 m
                        "standalone pre-verification" of 2026-10-05 21:41 → 2026-10-06 07:25 (rp1-r1 attempt log
                        L85, ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b) lacks its code hash, launch / custody record and output-segregation
                        evidence. B by D-13 PI-a. rp1-r2 instruction §5 (a) stopped the launch pending this record
what_this_record_is_not = not a closure of IR1-13; not a binding; not QUALIFIED; not a real-data authorization
```

## 1. Decision

```text
IR1-13   = RECORDED_LIMITATION (D-11 r1 §6)
effect   = the rp1-r2 launch gate of instruction §5 (a) is released: the executor may start attempt 1 once every
           other precondition holds. IR1-13 is NOT closed: it stays in the ledger as OPEN / B, recorded limitation
           of the rp1-r1 record, naming this record. Under rp1-r2 instruction §8 the executor's status remains
           PARTIAL_PENDING_PI with this record named; under §9 the rp1-r2 pass criterion accepts this record for
           IR1-13
scope    = the limitation concerns the rp1-r1 historical record only. It does not extend to rp1-r2, whose own
           executions fall under instruction §5 (b)
```

## 2. Reasons

```text
(1) partial evidence was found: a test script that loads the rp1-r1 harness by path and calls the loader,
    handoff and context tests, with its stdout, stderr and an exit record (EXIT=0). Executor-reported; hashes in
    the executor's intake evidence f3_realdata_prep_rp1-r2_intake_verification_2026-10-10.json (SHA256 reported
    by the executor as ef4a2ebf4d41bc85e755e35fac3f6060973fdcac748ce503266d01f50bd78721; not verified by the
    drafter, the file is not in the repository)
(2) the rp1-r1 attempt-2 store manifest (f64e0aa9344f7b2187d91a113cdc83c0f006bfd288fef8f86060ce9ab3f39da5) lists 67,313 units, every one with writer pid 34588
    and process start 2026-10-07T14:51:58.715047, i.e. after the standalone window; the store-read log
    (92b3af34f8c63347f839a7c0f1826e1bb566072cb25d40da17ad3bbd55939d7d) has 730 rows, writer and reader pid 34588 in every row. This is a record written by
    the harness, not a reading of the physical store files
(3) the rp1-r1 independent audit re-ran the unchanged harness in a separate root from an empty store, in an
    environment matching the binding one field by field, and reproduced every S object (37 objects, RUN1 = RUN2 =
    556106e7…, residual 3ee624f3…) and the non-regression classes row by row
(4) neither the rp1 nor the rp1-r1 bytes are bound (D-13 §4); IR1-13 cannot reach a binding
(5) rp1-r2 starts with a new harness and an empty store tagged rp1-r2, and instruction §5 (b) requires every
    execution of the harness, a copy or an excerpt to be logged
residual = the hash of the harness that ran in the standalone window is NOT OBSERVED and stays so
```

## 3. Related disclosure (no decision needed)

The rp1-r2 instruction and D-13 were first handed by mistake to the rp1-r1 auditor session, which wrote an rp1-r2
draft in `G:\PycharmProjects\rp1r1_audit\repo`. The executor did not use it and wrote its own code in
`pkp-worktree`; the disclosure is in the rp1-r2 attempt log (executor-reported). Consequence: that auditor
session does not audit rp1-r2; a new auditor session in a new directory does.

## 4. To the executor

```text
1. Place this record, signed, with its sidecar, in p_konum_plus/prompts/ unchanged; verify its hash against the
   sidecar and the value in the PI's message; stop if they differ
2. Record in the attempt log: IR1-13 = RECORDED_LIMITATION by D-14 (its SHA256); the ledger row of IR1-13 stays
   OPEN / B and names D-14
3. If the harness carries a launch authorization for IR1-13, it is set from this record (its SHA256), not from a
   free-standing flag
4. Then proceed under the rp1-r2 instruction. Before the full launch, the new tests may be run on small inputs
   as §5 (b) logged executions, outputs kept out of every deliverable and attempt store. Commit only on the PI's
   separate instruction
```

## 5. Signature

```text
PI                    = Öner
decision              = IR1-13 RECORDED_LIMITATION (§1)
signature / approval  = APPROVED. The PI's message of 2026-10-10, verbatim:
                        «D-14'ü onaylıyorum»
                        The approved content is the DRAFT named in the header; this final text differs from it only
                        in the title, the header lines and §5 (§7). This final text was delivered to the PI; the PI's
                        forwarding it to the executor adopts it
date_time_local       = 2026-10-10, UTC+3
```

## 6. Hashes (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
d9a5e9905e25c634ad3132aae85c6c346e5ead30	refs/heads/p_konum_plus
$ sha256sum <files; repository files from the git archive of 9035df0; each equal to its sidecar>
6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f  f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md (signed, as delivered)
f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913  f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md
ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b  provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md
f64e0aa9344f7b2187d91a113cdc83c0f006bfd288fef8f86060ce9ab3f39da5  calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv
92b3af34f8c63347f839a7c0f1826e1bb566072cb25d40da17ad3bbd55939d7d  calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv
```

## 7. Changes from the DRAFT (fb9eb588…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, header | DRAFT → signed; file name without DRAFT; draft and status lines | PI approval |
| 2 | §5 | approval message verbatim, date | PI approval |

No other change: §1 – §4 and §6 stand as in the DRAFT.
