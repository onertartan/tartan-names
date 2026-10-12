# p_konum_plus — F3 real-data PREPARATION, second correction cycle rp1-r2 — Instruction (DRAFT r1, 2026-10-10)

```text
instrument            = Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md   (DRAFT r1; binding only when
                        a signed PI dispatch record (D-13) names its final bytes by SHA256)
parent_draft          = Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_2026-10-10.md
                        599d7f2d60e2179c1c8d7ab634d9e365041e38d278a09ffe97d23125ae05a93f ; changes in §12 (the one review round of D-11 r1 §6)
instrument_class      = PI instruction for the SECOND B-correction cycle of rp1 (tag rp1-r2). It closes the open
                        findings of the rp1-r1 independent audit. It prepares; it does not execute on real data
drafted_by            = Claude (Claude Code cloud session) at the PI's request of 2026-10-10 («8 B bulgusunu kabul
                        ediyorum; rp1-r2 talimatını ve D-13'ü hazırla»). This session drafted the rp1, rp1-r1 and
                        audit instructions, D-9 … D-12 and D-11 r1 Ek-1 r1; it did not run or audit rp1-r1
governing             = D-11 r1  0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639
                        D-11 r1 Ek-1 r1 (value-transfer rule)  4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955
binding instruments   = D-9  1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 (§2 (a))
                        rp1 instruction a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5 and rp1-r1 instruction (DRAFT r2) 2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d — every rule of
                        both stands for rp1-r2 unless a section below replaces it by name
                        D-12 2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364 (PI-b, PI-c carried; T-RP-1, S-c, S-e, S-f carried from D-10)
                        D-13 the rp1-r2 dispatch record (to be signed; names this file's final bytes; carries PI-a,
                             PI-b of §2)
inputs, not directives = rp1-r1 independent audit (GPT-6 / Codex)
                             f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md  f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913
                        rp1-r1 audit instruction r2  82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e
parent package        = rp1-r1 at commit 9035df0 (transmission list r1 98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956); historical and read-only.
                        Repository head at drafting: d9a5e99 (adds D-11 r1 Ek-1 r1 only)
frozen upstream       = untouched: v11 ; F1 freeze record ; F2 FINAL FREEZE r1 ; F3 STEP-1 r1 ; D-2. No new
                        scientific literal. real_data_access = false throughout. No algorithm × CVI output
```

## 0. Purpose and what this cycle does NOT do

```text
does    close every open finding of the rp1-r1 audit: B IR1-02 … 07, 12, 13 ; K IR1-08 … 11, 18 ;
        T IR1-14 … 17, 19 ; and the ledger items they keep open (RP1A-01 … 06, R42A-03 (b))
does not  read, open, hash-check or import any real SSA / F1 file (the F1 input hash table and eligible
          manifest stay unopened; REAL_DATA_MODE = False in every launch) ; fit anything on real data ; change
          the decision layer, the evaluator arithmetic, the criteria, the generator (68d126cf…), the fixture
          manifest (5c09c4f0…), any frozen scientific literal or any existing scientific expected_* value ;
          write 6B code (S-f) ; declare anything QUALIFIED or set F3_EXECUTION_READY ; commit
allowed   new test expectations of §4 and E declarations for the technical changes of §4, each with its reason,
          written in the harness source before launch 1 (so the W-3 custody hash fixes them). An expectation or
          declaration is never changed after an observed failure to make a run pass. A change after an observed
          failure is allowed only as the correction of a defect in the expectation or declaration itself, in a new
          attempt, with the observed failure, the defect and the change written in the attempt log; the auditor
          judges each such change
B round   this is the SECOND B-correction cycle of rp1. Under D-11 r1 §6, a new B found after it goes to the PI
          before any further round (continue / recorded limitation / STOP)
```

## 1. Preconditions (STOP before the first write, including any copy of the harness)

```text
1. this file and D-13 are the bytes D-13 names; every PI field of D-13 is filled (blank ⇒ STOP)
2. D-11 r1, Ek-1 r1, D-9, D-12, the rp1 and rp1-r1 instructions, the audit record and audit instruction r2 have
   the printed hashes (the two audit files are handed over with this file and placed unchanged in prompts/)
3. every file of the rp1-r1 transmission list r1 has its listed hash and sidecar; the rp1-r1 harness is
   cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb
4. the r4-2 baselines: results f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba, telemetry ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d,
   test evidence c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf
```

## 2. PI decisions (recorded in D-13, quoted here, not chosen here)

