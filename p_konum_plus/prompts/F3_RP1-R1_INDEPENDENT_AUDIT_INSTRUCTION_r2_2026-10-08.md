# p_konum_plus — F3 real-data preparation rp1-r1 — Independent audit instruction r2 (2026-10-08)

```text
instrument          = F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md
supersedes          = r1 47f7e6de28b46db8c1aa1e29ad466b1c8a51497399d655529714d13a21116b6d and the first version
                      ddcbcb8451b3ed15c90f78f59a0f5da5e342098bcb04a56f1361b942606468ff (neither used by an auditor);
                      changes listed in §9 (r1) and §10 (r2)
purpose             = the independent TEKNİK audit that rp1-r1 instruction §10 and D-11 r1 §4 require before the PI
                      decides whether the rp1-r1 harness bytes are bound under D-9 §2 (a)
repository          = github.com/onertartan/tartan-names, branch p_konum_plus, commit 9035df0
                      (9035df0831d8646cca7f1e73937161a3d2d7d018; read-only for you). 9035df0 = the rp1-r1 package
                      (63d4846) + 4 added files: transmission list r1 and the executor's disclosure note, with sidecars
drafted_by          = Claude (Claude Code cloud session) at the PI's request. That session drafted the rp1-r1
                      instruction (DRAFT r2, 2226fc96…) and D-12; it did NOT run rp1-r1 and does NOT perform this
                      audit. Its post-push custody check (§7 below) is an input, not evidence you may rely on
you are             = the auditor. Not the executor, not the drafter. You decide nothing for the PI and declare
                      nothing qualified, bound or closed except ledger items (D-11 r1 §7; rp1-r1 instruction §3)
governing text      = rp1-r1 instruction p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
                      (2226fc96…), especially §4 R-1 … R-5, §6, §8 and the pass criterion of §9 ; D-12
                      (2c23130d…) ; D-11 r1 (0b177ee4…) §4, §5, §7 ; the rp1 instruction (a57b6fca…) where rp1-r1
                      does not replace it
```

## 0. Rules

```text
- Evidence is the delivered bytes at 9035df0 and what you execute yourself. Chat messages, the executor's report
  and this instruction's §7 are claims to check, not evidence.
- No writes to the repository, no commit, no push. Re-runs only in a disposable copy (rp1-r1 R-4 procedure).
- No real SSA / F1 data. Do not open data/raw/…, the F1 eligible manifest, or any file named in
  manifests/f1_input_hash_table_2026-08-28.csv. You may read the hash column of that table to check that the
  synthetic fixtures are hash-disjoint from it. Compute no algorithm × CVI outcome.
- Evidence tiers on every claim: [A] verified on the delivered bytes; [A-S] executed by you; [X] executor claim
  not verified. A check you could not run is NOT PERFORMED, with the reason.
- Findings: give both labels — v6 (global blocker / gate-specific blocker / cleanup / informational) and
  D-11 r1 §5 (STOP / B / K / T / I) — with file:line, evidence and closure action. You may raise a class the
  executor or this instruction assigned (D-11 r1 §2); only the PI lowers one.
- State your identity (model, session) and prior exposure to this project.
```

## 1. Custody (D-11 r1 §4 item 1)

