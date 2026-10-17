# p_konum_plus — F3 real-data preparation rp1-r2 — Independent audit instruction — DRAFT r1 (2026-10-12)

```text
instrument          = F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md   (DRAFT r1; binding when the
                      PI forwards it to the auditor naming its SHA256)
parent_draft        = F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_2026-10-12.md
                      0e95f5800c28fe00493a4d0f468ece95361c370b1e2bc00898a34ed1bb862301 ; changes in §10. This was the
                      one review round of D-11 r1 §6; remaining points go to the PI at signature
purpose             = the independent TEKNİK audit that rp1-r2 instruction §9 and §10 and D-11 r1 §4 require before
                      the PI decides whether the rp1-r2 bytes are bound under D-9 §2 (a)
repository          = github.com/onertartan/tartan-names, branch p_konum_plus, commit 25c7d51 (full id in §11;
                      read-only for you). 25c7d51 = d9a5e99 + 4,598 added files, all under p_konum_plus/
drafted_by          = Claude (Claude Code cloud session) at the PI's request of 2026-10-12. That session drafted
                      the rp1, rp1-r1 and rp1-r2 instructions, D-9 … D-14, D-11 r1 Ek-1 r1 and the rp1-r1 audit
                      instruction; it did NOT run rp1-r2 and does NOT perform this audit. Its post-push check
                      (§7) is an input, not evidence you may rely on
you are             = the auditor: a NEW session in a NEW directory. Not the executor (pkp-worktree), not the
                      drafter, and not the rp1-r1 auditor session (G:\PycharmProjects\rp1r1_audit), which wrote an
                      rp1-r2 draft by mistake (D-14 §3). You decide nothing for the PI and declare nothing
                      qualified, bound or closed except ledger items (D-11 r1 §7; rp1-r2 instruction §3, §7)
governing text      = rp1-r2 instruction p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
                      (bf53e1e9…), especially §0, §4 Q1 … Q11, §5, §6, §7, §8 and the pass criterion of §9 ;
                      D-13 (6b9ae30e…) ; D-14 (a0ec71cb…) ; D-11 r1 (0b177ee4…) §4, §5, §6, §7 ; Ek-1 r1
                      (4d43682f…) ; the rp1-r1 instruction (2226fc96…) and the rp1 instruction (a57b6fca…) where
                      rp1-r2 does not replace them by name
inputs, not directives = the rp1-r1 independent audit record (f3a6f369…), its findings IR1-01 … IR1-19 ; the
                      executor's auditor rerun procedure provenance/f3_realdata_prep_rp1-r2_auditor_rerun_procedure_2026-10-12.md
                      (f745aaba…)
```

## 0. Rules

```text
- Evidence is the delivered bytes at 25c7d51 and what you execute yourself. Chat messages, the executor's report,
  the executor's rerun procedure and §7 of this instruction are claims to check, not evidence.
- No writes to the repository, no commit, no push. Re-runs only in a disposable copy (§3).
- No real SSA / F1 data. Do not open data/raw/…, the F1 eligible manifest, or any file named in
  manifests/f1_input_hash_table_2026-08-28.csv. You may read the hash column of that table, for the
  disjointness check of §5.12 only. Compute no algorithm × CVI outcome.
- Evidence tiers on every claim: [A] verified on the delivered bytes; [A-S] executed by you; [X] executor claim
  not verified. A check you could not run is NOT PERFORMED, with the reason.
- Ek-1 r1 applies to you: every hash, count, status and timestamp in your record is transferred by machine from
  bytes or command output; an unavailable value is NOT OBSERVED; a prefix is written only as a prefix (`556106e7…`).
- Findings: give both labels — v6 (global blocker / gate-specific blocker / cleanup / informational) and
  D-11 r1 §5 (STOP / B / K / T / I) — with file:line, evidence and closure action. You may raise a class the
  executor or this instruction assigned (D-11 r1 §2); only the PI lowers one.
- This is the SECOND B-correction cycle of rp1 (D-13 PI-a). A new B you find is reported and goes to the PI
  before any further round (D-11 r1 §6): do not propose a third correction cycle as decided, and do not
  resolve it yourself.
- The pass criterion is the one of rp1-r2 instruction §9, quoted in §8 below. It is not widened by this
  instruction (D-11 r1 §6). The checks of §1 – §6 are how you establish it; a defect they reveal is a finding,
  classed under D-11 r1 §5, and counts against the verdict only through that class.
- State your identity (model, session, directory) and prior exposure to this project.
```