```text
PI-a  B confirmation     IR1-02, 03, 04, 05, 06, 07, 12, 13 are B (D-11 r1 §5 (iii)), as the audit classed them
PI-b  F1 reproduction    the F1 freeze record §7 names the eligible manifest's fields, ordering rule, row count
      gate form          and hash, but not its serialization (header, quoting, line endings, value spelling), and
                         no generator script is in the repository; a byte-exact re-serialization (rp1 C-3,
                         rp1-r1 R-1 (iv)) therefore needs values no ratified text names. D-13 records the PI's
                         choice of the gate form; R-Q3 below implements the chosen form
PI-c  consumer scope     D-12 PI-c unchanged. Q1 (intake guard for real_x / real_mask_ids) and Q2 (shared id
                         builder) are inside it
```

## 3. Start-state inventory and ledger (new file, before the first write)

As rp1-r1 §3, with: (a) every rp1-r1 deliverable re-hashed against list r1; (b) the audit record and D-13;
(c) the ledger carries every open item with class, closure point and status (OPEN / IMPLEMENTED_PENDING_VERIFICATION
/ CLOSED — only an audit or PI record writes CLOSED), INCLUDING the deferred F1 input-hash-table sidecar (T, closure
at real-data step 1) and every IR1-xx item; (d) previous_inventory_sha256 = dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286.

## 4. Code changes (child of the rp1-r1 harness; each with a positive and a NEGATIVE test, expected values in
## the test before the run)

```text
Q1  REAL-MODE INTAKE (IR1-02, B)
    a scenario is real-mode iff it carries real_x or real_mask_ids or any stratum kind "F1REAL". For a
    real-mode scenario the required keys are the legacy four PLUS real_x and real_mask_ids, and every
    (sex, trajectory) of strata has an entry in both. A missing key or entry raises F1ContractGap naming it,
    before any fit. Synthetic scenarios: unchanged behaviour.
    negative tests: remove real_x; remove real_mask_ids; remove one (sex, ti) entry of each → F1ContractGap
    with the named key/entry; no optimizer is reached (assert by a call counter)
Q2  ONE ID BUILDER (IR1-03, B)
    one function builds the real-mode mask id from (base, family, context); the consumer and
    f1_context_id_table both call it. negative/static test: the id format string occurs once in the harness
    source (AST/string count = 1); equality of consumer ids and dry table as in rp1-r1
Q3  F1 REPRODUCTION GATE (IR1-04, B) — form as chosen in D-13 PI-b
    form B (recommended): at real-data step 1, (i) the frozen eligible manifest's bytes are verified against
      8a6034eb… (custody; STOP on mismatch); (ii) it is parsed with the §7 field list and checked for the §7
      ordering rule and row counts (906 / F 435 / M 471); (iii) the pipeline re-derives, from the verified raw
      files, every field the frozen rule defines (trajectory_id, sex, name, year_min, year_max, T,
      n_observed_years, n_missing_total, eligible, eligibility_rule_id, trajectory_value_id) and compares them
      with the parsed rows field by field; any difference is a STOP naming row and field. Fields the freeze
      record does not define (source_scope, source_record_status, exclusion_reason) are listed as
      "verified by custody hash only". (iv) the complete hash-table file list check of rp1-r1 R-1 (iv) stands.
    form A: byte-exact re-serialization — only if D-13 names every serialization value; otherwise STOP.
    synthetic tests (deliverables, each with sidecar): a synthetic input hash table and a synthetic eligible
      manifest in the §7 field schema, written by a delivered generator from manifest-declared RNG; cases:
      complete list passes; missing / extra / changed-hash raw file; manifest hash mismatch; one field value
      changed in one row; one row removed; ordering violated → each STOPs with its own named reason.
      Each negative case satisfies every precondition except the one it targets, so that it reaches its
      target check: for the field / row / ordering cases the expected manifest hash of the MODIFIED synthetic
      file is computed in the test setup (custody passes) and the re-derived content is the unmodified one, so
      the STOP must come from the content, row-count or ordering check, and the test asserts which check
      raised it; the manifest-hash case changes only the bytes against an unchanged expected hash. The frozen
      real hash constant (8a6034eb…) is never changed by any test
Q4  NO CONSTANT ok (IR1-05, B)
    in t_f1_loader_synth every case's ok is computed from its got and expected (z_qc_pass, gate_pass included).
    static test: AST over that function finds no ok=<constant>
Q5  NON-REGRESSION COMPARATOR (IR1-06, IR1-07, B; replaces rp1-r1 R-3's comparison method, not its classes)
    (a) every declaration is evaluated whether or not the two values are equal:
        EQUAL holds iff equal ; COUNT a→b holds iff r4-2 = a and rp1-r2 = b ; ADDITION holds iff absent in
        r4-2 and present in rp1-r2 ; MAY_DIFFER always holds. A declaration whose path is absent from both
        documents fails
    (b) full depth: comparison and declarations are at leaf level; "[*]" may stand for a list index; no
        declaration covers a subtree. Telemetry: per row and column, as in rp1-r1
    (c) CSV: one row per compared leaf that differs or is declared, with path, class, declaration_id, kind,
        held, r4_2 value, rp1-r2 value (column named rp1-r2)
    (d) negative tests on constructed documents: wrong equal COUNT; ADDITION present in both; EQUAL that
        differs; undeclared deep-leaf difference under a declared parent; declaration on an absent path →
        each fails the gate; the S comparison (37 objects, stops, canonical, residual) is unchanged
Q6  TRACEBACK COMPARISON (IR1-08, K)
    replace whole-traceback stripping: normalize the harness file path to <HARNESS> and map each harness frame
    to (function name, source statement text); compare the resulting frame sequence and exception type and
    message. negative test: an exception raised from a different statement fails
Q7  STORE-READ TEST, RESUMED COLD CASE (IR1-09, K)
    the aggregate no longer requires cold fit1_reads == 0; a cold case is "empty test namespace at the start of
    the attempt"; a resumed read inside the same attempt is accepted and still checked replay == stored.
    negative test: replay row differing from stored payload fails
Q8  REPLAY PROVENANCE ON EVERY RESTORE PATH (IR1-10, K)
    every cache restoration (nrgates_all, unittests_all, realscen and any other) labels restored telemetry
    rows source = replay. test: write and restore one unit of each coarse kind in a TEST_ONLY namespace → rows
    labelled replay
Q9  PHASE AND FAMILY ATTRIBUTION (IR1-11, K)
    handoff rows carry phase f1_handoff; _key_family maps f1handoff__ keys to their underlying family
    (onestart / splmode) with scope f1handoff
Q10 HANDOFF FAMILY TELEMETRY (IR1-12, B)
    the telemetry run_real_scenario returns in T-F1-HANDOFF-SYNTH is kept and delivered: one row per optimizer
    call with phase, sex, trajectory, family, context, start_id, stage (primary / fallback), status, nit,
    nfev, wall_clock_seconds, source; plus a per-trajectory section timing table (start / end timestamps from
    the process clock). Accounting: rows per key family reconcile with the store manifest's handoff units
Q11 W-3 WRITER LAUNCH FIELD (IR1-18, K)
    the writer records the launch number given to it (environment variable), not a constant; the harness
    asserts the custody record's launch field equals its own launch number
nothing else changes
```