```text
1.1 Every file of the CURRENT transmission list provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md
    (98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956) equals its listed hash and its sidecar.
    The superseded list (…_2026-10-05.md, 99c5d103…) stays in place unchanged; it differs from r1 in its table
    by exactly two rows: the correction-report row and the list's self-reference row (which names its own file
    and points to its sidecar; it carries no self-hash, and this item does not permit one). Check this with a
    diff; any other table difference is a finding. Every file added in b6d2483..9035df0 has a
    sidecar or is listed with a reason why not.
1.2 Dispatch: instruction 2226fc96…, D-12 2c23130d…, the rp1 audit record 2fa28e2a…, the review aa9fcaa9…; the
    standing instruments of rp1-r1 §1 at their hashes.
1.3 Parents unchanged: git diff b6d2483 9035df0 shows only additions under p_konum_plus/.
1.4 Restart stores are not in the repository; the store manifest and store-read log are the store evidence.
1.5 Hash fabrication. The executor's disclosure note provenance/pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md
    (c446395e497bb42baa179d9c756c8b2664ea92ebbe6f80b064c5bb8ba6d63444) states that one hash of the superseded
    list (correction-report row) was completed by invention from a 16-hex printout, and that a self-scan of 108
    hash occurrences in 8 documents found no second case. (a) Classify this finding with both labels and the
    reason. (b) Do not rely on the self-scan: check every hash, count and status value the executor wrote in the
    report, register, attempt log, start-state inventory, NR CSV header lines and both lists against the bytes or
    against your own run; a value you cannot trace to bytes or to command output is a finding. (c) Check the
    claim that every hash in list r1 was computed by script at write time as far as the bytes allow (no remaining
    mismatch; the erratum is the only place the wrong value appears).
```

## 2. Code (D-11 r1 §4 item 2)

```text
2.1 Final harness calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py (cac93ac6…) == the attempt-2 W-3
    custody record's harness hash.
2.2 Recompute both diffs yourself (vs rp1 39c733a3…, vs r4-2 b988e962…) and compare with the delivered .diff
    files. Every hunk maps to exactly one of C-1 … C-6 / R-1 … R-5 / "§5 wiring" / "§9 wiring". A hunk in
    run_real_scenario outside PI-c (D-12 §2: trajectory and mask ids of a scenario only) is a finding.
2.3 Attempt 1 → attempt 2 (quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py,
    4bffb33a…): the only change is the R-3 comparison-logic fix the supersession note describes. For EACH of the
    three fixes, decide whether it corrects a defect or relaxes the gate after a failure was observed:
      (a) COUNT double-canonicalization ; (b) removal of the "exc_injection_fixtures" declaration ;
      (c) exc_captures* compared with pid / start_iso / traceback stripped. For (c), check that the traceback
      differs only by the harness path (normalize the path and compare the rest); stripping the whole traceback
      would hide a change in where an exception is raised.
2.4 E declarations: every entry of EXPECTATIONS_E is an exact path with one kind (EQUAL / ADDITION / COUNT /
    MAY_DIFFER), none a subtree prefix; tests present in r4-2 have equal ran / passed; the INJ-EXC capture
    counts are declared with values. List which declarations changed between attempt 1 and attempt 2.
```

## 3. Re-execution (D-11 r1 §4 item 3; rp1-r1 §9 (3), (5))

```text
3.1 Follow provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md (f7b5baf1…) with the UNCHANGED
    harness in a disposable copy. Record your environment and compare it field by field with the binding one
    (Windows-10-10.0.19045-SP0, Python 3.11.7, numpy 1.26.4, scipy 1.14.1, thread pins 1). Match the Python /
    numpy / scipy versions if you can. Expected run time on the executor's machine: about 12 h, of which about
    10 h is T-F1-HANDOFF-SYNTH.
3.2 S class must be identical in your run: 37 evaluation objects and stop records in canon() form; RUN1 canonical
    556106e7…; residual 3ee624f3…; RUN1 == RUN2. An S difference is never a pass in any environment:
    T-NONREG-R4-2 fails and the D-11 r1 §5 STOP behaviour applies — report it to the PI, do not resolve it.
3.3 Every mandatory test (rp1 §4, rp1-r1 §4) RAN and PASSED in your run, including T-F1-HANDOFF-SYNTH,
    T-CONTEXT-ID-UNIQUE, T-F1-CONTRACT-GAP, T-F1-REPRO-GATE-SYNTH, T-F1-LOADER-SYNTH (all branches),
    T-STORE-READ-ACCOUNTING (cold and warm), T-KEY-NAMESPACE, T-NONREG-R4-2.
3.4 If the procedure cannot be completed, report exactly where it stopped. Do not edit the harness to proceed.
```