## 1. Custody (D-11 r1 §4 item 1, with Ek-1 r1 §3)

```text
1.1 Every file of provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv (e48f5f6b…) equals its listed
    bytes count, its listed hash and its sidecar, and the sidecar's own hash equals the listed sidecar_sha256. The
    list plus its own sidecar is exactly the set of files added in d9a5e99..25c7d51; nothing is modified or
    deleted (git diff --name-status d9a5e99 25c7d51).
1.2 Dispatch and standing instruments at their hashes: rp1-r2 instruction bf53e1e9…, D-13 6b9ae30e…, D-14 a0ec71cb…,
    the rp1-r1 audit record f3a6f369…, the rp1-r1 audit instruction r2 82472d63…, D-11 r1, Ek-1 r1, D-9, D-12, the
    rp1 and rp1-r1 instructions; the rp1-r1 package files of transmission list r1 (98ed374d…) unchanged.
1.3 The fixture tree. 2,204 files under calibration/f3_step2_rp1-r2_f1_synth_fixtures_2026-10-10/ have their
    delivery sidecars in a separate tree, provenance/f3_rp1-r2_fixture_delivery_sidecars_2026-10-12/, because
    the .sha256 files INSIDE the fixture tree are test input (raw checksum files of Q3). Check that the two
    trees correspond one to one and that no delivery sidecar lies inside the fixture tree.
1.4 Restart stores are not in the repository; the store manifest and store-read log are the store evidence. The
    attempt-1 quarantine (quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/) carries an inventory of 69,614
    quarantined local files; their store units are not delivered. Say what that inventory can and cannot
    establish.
1.5 Ek-1 r1 trace. Check every hash, count, status and timestamp the executor wrote in the report, the ledger
    (both versions), the requirement map, the response table, the final observed summary, the attempt log, the
    start-state inventory, the size estimates, the errata file and the transmission list against the bytes it
    names or against your own run. Match each hash to the file NAMED beside it, not to any file in the
    repository. A value you cannot trace is a finding.
1.6 D-14 §2 (1) cites the executor's intake evidence f3_realdata_prep_rp1-r2_intake_verification_2026-10-10.json
    (ef4a2ebf…) as "not in the repository". It is not among the 4,598 added files either (drafter's check, §7).
    Record it as [X]; it does not reopen D-14, which is a PI decision.
```

## 2. Code (D-11 r1 §4 item 2)

