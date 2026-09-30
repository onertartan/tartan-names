# p_konum_plus — F3 STEP-2 r4-1 — Correction revision instruction (2026-09-29)

```text
instrument            = Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md
instrument_class      = PI instruction for a correction revision INSIDE the r4 cycle (tag r4-1). It is a NARROW
                        child of the r4 instruction (e1283958…), which stays in force unchanged together with D-3,
                        D-1 and D-2. This file only (a) adopts the closure actions of the r4 independent audit
                        (DRAFT r1 and its child DRAFT r2) for the findings the PI selected, and (b) states the
                        r4-1 deliverables. Where this file is silent, the r4 instruction (and through it D-3 and
                        v6) governs. No new S / T decision is made or needed
drafted_by            = Claude (Cowork session; configured model identifier claude-opus-5-5) at the PI's request;
                        the same session drafted D-3 and the r4 instruction, filled D-4, D-5 and D-6 at the PI's
                        instruction and wrote the r3 and r4 audits. Prior exposure is disclosed; the auditor of
                        the r4-1 package will state it again
binding instruments   = r4 instruction  Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md
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
                        D-6  f3_step2_r4-1_pi_dispatch_record_2026-09-29.md — the r4-1 dispatch record (child of
                             D-5); it names this file by hash; its own hash stands in its .sha256 sidecar
                        this file
inputs, not directives = A-2  f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md
                             b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a
                        A-3  f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md
                             9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9
                        (their findings are adopted as listed in §3; the records decide nothing and are not
                        rewritten). Advisory notes and external AI reviews are not inputs
frozen upstream       = untouched: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (as ratified by freeze record r1).
                        No new scientific literal. No real SSA data. No 6B. No QUALIFIED
non-retroactivity     = the r4 package as audited (harness 54274b4e…, generator 39391730…, manifest c0b38ceb…,
                        results a15b7eff…, register 0eed314c…, report 5c9dea88…, attempt log 84090147…), every
                        r3 file and every quarantined file are historical and read-only. Nothing is overwritten,
                        renamed or moved; every r4-1 deliverable is a new file with the r4-1 name tag
```

## 1. Preconditions

Before writing anything: verify by SHA256 that the r4 instruction, D-3, D-1, D-2, D-5, D-6 and this file are the
bytes named above and in D-6 (this file's hash stands in D-6 §1; D-6's hash stands in its sidecar), and that
the r4 package files named under non-retroactivity still have the hashes printed there. Any mismatch, blank or
template residue: STOP before the first computation (D-3 §3). A missing sidecar of a repository file is recorded
and created; it is not a STOP.

## 2. Scope chosen by the PI (D-6 §3)

```text
in scope      R4A-01 (gate-specific blocker) ; R4A-02, R4A-03, R4A-04, R4A-10 (cleanup)
not in scope  R4A-08 (optional; not applied — corrections_complete keeps its r4 test-based computation)
              R4A-05 (closed by A-3) ; R4A-06, R4A-07, R4A-09 (informational; no action)
```

## 3. Corrections (X; blocker first)

Each closure action is quoted from A-2 §4 or A-3 §6 and is the instruction; the lines after "→" state how it is
to be evidenced. Every correction is evidenced by a test that RAN and PASSED or by a delivered file; a correction
reported as applied without such evidence counts as not applied (D-3 §10, v6 §13).

