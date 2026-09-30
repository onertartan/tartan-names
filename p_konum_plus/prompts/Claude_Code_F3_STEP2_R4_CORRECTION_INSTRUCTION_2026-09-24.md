# p_konum_plus — F3 STEP-2 r4 — Correction and execution instruction (2026-09-24)

```text
instrument            = Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md
instrument_class      = PI instruction for the r4 correction cycle. It is a NARROW child of the r3 prompt
                        DRAFT v2 (D-3, 5b0e19ea…): D-3 stays in force unchanged; this file only (a) adopts the
                        closure actions of the r3 independent audit as X corrections, (b) carries the PI's
                        S-R2-1 decision of the r4 dispatch record, and (c) states the r4 deliverables. Where
                        this file is silent, D-3 (and through it v6) governs
drafted_by            = Claude (Cowork session; configured model identifier claude-fable-5-1) at the PI's
                        request; the same session drafted D-3, filled D-4 at the PI's instruction and wrote the
                        r3 audit. Prior exposure is disclosed; the auditor of the r4 package will state it again
binding instruments   = D-3  Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
                             5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 (unchanged)
                        D-1  Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
                             17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 (unchanged)
                        D-2  f3_step2_pi_ratified_content_2026-09-07.md
                             da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 (unchanged)
                        D-5  f3_step2_r4_pi_dispatch_record_2026-09-24.md — the r4 dispatch record (child of
                             D-4 4e623536…); its hash stands in its own .sha256 sidecar, never inside it
                        this file
inputs, not directives = A-1  f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md
                             11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6
                             (the r3 audit; its findings R3A-01 … R3A-17 are adopted here as listed in §3;
                             the record itself decides nothing and is not rewritten)
                        Advisory notes and external AI reviews are NOT inputs to this cycle; nothing in them is
                        implemented unless it appears in D-5 or here
frozen upstream       = untouched: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (r4 5e594136… as ratified by freeze
                        record r1 7055f186…). No new scientific literal. No real SSA data. No 6B. No QUALIFIED
non-retroactivity     = the r3 package (harness 5fea165c…, generator cc23c9b5…, manifest 9c944543…, results
                        35279164…, its DEFERRED_THIS_CYCLE wiring) and the r3 audit are historical and
                        read-only. Nothing of r3 is overwritten; every r4 deliverable is a new file with the r4
                        name tag
```

## 1. Preconditions (D-3 §3, P-1 … P-4, applied to r4)

Before writing anything: verify by SHA256 that D-3, D-1, D-2, D-5 and this file are the bytes named above and
in D-5 (this file's hash stands in D-5 §1; D-5's hash stands in its sidecar). Read the six P-3 fields from D-5.
S-R2-1 = PI_RULE with a rule text; T-R2-2 as read. Any mismatch, blank or template residue: STOP before the
first computation (D-3 §3). A missing sidecar of a repository file is recorded and created; it is not a STOP.

## 2. Transmission first (audit register T-R3-1; no computation needed)

Deliver, before or with the r4 package, byte-exact with their hashes listed in the r4 report:

```text
(a) the .sha256 sidecars of the r3 deliverables 1–12 as they exist in the repository
(b) the five quarantine notes the r3 correction report names (attempt-1 note, classifier-defect note,
    P-1 … P-7 corrections note f3_step2_r3_independent_audit_corrections_note_2026-09-23.md, attempt-8
    telemetry-replay note f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md, transmittal-note
    corruption note)
(c) the superseded r3 harness revisions and custody records (6ddcc26d…, 891574fc…, d67e097d…, f882b922…,
    99f895c1… and their custody files), if they still exist; if any no longer exists, say so in the report
```

## 3. Corrections adopted from the r3 audit (X; blockers first)

The closure action of each finding is quoted from A-1 §4 and is the instruction. Test names are those of D-3 /
v6. Every correction is evidenced by a test that RAN and PASSED or by a delivered file; a correction reported as
applied without such evidence counts as not applied (D-3 §10, v6 §13).