```text
2.1 Final harness calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py (4d2e3db0…) == the attempt-2 W-3
    custody record's harness hash == the launch end record's code_sha256. The harness loads three pinned
    dependencies (RP2_DEPENDENCY_PINS: gate tools, reproduction fixture generator, technical tests); each
    equals its pin. List every file the real-data path of this harness would load, so that the PI knows
    which bytes a D-9 §2 (a) binding would name.
2.2 Recompute both harness diffs yourself (vs the rp1-r1 harness cac93ac6…, vs the r4-2 harness) and compare
    with provenance/f3_realdata_prep_rp1-r2_harness_diff_vs_rp1-r1_2026-10-12.diff and …_vs_r4-2_2026-10-12.diff
    and their label CSVs. IR1-16: every hunk carries exactly one label assigned from its content; mixed hunks
    are split or listed once per label with line ranges. The two diffs are mapped to different label sets:
      vs rp1-r1 (the new changes of this package): every hunk maps to an rp1-r2 authorization — Q1 … Q11, §5 (a)
        / §5 (b) wiring, §8 delivery wiring (the delivered labels use Q1 … Q11, S5A, S8);
      vs r4-2 (cumulative): every hunk maps either to an earlier authorized change, marked as inherited — rp1
        C-1 … C-6 or rp1-r1 R-1 … R-5 (the delivered labels use C2, C3, C5, R1, R2, R5) — or to an rp1-r2
        authorization as above. An inherited hunk is checked against its own instruction, not re-labelled as
        a Q change; an inherited hunk that rp1-r2 modified carries the Q label for the modified lines.
    A hunk that maps to none of these is a finding. A label that names two items (the delivered CSVs contain
    "Q10 with Q9 phase ranges") is checked against the IR1-16 rule for mixed hunks. A hunk in
    run_real_scenario outside D-12 PI-c (Q1, Q2 lie inside it) is a finding.
2.3 Attempt 1 → attempt 2. Attempt 1 (harness 92181f38…, quarantined) failed at T-NONREG-R4-2 with 22 U. Two
    source changes followed, each with a delivered diff:
      (a) provenance/f3_realdata_prep_rp1-r2_attempt2_declaration_only_diff_2026-10-11.diff: 92181f38… → d34676d0…,
          22 ADDITION declarations for tests_run.T-RP1R2-Q1 … Q11 .ran / .passed in the test_evidence namespace;
      (b) provenance/f3_realdata_prep_rp1-r2_attempt2_harness_provenance_diff_2026-10-11.diff: d34676d0… →
          4d2e3db0…, ATTEMPT_NUMBER 1 → 2, SUPERSEDES_* fields, attempt-bound names of the log pair, the restart
          store directory and the runtime fixture custody file; plus …_launcher_provenance_diff_2026-10-11.diff
          for the launcher.
    rp1-r2 instruction §0 allows a change after an observed failure "only as the correction of a defect in the
    expectation or declaration itself, in a new attempt, with the observed failure, the defect and the change
    written in the attempt log; the auditor judges each such change". Judge (a) and (b) separately: defect
    correction or relaxation of the gate, with the reason written out.
    For (a), that the 22 paths equal the 22 attempt-1 U paths is necessary, not sufficient. For EACH of the 22:
      (i)   the Q requirement of rp1-r2 §4 that introduced the test, i.e. the authorization that existed before
            launch 1;
      (ii)  why the attempt-1 declarations lacked it (the attempt log says the results namespace already declared
            the new tests and the test_evidence namespace did not: check this on the attempt-1 harness);
      (iii) that the declaration only completes the missing namespace declaration: no existing declaration, kind,
            expected value, comparison logic or test changed, and no other leaf became acceptable;
      (iv)  that the observed failure, the defect and the change are in the attempt log before attempt 2.
    An ADDITION holds when the leaf is absent in r4-2 and present in rp1-r2, WHATEVER its value, so also show
    where a false .ran / .passed value would still fail the run (mandatory-test registry,
    end_state.mandatory_tests_all_run, record_test assertions), or report that the ADDITION would hide it.
    For (b): the attempt log says the PI authorized it by message ([X]; no PI record names it). Say whether it
    lies within "in a new attempt" or needs a PI record. Check that (a) and (b) are the ONLY changes (apply the
    diffs yourself; the drafter's result is in §7).
2.4 E declarations: every entry is an exact leaf path with one kind (EQUAL / ADDITION / COUNT / MAY_DIFFER);
    "[*]" stands only for a list index; no declaration covers a subtree (Q5 (b)). List the MAY_DIFFER
    declarations and say for each whether a scientific or firewall-relevant leaf can sit under it. What counts
    is the scope of the difference a declaration permits, not how many rows it covers. In particular
    results:opened_files_audit_derived[*] and results:opened_files_declared[*] are MAY_DIFFER, so the opened-file
    audit is NOT compared by the gate. Because these leaves record file access, it is not enough that no
    scientific leaf sits under them: the independent firewall check of §5.13 must show that the permitted
    difference hides no access to real data or to a result path.
```

## 3. Re-execution (D-11 r1 §4 item 3; rp1-r2 instruction §9)

