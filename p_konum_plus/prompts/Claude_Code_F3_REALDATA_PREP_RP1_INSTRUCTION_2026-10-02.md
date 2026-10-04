# p_konum_plus — F3 real-data PREPARATION cycle rp1 — Instruction (2026-10-02)

```text
instrument            = Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md   (final text of DRAFT r1
                        6a367902…; dispatched under the signed D-10, which names this file by SHA256)
instrument_class      = PI instruction for the F3 real-data PREPARATION cycle (tag rp1). It merges the two items D-8
                        sends forward: R42A-01 (record item, "the first record of the next cycle") and R42A-03 (b)
                        (code item that "must be closed before real-data fitting starts"), and it carries out the
                        byte-binding rule the PI chose in D-9 §2 (a). It prepares; it does not execute on real data
drafted_by            = Claude (Claude Code cloud session) at the PI's request of 2026-10-02 ("sıradaki işlerdeki 2 ve 3.
                        adımları senin önerdiğin gibi onaylıyorum"), with the PI's selections S-b (restart layer used,
                        R42A-03 closed) and S-c (child harness of r4-2), and S-e = SYNTHETIC_ONLY_IN_RP1, S-f =
                        EXCLUDED_FROM_RP1 (PI, 2026-10-02). r1 applies a review of the DRAFT (changes in §13;
                        parent DRAFT 5f8fa4cf…). This session drafted D-9; it did not draft D-1 …
                        D-8 or write A-1 … A-5. Same model family as the executor and the auditors
binding instruments   = D-9  f3_step2_qualification_pi_decision_record_2026-10-02.md
                             1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 (QUALIFIED; §2 (a);
                             committed in p_konum_plus at fadf771)
                        D-8  f3_step2_r4-2_pi_decision_record_2026-10-01.md
                             aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae (PI-1 … PI-4; PI-3 flow)
                        D-3  Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
                             5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 (§2, §3, §8, §9, §10 as
                             adapted below)
                        D-1  Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
                             17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
                        D-2  f3_step2_pi_ratified_content_2026-09-07.md
                             da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
                        r4-2 instruction  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
                             d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe (custody and log rules of
                             its R41A-02, adopted here unchanged)
                        D-10 f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md — the signed rp1 dispatch record; it names
                             this file by hash; its own hash stands in its .sha256 sidecar
inputs, not directives = A-5  f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md
                             9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575
frozen upstream       = untouched: v11 ; F1 freeze record ; F2 FINAL FREEZE r1 ; F3 STEP-1 (freeze record r1) ; D-2.
                        No new scientific literal. No real SSA data (real_data_access = false throughout). No
                        algorithm × CVI output. QUALIFIED (D-9) is not re-opened and not extended by this cycle
non-retroactivity     = the r4-2 package (harness b988e962…, results f2a0a4d5…, register c281e713…, report
                        7754ba02…, …) and every earlier package, quarantined file and audit or PI record are
                        historical and read-only. Every rp1 deliverable is a new file tagged rp1
```

## 0. Purpose and what this cycle does NOT do

```text
does    P-1  R42A-01: the start-state inventory of this cycle carries the record items of D-8 PI-3 "İLK YOL" (§3)
        P-2  R42A-03 (b): store reads inside a process are counted and reported at full granularity (§4 C-1)
        P-3  R42A-03, second half: the second INJ-EXC pass gets its own key namespace, so it is a second execution
             and not a replay (§4 C-2)
        P-4  a real-data input path behind an explicit switch that stays OFF in every rp1 launch (§4 C-3)
        P-5  unique context identities for real-data contexts (A-5 R42A-09; §4 C-4)
        P-6  D-8 PI-2 (iii): establish whether "numerically completed but inadmissible" refits are observable from
             the frozen output / telemetry, and prepare the count if they are (§4 C-5)
        P-7  the restart layer active from the first attempt, under T-RP-1 (§4 C-6, §6)
        P-8  D-9 §2 (a): non-regression of the rp1 harness against r4-2, no whitelist (§5)
        P-9  an engineering estimate of the real-data run's size from the synthetic per-call telemetry (§7)
does not  read, open, hash-check or import any real SSA / F1 trajectory or raw file (the F1 manifests are NOT
          opened either; their paths and hashes are written into the code as constants copied from the F1 freeze
          record, see C-3) ; fit anything on real data ; compute any threshold or adequacy statistic on real data ;
          select a generator ; write any 6B code (S-f) ; change any frozen or ratified text,
          hash or parameter ; declare anything QUALIFIED or set F3_EXECUTION_READY ; commit
```