## 5. Executions outside an attempt (IR1-13, B)

```text
(a) For the rp1-r1 "standalone pre-verification" (attempt log L85): deliver what exists — code hash, directory,
    start / end, what it wrote and where, evidence that none of its outputs entered a deliverable or the
    attempt-2 store. A value that does not exist is written NOT OBSERVED (Ek-1 r1); nothing is reconstructed.
    If the evidence cannot be supplied, STOP-report to the PI before the first rp1-r2 launch. A report to the PI
    or a decision to continue does not close IR1-13: it closes only with evidence verified by the audit, or by a
    PI record that names it and decides it under D-11 r1 §5–§6 with its reason; until then it stays OPEN
(b) From now on: every execution of the harness file, a copy of it, or an excerpt of its test sections is
    logged in the attempt log (code hash, directory, start / end, outputs, and whether its outputs were
    discarded). No output of an execution outside a W-3 attempt enters a deliverable or an attempt store
```

## 6. Record items (T)

```text
IR1-14  verification wording: a value whose bytes are absent is X / NOT OBSERVED, never "verified"
IR1-15  narrative counts in the rp1-r2 documents written from bytes (Ek-1 r1); the rp1-r1 documents stay as
        they are; an errata section in the rp1-r2 report lists the rp1-r1 counts the audit corrected
IR1-16  both harness diffs (vs rp1-r1 and vs r4-2): every hunk carries exactly one label assigned from its
        content (not by keyword); mixed hunks are split by producing the diff with smaller context or by
        listing the hunk once per label with the line ranges each label covers
IR1-17  ledger complete and statuses as §3
IR1-19  a new fixture custody file lists every synthetic fixture file with its SHA256 (fixture files are not
        rewritten); new synthetic files of Q3 get sidecars
```

## 7. Requirement map (deliverable)

A table with one row per requirement of §4 – §6.
- code requirement (§4, §5 (b)): requirement id ; code location (file:line) ; positive test ; negative test ;
  result as observed in the final launch (copied from the results file by script)
- record requirement (§5 (a), §6): requirement id ; file:line of the record ; verification method ; evidence ;
  test columns N/A with the reason
This is a map for the auditor, not a self-audit: it closes nothing and the executor writes no CLOSED status.

## 8. Run, custody, deliverables, report

As rp1-r1 §5, §7, §8, with "rp1-r2" in every name, plus: the requirement map (§7), the Q3 synthetic files and
generator, the handoff family telemetry and timing table (Q10), the fixture custody file (IR1-19), the §5 (a)
evidence or its NOT OBSERVED record. Every hash, count and status in every delivered document follows Ek-1 r1
(written by script from bytes or command output). The size estimate is recomputed from the Q10 telemetry,
labelled ESTIMATE, with its scope.