```text
3.1 Directories. Use a NEW directory, e.g. G:\PycharmProjects\rp1r2_audit, with two clones of the remote at 25c7d51:
      ref\  the reference: never executed in, never written to; every comparison is against its bytes
      run\  the disposable copy you execute in
    git clone --branch p_konum_plus https://github.com/onertartan/tartan-names.git <dir>
    git -C <dir> checkout --detach <25c7d51 full id, §11>
    Record the exact commands you ran and their output. Do not copy anything from pkp-worktree or rp1r1_audit.
3.2 Follow the executor's procedure (f745aaba…) in run\ with the UNCHANGED harness, its dependencies, launcher and
    writer: move run\'s attempt-2 / launch-1 W-3, writer, start, pid, end and controller records and the attempt-2
    log pair (with sidecars) aside; F3_REPO_ROOT = run\ ; F3_RP1R2_LAUNCH = 1 ; OMP_NUM_THREADS =
    OPENBLAS_NUM_THREADS = MKL_NUM_THREADS = 1 ; the launcher f3_rp1-r2_launch_attempt_2026-10-10.py with Python
    3.11.7. The restart store .rp1-r2_attempt2_restart_store_2026-10-10 must not exist in run\ at launch. The
    launcher checks D-14 by its fixed hash: do not edit or bypass it. Gaps in the procedure (it does not say
    which delivered outputs the run overwrites in run\) are findings on the procedure (RP1A-07 / R-4 line), not
    licence to improvise: write down what you did.
3.3 Environment. Record yours and compare it field by field with the binding one (Windows-10-10.0.19045-SP0,
    Python 3.11.7, numpy 1.26.4, scipy 1.14.1, thread pins 1). Expected run time on the executor's machine:
    about 10 h (attempt 2: 10:05:26).
3.4 S class must be identical in your run: 37 evaluation objects and the 6 stop records in canon() form, RUN1
    canonical 556106e7…, RUN1 == RUN2, residual series 3ee624f3…. Compare your results file with ref\'s and with
    the r4-2 results (f2a0a4d5…) by your own script, not only through T-NONREG-R4-2. An S difference is never a
    pass in any environment: the D-11 r1 §5 STOP behaviour applies — report it to the PI, do not resolve it.
3.5 Every mandatory test (rp1 §4, rp1-r1 §4, rp1-r2 §4) RAN and PASSED in your run; every Q1 … Q11 positive case
    passes and every negative case fails with its expected token; T-NONREG-R4-2 has 0 S and 0 U.
3.6 Compare your non-regression CSV, telemetry, per-call telemetry, family telemetry, timing table, store manifest
    and store-read log with ref\'s: same rows except the leaves declared as process-specific (pid, timestamps,
    wall-clock, paths). Identical wall-clock values across the two runs are a red flag (D-11 r1 §4 item 5).
3.7 stderr. The attempt-2 stderr (afc4a041…) is byte-identical to the rp1-r1 launch-2 stderr, and the attempt-1
    stderr is the same bytes plus a final traceback (drafter's check, §7). This is an OPEN QUESTION, not a
    finding. Deterministic warnings of scipy and of the frozen F2 engine are a possible explanation. Equal bytes
    alone prove neither that the computation was redone nor that an output was copied, so examine three things
    together: your re-run's stderr against ref\'s; the launch records (start / pid / end, stderr_sha256) of
    rp1-r1 launch 2 and rp1-r2 attempts 1 and 2; and the launcher's output redirection (each log opened "xb"
    by the launcher for its own process). A difference in your run is not by itself a finding; explain it.
3.8 If the procedure cannot be completed, report exactly where it stopped. Do not edit the harness to proceed.
    Independent probes (mutations, constructed inputs) go in a THIRD copy, never in run\.
```

## 4. Non-regression and accounting (D-11 r1 §4 items 4, 5)