## 1. Preconditions (STOP before the first write if any fails)

```text
1. this file and D-10 are the bytes D-10 names (D-10's own hash stands in its sidecar); every field of D-10 §2 is
   filled with one of its listed values (a blank or template residue ⇒ STOP, D-3 §3)
2. the binding instruments and A-5 above have the printed hashes
3. the r4-2 package files named in the r4-2 transmission list
   (provenance/f3_step2_r4-2_transmission_list_2026-09-30.md, 711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606)
   have the hashes printed there and in their sidecars
4. the frozen upstream files of D-3 §2.1 and the F1 freeze record
   (calibration/f1_input_freeze_record_2026-08-28.md, 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0)
   have their recorded hashes
A missing sidecar of a repository file is recorded and created; it is not a STOP (r4-2 instruction §1).
```

## 2. PI fields (read from D-10, verbatim; nothing is chosen by this instruction)

```text
T-RP-1  restart layer         ACTIVE_FROM_START (PI, 2026-10-02, S-b). Replaces, for rp1 only, the sentence of
                              D-3 §8.3 "Attempt 1 runs without it"; every other condition of D-3 §8.3 applies
S-c     code form             CHILD_HARNESS_OF_R4-2 (PI, 2026-10-02): the rp1 harness is a child of
                              f3_step2_adequacy_harness_r4-2_2026-09-30.py (b988e962…), changed only as §4 lists
S-e     F1 loader validation  SYNTHETIC_ONLY_IN_RP1 (PI, 2026-10-02): the F1 pipeline is tested only on generated
                              raw-format files; no real file is read in rp1
S-f     6B implementation     EXCLUDED_FROM_RP1 (PI, 2026-10-02): no 6B code in rp1; 6B enters later through a
                              narrow child under the same D-9 §2 (a) binding
```

## 3. Start-state inventory (deliverable 11) — R42A-01 closure (D-8 PI-3, "İLK YOL")

Taken before the first rp1 write. In addition to D-3 §9 item 11:

```text
(a) every file of the r4-2 package with its FULL SHA256 — none by prefix, none "by sidecar". Among them the hashes
    A-5 R42A-01 names as missing from the r4-2 report (each re-computed from the file, not copied from here):
      register        calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md                c281e713…
      attempt log     provenance/f3_step2_r4-2_attempt_log_2026-09-30.md                           b69a5915…
      interruption    quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md           a4b5e176…
      launch logs     calibration/…_r4-2_launch1_stdout/stderr, …_launch2_stdout/stderr (4 files) and the two
                      quarantine copies of the launch-1 pair
      attempt-1 copy  quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py 9e4d2803…
(b) the r4-1 and r4 packages re-hashed file by file (every file their transmission lists name), each value printed
    in full next to the value recorded in that list, with EQUAL / DIFFERENT
(c) ERRATUM-R41A-04 — one line for the r4-2 report's R41A-04 response row (report L102), worded as what the r4-2
    hash block actually shows: "the r4-2 report's hash block printed 14 deliverables in full, the four launch logs
    and the attempt-1 harness copy by 8-hex prefix, and the register, the attempt log and the interruption note by
    sidecar reference; the full values are listed in (a) of the rp1 start-state inventory". The r4-2 report stays
    unmodified
(d) optional, same record (A-5 R42A-05 (i)): the r4-2 attempt log L164 gives 0f32c7911cf8fccb (attempt 1, no unit
    written) as r4-2's fingerprint; the r4-2 units are under 4ced291f15fb5afd. One erratum line, re-verified from
    the store manifest
(e) D-8, A-5 and D-9 with their hashes and sidecars, as found in the repository
```

## 4. Code changes of the rp1 harness (each with a test that RAN and PASSED, or a delivered file)