## 4. Non-regression and accounting (D-11 r1 §4 items 4, 5)

```text
4.1 calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv: 2,115 rows (1 S, 2,114 E). Check it is
    full depth for results JSON, telemetry and test evidence; that every E row names its declaration and whether
    the declared expectation held (rp1-r1 R-3 asks for both; check whether the CSV carries them); that the three
    "stale at comparison time" end_state rows are a real ordering artefact and the final results file carries
    the refreshed values.
4.2 Derive from the plan the expected computations per phase and key family; compare with the per-call
    telemetry (22,217 rows: 21,725 fresh / 492 replay), the store-read log (730 rows) and the store manifest
    (67,313 units, one pid 34588). Replay rows equal the stored units' telemetry, cold and warm.
4.3 T-F1-HANDOFF-SYNTH runs under phase label "nr_gates" in the per-call telemetry. The executor classed this T;
    under D-11 r1 §5 a fix that changes a code-produced record is never T — classify it.
4.4 The family-fit telemetry of T-F1-HANDOFF-SYNTH is not row-logged (attempt log: "discarded by design"), while
    it is about 95 % of the run time and the basis of the §7 estimate. Say whether this blocks the accounting of
    item 4.2 and what the real-data instruction would need.
```

## 5. Item-by-item

```text
5.1 R-1: consumer handoff (x hashes fitted == real_x hashes), mask ids with family, ONE builder for dry table and
    consumer ids, F1ContractGap STOP, F1 reproduction gate on synthetic files (complete list, extra / missing /
    changed file, eligible manifest byte change). Map f1_* code to F1 freeze record §8.1 steps 1–11 and §8.2.
    In the harness's runs (executor's and yours) the F1 input hash table and the F1 eligible manifest are never
    opened: their paths and hashes are constants only (check the opened-file audit). This is a property of the
    harness. It is separate from your own limited read under §0 (the hash column of the F1 input hash table,
    for the disjointness check only). The eligible manifest and every raw / F1 data file stay unopened by you
    as well.
5.2 R-2: every QC branch tested with ok computed from got; the partial-name denominator test compares exact
    values; any branch claimed unreachable has its derivation in the register.
5.3 R-4: the procedure isolates root, custody, store and outputs; it worked for you (3.1).
5.4 R-5: source column; T-STORE-READ-ACCOUNTING phase label; cold / warm cases.
5.5 R-6: register (key-family field mapping, realscen row, unit conversion); §7 estimate labels (~3.6 days
    smooth SCEN-A scale vs ~62 days measured on F1-shaped flat-noise synthetic, family-fit dominated) — informational;
    report response rows; both diffs; three new standing sidecars; the F1 input hash table NOT sidecarred (ledger T,
    closure at real-data step 1).
5.6 Start-state inventory (dd18ce3d…) and ledger: previous_inventory_sha256 = a3ddcf1f…; every item has class,
    closure point and status; no item of this package marked CLOSED by the executor.
5.7 Attempt log (ba465fc5…): attempts and process starts; the pre-launch file write disclosed (harness copy made
    before §1 was complete, then removed); the "standalone pre-verification" of 2026-10-05 21:41 → 2026-10-06
    07:25 (attempt log L85): what code ran, where it wrote, and that no output of it entered a deliverable or the
    attempt-2 store. An undisclosed computation outside the attempt record is a custody finding.
5.8 Firewall: real_data_access = false; REAL_DATA_MODE = False asserted at start in every launch; no
    algorithm × CVI computation.
```

## 6. Ledger closure

For each of RP1A-01 … RP1A-07 and R42A-03 (b): CLOSED with the evidence you verified, or OPEN with the reason. You
are the only party that may write CLOSED for these items (rp1-r1 §3).

## 7. Input from the drafter's post-push checks (claims to verify, not findings)

The drafting session checked 63d4846 and then 9035df0 after each push (commands and output given to the PI on
2026-10-08):