```text
4.1 calibration/f3_step2_rp1-r2_nonregression_vs_r4-2_2026-10-10.csv: 219,434 rows (1 S, 219,433 E; U = 0), columns
    path, classification, declaration_id, kind, held, reason, r4_2, rp1-r2. Check Q5 (a)–(c) on the bytes:
    full leaf depth for results JSON, telemetry and test evidence; every E row names its declaration and
    whether it held; EQUAL rows compare equal values too. Some MAY_DIFFER reasons still speak of "rp1-r1's
    own …" — say whether the reason text matches the leaf (T at most, unless it hides a wrong declaration).
4.2 The S row of that CSV is one summary row; the 37-object comparison sits in the harness (S block) and in
    test_evidence nonregression_vs_r4_1 (compared = 37). Confirm by reading the code that Q5 changed neither the
    S block nor the residual check (Q5 (d), last clause), and that the S block still runs on the same objects
    in the final harness.
4.3 Derive from the plan the expected computations per phase and key family; compare with the per-call telemetry
    (22,217 rows: 21,725 fresh / 492 replay), the family telemetry (47,706 rows), the store-read log (733 rows)
    and the store manifest (67,316 units, one pid 17884). rp1-r1 had 67,313 units and 730 read rows: account for
    the difference from the code changes. Replay rows equal the stored units' telemetry.
4.4 Q10. Every family-telemetry row in the delivered file is stage = primary and source = fresh. Say whether a
    fallback path was reachable on these inputs and, if so, why no fallback row exists; reconcile rows per key
    family with the store manifest's handoff units; check the timing table (6 rows) against the process clock.
4.5 The results file's end_state.rp1_r2_open_findings lists 13 items (IR1-04, RP1A-01 … 06 among them), the final
    ledger 5 OPEN items. The ledger note says the run results preserve the prelaunch ledger snapshot. Explain the
    difference ITEM BY ITEM: a table of the 13 ids with the prelaunch status, the final ledger status, the
    evidence named and the record (and timestamp) that moved it. IMPLEMENTED_PENDING_VERIFICATION is not a
    closure; only you or a PI record write CLOSED. IR1-13 stays OPEN / B under D-14 in both lists; a list or
    record that shows it otherwise is a finding.
4.6 The final size estimate (provenance/f3_realdata_prep_rp1-r2_size_estimate_final_2026-10-12.json) is labelled
    ESTIMATE and derived from Q10 telemetry: reproduce its arithmetic from the delivered bytes and state its scope.
    Informational for the PI's run-time decision; not part of the pass criterion.
```

## 5. Item by item (rp1-r2 instruction §4 – §6; the requirement map)

For each item: read the code at the location the requirement map gives, decide whether the positive and the
negative tests exercise the requirement as written (not only whether they pass), and add at least one probe of
your own where the delivered negative test could pass for the wrong reason.