```text
R3A-01  author the r3/r4 register as a child of R-09 with the rows v6 §11 and Y-10 … Y-19 name; VERBATIM rows
        byte-substrings of D-2 / D-4 / D-5; SUMMARY rows for the engineering of Y-04. Add the rows for the
        restart layer (§8.3), the TEST_ONLY evaluator branches (force_c4_pending, the post-construction hook)
        and S-R2-1 = PI_RULE (§4 below, tagged PI_RATIFIED with the hash of D-5)
R3A-02  implement X-11 (b) … (f) as written in v6: family telemetry rows with L and failure codes; the §6
        fields; the enlarged canonical document (per-fit endpoint, masked L, start-bank size,
        FEATURE_START_REJECTED; per spline fit the winner mode, RSS, equivalent-mode set, per-mode validity);
        `sexes` filled or removed; T-SCHEMA as a machine assertion; T-CANON over the enlarged document;
        FIX-STARTS-* write their rows; RUN2 mode rows kept
R3A-03  route an UNRELATED event to STOP_EXACTNESS_PENDING(<id>) for its context with a capture record (kind
        UNRELATED, TEST_ONLY where injected); catch every exception class at mode level for that purpose only;
        deliver every capture record (unit phase, RUN1, RUN2); compare RUN1 / RUN2 records; install /
        uninstall wrappers per scope (no stacking); run the INJ-EXC-* contexts as the manifest's run_scope says
R3A-04  re-validate every member of U from the data after construction; guard the comparator against a NaN /
        None scalar (INCONSISTENT_U); make T-COMPARATOR-NAN call the guarded comparator; record the offending
        (fitter, observation) pairs of rule (i)
R3A-05  write T-A5-SUPPORT (threshold equality included, next float below excluded, disconnected components
        united, partly observed versus fully masked, constant reference ⇒ S = G, invalid references ⇒
        violations); wire a CONTRACT_VIOLATION_A5_REFERENCE as STOP_EXACTNESS_PENDING / PENDING for C4a and C4b
        of that sex — never a C4 pass or fail (content §2.3)
R3A-06  replay the per-call telemetry snapshot for every unit kind read from the store (nrgates_all,
        unittests_all included); count per-fit reads; report calls per phase and per pid for the whole
        execution; add pid and start_iso to the store manifest; report "the units read from the store, with
        their pids" (D-3 §8.3)
R3A-07  correct the attempt log (rows 9–10 ran 5fea165c…, not 99f895c1…); record the three W-3 hashes per
        attempt; quarantine and list the foreign store entries (prefix 548ae790f6ac756a; audit register
        T-R3-2); write the W-3 custody record once per revision, outside the run process, with observed values
        (no "ALL PASS" literal, no constant dispatch-record hash); fix the harness docstring
R3A-08  derive the coverage statuses from the run; split or mark the row "C4b pass/fail (real)"; adopt the
        content §6 wording for the K-05 row (T-3)
R3A-09  make the consulted-level return on a None scalar write a `stops` record, or remove the branch
R3A-10  expose the U-set construction as pure functions and call them from UT-USET-CONSTRUCTION
R3A-11  compute corrections_complete and mandatory_tests_all_run from the test records (no literal)
R3A-12  complete the report as v6 §12 item 10, §14 and D-3 §10: custody table with observed hashes,
        per-finding table with test ids and results, coverage matrix, opened-file classification, hash line
        block, response table for every Y and every R3A item, attempt history of the r3 cycle with sources,
        parents re-hashed with values
R3A-16  optional: structural expectation columns for SCEN-A and the unit-test rows
```

## 4. S-R2-1 = PI_RULE (D-3 §5; the rule text is in D-5 §3 and is implemented word for word)

