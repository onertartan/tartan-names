# p_konum_plus — F3 real-data PREPARATION, correction cycle rp1-r1 — Instruction (DRAFT r2, 2026-10-05)

```text
instrument            = Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md   (DRAFT r2; becomes
                        binding only when a signed PI dispatch record (D-12) names its final bytes by SHA256)
parent_drafts         = DRAFT r1 Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r1_2026-10-05.md
                        28fdc98dfda5fade516ce4e06a49359d2ddcd47b235ec21f2989ac3f8f270860 (changes in §14) ;
                        DRAFT Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_2026-10-05.md
                        53b7921409e6c1d779392b83af1d2e5f903311a17649f00873585acf03dc1276 (changes in §13).
                        §13 = the one review round of D-11 r1 §6; §14 = the second round it allows, opened because
                        the reviewer named a finding that would cause a B or STOP if signed. No further round
instrument_class      = PI instruction for the B-correction cycle of rp1 (tag rp1-r1). It closes the three
                        gate-specific blockers of the independent rp1 audit and the code/record items that ride
                        with them. It prepares; it does not execute on real data
drafted_by            = Claude (Claude Code cloud session) at the PI's request of 2026-10-05 ("benim vermem
                        kararlar için önerilerini kabul ediyorum: rp1-r1 talimatını hazırla"). This session drafted
                        the rp1 instruction, D-9, D-10, D-11 r1 and the rp1 audit instruction; it did not run rp1
                        and did not audit it. It missed RP1A-01 … 03 when it checked the b6d2483 push (hash and
                        custody only)
governing             = D-11 r1  p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
                             0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639
                        (rp1-r1 is a new package: D-11 r1 applies; §8 block below)
binding instruments   = D-9  f3_step2_qualification_pi_decision_record_2026-10-02.md
                             1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 (§2 (a))
                        rp1 instruction  Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
                             a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5 — every rule of it
                             stands for rp1-r1 unless a section below replaces it by name
                        D-10 f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md
                             4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34 (T-RP-1, S-c, S-e, S-f
                             carried over unchanged)
                        D-12 the rp1-r1 dispatch record (to be signed; names this file's final bytes; carries the
                             PI decisions of §2)
inputs, not directives = rp1 independent audit (GPT Codex)
                             f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md
                             2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989
                             (computed on the copy the PI uploaded; no sidecar was received with it)
                        review of the DRAFT (GPT Codex) RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md
                             aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef (as uploaded; §13)
parent package        = rp1 at commit b6d2483 (transmission list 858091d6…); historical and read-only
frozen upstream       = untouched: v11 ; F1 freeze record ; F2 FINAL FREEZE r1 ; F3 STEP-1 r1 ; D-2. No new
                        scientific literal. No real SSA data (real_data_access = false throughout). No
                        algorithm × CVI output. QUALIFIED (D-9) is not re-opened
```

## 0. Purpose and what this cycle does NOT do

```text
does    R-1  RP1A-01: the F1 scenario the loader builds is CONSUMED by run_real_scenario; real-mode context ids
             carry the family (C-4 as the PI read it, §2 PI-b); a contract gap STOPs by construction; the deferred
             F1 reproduction gate is implemented and tested on synthetic files
        R-2  RP1A-02: T-F1-LOADER-SYNTH covers every QC failure branch; no test field is a constant
        R-3  RP1A-03: T-NONREG-R4-2 compares results JSON, telemetry and test evidence field by field, full depth
        R-4  RP1A-07 (evidence limit): an auditor in another environment can run the unchanged harness end to end
        R-5  RP1A-04 (code part): fresh vs replayed per-call telemetry rows distinguishable; T-STORE-READ in its
             own phase
        R-6  record items RP1A-04 (register part), RP1A-05, RP1A-06; first open-items ledger (D-11 r1 §7)
does not  read, open, hash-check or import any real SSA / F1 file (the F1 hash table and eligible manifest stay
          unopened; REAL_DATA_MODE = False in every launch) ; fit anything on real data ; select a generator ;
          write 6B code (S-f) ; change the decision layer, the evaluator, the criteria, the generator
          (68d126cf…), the manifest (5c09c4f0…), any expected_* value or any literal ; change any frozen text ;
          declare anything QUALIFIED or set F3_EXECUTION_READY ; commit
```

## 1. Preconditions (STOP before the first write if any fails)