rp1-r2_status = PREPARED_PENDING_INDEPENDENT_AUDIT iff every mandatory test of rp1, rp1-r1 and §4 RAN and PASSED,
no S difference, no U, every declared expectation held, open_findings = [], every item due in this package is
IMPLEMENTED_PENDING_VERIFICATION with evidence named, and the §5 (a) evidence is delivered; otherwise
PARTIAL_PENDING_PI (§5 (a): a PI decision does not by itself make the status PREPARED). End state as rp1-r1 §8 with D-13.

## 9. D-11 r1 §8 block

```text
denetim ve kapanış (D-11 r1'e göre; talimat imzasıyla kesinleşir, denetçi yükseltebilir)
  değişiklikler, sınıfları ve gerekçeleri :
    Q1–Q11  HESAPLAMA — code of the real-data path and of its gates, run on synthetic inputs only
            (real_data_access = false). Q3 form B changes the form of an instruction gate (not a frozen rule);
            PI-b decides it. Any serialization or field value the freeze record does not name ⇒ STOP (BİLİMSEL-a)
    §5      KAYIT + custody evidence (B by PI-a)
    §6, §7  KAYIT
  denetim türü                            : TEKNİK, D-11 r1 §4 items 1–7, with Ek-1 r1; item 3: the auditor re-runs
                                            end to end in an environment matched to the binding one, as in rp1-r1
  geçme ölçütü                            : rp1-r1 §9 (1)–(8) with "rp1-r2", plus: every §4 negative test fails
                                            the right way and every positive test passes in the executor run AND
                                            the auditor run ; IR1-13 closed with evidence verified by the
                                            auditor, or decided by a PI record under D-11 r1 §5–§6 that names it ;
                                            the
                                            requirement map's rows match the auditor's own reading of the code
  kapı prosedürünün PI onayları           : PI-a, PI-b (D-13, before launch 1)
  D-9 §2 (a) bağlaması                    : evet — after the rp1-r2 audit, one line in the dependent package's
                                            dispatch record; neither rp1's nor rp1-r1's bytes are bound
  kod-yol maddeleri (§3)                  : Q1–Q11 close in this package, verified by the rp1-r2 audit
  bu pakette kapanacak açık maddeler      : IR1-02 … 19 (except IR1-01, closed) ; RP1A-01 … 06 ; R42A-03 (b)
  korunan zorunlu kontroller              : rp1 and rp1-r1 instructions except where replaced by name ; D-3 §8.3 ;
                                            D-9 §2 (a) ; D-11 r1 Ek-1 r1
```

## 10. Independent audit after return (do NOT perform it yourself)

By a session that did not execute rp1-r2, with a re-run in a matched environment. A new B after this package goes
to the PI before any new round (D-11 r1 §6).

## 11. Cited hashes (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
d9a5e9905e25c634ad3132aae85c6c346e5ead30	refs/heads/p_konum_plus
$ sha256sum <git archive of 9035df0 unless noted> (each also equal to its .sha256 sidecar where one exists)
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md (origin/p_konum_plus)
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md
a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5  prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d  prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364  prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md
f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913  f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md (as uploaded)
82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e  F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md
98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956  provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md
cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb  calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  calibration/f3_step2_results_r4-2_2026-09-30.json
ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d  calibration/f3_step2_telemetry_r4-2_2026-09-30.csv
c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf  calibration/f3_step2_test_evidence_r4-2_2026-09-30.json
dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286  provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md
```

## 12. Changes from the DRAFT (599d7f2d…) — review relayed by the PI on 2026-10-10

| # | where | change | reason |
|---|---|---|---|
| 1 | §4 Q3 | each negative test meets every precondition except its target; for field / row / ordering cases the modified file's hash is computed in setup so the content check is reached, and the test asserts which check raised; the frozen real hash constant is never changed | as drafted, those cases could stop at the custody hash and never reach the content checks |
| 2 | §0 | the prohibition names frozen scientific literals and existing scientific expected_* values; new test expectations and E declarations are allowed before launch 1 with reasons; no change after an observed failure to make a run pass, except a disclosed defect correction in a new attempt, judged by the auditor | "any expected_* value or any literal" also forbade the new expectations §4 requires |
| 3 | §7 | code requirements: tests and observed result; record requirements: record location, verification method, evidence, test columns N/A with reason | record items have no harness test |
| 4 | §5 (a), §8, §9 | a report or a "continue" decision does not close IR1-13; it closes by audited evidence or by a PI record naming it under D-11 r1 §5–§6; status PREPARED needs the evidence | as drafted, "or the PI decided" could be read as closing an open custody B |

No other change.
