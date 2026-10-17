# p_konum_plus — F3 real-data PREPARATION, third correction cycle rp1-r3 — Instruction (DRAFT r1, 2026-10-14)

```text
instrument            = Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md   (DRAFT r1; binding only when
                        a signed PI dispatch record (D-19) names its final bytes by SHA256)
previous draft        = Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_2026-10-14.md  4081e16a… ; this r1 applies
                        the four corrections of the instruction's single review round, approved by the PI on 2026-10-14
                        (§12)
instrument_class      = PI instruction for the THIRD, narrowly scoped correction cycle of rp1 (tag rp1-r3), decided by
                        D-18 PI-3 A. It closes the K and T findings of the rp1-r2 independent audit that D-18 names. It
                        prepares; it does not execute on real data
drafted_by            = Claude (Claude Code cloud session) at the PI's request of 2026-10-14 («önerileri kabul ediyorum,
                        buna göre imzala ve gerekli çıktıları hazırla»). This session drafted the rp1, rp1-r1, rp1-r2 and
                        audit instructions and D-9 … D-18; it did not run or audit rp1-r2
governing             = D-11 r1 0b177ee4… ; D-11 r1 Ek-1 r1 4d43682f… ; D-18 (PI-2, PI-3 A) fe9b2b53…
binding instruments   = D-9 1ab17e44… (§2 (a)) ; the rp1, rp1-r1 and rp1-r2 instructions (a57b6fca…, 2226fc96…, bf53e1e9…) —
                        every rule of them stands for rp1-r3 unless a section below replaces it by name ; D-12 2c23130d…
                        (PI-b; PI-c as extended by D-18 PI-2) ; D-13 6b9ae30e… (PI-b = B, the F1 reproduction gate form) ;
                        D-14 a0ec71cb… ; D-19, the rp1-r3 dispatch record (to be signed; names this file's final bytes)
inputs, not directives = the rp1-r2 independent audit record dfa76b94… (findings IR1-08, IR2-01 … 07, IR1-16) ; the
                        stopped audit record f3f24b6a… ; D-15 278532bf…, D-16 3e2a5fe3…, D-17 25023f45…
parent package        = rp1-r2 at commit 25c7d51 (harness 4d2e3db0…, gate tools ca7233e7…, technical tests cd44ea6e…;
                        transmission list e48f5f6b…); historical and read-only
frozen upstream       = untouched: v11 ; F1 freeze record ; F2 FINAL FREEZE r1 ; F3 STEP-1 r1 ; D-2. No new scientific
                        literal. real_data_access = false throughout. No algorithm × CVI output
```

## 0. Purpose and what this cycle does NOT do

```text
does      close, in code: IR1-08 (Q6), IR2-01 (Q4), IR2-02 (Q5) — RP1A-03 closes with IR1-08 ; in records: IR1-16,
          IR2-04, IR2-05, IR2-06, IR2-07 ; and deliver what the next audit needs to verify D-18 PI-2 (IR2-03)
does not  read, open, hash-check or import any real SSA / F1 file ; fit anything on real data ; change any line of
          run_real_scenario (its body stays byte-identical to rp1-r2, §4 R3-5) ; change the decision layer, the
          evaluator arithmetic, the criteria, the generator (68d126cf…), the fixture manifest (5c09c4f0…), any frozen
          scientific literal or any existing scientific expected_* value ; widen any E declaration ; write 6B code ;
          declare anything QUALIFIED or set F3_EXECUTION_READY ; commit
allowed   the code changes of §4 and their tests; new test expectations and E declarations for them, each with its
          reason, written in the source before launch 1. The rp1-r2 §0 rule on changes after an observed failure stands
          unchanged: only as the correction of a defect in the expectation or declaration itself, in a new attempt,
          disclosed in the attempt log; the auditor judges each
round     this is the THIRD correction cycle of rp1 (D-18 PI-3 A). A new B after it goes to the PI before any further
          round (D-11 r1 §6)
```

## 1. Preconditions (STOP before the first write, including any copy of a source file)