```text
1. this file and D-12 are the bytes D-12 names; every PI field of D-12 is filled (blank ⇒ STOP)
2. D-11 r1, D-9, D-10, the rp1 instruction and the audit record above have the printed hashes
3. every file of the rp1 transmission list (858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9)
   has the hash printed there and in its sidecar; the rp1 harness is
   39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09
4. the r4-2 baselines: results f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba,
   telemetry ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d,
   test evidence c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf
5. the frozen upstream of rp1 instruction §1 item 4 has its recorded hashes
```

## 2. PI decisions (2026-10-05; recorded in D-12, quoted here, not chosen here)

```text
PI-a  B classification   RP1A-01, RP1A-02, RP1A-03 are B under D-11 r1 §5 (iii): a gate precondition (D-9 §2 (a)
                         non-regression; rp1 C-3/C-4 readiness) left unmet by a defect of the package. This is the
                         FIRST B correction of rp1 (D-11 r1 §6 counts from here)
PI-b  C-4 reading        "unique per sex, trajectory, family and context" is read literally: the family is part of
                         every real-mode (fixture_id, mask_id). Synthetic-path mask ids are NOT changed
PI-c  consumer change    run_real_scenario may change ONLY where it takes the trajectory and the mask ids of a
                         scenario: when the scenario carries real_x / real_mask_ids it uses them; otherwise the
                         r4-2 code path runs unchanged. This is the only change to the consumer the PI authorizes;
                         the rp1 rule "no change to the evaluator" stands for everything else
PI-d  ride-along         RP1A-04 and RP1A-06 close in this package
```

## 3. Start-state inventory (deliverable 11) and first ledger

Before the first rp1-r1 write, a new file `provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md`:

```text
(a) every rp1 deliverable with its FULL SHA256, re-computed, EQUAL / DIFFERENT against the rp1 transmission list
(b) D-11 r1, D-12 and the audit record with hashes as found; D-12's hash re-computed against its sidecar
(c) LEDGER (D-11 r1 §7; the first one). One row per open item with: id, source (record + finding no), class
    (D-11 r1 §5, both labels as the audit wrote them), closure point, status, closing package and evidence.
    At least: RP1A-01 … RP1A-07; every item that D-8, D-9 or A-5 left open with a closure point at or before
    "real-data fitting". An item the executor cannot classify from the text: list it as UNCLASSIFIED and
    STOP-report it, do not choose.
    Status values: OPEN ; IMPLEMENTED_PENDING_VERIFICATION (the executor's highest status: the change and its
    test are delivered) ; CLOSED (set only by the independent audit or a PI record, with its evidence). The
    executor never writes CLOSED for an item of this package; R42A-03 and RP1A-01 … 06 end the executor's
    phase as IMPLEMENTED_PENDING_VERIFICATION at most
(d) previous_inventory_sha256 = a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d (rp1)
```

## 4. Code changes (child of the rp1 harness 39c733a3…; each with a test that RAN and PASSED)