```text
5.1  Q1 (IR1-02) real-mode intake: missing key / entry → F1ContractGap naming it, before any optimizer (call
     counter). Probe: a real-mode scenario detected only by a stratum kind "F1REAL".
5.2  Q2 (IR1-03) one id builder: the static test counts the literal "real:%s:%s:%s" once. Check that no other
     construction of the same id exists (f-string, concatenation, format with another literal).
5.3  Q3 (IR1-04) F1 reproduction gate, form B (D-13 PI-b): (i) custody hash, (ii) §7 field list, ordering and row
     counts 906 / F 435 / M 471, (iii) field-by-field re-derivation of the fields the freeze record defines, the
     others "verified by custody hash only", (iv) complete file list. Each negative case satisfies every
     precondition except its target and the test asserts which check raised (field / row / ordering pin the
     modified file's hash; manifest_hash keeps the original pin). The frozen real constant 8a6034eb… is never
     changed. Map the code to the F1 freeze record §7 and §8.1 / §8.2; a field or serialization value the record
     does not name and the code chooses is BİLİMSEL-a (instruction §9).
5.4  Q4 (IR1-05) no constant ok in t_f1_loader_synth: check the AST test catches every spelling of a constant.
5.5  Q5 (IR1-06, IR1-07) comparator: §2.4, §4.1, §4.2. The delivered Q5 cases report expected = got = true. A
     boolean result is not by itself a defect; what matters is that it is computed from the actual
     comparator output on the constructed documents. Show for each negative case (wrong equal COUNT, ADDITION
     present in both, EQUAL that differs, undeclared deep leaf under a declared parent, declaration on an absent
     path) that the gate fails FOR THAT REASON: the failing declaration or leaf it names, not another failure on
     the same document. Run the five constructions yourself, each with exactly one defect: each one alone must
     fail the gate. As a diagnostic probe, not a pass condition, also run one document with two defects and
     record how the comparator reports them; Q5 does not state a contract for reporting several defects at
     once, so a comparator that stops at the first is not by itself a defect.
5.6  Q6 (IR1-08) traceback signature: a different raising statement fails; the message and type still compared.
5.7  Q7 (IR1-09) resumed cold case accepted; replay == stored still checked.
5.8  Q8 (IR1-10) replay label on EVERY restore path: list the restore paths in the code and show each one.
5.9  Q9 (IR1-11) handoff rows phase f1_handoff; f1handoff__ keys map to onestart / splmode with scope f1handoff.
5.10 Q10 (IR1-12) §4.3, §4.4.
5.11 Q11 (IR1-18) the writer records the launch number from F3_RP1R2_LAUNCH; the harness asserts it. Your own
     W-3 record must say launch 1.
5.12 IR1-19 fixture custody: provenance/…_synthetic_fixture_delivery_custody_2026-10-12.csv (2,204 rows) and
     …_existing_synthetic_fixture_custody_2026-10-10.csv (1,023 rows) list every synthetic fixture with its SHA256.
     1,022 files of the rp1-r2 fixture tree are byte copies of the 2026-10-05 set (1,021 data files and the
     manifest), 1,182 are new Q3 files (§7). Say whether the copy is needed and whether the harness reads the
     copy or the original. Check that all 2,204 are hash-disjoint from the hash column of the F1 input hash
     table (§0), and that the Q3 files are synthetic by construction (generator, manifest-declared RNG, seed).
5.13 Firewall (D-11 r1 §4 item 6): real_data_access = false and REAL_DATA_MODE = False in every launch; the
     opened-file leaves of results (not compared by the gate, §2.4) contain no F1 / raw data path and no result
     path outside the declared set; no algorithm × CVI computation.
5.14 §5 (a) / IR1-13: the ledger keeps IR1-13 OPEN / B naming D-14; the executor wrote no CLOSED; status
     PARTIAL_PENDING_PI follows from instruction §8 because the standalone evidence is NOT OBSERVED.
5.15 §5 (b): the attempt log records two small-input executions (harness 92181f38…), one comparator-excerpt
     execution (harness d34676d0…) and a child pid, outputs kept outside the repository. (a) Every logged field
     §5 (b) asks for is present (code hash, directory, start / end, outputs, disposition). (b) Nothing they wrote
     appears in a deliverable or in the attempt-2 store (store manifest: one pid, one process start). (c) The
     post-run record scripts (finalize_delivery, verify_final_delivery, prepare_review_records) — say whether any
     of them executes the harness, a copy or an excerpt of its test sections; if one does and is not logged, that
     is a §5 (b) finding.
5.16 §6 records: IR1-14 (no absent value called verified), IR1-15 (errata counts from bytes; check each against
     the file it names), IR1-16 (§2.2), IR1-17 (§6), IR1-19 (§5.12).
5.17 Requirement map (18 rows): the rows match your own reading of the code (this is a pass condition, §8).
```

## 6. Ledger closure

```text
- For each of IR1-02 … IR1-12, IR1-14 … IR1-19, RP1A-01 … RP1A-06 and R42A-03 (b): CLOSED with the evidence you
  verified, or OPEN with the reason. You are the only party that may write CLOSED for these items.
- IR1-01 and RP1A-07 are recorded as closed by the rp1-r1 audit: confirm against that record (its lines 155 and
  169); do not re-close them.
- IR1-13 stays OPEN / B; D-14 decides it for the pass criterion (§8). Do not close it.
- R42A-09: the ledger gives its closure point as "re-verified this package" and keeps it OPEN, while instruction
  §9 does not list it among the items closing here. Say whether its closure point has arrived (D-11 r1 §4 item 7)
  and class the discrepancy.
- D-9 §2 (a) binding, A.5 (iii) inadmissible refit and the F1 input-hash-table sidecar stay OPEN; their closure
  points are a PI record, a PI decision and real-data step 1. Confirm only that the ledger says so.
```

## 7. Input from the drafter's post-push check (claims to verify, not findings)

The drafting session checked 25c7d51 on 2026-10-12 against a `git archive` of the commit (commands and output given
to the PI the same day):