```text
1. this file and D-19 are the bytes D-19 names; every PI field of D-19 is filled (blank ⇒ STOP)
2. D-11 r1, Ek-1 r1, D-9, D-12 … D-18 and the rp1, rp1-r1 and rp1-r2 instructions have the printed hashes; D-15 …
   D-18 and the two audit records are handed over with this file and placed unchanged in prompts/
3. every file of the rp1-r2 transmission list (e48f5f6b…) has its listed hash and sidecar; the rp1-r2 harness is
   4d2e3db0…, its gate tools ca7233e7…, its technical tests cd44ea6e…
4. the r4-2 baselines: results f2a0a4d5…, telemetry ac70eaf5…, test evidence c156b9e0…
```

## 2. PI decisions (recorded in D-18 and D-19, quoted here, not chosen here)

```text
D-18 PI-1  rp1-r2 NOT PASSED; its bytes are not bound
D-18 PI-2  PI-c extended by exactly the Q10 timing statements of run_real_scenario (harness 4d2e3db0…, lines 2235–2236
           and 2375–2379); nothing else in run_real_scenario. IR2-03 disposed; the next audit verifies the scope
D-18 PI-3 A  rp1-r3 within the scope of §0
D-19       dispatch of this instruction (its PI fields)
carried    D-12 PI-b ; D-13 PI-b = B (F1 reproduction gate form) ; D-14 (IR1-13 RECORDED_LIMITATION, OPEN / B) ;
           T-RP-1, S-c (child of the rp1-r2 harness), S-e, S-f
```

## 3. Start-state inventory and ledger (new file, before the first write)

As rp1-r2 §3, with: (a) every rp1-r2 deliverable re-hashed against its transmission list; (b) D-15 … D-19 and the two
audit records; (c) the ledger carries every item of the rp1-r2 audit's auditor table with its auditor status and the
attribution "closed by the rp1-r2 independent audit dfa76b94…" where the auditor closed it — the executor writes no
CLOSED of its own; IR2-03 "disposed by D-18 PI-2, scope verification pending"; RP1A-01 OPEN pending that verification;
IR1-13 OPEN / B under D-14; the D-9 binding, A.5 (iii) and the F1 input-hash-table sidecar with their closure points;
(d) previous_inventory_sha256 = the rp1-r2 start-state inventory's hash.

## 4. Code changes (child of the rp1-r2 harness; each with positive and NEGATIVE tests, expected values in the source
## before the run)

