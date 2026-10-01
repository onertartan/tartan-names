# p_konum_plus — F3 STEP-2 r4-2 — Independent Audit — DRAFT r1 (2026-10-01)

```text
record                  = f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md
record_class            = independent audit of the STEP-2 r4-2 correction revision (the second correction revision
                          inside the r4 cycle), received 2026-10-01 as one zip; child of the r4-1 audit DRAFT r1
                          (A-4, ad222936…), which it does not rewrite
auditor                 = claude-opus-5-5 (Claude, Cowork session; the model the PI selected — the serving model may
                          differ). Not the executor. Decides nothing for the PI. Declares no QUALIFIED
reviewer_prior_exposure = true — this session drafted D-3 and the r4, r4-1 and r4-2 instructions, filled D-4 … D-7 at
                          the PI's written instructions (D-7 §3, which R42A-02 discusses, included) and wrote A-1 …
                          A-4. On 2026-09-30 it also told the PI, before the PI accepted it, that the executor's
                          per-criterion reading of R41A-01 (b) is consistent with the instruction's intent, without
                          pointing out that D-7 §3 (2) would then need a superseding record. The closure actions
                          checked here are this session's own; agreement with them is not an independent derivation
second reading          = before release, a read-only sub-agent of this session checked sections 0–7 against the
                          files. Its points were re-checked by the auditor on the files; those that held are adopted
                          (R42A-01 (b) and (c), R42A-02's classification, R42A-03, and several wordings)
other auditors' records = none received; none used
executor                = Claude Code; per its report: claude-opus-4-8[1m] up to the instrument verification and
                          claude-fable-5 from the scope execution on (harness b988e962… ; generator 68d126cf… and
                          manifest 5c09c4f0… reused unchanged from r4-1)
dispatched instruments  = r4-2 instruction d6680338… ; D-7 a3e70509… ; standing: r4-1 instruction 283ac4e2… ; D-6
                          a92a0518… ; r4 instruction e1283958… ; D-5 0cd87ad5… ; D-3 5b0e19ea… ; D-1 17187d31… ;
                          D-2 da0c4064… ; inputs, not directives: A-1 11cfa591…, A-2 b7217027…, A-3 9c16abb5…, A-4
frozen upstream         = untouched: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (as ratified by freeze record r1). Nothing
                          reopened; no scientific literal produced
evidence tiers          = [A] auditor-verified on the delivered bytes (and on the auditor's own copies of earlier
                          packages, verified in A-1 … A-4) ; [A-S] auditor-environment execution of the delivered code
                          (Linux; Python 3.11.15, numpy 2.4.4, scipy 1.17.1 — never a claim about an executor hash) ;
                          [X] executor claim ; [E] external
honesty rule            = every hash here was computed by the auditor with the scripts of §9 or is quoted from a named
                          file; a check the auditor could not run is NOT PERFORMED
sidecar                 = external .sha256 ; no self-hash
```

## 0. Verdict

```text
audit_verdict                 = PASSED — no global and no gate-specific blocker is open on the delivered bytes.
                                PASSED is this record's audit vocabulary only: it is not QUALIFIED, not an
                                acceptance of the package and not a status change
global blockers               = 0
gate-specific blockers        = 0
cleanup                       = 3   (R42A-01 … R42A-03)
informational                 = 7   (R42A-04 … R42A-10)
A-4 findings in scope (D-7 §3) = R41A-01, R41A-02, R41A-03, R41A-05, R41A-06 CLOSED ; R41A-04 PARTIALLY CLOSED (§6)
F3_STEP2_r4_status (executor) = PARTIAL_PENDING_PI — supported [A]; narrowed_evidence [T-R2-2] and the uncovered
                                row "A.5 (iii) inadmissible refit" keep it there (PI decisions, §7)
F3_STEP2 = QUALIFIED          = NOT declared (PI only)
```

In plain words. The r4-2 revision does what A-4 asked on the point that mattered most. The latent defect of r4-1 is
gone: when the spline solver fails in a way that cannot be verified, the affected criteria are now put on hold whether
the failure is natural or deliberately injected, and each held criterion says which kind it was; a declared test
failure of the spline fit is still treated as an ordinary failure. The auditor checked this three ways: the executor's
new real-path test, re-run in the auditor's environment, reproduces the delivered test record exactly; the auditor's
own probe, with twelve cases of its own, gives exactly the expected held cells; and the decision layer reproduces all
35 decision-layer objects identically (§5). Nothing else moved: all 37 evaluation objects and all 6 stop records are
identical to r4-1's in canonical JSON, the residual series is byte-identical, and the telemetry files differ from
r4-1's only in timing and process-id columns. One process (pid 10412) computed everything, so the single-process rule
of D-3 applies and holds, and RUN1, RUN2 and every evaluation object were computed without reading the restart store.
The custody discipline asked for after r4-1 was applied from the first write: one custody record per attempt, the
superseded harness preserved in quarantine and equal to the hash its record names, one log pair per launch.

Three cleanup items remain; none changes a result. First, records are incomplete: the report's hash block leaves out
several hashes, the transmission list gives the interruption note only by its sidecar, and the report states that
the parent packages are unchanged without printing their re-hash values (R42A-01). Second, the PI accepted the
executor's per-criterion reading of the mixed-tag rule by a chat message; the PI's own dispatch record D-7 still
words that rule per sex, and no PI record supersedes it yet (R42A-02). Third, the restart store was read inside the
run after all: the second pass of three unit-test fixtures was served from what the first pass had just stored, so
that pass is a replay rather than a second execution, while the process block, the report and the attempt log say
that nothing was read. The same pattern is in the r4 and r4-1 telemetry, and the earlier audits missed it (R42A-03).
The seven informational items change no result.

## 1. Custody at reception [A]

Received 2026-10-01 as one zip (SHA256 3a93e558c78b37e32228498fe3ba634e6f80394ee06d6d64ea7fb33eb8855cad, 1,409,226
bytes, 54 entries): 27 files and 27 sidecars, each sidecar in the form hash, two spaces, own name, LF, and each equal
to its file (§9 block [1]). The 22 rows of the transmission list (711e728d…) that carry a full hash equal the
delivered files; the five files without a full hash in the list (the three instruments, the attempt-1 interruption
note and the list itself) equal their sidecars. The r4-2 instruction, D-7 and A-4 in the zip are byte-identical to
the auditor's own files, and the reused generator and manifest are byte-identical to the audited r4-1 files, with
the same sidecars. CR bytes occur only in the four launch logs (Windows console output) and in the two
non-regression CSVs (CRLF rows; see R42A-10).

| deliverable | file | SHA256 |
|---|---|---|
| 1 harness (attempt 2) | f3_step2_adequacy_harness_r4-2_2026-09-30.py | b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 |
| 2 generator (reused) | f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3 manifest (reused) | f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4 custody, attempt 2 | f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md | 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1 |
| 4' custody, attempt 1 | f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md | ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e |
| 5 telemetry | f3_step2_telemetry_r4-2_2026-09-30.csv | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d |
| 6 results | f3_step2_results_r4-2_2026-09-30.json | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba |
| 7 residual series | f3_step2_residual_series_r4-2_2026-09-30.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 test evidence | f3_step2_test_evidence_r4-2_2026-09-30.json | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf |
| 9 register | f3_step2_class_c_pin_register_r4-2_2026-09-30.md | c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c |
| 10 correction report | f3_step2_correction_report_r4-2_2026-09-30.md | 7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6 |
| 11 start-state inventory | f3_step2_r4-2_start_state_inventory_2026-09-30.md | 66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5 |
| 12 attempt log | f3_step2_r4-2_attempt_log_2026-09-30.md | b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65 |
| A per-call telemetry | f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv | 7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c |
| B store manifest | f3_step2_r4-2_restart_store_manifest_2026-09-30.csv | 1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95 |
| D non-regression vs r4-1 | f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d |
| D' non-regression vs r4 | f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| E attempt-1 harness bytes | f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py | 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74 |
| E interruption note | f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md | a4b5e176de9be9e8caa1b2145ce99e9c2539fcbea254df0a23ba2bfada470bbe |
| E launch 1 stdout / stderr | f3_step2_r4-2_launch1_{stdout,stderr}_2026-09-30.log | 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 / d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 |
| E launch 2 stdout / stderr | f3_step2_r4-2_launch2_{stdout,stderr}_2026-09-30.log | 3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7 / df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| F transmission list | f3_step2_r4-2_transmission_list_2026-09-30.md | 711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606 |

Not delivered and therefore not verified: the quarantine copies of the launch-1 log pair (transmission list line 59
gives them the hashes of the delivered originals) [X]; the store unit files themselves (the store manifest is
delivered) [X]; the standalone W-3 writer [X].

## 2. Which bytes ran [A]

```text
fingerprint formula (harness L3057) with the F2 and spline constants read from the harness and the environment the
     custody records state:
     attempt 1: harness 9e4d2803… + generator 68d126cf… + manifest 5c09c4f0… -> 0f32c7911cf8fccb = attempt-1 record
     attempt 2: harness b988e962… + the same pair                           -> 4ced291f15fb5afd = attempt-2 record
                = the ONLY prefix of the 11,869 units of the store manifest
every launch asserts the custody record of its attempt before computing (harness, generator, manifest and
     fingerprint compared, L3080–3088); both launch logs print the verification line for their own record
attempt-1 bytes: the quarantined copy hashes to 9e4d2803… = the attempt-1 record's harness_sha256, and launch 1
     verified that record at start, so the preserved bytes are the bytes launch 1 ran; when the copy was taken
     relative to the edit is [X]
attempt 1 -> 2 changes (§9 block [6]): the revision constants (ATTEMPT_NUMBER, RESTART_LAYER_ACTIVE, the three
     SUPERSEDES_* values, LAUNCH_NUMBER now read from F3_R42_LAUNCH), the launch-number assertion and print at the
     top of main(), three process-block fields; no fit, decision or test code
attempt-2 record: supersedes_custody_sha256 = ae0f0768… = SHA256 of the attempt-1 record ; supersedes_harness =
     9e4d2803… = SHA256 of the quarantined copy
the 13 instrument hashes the attempt-2 record states as observed = the auditor's own copies, D-1 and D-2 included
single process: pid 10412 (start 2026-09-30T20:38:58.140644) is the only pid and start time in the results, the
     test evidence, the per-call telemetry and the store manifest; launch 2 ends with RUN_COMPLETE 10412 —
     T-SINGLE-PROCESS (D-3 Y-01) holds on the delivered objects
store reads inside the process: the coarse counters units_read_from_store are 0, but under the active layer the
     second pass of the INJ-EXC-* unit fixtures was served from the store (block below; R42A-03). RUN1 and RUN2 use
     run-labelled keys, no RUN1/RUN2 per-call pair shares a wall-clock value, and no family-fit or spline-mode
     telemetry key repeats outside the INJ-EXC fixtures: the evaluation objects were computed without store reads
r4-1 and r4 stores: the opened-files list the process recorded (results, 24,033 entries) contains store paths of
     the r4-2 store only (23,738 = 2 × 11,869, all under 4ced291f…) and no quarantine path [A on the record; the
     physical directories are not delivered, X]
unit names of the r4-2 store = the r4-1 store's unit names (prefix removed): the same work, recomputed
```

The in-process reads, shown on the delivered telemetry (§9 block [8]); a row replayed from the store carries the
wall-clock value stored with it, so two rows of different executions do not share all columns:

```text
== per-call telemetry, INJ-EXC-* rows of the unit-test phase: second half against first half
  r4    d7f689fe5e9f… rows 984 | halves equal on every other column: True | equal wall-clock in 492 of 492 pairs | pids ['31388']
  r4-1  22a5ae8f9cdc… rows 984 | halves equal on every other column: True | equal wall-clock in 492 of 492 pairs | pids ['22616']
  r4-2  7e44fdf95d37… rows 984 | halves equal on every other column: True | equal wall-clock in 492 of 492 pairs | pids ['10412']
  r4-2 RUN1/RUN2: 5256 / 5256 rows ; pairs with equal wall-clock: 0 ; mask ids carry the run label: True
  r4-2 run1: wall-clock values shared by two or more rows 4 ; of them shared by the same (fixture, mask, mode): 0
  r4-2 run2: wall-clock values shared by two or more rows 11 ; of them shared by the same (fixture, mask, mode): 0

== telemetry (deliverable 5, r4-2): family fits and spline modes
  rows 12298 by fitter {'P-01': 1012, 'P-02': 1062, 'SPL': 10224}
  family-fit rows 2074 ; keys (fixture, fitter, mask, family, start, path) occurring more than once: 0 ; rows equal in every column to another row: 0
  spline mode rows 10224 ; keys (fixture, mask, mode) occurring more than once: 438, by fixture {'INJ-EXC-CAPTURE-S1': 146, 'INJ-EXC-CAPTURE-S2': 146, 'INJ-EXC-UNRELATED-TYPE': 146}

== store manifest (r4-2)
  unit kinds {'nrgates': 1, 'onestart': 2081, 'realscen': 4, 'splmode': 9782, 'unittests': 1} ; INJ-EXC mode units 438 (one per fixture context and mode: 3 x 146 = 438: True)

== the harness
  L1104  mkey = "splmode_%s_%s_%s_%s" % (fixture_id, mask_id, m, xhash)
  L1105  cached_mode = ckpt_load(mkey)
  L2573  fixtures -- honored as TWO full deterministic passes, results asserted
  L2578  p1 = _exc_injection_pass(spl)
  L2579  p2 = _exc_injection_pass(spl)
  L3135  UNITS_READ_FROM_STORE["nr_gates"] += 1
  L3237  UNITS_READ_FROM_STORE["unit_tests"] += 1
  L3327  UNITS_READ_FROM_STORE[run_label] += 1

== process block and test evidence (r4-2)
  units_read_from_store: {"nr_gates": 0, "residual_export": 0, "run1": 0, "run2": 0, "unit_tests": 0}
  exc_injection_fixtures: passes_identical True ; pass2 == pass1 fields: True
  launch 1 (RESTART_LAYER_ACTIVE = False): S1 / S2 / UNRELATED_TYPE pass_ True / True / True ; passes_identical True
  launch 2 (RESTART_LAYER_ACTIVE = True): S1 / S2 / UNRELATED_TYPE pass_ True / True / True ; passes_identical True
  launch 1 progress lines for INJ-EXC contexts: ['5', '6', '7', '8', '9', '10']
  launch 2 progress lines for INJ-EXC contexts: ['5', '6', '7', '8', '9', '10']
```

So every object of the final output was computed by one process running the delivered bytes after the custody check.
The determinism wording of v6 §8 stands for RUN1 == RUN2 (one process, no store read between or within the runs);
RUN1 == RUN2 itself is the executor's measurement [X], and the delivered RUN1 content hashes to the claimed value [A].

## 3. Checklist