```text
C-1  STORE-READ ACCOUNTING (R42A-03 (b); A-5 C-31 FAIL)
     Every hit of ckpt_load (r4-2 harness L200; read sites L961 start units, L1105 spline mode units, L3122 NR
     gates, L3197 unit tests, L3279 run units) is counted by (phase or run label, key family, pid of the reader)
     and logged with the key and the pid / start time of the process that wrote the unit. The results JSON
     reports units_read_from_store at that granularity; the process block, the report and the attempt log state
     the counts as computed, never "no unit read" unless every count is 0. A new deliverable lists every read
     (key family, key, writer pid, reader pid).
     test T-STORE-READ-ACCOUNTING (mandatory): inside the unit-test phase, a TEST_ONLY context is fitted twice
     under the active layer with identical keys; the count of served mode units equals the number of units the
     first fit wrote, and the per-read log has exactly that many rows; expected numbers written in the test
     before the run. The test's units live in their own namespace and are removed from neither the store nor the
     manifest
C-2  KEY NAMESPACES (R42A-03, second half; D-3 §8.3 "separation")
     (i)  the second INJ-EXC pass (run_exc_injection_fixtures, r4-2 L2573–2579) runs under its own key
          namespace (a pass label in every key it writes), so pass 2 is a second execution in the same process;
          passes_identical then compares two executions
     (ii) T-KEY-NAMESPACE (mandatory): a table, delivered in the register, of every key family the harness
          writes — its key fields and the namespace fields (run label, pass label, test id). The rule it checks:
          two DIFFERENT computations never share a key. The scopes are RUN1, RUN2, NR gates and the unit-test
          phase; inside the unit-test phase, INJ-EXC pass 1, INJ-EXC pass 2 and every other test are separate
          scopes. A deliberate, declared re-read of the SAME computation is allowed only inside the namespace of
          the test that declares it (T-STORE-READ-ACCOUNTING, C-1) and is counted by C-1
     expectation: the number of INJ-EXC capture records in the test evidence after (i) is declared in the
     manifest of expectations BEFORE the run, with the reason (A-5 R42A-08 (a) explains the 8 records of r4-2)
C-3  REAL-DATA INPUT PATH — present, switched OFF
     A module-level switch REAL_DATA_MODE = False, asserted False at start in every rp1 launch; with it False no
     F1 path is opened (the opened-file audit, v6 X-18, shows it). The path implements the F1 frozen pipeline
     (F1 freeze record §8.1 steps 1–11, post_z_tolerance = 1e-8 of §8.2) and builds the scenario structure
     run_real_scenario consumes; F1 paths and hashes (manifests/f1_eligible_trajectory_manifest_2026-08-28.csv
     8a6034eb…, manifests/f1_input_hash_table_2026-08-28.csv aa86f1ea…) are constants copied from the F1
     freeze record §0 and §7, never read from those files in rp1. Before any read in a later cycle the path must
     verify every raw file against the hash table and reproduce the eligible manifest byte-exact (906 rows,
     F 435 / M 471) — a gate that ends the process on failure.
     Every per-scenario parameter the real path needs (start bank, masks, folds, injection list = empty, …) is
     taken from the ratified contract (F3 STEP-1 as ratified; D-2); where the scenario structure needs a value
     that contract does not name: STOP and report it — do not choose.
     test T-F1-LOADER-SYNTH (mandatory): raw-format files (SSA national yob<year>.txt layout: name,sex,count)
     generated from manifest-declared RNG, small, not resembling or calibrated to any F1 trajectory (v6 L936),
     exercising every step of §8.1 and every QC failure branch (missing year, duplicate key, zero denominator,
     zero variance, non-finite, tolerance breach); expected outcomes written before the run.
     Under S-e = SYNTHETIC_ONLY_IN_RP1 the F1 reproduction gate first runs as step 1 of the later real-data
     execution cycle
C-4  UNIQUE CONTEXT IDENTITIES (A-5 R42A-09)
     In real mode every (fixture_id, mask_id) pair is unique per sex, trajectory, family and context, so that
     fit_spline cannot derive a context's tag from another context's captures. test T-CONTEXT-ID-UNIQUE
     (mandatory): a dry construction of the real-mode context list on the T-F1-LOADER-SYNTH output asserts
     uniqueness
C-5  PI-2 (iii) OBSERVABILITY (D-8 PI-2 (iii), (iv))
     State, with line citations into the frozen F2 engine (01714752…) and the frozen spline harness
     (b31e5a6b…), whether a refit that completes numerically but is inadmissible under the frozen taxonomy is
     visible in the output or telemetry the harness already receives. If it is: add a report-only counter that
     reads only those existing fields (no frozen code change; no new classification), with a test on synthetic
     input where one can be built without touching frozen code. If it is not: say so and stop there. Either way
     the counter or the statement is carried into the real-data execution instruction; any such event in real
     data goes to the PI (D-8 PI-2 (iv))
C-6  RESTART LAYER (T-RP-1)
     Active from attempt 1. D-3 §8.3 keys, store, provenance, separation, interruption, check, progress and
     wording rules apply unchanged; the store starts empty in a directory tagged rp1; T-SINGLE-PROCESS if one
     process computed every object of deliverables 5–8, otherwise T-RESTART-PROVENANCE. T-RP-1 enters
     narrowed_evidence by value, as T-R2-2 did (D-3 §5, §8.3)
C-7  6B: none (S-f = EXCLUDED_FROM_RP1). The harness diff contains no 6B code
nothing else changes: no change to the decision layer, the evaluator, the criteria, the generator (68d126cf…),
the manifest (5c09c4f0…), any expected_* value or any literal
```