```text
R3-1  Q6 TRACEBACK SIGNATURE (IR1-08, K; closes RP1A-03 with it)
      in the gate tools, traceback_signature keeps, besides the normalised frame sequence it keeps today, the FULL
      exception text: every line of the traceback that is not the "Traceback (most recent call last):" header, not a
      frame line ('  File "…", line …, in …') and not the source line printed under a frame — in order, including
      multi-line messages and chained sections ("During handling of the above exception…", "The above exception was
      the direct cause…"), with the harness path normalised to <HARNESS> as for frames. Nothing else in the
      normalisation changes
      tests (in the technical tests, Q6 block; existing cases kept). The signature has two parts, the frame /
      source-statement part and the exception part; each case asserts both parts and the whole signature:
        positive  path-only difference → frame part equal, exception part equal, signature equal (kept)
        negative  changed raising statement (same exception type and message, different source statement; kept)
                  → frame / source-statement part DIFFERENT, exception part equal, signature different
        negative  same frames, DIFFERENT exception type, identical final line (multi-line message)
                  → frame part equal, exception part DIFFERENT, signature different
        negative  same frames, same type, multi-line message differing in a NON-final line
                  → frame part equal, exception part DIFFERENT, signature different
        negative  chained exception differing only in the cause's type
                  → frame part equal, exception part DIFFERENT, signature different
      the tests read the two parts from the signature as the gate tools build it; no second normalisation is
      written in the tests
R3-2  Q4 CONSTANT-ok GUARD (IR2-01, K)
      constant_ok_count also counts a constant assigned to ok in any of these spellings: x["ok"] = <constant>
      (subscript with constant key "ok", in Assign and AnnAssign), ok = <constant> (name target), x.ok = <constant>
      (attribute target), besides the keyword and dict-literal spellings it counts today
      tests: positive — the actual t_f1_loader_synth has count 0 (kept); one NEGATIVE per spelling (keyword,
      dict literal, subscript, name, attribute), each a constructed function with exactly that one spelling → count 1
R3-3  Q5 NEGATIVE ISOLATION (IR2-02, K)
      every Q5 negative carries exactly one defect and asserts the failing row's path and its classification /
      declaration id, not only that the gate failed. deep_not_hidden tests that a declaration on a PARENT path does
      not hide an undeclared leaf BELOW it. It is rebuilt on the rp1-r2 auditor's isolated construction
      deep_leaf_single_defect (audit record dfa76b94…, independent_probes): old {"n": {}}, new {"n": {"leaf": 3}},
      one declaration, path "n", kind MAY_DIFFER. The comparator keeps an empty container as a leaf, so the parent
      path "n" exists in the old document and its declaration genuinely holds there. Expected, asserted exactly:
        rows      two — "test.n" E, the declaration held ; "test.n.leaf" U_FINDING, kind UNDECLARED,
                  reason "undeclared differing leaf"
        failures  exactly one — path "test.n.leaf", kind UNDECLARED
      a comparator that applied the "n" declaration to the whole subtree would return no failure, and the test
      fails. The delivered two-defect construction may be kept as a diagnostic case outside the pass condition
R3-4  MAY_DIFFER REASON TEXT (IR2-06, T in a code file)
      the reasons of the declarations results:end_state.PI_dispatch_record_hash and …_path name the current dispatch
      record (D-19). Path, id and kind unchanged; no other declaration text is touched except where §4 R3-5 requires a
      new declaration
R3-5  IDENTITY, DEPENDENCIES, SCOPE GUARD (§8 wiring)
      new files, children of the rp1-r2 files: harness f3_step2_adequacy_harness_rp1-r3_<date>.py, gate tools
      f3_rp1-r3_gate_tools_<date>.py, technical tests f3_rp1-r3_technical_tests_<date>.py; the dependency pins name
      the new gate tools and technical tests and the unchanged fixture generator; launcher and custody writer only as
      far as names, the rp1-r3 tag, ATTEMPT_NUMBER = 1 and the SUPERSEDES chain (rp1-r2 harness 4d2e3db0… and its
      attempt-2 W-3 record) require; the restart store starts empty in a directory tagged rp1-r3
      scope guard, a new mandatory test T-RP1R3-RRS-UNCHANGED: the AST source segment of run_real_scenario in the
      rp1-r3 harness equals the one in the rp1-r2 harness 4d2e3db0… byte for byte (positive: equal; negative: a
      constructed copy with one changed statement → unequal)
      E declarations: every new leaf the changed tests produce (results and test_evidence namespaces alike, the
      rp1-r2 attempt-1 lesson) is declared before launch 1, with its reason, and pre-validated on synthetic
      documents under §5 (a2). The delivered rp1-r2 outputs do not contain these leaves; they are not checked
      against them
nothing else changes
```

## 5. Executions outside an attempt