| # | check | executor claim | auditor result |
|---|---|---|---|
| C-01 | zip, 27 files, 27 sidecars, 22 list rows | equal | PASS [A] |
| C-02 | instrument hashes observed in the custody records = auditor copies (13) ; forwarded instruments byte-identical | EQUAL ×15 | PASS [A] |
| C-03 | delivered bytes = executed bytes (fingerprints, store prefix, pid, custody assertions) | implied | PASS [A] (§2) |
| C-04 | generator and manifest reused unchanged; manifest regenerated in memory and asserted equal | reused, equal | PASS [A] (byte-identical to the audited r4-1 files; asserts L3045, L3048; both logs print the reuse line) |
| C-05 | canonical RUN1 document = claimed hash | 556106e7… | PASS [A] (recomputed from the delivered evaluations and stops) |
| C-06 | RUN1 == RUN2 | true | [X], within one process (C-24) |
| C-07 | T-EXPECT-ALL | 36 / 36 | PASS [A] by identity: the manifest is byte-identical and all 37 evaluation objects are identical (canonical JSON) to r4-1's, for which A-4 re-did the 36 checks |
| C-08 | R41A-01 (a): TEST_ONLY clause dropped at the three flag sites; tag taken from the failure string | done | PASS [A] (L2061, L2089, L2102; helper L421; §9 block [6]) |
| C-09 | R41A-01 real path, natural event → dependent criteria STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04), both families | PASS | PASS [A-S] (executor's test reproduced; auditor probe P2, P3, P10) |
| C-10 | R41A-01 real path, injected event → STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED), no definite outcome | PASS | PASS [A-S] (P4, P5, P9, P12; no PENDING cell carries a verdict) |
| C-11 | declared spline failure stays an ordinary failure (D-5's SCEN-B pin) | PASS | PASS [A-S] (P11; real fit_spline returns no STOP string, §5.2 part 2) and [A] (SCEN-B object byte-identical) |
| C-12 | both kinds in one sex | per criterion | PASS [A-S] under the per-criterion reading the PI accepted by chat (known from the executor's quotation, [X]); departs from D-7 §3 (2) — R42A-02 |
| C-13 | finding machinery unchanged: a natural event opens F3-STEP2-EXACT-04, an injected one is not entered | unchanged | PASS [A] (fit_spline and fit_family identical to r4-1; the natural_unrelated block L3428 verbatim in both) |
| C-14 | T-SPL-PENDING-REALPATH mandatory, ran and passed in both launches; stubs and globals restored | 9 / 9 | PASS [A] (MANDATORY_TESTS, tests_run, both stdout logs) and [A-S] (whole delivered record reproduced); its stubs end the baseline in BOTH_FAIL, so for fold and probe events it shows held cells without verdicts but not an open fixture outcome, which the auditor's probe shows (§5) |
| C-15 | T-NONREG-R4-1: 37 objects and stops vs r4-1, no whitelist; canonical and residual at named values | 0 findings | PASS [A] (independent comparison of the delivered files: 37 / 37 identical, 6 stops identical in order, residual byte-identical) |
| C-16 | T-NONREG-R4 retained | 0 findings | PASS [A] (CSV byte-identical to r4-1's) |
| C-17 | R41A-02 (a) one custody record per attempt, supersedes filled | done | PASS [A] |
| C-18 | R41A-02 (b) superseded harness copied before the edit, copy = custody-named hash | done | PASS [A] on the bytes; timing [X] |
| C-19 | R41A-02 (c) one launch-numbered log pair per launch | done | PASS [A] (both pairs delivered; launch 2 prints LAUNCH_NUMBER = 2) |
| C-20 | R41A-03 end state names D-7 as observed; S-R2-1 source in its own field; assertions | done | PASS [A] (fields = SHA256 of the auditor's D-7 and D-5; assertions L4041–4044, L4148–4154) |
| C-21 | R41A-04 hash block | CLOSED | PARTIAL — R42A-01 (a) (the three r4-1 hashes printed correctly) |
| C-22 | R41A-05 ERRATUM-3 | CLOSED | PASS [A] (every point checked, §9 block [3] J7); imprecisions — R42A-05 |
| C-23 | R41A-06 descriptions | CLOSED | PASS [A] (report and register match the delivered stop record) |
| C-24 | T-SINGLE-PROCESS | holds | PASS [A] (§2; the in-process reads of C-31 read units the same process computed) |
| C-25 | r4-1 and r4 stores untouched and unread; nothing renamed or moved | stated | PASS [A] on the process's opened-files record; physical state [X] |
| C-26 | parents unchanged at the start: the 12 r4-1 files of the inventory | true | PASS [A] (= the auditor's r4-1 bytes) |
| C-27 | telemetry and per-call telemetry | 12,298 / 12,174 rows | PASS [A] (equal to r4-1 row by row except wall-clock, pid and start columns) |
| C-28 | coverage 64 rows; only A.5 (iii) uncovered | 64, 0 downgraded | PASS [A] (identical to r4-1's coverage) |
| C-29 | no real data; no QUALIFIED claim; no new scientific literal | asserted | PASS [A] |
| C-30 | end state PARTIAL_PENDING_PI | as D-7 §5 expected | PASS as status |
| C-31 | units read from the store reported (D-3 §8.3 provenance) | none read | FAIL — the second INJ-EXC pass read the 438 INJ-EXC mode units the first pass stored; they are not counted — R42A-03 (b) |
| C-32 | INJ-EXC-* fixtures executed twice (run_scope both) | passes identical | launch 1 (layer off) executed both passes [A]; in the final process the second pass is a replay — R42A-03 (a) |
| C-33 | parents_unchanged with the re-hash values of the r4-1 and r4 packages (instruction §6) | true | PARTIAL — R42A-01 (c) |
| C-34 | the transmission list gives every file with its SHA256 (instruction §5 F) | complete | PARTIAL — the interruption note by sidecar only — R42A-01 (b) |

## 4. Findings

| id | classification | finding | gate effect | closure action | authority |
|---|---|---|---|---|---|
| R42A-01 | cleanup | Records incomplete against the r4-2 instruction. (a) R41A-04 is only partly done: the instruction asks that the report's hash block print the hash of every r4-2 deliverable except the report itself. The block (report L108–128) prints full hashes for 14 deliverables and 8-hex prefixes for the four launch logs and the attempt-1 harness copy (L128), gives the register (L121) and the attempt log (L123) as sidecar references and the interruption note as sidecars (L128). Its explanation (L130–131) covers the register and the attempt log only. None of these files contains the report's hash — only the transmission list does — so nothing circular prevents printing them. The response-table row (L102) says CLOSED and that the block prints every r4-2 deliverable except the report. The second half of R41A-04 is done: the three r4-1 hashes are printed and equal the auditor's copies. (b) Instruction §5 F (L178) asks the transmission list to give every file with its SHA256; the list gives the interruption note as sidecar only (list L57), so its hash a4b5e176… stands in no delivered file but its own sidecar. (c) Instruction §6 (L189) asks for parents_unchanged with the re-hash values of the r4-1 and r4 packages; the report states parents_unchanged = true (L178) and refers to the start-state inventory (L53–54), which lists the r4-1 package in full but the r4 package as two 8-hex prefixes (inventory L55); no end-of-revision re-hash is printed | none: every file's hash stands in its delivered sidecar and was verified at reception; §1 of this record prints all of them; the auditor's r4-1 copies equal the inventory; the run asserted the r4-1 and r4 results hashes when it read them | in the next record child, print the missing hashes in full (register c281e713…, attempt log b69a5915…, interruption note a4b5e176…, the four launch logs and the attempt-1 copy) and the end-of-revision re-hash of the r4-1 and r4 packages, and word the response row as what the block shows; or the PI accepts §1 of this record as the hash list | X |
| R42A-02 | cleanup | The mixed-tag rule. D-7 §3 (2) (L77), accepted by the PI with that record (L83), words it per sex: when a sex has both a natural and an injected pending event, F3-STEP2-EXACT-04 is used; so does the case line of the instruction (L91). The instruction's rule (L80) adds "for the criteria it routes", and the executor read it per criterion, so its mixed case (injected full, natural probeL, sex F) expects and gets C3 = TEST_ONLY_INJECTED and C4b = F3-STEP2-EXACT-04. The PI accepted that reading by a chat message on 2026-09-30, which the auditor knows from the executor's quotation (report §1; register L49, which calls it a dispatch message) [X] and from the PI's statement in the Cowork session that he would send it [E]. Under this reading a natural event is never masked (it reaches C4b and the mechanism outcome), so the stated purpose of the rule holds; but the governing PI record says otherwise for this case and no PI record supersedes it | none on any delivered output (no fixture has both kinds) | a PI-owned record (child of D-7) stating that the per-criterion reading supersedes D-7 §3 (2) for a sex whose two kinds reach different criteria | T (PI) |
| R42A-03 | cleanup | Store reads inside the final process. (a) Under the active layer fit_spline keys a mode unit by fixture, mask id, mode and input hash only (L1104), and the INJ-EXC-* fixtures are fitted twice with the same keys (L2578–2579; the docstring, L2573, calls them two full deterministic passes). In the per-call telemetry the second 492 INJ-EXC rows equal the first 492 in every column, wall-clock included, and the store holds one set of these units (438 = 3 contexts × 146 modes): the second pass was read from the store, its captures replayed without a check for equal records (L1108), and passes_identical is true by construction. The tests' pass_ values come from the first pass, and launch 1 (layer off, attempt-1 bytes, the same code for these functions) executed both passes fresh with the same results. (b) units_read_from_store counts only the coarse units (L3135, L3237, L3327), so the process block, the report (L68) and the attempt log (L67) state that no unit was read; D-3 §8.3 asks the results to report the units read from the store. The same pattern is in the r4 and r4-1 telemetry; A-2, A-3 and A-4 did not detect it. RUN1 and RUN2 are not affected (run-labelled keys; no shared wall-clock pair) | none on the evaluation objects, stops, residual series or RUN1 == RUN2; for the T-R2-2 decision it means the layer did serve reads in the final process (unit phase only) | report fine-grained store reads, or state that the counter is coarse and list the replayed units; if the second pass is meant as determinism evidence, give it its own key namespace as RUN1/RUN2 have | X |
| R42A-04 | informational | Mechanism outcome with both kinds: r4-1 joined the tags (comma-separated); r4-2 folds them to the natural tag (L1639). Each held criterion still carries its own tag, so the evaluation object keeps the information; no delivered fixture has both kinds, so no output changed. The change is disclosed in the code comment and the register row L49, not in the report's response table | none | none | — |
| R42A-05 | informational | ERRATUM-3 meets R41A-05 (all points recomputed or looked up, §9 block [3] J7), with three imprecisions: (i) the scope-of-impact sentence (attempt log L164) gives r4-2's fingerprint as 0f32c7911cf8fccb, which is attempt 1's (no unit written); the r4-2 units are under 4ced291f15fb5afd — the conclusion holds for both; (ii) Observation 1 (L116) says the custody records state the r3 environment; they state only the fingerprints, the environment stands in the r3 results JSON, and the recomputation reproduces the recorded fingerprints either way; (iii) the ATTEMPT8-labelled custody record's own supersedes_harness_sha256 = f882b922… — which points the same way as Inference A, like the rows 9–10 pattern A-1 found (R3A-07) — is not cited. Informational because the correct values stand in the custody records, the store manifest and the report, and the conclusions hold either way — unlike R41A-06, none of them misdescribes a delivered output | none | none; (i) can be corrected in the same record child as R42A-01 | — |
| R42A-06 | informational | Text carried from the previous attempt or revision, or loosely worded: (a) the attempt-2 custody record (L93) states the restart layer as True but keeps the attempt-1 parenthesis that begins with r4-2 attempt 1 being one process; (b) the process block's executor_models literal (harness L3943) still names claude-opus-4-8[1m] and the r4-1 report, while the r4-2 report (L155) discloses a model change mid-revision — the harness cannot observe the model, and the report is the disclosure; (c) the non-regression CSV against r4 keeps r4-1's labels (column r4_1, status NEW_IN_R4-1), being byte-identical to r4-1's file; (d) the attempt log gives launch 1's start as an evening (L40) although launch-1 stdout prints START = 2026-09-30T19:51:46.884861, and no end time, only the last context reached (D-3 §8.2 asks for start and end); (e) report §2 presents the W-3 writer's and the launches' checks as the same 15, but the launches check the r4-1 results and not D-1, the writer the reverse; (f) the harness docstring (L2375) points the reading to the register row PIN-SPLINE-PENDING-ROUTING, which the register states under PIN-SPLINE-PENDING-TAG-SCOPE | none | none | — |
| R42A-07 | informational | D-3 §8.3 asks for the store directory to be named in the W-3 record. No custody record of r3, r4, r4-1 or r4-2 names it literally; it is fixed by the harness constant RESTART_STORE_DIR (L170), whose bytes the record pins, and named in the interruption note and the transmission list. The requirement's purpose — the directory fixed before the run — is met through the pinned bytes, hence informational. Not raised by A-1 … A-4 | none | none | — |
| R42A-08 | informational | Test evidence: (a) exc_captures_unit_phase holds 8 records where r4-1 and r4 held 4. Records 5–8 equal records 1–4 field by field: they are the second INJ-EXC pass's replay of the first pass's captures from the store (R42A-03). In r4 and r4-1 the whole unit phase was read back as one coarse unit, and that replay keeps a record only if an equal one is not yet present (L3234), so their files list each record once. (b) The test-evidence copy of tests_run lacks T-CALLCOUNT, which is recorded after the file is written (as in r4-1) | none | none | — |
| R42A-09 | informational (latent) | fit_spline derives a context's tag from every UNRELATED capture recorded in the process for the same fixture and mask id (L1187), not only from the current call: in the auditor's probe a TEST_ONLY-only fit reusing the id of an earlier natural fit came back tagged F3-STEP2-EXACT-04 (§5.2 part 2, last call). No delivered path refits one fixture and mask id with events of different kinds (RUN1 and RUN2 mask ids carry the run label; the INJ-EXC-* fixtures refit with TEST_ONLY events only). The criteria are held either way; only the tag can differ, and only towards the natural one; in r4-1 the same carry-over would have produced the same string. Hence informational, unlike R41A-01, whose latent path produced a definite outcome. Unchanged since r4 | none | none in this cycle | X (if ever addressed) |
| R42A-10 | informational | Auditor self-correction: A-4 R41A-09 says every r4-1 deliverable is LF; the r4-1 non-regression CSV (41dca0ba…) has 38 CR bytes (CRLF rows, the csv module's default), as do both r4-2 non-regression CSVs; the launch logs of both revisions carry Windows console CRLF. A-4 is not rewritten | none | none | — |

## 5. Auditor execution [A-S]

### 5.1 Decision layer, unit tests and the executor's real-path test

The script r42_04_decision_layer_repro.py (§9) imports the unmodified r4-2 harness and the reused generator from the
auditor's repository mirror, evaluates all 35 decision-layer fixtures twice in one process, calls the pure unit
tests, runs the executor's own t_spl_pending_realpath (with the numerical engines it stubs, so no fit runs) and
probes the two new helper functions. main() is not called; nothing is written into the mirror.

```text
environment: python 3.11.15 numpy 2.4.4 scipy 1.17.1 Linux-6.18.44-fc-v50-x86_64-with-glibc2.39 ; cwd /home/claude/audit_ws/G:/PycharmProjects/pkp-worktree
harness sha256: b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 | GEN_PATH p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py
generator sha256: 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
RESTART_LAYER_ACTIVE as delivered: True | store dir p_konum_plus/calibration/.r4-2_restart_store_2026-09-30 | exists before: False

(a) decision layer
decision-layer fixtures: 35 | pass1 == pass2 (same process): True | fixture data changed by pass 1: False
identical to the delivered r4-2 evaluation objects: 35 / 35 | differing: []
INJ stops identical to the delivered ones: True [('INJ-BOTH-FAIL', 'BOTH_FAIL_REDESIGN'), ('INJ-DP04-EMPTY-U', 'CONTRACT_VIOLATION_EMPTY_U'), ('INJ-U-POST-CONSTRUCTION-INVALID', 'CONTRACT_VIOLATION_INCONSISTENT_U'), ('INJ-NAN-STAT-SPL', 'BOTH_FAIL_REDESIGN'), ('INJ-P03-BOTHFAIL-C4PENDING', 'BOTH_FAIL_REDESIGN')]
  INJ-SPL-PENDING-FULL   pending {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | expected cells ['P01:C3:F', 'P01:C4b:F', 'P02:C3:F', 'P02:C4b:F'] | C4a F passed True | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)
  INJ-SPL-PENDING-FOLD   pending {"P01:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | expected cells ['P01:C2:F', 'P02:C2:F'] | C4a F passed True | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)
  INJ-SPL-PENDING-PROBE  pending {"P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | expected cells ['P01:C4b:F', 'P02:C4b:F'] | C4a F passed True | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)

(b) pure unit tests
t_a5_support equal to delivered: True | pass: True
t_comparator_nan equal to delivered: True | pass: True
ut_uset_construction equal to delivered: True | cases ok: {'a': True, 'b': True, 'c': True, 'd': True, 'e': True}

(c) the executor's T-SPL-PENDING-REALPATH, run here (f2m/spl/grids passed as None: the stubs never use them)
stdout lines printed during the test: 0
pass_ True | all_cases_ok True | restored {"exc_captures": true, "fidelity_declared": true, "fidelity_executed": true, "fit_family": true, "fit_spline": true, "phase": true, "progress_counter": true, "telemetry": true}
  baseline                         ok True  | identical to the delivered case record: True  | got {} | mechanism STOP_BOTH_FAIL_REDESIGN
  natural full                     ok True  | identical to the delivered case record: True  | got {"P01:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04)
  natural fold                     ok True  | identical to the delivered case record: True  | got {"P01:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism STOP_BOTH_FAIL_REDESIGN
  natural probe                    ok True  | identical to the delivered case record: True  | got {"P01:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism STOP_BOTH_FAIL_REDESIGN
  injected full                    ok True  | identical to the delivered case record: True  | got {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)
  injected fold                    ok True  | identical to the delivered case record: True  | got {"P01:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | mechanism STOP_BOTH_FAIL_REDESIGN
  injected probe                   ok True  | identical to the delivered case record: True  | got {"P01:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | mechanism STOP_BOTH_FAIL_REDESIGN
  declared spline failure          ok True  | identical to the delivered case record: True  | got {} | mechanism STOP_BOTH_FAIL_REDESIGN
  natural and injected, same sex   ok True  | identical to the delivered case record: True  | got {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04)
globals and engines restored after the test (auditor's own snapshot): {"ctx": true, "exc": true, "fd": true, "fe": true, "ff": true, "fs": true, "ph": true, "tel": true}
whole record equal to the delivered spl_pending_realpath block: True

(d) helper functions
  spl_pending_tag('STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)') -> 'F3-STEP2-EXACT-04'
  spl_pending_tag('STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)') -> 'TEST_ONLY_INJECTED'
  spl_pending_tag('TEST_ONLY_INJECTION_SPLINE_FAILURE') -> False
  spl_pending_tag('NO_VALID_MODE') -> False
  spl_pending_tag('ZERO_VARIANCE_OR_NONFINITE') -> False
  spl_pending_tag(None) -> False
  spl_pending_tag('') -> False
  spl_pending_tag('xSTOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)') -> False
  merge_pending_tags([]) -> None
  merge_pending_tags([False, False]) -> None
  merge_pending_tags(['TEST_ONLY_INJECTED']) -> 'TEST_ONLY_INJECTED'
  merge_pending_tags(['TEST_ONLY_INJECTED', 'F3-STEP2-EXACT-04']) -> 'F3-STEP2-EXACT-04'
  merge_pending_tags([True]) -> 'TEST_ONLY_INJECTED'
  merge_pending_tags([True, 'F3-STEP2-EXACT-04']) -> 'F3-STEP2-EXACT-04'
  merge_pending_tags([False], ['F3-STEP2-EXACT-04']) -> 'F3-STEP2-EXACT-04'
  merge_pending_tags(['TEST_ONLY_INJECTED'], [False]) -> 'TEST_ONLY_INJECTED'
  merge_pending_tags('TEST_ONLY_INJECTED') -> 'TEST_ONLY_INJECTED'
  merge_pending_tags(['SOME-OTHER-TAG', 'TEST_ONLY_INJECTED']) -> 'SOME-OTHER-TAG'

store dir exists after the run (nothing may be written): False
```

Reading. The decision layer reproduces 35 / 35 objects and the stops identically (canonical JSON), twice. The
executor's real-path test, run here, produces a record equal to the delivered one in every field, restores every
engine and global it touches, and prints nothing. Under its stubs the baseline already ends in BOTH_FAIL_REDESIGN: the
full-context cases end with p03 PENDING for both families, but the fold and probe cases end in BOTH_FAIL_REDESIGN with
the held cells carrying no verdict, so for those contexts the test cannot show an open fixture outcome; the auditor's
probe (§5.2), whose baseline passes, shows it for every context. The helper table shows the rule as implemented: only
a STOP_EXACTNESS_PENDING string sets a tag; within one criterion's contexts a natural tag wins; a decision-layer flag
(True) counts as TEST_ONLY_INJECTED. An unknown tag would pass through (last line); fit_spline emits only the two
known ones (L1195).

### 5.2 The auditor's own probe of the real path

The script r42_05_realpath_probe.py calls the unmodified run_real_scenario and evaluate_fixture on the generator's
REAL_SCENARIOS with the auditor's own stand-ins for the two fit engines (different from the executor's: family fits
return a smoothed series, spline fits valid except where a case says otherwise). The twelve cases and their expected
held cells are written in the script before the run, from the instruction read per criterion. Part 2 calls the real
fit_spline with a stand-in solver that raises, to confirm that the two strings the stand-ins use are the ones
fit_spline itself produces; the restart layer is switched off in that process only, so nothing is stored.

```text
harness sha256: b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730
REAL_SCENARIOS trajectories per sex: {'SCEN-A': {'F': 1, 'M': 1}, 'SCEN-B': {'F': 1, 'M': 1}} | declared SPL injections: {'SCEN-A': [], 'SCEN-B': [(('M', 0), 'full', 'TEST_ONLY_INJECTION'), (('M', 0), 'fold1', 'TEST_ONLY_INJECTION')]}

[SCEN-A] P1 baseline -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": [false], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PASS', 'PASS') | mechanism TERMINAL_FALLBACK_MECHANISM_P01 | stops []

[SCEN-A] P2 natural F0 fold0 -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": ["F3-STEP2-EXACT-04"], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {"P01:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops []

[SCEN-A] P3 natural M0 probeR -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": [false], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": ["F3-STEP2-EXACT-04"]}}
  pending cells: {"P01:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops []

[SCEN-A] P4 injected M0 probeR -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": [false], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": ["TEST_ONLY_INJECTED"]}}
  pending cells: {"P01:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED) | stops []

[SCEN-A] P5 injected F0 fold4 -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": ["TEST_ONLY_INJECTED"], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {"P01:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED) | stops []

[SCEN-A] P6 natural full + injected probeL, F0 -> AS EXPECTED
  flags: {"F": {"full": ["F3-STEP2-EXACT-04"], "fold": [false], "probe": ["TEST_ONLY_INJECTED"]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {"P01:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops []

[SCEN-A] P7 injected fold1 + natural fold3, F0 -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": ["F3-STEP2-EXACT-04"], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {"P01:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops []

[SCEN-A] P8 injected F0 full + natural M0 full -> AS EXPECTED
  flags: {"F": {"full": ["TEST_ONLY_INJECTED"], "fold": [false], "probe": [false]}, "M": {"full": ["F3-STEP2-EXACT-04"], "fold": [false], "probe": [false]}}
  pending cells: {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C3:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops []

[SCEN-A] P9 injected probeL + injected probeR, M0 -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": [false], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": ["TEST_ONLY_INJECTED"]}}
  pending cells: {"P01:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED) | stops []

[SCEN-A] P10 natural in every context, F0 -> AS EXPECTED
  flags: {"F": {"full": ["F3-STEP2-EXACT-04"], "fold": ["F3-STEP2-EXACT-04"], "probe": ["F3-STEP2-EXACT-04"]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {"P01:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('PENDING', 'PENDING') | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04) | stops []

[SCEN-B] P11 SCEN-B as declared (spline failures M0 full, M0 fold1) -> AS EXPECTED
  flags: {"F": {"full": [false], "fold": [false], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('FAIL', 'FAIL') | mechanism STOP_BOTH_FAIL_REDESIGN | stops ['BOTH_FAIL_REDESIGN']

[SCEN-B] P12 SCEN-B as declared + injected F0 full -> AS EXPECTED
  flags: {"F": {"full": ["TEST_ONLY_INJECTED"], "fold": [false], "probe": [false]}, "M": {"full": [false], "fold": [false], "probe": [false]}}
  pending cells: {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}
  C4a routed: none | PENDING cell with a verdict: none | p03 ('FAIL', 'FAIL') | mechanism STOP_BOTH_FAIL_REDESIGN | stops ['BOTH_FAIL_REDESIGN']

ALL STUB CASES AS EXPECTED: True | engines restored: True

== part 2: the REAL fit_spline with a raising stand-in solver (restart layer off in this process)
  AUD-PROBE-1 every mode natural                         failure 'STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)'  -> spl_pending_tag 'F3-STEP2-EXACT-04'    | captures 146 (UNRELATED 146, with TEST_ONLY 0)
  AUD-PROBE-2 every mode TEST_ONLY                       failure 'STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)' -> spl_pending_tag 'TEST_ONLY_INJECTED'   | captures 146 (UNRELATED 146, with TEST_ONLY 146)
  AUD-PROBE-3 mode 0 natural, others TEST_ONLY           failure 'STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)'  -> spl_pending_tag 'F3-STEP2-EXACT-04'    | captures 146 (UNRELATED 146, with TEST_ONLY 145)
  AUD-PROBE-4 declared injected failure                  failure 'TEST_ONLY_INJECTION_SPLINE_FAILURE'         -> spl_pending_tag False                  | captures 0 (UNRELATED 0, with TEST_ONLY 0)
  AUD-PROBE-1 every mode TEST_ONLY, id of call 1 reused  failure 'STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)'  -> spl_pending_tag 'F3-STEP2-EXACT-04'    | captures 146 (UNRELATED 146, with TEST_ONLY 146)
store dir exists (nothing may be written): False
```

Reading. All twelve cases come out as written beforehand. With a passing baseline, a natural event in any context of
a sex puts exactly the dependent criteria of that sex on hold with F3-STEP2-EXACT-04 and leaves p03 PENDING for both
families (P2, P3, P10); an injected one does the same with TEST_ONLY_INJECTED (P4, P5, P9); C4a is never held and no
held cell carries a verdict. Where both kinds reach the same criterion, the natural tag is reported (P6 for C4b, P7
for C2); across sexes each sex keeps its own tag (P8). SCEN-B's declared spline failures set no flag (P11), and an
injected event added there is held as such (P12). In part 2 the real fit_spline returns the natural tag, the injected
tag, the natural tag for a mixed sweep and the ordinary failure string for a declared failure, as the stand-ins
assume; the fifth call shows the carry-over of R42A-09.

## 6. Closure map (A-4 findings in the scope of D-7 §3)

| item | executor claim | auditor result |
|---|---|---|
| R41A-01 (a) | CLOSED | CLOSED [A] (C-08) [A-S] (C-09 … C-11) |
| R41A-01 (b) | CLOSED | CLOSED under the per-criterion reading the PI accepted by chat [X] (C-12); a PI record is open — R42A-02; disclosure — R42A-04 |
| R41A-01 (c) | CLOSED | CLOSED [A] [A-S] (C-14) |
| R41A-01 (d) | CLOSED | CLOSED [A] (C-15) |
| R41A-02 (a) (b) (c) | CLOSED | CLOSED [A] (C-17 … C-19); copy timing [X]; residue — R42A-06 (a) |
| R41A-03 | CLOSED | CLOSED [A] (C-20) |
| R41A-04 | CLOSED | PARTIALLY CLOSED — the three r4-1 hashes printed [A]; the r4-2 block incomplete — R42A-01 (a) |
| R41A-05 | CLOSED | CLOSED [A] (C-22); imprecisions — R42A-05 |
| R41A-06 | CLOSED | CLOSED [A] (C-23) |
| R41A-07, -09, -10, -11 | no action | none required; R41A-07's settlement applied (stores left in place: [A] on the process's opened-files record, physical state [X], C-25); R41A-09 corrected by R42A-10 |
| R41A-08 | NOT APPLIED | as scoped by the PI (D-7 §3) |

## 7. Register (S / T / X) and status

```text
S  none open. S-R2-1 = PI_RULE (D-5) — unchanged; nothing here reopens it
T  T-R2-2 = AUTHORIZE_RESTART (in narrowed_evidence by D-3 §8.3, whether or not the layer is used). In r4-2 one
   process computed every unit; RUN1, RUN2 and the evaluation objects read nothing from the store; the second pass
   of the INJ-EXC-* unit fixtures was served from it (R42A-03)
   R42A-02: a PI record that supersedes D-7 §3 (2) for the mixed case
X  cleanup R42A-01, R42A-03

corrections_complete      = true by its test-based definition [A]; in the auditor's view the records (R42A-01) and
                            the store-read reporting (R42A-03) are incomplete — cleanup, not blocking
mandatory_tests_all_run   = true [A] (29 mandatory, all among the 30 recorded, all passed)
deferred_decisions        = []
narrowed_evidence         = [T-R2-2]
uncovered_coverage_rows   = ["A.5 (iii) inadmissible refit"] [A]
open_findings             = [] (no natural UNRELATED event)
F3_STEP2_r4_status        = PARTIAL_PENDING_PI (agrees with the executor)
F3_STEP2 = QUALIFIED      = NOT declared ; F3_EXECUTION_READY = false ; commit = false (within the package)
```

What remains. From the PI: the two decisions that keep the status at PARTIAL_PENDING_PI — whether the narrowed
evidence of T-R2-2 is acceptable, and whether the untestable row A.5 (iii) is accepted as a recorded limitation. For
the first, this revision adds two facts: the evaluation objects, the stops and RUN1 == RUN2 were computed by a single
process without reading the store; and the layer, active in that process, did serve the second pass of three
unit-test fixtures from the store (R42A-03). D-3 §8.3 keeps T-R2-2 in narrowed_evidence by rule either way. Also from
the PI: a record for R42A-02, and whether R42A-01 and R42A-03 must be closed before the next step or may travel with
the next record. The repository commit and push the PI ordered after the revision is outside the package and was not
examined (NOT PERFORMED). Whether this end state is enough to move on is the PI's decision, not this record's.

## 8. Evidence cited (delivered files, by line)

```text
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 421            | def spl_pending_tag(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 432            | def merge_pending_tags(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 453            | return sorted(set(tags))[0]
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1086           | def fit_spline(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1187           | ctx_unrel = [c for c in EXC_CAPTURES
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1195           | tag = "TEST_ONLY_INJECTED" if all_test_only else "F3-STEP2-EXACT-04"
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1384           | def evaluate_fixture(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1427           | _tag = merge_pending_tags(dS.get("spl_pending_fold", []))
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1461           | _tag = merge_pending_tags(dS.get("spl_pending_full", []))
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1507           | _tag = merge_pending_tags(dS.get("spl_pending_full", []),
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1639           | tag = merge_pending_tags(sorted(spl_tags))
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1939           | def run_real_scenario(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2061           | spl_pending_tag(spf.get("failure")))
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2089           | fold_tags.append(spl_pending_tag(r.get("failure")))
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2102           | probe_tags.append(spl_pending_tag(r.get("failure")))
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2352           | def t_spl_pending_realpath(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2430           | CASES = [
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2497           | globals()["fit_family"], globals()["fit_spline"] = real_fit_family, real_fit_spline
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2571           | def run_exc_injection_fixtures(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2579           | p2 = _exc_injection_pass(spl)
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2999           | def main():
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3002           | assert LAUNCH_NUMBER >= 1, (
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 159            | LAUNCH_NUMBER = int(os.environ.get("F3_R42_LAUNCH", "0"))
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 141            | RESTART_LAYER_ACTIVE = True
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 170            | RESTART_STORE_DIR =
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 317            | CUSTODY_PATH = (
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3045           | assert man_hash == MANIFEST_HASH_REUSED, (
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3048           | assert _regen_hash == man_hash, (
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3057           | _CODE_ENV_FINGERPRINT[0] = hashlib.sha256(
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3088           | print("PRE_EXECUTION_CUSTODY_RECORD_VERIFIED
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3159           | spl_pending_realpath = t_spl_pending_realpath(f2m, spl, grids)
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3234           | for cr in ut_caps:
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3348           | exc_unit_phase = list(EXC_CAPTURES)
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3428           | natural_unrelated = [c for c in EXC_CAPTURES
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3556           | CURRENT_PHASE[0] = "nonregression_r4_1"
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3775           | assert record_test("T-NONREG-R4-1", _nonreg41_ok), (
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 4041           | _d7_observed = sha256_of(D7_DISPATCH_RECORD_PATH)
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 4113           | PI_dispatch_record_hash=_d7_observed,
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 4148           | assert six["PI_dispatch_record_hash"] == sha256_of(D7_DISPATCH_RECORD_PATH), (
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3943           | executor_models="claude-opus-4-8[1m]; see r4-1 report",
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 121            | | 9 | calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 123            | | 12 | provenance/f3_step2_r4-2_attempt_log_2026-09-30.md
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 102            | | **R41A-04** |
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 130            | The report and the attempt log/register hashes stand only in their sidecars and in the
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 155            | executor_models = claude-opus-4-8[1m] up to the r4-2 instrument verification
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 76             | ## 4. The R41A-01(b) reading
REG  f3_step2_class_c_pin_register_r4-2_2026-09-30. line(s) 49             | | **PIN-SPLINE-PENDING-TAG-SCOPE
REG  f3_step2_class_c_pin_register_r4-2_2026-09-30. line(s) 54             | | PIN-REVALIDATION-INCONSISTENT-U
C2   f3_step2_r4-2_preexecution_custody_attempt2_20 line(s) 93             | restart_layer_active_at_this_W3 = True (r4-2 attempt 1 is ONE process from the
LOG  f3_step2_r4-2_attempt_log_2026-09-30.md        line(s) 73             | ## ERRATUM-3
LOG  f3_step2_r4-2_attempt_log_2026-09-30.md        line(s) 164            | under `0f32c7911cf8fccb`
LOG  f3_step2_r4-2_attempt_log_2026-09-30.md        line(s) 116            | **Observation 1 (recomputed here).** With the r3 environment the custody records state
NOTE f3_step2_r4-2_attempt1_interruption_note_2026- line(s) 45             | filed in quarantine beside this note
TL   f3_step2_r4-2_transmission_list_2026-09-30.md  line(s) 59             | | launch-1 log pair, quarantine copies |
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1104           | mkey = "splmode_%s_%s_%s_%s" % (fixture_id, mask_id, m, xhash)
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 1108           | for cr in cap_recs:
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2573           | honored as TWO full deterministic passes
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2578           | p1 = _exc_injection_pass(spl)
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3135           | UNITS_READ_FROM_STORE["nr_gates"] += 1
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3237           | UNITS_READ_FROM_STORE["unit_tests"] += 1
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 3327           | UNITS_READ_FROM_STORE[run_label] += 1
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py   line(s) 2375           | (register row PIN-SPLINE-PENDING-ROUTING; r4-2 report section 4)
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 53             | re-hash at their
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 68             | units_read_from_store all 0
REP  f3_step2_correction_report_r4-2_2026-09-30.md  line(s) 178            | parents_unchanged = true
LOG  f3_step2_r4-2_attempt_log_2026-09-30.md        line(s) 40             | | 14804 | 2026-09-30 (evening) |
LOG  f3_step2_r4-2_attempt_log_2026-09-30.md        line(s) 67             | zero units from the store
REG  f3_step2_class_c_pin_register_r4-2_2026-09-30. line(s) 49             | ACCEPTED by the PI's dispatch message of 2026-09-30
INV  f3_step2_r4-2_start_state_inventory_2026-09-30 line(s) 55             | The r4 package was re-checked at the same time
TL   f3_step2_r4-2_transmission_list_2026-09-30.md  line(s) 57             | | attempt-1 interruption note |
D7   f3_step2_r4-2_pi_dispatch_record_2026-09-30.md line(s) 77             | (2) when a sex has both a natural
D7   f3_step2_r4-2_pi_dispatch_record_2026-09-30.md line(s) 83             | accepted_with_this_record = YES
INS  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTI line(s) 80             | if a sex has both kinds for the criteria
INS  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTI line(s) 91             | a natural and an injected event in the same
INS  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTI line(s) 189            | parents_unchanged with the re-hash values
INS  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTI line(s) 178            | F  f3_step2_r4-2_transmission_list_<date>.md
H    f3_step2_adequacy_harness_r4-2_2026-09-30.py sha256 b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730
REP  f3_step2_correction_report_r4-2_2026-09-30.md sha256 7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6
REG  f3_step2_class_c_pin_register_r4-2_2026-09-30.md sha256 c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c
C2   f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md sha256 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1
LOG  f3_step2_r4-2_attempt_log_2026-09-30.md sha256 b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65
NOTE f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md sha256 a4b5e176de9be9e8caa1b2145ce99e9c2539fcbea254df0a23ba2bfada470bbe
TL   f3_step2_r4-2_transmission_list_2026-09-30.md sha256 711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606
INV  f3_step2_r4-2_start_state_inventory_2026-09-30.md sha256 66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5
D7   f3_step2_r4-2_pi_dispatch_record_2026-09-30.md sha256 a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb
INS  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md sha256 d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe
```

## 9. Appendix — evidence scripts and their verbatim output

Block [1] — r42_01_reception.py:

```python
"""Evidence script 01 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). Read-only.
Reception: the delivery zip, every file in it against its own sidecar and against the r4-2 transmission list, line
endings, and the files that must be byte-identical to copies the auditor already holds."""
import hashlib, os, re, zipfile
B = "/home/claude/audit_r42/"; D = B + "zip/r4-2 teslim/"; OUT = "/mnt/user-data/outputs/"; R41 = "/home/claude/audit_r41/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
Z = B + "f3_step2_r4-2_delivery_2026-09-30.zip"
print("zip sha256 %s | bytes %d | entries %d | expected 3a93e558c78b37e3… : %s" % (sha(Z), os.path.getsize(Z), len(zipfile.ZipFile(Z).namelist()),
      sha(Z) == "3a93e558c78b37e32228498fe3ba634e6f80394ee06d6d64ea7fb33eb8855cad"))
files = sorted(f for f in os.listdir(D) if os.path.isfile(D + f))
data = [f for f in files if not f.endswith(".sha256")]; side = [f for f in files if f.endswith(".sha256")]
print("files %d | data %d | sidecars %d | every data file has a sidecar: %s | every sidecar has its file: %s" % (len(files), len(data), len(side),
      all(f + ".sha256" in side for f in data), all(s[:-7] in data for s in side)))
H = {f: sha(D + f) for f in data}
print("\n== every data file against its own sidecar (format: <64 hex>  <own name> + LF)")
bad = []
for f in data:
    t = open(D + f + ".sha256", "rb").read().decode("utf-8")
    m = re.fullmatch(r"([0-9a-f]{64})  (\S+)\n", t)
    ok = bool(m) and m.group(1) == H[f] and m.group(2) == f
    cr = open(D + f, "rb").read().count(b"\r")
    print("  %-78s %s… sidecar %s | CR %d" % (f, H[f][:12], "EQUAL" if ok else "MISMATCH %r" % t, cr))
    if not ok: bad.append(f)
print("  sidecar mismatches:", bad or "none")
tl = open(D + "f3_step2_r4-2_transmission_list_2026-09-30.md", encoding="utf-8").read()
rows = {os.path.basename(m.group(1)): m.group(2) for m in re.finditer(r"\| (?:[a-z]+/)?(\S+?\.(?:py|csv|json|md|log)) \| ([0-9a-f]{64}) \|", tl)}
print("\n== transmission list rows with a full hash: %d" % len(rows))
for f, h in sorted(rows.items()):
    print("  %-78s %s" % (f, "EQUAL" if H.get(f) == h else ("NOT IN ZIP" if f not in H else "DIFF")))
print("  data files not named with a full hash in the list:", [f for f in data if f not in rows])
print("\n== files the auditor already holds (byte identity)")
# (data copy, sidecar copy) as the auditor holds them; the r4-1 sidecars arrived in a different upload batch (recv2) than the data files
pairs = [("Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md", OUT, OUT), ("f3_step2_r4-2_pi_dispatch_record_2026-09-30.md", OUT, OUT),
         ("f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md", OUT, OUT),
         ("f3_step2_fixture_generator_r4-1_2026-09-29.py", R41 + "recv7/", R41 + "recv2/"),
         ("f3_step2_fixture_manifest_r4-1_2026-09-29.csv", R41 + "recv3/", R41 + "recv2/")]
for f, base, sbase in pairs:
    mine, mine_s = base + f, sbase + f + ".sha256"
    print("  %-72s zip == auditor copy: %s | zip sidecar == auditor sidecar (%s): %s" % (f, open(D + f, "rb").read() == open(mine, "rb").read(),
          mine_s.replace(R41, "audit_r41/").replace(OUT, "outputs/"), os.path.exists(mine_s) and open(D + f + ".sha256", "rb").read() == open(mine_s, "rb").read()))
r41nr = R41 + "recv3/f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv"
print("  r4-2 non-regression-vs-r4 CSV == r4-1's non-regression-vs-r4 CSV (41dca0ba…): %s" % (open(D + "f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv", "rb").read() == open(r41nr, "rb").read()))
```

```text
zip sha256 3a93e558c78b37e32228498fe3ba634e6f80394ee06d6d64ea7fb33eb8855cad | bytes 1409226 | entries 54 | expected 3a93e558c78b37e3… : True
files 54 | data 27 | sidecars 27 | every data file has a sidecar: True | every sidecar has its file: True

== every data file against its own sidecar (format: <64 hex>  <own name> + LF)
  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md                 d66803386791… sidecar EQUAL | CR 0
  f3_step2_adequacy_harness_r4-2_2026-09-30.py                                   b988e9628731… sidecar EQUAL | CR 0
  f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py              9e4d2803101d… sidecar EQUAL | CR 0
  f3_step2_class_c_pin_register_r4-2_2026-09-30.md                               c281e713eac7… sidecar EQUAL | CR 0
  f3_step2_correction_report_r4-2_2026-09-30.md                                  7754ba029724… sidecar EQUAL | CR 0
  f3_step2_fixture_generator_r4-1_2026-09-29.py                                  68d126cf07b1… sidecar EQUAL | CR 0
  f3_step2_fixture_manifest_r4-1_2026-09-29.csv                                  5c09c4f0811f… sidecar EQUAL | CR 0
  f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md         ad2229366139… sidecar EQUAL | CR 0
  f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md                         a4b5e176de9b… sidecar EQUAL | CR 0
  f3_step2_r4-2_attempt_log_2026-09-30.md                                        b69a59158786… sidecar EQUAL | CR 0
  f3_step2_r4-2_launch1_stderr_2026-09-30.log                                    d688ac98f061… sidecar EQUAL | CR 1220
  f3_step2_r4-2_launch1_stdout_2026-09-30.log                                    5d58afbbe845… sidecar EQUAL | CR 40
  f3_step2_r4-2_launch2_stderr_2026-09-30.log                                    df257d124c12… sidecar EQUAL | CR 1562
  f3_step2_r4-2_launch2_stdout_2026-09-30.log                                    3af46762c133… sidecar EQUAL | CR 146
  f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv                             0192f7dd9243… sidecar EQUAL | CR 38
  f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv                               41dca0ba7fab… sidecar EQUAL | CR 38
  f3_step2_r4-2_pi_dispatch_record_2026-09-30.md                                 a3e705093577… sidecar EQUAL | CR 0
  f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md                      ae0f0768d90f… sidecar EQUAL | CR 0
  f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md                      766ad7b6c5b2… sidecar EQUAL | CR 0
  f3_step2_r4-2_restart_store_manifest_2026-09-30.csv                            1082e0eb6caa… sidecar EQUAL | CR 0
  f3_step2_r4-2_start_state_inventory_2026-09-30.md                              66b08a96ca25… sidecar EQUAL | CR 0
  f3_step2_r4-2_transmission_list_2026-09-30.md                                  711e728d5dc1… sidecar EQUAL | CR 0
  f3_step2_residual_series_r4-2_2026-09-30.json                                  3ee624f3a3e0… sidecar EQUAL | CR 0
  f3_step2_results_r4-2_2026-09-30.json                                          f2a0a4d5a94d… sidecar EQUAL | CR 0
  f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv                          7e44fdf95d37… sidecar EQUAL | CR 0
  f3_step2_telemetry_r4-2_2026-09-30.csv                                         ac70eaf580ba… sidecar EQUAL | CR 0
  f3_step2_test_evidence_r4-2_2026-09-30.json                                    c156b9e0ef70… sidecar EQUAL | CR 0
  sidecar mismatches: none

== transmission list rows with a full hash: 22
  f3_step2_adequacy_harness_r4-2_2026-09-30.py                                   EQUAL
  f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py              EQUAL
  f3_step2_class_c_pin_register_r4-2_2026-09-30.md                               EQUAL
  f3_step2_correction_report_r4-2_2026-09-30.md                                  EQUAL
  f3_step2_fixture_generator_r4-1_2026-09-29.py                                  EQUAL
  f3_step2_fixture_manifest_r4-1_2026-09-29.csv                                  EQUAL
  f3_step2_r4-2_attempt_log_2026-09-30.md                                        EQUAL
  f3_step2_r4-2_launch1_stderr_2026-09-30.log                                    EQUAL
  f3_step2_r4-2_launch1_stdout_2026-09-30.log                                    EQUAL
  f3_step2_r4-2_launch2_stderr_2026-09-30.log                                    EQUAL
  f3_step2_r4-2_launch2_stdout_2026-09-30.log                                    EQUAL
  f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv                             EQUAL
  f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv                               EQUAL
  f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md                      EQUAL
  f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md                      EQUAL
  f3_step2_r4-2_restart_store_manifest_2026-09-30.csv                            EQUAL
  f3_step2_r4-2_start_state_inventory_2026-09-30.md                              EQUAL
  f3_step2_residual_series_r4-2_2026-09-30.json                                  EQUAL
  f3_step2_results_r4-2_2026-09-30.json                                          EQUAL
  f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv                          EQUAL
  f3_step2_telemetry_r4-2_2026-09-30.csv                                         EQUAL
  f3_step2_test_evidence_r4-2_2026-09-30.json                                    EQUAL
  data files not named with a full hash in the list: ['Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md', 'f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md', 'f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md', 'f3_step2_r4-2_pi_dispatch_record_2026-09-30.md', 'f3_step2_r4-2_transmission_list_2026-09-30.md']

== files the auditor already holds (byte identity)
  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md           zip == auditor copy: True | zip sidecar == auditor sidecar (outputs/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md.sha256): True
  f3_step2_r4-2_pi_dispatch_record_2026-09-30.md                           zip == auditor copy: True | zip sidecar == auditor sidecar (outputs/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md.sha256): True
  f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md   zip == auditor copy: True | zip sidecar == auditor sidecar (outputs/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md.sha256): True
  f3_step2_fixture_generator_r4-1_2026-09-29.py                            zip == auditor copy: True | zip sidecar == auditor sidecar (audit_r41/recv2/f3_step2_fixture_generator_r4-1_2026-09-29.py.sha256): True
  f3_step2_fixture_manifest_r4-1_2026-09-29.csv                            zip == auditor copy: True | zip sidecar == auditor sidecar (audit_r41/recv2/f3_step2_fixture_manifest_r4-1_2026-09-29.csv.sha256): True
  r4-2 non-regression-vs-r4 CSV == r4-1's non-regression-vs-r4 CSV (41dca0ba…): True
```

Block [2] — r42_02_package_checks.py:

```python
"""Evidence script 02 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). Read-only, tier [A]:
every check runs on the delivered r4-2 bytes and on copies of earlier packages the auditor received and verified in
earlier audits (A-1 ... A-4). Nothing here executes the harness. Sections: A custody and fingerprints; B results;
C residual series; D test evidence; E telemetry files; F store manifest; G non-regression CSVs; H launch logs;
I T-SINGLE-PROCESS (D-3 Y-01) on the delivered objects."""
import csv, collections, difflib, hashlib, json, os, re
D = "/home/claude/audit_r42/zip/r4-2 teslim/"
R41 = "/home/claude/audit_r41/"
OUT = "/mnt/user-data/outputs/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
J = lambda o: json.dumps(o, sort_keys=True)
HARN, HARN1 = D + "f3_step2_adequacy_harness_r4-2_2026-09-30.py", D + "f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py"
C1, C2 = D + "f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md", D + "f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md"
RES, RES41 = D + "f3_step2_results_r4-2_2026-09-30.json", R41 + "recv3/f3_step2_results_r4-1_2026-09-29.json"
TE, TE41 = D + "f3_step2_test_evidence_r4-2_2026-09-30.json", R41 + "recv3/f3_step2_test_evidence_r4-1_2026-09-29.json"

def field(path, name):
    for line in open(path, encoding="utf-8").read().splitlines():
        if line.startswith(name + " = "):
            return line.split(" = ", 1)[1].strip()
    return None

def const(path, name):
    m = re.search(r"^%s = (.+)$" % re.escape(name), open(path, encoding="utf-8").read(), re.M)
    return m.group(1).strip() if m else None

def fp(harness, gen, man, py="3.11.7", npv="1.26.4", spv="1.14.1", plat="Windows-10-10.0.19045-SP0", src=HARN):
    f2, sp = const(src, "F2_HASH").strip('"'), const(src, "SPL_HASH").strip('"')
    return hashlib.sha256("|".join([harness, gen, man, f2, sp, py, npv, spv, plat, "1", "1", "1"]).encode()).hexdigest()[:16]

print("== A. custody records and fingerprints")
for lab, c in (("attempt 1", C1), ("attempt 2", C2)):
    print("  %s record sha256 %s" % (lab, sha(c)))
    for k in ("harness_sha256", "generator_sha256", "manifest_sha256", "manifest_regenerated_sha256", "code_env_fingerprint",
              "attempt_number", "launch_number_of_first_launch_under_these_bytes", "supersedes_harness_sha256",
              "supersedes_custody_sha256", "supersedes_note_path", "environment"):
        print("    %-50s = %s" % (k, field(c, k)))
    print("    %-50s = %s" % ("restart_layer_active_at_this_W3 (first line)", field(c, "restart_layer_active_at_this_W3")))
h1, h2 = sha(HARN1), sha(HARN)
print("  attempt-1 harness copy sha256 %s == attempt-1 record harness_sha256: %s" % (h1, h1 == field(C1, "harness_sha256")))
print("  delivered harness sha256      %s == attempt-2 record harness_sha256: %s" % (h2, h2 == field(C2, "harness_sha256")))
print("  attempt-2 supersedes_custody_sha256 == sha256(attempt-1 record) (%s): %s" % (sha(C1), field(C2, "supersedes_custody_sha256") == sha(C1)))
print("  attempt-2 supersedes_harness_sha256 == sha256(attempt-1 harness copy): %s" % (field(C2, "supersedes_harness_sha256") == h1))
gen, man = D + "f3_step2_fixture_generator_r4-1_2026-09-29.py", D + "f3_step2_fixture_manifest_r4-1_2026-09-29.csv"
for lab, c in (("attempt 1", C1), ("attempt 2", C2)):
    print("  %s record generator/manifest == delivered reused files (68d126cf / 5c09c4f0): %s / %s" % (
        lab, field(c, "generator_sha256") == sha(gen), field(c, "manifest_sha256") == sha(man)))
print("  harness constants (source text):")
for lab, hp in (("attempt-1 copy", HARN1), ("attempt-2 (delivered)", HARN)):
    print("    %-22s ATTEMPT_NUMBER=%s RESTART_LAYER_ACTIVE=%s SUPERSEDES_HARNESS=%s SUPERSEDES_CUSTODY=%s LAUNCH_NUMBER=%s" % (
        lab, const(hp, "ATTEMPT_NUMBER"), const(hp, "RESTART_LAYER_ACTIVE"), (const(hp, "SUPERSEDES_HARNESS_SHA256") or "")[:14],
        (const(hp, "SUPERSEDES_CUSTODY_SHA256") or "")[:14], const(hp, "LAUNCH_NUMBER")))
print("    attempt-2 RESTART_STORE_DIR = %s | GEN_PATH = %s | MANIFEST_REUSED_PATH = %s" % (
    const(HARN, "RESTART_STORE_DIR"), const(HARN, "GEN_PATH"), const(HARN, "MANIFEST_REUSED_PATH")))
print("    attempt-2 CUSTODY_PATH source line(s):", re.search(r"^CUSTODY_PATH = \((.+?)\)$", open(HARN).read(), re.M | re.S).group(1).replace("\n", " "))
f1, f2 = fp(h1, sha(gen), sha(man)), fp(h2, sha(gen), sha(man))
print("  fingerprint recomputed (formula of harness line 3057; F2/SPL constants read from the harness; environment of the records):")
print("    attempt 1: %s == record %s: %s" % (f1, field(C1, "code_env_fingerprint"), f1 == field(C1, "code_env_fingerprint")))
print("    attempt 2: %s == record %s: %s" % (f2, field(C2, "code_env_fingerprint"), f2 == field(C2, "code_env_fingerprint")))
print("  instruments named in the attempt-2 record vs the auditor's own copies:")
INSTR = {"D-3": "/home/claude/prompt_r3v2/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
         "r4_instruction": "/home/claude/audit_r3/r4_dispatch/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md",
         "D-5": "/home/claude/audit_r3/r4_dispatch/f3_step2_r4_pi_dispatch_record_2026-09-24.md",
         "r4-1_instruction": "/home/claude/r41_dispatch/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md",
         "D-6": "/home/claude/r41_dispatch/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md",
         "r4-2_instruction": OUT + "Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md",
         "D-7": OUT + "f3_step2_r4-2_pi_dispatch_record_2026-09-30.md",
         "A-1": "/home/claude/audit_r3/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md",
         "A-2": "/home/claude/audit_r4/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md",
         "A-3": "/home/claude/audit_r4/r2/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md",
         "A-4": OUT + "f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md",
         "D-1": "/root/.claude/uploads/9c789a02-f865-56de-9f2f-e299f3cfca3a/892d0f75-Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md",
         "D-2": "/home/claude/audit_ws/executor_deliverables/f3_step2_pi_ratified_content_2026-09-07.md"}
for k, p in INSTR.items():
    rec = field(C2, k + "_sha256_observed")
    print("    %-17s record %s… | auditor copy %s… | equal %s" % (k, (rec or "ABSENT")[:16], sha(p)[:16], rec == sha(p)))
print("  attempt-2 record, the restart-layer line and its parenthesis as written:")
t2 = open(C2, encoding="utf-8").read().splitlines()
i = [n for n, l in enumerate(t2) if l.startswith("restart_layer_active_at_this_W3")][0]
for l in t2[i:i + 4]: print("    | " + l)
print("  harness diff attempt-1 copy -> attempt 2 (line ranges of the attempt-1 file that changed):")
a, b = open(HARN1, encoding="utf-8").read().splitlines(), open(HARN, encoding="utf-8").read().splitlines()
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if tag != "equal":
        print("    %-7s attempt-1 lines %d-%d -> attempt-2 lines %d-%d" % (tag, i1 + 1, i2, j1 + 1, j2))

print("\n== B. results (deliverable 6)")
r, r41 = json.load(open(RES)), json.load(open(RES41))
print("  sha256 %s | top-level keys %d | same key set as r4-1: %s" % (sha(RES), len(r), set(r) == set(r41)))
print("  top-level keys whose content differs from r4-1:", [k for k in sorted(r) if J(r[k]) != J(r41[k])])
se, se41 = r["solver_exceptions"], r41["solver_exceptions"]
print("  solver_exceptions: %d record(s); fields that differ from r4-1: %s" % (len(se), sorted({k for x, y in zip(se, se41) for k in x if x[k] != y.get(k)})))
e2, e1 = {e["fixture_id"]: e for e in r["evaluations"]}, {e["fixture_id"]: e for e in r41["evaluations"]}
same = [f for f in e2 if f in e1 and J(e2[f]) == J(e1[f])]
print("  evaluation objects: r4-2 %d, r4-1 %d, identical (canonical JSON) %d, only in one %s" % (len(e2), len(e1), len(same), sorted(set(e2) ^ set(e1))))
print("  stops identical to r4-1 (order-independent): %s ; in order: %s ; count %d" % (
    sorted(J(s) for s in r["stops"]) == sorted(J(s) for s in r41["stops"]), J(r["stops"]) == J(r41["stops"]), len(r["stops"])))
canon = lambda rr: hashlib.sha256(json.dumps(dict(evals=rr["evaluations"], stops=rr["stops"], pins=dict(mask_full=True, fs=True)), sort_keys=True).encode()).hexdigest()
print("  canonical RUN1 document recomputed from the delivered evaluations+stops: %s | from r4-1: %s" % (canon(r), canon(r41)))
print("  run1_canonical_sha256 %s | run2_canonical_sha256 %s | determinism %s" % (r["run1_canonical_sha256"], r["run2_canonical_sha256"], r["determinism"]))
es = r["end_state"]
print("  end_state:", J(es))
print("  PI_dispatch_record_hash == sha256(D-7 file): %s | S_R2_1_source_dispatch_record_hash == sha256(D-5 file): %s | distinct: %s" % (
    es["PI_dispatch_record_hash"] == sha(INSTR["D-7"]), es["S_R2_1_source_dispatch_record_hash"] == sha(INSTR["D-5"]),
    es["PI_dispatch_record_hash"] != es["S_R2_1_source_dispatch_record_hash"]))
print("  r4-1 end_state.PI_dispatch_record_hash (for contrast): %s" % r41["end_state"]["PI_dispatch_record_hash"])
tr = r["tests_run"]
print("  tests_run: %d entries ; all ran and passed: %s ; new vs r4-1: %s ; dropped vs r4-1: %s" % (
    len(tr), all(v == dict(passed=True, ran=True) for v in tr.values()), sorted(set(tr) - set(r41["tests_run"])), sorted(set(r41["tests_run"]) - set(tr))))
mand = re.search(r"^MANDATORY_TESTS = \[(.*?)^\]", open(HARN).read(), re.M | re.S)
mand_ids = re.findall(r'"([^"]+)"', mand.group(1)) if mand else []
print("  MANDATORY_TESTS in the harness: %d ids ; includes T-SPL-PENDING-REALPATH and T-NONREG-R4-1: %s ; every mandatory id in tests_run: %s ; recorded but not mandatory: %s" % (
    len(mand_ids), {"T-SPL-PENDING-REALPATH", "T-NONREG-R4-1"} <= set(mand_ids), set(mand_ids) <= set(tr), sorted(set(tr) - set(mand_ids))))
ec = r["expectation_checks"]
print("  expectation_checks:", J({k: ec[k] for k in ec if k != "detail"}), "| detail:", ec.get("detail"))
pr = r["process"]
print("  process:", J({k: pr[k] for k in ("pid", "start", "end", "attempt_number", "launch_number", "restart_layer_active", "supersedes_harness_sha256",
                                           "units_computed_this_process", "units_read_from_store", "spline_telemetry_calls_by_phase_pid",
                                           "spline_telemetry_call_total", "store_rows", "store_manifest_sha256", "executor_models")}))
print("  process.store_manifest_sha256 == sha256(delivered store manifest): %s" % (pr["store_manifest_sha256"] == sha(D + "f3_step2_r4-2_restart_store_manifest_2026-09-30.csv")))
cov = r["coverage"]
print("  coverage: %d rows ; identical to r4-1's: %s ; coverage_downgraded_rows %s" % (len(cov), J(cov) == J(r41["coverage"]), r["coverage_downgraded_rows"]))
print("  exactness_findings %s ; exactness_findings_closed_this_cycle %s ; engineering_findings %s" % (r["exactness_findings"], r["exactness_findings_closed_this_cycle"], r["engineering_findings"]))
paths = [str(p) for p in r["opened_files_audit_derived"]]
store = [p for p in paths if "restart_store" in p and not p.endswith(".csv")]
pref = collections.Counter(re.search(r"([0-9a-f]{16})__", p).group(1) for p in store)
print("  opened_files_audit_derived: %d entries ; store-unit paths %d (= 2 x 11,869: %s) ; store directories %s ; prefixes %s" % (
    len(paths), len(store), len(store) == 2 * 11869, sorted({p.split("\\")[0] for p in store}), dict(pref)))
print("  any opened path under an r4-1 or r4 store, or under quarantine: %s" % [p for p in paths if re.search(r"\.r4(-1)?_restart_store|quarantine", p)])

print("\n== C. residual series (deliverable 7)")
rs, rs41 = D + "f3_step2_residual_series_r4-2_2026-09-30.json", R41 + "recv3/f3_step2_residual_series_r4-1_2026-09-29.json"
print("  sha256 %s | byte-identical to r4-1's residual series (%s…): %s" % (sha(rs), sha(rs41)[:16], open(rs, "rb").read() == open(rs41, "rb").read()))

print("\n== D. test evidence (deliverable 8)")
t, t41 = json.load(open(TE)), json.load(open(TE41))
print("  sha256 %s | keys new vs r4-1: %s | removed: %s" % (sha(TE), sorted(set(t) - set(t41)), sorted(set(t41) - set(t))))
print("  shared keys whose content differs:", [k for k in sorted(set(t) & set(t41)) if J(t[k]) != J(t41[k])])
for k in ("exc_captures", "exc_captures_run2"):
    print("    %-22s fields differing from r4-1: %s" % (k, sorted({f for x, y in zip(t[k], t41[k]) for f in x if x[f] != y.get(f)})))
u, u41 = t["exc_captures_unit_phase"], t41["exc_captures_unit_phase"]
strip = lambda c: {k: v for k, v in c.items() if k not in ("pid", "start_iso", "traceback")}
print("    exc_captures_unit_phase: r4-2 %d records, r4-1 %d ; r4-2 records 1-4 == records 5-8 (every field): %s ; r4-2 records 1-4 == r4-1's 4 (pid/start/traceback aside): %s" % (
    len(u), len(u41), u[:4] == u[4:], [strip(c) for c in u[:4]] == [strip(c) for c in u41]))
print("    exc_injection_fixtures.passes_identical (the INJ-EXC-* fixtures run twice by design): %s" % t["exc_injection_fixtures"].get("passes_identical"))
sp = t["spl_pending_realpath"]
print("  spl_pending_realpath: pass_ %s ; all_cases_ok %s ; restored %s" % (sp["pass_"], sp["all_cases_ok"], J(sp["restored"])))
for c in sp["cases"]:
    print("    %-32s ok %-5s expected==got %-5s verdict cells %s | cells %s | mechanism %s" % (
        c["case"], c["ok"], c["expected"] == c["got"], c["pending_cells_with_a_verdict"], J(c["got"]), c["mechanism"]))
print("  nonregression_vs_r4_1:", J(t["nonregression_vs_r4_1"]))
print("  test-evidence tests_run == results tests_run: %s ; only in results: %s ; only in test evidence: %s ; r4-1 the same way: %s" % (
    J(t["tests_run"]) == J(r["tests_run"]), sorted(set(r["tests_run"]) - set(t["tests_run"])), sorted(set(t["tests_run"]) - set(r["tests_run"])),
    sorted(set(r41["tests_run"]) - set(t41["tests_run"]))))

print("\n== E. telemetry (deliverable 5) and per-call telemetry (item A)")
def rows(p): return list(csv.DictReader(open(p, newline="", encoding="utf-8")))
tm, tm41 = rows(D + "f3_step2_telemetry_r4-2_2026-09-30.csv"), rows(R41 + "recv3/f3_step2_telemetry_r4-1_2026-09-29.csv")
dc = sorted({k for x, y in zip(tm, tm41) for k in x if x[k] != y[k]})
print("  telemetry rows r4-2 %d / r4-1 %d ; columns that differ anywhere: %s ; all other columns equal row by row: %s" % (
    len(tm), len(tm41), dc, [tuple(v for k, v in x.items() if k not in dc) for x in tm] == [tuple(v for k, v in x.items() if k not in dc) for x in tm41]))
pc, pc41 = rows(D + "f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv"), rows(R41 + "recv3/f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv")
det = [k for k in pc[0] if k not in ("pid", "start_iso", "wall_clock_seconds")]
print("  per-call rows r4-2 %d / r4-1 %d ; (phase, pid) %s ; start_iso values %s" % (
    len(pc), len(pc41), dict(collections.Counter((x["phase"], x["pid"]) for x in pc)), sorted({x["start_iso"] for x in pc})))
print("  per-call rows equal to r4-1 row by row on %s: %s" % (det, [tuple(x[k] for k in det) for x in pc] == [tuple(x[k] for k in det) for x in pc41]))

print("\n== F. restart-store manifest (item B)")
sm, sm41 = rows(D + "f3_step2_r4-2_restart_store_manifest_2026-09-30.csv"), rows(R41 + "recv6/f3_step2_r4-1_restart_store_manifest_2026-09-29.csv")
print("  rows %d ; prefixes %s ; pids %s ; start_iso %s" % (len(sm), dict(collections.Counter(x["path"][:16] for x in sm)),
      dict(collections.Counter(x["pid"] for x in sm)), sorted({x["start_iso"] for x in sm})))
names = lambda m: sorted(x["path"].split("__", 1)[1] for x in m)
print("  unit names (prefix removed) identical to the r4-1 store manifest's (%d rows, prefix %s): %s" % (len(sm41), sm41[0]["path"][:16], names(sm) == names(sm41)))

print("\n== G. non-regression CSVs (items D and D')")
nr41 = rows(D + "f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv")
print("  vs r4-1: rows %d ; header %s ; status counts %s ; stops row present: %s" % (len(nr41), list(nr41[0].keys()),
      dict(collections.Counter(x["status"] for x in nr41)), any("stops" in x["fixture"] for x in nr41)))
nr4 = rows(D + "f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv")
print("  vs r4: rows %d ; header %s ; status counts %s ; classifications %s" % (len(nr4), list(nr4[0].keys()),
      dict(collections.Counter(x["status"] for x in nr4)), dict(collections.Counter(x["classification"] for x in nr4))))

print("\n== H. launch logs (item E)")
for n in (1, 2):
    so = open(D + "f3_step2_r4-2_launch%d_stdout_2026-09-30.log" % n, "rb").read().decode("utf-8").replace("\r\n", "\n")
    se_ = open(D + "f3_step2_r4-2_launch%d_stderr_2026-09-30.log" % n, "rb").read().decode("utf-8").replace("\r\n", "\n")
    L = so.rstrip("\n").split("\n")
    pid = re.search(r"^PID = (\d+) ; START = (\S+)", so, re.M)
    print("  launch %d stdout: %d lines ; PID %s START %s ; RESTART_LAYER_ACTIVE line %r ; custody line %r" % (
        n, len(L), pid.group(1), pid.group(2), re.search(r"^RESTART_LAYER_ACTIVE = .*$", so, re.M).group(0),
        re.search(r"^PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = .*$", so, re.M).group(0)))
    print("    LAUNCH_NUMBER line: %r ; T-SPL-PENDING-REALPATH in-run pass_: %s ; RUN_COMPLETE line: %r ; last line: %r" % (
        (re.search(r"^LAUNCH_NUMBER = .*?;", so, re.M) or [None])[0],
        json.loads(re.search(r"^T_SPL_PENDING_REALPATH = (.*)$", so, re.M).group(1))["pass_"],
        (re.search(r"^RUN_COMPLETE .*$", so, re.M) or [None])[0], L[-1][:80]))
    print("    stderr: %d lines ; Traceback count %d ; Error lines %d" % (len(se_.rstrip("\n").split("\n")), se_.count("Traceback"),
          len([l for l in se_.split("\n") if re.search(r"\b\w*Error\b", l) and "Warning" not in l])))
so2 = open(D + "f3_step2_r4-2_launch2_stdout_2026-09-30.log", "rb").read().decode("utf-8")
for key in ("NATURAL_UNRELATED_EVENTS", "NONREGRESSION_VS_R4 ", "NONREGRESSION_VS_R4_1 ", "T_EXPECT_ALL", "DETERMINISM", "COVERAGE_DERIVED", "F3_STEP2_r4_status",
            "RESULTS_WRITTEN", "TEST_EVIDENCE_WRITTEN", "RESIDUAL_SERIES_WRITTEN", "STORE_MANIFEST_WRITTEN", "PERCALL_TELEMETRY_WRITTEN", "TELEMETRY_WRITTEN"):
    m = re.search(r"^%s.*$" % re.escape(key), so2, re.M)
    print("    launch 2 | %s" % (m.group(0).strip()[:170] if m else key + " ABSENT"))
for key, f in (("RESULTS_WRITTEN", "f3_step2_results_r4-2_2026-09-30.json"), ("TEST_EVIDENCE_WRITTEN", "f3_step2_test_evidence_r4-2_2026-09-30.json"),
               ("RESIDUAL_SERIES_WRITTEN", "f3_step2_residual_series_r4-2_2026-09-30.json"), ("STORE_MANIFEST_WRITTEN", "f3_step2_r4-2_restart_store_manifest_2026-09-30.csv"),
               ("PERCALL_TELEMETRY_WRITTEN", "f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv"), ("TELEMETRY_WRITTEN", "f3_step2_telemetry_r4-2_2026-09-30.csv"),
               ("NONREGRESSION_WRITTEN", "f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv"), ("NONREGRESSION_R4_1_WRITTEN", "f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv")):
    m = re.search(r"^%s = \S+ sha256=([0-9a-f]{64})" % key, so2, re.M)
    print("    hash the process printed for %-28s == delivered file: %s" % (key, m is not None and m.group(1) == sha(D + f)))

print("\n== I. T-SINGLE-PROCESS (D-3 Y-01) on the delivered objects of deliverables 5-8 and items A/B")
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("pid", "start_iso"): yield k, v
            yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
for lab, obj in (("results", r), ("test evidence", t)):
    print("  %-14s pid/start_iso values: %s" % (lab, dict(collections.Counter(walk(obj)))))
print("  results process: pid %s start %s ; per-call pids %s ; store pids %s" % (pr["pid"], pr["start"], sorted({x["pid"] for x in pc}), sorted({x["pid"] for x in sm})))
print("  units_read_from_store all zero: %s ; launch-2 stdout PID %s and RUN_COMPLETE %s" % (
    all(v == 0 for v in pr["units_read_from_store"].values()), re.search(r"^PID = (\d+)", so2, re.M).group(1), re.search(r"^RUN_COMPLETE (\d+)", so2, re.M).group(1)))
print("  telemetry (deliverable 5) carries no pid column: %s (covered by the process block of the results it was written with)" % ("pid" not in tm[0]))
```

```text
== A. custody records and fingerprints
  attempt 1 record sha256 ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e
    harness_sha256                                     = 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74
    generator_sha256                                   = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
    manifest_sha256                                    = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
    manifest_regenerated_sha256                        = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
    code_env_fingerprint                               = 0f32c7911cf8fccb
    attempt_number                                     = 1
    launch_number_of_first_launch_under_these_bytes    = 1
    supersedes_harness_sha256                          = None
    supersedes_custody_sha256                          = None      # R41A-02(a): filled from attempt 2 on
    supersedes_note_path                               = None
    environment                                        = python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ; Windows-10-10.0.19045-SP0 ; OMP/OPENBLAS/MKL = 1
    restart_layer_active_at_this_W3 (first line)       = False (r4-2 attempt 1 is ONE process from the
  attempt 2 record sha256 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1
    harness_sha256                                     = b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730
    generator_sha256                                   = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
    manifest_sha256                                    = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
    manifest_regenerated_sha256                        = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
    code_env_fingerprint                               = 4ced291f15fb5afd
    attempt_number                                     = 2
    launch_number_of_first_launch_under_these_bytes    = env-driven (F3_R42_LAUNCH; first launch of this attempt = 2)
    supersedes_harness_sha256                          = 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74
    supersedes_custody_sha256                          = ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e
    supersedes_note_path                               = p_konum_plus/quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md
    environment                                        = python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ; Windows-10-10.0.19045-SP0 ; OMP/OPENBLAS/MKL = 1
    restart_layer_active_at_this_W3 (first line)       = True (r4-2 attempt 1 is ONE process from the
  attempt-1 harness copy sha256 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74 == attempt-1 record harness_sha256: True
  delivered harness sha256      b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 == attempt-2 record harness_sha256: True
  attempt-2 supersedes_custody_sha256 == sha256(attempt-1 record) (ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e): True
  attempt-2 supersedes_harness_sha256 == sha256(attempt-1 harness copy): True
  attempt 1 record generator/manifest == delivered reused files (68d126cf / 5c09c4f0): True / True
  attempt 2 record generator/manifest == delivered reused files (68d126cf / 5c09c4f0): True / True
  harness constants (source text):
    attempt-1 copy         ATTEMPT_NUMBER=1 RESTART_LAYER_ACTIVE=False SUPERSEDES_HARNESS=None SUPERSEDES_CUSTODY=None      # R4 LAUNCH_NUMBER=1
    attempt-2 (delivered)  ATTEMPT_NUMBER=2 RESTART_LAYER_ACTIVE=True SUPERSEDES_HARNESS="9e4d2803101de SUPERSEDES_CUSTODY="ae0f0768d90fa LAUNCH_NUMBER=int(os.environ.get("F3_R42_LAUNCH", "0"))
    attempt-2 RESTART_STORE_DIR = "p_konum_plus/calibration/.r4-2_restart_store_2026-09-30" | GEN_PATH = "p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py" | MANIFEST_REUSED_PATH = "p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv"
    attempt-2 CUSTODY_PATH source line(s): f"p_konum_plus/provenance/"                 f"f3_step2_r4-2_preexecution_custody_attempt{ATTEMPT_NUMBER}_{DATE_TAG}.md"
  fingerprint recomputed (formula of harness line 3057; F2/SPL constants read from the harness; environment of the records):
    attempt 1: 0f32c7911cf8fccb == record 0f32c7911cf8fccb: True
    attempt 2: 4ced291f15fb5afd == record 4ced291f15fb5afd: True
  instruments named in the attempt-2 record vs the auditor's own copies:
    D-3               record 5b0e19ea58ddd655… | auditor copy 5b0e19ea58ddd655… | equal True
    r4_instruction    record e12839587153cd9e… | auditor copy e12839587153cd9e… | equal True
    D-5               record 0cd87ad5b95264f6… | auditor copy 0cd87ad5b95264f6… | equal True
    r4-1_instruction  record 283ac4e29b6a42fa… | auditor copy 283ac4e29b6a42fa… | equal True
    D-6               record a92a0518dd053a54… | auditor copy a92a0518dd053a54… | equal True
    r4-2_instruction  record d668033867913f72… | auditor copy d668033867913f72… | equal True
    D-7               record a3e705093577135f… | auditor copy a3e705093577135f… | equal True
    A-1               record 11cfa591cee0a3db… | auditor copy 11cfa591cee0a3db… | equal True
    A-2               record b721702785d0eca6… | auditor copy b721702785d0eca6… | equal True
    A-3               record 9c16abb5beb112cd… | auditor copy 9c16abb5beb112cd… | equal True
    A-4               record ad22293661393f84… | auditor copy ad22293661393f84… | equal True
    D-1               record 17187d31f772a918… | auditor copy 17187d31f772a918… | equal True
    D-2               record da0c4064615263b1… | auditor copy da0c4064615263b1… | equal True
  attempt-2 record, the restart-layer line and its parenthesis as written:
    | restart_layer_active_at_this_W3 = True (r4-2 attempt 1 is ONE process from the
    |          beginning; a restart layer is introduced only after a recorded interruption of
    |          THIS revision - D-3 S8.1/S8.2/S8.3. The r4-2 store is its own directory; the r4-1
    |          and r4 stores stay where they are, untouched and unread.)
  harness diff attempt-1 copy -> attempt 2 (line ranges of the attempt-1 file that changed):
    replace attempt-1 lines 129-137 -> attempt-2 lines 129-141
    replace attempt-1 lines 139-146 -> attempt-2 lines 143-150
    replace attempt-1 lines 148-152 -> attempt-2 lines 152-161
    insert  attempt-1 lines 2991-2990 -> attempt-2 lines 3000-3006
    insert  attempt-1 lines 3909-3908 -> attempt-2 lines 3925-3927

== B. results (deliverable 6)
  sha256 f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | top-level keys 42 | same key set as r4-1: True
  top-level keys whose content differs from r4-1: ['end_state', 'opened_files_audit_derived', 'opened_files_declared', 'process', 'solver_exceptions', 'tests_run']
  solver_exceptions: 1 record(s); fields that differ from r4-1: ['pid', 'start_iso', 'traceback']
  evaluation objects: r4-2 37, r4-1 37, identical (canonical JSON) 37, only in one []
  stops identical to r4-1 (order-independent): True ; in order: True ; count 6
  canonical RUN1 document recomputed from the delivered evaluations+stops: 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 | from r4-1: 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77
  run1_canonical_sha256 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 | run2_canonical_sha256 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 | determinism True
  end_state: {"F3_STEP2_r4_status": "PARTIAL_PENDING_PI", "PI_dispatch_record_hash": "a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb", "PI_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md", "S_R2_1_source_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851", "S_R2_1_source_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md", "corrections_complete": true, "deferred_decisions": [], "mandatory_tests_all_run": true, "mandatory_tests_missing": [], "narrowed_evidence": ["T-R2-2"], "open_findings": [], "uncovered_coverage_rows": ["A.5 (iii) inadmissible refit"]}
  PI_dispatch_record_hash == sha256(D-7 file): True | S_R2_1_source_dispatch_record_hash == sha256(D-5 file): True | distinct: True
  r4-1 end_state.PI_dispatch_record_hash (for contrast): 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
  tests_run: 30 entries ; all ran and passed: True ; new vs r4-1: ['T-NONREG-R4-1', 'T-SPL-PENDING-REALPATH'] ; dropped vs r4-1: []
  MANDATORY_TESTS in the harness: 29 ids ; includes T-SPL-PENDING-REALPATH and T-NONREG-R4-1: True ; every mandatory id in tests_run: True ; recorded but not mandatory: ['T-NONREG-R4']
  expectation_checks: {"EXPECTATION_FAIL": "none", "declared": 36, "ran": 36} | detail: []
  process: {"attempt_number": 2, "end": "2026-09-30T21:36:01.300416", "executor_models": "claude-opus-4-8[1m]; see r4-1 report", "launch_number": 2, "pid": 10412, "restart_layer_active": true, "spline_telemetry_call_total": 12174, "spline_telemetry_calls_by_phase_pid": {"nr_gates/10412": 60, "run1/10412": 5256, "run2/10412": 5256, "unit_tests/10412": 1602}, "start": "2026-09-30T20:38:58.140644", "store_manifest_sha256": "1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95", "store_rows": 11869, "supersedes_harness_sha256": "9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74", "units_computed_this_process": {"nr_gates": 1, "residual_export": 1, "run1": 2, "run2": 2, "unit_tests": 1}, "units_read_from_store": {"nr_gates": 0, "residual_export": 0, "run1": 0, "run2": 0, "unit_tests": 0}}
  process.store_manifest_sha256 == sha256(delivered store manifest): True
  coverage: 64 rows ; identical to r4-1's: True ; coverage_downgraded_rows []
  exactness_findings [] ; exactness_findings_closed_this_cycle [{'id': 'F3-STEP2-EXACT-03', 'source': 'p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md', 'source_sha256': '0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851'}] ; engineering_findings []
  opened_files_audit_derived: 24033 entries ; store-unit paths 23738 (= 2 x 11,869: True) ; store directories ['p_konum_plus/calibration/.r4-2_restart_store_2026-09-30'] ; prefixes {'4ced291f15fb5afd': 23738}
  any opened path under an r4-1 or r4 store, or under quarantine: []

== C. residual series (deliverable 7)
  sha256 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | byte-identical to r4-1's residual series (3ee624f3a3e0ddb9…): True

== D. test evidence (deliverable 8)
  sha256 c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | keys new vs r4-1: ['nonregression_vs_r4_1', 'spl_pending_realpath'] | removed: []
  shared keys whose content differs: ['exc_captures', 'exc_captures_run2', 'exc_captures_unit_phase', 'tests_run']
    exc_captures           fields differing from r4-1: ['pid', 'start_iso', 'traceback']
    exc_captures_run2      fields differing from r4-1: ['pid', 'start_iso', 'traceback']
    exc_captures_unit_phase: r4-2 8 records, r4-1 4 ; r4-2 records 1-4 == records 5-8 (every field): True ; r4-2 records 1-4 == r4-1's 4 (pid/start/traceback aside): True
    exc_injection_fixtures.passes_identical (the INJ-EXC-* fixtures run twice by design): True
  spl_pending_realpath: pass_ True ; all_cases_ok True ; restored {"exc_captures": true, "fidelity_declared": true, "fidelity_executed": true, "fit_family": true, "fit_spline": true, "phase": true, "progress_counter": true, "telemetry": true}
    baseline                         ok True  expected==got True  verdict cells [] | cells {} | mechanism STOP_BOTH_FAIL_REDESIGN
    natural full                     ok True  expected==got True  verdict cells [] | cells {"P01:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04)
    natural fold                     ok True  expected==got True  verdict cells [] | cells {"P01:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism STOP_BOTH_FAIL_REDESIGN
    natural probe                    ok True  expected==got True  verdict cells [] | cells {"P01:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism STOP_BOTH_FAIL_REDESIGN
    injected full                    ok True  expected==got True  verdict cells [] | cells {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)
    injected fold                    ok True  expected==got True  verdict cells [] | cells {"P01:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | mechanism STOP_BOTH_FAIL_REDESIGN
    injected probe                   ok True  expected==got True  verdict cells [] | cells {"P01:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"} | mechanism STOP_BOTH_FAIL_REDESIGN
    declared spline failure          ok True  expected==got True  verdict cells [] | cells {} | mechanism STOP_BOTH_FAIL_REDESIGN
    natural and injected, same sex   ok True  expected==got True  verdict cells [] | cells {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"} | mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04)
  nonregression_vs_r4_1: {"baseline": "p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json", "baseline_sha256": "6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385", "compared": 37, "findings": [], "residual_series_expected": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f", "residual_series_observed": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f", "residual_series_unchanged": true, "run1_canonical_expected": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77", "run1_canonical_observed": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77", "run1_canonical_unchanged": true, "stops_equal": true}
  test-evidence tests_run == results tests_run: False ; only in results: ['T-CALLCOUNT'] ; only in test evidence: [] ; r4-1 the same way: ['T-CALLCOUNT']

== E. telemetry (deliverable 5) and per-call telemetry (item A)
  telemetry rows r4-2 12298 / r4-1 12298 ; columns that differ anywhere: ['wall_clock_seconds'] ; all other columns equal row by row: True
  per-call rows r4-2 12174 / r4-1 12174 ; (phase, pid) {('nr_gates', '10412'): 60, ('unit_tests', '10412'): 1602, ('run1', '10412'): 5256, ('run2', '10412'): 5256} ; start_iso values ['2026-09-30T20:38:58.140644']
  per-call rows equal to r4-1 row by row on ['phase', 'fixture', 'sex', 'trajectory', 'mask_id', 'mode', 'method', 'status', 'message', 'nit', 'nfev', 'njev', 'objective']: True

== F. restart-store manifest (item B)
  rows 11869 ; prefixes {'4ced291f15fb5afd': 11869} ; pids {'10412': 11869} ; start_iso ['2026-09-30T20:38:58.140644']
  unit names (prefix removed) identical to the r4-1 store manifest's (11869 rows, prefix dc228827920a9633): True

== G. non-regression CSVs (items D and D')
  vs r4-1: rows 37 ; header ['fixture', 'status', 'changed_keys', 'r4_1', 'r4_2'] ; status counts {'IDENTICAL': 37} ; stops row present: False
  vs r4: rows 37 ; header ['fixture', 'status', 'changed_keys', 'classification', 'r4', 'r4_1'] ; status counts {'IDENTICAL': 33, 'CHANGED': 1, 'NEW_IN_R4-1': 3} ; classifications {'': 33, 'EXPECTED_R4A03': 1, 'R4A-01 fixture (no r4 counterpart)': 3}

== H. launch logs (item E)
  launch 1 stdout: 40 lines ; PID 14804 START 2026-09-30T19:51:46.884861 ; RESTART_LAYER_ACTIVE line 'RESTART_LAYER_ACTIVE = False' ; custody line 'PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = true (p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md)'
    LAUNCH_NUMBER line: None ; T-SPL-PENDING-REALPATH in-run pass_: True ; RUN_COMPLETE line: None ; last line: 'PROGRESS SPL ctx 13 SCEN-A run1:F0:fold1'
    stderr: 1220 lines ; Traceback count 0 ; Error lines 0
  launch 2 stdout: 146 lines ; PID 10412 START 2026-09-30T20:38:58.140644 ; RESTART_LAYER_ACTIVE line 'RESTART_LAYER_ACTIVE = True' ; custody line 'PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = true (p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md)'
    LAUNCH_NUMBER line: 'LAUNCH_NUMBER = 2 ;' ; T-SPL-PENDING-REALPATH in-run pass_: True ; RUN_COMPLETE line: 'RUN_COMPLETE 10412' ; last line: 'RUN_COMPLETE 10412'
    stderr: 1562 lines ; Traceback count 0 ; Error lines 0
    launch 2 | NATURAL_UNRELATED_EVENTS = 0 ; exactness_findings = []
    launch 2 | NONREGRESSION_VS_R4 shared=34 new=3 dropped=0 findings=0 real_path_spline_pending=0
    launch 2 | NONREGRESSION_VS_R4_1 compared=37 findings=0 stops_equal=True
    launch 2 | T_EXPECT_ALL = declared/ran 36/36 ; EXPECTATION_FAIL = []
    launch 2 | DETERMINISM = True
    launch 2 | COVERAGE_DERIVED = 64 rows ; downgraded_to_UNCOVERED = []
    launch 2 | F3_STEP2_r4_status = PARTIAL_PENDING_PI
    launch 2 | RESULTS_WRITTEN = p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json sha256=f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba
    launch 2 | TEST_EVIDENCE_WRITTEN = p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json sha256=c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf
    launch 2 | RESIDUAL_SERIES_WRITTEN = p_konum_plus/calibration/f3_step2_residual_series_r4-2_2026-09-30.json sha256=3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f
    launch 2 | STORE_MANIFEST_WRITTEN = p_konum_plus/calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv sha256=1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87
    launch 2 | PERCALL_TELEMETRY_WRITTEN = p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv sha256=7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b0
    launch 2 | TELEMETRY_WRITTEN = p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv sha256=ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d
    hash the process printed for RESULTS_WRITTEN              == delivered file: True
    hash the process printed for TEST_EVIDENCE_WRITTEN        == delivered file: True
    hash the process printed for RESIDUAL_SERIES_WRITTEN      == delivered file: True
    hash the process printed for STORE_MANIFEST_WRITTEN       == delivered file: True
    hash the process printed for PERCALL_TELEMETRY_WRITTEN    == delivered file: True
    hash the process printed for TELEMETRY_WRITTEN            == delivered file: True
    hash the process printed for NONREGRESSION_WRITTEN        == delivered file: True
    hash the process printed for NONREGRESSION_R4_1_WRITTEN   == delivered file: True

== I. T-SINGLE-PROCESS (D-3 Y-01) on the delivered objects of deliverables 5-8 and items A/B
  results        pid/start_iso values: {('pid', 10412): 2, ('start_iso', '2026-09-30T20:38:58.140644'): 1}
  test evidence  pid/start_iso values: {('pid', 10412): 10, ('start_iso', '2026-09-30T20:38:58.140644'): 10}
  results process: pid 10412 start 2026-09-30T20:38:58.140644 ; per-call pids ['10412'] ; store pids ['10412']
  units_read_from_store all zero: True ; launch-2 stdout PID 10412 and RUN_COMPLETE 10412
  telemetry (deliverable 5) carries no pid column: True (covered by the process block of the results it was written with)
```

Block [3] — r42_03_text_checks.py:

```python
"""Evidence script 03 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). Read-only, tier [A]:
the narrative deliverables against the bytes they describe -- report (hash block, response table, quotes, process
note), register, start-state inventory, transmission list, interruption note, attempt log and its ERRATUM-3 (each
point recomputed or looked up in the auditor's own copies of the r3 and r4 files)."""
import csv, collections, hashlib, json, os, re
D = "/home/claude/audit_r42/zip/r4-2 teslim/"
R41 = "/home/claude/audit_r41/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
txt = lambda p: open(p, encoding="utf-8").read()
REP, REG = D + "f3_step2_correction_report_r4-2_2026-09-30.md", D + "f3_step2_class_c_pin_register_r4-2_2026-09-30.md"
INV, TL = D + "f3_step2_r4-2_start_state_inventory_2026-09-30.md", D + "f3_step2_r4-2_transmission_list_2026-09-30.md"
LOG, NOTE = D + "f3_step2_r4-2_attempt_log_2026-09-30.md", D + "f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md"
RES = D + "f3_step2_results_r4-2_2026-09-30.json"
H = {f: sha(D + f) for f in os.listdir(D) if not f.endswith(".sha256")}
byname = lambda frag: [f for f in H if frag in f]

print("== J1. report hash block (section 6) against the delivered files")
rep = txt(REP)
blk = rep.split("## 6. Hash block")[1].split("**Correction of the r4-1 report")[0]
for m in re.finditer(r"^\| (\S+) \| (\S+?)(?: \(.*?\))? \| (.+?) \|$", blk, re.M):
    item, path, val = m.group(1), m.group(2), m.group(3).strip()
    if item in ("#", "---"): continue
    name = os.path.basename(path)
    full = re.fullmatch(r"[0-9a-f]{64}", val)
    status = ("EQUAL" if H.get(name) == val else "DIFF") if full else "NO HASH PRINTED: %r" % val[:60]
    print("  %-3s %-70s %s" % (item, name[:70], status))
print("  report sha256 %s ; deliverables whose hash the block does not print: register %s…, attempt log %s…, interruption note %s…" % (
    sha(REP)[:16], H["f3_step2_class_c_pin_register_r4-2_2026-09-30.md"][:16], H["f3_step2_r4-2_attempt_log_2026-09-30.md"][:16],
    H["f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md"][:16]))
print("  the report's own explanation:", re.search(r"The report and the attempt log/register hashes stand only.*?values\)\.", rep, re.S).group(0).replace("\n", " "))
rh = sha(REP)
print("  circularity check -- delivered files that contain the report's hash (full, or its first 16 hex):",
      [f for f in sorted(H) if f != os.path.basename(REP) and rh[:16] in open(D + f, "rb").read().decode("utf-8", "replace")])
print("  files that contain the register's / attempt log's hash:",
      {lab: [f for f in H if f.endswith(".md") and h in txt(D + f)] for lab, h in (("register", H["f3_step2_class_c_pin_register_r4-2_2026-09-30.md"]),
                                                                              ("attempt log", H["f3_step2_r4-2_attempt_log_2026-09-30.md"]))})
row = [l for l in rep.splitlines() if l.startswith("| **R41A-04**")][0]
print("  response-table row R41A-04:", row)

print("\n== J2. the three r4-1 hashes printed as the correction of the r4-1 report (R41A-04)")
for lab, p in (("register", R41 + "recv6/f3_step2_class_c_pin_register_r4-1_2026-09-29.md"), ("start-state inventory", R41 + "recv7/f3_step2_r4-1_start_state_inventory_2026-09-29.md"),
               ("attempt log", R41 + "recv6/f3_step2_r4-1_attempt_log_2026-09-29.md")):
    h = sha(p)
    print("  %-22s auditor copy %s | printed in the r4-2 report: %s" % (lab, h, h in rep.split("**Correction of the r4-1 report")[1]))
r41rep = txt(R41 + "recv6/f3_step2_correction_report_r4-1_2026-09-29.md")
print("  r4-1 report still at e7939a22… (non-retroactivity): %s" % sha(R41 + "recv6/f3_step2_correction_report_r4-1_2026-09-29.md").startswith("e7939a22"))

print("\n== J3. quotes and process statements in the report")
PI_ACCEPT = "R41A-01 (b) için kriter bazındaki okuman kabul; register satırında ve raporda açıkça yaz. Devam et."
print("  the PI's acceptance message (text the PI said he would send, Cowork session 2026-09-30) quoted verbatim in report section 1: %s" % (PI_ACCEPT in rep))
print("  the same acceptance quoted (short form) in the register row PIN-SPLINE-PENDING-TAG-SCOPE: %s" % ('"R41A-01 (b) için kriter bazındaki okuman kabul"' in txt(REG)))
r = json.load(open(RES))
print("  report section 8 executor_models: %r" % re.search(r"executor_models = (.*?)\n\s+(?:model -- this|commit note)", rep, re.S).group(1).replace("\n", " ")[:220])
print("  results process.executor_models: %r" % r["process"]["executor_models"])
for claim in ("12,174", "11,869", "20:38:58", "21:36:01", "pid 10412", "nr_gates 60", "unit_tests 1602", "run1 5256", "run2 5256"):
    print("  report mentions %-16s : %s" % (claim, claim in rep))

print("\n== J4. register")
reg = txt(REG)
for k, v in (("parent 45a10494…", sha(R41 + "recv6/f3_step2_class_c_pin_register_r4-1_2026-09-29.md")), ("harness", H["f3_step2_adequacy_harness_r4-2_2026-09-30.py"]),
             ("D-7", sha("/mnt/user-data/outputs/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md")), ("results", H["f3_step2_results_r4-2_2026-09-30.json"]),
             ("generator", H["f3_step2_fixture_generator_r4-1_2026-09-29.py"]), ("manifest", H["f3_step2_fixture_manifest_r4-1_2026-09-29.csv"])):
    print("  register names %-17s %s… : %s" % (k, v[:16], v in reg))
print("  amended/new rows:", re.findall(r"^\| (?:\*\*)?(PIN-[A-Z0-9-]+)", reg, re.M))
stop = [s for s in r["stops"] if s["fixture"] == "INJ-U-POST-CONSTRUCTION-INVALID"][0]
print("  delivered stop record INJ-U-POST-CONSTRUCTION-INVALID: %s" % json.dumps(stop, sort_keys=True))
print("  register R41A-06 text names (F, P01, 0) and (M, P01, 0) and the first hit's sex (F): %s" % (
    "(F, P01, 0) and (M, P01, 0)" in reg and "FIRST hit (F)" in reg))
print("  report R41A-06 row names the same: %s" % ("(F, P01, 0) and (M, P01, 0)" in rep and "first hit's (F)" in rep))
print("  pairs in the record = [(F,P01,0),(M,P01,0)] and record sex = F: %s" % (
    [(p["sex"], p["fitter"], p["observation"]) for p in stop["offending_pairs"]] == [("F", "P01", 0), ("M", "P01", 0)] and stop["sex"] == "F"))

print("\n== J5. start-state inventory against the auditor's copies")
inv = txt(INV)
COP = {"f3_step2_adequacy_harness_r4-1_2026-09-29.py": R41 + "recv4/", "f3_step2_fixture_generator_r4-1_2026-09-29.py": R41 + "recv7/",
       "f3_step2_fixture_manifest_r4-1_2026-09-29.csv": R41 + "recv3/", "f3_step2_r4-1_preexecution_custody_2026-09-29.md": R41 + "recv4/",
       "f3_step2_results_r4-1_2026-09-29.json": R41 + "recv3/", "f3_step2_test_evidence_r4-1_2026-09-29.json": R41 + "recv3/",
       "f3_step2_class_c_pin_register_r4-1_2026-09-29.md": R41 + "recv6/", "f3_step2_correction_report_r4-1_2026-09-29.md": R41 + "recv6/",
       "f3_step2_r4-1_start_state_inventory_2026-09-29.md": R41 + "recv7/", "f3_step2_r4-1_attempt_log_2026-09-29.md": R41 + "recv6/",
       "f3_step2_r4-1_transmission_list_2026-09-29.md": R41 + "recv/", "f3_step2_r4-1_transmission_supplement_2026-09-30.md": R41 + "recv6/"}
for m in re.finditer(r"^\| \S+ \| \S+/(\S+) \| ([0-9a-f]{64}) \|$", inv, re.M):
    f, h = m.group(1), m.group(2)
    print("  %-58s inventory %s… | auditor copy equal: %s" % (f, h[:12], f in COP and sha(COP[f] + f) == h))
OUTD = "/mnt/user-data/outputs/"
ICOP = {"r4-2 instruction": OUTD + "Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md",
        "D-7 (r4-2 dispatch record)": OUTD + "f3_step2_r4-2_pi_dispatch_record_2026-09-30.md",
        "A-4 (r4-1 audit DRAFT r1; input, not directive)": OUTD + "f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md",
        "r4-1 instruction (standing)": "/home/claude/r41_dispatch/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md",
        "r4 instruction (standing)": "/home/claude/audit_r3/r4_dispatch/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md",
        "D-3 (standing)": "/home/claude/prompt_r3v2/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
        "D-1 v6 (standing)": "/root/.claude/uploads/9c789a02-f865-56de-9f2f-e299f3cfca3a/892d0f75-Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md",
        "D-2 content (standing)": "/home/claude/audit_ws/executor_deliverables/f3_step2_pi_ratified_content_2026-09-07.md",
        "D-5 (S-R2-1 source)": "/home/claude/audit_r3/r4_dispatch/f3_step2_r4_pi_dispatch_record_2026-09-24.md",
        "D-6 (parent of D-7)": "/home/claude/r41_dispatch/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md"}
for m in re.finditer(r"^\| ([^|]+?) \| ([0-9a-f]{64}) \| ([^|]+) \|$", inv, re.M):
    lab = m.group(1).strip()
    print("  instrument %-50s %s… == auditor copy: %s" % (lab[:50], m.group(2)[:12], lab in ICOP and sha(ICOP[lab]) == m.group(2)))

print("\n== J6. interruption note and attempt log against the logs, custody records and results")
note, log = txt(NOTE), txt(LOG)
so1 = open(D + "f3_step2_r4-2_launch1_stdout_2026-09-30.log", "rb").read().decode("utf-8").replace("\r\n", "\n")
print("  note last_progress_stdout %r == launch-1 last line: %s ; note 'stdout 40 lines' == %d" % (
    re.search(r'last_progress_stdout\s+= "(.*?)"', note).group(1), re.search(r'last_progress_stdout\s+= "(.*?)"', note).group(1) == so1.rstrip("\n").split("\n")[-1],
    len(so1.rstrip("\n").split("\n"))))
for k in ("harness_sha256", "generator_sha256", "manifest_sha256", "custody_sha256", "code_env_fingerprint"):
    v = re.search(r"^%s\s+= (\S+)" % k, note, re.M).group(1)
    print("  note %-22s %s" % (k, v))
print("  attempt log: pid 14804 and 10412 named: %s ; launch-2 start/end equal results process: %s" % (
    "| 14804 |" in log and "| 10412 |" in log, "2026-09-30T20:38:58" in log and "21:36:01" in log and r["process"]["start"].startswith("2026-09-30T20:38:58") and r["process"]["end"].startswith("2026-09-30T21:36:01")))

print("\n== J7. ERRATUM-3 (R41A-05) point by point")
R3LOG = "/home/claude/audit_r3/recv2/f3_step2_r3_attempt_log_2026-09-22.md"
A8 = "/home/claude/audit_r4/recv7/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md"
R4LOG = "/home/claude/audit_r4/recv/f3_step2_r4_attempt_log_2026-09-24.md"
NOTE8 = "/home/claude/audit_r4/recv7/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md"
H5 = "/home/claude/audit_r4/recv7/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py"
R3H = "/home/claude/audit_r3/recv2/f3_step2_adequacy_harness_r3_2026-09-22.py"
print("  r3 attempt log: auditor copy %s ; ERRATUM-3 names 253163891bab…: %s" % (sha(R3LOG), sha(R3LOG) in log))
r3l = txt(R3LOG).splitlines()
for n in ("6", "7", "8"):
    l = [x for x in r3l if x.startswith("| %s | " % n)][0]
    print("    r3 log row %s, harness column: %s" % (n, l.split(" | ")[1][:120]))
print("  ATTEMPT8-labelled custody: auditor copy %s ; ERRATUM-3 names 2e55e150…: %s" % (sha(A8), sha(A8) in log))
fld = lambda p, k: (re.search(r"^%s = (\S+)" % k, txt(p), re.M) or [None, None])[1]
for k in ("attempt_number", "harness_sha256", "generator_sha256", "manifest_sha256", "code_env_fingerprint", "supersedes_harness_sha256"):
    v = fld(A8, k)
    print("    %-26s = %-66s quoted in ERRATUM-3: %s" % (k, v, (v in log) if k != "supersedes_harness_sha256" else "(not cited)"))
env = json.load(open("/home/claude/audit_r3/recv2/f3_step2_results_r3_2026-09-22.json"))["environment"]
print("  r3 environment as the r3 results JSON states it: %s" % json.dumps(env, sort_keys=True))
print("  r3 custody records carry an environment line: %s" % any("numpy" in txt(p) for p in (A8, "/home/claude/audit_r3/recv2/f3_step2_r3_preexecution_custody_2026-09-22.md")))
C = lambda s: re.search(r'^%s = "([0-9a-f]{64})"' % s, txt(R3H), re.M).group(1)
def fp(hh, g, m):
    return hashlib.sha256("|".join([hh, g, m, C("F2_HASH"), C("SPL_HASH"), env["python"], env["numpy"], env["scipy"], env["platform"],
                                    env["OMP"], env["OPENBLAS"], env["MKL"]]).encode()).hexdigest()[:16]
HX = dict(h5fea="5fea165cf59358d6dab8aa942e0fee75c3ff9cf6a7bc16d672e622bf7c68be77", h390="390f42b72971030033c6964731d699358a1547bf9093b8e949c0e338e6bc0336",
          hf88="f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5", gcc="cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8",
          m9c="9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a", ge35="e35c2bf06ee4087bac97bd5b6e81d35d079ff1dddf8d2e68555c6c7d18859638",
          m45="4544ff7565165f7541c0264b886bc2692374caf2ee875ec65a877c1a2909ec33")
print("  r3 FINAL harness file in the auditor's r3 copy is 5fea165c…: %s ; e35c2bf0/4544ff75 named in the r3 pre-flight custody record: %s" % (
    sha(R3H) == HX["h5fea"], HX["ge35"] in txt("/home/claude/audit_r3/recv/f3_step2_r3_preexecution_custody_2026-09-22.md") and HX["m45"] in txt("/home/claude/audit_r3/recv/f3_step2_r3_preexecution_custody_2026-09-22.md")))
tab = {m.group(3): None for m in re.finditer(r"^\| (\S+)… \(.*?\) \| (\S+)… / (\S+)… \| \*{0,2}([0-9a-f]{16})\*{0,2} \|$", log, re.M)}
rows6 = re.findall(r"^\| ([0-9a-f]{8})… [^|]*\| ([0-9a-f]{8})… / ([0-9a-f]{8})… \| \*{0,2}([0-9a-f]{16})\*{0,2} \|$", log, re.M)
full = {v[:8]: v for v in HX.values()}
for hh, g, m, claimed in rows6:
    got = fp(full[hh], full[g], full[m])
    print("    fingerprint(%s…, %s…, %s…) recomputed %s | ERRATUM-3 %s | equal %s" % (hh, g, m, got, claimed, got == claimed))
sm3 = list(csv.DictReader(open("/home/claude/audit_r3/recv2/f3_step2_r3_restart_store_manifest_2026-09-22.csv", newline="")))
print("  r3 store manifest (delivered with r3, %s…): %d rows ; prefixes %s" % (sha("/home/claude/audit_r3/recv2/f3_step2_r3_restart_store_manifest_2026-09-22.csv")[:16],
      len(sm3), dict(collections.Counter(x["path"].replace("\\", "/").split("/")[-1][:16] for x in sm3))))
for q in ("resumed from the restart store", "RUN1's real-scenario fixtures were already cached", "from attempt 6"):
    print("  attempt-8 note contains %r: %s" % (q, q in " ".join(txt(NOTE8).split())))
print("  r4 attempt log: auditor copy %s ; ERRATUM-3 names it: %s ; contains 'matching no combination named in any r3 file': %s" % (
    sha(R4LOG)[:16], sha(R4LOG) in log, "matching no combination named in any r3 file" in " ".join(txt(R4LOG).split())))
print("  the ATTEMPT5-labelled harness in the auditor's r4 copies is f882b922…: %s" % (sha(H5) == HX["hf88"]))
for lab, p, pre in (("r4 store manifest", "/home/claude/audit_r4/recv/f3_step2_r4_restart_store_manifest_2026-09-24.csv", "5ef61a41"),
                    ("r4-1 store manifest", R41 + "recv6/f3_step2_r4-1_restart_store_manifest_2026-09-29.csv", "dc228827"),
                    ("r4-2 store manifest", D + "f3_step2_r4-2_restart_store_manifest_2026-09-30.csv", "4ced291f")):
    ps = sorted({x["path"].replace("\\", "/").split("/")[-1][:16] for x in csv.DictReader(open(p, newline=""))})
    print("  %-20s prefixes %s" % (lab, ps))
m = re.search(r"r4 under `(\S+?)…`, r4-1 under `(\S+?)…` and r4-2\s+under `(\S+?)`", log)
print("  ERRATUM-3 'scope of impact' names: r4 %s, r4-1 %s, r4-2 %s" % m.groups())
```

```text
== J1. report hash block (section 6) against the delivered files
  1   f3_step2_adequacy_harness_r4-2_2026-09-30.py                           EQUAL
  2   f3_step2_fixture_generator_r4-1_2026-09-29.py                          EQUAL
  3   f3_step2_fixture_manifest_r4-1_2026-09-29.csv                          EQUAL
  4   f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md              EQUAL
  4'  f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md              EQUAL
  5   f3_step2_telemetry_r4-2_2026-09-30.csv                                 EQUAL
  6   f3_step2_results_r4-2_2026-09-30.json                                  EQUAL
  7   f3_step2_residual_series_r4-2_2026-09-30.json                          EQUAL
  8   f3_step2_test_evidence_r4-2_2026-09-30.json                            EQUAL
  9   f3_step2_class_c_pin_register_r4-2_2026-09-30.md                       NO HASH PRINTED: '(sidecar; see transmission list)'
  11  f3_step2_r4-2_start_state_inventory_2026-09-30.md                      EQUAL
  12  f3_step2_r4-2_attempt_log_2026-09-30.md                                NO HASH PRINTED: '(sidecar; see transmission list)'
  A   f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv                  EQUAL
  B   f3_step2_r4-2_restart_store_manifest_2026-09-30.csv                    EQUAL
  D   f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv                     EQUAL
  D'  f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv                       EQUAL
  report sha256 7754ba029724231d ; deliverables whose hash the block does not print: register c281e713eac753ea…, attempt log b69a591587867e43…, interruption note a4b5e176de9be9e8…
  the report's own explanation: The report and the attempt log/register hashes stand only in their sidecars and in the transmission list (no self-hash; items 9/12 were finalized after this block's other values).
  circularity check -- delivered files that contain the report's hash (full, or its first 16 hex): ['f3_step2_r4-2_transmission_list_2026-09-30.md']
  files that contain the register's / attempt log's hash: {'register': ['f3_step2_r4-2_transmission_list_2026-09-30.md'], 'attempt log': ['f3_step2_r4-2_transmission_list_2026-09-30.md']}
  response-table row R41A-04: | **R41A-04** | **CLOSED** | the hash block in §6 prints every r4-2 deliverable except this report, AND the three r4-1 hashes A-4 names (register 45a10494…, inventory fedd964a…, attempt log ee5b4862…) as the correction of the r4-1 report §2 (which stays unmodified) |

== J2. the three r4-1 hashes printed as the correction of the r4-1 report (R41A-04)
  register               auditor copy 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 | printed in the r4-2 report: True
  start-state inventory  auditor copy fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 | printed in the r4-2 report: True
  attempt log            auditor copy ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 | printed in the r4-2 report: True
  r4-1 report still at e7939a22… (non-retroactivity): True

== J3. quotes and process statements in the report
  the PI's acceptance message (text the PI said he would send, Cowork session 2026-09-30) quoted verbatim in report section 1: True
  the same acceptance quoted (short form) in the register row PIN-SPLINE-PENDING-TAG-SCOPE: True
  report section 8 executor_models: "claude-opus-4-8[1m] up to the r4-2 instrument verification; claude-fable-5                   (Fable 5) from the r4-2 scope execution on (the session's configured                   model changed mid-revision); the harness"
  results process.executor_models: 'claude-opus-4-8[1m]; see r4-1 report'
  report mentions 12,174           : True
  report mentions 11,869           : True
  report mentions 20:38:58         : True
  report mentions 21:36:01         : True
  report mentions pid 10412        : True
  report mentions nr_gates 60      : True
  report mentions unit_tests 1602  : True
  report mentions run1 5256        : True
  report mentions run2 5256        : True

== J4. register
  register names parent 45a10494…  45a10494eb8938a8… : True
  register names harness           b988e9628731f6d0… : True
  register names D-7               a3e705093577135f… : True
  register names results           f2a0a4d5a94de0e9… : True
  register names generator         68d126cf07b11b84… : True
  register names manifest          5c09c4f0811fa51b… : True
  amended/new rows: ['PIN-SPLINE-PENDING-ROUTING', 'PIN-SPLINE-PENDING-TAG-SCOPE', 'PIN-SPL-PENDING-REALPATH-STUBS', 'PIN-NONREGRESSION-VS-R4-1', 'PIN-CUSTODY-PER-ATTEMPT', 'PIN-END-STATE-DISPATCH', 'PIN-REVALIDATION-INCONSISTENT-U']
  delivered stop record INJ-U-POST-CONSTRUCTION-INVALID: {"fixture": "INJ-U-POST-CONSTRUCTION-INVALID", "level": "C2", "member": 0, "offending_pairs": [{"fitter": "P01", "observation": 0, "sex": "F"}, {"fitter": "P01", "observation": 0, "sex": "M"}], "sex": "F", "stop": "CONTRACT_VIOLATION_INCONSISTENT_U"}
  register R41A-06 text names (F, P01, 0) and (M, P01, 0) and the first hit's sex (F): True
  report R41A-06 row names the same: True
  pairs in the record = [(F,P01,0),(M,P01,0)] and record sex = F: True

== J5. start-state inventory against the auditor's copies
  f3_step2_adequacy_harness_r4-1_2026-09-29.py               inventory 4e0dc8cfb815… | auditor copy equal: True
  f3_step2_fixture_generator_r4-1_2026-09-29.py              inventory 68d126cf07b1… | auditor copy equal: True
  f3_step2_fixture_manifest_r4-1_2026-09-29.csv              inventory 5c09c4f0811f… | auditor copy equal: True
  f3_step2_r4-1_preexecution_custody_2026-09-29.md           inventory 3bc4e5784b7d… | auditor copy equal: True
  f3_step2_results_r4-1_2026-09-29.json                      inventory 6dd4185b895d… | auditor copy equal: True
  f3_step2_test_evidence_r4-1_2026-09-29.json                inventory f74dccf0dfaa… | auditor copy equal: True
  f3_step2_class_c_pin_register_r4-1_2026-09-29.md           inventory 45a10494eb89… | auditor copy equal: True
  f3_step2_correction_report_r4-1_2026-09-29.md              inventory e7939a220b26… | auditor copy equal: True
  f3_step2_r4-1_start_state_inventory_2026-09-29.md          inventory fedd964a95da… | auditor copy equal: True
  f3_step2_r4-1_attempt_log_2026-09-29.md                    inventory ee5b48623a84… | auditor copy equal: True
  f3_step2_r4-1_transmission_list_2026-09-29.md              inventory 31b27c28383c… | auditor copy equal: True
  f3_step2_r4-1_transmission_supplement_2026-09-30.md        inventory 0b3f4358c1ea… | auditor copy equal: True
  instrument r4-2 instruction                                   d66803386791… == auditor copy: True
  instrument D-7 (r4-2 dispatch record)                         a3e705093577… == auditor copy: True
  instrument A-4 (r4-1 audit DRAFT r1; input, not directive)    ad2229366139… == auditor copy: True
  instrument r4-1 instruction (standing)                        283ac4e29b6a… == auditor copy: True
  instrument r4 instruction (standing)                          e12839587153… == auditor copy: True
  instrument D-3 (standing)                                     5b0e19ea58dd… == auditor copy: True
  instrument D-1 v6 (standing)                                  17187d31f772… == auditor copy: True
  instrument D-2 content (standing)                             da0c40646152… == auditor copy: True
  instrument D-5 (S-R2-1 source)                                0cd87ad5b952… == auditor copy: True
  instrument D-6 (parent of D-7)                                a92a0518dd05… == auditor copy: True

== J6. interruption note and attempt log against the logs, custody records and results
  note last_progress_stdout 'PROGRESS SPL ctx 13 SCEN-A run1:F0:fold1' == launch-1 last line: True ; note 'stdout 40 lines' == 40
  note harness_sha256         9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74
  note generator_sha256       68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
  note manifest_sha256        5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
  note custody_sha256         ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e
  note code_env_fingerprint   0f32c7911cf8fccb
  attempt log: pid 14804 and 10412 named: True ; launch-2 start/end equal results process: True

== J7. ERRATUM-3 (R41A-05) point by point
  r3 attempt log: auditor copy 253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5 ; ERRATUM-3 names 253163891bab…: True
    r3 log row 6, harness column: 4 (`f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5`, P-1..P-7 corrections)
    r3 log row 7, harness column: 4 (same bytes as #6)
    r3 log row 8, harness column: 4 (same bytes as #6, resumed via absolute path)
  ATTEMPT8-labelled custody: auditor copy 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657 ; ERRATUM-3 names 2e55e150…: True
    attempt_number             = 4                                                                  quoted in ERRATUM-3: True
    harness_sha256             = 390f42b72971030033c6964731d699358a1547bf9093b8e949c0e338e6bc0336   quoted in ERRATUM-3: True
    generator_sha256           = cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8   quoted in ERRATUM-3: True
    manifest_sha256            = 9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a   quoted in ERRATUM-3: True
    code_env_fingerprint       = 548ae790f6ac756a                                                   quoted in ERRATUM-3: True
    supersedes_harness_sha256  = f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5   quoted in ERRATUM-3: (not cited)
  r3 environment as the r3 results JSON states it: {"MKL": "1", "OMP": "1", "OPENBLAS": "1", "numpy": "1.26.4", "platform": "Windows-10-10.0.19045-SP0", "python": "3.11.7", "scipy": "1.14.1"}
  r3 custody records carry an environment line: False
  r3 FINAL harness file in the auditor's r3 copy is 5fea165c…: True ; e35c2bf0/4544ff75 named in the r3 pre-flight custody record: True
    fingerprint(5fea165c…, cc23c9b5…, 9c944543…) recomputed 1ba561daefb48b2e | ERRATUM-3 1ba561daefb48b2e | equal True
    fingerprint(390f42b7…, cc23c9b5…, 9c944543…) recomputed 548ae790f6ac756a | ERRATUM-3 548ae790f6ac756a | equal True
    fingerprint(f882b922…, cc23c9b5…, 9c944543…) recomputed e3ccc7d133c9ff2f | ERRATUM-3 e3ccc7d133c9ff2f | equal True
    fingerprint(f882b922…, e35c2bf0…, 4544ff75…) recomputed 9bb07bae05cdeb5e | ERRATUM-3 9bb07bae05cdeb5e | equal True
    fingerprint(390f42b7…, e35c2bf0…, 4544ff75…) recomputed e965ecee77046155 | ERRATUM-3 e965ecee77046155 | equal True
    fingerprint(5fea165c…, e35c2bf0…, 4544ff75…) recomputed f399c3d0b0398816 | ERRATUM-3 f399c3d0b0398816 | equal True
  r3 store manifest (delivered with r3, 933dcaeeb979ae28…): 23446 rows ; prefixes {'1ba561daefb48b2e': 11723, '548ae790f6ac756a': 11723}
  attempt-8 note contains 'resumed from the restart store': True
  attempt-8 note contains "RUN1's real-scenario fixtures were already cached": True
  attempt-8 note contains 'from attempt 6': True
  r4 attempt log: auditor copy 8409014748679248 ; ERRATUM-3 names it: True ; contains 'matching no combination named in any r3 file': True
  the ATTEMPT5-labelled harness in the auditor's r4 copies is f882b922…: True
  r4 store manifest    prefixes ['5ef61a412c6bd76c']
  r4-1 store manifest  prefixes ['dc228827920a9633']
  r4-2 store manifest  prefixes ['4ced291f15fb5afd']
  ERRATUM-3 'scope of impact' names: r4 5ef61a41, r4-1 dc228827, r4-2 0f32c7911cf8fccb
```

Block [4] — r42_04_decision_layer_repro.py (output in §5.1):

```python
"""Evidence script 04 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). [A-S] auditor-environment
reproduction of the platform-independent parts with the UNMODIFIED r4-2 harness (b988e962...) and the reused r4-1
generator (68d126cf...): (a) evaluate_fixture on every decision-layer fixture in generator order, twice in one
process, compared with the delivered r4-2 evaluation objects and stops; (b) the pure unit tests t_a5_support,
t_comparator_nan, ut_uset_construction against the delivered test evidence; (c) the executor's own
t_spl_pending_realpath (R41A-01 (c)) executed here and compared case by case with the delivered record; (d) the two
new helper functions spl_pending_tag / merge_pending_tags on a truth table. main() is NOT called; no real fit is run;
nothing is written under the repository mirror (asserted)."""
import importlib.util, sys, json, hashlib, os, warnings, io, contextlib
warnings.filterwarnings("ignore")
HP = "G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py"
spec = importlib.util.spec_from_file_location("h_r42", HP); h = importlib.util.module_from_spec(spec); sys.modules["h_r42"] = h; spec.loader.exec_module(h)
gs = importlib.util.spec_from_file_location(h.GEN_MODULE_NAME, h.GEN_PATH); gen = importlib.util.module_from_spec(gs); sys.modules[h.GEN_MODULE_NAME] = gen; gs.loader.exec_module(gen)
import numpy as np, scipy, platform
print("environment: python %s numpy %s scipy %s %s ; cwd %s" % (platform.python_version(), np.__version__, scipy.__version__, platform.platform(), os.getcwd()))
print("harness sha256:", hashlib.sha256(open(h.__file__, "rb").read()).hexdigest(), "| GEN_PATH", h.GEN_PATH)
print("generator sha256:", hashlib.sha256(open(h.GEN_PATH, "rb").read()).hexdigest())
print("RESTART_LAYER_ACTIVE as delivered:", h.RESTART_LAYER_ACTIVE, "| store dir", h.RESTART_STORE_DIR, "| exists before:", os.path.isdir(h.RESTART_STORE_DIR))
D = "/home/claude/audit_r42/zip/r4-2 teslim/"
R = json.load(open(D + "f3_step2_results_r4-2_2026-09-30.json")); TE = json.load(open(D + "f3_step2_test_evidence_r4-2_2026-09-30.json"))
ER = {e["fixture_id"]: e for e in R["evaluations"]}
J = lambda o: json.dumps(o, sort_keys=True, default=str)

print("\n(a) decision layer")
def one_pass():
    stops, evals = [], []
    for fx in gen.INJ_FIXTURES:
        evals.append(h.canon(h.evaluate_fixture(fx["fixture_id"], fx["strata"], gen.N_INJ, "TEST_ONLY_INJECTION_DECISION_LAYER",
                                                fx["flags"], stops, force_c4_pending=fx["fixture_id"] in gen.FORCE_C4_PENDING_FIXTURE_IDS)))
    return evals, h.canon(stops)
snap = json.dumps([fx["strata"] for fx in gen.INJ_FIXTURES], sort_keys=True, default=str)
e1, s1 = one_pass()
leak = json.dumps([fx["strata"] for fx in gen.INJ_FIXTURES], sort_keys=True, default=str) != snap
e2, s2 = one_pass()
print("decision-layer fixtures:", len(e1), "| pass1 == pass2 (same process):", J(e1) == J(e2) and J(s1) == J(s2), "| fixture data changed by pass 1:", leak)
same = [e["fixture_id"] for e in e1 if J(e) == J(ER[e["fixture_id"]])]
print("identical to the delivered r4-2 evaluation objects:", len(same), "/", len(e1), "| differing:", [e["fixture_id"] for e in e1 if e["fixture_id"] not in same])
exp_stops = [s for s in R["stops"] if s["fixture"].startswith("INJ-")]
print("INJ stops identical to the delivered ones:", J(s1) == J(exp_stops), [(s["fixture"], s["stop"]) for s in s1])
for fid, crits in {"INJ-SPL-PENDING-FULL": ["C3", "C4b"], "INJ-SPL-PENDING-FOLD": ["C2"], "INJ-SPL-PENDING-PROBE": ["C4b"]}.items():
    e = [x for x in e1 if x["fixture_id"] == fid][0]
    pend = {f"{fam}:{c}:{sx}": e["criteria"][fam][c][sx]["status"] for fam in ("P01", "P02") for c in e["criteria"][fam] for sx in ("F", "M")
            if "status" in e["criteria"][fam][c][sx]}
    print("  %-22s pending %s | expected cells %s | C4a F passed %s | mechanism %s" % (fid, J(pend), sorted(f"{fam}:{c}:F" for fam in ("P01", "P02") for c in crits),
          e["criteria"]["P01"]["C4a"]["F"].get("passed"), e["mechanism_outcome"]))

print("\n(b) pure unit tests")
ta = h.t_a5_support(); tc = h.t_comparator_nan(); uu = h.ut_uset_construction(gen)
print("t_a5_support equal to delivered:", J(h.canon(ta)) == J(TE["t_a5_support"]), "| pass:", ta.get("pass_"))
print("t_comparator_nan equal to delivered:", J(h.canon(tc)) == J(TE["comparator_nan"]), "| pass:", tc.get("pass_"))
print("ut_uset_construction equal to delivered:", J(h.canon(uu)) == J(TE["uset_construction"]), "| cases ok:", {k: v.get("ok") for k, v in uu.items()})

print("\n(c) the executor's T-SPL-PENDING-REALPATH, run here (f2m/spl/grids passed as None: the stubs never use them)")
before = dict(fd=list(h.FIDELITY_DECLARED), fe=list(h.FIDELITY_EXECUTED), tel=list(h.SPLINE_TELEMETRY_CALLS), exc=list(h.EXC_CAPTURES),
              ctx=h.SPL_CTX_DONE[0], ph=h.CURRENT_PHASE[0], ff=h.fit_family, fs=h.fit_spline)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    sp = h.t_spl_pending_realpath(None, None, None)
print("stdout lines printed during the test: %d" % len(buf.getvalue().splitlines()))
print("pass_ %s | all_cases_ok %s | restored %s" % (sp["pass_"], sp["all_cases_ok"], J(sp["restored"])))
dl = {c["case"]: c for c in TE["spl_pending_realpath"]["cases"]}
for c in sp["cases"]:
    d = dl[c["case"]]
    print("  %-32s ok %-5s | identical to the delivered case record: %-5s | got %s | mechanism %s" % (c["case"], c["ok"], J(h.canon(c)) == J(d), J(c["got"]), c["mechanism"]))
after_ok = dict(fd=h.FIDELITY_DECLARED == before["fd"], fe=h.FIDELITY_EXECUTED == before["fe"], tel=h.SPLINE_TELEMETRY_CALLS == before["tel"],
                exc=h.EXC_CAPTURES == before["exc"], ctx=h.SPL_CTX_DONE[0] == before["ctx"], ph=h.CURRENT_PHASE[0] == before["ph"],
                ff=h.fit_family is before["ff"], fs=h.fit_spline is before["fs"])
print("globals and engines restored after the test (auditor's own snapshot):", J(after_ok))
print("whole record equal to the delivered spl_pending_realpath block:", J(h.canon(sp)) == J(TE["spl_pending_realpath"]))

print("\n(d) helper functions")
for f in ("STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "TEST_ONLY_INJECTION_SPLINE_FAILURE",
          "NO_VALID_MODE", "ZERO_VARIANCE_OR_NONFINITE", None, "", "xSTOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"):
    print("  spl_pending_tag(%r) -> %r" % (f, h.spl_pending_tag(f)))
for args in (([],), ([False, False],), (["TEST_ONLY_INJECTED"],), (["TEST_ONLY_INJECTED", "F3-STEP2-EXACT-04"],), ([True],), ([True, "F3-STEP2-EXACT-04"],),
             ([False], ["F3-STEP2-EXACT-04"]), (["TEST_ONLY_INJECTED"], [False]), ("TEST_ONLY_INJECTED",), (["SOME-OTHER-TAG", "TEST_ONLY_INJECTED"],)):
    print("  merge_pending_tags%s -> %r" % (repr(args) if len(args) > 1 else "(" + repr(args[0]) + ")", h.merge_pending_tags(*args)))
print("\nstore dir exists after the run (nothing may be written):", os.path.isdir(h.RESTART_STORE_DIR))
```

Block [5] — r42_05_realpath_probe.py (output in §5.2):

```python
"""Evidence script 05 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). [A-S] the auditor's own
probe of R41A-01 on the real path, independent of the executor's T-SPL-PENDING-REALPATH: the UNMODIFIED r4-2 functions
run_real_scenario and evaluate_fixture are called on the generator's REAL_SCENARIOS with the auditor's stubs for the
two fit engines (fit_family always eligible; fit_spline valid except in the contexts a case names, where it returns
the failure string the real fit_spline returns). Cases and expected pending cells are written below BEFORE the run,
from the r4-2 instruction section 3 R41A-01 (a)/(b) read per criterion (the reading the PI accepted on 2026-09-30).
Part 2 calls the REAL fit_spline with a stand-in spline namespace whose solver raises, to check that the two failure
strings the stubs use are the ones fit_spline itself produces (restart layer switched off in this process only, so
nothing is written). Numbers produced under stubs mean nothing."""
import importlib.util, sys, json, hashlib, os, io, contextlib, warnings
import numpy as np
warnings.filterwarnings("ignore")
HP = "G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py"
spec = importlib.util.spec_from_file_location("h_r42p", HP); h = importlib.util.module_from_spec(spec); sys.modules["h_r42p"] = h; spec.loader.exec_module(h)
gs = importlib.util.spec_from_file_location(h.GEN_MODULE_NAME, h.GEN_PATH); gen = importlib.util.module_from_spec(gs); sys.modules[h.GEN_MODULE_NAME] = gen; gs.loader.exec_module(gen)
print("harness sha256:", hashlib.sha256(open(h.__file__, "rb").read()).hexdigest())
REAL = {sc["fixture_id"]: sc for sc in gen.REAL_SCENARIOS}
print("REAL_SCENARIOS trajectories per sex:", {k: {sx: len(v["strata"][sx]) for sx in ("F", "M")} for k, v in REAL.items()},
      "| declared SPL injections:", {k: [(i["traj"], i["context"], i["mode"]) for i in v["injections"] if i["family"] == "SPL"] for k, v in REAL.items()})

def smooth(x):
    k = 5; pad = np.pad(np.asarray(x, dtype=float), (k // 2, k // 2), mode="edge"); return np.convolve(pad, np.ones(k) / k, mode="valid")
PLAN, real_ff, real_fs = {}, h.fit_family, h.fit_spline
def stub_family(f2m, grids, fixture_id, family, x, obs_idx, telemetry, mask_id, **kw):
    return dict(eligible=True, ghat=smooth(x), theta=np.ones(len(h.W_C5[family])), L=0.0, start_bank_size=0, feature_start_rejected=False, failure_codes=[])
def stub_spline(spl, fixture_id, x, obs_idx, telemetry, mask_id, inject_failure=False):
    if inject_failure:
        return dict(valid=False, failure="TEST_ONLY_INJECTION_SPLINE_FAILURE")
    if mask_id in PLAN:
        return dict(valid=False, failure=PLAN[mask_id], per_mode_valid=[])
    return dict(valid=True, ghat=smooth(x), mode=0, rss=0.0, equivalent_modes=[0], per_mode_valid=[True])
NAT, INJ = "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"
def cells(sex, crits, st): return {f"{fam}:{c}:{sex}": st for fam in ("P01", "P02") for c in crits}
def merge(*ds):
    out = {}
    for d in ds: out.update(d)
    return out
# (scenario, label, plan {mask_id: failure}, expected pending cells) -- written before the run
CASES = [
    ("SCEN-A", "P1 baseline", {}, {}),
    ("SCEN-A", "P2 natural F0 fold0", {"probe:F0:fold0": NAT}, cells("F", ("C2",), NAT)),
    ("SCEN-A", "P3 natural M0 probeR", {"probe:M0:probeR": NAT}, cells("M", ("C4b",), NAT)),
    ("SCEN-A", "P4 injected M0 probeR", {"probe:M0:probeR": INJ}, cells("M", ("C4b",), INJ)),
    ("SCEN-A", "P5 injected F0 fold4", {"probe:F0:fold4": INJ}, cells("F", ("C2",), INJ)),
    ("SCEN-A", "P6 natural full + injected probeL, F0", {"probe:F0:full": NAT, "probe:F0:probeL": INJ}, cells("F", ("C3", "C4b"), NAT)),
    ("SCEN-A", "P7 injected fold1 + natural fold3, F0", {"probe:F0:fold1": INJ, "probe:F0:fold3": NAT}, cells("F", ("C2",), NAT)),
    ("SCEN-A", "P8 injected F0 full + natural M0 full", {"probe:F0:full": INJ, "probe:M0:full": NAT},
     merge(cells("F", ("C3", "C4b"), INJ), cells("M", ("C3", "C4b"), NAT))),
    ("SCEN-A", "P9 injected probeL + injected probeR, M0", {"probe:M0:probeL": INJ, "probe:M0:probeR": INJ}, cells("M", ("C4b",), INJ)),
    ("SCEN-A", "P10 natural in every context, F0", {"probe:F0:" + c: NAT for c in ("full", "fold0", "fold1", "fold2", "fold3", "fold4", "probeL", "probeR")},
     cells("F", ("C2", "C3", "C4b"), NAT)),
    ("SCEN-B", "P11 SCEN-B as declared (spline failures M0 full, M0 fold1)", {}, {}),
    ("SCEN-B", "P12 SCEN-B as declared + injected F0 full", {"probe:F0:full": INJ}, cells("F", ("C3", "C4b"), INJ)),
]
h.fit_family, h.fit_spline = stub_family, stub_spline
allok = True
buf = io.StringIO()
for fid, label, plan, exp in CASES:
    PLAN.clear(); PLAN.update(plan)
    with contextlib.redirect_stdout(buf):
        recs, n_s, tel, ca, fmf = h.run_real_scenario(None, None, None, REAL[fid], "probe", [])
        stops = []
        ev = h.canon(h.evaluate_fixture(fid, recs, n_s, "REAL", {}, stops))
    flags = {sx: {k.replace("spl_pending_", ""): recs[sx]["SPL"][k] for k in ("spl_pending_full", "spl_pending_fold", "spl_pending_probe")} for sx in ("F", "M")}
    got = {f"{fam}:{c}:{sx}": ev["criteria"][fam][c][sx]["status"] for fam in ("P01", "P02") for c in ev["criteria"][fam] for sx in ("F", "M")
           if "status" in ev["criteria"][fam][c][sx]}
    verdict_in_pending = [k for k in got if "passed" in ev["criteria"][k.split(":")[0]][k.split(":")[1]][k.split(":")[2]]]
    c4a_routed = [k for k in got if k.split(":")[1] == "C4a"]
    ok = got == exp and not verdict_in_pending and not c4a_routed
    allok = allok and ok
    print("\n[%s] %s -> %s" % (fid, label, "AS EXPECTED" if ok else "DIFFERENT"))
    print("  flags:", json.dumps(flags))
    print("  pending cells:", json.dumps(got, sort_keys=True))
    if not ok: print("  expected     :", json.dumps(exp, sort_keys=True))
    print("  C4a routed: %s | PENDING cell with a verdict: %s | p03 %s | mechanism %s | stops %s" % (
        c4a_routed or "none", verdict_in_pending or "none", (ev["p03"]["P01"], ev["p03"]["P02"]), ev["mechanism_outcome"], [s["stop"] for s in stops]))
h.fit_family, h.fit_spline = real_ff, real_fs
print("\nALL STUB CASES AS EXPECTED:", allok, "| engines restored:", h.fit_family is real_ff and h.fit_spline is real_fs)

print("\n== part 2: the REAL fit_spline with a raising stand-in solver (restart layer off in this process)")
h.RESTART_LAYER_ACTIVE = False
class Boom(ValueError): pass
def make_spl(msg_for_mode):
    def solver_config(name, x, obs, A):
        raise Boom(msg_for_mode(h._SPL_CTX["mode"]))
    return {"amat": lambda m: None, "solver_config": solver_config, "rss_of": lambda c, x, o: 0.0, "B": None}
x = np.linspace(-1.0, 1.0, h.T)
# each call gets its own fixture id, as every context of a delivered run has its own (fixture, mask_id); the last
# call deliberately REUSES the id of the first (natural) call: fit_spline derives the tag from every UNRELATED
# capture recorded in this process for the same (fixture, mask_id), not only from the current call's
for fxid, label, fn, kw in (("AUD-PROBE-1", "every mode natural", lambda m: "natural solver fault", {}),
                            ("AUD-PROBE-2", "every mode TEST_ONLY", lambda m: "TEST_ONLY_INJECTION: unrelated", {}),
                            ("AUD-PROBE-3", "mode 0 natural, others TEST_ONLY", lambda m: "natural solver fault" if m == 0 else "TEST_ONLY_INJECTION: unrelated", {}),
                            ("AUD-PROBE-4", "declared injected failure", lambda m: "unused", {"inject_failure": True}),
                            ("AUD-PROBE-1", "every mode TEST_ONLY, id of call 1 reused", lambda m: "TEST_ONLY_INJECTION: unrelated", {})):
    n0 = len(h.EXC_CAPTURES)
    with contextlib.redirect_stdout(io.StringIO()):
        out = h.fit_spline(make_spl(fn), fxid, x, h.FULL_O, [], "probe:F0:full", **kw)
    caps = h.EXC_CAPTURES[n0:]
    print("  %-11s %-42s failure %-44r -> spl_pending_tag %-22r | captures %d (UNRELATED %d, with TEST_ONLY %d)" % (
        fxid, label, out.get("failure"), h.spl_pending_tag(out.get("failure")), len(caps), sum(c["kind"] == "UNRELATED" for c in caps),
        sum("TEST_ONLY" in c["message"] for c in caps)))
print("store dir exists (nothing may be written):", os.path.isdir(h.RESTART_STORE_DIR))
```

Block [6] — r42_06_code_diff.py:

```python
"""Evidence script 06 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). Read-only, tier [A]:
function-level comparison of the harness r4-1 (4e0dc8cf..., the audited parent) -> r4-2 attempt 2 (b988e962...), and
of the attempt-1 bytes (9e4d2803...) -> attempt 2; byte identity of the reused generator and manifest; the changed
lines of the two decision functions printed in full (evaluate_fixture, run_real_scenario)."""
import ast, difflib, hashlib
D = "/home/claude/audit_r42/zip/r4-2 teslim/"
P41 = "/home/claude/audit_r41/recv4/f3_step2_adequacy_harness_r4-1_2026-09-29.py"
P42 = D + "f3_step2_adequacy_harness_r4-2_2026-09-30.py"
P42a1 = D + "f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()

def units(path):
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    lines = src.splitlines()
    out = {}
    for node in tree.body:
        seg = "\n".join(lines[node.lineno - 1: node.end_lineno])
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            out["def " + node.name] = (seg, node.lineno)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            names = [t.id for t in (node.targets if isinstance(node, ast.Assign) else [node.target]) if isinstance(t, ast.Name)]
            for n in names: out["= " + n] = (seg, node.lineno)
    return out, src

for a_path, b_path, lab in ((P41, P42, "r4-1 (4e0dc8cf) -> r4-2 attempt 2 (b988e962)"), (P42a1, P42, "r4-2 attempt 1 (9e4d2803) -> attempt 2 (b988e962)")):
    A, asrc = units(a_path); B, bsrc = units(b_path)
    print("== %s ; sha256 %s -> %s" % (lab, sha(a_path)[:16], sha(b_path)[:16]))
    added = sorted(k for k in B if k not in A); removed = sorted(k for k in A if k not in B)
    changed = sorted(k for k in A if k in B and A[k][0] != B[k][0])
    print("  top-level units: %d -> %d" % (len(A), len(B)))
    print("  functions added:", [k for k in added if k.startswith("def")])
    print("  functions removed:", [k for k in removed if k.startswith("def")])
    print("  functions changed (body text differs):", [(k, "line %d" % B[k][1]) for k in changed if k.startswith("def")])
    print("  module constants added:", [k[2:] for k in added if k.startswith("=")])
    print("  module constants removed:", [k[2:] for k in removed if k.startswith("=")])
    print("  module constants changed:", [k[2:] for k in changed if k.startswith("=")])
    if lab.startswith("r4-1"):
        for fn in ("def evaluate_fixture", "def run_real_scenario"):
            d = list(difflib.unified_diff(A[fn][0].splitlines(), B[fn][0].splitlines(), lineterm="", n=0))
            code = [l for l in d[2:] if l[:1] in "+-" and not l[1:].strip().startswith("#") and l[1:].strip()]
            print("  %s: %d changed lines, %d of them code (non-comment, non-blank):" % (fn[4:], len([l for l in d[2:] if l[:1] in "+-"]), len(code)))
            for l in code: print("      " + l[:150])
A41, _ = units(P41); A42, _ = units(P42)
blk = """    natural_unrelated = [c for c in EXC_CAPTURES
                         if c.get("kind") == "UNRELATED"
                         and "TEST_ONLY" not in c.get("message", "")]
    natural_unrelated_findings = (
        ["F3-STEP2-EXACT-04"] if natural_unrelated else [])"""
print("\n== finding machinery")
print("  fit_spline body identical r4-1 -> r4-2: %s ; fit_family identical: %s" % (A41["def fit_spline"][0] == A42["def fit_spline"][0], A41["def fit_family"][0] == A42["def fit_family"][0]))
print("  main(): the natural_unrelated block (EXACT-04 opening) present verbatim in both: %s / %s" % (blk in A41["def main"][0], blk in A42["def main"][0]))
print("  main(): exactness_findings / open_findings fed by natural_unrelated_findings in both: %s / %s" % (
    all(t in A41["def main"][0] for t in ("exactness_findings=natural_unrelated_findings", "open_findings=natural_unrelated_findings")),
    all(t in A42["def main"][0] for t in ("exactness_findings=natural_unrelated_findings", "open_findings=natural_unrelated_findings"))))
print("\n== reused files")
for f, ref in (("f3_step2_fixture_generator_r4-1_2026-09-29.py", "/home/claude/audit_r41/recv7/"), ("f3_step2_fixture_manifest_r4-1_2026-09-29.csv", "/home/claude/audit_r41/recv3/")):
    print("  %-48s delivered %s… == audited r4-1 copy: %s" % (f, sha(D + f)[:16], open(D + f, "rb").read() == open(ref + f, "rb").read()))
```

```text
== r4-1 (4e0dc8cf) -> r4-2 attempt 2 (b988e962) ; sha256 4e0dc8cfb81543ee -> b988e9628731f6d0
  top-level units: 194 -> 215
  functions added: ['def merge_pending_tags', 'def spl_pending_tag', 'def t_spl_pending_realpath']
  functions removed: []
  functions changed (body text differs): [('def evaluate_fixture', 'line 1384'), ('def main', 'line 2999'), ('def run_real_scenario', 'line 1939')]
  module constants added: ['AUDIT_A4_HASH', 'AUDIT_A4_PATH', 'D7_DISPATCH_RECORD_HASH', 'D7_DISPATCH_RECORD_PATH', 'GEN_HASH_REUSED', 'INJECTED_EXACTNESS_TAG', 'LAUNCH_NUMBER', 'LAUNCH_STDERR_PATH', 'LAUNCH_STDOUT_PATH', 'MANIFEST_HASH_REUSED', 'MANIFEST_REUSED_PATH', 'NATURAL_EXACTNESS_TAG', 'NONREG_R41_PATH', 'R4_1_RESULTS_HASH', 'R4_1_RESULTS_PATH', 'R4_2_INSTRUCTION_HASH', 'R4_2_INSTRUCTION_PATH', '_PENDING_RE']
  module constants removed: []
  module constants changed: ['ATTEMPT_LOG_PATH', 'ATTEMPT_NUMBER', 'CUSTODY_PATH', 'DATE_TAG', 'MANDATORY_TESTS', 'MANIFEST_PATH', 'NONREG_PATH', 'PERCALL_TELEMETRY_PATH', 'REGISTER_PATH', 'RESIDUAL_PATH', 'RESTART_STORE_DIR', 'RESULTS_PATH', 'STORE_MANIFEST_PATH', 'SUPERSEDES_CUSTODY_SHA256', 'SUPERSEDES_HARNESS_SHA256', 'SUPERSEDES_NOTE_PATH', 'TELEMETRY_PATH', 'TEST_EVIDENCE_PATH']
  evaluate_fixture: 63 changed lines, 34 of them code (non-comment, non-blank):
      -    _spl_pend_tag = ("TEST_ONLY_INJECTED"
      -                     if c4_source == "TEST_ONLY_INJECTION_DECISION_LAYER"
      -                     else "F3-STEP2-EXACT-04")
      -                    if any(dS.get("spl_pending_fold", [])):
      -                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
      -                                                  % _spl_pend_tag)
      +                    _tag = merge_pending_tags(dS.get("spl_pending_fold", []))
      +                    if _tag:
      +                        per_sex[sx] = dict(
      +                            status="STOP_EXACTNESS_PENDING(%s)" % _tag)
      -                    if any(dS.get("spl_pending_full", [])):
      -                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
      -                                                  % _spl_pend_tag)
      +                    _tag = merge_pending_tags(dS.get("spl_pending_full", []))
      +                    if _tag:
      +                        per_sex[sx] = dict(
      +                            status="STOP_EXACTNESS_PENDING(%s)" % _tag)
      -                    if (any(dS.get("spl_pending_full", []))
      -                            or any(dS.get("spl_pending_probe", []))):
      -                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
      -                                                  % _spl_pend_tag)
      +                    _tag = merge_pending_tags(dS.get("spl_pending_full", []),
      +                                              dS.get("spl_pending_probe", []))
      +                    if _tag:
      +                        per_sex[sx] = dict(
      +                            status="STOP_EXACTNESS_PENDING(%s)" % _tag)
      -        import re as _re_tag
      -                    m = _re_tag.search(r"STOP_EXACTNESS_PENDING\(([^)]+)\)", st_str)
      -                    if m and m.group(1) in ("TEST_ONLY_INJECTED", "F3-STEP2-EXACT-04"):
      +                    m = re.search(r"STOP_EXACTNESS_PENDING\(([^)]+)\)", st_str)
      +                    if m and m.group(1) in (INJECTED_EXACTNESS_TAG,
      +                                            NATURAL_EXACTNESS_TAG):
      -            tag = ",".join(sorted(spl_tags))
      +            tag = merge_pending_tags(sorted(spl_tags))
  run_real_scenario: 45 changed lines, 21 of them code (non-comment, non-blank):
      -                str(spf.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
      -                and "TEST_ONLY" not in str(spf.get("failure", "")))
      +                spl_pending_tag(spf.get("failure")))
      -            cc, pred_cv, fold_pending = True, np.full(T, np.nan), False
      +            cc, pred_cv, fold_tags = True, np.full(T, np.nan), []
      -                    if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
      -                            and "TEST_ONLY" not in str(r.get("failure", ""))):
      -                        fold_pending = True   # R4A-01: any fold unverifiable
      -            recs["SPL"]["spl_pending_fold"].append(fold_pending)
      +                    fold_tags.append(spl_pending_tag(r.get("failure")))
      +            recs["SPL"]["spl_pending_fold"].append(
      +                merge_pending_tags(fold_tags) or False)
      -            probe_pending = False
      +            probe_tags = []
      -                if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
      -                        and "TEST_ONLY" not in str(r.get("failure", ""))):
      -                    probe_pending = True   # R4A-01: either probe unverifiable
      +                probe_tags.append(spl_pending_tag(r.get("failure")))
      -            recs["SPL"]["spl_pending_probe"].append(probe_pending)
      +            recs["SPL"]["spl_pending_probe"].append(
      +                merge_pending_tags(probe_tags) or False)
== r4-2 attempt 1 (9e4d2803) -> attempt 2 (b988e962) ; sha256 9e4d2803101de6b4 -> b988e9628731f6d0
  top-level units: 215 -> 215
  functions added: []
  functions removed: []
  functions changed (body text differs): [('def main', 'line 2999')]
  module constants added: []
  module constants removed: []
  module constants changed: ['ATTEMPT_NUMBER', 'LAUNCH_NUMBER', 'RESTART_LAYER_ACTIVE', 'SUPERSEDES_CUSTODY_SHA256', 'SUPERSEDES_HARNESS_SHA256', 'SUPERSEDES_NOTE_PATH']

== finding machinery
  fit_spline body identical r4-1 -> r4-2: True ; fit_family identical: True
  main(): the natural_unrelated block (EXACT-04 opening) present verbatim in both: True / True
  main(): exactness_findings / open_findings fed by natural_unrelated_findings in both: True / True

== reused files
  f3_step2_fixture_generator_r4-1_2026-09-29.py    delivered 68d126cf07b11b84… == audited r4-1 copy: True
  f3_step2_fixture_manifest_r4-1_2026-09-29.csv    delivered 5c09c4f0811fa51b… == audited r4-1 copy: True
```

Block [7] — r42_07_line_facts.py (output in §8):

```python
"""Evidence script 07 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). Read-only, tier [A]:
the line numbers the record cites, found by searching the delivered files for fixed text (file:line: text)."""
import hashlib
D = "/home/claude/audit_r42/zip/r4-2 teslim/"
F = {"H": "f3_step2_adequacy_harness_r4-2_2026-09-30.py", "REP": "f3_step2_correction_report_r4-2_2026-09-30.md",
     "REG": "f3_step2_class_c_pin_register_r4-2_2026-09-30.md", "C2": "f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md",
     "LOG": "f3_step2_r4-2_attempt_log_2026-09-30.md", "NOTE": "f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md",
     "TL": "f3_step2_r4-2_transmission_list_2026-09-30.md", "INV": "f3_step2_r4-2_start_state_inventory_2026-09-30.md",
     "D7": "f3_step2_r4-2_pi_dispatch_record_2026-09-30.md", "INS": "Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md"}
PAT = [("H", "def spl_pending_tag("), ("H", "def merge_pending_tags("), ("H", "    return sorted(set(tags))[0]"),
       ("H", "def fit_spline("), ("H", "        ctx_unrel = [c for c in EXC_CAPTURES"), ("H", '        tag = "TEST_ONLY_INJECTED" if all_test_only else "F3-STEP2-EXACT-04"'),
       ("H", "def evaluate_fixture("), ("H", '_tag = merge_pending_tags(dS.get("spl_pending_fold", []))'),
       ("H", '_tag = merge_pending_tags(dS.get("spl_pending_full", []))'), ("H", '_tag = merge_pending_tags(dS.get("spl_pending_full", []),'),
       ("H", "            tag = merge_pending_tags(sorted(spl_tags))"),
       ("H", "def run_real_scenario("), ("H", 'spl_pending_tag(spf.get("failure")))'), ("H", 'fold_tags.append(spl_pending_tag(r.get("failure")))'),
       ("H", 'probe_tags.append(spl_pending_tag(r.get("failure")))'),
       ("H", "def t_spl_pending_realpath("), ("H", "    CASES = ["), ("H", '        globals()["fit_family"], globals()["fit_spline"] = real_fit_family, real_fit_spline'),
       ("H", "def run_exc_injection_fixtures("), ("H", "    p2 = _exc_injection_pass(spl)"),
       ("H", "def main():"), ("H", "    assert LAUNCH_NUMBER >= 1, ("), ("H", 'LAUNCH_NUMBER = int(os.environ.get("F3_R42_LAUNCH", "0"))'),
       ("H", "RESTART_LAYER_ACTIVE = True"), ("H", "RESTART_STORE_DIR = "), ("H", "CUSTODY_PATH = ("),
       ("H", "    assert man_hash == MANIFEST_HASH_REUSED, ("), ("H", "    assert _regen_hash == man_hash, ("),
       ("H", "    _CODE_ENV_FINGERPRINT[0] = hashlib.sha256("), ("H", '    print("PRE_EXECUTION_CUSTODY_RECORD_VERIFIED'),
       ("H", "    spl_pending_realpath = t_spl_pending_realpath(f2m, spl, grids)"),
       ("H", "        for cr in ut_caps:"), ("H", "    exc_unit_phase = list(EXC_CAPTURES)"),
       ("H", "    natural_unrelated = [c for c in EXC_CAPTURES"),
       ("H", '    CURRENT_PHASE[0] = "nonregression_r4_1"'), ('H', '    assert record_test("T-NONREG-R4-1", _nonreg41_ok), ('),
       ("H", "    _d7_observed = sha256_of(D7_DISPATCH_RECORD_PATH)"), ("H", "            PI_dispatch_record_hash=_d7_observed,"),
       ("H", '    assert six["PI_dispatch_record_hash"] == sha256_of(D7_DISPATCH_RECORD_PATH), ('),
       ("H", '        executor_models="claude-opus-4-8[1m]; see r4-1 report",'),
       ("REP", "| 9 | calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md"), ("REP", "| 12 | provenance/f3_step2_r4-2_attempt_log_2026-09-30.md"),
       ("REP", "| **R41A-04** |"), ("REP", "The report and the attempt log/register hashes stand only in their sidecars and in the"),
       ("REP", "executor_models = claude-opus-4-8[1m] up to the r4-2 instrument verification"), ("REP", "## 4. The R41A-01(b) reading"),
       ("REG", "| **PIN-SPLINE-PENDING-TAG-SCOPE"), ("REG", "| PIN-REVALIDATION-INCONSISTENT-U"),
       ("C2", "restart_layer_active_at_this_W3 = True (r4-2 attempt 1 is ONE process from the"),
       ("LOG", "## ERRATUM-3"), ("LOG", "under `0f32c7911cf8fccb`"), ("LOG", "**Observation 1 (recomputed here).** With the r3 environment the custody records state"),
       ("NOTE", "filed in quarantine beside this note"), ("TL", "| launch-1 log pair, quarantine copies |"),
       ("H", 'mkey = "splmode_%s_%s_%s_%s" % (fixture_id, mask_id, m, xhash)'), ("H", "            for cr in cap_recs:"),
       ("H", "honored as TWO full deterministic passes"), ("H", "    p1 = _exc_injection_pass(spl)"),
       ("H", 'UNITS_READ_FROM_STORE["nr_gates"] += 1'), ("H", 'UNITS_READ_FROM_STORE["unit_tests"] += 1'), ("H", "UNITS_READ_FROM_STORE[run_label] += 1"),
       ("H", "(register row PIN-SPLINE-PENDING-ROUTING; r4-2 report section 4)"),
       ("REP", "re-hash at their"), ("REP", "units_read_from_store all 0"), ("REP", "parents_unchanged = true"),
       ("LOG", "| 14804 | 2026-09-30 (evening) |"), ("LOG", "zero units from the store"),
       ("REG", "ACCEPTED by the PI's dispatch message of 2026-09-30"),
       ("INV", "The r4 package was re-checked at the same time"), ("TL", "| attempt-1 interruption note |"),
       ("D7", "(2) when a sex has both a natural"), ("D7", "accepted_with_this_record = YES"),
       ("INS", "if a sex has both kinds for the criteria"), ("INS", "a natural and an injected event in the same"),
       ("INS", "parents_unchanged with the re-hash values"), ("INS", "F  f3_step2_r4-2_transmission_list_<date>.md")]
for key, pat in PAT:
    lines = open(D + F[key], encoding="utf-8").read().splitlines()
    hits = [i + 1 for i, l in enumerate(lines) if pat in l]
    print("%-4s %-46s line(s) %-14s | %s" % (key, F[key][:46], ",".join(map(str, hits)) or "NOT FOUND", pat.strip()[:90]))
for k, f in F.items():
    print("%-4s %s sha256 %s" % (k, f, hashlib.sha256(open(D + f, "rb").read()).hexdigest()))
```

Block [8] — r42_08_replay_check.py (output in §2):

```python
"""Evidence script 08 (F3 STEP-2 r4-2 independent audit A-5; auditor claude-opus-5-5; 2026-10-01). Read-only, tier [A]:
store reads INSIDE the final process. Under the active restart layer fit_spline keys a mode unit by fixture, mask id,
mode and input hash only; the INJ-EXC-* fixtures are fitted twice (two passes) with the same keys, so the second pass
can be served from the store. This script tests that on the delivered per-call telemetry (rows replayed from the store
carry the stored wall-clock value), the store manifest and the test evidence, for r4-2 and for the auditor's copies of
r4 and r4-1, and shows which counters the process block uses."""
import csv, collections, hashlib, json, re
D = "/home/claude/audit_r42/zip/r4-2 teslim/"
H = D + "f3_step2_adequacy_harness_r4-2_2026-09-30.py"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
PC = {"r4": "/home/claude/audit_r4/recv/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv",
      "r4-1": "/home/claude/audit_r41/recv3/f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv",
      "r4-2": D + "f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv"}
print("== per-call telemetry, INJ-EXC-* rows of the unit-test phase: second half against first half")
for lab, p in PC.items():
    rows = list(csv.DictReader(open(p, newline="", encoding="utf-8")))
    exc = [r for r in rows if r["phase"] == "unit_tests" and r["fixture"].startswith("INJ-EXC")]
    h = len(exc) // 2; a, b = exc[:h], exc[h:]
    content = lambda r: tuple(v for k, v in r.items() if k != "wall_clock_seconds")
    print("  %-5s %s… rows %d | halves equal on every other column: %s | equal wall-clock in %d of %d pairs | pids %s" % (
        lab, sha(p)[:12], len(exc), [content(x) for x in a] == [content(y) for y in b],
        sum(x["wall_clock_seconds"] == y["wall_clock_seconds"] for x, y in zip(a, b)), h, sorted({r["pid"] for r in exc})))
rows = list(csv.DictReader(open(PC["r4-2"], newline="", encoding="utf-8")))
r1 = [r for r in rows if r["phase"] == "run1"]; r2 = [r for r in rows if r["phase"] == "run2"]
print("  r4-2 RUN1/RUN2: %d / %d rows ; pairs with equal wall-clock: %d ; mask ids carry the run label: %s" % (
    len(r1), len(r2), sum(x["wall_clock_seconds"] == y["wall_clock_seconds"] for x, y in zip(r1, r2)),
    all(r["mask_id"].startswith("run1:") for r in r1) and all(r["mask_id"].startswith("run2:") for r in r2)))
for ph, R in (("run1", r1), ("run2", r2)):
    w = collections.defaultdict(list)
    for r in R: w[r["wall_clock_seconds"]].append((r["fixture"], r["mask_id"], r["mode"]))
    same_call = [v for v in w.values() if len(v) > 1 and len(set(v)) < len(v)]
    print("  r4-2 %s: wall-clock values shared by two or more rows %d ; of them shared by the same (fixture, mask, mode): %d" % (
        ph, sum(1 for v in w.values() if len(v) > 1), len(same_call)))
print("\n== telemetry (deliverable 5, r4-2): family fits and spline modes")
tm = list(csv.DictReader(open(D + "f3_step2_telemetry_r4-2_2026-09-30.csv", newline="", encoding="utf-8")))
fam = [r for r in tm if r["fitter"] != "SPL"]; spl = [r for r in tm if r["fitter"] == "SPL"]
fk = collections.Counter((r["fixture"], r["fitter"], r["mask_id"], r["family"], r["start_id"], r["optimizer_path"]) for r in fam)
sk = collections.Counter((r["fixture"], r["mask_id"], r["start_id"]) for r in spl)
print("  rows %d by fitter %s" % (len(tm), dict(collections.Counter(r["fitter"] for r in tm))))
print("  family-fit rows %d ; keys (fixture, fitter, mask, family, start, path) occurring more than once: %d ; rows equal in every column to another row: %d" % (
    len(fam), sum(1 for v in fk.values() if v > 1), sum(v for v in collections.Counter(tuple(r.values()) for r in fam).values() if v > 1)))
print("  spline mode rows %d ; keys (fixture, mask, mode) occurring more than once: %d, by fixture %s" % (
    len(spl), sum(1 for v in sk.values() if v > 1), dict(collections.Counter(k[0] for k, v in sk.items() if v > 1))))
print("\n== store manifest (r4-2)")
sm = list(csv.DictReader(open(D + "f3_step2_r4-2_restart_store_manifest_2026-09-30.csv", newline="", encoding="utf-8")))
kinds = collections.Counter(x["path"].split("__", 1)[1].split("_")[0] for x in sm)
exc_units = [x["path"] for x in sm if "INJ-EXC" in x["path"]]
print("  unit kinds %s ; INJ-EXC mode units %d (one per fixture context and mode: 3 x 146 = 438: %s)" % (dict(kinds), len(exc_units), len(exc_units) == 3 * 146))
print("\n== the harness")
src = open(H, encoding="utf-8").read().split("\n")
for i, l in enumerate(src, 1):
    if 'mkey = "splmode_%s_%s_%s_%s"' in l or "cached_mode = ckpt_load(mkey)" in l or "UNITS_READ_FROM_STORE[" in l or "p1 = _exc_injection_pass(spl)" in l \
            or "p2 = _exc_injection_pass(spl)" in l or 'honored as TWO full deterministic passes' in l:
        print("  L%-5d %s" % (i, l.strip()))
print("\n== process block and test evidence (r4-2)")
res = json.load(open(D + "f3_step2_results_r4-2_2026-09-30.json"))
te = json.load(open(D + "f3_step2_test_evidence_r4-2_2026-09-30.json"))
print("  units_read_from_store:", json.dumps(res["process"]["units_read_from_store"], sort_keys=True))
ex = te["exc_injection_fixtures"]
print("  exc_injection_fixtures: passes_identical %s ; pass2 == pass1 fields: %s" % (ex["passes_identical"], json.dumps({k: ex[k] for k in ("S1", "S2", "UNRELATED_TYPE")}, sort_keys=True) == json.dumps(ex["pass2"], sort_keys=True)))
for n in (1, 2):
    so = open(D + "f3_step2_r4-2_launch%d_stdout_2026-09-30.log" % n, "rb").read().decode("utf-8")
    e = json.loads(re.search(r"^EXC_INJECTION_FIXTURES = (.*?)\r?$", so, re.M).group(1))
    print("  launch %d (%s): S1 / S2 / UNRELATED_TYPE pass_ %s / %s / %s ; passes_identical %s" % (
        n, re.search(r"RESTART_LAYER_ACTIVE = \w+", so).group(0), e["S1"]["pass_"], e["S2"]["pass_"], e["UNRELATED_TYPE"]["pass_"], e["passes_identical"]))
for n in (1, 2):
    so = open(D + "f3_step2_r4-2_launch%d_stdout_2026-09-30.log" % n, "rb").read().decode("utf-8")
    print("  launch %d progress lines for INJ-EXC contexts: %s" % (n, re.findall(r"PROGRESS SPL ctx (\d+) INJ-EXC", so)))
```
