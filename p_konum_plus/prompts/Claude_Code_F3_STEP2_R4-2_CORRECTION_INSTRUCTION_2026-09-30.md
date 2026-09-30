# p_konum_plus — F3 STEP-2 r4-2 — Correction revision instruction (2026-09-30)

```text
instrument            = Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
instrument_class      = PI instruction for a second correction revision INSIDE the r4 cycle (tag r4-2). It is a
                        NARROW child of the r4-1 instruction (283ac4e2…), which stays in force unchanged together
                        with the r4 instruction, D-3, D-1 and D-2. This file only (a) adopts the closure actions of
                        the r4-1 independent audit (A-4) for the six cleanup findings the PI selected, and (b) states
                        the r4-2 deliverables. Where this file is silent, the r4-1 instruction (and through it the r4
                        instruction, D-3 and v6) governs. No new S / T decision is made or needed
drafted_by            = Claude (Cowork session; configured model identifier claude-opus-5-5) at the PI's request;
                        the same session drafted D-3 and the r4 and r4-1 instructions, filled D-4 … D-7 at the PI's
                        instruction and wrote the r3, r4 and r4-1 audits. Prior exposure is disclosed; the auditor
                        of the r4-2 package will state it again
binding instruments   = r4-1 instruction  Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md
                                          283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330 (unchanged)
                        r4 instruction    Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md
                                          e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 (unchanged)
                        D-3  Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
                             5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 (unchanged)
                        D-1  Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
                             17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 (unchanged)
                        D-2  f3_step2_pi_ratified_content_2026-09-07.md
                             da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 (unchanged)
                        D-5  f3_step2_r4_pi_dispatch_record_2026-09-24.md
                             0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 (unchanged; S-R2-1 =
                             PI_RULE and its rule text; the PI_RATIFIED tag keeps citing D-5)
                        D-6  f3_step2_r4-1_pi_dispatch_record_2026-09-29.md
                             a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0 (unchanged; parent of D-7)
                        D-7  f3_step2_r4-2_pi_dispatch_record_2026-09-30.md — the r4-2 dispatch record (child of
                             D-6); it names this file by hash; its own hash stands in its .sha256 sidecar
                        this file
inputs, not directives = A-4  f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md
                             ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82
                        (its findings are adopted as listed in §3; the record decides nothing and is not rewritten).
                        Advisory notes and external AI reviews are not inputs
frozen upstream       = untouched: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (as ratified by freeze record r1).
                        No new scientific literal. No real SSA data. No 6B. No QUALIFIED
non-retroactivity     = the r4-1 package as audited (harness 4e0dc8cf…, generator 68d126cf…, manifest 5c09c4f0…,
                        custody 3bc4e578…, results 6dd4185b…, test evidence f74dccf0…, register 45a10494…, report
                        e7939a22…, inventory fedd964a…, attempt log ee5b4862…, transmission list 31b27c28…,
                        supplement 0b3f4358…), the r4 package, every r3 file and every quarantined file are historical
                        and read-only. Nothing is overwritten, renamed or moved; every r4-2 deliverable is a new file
                        with the r4-2 tag, except the generator and the manifest, which are reused unchanged (§5)
```

## 1. Preconditions

Before writing anything: verify by SHA256 that the r4-1 instruction, the r4 instruction, D-3, D-1, D-2, D-5, D-6,
D-7, A-4 and this file are the bytes named above and in D-7 (this file's hash stands in D-7 §1; D-7's hash stands
in its sidecar), and that the r4-1 package files named under non-retroactivity still have the hashes printed
there. Any mismatch, blank or template residue: STOP before the first computation (D-3 §3). A missing sidecar of a
repository file is recorded and created; it is not a STOP.

## 2. Scope chosen by the PI (D-7 §3)

```text
in scope      R41A-01, R41A-02, R41A-03, R41A-04, R41A-05, R41A-06 (cleanup)
not in scope  R41A-08 (optional; not applied)
              R41A-07, R41A-09, R41A-10, R41A-11 (informational; no action)
              the PI's decisions on the narrowed evidence of T-R2-2 and on the uncovered row
              "A.5 (iii) inadmissible refit" — not part of this revision; nothing here changes them
```

## 3. Corrections (X)

Each closure action is quoted from A-4 §4 and is the instruction; the lines after "→" state how it is to be
evidenced. Every correction is evidenced by a test that RAN and PASSED or by a delivered file; a correction
reported as applied without such evidence counts as not applied (D-3 §10, v6 §13).