```text
(a) BEFORE launch 1, two separate checks, each one logged execution under rp1-r2 §5 (b), with no harness
    computation, no optimizer and no store. Outputs stay outside every deliverable and store; the attempt log records
    for each: code hash, directory, start / end, inputs, outputs and their disposition
    (a1) HISTORICAL COMPARISON. The rp1-r3 comparator, with the R3-1 normalisation, compares the r4-2 baselines with
         the delivered rp1-r2 results, telemetry and test evidence under the rp1-r2 declarations as delivered (no
         rp1-r3 declaration is used here). Purpose: find before the long run an exception-text difference that the
         old last-line normalisation hid. Expected: the same rows as the delivered rp1-r2 non-regression. A
         further row, which only the full exception text can produce, means a traceback differs against r4-2: do
         not declare it away; record it in the attempt log and STOP-report to the PI before launch 1 (a changed
         raising site or message is a behaviour difference the gate exists to show)
    (a2) SYNTHETIC PRE-VALIDATION OF THE NEW DECLARATIONS. The new Q4, Q5, Q6 and RRS test blocks are run alone
         (they need no harness computation) to obtain the leaves they will write. For each namespace (results,
         test_evidence) two small constructed documents are built: an "old" one without the new leaves (and with
         the old value of each changed leaf) and a "new" one carrying them. The rp1-r3 comparator compares them
         under the rp1-r3 declarations of the new or changed leaves only. Expected: every one of those
         declarations holds, and no U. A U here means a leaf is undeclared or a declaration is wrong: correct it
         before launch 1 with its reason
    neither check replaces the final condition: the rp1-r3 outputs show 0 U against r4-2 and every declared
    expectation holds (§9 (4)). The comparator rule "a declared path absent from both documents is a failure"
    stays; no exception for absent paths is added anywhere
(b) rp1-r2 §5 (b) stands: every execution of the harness, a copy or an excerpt is logged; no output of an execution
    outside a W-3 attempt enters a deliverable or an attempt store
```

## 6. Record items (T)

```text
IR1-16  diffs of rp1-r3 against rp1-r2 and against r4-2: every hunk carries exactly one label, assigned from its
        content; mixed hunks split or listed once per label with the line ranges each covers; no combined labels.
        The two diffs have different label sets:
          rp1-r3 ↔ rp1-r2  only this package's changes: R3-1 … R3-5 and §8 wiring
          rp1-r3 ↔ r4-2    the inherited, recorded changes of rp1, rp1-r1 and rp1-r2, each labelled with its
                           originating package and item (as delivered in their label files), and this package's
                           changes, each with its own label
        For the rp1-r2 diffs: new, corrected label files (r1) beside the delivered ones, which stay unchanged
IR2-04  the auditor rerun procedure r1 for rp1-r3 lists every file the unchanged rerun overwrites — delivered outputs,
        logs, records and the regenerated synthetic fixture tree — and the preservation steps for each; the rp1-r2
        procedure stays unchanged
IR2-05  the R42A-09 ledger entry carries the current evidence: closed by the rp1-r2 independent audit dfa76b94…, with
        that record's reason; the stale prelaunch reason is not repeated
IR2-07  for the two outside-W3 executions of rp1-r2 (attempt log L149 and L461 at 25c7d51): deliver, as new provenance
        files with sidecars, the named records that exist (the execution records, retained-output inventories, the
        comparator script and wrapper, and their outputs where they are synthetic-only test outputs), each checked
        against the hash the attempt log printed. What does not exist or does not match is written NOT OBSERVED with
        the reason; nothing is reconstructed. No contamination is inferred from an absence; D-14 is not extended
IR1-14, IR1-15, IR1-17, IR1-19 practices (verification wording, counts from bytes, ledger completeness, fixture
        custody) apply to every rp1-r3 record
```

## 7. Requirement map (deliverable)

As rp1-r2 §7: one row per requirement of §4 – §6; code rows give code location, positive test, negative test and the
result copied from the results file by script; record rows give record location, verification method and evidence.
It closes nothing.

## 8. Run, custody, deliverables, report

As rp1-r2 §8 with "rp1-r3" in every name, plus: the §5 (a1) and (a2) execution records; the corrected rp1-r2 label
files; the IR2-07 provenance files or their NOT OBSERVED record; the rerun procedure r1. Every hash, count and
status in every delivered document follows Ek-1 r1. Run-time planning: the rp1-r2 executor launch took 10 h 05 m and
the auditor's rerun about 16 h on the same machine class; plan the launch so that the long run is not interrupted.

rp1-r3_status = PREPARED_PENDING_INDEPENDENT_AUDIT iff every mandatory test of rp1, rp1-r1, rp1-r2 and §4 RAN and PASSED,
no S difference, no U, every declared expectation held, open_findings = [], and every item due in this package is
IMPLEMENTED_PENDING_VERIFICATION with evidence named; otherwise PARTIAL_PENDING_PI. IR1-13 is not due in this package;
it stays OPEN / B under D-14 and does not by itself make the status PARTIAL. End state as rp1-r2 §8 with D-19.