## 5. Non-regression against r4-2 (D-9 §2 (a))

D-9 §2 (a) binds the rp1 bytes through a non-regression "r4-2'ye karşı, whitelist'siz, RUN1 kanonik 556106e7… ve
artık serisi 3ee624f3… adlandırılmış değerlerinde". As in r4-1 → r4-2 (T-NONREG-R4-1: 37 objects, stops,
canonical and residual), "no whitelist" applies to the SCIENTIFIC objects. Every other field is compared too, but
is judged by class:

```text
T-NONREG-R4-2 (mandatory): the rp1 harness, on the r4-1 generator and manifest reused unchanged, against the r4-2
results (f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba). Every field of the r4-2 results JSON,
telemetry and test evidence is compared and every difference is printed; each difference falls in exactly one
class:
  S  SCIENTIFIC — must be identical, no whitelist, no exemption:
       every one of the 37 evaluation objects and every stop record in canon() form with sorted keys ;
       RUN1 canonical document = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 ;
       residual series = 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f ;
       RUN1 == RUN2
     any difference here is a finding, reported per fixture, never absorbed
  E  EXPECTED RUN-RECORD differences — declared BEFORE the run in the expectations manifest, each with its
     field path and reason, and then checked: pid, start / end times, wall-clock columns, file paths and
     hashes of rp1's own files (harness, custody, logs, store manifest), the store fingerprint, the counters
     C-1 corrects (units_read_from_store and the new fine-grained fields), the INJ-EXC capture records and
     passes_identical evidence C-2 changes, fields added by C-1 … C-5 (listed as ADDITIONS). An E difference
     that does not match its declaration is a finding
  U  UNEXPECTED — any other difference: an open finding
T-NONREG-R4-1 and T-NONREG-R4 stay as they are.
The environment is recorded as in v6 §8; if it differs from r4-2's (Windows-10-10.0.19045-SP0, Python 3.11.7,
numpy 1.26.4, scipy 1.14.1, thread pins 1) the report says so field by field (D-9 §2 (a) binds code AND
environment); an environment difference is reported under E only if declared in advance, otherwise under U.
```

## 6. Run, custody and logs

As D-3 §8.1–§8.3 with C-6, and as the r4-2 instruction's R41A-02: one W-3 custody record per attempt with an
attempt-numbered name and SUPERSEDES_CUSTODY_SHA256 from attempt 2 on; the harness copied to quarantine before
any edit of a superseded attempt; one stdout / stderr pair per launch with launch-numbered names; nothing
overwritten. A defect changes the harness ⇒ W-3 again and an empty store (D-3 §8.2, §8.3).

## 7. Real-data run size estimate (informational, not a requirement)

From the rp1 per-call telemetry: wall-clock per fit call by fitter and context, the number of fit calls per
trajectory implied by the ratified contract (full fit, K = 5 folds, LEFT / RIGHT probes, both families and the
spline, with the frozen start banks), and the resulting estimate for 906 trajectories in one process — with the
method stated and labelled ESTIMATE. It decides nothing.

## 8. Deliverables (each with an external .sha256 sidecar; no self-hash)

```text
D-3 §9 items 1–12 with "rp1" in every name, and:
 1  harness rp1 (child of b988e962…; diff against it delivered as a file)
 2–3 generator 68d126cf… and manifest 5c09c4f0… REUSED unchanged (named by path and hash)
 9  register — child of the r4-2 register (c281e713…), with T-KEY-NAMESPACE and a row per C-item
 10 report — its hash block prints the FULL SHA256 of every rp1 deliverable except the report itself (no prefix,
    no "by sidecar"; A-5 R42A-01); response table: one row per P-1 … P-9 and C-1 … C-6
 11 start-state inventory with §3 (a)–(e)
 12 attempt log
 A  per-call telemetry ; B store manifest ; B' store-read log (C-1) ; C capture records and the RUN1 / RUN2
    capture comparison ; D T-NONREG-R4-2 as CSV ; E quarantine copies, notes, every launch's log pair ;
 F1 the T-F1-LOADER-SYNTH fixture generator, manifest and files ; G the C-5 statement (and counter test) ;
 H  the §7 estimate ; T transmission list with every file and sidecar and its FULL SHA256 ; Z one zip for
    transport only
```