```text
R41A-01  "drop the TEST_ONLY clause in the three flag assignments, take the routing tag from the event's own
         failure string, and add one real-path test with an injected UNRELATED event (the stub technique of §5.2
         suffices)"
         → (a) behaviour: on the real path, a spline context (full, fold, probe) whose fit returns
               STOP_EXACTNESS_PENDING(<tag>) sets that context's pending flag whatever <tag> is; the declared
               spline-failure injection (failure TEST_ONLY_INJECTION_SPLINE_FAILURE) stays an ordinary failure,
               so D-5's SCEN-B pin is unchanged
           (b) tag: a routed criterion carries the tag of the event that set the flag — F3-STEP2-EXACT-04 for a
               natural event, TEST_ONLY_INJECTED for an injected one; if a sex has both kinds for the criteria
               it routes, F3-STEP2-EXACT-04 is used (a natural event is never masked); the decision-layer
               fixtures keep TEST_ONLY_INJECTED; the finding machinery is unchanged (a natural event opens
               F3-STEP2-EXACT-04; an injected one is not entered, D-3 Y-04 (b))
           (c) test: a new mandatory unit test T-SPL-PENDING-REALPATH calls the real run_real_scenario and
               evaluate_fixture on a REAL_SCENARIOS trajectory with fit_family and fit_spline replaced by
               TEST_ONLY stubs (the technique of A-4 §5.2). Cases, each with its expected outcome written in the
               test before the run: baseline → no pending cell; a natural event in full, fold and probe → the
               dependent criteria (full → C3, C4b; fold → C2; probe → C4b) of that sex are
               STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04) for both families; the same three injected →
               STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED), no definite outcome; the declared spline-failure
               injection → an ordinary failure, no pending cell; a natural and an injected event in the same
               sex → F3-STEP2-EXACT-04. The stubs are installed for this test only and restored by reassignment,
               restoration asserted (D-3 Y-04 (d)); every global the test touches (FIDELITY lists, telemetry,
               EXC_CAPTURES, progress counters) is snapshotted and restored, equality asserted; a register row
               (SUMMARY) discloses the stubs
           (d) non-regression against r4-1 (results 6dd4185b…): a new check T-NONREG-R4-1 compares every one of
               the 37 evaluation objects and every stop record in canon() form with sorted keys; any difference
               is reported per fixture and is a finding; there is no whitelist. T-NONREG-R4 (against r4) stays as
               it is. Because evaluations and stops must not change, the RUN1 canonical document is expected to
               stay 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 and the residual series
               3ee624f3…; a different value is reported with its per-fixture difference, never absorbed
R41A-02  "from the next cycle: one custody file per attempt (attempt-numbered name) with SUPERSEDES_CUSTODY_SHA256
         filled; copy the harness to quarantine before the first edit; one log file pair per launch"
         → applied from the first write of r4-2:
           (a) custody: the W-3 record of attempt k is written to an attempt-numbered path
               (provenance/f3_step2_r4-2_preexecution_custody_attempt<k>_<date>.md); CUSTODY_PATH in the harness
               follows ATTEMPT_NUMBER; no custody file is ever overwritten; from attempt 2 on,
               SUPERSEDES_CUSTODY_SHA256 in the harness and supersedes_custody_sha256 in the new custody record
               carry the hash of the superseded attempt's custody record
           (b) bytes: before the first edit of a superseded harness, its bytes are copied to quarantine and hashed;
               the copy's hash equals the harness hash its custody record names (a reconstruction is not needed
               and not accepted)
           (c) logs: every launch writes its own stdout / stderr pair with launch-numbered names
               (…_r4-2_launch<n>_stdout_<date>.log / …_stderr_…); no log file is ever overwritten
           If the run completes in one attempt and one launch, (a)–(c) hold trivially and the report says so
R41A-03  "the next revision's end state names its own dispatch record"
         → end_state.PI_dispatch_record_hash = the hash of D-7 as observed; the S-R2-1 source (D-5, 0cd87ad5…) is
           written in a separate field of its own, never in PI_dispatch_record_hash; an assertion in the harness
           checks that the value written equals the observed D-7 hash
R41A-04  "print the three hashes"
         → the r4-2 report's hash block prints the hash of every r4-2 deliverable except the report itself (whose
           hash stands only in its sidecar and in the transmission list); in addition it prints, as the correction
           of the r4-1 report (which stays unmodified), the three r4-1 hashes A-4 names: register
           45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671, start-state inventory
           fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2, attempt log
           ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739
R41A-05  "add (d) and the two references in the next record child"
         → ERRATUM-3 in the r4-2 attempt log (the r3, r4 and r4-1 logs stay untouched), with each point's source:
           (d) the r3 attempt log (253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5) names,
               in rows 6–8, revision 4 = f882b922…, while the revision-4 custody record (filed under the
               ATTEMPT8 label, 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657,
               attempt_number = 4) names harness 390f42b7…; state what the records support about the bytes that
               ran attempts 6–8 (the attempt-8 note's resume from units attempt 6 had cached; 548ae790… as the
               only non-final prefix of the r3 final store and the fingerprint of the 390f42b7 triple; no store
               unit under a fingerprint of f882b922… with any generator / manifest pair named in r3), marking
               every inference as an inference
           references: the r3 attempt log hash above, and item 3 of the r4 log's erratum named as the statement
               corrected ("matching no combination named in any r3 file")
R41A-06  "correct the two descriptions; state that the record's sex is the first hit's"
         → the r4-2 report and register describe the INJ-U-POST-CONSTRUCTION-INVALID stop record as delivered:
           two offending pairs, (F, P01, 0) and (M, P01, 0); the record-level sex field is the sex of the first hit
           (F). The r4-1 report and register stay unmodified; the code that builds the record does not change
```