```text
R-1  F1 HANDOFF (RP1A-01; PI-b, PI-c)
     (i)   run_real_scenario: if sc carries "real_x", x = sc["real_x"][(sx, ti)] and the mask ids of every fit
           call of that trajectory come from sc["real_mask_ids"]; gen.make_traj is not called for it. Without
           "real_x" the code is the r4-2 path, byte-for-byte in behaviour (proved by R-3's S class)
     (ii)  real-mode mask ids contain sex, per-sex trajectory index, trajectory id, family and context; the dry
           table f1_context_id_table and the ids the consumer actually passes are built by ONE function
     (iii) contract gap STOP: f1_build_scenarios returns exactly the key set run_real_scenario reads from a
           scenario (list it in the register); each value is traced to the ratified contract (F3 STEP-1 r1 /
           D-2) by a comment with the clause. A key the consumer reads and the builder does not set raises a
           named STOP (F1ContractGap: <key>), never a default and never a KeyError crash
     (iv)  deferred F1 reproduction gate (rp1 C-3, last paragraph): code that, before any F1 read in a later
           cycle, (1) verifies the COMPLETE file list of the hash table — a missing, extra or mismatching file is
           a STOP — and (2) reproduces the eligible manifest byte-exact (906 rows, F 435 / M 471) — a mismatch is
           a STOP. In rp1-r1 it runs only on a synthetic hash table and synthetic eligible manifest generated with
           the T-F1-LOADER-SYNTH fixtures (manifest-declared RNG; no F1 file opened; F1 constants unread)
     tests (mandatory, expected values written in the test before the run):
       T-F1-HANDOFF-SYNTH: the T-F1-LOADER-SYNTH output → f1_build_scenarios → run_real_scenario, under the
         ratified per-scenario parameters, in its own key namespace (test id in every key); asserts that the
         consumer ran on the loader's arrays (the x hashes it fitted equal the hashes of real_x), finished
         without exception, and that the set of (fixture_id, mask_id, fitter) it passed equals the dry table
       T-CONTEXT-ID-UNIQUE (replaces rp1's): on the ids the consumer actually passed in T-F1-HANDOFF-SYNTH, every
         (fixture_id, mask_id) is unique per sex, trajectory, family and context
       T-F1-CONTRACT-GAP: a scenario with one consumer-read key removed STOPs with F1ContractGap naming the key
       T-F1-REPRO-GATE-SYNTH: complete synthetic list passes; missing file, extra file, one hash changed,
         eligible manifest with one byte changed: each STOPs with its own named reason
     The run time of T-F1-HANDOFF-SYNTH is reported per trajectory (it feeds R-6 RP1A-05). If the ratified
     contract does not name a value the handoff needs: STOP and report (D-11 r1 §2) — do not choose
R-2  QC COVERAGE (RP1A-02)
     T-F1-LOADER-SYNTH gains one case per remaining failure branch, each with expected = the named failure
     reason and ok = (got == expected): NONFINITE_PRE_Z (NaN and +Inf separately), NONFINITE_POST_Z,
     NEGATIVE_SHARE, BAD_SEMANTICS, RAW_FILE_MISSING, Z_STD_QC, Z_NORM_QC. A branch that cannot be reached
     through the public pipeline: the register gives the derivation (which earlier guard makes it unreachable)
     and the test calls the guard function directly on an input that trips it.
     denominator_includes_partial: expected = the per-year denominator computed in the test from the fixture
     rows INCLUDING the partial name; got = the loader's denominator; ok = (got == expected) exactly.
     In T-F1-LOADER-SYNTH and in every test this package adds or changes, each case's ok is computed from its
     observed got (the test evidence lists every (test, case, expected, got, ok)); no case of these tests carries
     a constant ok. Unchanged rp1 / r4-2 tests are not edited (a test that returns passed=True after its
     assertions have run is not a constant PASS)
R-3  NON-REGRESSION, FULL (RP1A-03; replaces rp1 §5's comparison method, not its classes)
     T-NONREG-R4-2 compares, against the r4-2 baselines of §1 item 4, at full depth:
       results JSON   recursive, every leaf, path printed
       telemetry CSV  row by row (same row order key as r4-2), column by column
       test evidence  recursive, every leaf
     Classes S / E / U as rp1 §5, with these rules:
       - E declarations are EXACT paths (or a telemetry column name), never a prefix that covers a subtree,
         each with its reason and ONE expectation kind:
           EQUAL          the value must be the same as r4-2 (e.g. a capture count 8 → 8)
           ADDITION       the field is absent in r4-2 and must be present in rp1-r1
           COUNT a → b    the value must change from a to b exactly
           MAY_DIFFER     the value is free (pid, start / end times, wall-clock, own paths and hashes); equal
                          or different both satisfy it
         They are a source constant in the harness, so the W-3 custody hash fixes them before launch 1
       - for every test present in r4-2, its ran / passed fields must be equal; any difference there is U
       - the INJ-EXC capture counts are declared with their values and reason before the run
         (exc_captures_unit_phase, exc_captures, exc_captures_run2; C-2's expectation, unmet in rp1)
       - telemetry: only the columns declared E may differ; a row count change is U unless declared
     Every compared field with a difference or a declaration is printed in the CSV (deliverable D) with class,
     declaration id and whether the declared expectation held; the run fails if any U exists or any declared
     expectation does not hold (EQUAL that differs, ADDITION missing, COUNT with another value). MAY_DIFFER
     never fails
R-4  AUDITOR RE-RUN PATH (RP1A-07)
     REPO = os.environ.get("F3_REPO_ROOT", "G:/PycharmProjects/pkp-worktree") in the harness and the W-3 writer;
     the default keeps the executor's behaviour. Deliver provenance/…_rp1-r1_auditor_rerun_procedure_….md
     stating, step by step, for a disposable copy and the UNCHANGED harness:
       isolation  the copy is a separate directory (F3_REPO_ROOT points at it); the committed custody record of
                  the final attempt is moved out of the copy's custody path into a kept-aside folder (the writer
                  refuses to overwrite and must not be edited); the restart store directory of the copy starts
                  empty and is not the executor's; outputs overwrite only files inside the copy
       custody    the auditor writes its own W-3 record with the delivered writer, for its own launch number;
                  the environment guard stays active and checks the auditor's environment against that record
       compare    S class and mandatory tests of §9 (3) and (5), side by side with the delivered values;
                  environment fields side by side with the binding environment (Windows-10-10.0.19045-SP0,
                  Python 3.11.7, numpy 1.26.4, scipy 1.14.1, thread pins 1). Running in a different environment
                  does not guarantee identical S values; the procedure recommends matching the Python / numpy /
                  scipy versions. An S difference in the auditor run is a failure whatever the environment
                  (§9 (3)); an environment difference is recorded but does not show that it caused the
                  difference
     The executor runs the procedure once itself in a second directory (Windows, same machine) as a dry check
     that it works end to end — not as an audit
R-5  TELEMETRY PROVENANCE (RP1A-04, code part)
     per-call telemetry gains a column source ∈ {fresh, replay}; rows appended from a stored unit are replay.
     T-STORE-READ-ACCOUNTING runs under its own phase label and additionally asserts: the replay rows of its
     deliberate second read equal, row for row, the telemetry records stored in the units it read — whether the
     first fit computed those units fresh in this process or itself read them from a store left by an earlier
     process of the same attempt. The test never requires the first fit to have been fresh. Both cases are
     tested: cold (empty test namespace) and warm (units already present, as after a restart). The column and
     the phase label are E (ADDITION / COUNT) in R-3
nothing else changes (rp1 §4 last paragraph stands)
```