## 9. Report and end state

```text
status fields as v6 §13 / D-3 §10: corrections_complete ; mandatory_tests_all_run ; deferred_decisions ;
  narrowed_evidence (T-RP-1 by value) ; uncovered_coverage_rows ; open_findings
rp1_status = PREPARED_PENDING_INDEPENDENT_AUDIT iff every mandatory test of §4–§5 RAN and PASSED, the
  non-regression shows no S difference, every E difference matches its declaration, there is no U difference,
  and open_findings = [] ; otherwise PARTIAL_PENDING_PI with every non-empty
  list. Neither is QUALIFIED; neither binds the rp1 bytes under D-9 §2 (a) — that happens only after the
  independent audit, by a PI record
end state: PI_dispatch_record_hash = D-10 as observed ; real_data_access = false ; REAL_DATA_MODE = False in
  every launch ; F3_EXECUTION_READY = false ; F3_started = false ; commit = false
```

## 10. Independent audit after return (do NOT perform it yourself)

The auditor re-hashes every deliverable; re-runs T-NONREG-R4-2, T-STORE-READ-ACCOUNTING, T-KEY-NAMESPACE,
T-F1-LOADER-SYNTH and T-CONTEXT-ID-UNIQUE in an auditor environment; checks every E declaration against the
observed difference and that it was written before the run; reads the store manifest and the store-read
log against the attempt log (the D-3 §8.3 reading A-5 C-31 failed); diffs the rp1 harness against b988e962…
and checks that the diff contains only C-1 … C-6; checks the opened-file audit for any F1 path; checks the C-5
statement against the cited lines. The PI then decides whether the rp1 bytes are bound under D-9 §2 (a).

## 11. Not in scope

Any real-data read, fit or statistic; P03 thresholds; generator selection; F4 … F12; 6B (S-f);
any change to D-1 … D-9, A-1 … A-5, the r3 … r4-2 packages or frozen texts; QUALIFIED; F3_EXECUTION_READY;
commit.

## 12. Cited hashes (computed in this session on the 922f02d archive; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
922f02d39b2b01ddfe783402f4310fc68a04edce	refs/heads/p_konum_plus
$ cd <git archive of 922f02d> && sha256sum <cited files>
aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae  p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md
9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575  p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md
5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5  p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376  p_konum_plus/prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498  p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe  p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606  p_konum_plus/provenance/f3_step2_r4-2_transmission_list_2026-09-30.md
5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0  p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32  p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv
aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac  p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730  p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/calibration/f3_step2_residual_series_r4-2_2026-09-30.json
c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c  p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md
b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65  p_konum_plus/provenance/f3_step2_r4-2_attempt_log_2026-09-30.md
a4b5e176de9be9e8caa1b2145ce99e9c2539fcbea254df0a23ba2bfada470bbe  p_konum_plus/quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md
9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py
68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830  p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py
5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe  p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv
01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077  p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py
b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d  p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py
$ sha256sum <D-9 as delivered to the PI>
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  f3_step2_qualification_pi_decision_record_2026-10-02.md
```

## 13. Changes from the DRAFT (5f8fa4cf…) — review relayed by the PI on 2026-10-02

| # | where | change | reason |
|---|---|---|---|
| 1 | header, §0, §2, C-3, C-7, §11 | S-e = SYNTHETIC_ONLY_IN_RP1 and S-f = EXCLUDED_FROM_RP1 written in; the alternative branches removed | PI, 2026-10-02 |
| 2 | §5, §9, §10 | non-regression split into classes S (scientific: identical, no whitelist), E (expected run-record differences, declared before the run) and U (unexpected: open finding); the pass condition uses the classes | review: "every r4-2 field, no whitelist" would make a correct C-1 fix and new pids a finding; D-9's "whitelist'siz" refers to the named scientific values, as T-NONREG-R4-1 applied it in r4-2 |
| 3 | C-2 (ii) | scopes stated (the INJ-EXC passes lie inside the unit-test phase); the rule is "different computations never share a key"; a declared re-read of the same computation is allowed only in the declaring test's namespace | review: the list read the INJ-EXC passes as separate from the unit tests, and C-1's test re-reads on purpose |

## 14. Final text (PI approval of 2026-10-02)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, instrument, D-9 and D-10 lines | DRAFT r1 → final name; D-9's commit (fadf771) and D-10's file name written in | PI: "Push bitti. D-10'u onaylıyorum" |

No other change: every rule of DRAFT r1 (6a3679021abf10174b9267aa87398afade09a5f4be59d424d6ea67986d07bb54) stands.