```text
- 4,598 files added, all A, all under p_konum_plus/; no .pkl / .zip / store directory / rp1r1_audit file.
- transmission list: 2,298 rows; rows × (file + sidecar) + the list and its sidecar = 4,598 = the added set;
  0 missing, 0 extra, 0 duplicate; bytes, hash, sidecar content, sidecar name and sidecar hash match on every row.
- fixture tree: 2,204 files = 1,022 byte copies of calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/ (1,021
  data files + SYNTH_FIXTURE_MANIFEST.json; that set has 1,023 files, the one not copied being
  SYNTH_FIXTURE_MANIFEST.json.sha256, whose role the delivery sidecar takes) + 1,182 new Q3 files (q3_complete 298,
  q3_negative 884). 1,022 + 1,182 = 2,204. (The drafter's first chat report of 2026-10-12 wrote "1,022 fixture
  files and the manifest"; that was wrong — the manifest is inside the 1,022.) All 591 inner .sha256 input files
  match their targets; both fixture custody files match every file.
- harness 4d2e3db0… = W-3 attempt-2 custody = end record; the 40 pin checks of that custody record match the
  repository bytes; generator 68d126cf…, fixture manifest 5c09c4f0… (the r4-1 fixture manifest).
- S, by the drafter's own script on the two results files: 37 = 37 evaluation objects, same ids, 0 differing;
  6 = 6 stops, equal as multisets; RUN1 = RUN2 = 556106e7… in both; determinism true; the rp1-r2 residual file is
  byte-identical to the r4-2 residual file (3ee624f3…).
- NR CSV: 219,434 rows = 1 S + 219,433 E, no U, held = True on every row; kinds MAY_DIFFER 205,346, ADDITION 13,027,
  EQUAL 1,054, COUNT 6; 192,922 rows come from the single declaration results:opened_files_audit_derived[*].
- attempt 1 → 2: applying the two delivered harness diffs reproduces d34676d0… and 4d2e3db0… exactly; the first
  adds 22 lines (one declaration each) and closes the list bracket; the 22 attempt-1 U paths equal the 22 new
  ADDITION paths and all hold in the final CSV. The launcher diff was not checked.
- requirement map: 18 rows (Q1 … Q11, S5A, S5B, IR1-14 … 17, IR1-19); the Q rows' result column equals the results
  file verbatim; all cases ok; the file:line references point at the named functions. Whether the tests test
  the requirement was NOT checked.
- ledger: 31 items (24 IMPLEMENTED_PENDING_VERIFICATION, 2 CLOSED (prior auditor decision only), 5 OPEN);
  IR1-13 OPEN / B naming D-14; current_executor_closures = [].
- stderr: attempt-2 stderr = rp1-r1 launch-2 stderr byte for byte (cmp); the attempt-1 stderr is the same
  13,034,310 bytes plus a T-NONREG-R4-2 traceback; 32,985 UserWarning and 28 RuntimeWarning lines, the latter all
  from calibration/f2_step2_feasibility_harness_r3_2026-09-01.py; no line names the rp1-r2 harness.
- the intake evidence file cited by D-14 §2 (1) (ef4a2ebf…) is not among the added files.
```

## 8. Output and verdict

```text
deliver one file to the PI (not into the repository):
  f3_realdata_prep_rp1-r2_independent_audit_<your model id>_DRAFT_r1_<date>.md with an external .sha256 sidecar
sections : identity and prior exposure ; verdict ; custody (§1) ; code (§2) ; re-execution with the environment
           table (§3) ; non-regression and accounting (§4) ; items (§5) ; ledger (§6) ; findings table ;
           NOT PERFORMED list ; the scripts you ran and their output
pass criterion (rp1-r2 instruction §9, verbatim):
           rp1-r1 §9 (1)–(8) with "rp1-r2", plus: every §4 negative test fails the right way and every positive
           test passes in the executor run AND the auditor run ; IR1-13 closed with evidence verified by the
           auditor, or decided by a PI record under D-11 r1 §5–§6 that names it ; the requirement map's rows
           match the auditor's own reading of the code
verdict  : PASSED if the pass criterion is met and no STOP, no B and no K whose closure point is this package is
           open on the delivered bytes — IR1-13 counting as decided by D-14 under the criterion's second clause;
           otherwise NOT PASSED. PASSED is not a binding, not QUALIFIED and not a decision. A new B goes to the PI
           (D-11 r1 §6; §0). Close with one line for the PI: whether the D-9 §2 (a) preconditions are met
           (non-regression against r4-2 with no S difference in the executor run and in yours; this audit), the
           list of files a binding would name (§2.1), and every environment difference
```