```text
- 1,100 files added, all under p_konum_plus/; no .pkl / .zip / store directory.
- dispatched files at their hashes (2226fc96…, 2c23130d…, 2fa28e2a…, aa9fcaa9…).
- 36 sidecars added, all match their files.
- 10 added files have no sidecar: calibration/_w3_writer_rp1-r1_tmp.py and the 9 quarantined attempt-1
  outputs (quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_*).
- transmission list: 30 of 34 hashes match their files; 3 are values without a file path (canonical hash, and
  the two .diff files — those two match the .diff files); ONE MISMATCH: row L37, correction report, listed
  ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260, file and sidecar
  ebc28df8a94bd3b2249389caba08c35e8071afd0a7766f48f984c78a2d78ec40 — the first 16 hex digits agree and the
  rest differ, which a re-edit of the file would not produce; the list's header says "every hash OBSERVED".
  Check every other hash the executor printed (report hash block, attempt log, register) against the bytes.
- residual series rp1-r1 = 3ee624f3… ; the 1,023 synthetic fixture files are hash-disjoint from the 217 hashes
  of the F1 input hash table.
- 9035df0: exactly 4 files added (list r1, disclosure note, two sidecars), no other change; both files equal
  their sidecars; list r1 vs the superseded list: the table differs only in the correction-report row (now the
  file's true hash) and the self-reference row; no hash in list r1 mismatches the file it names.
- a scan of all 64-hex values in the 8 executor documents at 63d4846: 108 occurrences; 106 match some file in
  the repository; the two others are the wrong list row and 892076fc… (custody record of the deleted dry-check
  copy, expected absent). This scan matches a hash to ANY repository file, not to the file named beside it.
- exc_captures / exc_captures_run2 / exc_captures_unit_phase (r4-2 vs attempt 1 vs attempt 2): counts 1/1/1,
  1/1/1, 8/8/8; records equal after stripping pid, start_iso, traceback; raw differences only in those three keys
  (the traceback text itself was not compared — item 2.3 (c)).
```

## 8. Output

```text
deliver one file to the PI (not into the repository):
  f3_realdata_prep_rp1-r1_independent_audit_<your model id>_DRAFT_r1_<date>.md with an external .sha256 sidecar
sections : identity and prior exposure ; verdict ; custody (§1) ; code (§2) ; re-execution with the environment
           table (§3) ; non-regression and accounting (§4) ; items (§5) ; ledger (§6) ; findings table ;
           NOT PERFORMED list ; the scripts you ran and their output
verdict  : PASSED if no STOP, no B and no K whose closure point is this package is open on the delivered bytes,
           otherwise NOT PASSED. PASSED is not a binding, not QUALIFIED and not a decision. Close with one line for
           the PI: whether the D-9 §2 (a) preconditions (non-regression against r4-2 with no S difference in the
           executor run and in yours; this audit) are met, and every environment difference
```

## 9. Changes from the first version (ddcbcb84…)

| # | where | change | reason |
|---|---|---|---|
| 1 | header, §0, §1.1, §1.3 | commit 63d4846 → 9035df0; current list = list r1 (98ed374d…); superseded list kept | the executor corrected the list after the drafter's post-push check (PI instruction, 2026-10-08) |
| 2 | §1.5 | new: classify the hash-fabrication finding; check every executor-written value against bytes, not the self-scan | executor disclosure note c446395e… |
| 3 | §7 | 9035df0 check and the 108-occurrence scan added | drafter's checks of 2026-10-08 |

## 10. Changes from r1 (47f7e6de…) — review relayed by the PI on 2026-10-08

| # | where | change | reason |
|---|---|---|---|
| 1 | §1.1 | allowed table differences between the two lists = correction-report row AND self-reference row (no self-hash permitted) | §1.1 named one row, §7 two |
| 2 | §5.1 | "never opened" stated as a property of the harness's runs; the auditor's §0 read of the hash column is separate; eligible manifest and raw data stay unopened by the auditor | §0 and §5.1 read as contradictory |