## 5. Run, custody, logs

As rp1 §6 (C-6, T-RP-1 ACTIVE_FROM_START, one W-3 custody record per attempt, SUPERSEDES chain, quarantine before
any edit, launch-numbered log pairs, nothing overwritten). The store starts empty in a directory tagged rp1-r1.
The attempt log states attempts and process starts separately.

## 6. Record items (R-6)

```text
RP1A-04  register: the T-KEY-NAMESPACE table maps every key family to its fields (sex, trajectory, family,
         context, phase, run label, pass label, test id); the "realscen" row describes the SCEN-A/B synthetic
         coarse checkpoints correctly; counts given in units (optimizer call rows / stored units / store reads)
         with the conversion between them
RP1A-05  §7 estimate: labelled with the scope it was measured on; a second line from T-F1-HANDOFF-SYNTH's
         per-trajectory full-lattice timing; both ESTIMATE, informational
RP1A-06  report response table: one row per R-1 … R-6 and per RP1A-01 … 07 (and, for rp1, the C-1 … C-6 rows
         split); the harness diff against rp1 (39c733a3…) AND against r4-2 (b988e962…) delivered as files, each
         hunk labelled with exactly one of C-1 … C-6 / R-1 … R-5 / "§5 wiring" / "§9 wiring"; sidecars created for
         three of the four standing files that lack one (F2 harness r3, spline harness r2, F1 freeze record).
         The fourth, the F1 input hash table, is NOT opened or hashed in rp1-r1 (§0): its sidecar is a ledger
         item, class T, closure point = step 1 of the real-data execution cycle, where the F1 reproduction gate
         reads it anyway; "verified" in executor text means executor self-check
```

## 7. Deliverables (each with an external .sha256 sidecar; no self-hash)

rp1 §8 list with "rp1-r1" in every name, plus: the two diffs (R-6), the auditor re-run procedure (R-4), the
synthetic hash table / eligible manifest for T-F1-REPRO-GATE-SYNTH and their generator, the start-state
inventory with the ledger (§3). Transmission list with every file, sidecar and FULL SHA256; one zip for transport.

## 8. Report and end state

```text
rp1-r1_status = PREPARED_PENDING_INDEPENDENT_AUDIT iff every mandatory test of rp1 §4 and §4 above RAN and PASSED,
  no S difference, no U difference, every declared E expectation held, open_findings = [] and every ledger item
  whose closure point is this package is IMPLEMENTED_PENDING_VERIFICATION with its evidence named ; otherwise
  PARTIAL_PENDING_PI with every non-empty list
end state: PI_dispatch_record_hash = D-12 as observed ; real_data_access = false ; REAL_DATA_MODE = False in every
  launch ; F3_EXECUTION_READY = false ; F3_started = false ; commit = false
```