## 9. Classes of this audit (D-11 r1 §8; from rp1-r2 instruction §9)

```text
denetim türü     : TEKNİK, D-11 r1 §4 items 1–7, with Ek-1 r1; item 3 by a re-run in an environment matched to the
                   binding one
classes          : Q1–Q11 HESAPLAMA ; §5 KAYIT + custody evidence (B by D-13 PI-a) ; §6, §7 KAYIT — as signed in
                   the instruction; you may raise one with evidence
korunan zorunlu kontroller : rp1 and rp1-r1 instructions except where replaced by name ; D-3 §8.3 ; D-9 §2 (a) ;
                   D-11 r1 Ek-1 r1
```

## 10. Changes

Before the first draft was delivered, the PI relayed an external review (ChatGPT, 2026-10-12) of the drafter's
post-push check report. It is worked into §2.3 (a), §2.4, §3.7, §4.5, §5.5 and §7 (fixture count) of the first draft
(0e95f580…).

Changes from the first draft (0e95f580…): review of that draft relayed by the PI on 2026-10-12 (ChatGPT; the one
review round of D-11 r1 §6)

| # | where | change | reason |
|---|---|---|---|
| 1 | §2.2 | the diff vs rp1-r1 maps to rp1-r2 authorizations; the cumulative diff vs r4-2 maps to inherited rp1 C / rp1-r1 R changes (marked as inherited) or to rp1-r2 authorizations; a combined label is checked under the IR1-16 mixed-hunk rule | the first draft required every hunk of both diffs to map to Q1 … Q11 or rp1-r2 wiring, which would turn the inherited rp1 / rp1-r1 hunks into false findings |
| 2 | §5.5 | each of the five negative constructions carries exactly one defect and must fail the gate alone; the two-defect document is a diagnostic probe, recorded, not a pass condition | the first draft made reporting both defects a requirement that Q5 does not state, contrary to D-11 r1 §6 (the criterion is not widened) |

No other change.

## 11. Hashes (computed in this session by script from `git archive 25c7d51`; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ git rev-parse d9a5e99
d9a5e9905e25c634ad3132aae85c6c346e5ead30
$ sha256sum <files of git archive 25c7d51>
bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md
a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md
2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364  p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md
a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913  p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md
82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e  p_konum_plus/prompts/F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md
98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956  p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md
e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75  p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv
f745aaba857135c6315b41151607318f6dddd50533dd956dd9c513f7b6bc9fff  p_konum_plus/provenance/f3_realdata_prep_rp1-r2_auditor_rerun_procedure_2026-10-12.md
4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3  p_konum_plus/provenance/f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c  p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py
eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8  p_konum_plus/calibration/f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py
5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe  p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json
81e1b523cc41561edabbea9098696646355b811d4b1ce86493bf10fae7e63818  p_konum_plus/calibration/f3_step2_results_rp1-r2_2026-10-10.json
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/calibration/f3_step2_residual_series_rp1-r2_2026-10-10.json
afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b  p_konum_plus/calibration/f3_step2_rp1-r2_attempt2_launch1_stderr_2026-10-10.log
afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b  p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log
$ python3 -I -c (canonical hash fields of the rp1-r2 results file)
run1_canonical_sha256 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77
run2_canonical_sha256 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77
$ grep (generator hash in the W-3 attempt-2 custody record; F1 eligible-manifest constant in the rp1-r2 harness)
generator_sha256 = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
F1 eligible manifest constant in harness = 8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32
$ grep (value cited in D-14 §2 (1); no file with these bytes is in 25c7d51)
executor intake evidence (D-14) = ef4a2ebf4d41bc85e755e35fac3f6060973fdcac748ce503266d01f50bd78721
```