## 4. Run rules and the store

As the r4-1 instruction §4 and D-3 §8, with R41A-02 applied: one process from the beginning first; the restart
layer only after an interruption and only as D-3 §8.3 says (T-R2-2 as read in D-5). The harness changes, so the
fingerprint changes and no r4-1 unit can be read; the r4-2 store starts empty in a directory of its own (tag
r4-2). The r4-1 and r4 stores stay where they are, untouched — nothing is moved (this settles the r4-1
instruction's §4 / §7 conflict, A-4 R41A-07, in favour of §7). W-3 custody record once per attempt, written
outside the run process, with observed values.

## 5. Deliverables (every file with an external .sha256 sidecar; no self-hash)

```text
D-3 §9 items 1–12 with "r4-2" in every name and path, with these specifics:
 1  harness r4-2 (new)
 2  generator — REUSED unchanged: the r4-1 generator (68d126cf…) is named by path and hash in the custody
    records; no r4-2 copy is made
 3  manifest — REUSED unchanged: the r4-1 manifest (5c09c4f0…); regenerated in memory and verified equal
 4  custody records, one per attempt (R41A-02 (a)); deliverable 4 is the record of the attempt whose run produced
    the final output
 5–8 telemetry, results, residual series, test evidence (with the T-SPL-PENDING-REALPATH and T-NONREG-R4-1
    records)
 9  register — child of the r4-1 register (45a10494…), with the SUMMARY row of R41A-01 (c) and the corrected
    description of R41A-06
 10 correction report — hash block as R41A-04; response table as §6
 11 start-state inventory, taken before the first r4-2 write
 12 attempt log — with ERRATUM-3 (R41A-05)
and in addition:
 A  f3_step2_spline_percall_telemetry_r4-2_<date>.csv (all phases, all pids)
 B  f3_step2_r4-2_restart_store_manifest_<date>.csv, if a store was used
 C  every capture record and the RUN1 / RUN2 capture comparison
 D  the non-regression comparison with r4-1 (R41A-01 (d)) as a CSV
 E  every quarantine copy and note of this revision (R41A-02 (b)); every launch's stdout / stderr pair
    (R41A-02 (c))
 F  f3_step2_r4-2_transmission_list_<date>.md: every file above and every sidecar, with SHA256
 G  for transport only: the whole auditor folder also as ONE zip file (its hash in the chat message is enough);
    the auditor verifies every file inside against its own sidecar
```

## 6. Report and end state

The six status fields computed from the run; a response table with one row per R41A item in scope (PASS / FAIL /
NOT_RUN(reason) / STOP, with test id or file and hash); the end-state block of D-3 §10 with PI_dispatch_record_hash
= the hash of D-7 as observed and S-R2-1 = PI_RULE with its source (D-5) in its own field; expectation_checks =
<ran> / <declared> (36 / 36 expected, the manifest being unchanged); the non-regression result against r4-1 and
against r4; parents_unchanged with the re-hash values of the r4-1 and r4 packages. Expected end status:
PARTIAL_PENDING_PI (T-R2-2 in narrowed_evidence; the coverage row "A.5 (iii) inadmissible refit" uncovered) — no
other status is claimed; QUALIFIED is not declared by anyone.

## 7. Not in scope

Anything not named here, in the r4-1 instruction, the r4 instruction, D-3 or D-5: no redesign, no new manifest
fixture (T-SPL-PENDING-REALPATH is a unit test, not a fixture), no change to the generator, the manifest or any
expected_* value, no change to any frozen or ratified text or to S-R2-1, no rewriting, renaming or moving of r3 /
r4 / r4-1 / quarantined files or of any audit record, no real SSA data, no algorithm × CVI results, no 6B, no
R41A-08.