## 9. D-11 r1 §8 block

```text
denetim ve kapanış (D-11 r1'e göre; talimat imzasıyla kesinleşir, denetçi yükseltebilir)
  değişiklikler, sınıfları ve gerekçeleri :
    R-1  HESAPLAMA — real-data input code + consumer handoff; runs only on synthetic files in this package
         (real_data_access = false), so not BİLİMSEL-b; no unfrozen rule is set (an unnamed value STOPs), so
         not BİLİMSEL-a. PI-c authorizes the consumer change
    R-2  HESAPLAMA — test code of the loader
    R-3  HESAPLAMA — the non-regression gate
    R-4  HESAPLAMA — reproducibility (repository root, auditor procedure)
    R-5  HESAPLAMA — telemetry/accounting record produced by code (D-11 r1 §5: a fix that changes code is never T)
    R-6  KAYIT — register, report, estimate wording, diffs, sidecars
  denetim türü                            : TEKNİK (D-11 r1 §4 items 1–7 all apply: every path of this package
                                            runs). Item 3: the auditor re-runs end to end with the R-4 procedure
                                            ([A-S]) and compares environment field by field
  geçme ölçütü                            : (1) §1 custody and every deliverable = sidecar = transmission list ;
                                            (2) both diffs contain only labelled hunks, consumer hunks only as PI-c ;
                                            (3) S class identical to r4-2 (37 objects, stops, 556106e7…,
                                            3ee624f3…, RUN1 == RUN2) in the executor run AND in the auditor run.
                                            An S difference in either run is never a pass, whatever the
                                            environment: T-NONREG-R4-2 fails in that run and the D-11 r1 §5
                                            STOP behaviour for an undeclared scientific-object difference
                                            applies (the matter goes to the PI; "devam" / "kayıtlı sınırlılık"
                                            do not apply). A different environment is recorded field by field
                                            but does not establish the cause and does not suspend the STOP.
                                            Re-verification in an environment matched to the binding one
                                            (Windows-10-10.0.19045-SP0, Python 3.11.7, numpy 1.26.4, scipy
                                            1.14.1, thread pins 1) may follow; a report to the PI alone never
                                            satisfies the equality condition ;
                                            (4) R-3 full comparison: 0 U, every declared E expectation held ;
                                            (5) T-F1-HANDOFF-SYNTH,
                                            T-CONTEXT-ID-UNIQUE, T-F1-CONTRACT-GAP, T-F1-REPRO-GATE-SYNTH,
                                            T-F1-LOADER-SYNTH (full branches) and every rp1 mandatory test RAN and
                                            PASSED in the executor run and in the auditor run ; (6) accounting per D-11 r1 §4 item 5 with fresh /
                                            replay separated ; (7) opened-file audit: no F1 path (the F1
                                            freeze record is a record, not F1 data, and may be hashed as in
                                            rp1 §1) ; (8) RP1A-01 … 06 IMPLEMENTED_PENDING_VERIFICATION in the
                                            ledger with evidence named; the auditor sets CLOSED item by item
  kapı prosedürünün PI onayları           : PI-a … PI-d (D-12, before launch 1)
  D-9 §2 (a) bağlaması                    : evet — the rp1-r1 harness is the code the real-data path will run.
                                            After the independent audit, one line in the dispatch record of the
                                            dependent package (D-11 r1 §6); rp1's bytes are not bound
  kod-yol maddeleri (§3)                  : R-1 … R-5 — close in this package, verified by the rp1-r1 audit,
                                            before any real-data computation
  bu pakette kapanacak açık maddeler      : RP1A-01 … RP1A-06 ; R42A-03 (b) re-verified ; RP1A-07 by R-4 and the
                                            auditor run — each closed by the auditor, not the executor.
                                            Later closure point, with reason (D-11 r1 §7): sidecar of the F1
                                            input hash table → step 1 of the real-data execution cycle (the file
                                            stays unopened until then, §0)
  korunan zorunlu kontroller              : rp1 instruction §1 … §11 except where replaced by name ; D-3 §8.3 ;
                                            STEP-1 r1 L525–526 (6B remains a separate artifact) ; D-9 §2 (a)
```

## 10. Independent audit after return (do NOT perform it yourself)