## 9. D-11 r1 §8 block

```text
denetim ve kapanış (D-11 r1'e göre; talimat imzasıyla kesinleşir, denetçi yükseltebilir)
  değişiklikler, sınıfları ve gerekçeleri :
    R3-1 … R3-3  HESAPLAMA — gate and test code of the real-data path's harness, run on synthetic inputs only
    R3-4         KAYIT (documentary text inside a code file; no value or declaration kind changes)
    R3-5         HESAPLAMA (identity, pins, scope-guard test)
    §5 (a1, a2)  HESAPLAMA (two logged pre-launch executions)
    §6, §7       KAYIT
  denetim türü                            : TEKNİK, D-11 r1 §4 items 1–7, with Ek-1 r1; item 3: the auditor re-runs
                                            end to end in an environment matched to the binding one; the auditor's
                                            reading follows D-15 §3 (O-1 … O-6)
  geçme ölçütü                            : (1) custody: every deliverable = sidecar = transmission list; only additions ;
                                            (2) one label per hunk in both diffs; rp1-r3 ↔ rp1-r2 contains only hunks
                                            of R3-1 … R3-5 and §8 wiring; rp1-r3 ↔ r4-2 contains only the inherited,
                                            recorded changes of rp1, rp1-r1 and rp1-r2 and the hunks of this package
                                            (§6 IR1-16); run_real_scenario byte-identical to rp1-r2
                                            (T-RP1R3-RRS-UNCHANGED and the auditor's reading), and its changes against
                                            r4-2 beyond PI-c are exactly those D-18 PI-2 authorises ;
                                            (3) S class identical to r4-2 (37 objects, stops,
                                            556106e7…, residual 3ee624f3…, RUN1 == RUN2) in the executor run AND the
                                            auditor run; an S difference is never a pass: STOP behaviour of D-11 r1 §5 ;
                                            (4) full-depth comparison: 0 U, every declared expectation held ;
                                            (5) every mandatory test of rp1, rp1-r1, rp1-r2 and §4 RAN and PASSED, and
                                            every §4 negative fails for its stated target (Q6: the signature part
                                            named in R3-1; Q5: the path and kind named in R3-3), in both runs ;
                                            (6) accounting per D-11 r1 §4 item 5, fresh / replay separated ;
                                            (7) opened-file audit: no F1 / raw path ; (8) IR1-08, IR2-01, IR2-02,
                                            RP1A-03, RP1A-06, IR1-16, IR2-04 … 07 IMPLEMENTED_PENDING_VERIFICATION with
                                            evidence; RP1A-01 verifiable under (2); the auditor sets CLOSED item by item;
                                            the requirement map's rows match the auditor's own reading of the code
  kapı prosedürünün PI onayları           : D-18 PI-2, PI-3 A ; D-19 (before launch 1)
  D-9 §2 (a) bağlaması                    : evet — after the rp1-r3 audit, one line in the dependent package's dispatch
                                            record; no rp1, rp1-r1 or rp1-r2 bytes are bound
  kod-yol maddeleri (§3)                  : R3-1 … R3-3, R3-5 close in this package, verified by the rp1-r3 audit
  bu pakette kapanacak açık maddeler      : IR1-08, IR2-01, IR2-02, RP1A-03 ; IR1-16 (with RP1A-06), IR2-04 … 07 ;
                                            RP1A-01 (verification of D-18 PI-2's scope). Carried with their own closure
                                            points: IR1-13 (D-14), D-9 binding, A.5 (iii), F1 input-hash-table sidecar
  korunan zorunlu kontroller              : rp1, rp1-r1 and rp1-r2 instructions except where replaced by name ; D-3 §8.3 ;
                                            D-9 §2 (a) ; D-11 r1 Ek-1 r1 ; D-15 §3 for the auditor
```

## 10. Independent audit after return (do NOT perform it yourself)