```text
R4A-01  "carry a per-trajectory, per-context pending flag into the decision grammar (as `a5v` is carried) for
        the spline full, fold and probe contexts; route every criterion that uses that context (C2, C3, C4a,
        C4b of that sex, and the D-P04 levels built on them) to STOP_EXACTNESS_PENDING(<id>); one
        decision-layer fixture with the flag set and an evaluation-level assertion added to
        T-EXC-UNRELATED-TYPE"
        → (a) propagation: a pending context propagates exactly as the A.5 reference violation (`a5v`,
              R3A-05) already propagates C4a / C4b PENDING — same criterion state, same stops-record shape, same
              effect on p03, D-P04 and the mechanism outcome. No new outcome grammar. If the existing grammar
              does not determine a case, record the ambiguity in the report and STOP for that item
          (b) the report lists, derived from the code, which criteria read each of the three spline contexts
              (full, fold, probe); the routing covers exactly those
          (c) <id>: F3-STEP2-EXACT-nn for a natural event (entered into exactness_findings / open_findings);
              TEST_ONLY_INJECTED for a manifest-declared injection (not entered) — D-3 Y-04 (b)
          (d) fixtures: decision-layer TEST_ONLY fixtures, manifest-declared, never inside SCEN-A / SCEN-B,
              that set the flag in each of the three contexts (one fixture with three sub-cases or three
              fixtures, executor's choice, disclosed). Their outcomes (criterion states, stops, mechanism) are
              predeclared in the manifest's expected_* columns BEFORE the run; a differing result is an
              EXPECTATION_FAIL, never a re-derivation
          (e) T-EXC-UNRELATED-TYPE additionally asserts at evaluation level that the dependent criteria of
              the injected context are PENDING and not PASS / FAIL
          (f) non-regression: for every fixture present in the r4 results (a15b7eff…), p03, every criterion
              outcome, the D-P04 block, the mechanism outcome and the stops are compared programmatically with
              r4; any difference is reported per fixture and is a finding. On the real path the flag is false
              everywhere unless a natural UNRELATED event occurs; the count is reported
R4A-02  "name fixture / test ids in the authored evidence texts and admit T-* test ids in the resolver"
        → the four rows of A-2 R4A-02 resolve from their evidence; any row still UNCOVERED is listed with the
          reason
R4A-03  "use the D-3 labels; de-duplicate the offending pairs and add the sex"
        → guarded comparator STOP = CONTRACT_VIOLATION_INCONSISTENT_U (D-3 Y-03 (iii)); the STOP label of an
          injected UNRELATED event = STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED) (D-3 Y-04 (b)); the
          INCONSISTENT_U stop record lists each (sex, fitter, observation) once. T-COMPARATOR-NAN asserts the
          new label
R4A-04  "author the inventory or record the PI-visible deviation; add the r3 per-revision triples; print the
        register and log hashes in the report"
        → (i) write provenance/f3_step2_r4-1_start_state_inventory_<date>.md (D-3 §9 item 11, W-1 (a)), taken
              before the first r4-1 write
          (ii) the r3 per-revision triples are taken from the custody records as observed bytes (harness,
              generator, manifest, recorded fingerprint, recomputed fingerprint), one row per custody record;
              where a triple conflicts with a log row or a quarantine label, say so (see R4A-10)
          (iii) every deliverable hash printed in the report's hash block (no "(sidecar)" placeholder)
R4A-10  "in the next r4 record child (the r3 files and the r4 log stay untouched): a second erratum stating
        (a)–(d); relabel or annotate the ATTEMPT5 and ATTEMPT8 quarantine files as bytes taken after the
        attempt, not the bytes run; either transmit d67e097d…, e35c2bf0… and 390f42b7… if the repository holds
        them, or record that they are not preserved and correct report §8 (c)"
        → (i) ERRATUM-2 in the r4-1 attempt log, addressed to the r3 attempt log (25316389…) and to item 3 of
              the r4 log's erratum: 548ae790f6ac756a is the fingerprint of the attempt-8 custody triple
              (390f42b7…, cc23c9b5…, 9c944543…); the ATTEMPT8 harness 99f895c1… and the ATTEMPT5 harness /
              generator f882b922… / cc23c9b5… are not the bytes their custody records name; the r3 log's
              "revision 4 = f882b922…" conflicts with the revision-4 custody record — each point with its source
          (ii) annotate, do not rename: write quarantine/f3_step2_r3_quarantine_label_annotation_<date>.md
              naming each affected quarantined file, its hash, what its label says and what the bytes are
          (iii) search the repository and quarantine for files with the hashes
              d67e097dc158c4909276b026ce66533f33dfab7a94d800e57342eb86e76f58ff (r3 attempt-5 harness),
              e35c2bf06ee4087bac97bd5b6e81d35d079ff1dddf8d2e68555c6c7d18859638 (r3 attempts 1–5 generator),
              390f42b72971030033c6964731d699358a1547bf9093b8e949c0e338e6bc0336 (r3 attempt-8 harness);
              transmit each one found; for each one not found write
              NOT_PRESERVED; correct the r4 report §8 (c) statement in the r4-1 report
```

## 4. Run rules and the store

As the r4 instruction §5 and D-3 §8: one process from the beginning first; the restart layer only after an
interruption and only as D-3 §8.3 says (T-R2-2 as read in D-5). The harness changes, so the fingerprint changes
and the r4 store cannot be read; start the r4-1 store empty and quarantine the r4 store directory whole (listed,
not deleted). W-3 custody record once per harness revision, written outside the run process, with observed
values. Every aborted attempt: quarantine note, bytes as they ran (copy BEFORE any edit), custody record.

## 5. Deliverables (r4 instruction §6 with the tag r4-1; every file with an external .sha256 sidecar; no self-hash)

```text
D-3 §9 items 1–12 with "r4-1" in every name and path — harness, generator, manifest, custody record, telemetry,
results, residual series, test evidence, register (child of the r4 register 0eed314c…, with a SUMMARY row for
the R4A-01 routing and the changed labels), correction report, start-state inventory (R4A-04), attempt log
(with ERRATUM-2, R4A-10) — and in addition:
 A  f3_step2_spline_percall_telemetry_r4-1_<date>.csv (all phases, all pids)
 B  f3_step2_r4-1_restart_store_manifest_<date>.csv, if a store was used
 C  every capture record and the RUN1 / RUN2 capture comparison
 D  the non-regression comparison with r4 (R4A-01 (f)) as a CSV or a report section
 E  the quarantine annotation note and any file found under R4A-10 (iii)
 F  f3_step2_r4-1_transmission_list_<date>.md: every deliverable, every sidecar, every quarantine / note file of
    this revision, the run logs (stdout AND stderr) of every launch, with SHA256 — and the same files attached
```

## 6. Report and end state

The six status fields computed from the run; a response table with one row per R4A item in scope (PASS / FAIL /
NOT_RUN(reason) / STOP, with test id or file and hash); the end-state block of D-3 §10 with
PI_dispatch_record_hash = the hash of D-6 as observed and S-R2-1 = PI_RULE (source D-5); expectation_checks =
<ran> / <declared>; parents_unchanged with the re-hash values of the r4 package and the r3 deliverables.
Expected end status: PARTIAL_PENDING_PI (T-R2-2 in narrowed_evidence; the coverage row "A.5 (iii) inadmissible
refit" uncovered unless a fixture covers it) — no other status is claimed; QUALIFIED is not declared by anyone.

## 7. Not in scope

Anything not named here, in the r4 instruction, D-3 or D-5: no redesign, no new fixture family beyond R4A-01 (d),
no change to any frozen or ratified text or to S-R2-1, no rewriting, renaming or moving of r3 / r4 / quarantined
files or of any audit record, no real SSA data, no algorithm × CVI results, no 6B, no R4A-08.