By a session that did not execute rp1-r1. The auditor follows D-11 r1 §4 and the pass criterion of §9; runs the
R-4 procedure; reports per finding with both labels (v6 vocabulary and D-11 r1 class). A new B after this package
goes to the PI before any new round (D-11 r1 §6: this is the first B correction of rp1).

## 11. Not in scope

Any real-data read, fit or statistic; 6B (S-f; separate E-3 artifact); P03 thresholds; generator selection;
F4 … F12; any change to D-1 … D-12, A-1 … A-5, the audit record, the rp1 / r4-2 or earlier packages or frozen
texts; QUALIFIED; F3_EXECUTION_READY; commit.

## 12. Cited hashes (computed in this session; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
b6d2483d4bbd991167bb633d8d96647cc553bde2	refs/heads/p_konum_plus
$ cd <git archive of b6d2483> && sha256sum <cited files>
a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34  p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md
39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py
858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9  p_konum_plus/provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md
a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d  p_konum_plus/provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json
ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d  p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv
c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf  p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json
$ sha256sum <audit record as uploaded by the PI>
2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989  f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md
```

## 13. Changes from the DRAFT (53b79214…) — review by GPT Codex relayed by the PI on 2026-10-05

| # | where | change | reason (review item) |
|---|---|---|---|
| 1 | §6 RP1A-06, §9 | the F1 input hash table gets no sidecar in rp1-r1; it stays unopened; its sidecar is a T ledger item closing at step 1 of the real-data cycle; the F1 freeze record (a record, not data) stays hashable | 1 — hashing the table is reading it, against §0 (STOP risk). Chosen: defer, not an exception, so §0 stays without exceptions |
| 2 | R-5 | the replay check compares second-read replay rows with the telemetry stored in the units read; the first fit need not be fresh; cold and warm cases both tested | 2 — after a restart the first fit can itself be served from the store (B risk, as in attempt 3) |
| 3 | R-3 | each E declaration has one kind: EQUAL / ADDITION / COUNT a → b / MAY_DIFFER; failure = a declared expectation that does not hold; MAY_DIFFER never fails; "declared but not observed" no longer fails by itself | 3 — a correct expectation can be "no change" (8 → 8) |
| 4 | §3, §8, §9 (8) | ledger statuses OPEN / IMPLEMENTED_PENDING_VERIFICATION / CLOSED; the executor's highest is IMPLEMENTED_PENDING_VERIFICATION; only the audit or a PI record sets CLOSED | 4 — the executor cannot meet a condition that needs the audit's result |
| 5 | R-2 | the "no constant ok" rule covers T-F1-LOADER-SYNTH and the tests this package adds or changes, not the whole harness; unchanged tests are not edited | simplification 1 — NR-01 returns passed=True after real assertions |
| 6 | R-4 | the procedure states isolation (separate root, committed custody record moved aside, empty store, outputs only in the copy) and recommends matching the binding Python / numpy / scipy versions; S equality in the auditor run stays required (as worded in DRAFT r2, §14 #1) | simplification 2 — the writer refuses an existing custody file; a different environment does not guarantee identical S, so the procedure aims at a matched environment; it does not relax equality |

No other change. The review recommended no new scientific decision and no further round; under D-11 r1 §6 a second
round is due only if a reviewer names a finding that would cause a B or STOP if signed.

## 14. Changes from DRAFT r1 (28fdc98d…) — second note of the same reviewer, relayed by the PI on 2026-10-05

| # | where | change | reason |
|---|---|---|---|
| 1 | §9 (3) | S identical in the executor run AND the auditor run; an S difference is never a pass in any environment: T-NONREG-R4-2 fails and the D-11 r1 §5 STOP behaviour applies; environment difference recorded, not treated as cause; matched-environment re-verification allowed; a report to the PI does not satisfy equality | DRAFT r1 added an exception (environment differs → report to PI) that the review had not proposed; it contradicted §9 (5) (mandatory tests incl. T-NONREG-R4-2 must pass in the auditor run) and would have suspended the D-11 r1 §5 STOP for a scientific difference. The reviewer's earlier note asked for S equality to be kept; DRAFT r1 misread it |
| 2 | R-4 compare | one sentence: an S difference in the auditor run is a failure whatever the environment; the environment difference does not show cause | consistency with #1 |
| 3 | §13 row 6 | rewritten: its isolation part stands; the environment exception it described is removed | the reviewer asked for row 6 to be adapted |

No other change.