```text
(a) read the value and the rule text from D-5; tag the implementation PI_RATIFIED with the hash of D-5 (D-3 §5)
(b) membership by flags: V4_s(F) and the level-C4b consulted set U4_s are built from the recorded fields pL,
    pR, full of the fitters P01, P02, SPL exactly as the rule states — in P03 (evaluate_fixture) and in D-P04
    (the level-C4b consulted set) alike; the DEFERRED_THIS_CYCLE pre-check that returned
    STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-03) is not taken (the state is a membership condition, never
    PENDING); D-3 §5's ambiguity fallback applies only if the executor records an ambiguity in the rule text
(c) no numeric outcome on an absent reference; n_s retained; C4a, C3 / CL-F3-04 unchanged (rule items 3, 4)
(d) EXACT-03 is closed with D-5 as its source (register row; report); deferred_decisions = [];
    the second half of UT-PROBE-DECOUPLE runs; the coverage row "D-P04 resolve at C1" is covered by
    INJ-DP04-C1; the real-path row "C4b fail" takes its evidence from SCEN-B
(e) expectations predeclared BEFORE the run, in the manifest's expected_* columns, for the four S-R2-1
    fixtures, as pinned in D-5 §3: SCEN-B, INJ-C1-FAIL, INJ-DP04-C1, INJ-C4B-NOREF. A run whose result differs
    from a pinned expectation is an EXPECTATION_FAIL (D-3 Y-02 (c)), never a re-derivation
(f) generator cleanup: the prose of INJ-C4B-NOREF says "phi and RMSE_edge absent" while the construction sets
    only the full flag to False and leaves phi, rL, rR finite; correct the prose (the construction is right:
    membership must come from the flag, not from the value)
```

## 5. Run rules (D-3 §8, unchanged) and the store

One process from the beginning first; a restart layer only after an interruption and only as D-3 §8.3 says
(T-R2-2 as read in D-5). The store is emptied at the start of the r4 cycle (new fingerprint by construction);
the r3 store directory and the foreign entries under 548ae790f6ac756a are quarantined and listed, not deleted
silently (R3A-07). Attempt log, custody record and per-call telemetry as §3 R3A-06 / R3A-07 say.

## 6. Deliverables (D-3 §9 with the r4 name tag; every file with an external .sha256 sidecar; no self-hash)

```text
D-3 §9 items 1–12 with "r3" replaced by "r4" in every name and path (item 9, the register, is mandatory this
cycle — R3A-01); D-3 §9 items 13 (attempt history of the r2 cycle as a report section), 14 (sidecars) and 15
(parents re-hashed with values) stand unchanged. In addition:
 A  f3_step2_spline_percall_telemetry_r4_<date>.csv — all phases, all pids (R3A-06)
 B  f3_step2_r4_restart_store_manifest_<date>.csv — path, size, sha256, pid, start_iso — if a store was used
 C  every capture record (unit phase, RUN1, RUN2) and the RUN1 / RUN2 capture comparison (R3A-03)
 D  the transmission items of §2
```

## 7. Report and end state (v6 §13 / §14, D-3 §10)

The six status fields computed from the run; the response table with one row per Y-01 … Y-21 and per R3A-01 …
R3A-16 (executor claim PASS / FAIL / NOT_RUN(reason) / NOT APPLICABLE(reason) / STOP, with evidence); the
end-state block of D-3 §10 with PI_dispatch_record_hash = the hash of D-5 as observed, S-R2-1 = PI_RULE and
T-R2-2 as read; expectation_checks = <ran> / <declared>; parents_unchanged with the re-hash values. Expected end
status: PARTIAL_PENDING_PI (T-R2-2 in narrowed_evidence if AUTHORIZE_RESTART; the coverage row "A.5 (iii)
inadmissible refit" uncovered unless covered by a fixture) — no other status is claimed; QUALIFIED is not
declared by anyone in this cycle.

## 8. Not in scope

Anything not named in D-3, D-5 or here: no redesign, no new fixture family beyond the rows named, no change to
frozen or ratified text, no rewriting of r3 files or of any audit record, no real SSA data, no algorithm × CVI
results, no 6B.