By a session that did not execute rp1-r3 and did not draft it, in a new directory, with a re-run in a matched
environment and under the D-15 §3 reading rules. A new B after this package goes to the PI before any new round
(D-11 r1 §6).

## 11. Cited hashes (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ sha256sum <repository files>   (from git archive 25c7d51)
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md
a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364  p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md
6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md
a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md
4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7  p_konum_plus/calibration/f3_rp1-r2_gate_tools_2026-10-10.py
cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b  p_konum_plus/calibration/f3_rp1-r2_technical_tests_2026-10-10.py
e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75  p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv
4560e80e3c4995a94aa0164ef0d6825bcd9d946ca9069c78797271b5a8f1bb57  p_konum_plus/provenance/f3_realdata_prep_rp1-r2_start_state_inventory_2026-10-10.md
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json
ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d  p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv
c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf  p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/calibration/f3_step2_residual_series_r4-2_2026-09-30.json
68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830  p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py
5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe  p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv
$ sha256sum <previous draft of this instruction>
4081e16aed557adc2277ae042f7f4976725054cc665af79f7f2948544ac83a71  Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_2026-10-14.md
$ sha256sum <PI records signed in this cycle, and the rp1-r2 audit instruction>
278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md
3e2a5fe3373ae08fc91831d7312c5f994ff332efdf3bae50818cced98d608e45  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md
25023f450dc443a8d248fc8ed662812947f098f1532042a6858f159cee39deb9  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md
fe9b2b539f55efeda94d61c77ad30bd146de2ebcbbbf4d7a203fb13a8c0dcfa0  f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md
25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
$ sha256sum <rp1-r2 audit records, as uploaded by the PI>   (each equals its auditor sidecar)
f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md
$ S-class anchor from the r4-2 results file (run1_canonical_sha256 = run2_canonical_sha256)
556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77  RUN1 == RUN2 canonical
```

## 12. Changes from the DRAFT (4081e16a…)

The PI approved, on 2026-10-14, four corrections relayed from the instruction's single review round («aşağıdaki
önerileri onaylıyorum, buna göre düzelt ve imzala»). The drafter checked corrections 1 and 2 against the rp1-r2
gate tools ca7233e7… by running its comparator and signature function on the synthetic constructions only
(D-19 §6).

| # | where | change | reason |
|---|---|---|---|
| 1 | §4 R3-1 tests | each case asserts the frame / source-statement part, the exception part and the whole signature separately; a changed raising statement differs in the frame part with the exception part equal; type, multi-line message and cause changes differ in the exception part | the DRAFT required every negative to differ in the exception part, which the kept changed-raise case cannot do |
| 2 | §4 R3-3 | deep_not_hidden rebuilt on the auditor's deep_leaf_single_defect: old {"n": {}}, new {"n": {"leaf": 3}}, declaration "n" MAY_DIFFER; exact rows and the single failure test.n.leaf UNDECLARED | the DRAFT's example (declaration n.a, failure n.leaf) used sibling paths and did not test that a parent declaration does not hide a leaf below it |
| 3 | §4 R3-5, §5 (a), §8, §9 | the pre-launch check split into (a1) historical comparison of the delivered outputs under the rp1-r2 declarations with the R3-1 normalisation and (a2) synthetic pre-validation of the new declarations; the requirement of 0 U on the delivered rp1-r2 outputs removed; the final 0 U condition and the absent-path rule kept | the new leaves do not exist in the delivered rp1-r2 outputs, and a declared path absent from both documents is a failure |
| 4 | §6 IR1-16, §9 (2), §9 (5) | separate label sets: rp1-r3 ↔ rp1-r2 only this package's changes; rp1-r3 ↔ r4-2 the inherited, recorded changes plus this package's, each with its own label; (5) names the target of the Q6 and Q5 negatives | the r4-2 diff necessarily contains the changes of rp1, rp1-r1 and rp1-r2 |

Header lines name this r1 and the previous draft. No other change: §0 – §3, R3-2, R3-4, §7, §10 and the rest of §11
stand as in the DRAFT.
