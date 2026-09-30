# Claude Code Prompt — F3 STEP-2 — Correction Execution (r3 cycle) — DRAFT v2
## Narrow child of prompt DRAFT v6 · closes the findings of the independent audit of the STEP-2 r2 package · child revisions only · no real SSA data · no 6B content · no QUALIFIED declaration by the executor

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`
**Date of draft:** 2026-09-21 (DRAFT v1: 2026-09-20)
**Task class:** CLASS_C implementation correction + synthetic path-coverage re-qualification (the STEP-2 r3 cycle)
**Authority:** Claude Code is execution/provenance authority only; NOT methodology authority, NOT PI authority, NOT an independent auditor
**Status:** DRAFT v2 — not dispatched. It replaces DRAFT v1, which was never dispatched and is not an input of the r3 cycle. This file becomes the dispatched instrument of the r3 cycle only through a PI dispatch record that names this file and its SHA256 (§3, P-4). The word DRAFT belongs to the file's identity; it is not by itself a dispatch prohibition

```text
prompt_id                  = Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
parent draft               = Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v1.md
                             53c5bfaf0412080effed12dd3d18d15f16cbdb00b024fdb432c8e053ee9292ca
                             (never dispatched; superseded by this file; the changes are listed in the table after
                              the reading guide below)
addressee / author         = addressed TO Claude Code (the executor); DRAFTED BY Claude (Cowork session;
                             independent/advisory auditor and prompt author). The same session wrote the
                             independent audit of the r2 package (DRAFT r1 … r5) and DRAFT v1 of this prompt,
                             and revised it into this DRAFT v2 at the PI's instruction of 2026-09-21
                             (configured model for this revision: claude-opus-5; for DRAFT v1 and the audit
                             records: claude-fable-5-1). Nothing in this lineage was produced or executed by
                             Claude Code
instrument type            = NARROW CHILD of Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
                             17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
                             v6 stays byte-unchanged and is PART OF THIS INSTRUCTION: every part of v6 that the
                             table in §4 does not replace stays binding in the r3 cycle
PI-ratified content        = f3_step2_pi_ratified_content_2026-09-07.md
                             da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
                             (S-1 = (a), S-2 = α, T-1 = AUTHORIZE, T-2 = T-2a, T-3 = AUTHORIZE, T-4 = T-4a,
                              T-5 = CONFIRM_WITHIN_SCOPE — unchanged; nothing in it is reopened)
basis (audit tier)         = independent audit of the r2 package, by Claude (Cowork session), NON-NORMATIVE:
                             DRAFT r1 bf23392339e27c7ee15adff4c72660d31765a71d239f9a2f8bf813aa6d1591be
                             DRAFT r2 2dcdfaa1325c607e713ed97bd32d574de5bbedb638533b7122b7d58933d5d3f7
                             DRAFT r3 25673517a26e626aaedf063b838b2bdf2f3ab9a991804beaa7929f51138e25fb
                             DRAFT r4 01305c61c600d801af0ad579baabc309caeaab3fa1ad4664a44627b705dc1a2e
                             DRAFT r5 916f48567402ff0ec036e415910ec79081b4548bf4188c913f480c3bd2e6804e
                             verdict NOT PASSED: 1 global blocker (R2A-01), 7 gate-specific blockers
                             (R2A-02 … R2A-08), cleanup items, informational items. Audit records identify
                             defects; they are not instructions. What the executor has to do is in THIS prompt.
                             One entry of DRAFT r1 is not relied on: its closure-map row AUD-07 (X-05,
                             "CLOSED [A]") — see Y-21
source hierarchy           = as prompt v6 (lines 95–101): v11 → F2 FINAL FREEZE r1 + accepted F2 execution
                             artifacts → r4 as ratified by freeze record r1 → audit records → the prompts →
                             historical provenance; the PI-ratified content stands where its own §1 places it.
                             Where this prompt or v6 and the frozen contract disagree, the frozen contract
                             governs and the executor records an exactness finding (v6 §10) — it never chooses
frozen contract            = r4 5e594136… AS RATIFIED BY record r1 7055f186… ; v11 d136502f…
PI decisions embedded      = 0            S / T options selected by this draft = none. The dispatch-record
                             template v2 carries T-R2-2 = AUTHORIZE_RESTART because the PI gave that value on
                             2026-09-21; the executor reads it from D-4, not from this file
new_scientific_literal_by_executor = 0
F2_reopening = false ; F3_STEP1_reopening = false ; new_methodology_review = false
drafter's own QC           = programmatic checks (every hash traceable to a file; every quotation and every cited line
                             number checked against its source; the v1 → v2 differences and the cross-references to
                             the dispatch-record template checked by script), one read-only consistency pass by a
                             sub-agent of the same session over both files, and a re-check of the resulting fixes by
                             the same sub-agent; its findings were worked in before release. This is the author's own
                             QC. It is NOT an independent review, and nothing here was executed against the real
                             harness or the executor's environment
```

How to read this prompt. (1) Read v6 first; it is long, and most of it still applies. (2) §4 below says, section
by section, what is replaced. (3) §6 lists the corrections of this cycle, Y-01 … Y-21 (Y is the letter after v6's
X; "K-05" always means the frozen K-05 invariant, never a correction; Y-21 was added in DRAFT v2 and numbered after
Y-20 so that the numbers of DRAFT v1 keep their meaning). Each names the audit finding it closes.
(4) Where v6 and this prompt are both silent, the frozen contract decides; where a choice remains, record an
exactness finding and STOP that path (v6 §10). (5) In every part of v6 that stays binding, read "r2" as "r3" for
the deliverables of this cycle — never inside the name of a frozen artifact (the spline qualification bundle r2,
its harness, manifest and results) — and read "the r1 files" as "the r1 and the r2 files" wherever v6 protects
parents.

Changes from DRAFT v1, made at the PI's instruction of 2026-09-21 and limited to six topics; apart from version
metadata (title, status, date, author and QC lines) nothing else was changed. The executor works from this file
only:

| topic | where | change |
|---|---|---|
| restart | §0 ; §1 ; §3 W-4 ; §4 (rows §4.4 / §4.5 and §8) ; §5 T-R2-2 ; Y-01 ; §8 ; §9 item 12 ; §10 ; §11 ; §12 | a restart layer is permitted under AUTHORIZE_RESTART, never required; the first attempt is one process; T-SINGLE-PROCESS applies when one process computed everything, T-RESTART-PROVENANCE when units came from several; keys over code, input and environment identity; RUN1 / RUN2 and test separation; counters over all processes. narrowed_evidence and the status rule are unchanged |
| RUN1 residual series | Y-21 (new) ; §4 ; list of carried-over corrections ; §8.1 ; §9 item 7 ; §10 ; §11 | X-05 is no longer carried over as closed: the r2 export re-fits in a separate pass. The series must be RUN1's own, linked by hash (T-RESIDUAL-LINK). The PI referred to finding G09 of an external (Codex) audit; the drafter did not have that record and checked the point against the r2 harness source |
| S-2 = α | Y-04 ; §12 B | the added condition "the class itself, not a subclass" is withdrawn; content §3 is quoted as written, and this prompt's implementation rules are marked as such (SUMMARY, not VERBATIM); call site and stage checks stay |
| invalid statistic in P03 | Y-03 ; §5 (S-R2-1 gap) ; §6.1 (new) ; §7 INJ-NAN-STAT-C4B, UT-USET-CONSTRUCTION (d) ; §12 A | C2, C4b and C5 mapped separately to their binding sources: a direct application of frozen r4 §2 and §3, not the drafter's composition; the one open state is S-R2-1. Scientific readings are no longer inside the list that `read_and_accepted` accepts. The C4b fixtures put the NaN on the RIGHT side, where Python's max would drop it |
| STOPs | §2.2 A (note on item 13), B (R-11) ; §2.3 D-2 ; §2 STOP scope ; §3 P-1, P-3 (d), W-1 (c) ; Y-17 and its check | a missing sidecar of a file that matches its printed hash is recorded and created, not a STOP; a disagreeing sidecar or a hash mismatch still STOPs; D-2 may be handed over like D-1; an unedited rule-text placeholder no longer reads as a rule text; the `stops` record is required only on STOP returns |
| dispatch record | §2.3 D-4 ; §3 P-3 ; §12 (lists and readiness table) | template v2; T-R2-2 read as it stands in D-4, any other text STOPs; `read_and_accepted` covers §12 B only |

---

# 0. Purpose

Correct the STEP-2 r2 harness so that every open X finding of the audit of the r2 package is closed (§6), re-run
the full synthetic qualification from scratch (§8: one clean process per attempt; units from several processes
only under §8.3), and deliver r3 child revisions of every STEP-2 artifact (§9). Fixture outcomes remain
`interpretation = PATH_COVERAGE_ONLY`. The executor records findings and STOPs where the contract is silent; it
never chooses. The executor does not audit its own output and never declares QUALIFIED.

---

# 1. Starting state and firewall (binding, except the two lines marked auditor tier)

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false
F3_STEP1 = FROZEN (r4 5e594136… as ratified by record r1 7055f186…) ; F3_STEP1_open_PI_rows = 0
F3_STEP2 r1 package        = historical parents
F3_STEP2 r2 package        = audited ; audit verdict NOT PASSED              [auditor tier ; non-normative]
F3_STEP2_status            = PARTIAL_PENDING_PI by v6 §13, as computed by the auditor ; the executor's r2 claim
                             was CORRECTED_PENDING_INDEPENDENT_AUDIT          [auditor tier ; non-normative]
F3_STEP2 = QUALIFIED       = NOT declared
F3_EXECUTION_READY = false ; F3_started = false
real_data_fit = false ; adequacy_measurement = false ; generator_selected = false
P03_threshold_values = NOT_COMPUTED (must remain so)
6B_companion = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED (separately governed; not in this task)
```

The firewall list of v6 §1 and the additional prohibitions of v6 §9 stand unchanged. Added for this cycle:

```text
the r2 STEP-2 files (§2.2 B) are read-only parents: never edited, never re-labelled, never overwritten
no computed object of an earlier cycle — output, checkpoint, pickle, cached or intermediate result — is read
  by the r3 harness or copied into an r3 deliverable, and no computed object of an earlier process of this
  cycle either, with one exception: under T-R2-2 = AUTHORIZE_RESTART, a unit read from the restart store under
  every condition of §8.3. The SOURCE CODE of the r2 harness and generator may be the starting point of the r3
  child files. Python bytecode caches are not computed objects in this sense; start the interpreter with -B so
  that the run writes none
no surrogate for a custody item ; no reconstruction of a missing file from memory, a transcript or a cache.
  A transcript may only be CITED as the source of an attempt-history statement (§9 item 13)
```

---

# 2. Custody — verify before any write

## 2.1 STOP-class — frozen upstream (v6 §2.1, unchanged; mismatch or absent ⇒ STOP, global blocker)

```text
 1. ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md    d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3
 2. f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md          ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43
 3. f2_step2_feasibility_harness_r3_2026-09-01.py   (frozen F2 engine)          01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077
 4. f2_step2_fixture_manifest_2026-09-01.csv                                   daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b
 5. f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv                     c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666
 6. f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md              8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6
 7. f2_step2_feasibility_telemetry_r3_2026-09-01.csv                           cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49
 8. spline qualification bundle r2: manifest e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32
                                    harness  b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d
                                    results  ffda04b01abb1dd5399e7fb6434c006616723bf6ba7d95bfc697baeb6dd40484
 9. f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md              5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad
10. f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md                    7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460
11. f3_step1_pi_ratification_freeze_record_2026-09-05.md  (parent; historical) bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f
```

## 2.2 STOP-class — parents

A. The STEP-2 r1 package — v6 §2.2 items 12–19, with their rules unchanged. The seven lines are copied from v6;
the note on item 13 and the restated item 19 follow them.

```text
12. p_konum_plus/calibration/f3_step2_adequacy_harness_r1_2026-09-06.py        a95ad152b1ebcca6ff8b9ccfd34d122b9d6225a44d51254f4621fd4776a5b12f
13. p_konum_plus/calibration/f3_step2_fixture_generator_r1_2026-09-06.py       <PENDING — hash never delivered to the auditor; record the observed value>
14. p_konum_plus/calibration/f3_step2_fixture_manifest_2026-09-06.csv          d9fb75f8c643f53a67032e4b65a5bec1af85ccbdf1cb47c58577c1d3f23b565b
15. p_konum_plus/calibration/f3_step2_telemetry_r1_2026-09-06.csv              3ee208e72cc9d4f83b5d7d696f7252499c971480bc75e9aaabf6f51dbe0b08e0
16. p_konum_plus/calibration/f3_step2_results_r1_2026-09-06.json               e32de3f7ae43d39c87a21384a46fe84c42c940d7a48bd2cdb83fe2d4d29f06eb
17. p_konum_plus/calibration/f3_step2_class_c_pin_register_r1_2026-09-06.md    03486232ac62206b1eed52c2355e465364ec10fc02fb13d62dd32e2dfd50f9ca
18. p_konum_plus/provenance/f3_step2_synthetic_qualification_report_r1_2026-09-06.md 413283efd5f5212d3c5bb0b5a5a0be3c22adc2fad41c6a4ab142733fbdde2b95
note on item 13: v6 printed no hash for it. Record the OBSERVED hash. The file must agree with its own sidecar
    if one is present (disagreement ⇒ STOP). In the r2 cycle the executor reported the value
    03f3ac07e354342f41493b3ed771cdef10e3ba373d3bde92020ec6a730cdcdc3 (r2 generator docstring; [X], never verified
    by the auditor): if the observed hash differs from it, record a cleanup finding — that is NOT a STOP. Item 13
    is not an input of the r3 run (the r3 generator is a child of R-02)
19. external .sha256 sidecars of 12–18 (v6 rule, unchanged): each PRESENT sidecar is verified against its file,
    and a sidecar that disagrees with its file is a mismatch ⇒ STOP. A MISSING r1 sidecar is recorded
    NOT_LOCATED and created in W-1 (c) as a custody action only (it attests the current bytes; it is not
    retrospective evidence about the r1 run)
```

B. The STEP-2 r2 package — read-only parents of every r3 deliverable; byte-unchanged at the end of the task.
Hashes as computed by the auditor on the files the PI supplied.

```text
R-01. p_konum_plus/calibration/f3_step2_adequacy_harness_r2_2026-09-07.py        78b6210ace605fe9b43a3b15716535df28b8a25a11a072f68484e9cb7ad12776
R-02. p_konum_plus/calibration/f3_step2_fixture_generator_r2_2026-09-07.py       a1e6068c0868e7594242fcc6d588cc255f3b0f4bdf21d1e93851e5bafcf98e25
R-03. p_konum_plus/calibration/f3_step2_fixture_manifest_r2_2026-09-07.csv       807f49b30ac453e95259d39b546515acff8f93c2d6b7bebf81cd4a44621e3beb
R-04. p_konum_plus/provenance/f3_step2_r2_preexecution_custody_2026-09-07.md     afddfb590b78caea08dcde0ca28141e31835a8b3857af973b30a6a5eeff8a743
R-05. p_konum_plus/calibration/f3_step2_telemetry_r2_2026-09-07.csv              0459344f2b518531d5732577b98f031684ca29e3815c0e51af75b857be60155a
R-06. p_konum_plus/calibration/f3_step2_results_r2_2026-09-07.json               7b78b7ba64ded891fdd5098d3a35556938d1314c5d712a7dc6ee6046b7a26ed2
R-07. p_konum_plus/calibration/f3_step2_residual_series_r2_2026-09-07.json       f28bd6a02978154d1ba71d83a8ffe42cdc5e95d12a26c43b886439cca19b94f5
R-08. p_konum_plus/calibration/f3_step2_test_evidence_r2_2026-09-07.json         109ca273fbaf2e47800c048a87e72e9064c576642ecbe2a7e9e1331cf9426c0b
R-09. p_konum_plus/calibration/f3_step2_class_c_pin_register_r2_2026-09-07.md    f263eaceffb94a458f331fb80258e779f0a740634d2420e696406b191a7142d5
R-10. p_konum_plus/provenance/f3_step2_correction_report_r2_2026-09-07.md        af5b9151ebe4fc66e897899c1bc977f3cf7b3c0222da04601610affbb02c851b
R-11. the ten external .sha256 sidecars of R-01 … R-10, under the rule of item 19: each PRESENT sidecar is
      verified against its file, and a sidecar that disagrees with its file is a mismatch ⇒ STOP. A MISSING
      sidecar is not a STOP when its file hashes to the value printed above: it is recorded NOT_LOCATED and
      created in W-1 (c) as a custody action (it attests the current bytes; it is not evidence about the r2
      run). By the executor's own repository check of 2026-09-20 [X] all ten were present and agreed. Both
      line formats are accepted: `<hash> *<name>` and `<hash>  <name>`.
      Note on R-10: on 2026-09-20 the repository copy of R-10 was found modified (4 inserted bytes), was
      quarantined and restored byte-exact (custody incident CI-01). The value above is the original and
      restored value. If R-10 does not hash to it ⇒ STOP; do not repair it yourself
```

## 2.3 Dispatch-class (absence or mismatch ⇒ STOP via §3)

```text
D-1. Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md                 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
     expected under p_konum_plus/prompts/ ; if it is not in the repository, the copy the PI hands over at
     dispatch counts as present, provided it hashes to this value
D-2. p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md             da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
     if it is not in the repository, the copy the PI hands over at dispatch counts as present, provided it
     hashes to this value (as for D-1)
D-3. this prompt — record its observed SHA256 from the dispatched file (canonical name as in prompt_id; a
     download variant is renamed byte-unchanged before dispatch)
D-4. the PI dispatch record of the r3 cycle, f3_step2_r3_pi_dispatch_record_<date>.md, filled in from
     f3_step2_r3_pi_dispatch_record_TEMPLATE_v2.md (PI-owned; §3 P-3, §5) — supplied by the PI at dispatch;
     record its observed SHA256; verify its sidecar if one is supplied
```

## 2.4 Record-class (mismatch ⇒ cleanup; absent ⇒ import byte-exact from the PI attachment if attached, else NOT_LOCATED — never a STOP)

```text
C-1. v6 §2.3 items 20–23 and 26–28, as listed there (audit r4 of the r1 package 54e641e4… ; reconciliation r3 ;
     ADDENDUM A r1 cc4f97b4… ; PIN prompts v2 / v3 / v4 ; audit lineage ; correction candidates ; reviews)
C-2. Claude_Code_F3_STEP2_CLASS_C_IMPLEMENTATION_PIN_PROMPT_v5_2026-09-06.md      1532a5e481946d7c64d2ac5025ef16372b1f6530ab4fbc8aa5567392f18cf0af
     (the executed predecessor whose §4 pins v6 §6 keeps in force; the lines this cycle relies on are quoted
      in §6 Y-03 or cited in §6.1 next to the frozen r4 text they restate (STOP-class item 9), so the run does
      not depend on this file being present)
C-3. the five audit records of the r2 package named in the header, and their sidecars
C-4. objects of custody incident CI-01, under p_konum_plus/quarantine/ unless stated otherwise:
       the modified copy of R-10            6b8cf801c66e15356dd4fa138b3f2bbc7e26c4b2a02d61599349d32dd487d94d
       the executor's incident note         0de72545392a71e1b8c8ff4c10aa055ff2b26b629eb088b0d5235331fb7647b5
       the restored R-10 (provenance/)      = R-10 above (a newly written file with the original bytes)
     They are listed in the start-state inventory (§3 W-1) and are NOT files of an aborted attempt
C-5. p_konum_plus/provenance/f3_step2_r2_dispatch_precondition_stop_report_<date>.md, if it exists: the r2
     pre-execution custody record refers to it; record path and hash, or NOT_LOCATED
C-6. session transcripts of the executor from the r2 cycle, if they exist on the machine (for example
     b800288b-637c-4206-9aff-fe894d0b09e7.jsonl, named in the CI-01 incident note): record path and hash;
     read-only; used only for §9 item 13
```

Surrogates are prohibited (v6 §2, unchanged). STOP scope (exact): absence or hash mismatch of any item of §2.1,
§2.2 or §2.3 ⇒ STOP with the item named. The exceptions are these and no others: item 13, which must be
present but whose hash is recorded instead of compared (§2.2 A), and a MISSING sidecar under item 19 or R-11,
which is recorded NOT_LOCATED and created in W-1 (c) — the file itself is still checked against its printed hash
(item 13: recorded). A PRESENT sidecar that disagrees with its file is a mismatch.
Absence of a record-class item ⇒ NOT_LOCATED and continue. Hash comparisons are case-insensitive.

Repository state: record root / branch / HEAD and `git status` at start (at the audit date: root
`G:/PycharmProjects/pkp-worktree`, branch `p_konum_plus`, HEAD `3e4daf4`, r2 files untracked — executor
statements [X]); preserve every existing user modification; `commit = false`.

---

# 3. Dispatch preconditions and write order (binding; replaces v6 §3)

```text
P-1  every item of §2.1, §2.2 A, §2.2 B present and exact (no surrogate), with the exceptions of the §2 STOP
     scope (the hash of item 13 is recorded, not compared ; missing sidecars)
P-2  D-1 and D-2 present and exact
P-3  D-4 present, and these SIX fields of it — and no others — are checked, readable without interpretation:
       (a) `sha256_computed_by_PI`: a 64-hex value (the SHA256 the PI computed on this file)
       (b) `values_equal = YES`
       (c) `confirmed = YES` (the seven values of D-2 stand unchanged)
       (d) S-R2-1 `value`: exactly one value from its allowed set (§5); for PI_RULE a rule text is given
           (the words "not applicable", an empty field or the unedited bracketed placeholder mean: no rule text)
       (e) T-R2-2 `value`: NOT_AUTHORIZED or AUTHORIZE_RESTART, read as it stands in D-4 (template v2 carries
           AUTHORIZE_RESTART, entered there at the PI's instruction); a blank counts as NOT_AUTHORIZED; any
           other text ⇒ STOP
       (f) `read_and_accepted = YES` (the engineering and test-design list of §12 B here; it accepts no
           scientific reading — §12 A)
     PENDING ⇒ STOP if: one of (a), (b), (c), (f) or the S-R2-1 value of (d) still shows its template
     placeholder ; T-R2-2 carries a text other than those of (e) ; (b), (c) or (f)
     is not YES ; S-R2-1 is blank or carries more than one value ; PI_RULE comes without a rule text ; a rule
     text comes with a value other than PI_RULE. Every other field of D-4 is informational and never a STOP
P-4  the observed SHA256 of D-3 equals, case-insensitively, `sha256_computed_by_PI` of D-4. The report cites D-4
     (path and hash) as the evidence of P-4 — not the source table of the content file, which disclaims that
     role
if any of P-1 … P-4 fails: STOP before any implementation ; report the failing precondition, observed vs
     expected values ; write nothing except the STOP report
     (p_konum_plus/provenance/f3_step2_r3_dispatch_precondition_stop_report_<date>.md)

write order (binding): every §2 check and every §3 evaluation is READ-ONLY. After P-1 … P-4 pass:
  W-1  start-state inventory and quarantine, then custody writes:
       (a) write p_konum_plus/provenance/f3_step2_r3_start_state_inventory_<date>.md. It lists, with size,
           modification time and SHA256: every file and directory under p_konum_plus/ whose name contains
           "f3_step2" or "checkpoint", and every untracked or modified path that
           `git status --porcelain -uall -- p_konum_plus` reports. For a directory with many files: a manifest
           CSV (path, size, modification time, SHA256 per file) plus the manifest's own SHA256. Each entry is
           classified: frozen / r1 package / r2 package / sidecar / prompt or PI file / CI-01 object /
           file of an earlier attempt / unlisted. "File of an earlier attempt" means: written by a harness
           process of the r2 cycle and not one of R-01 … R-11 — the checkpoint directory, logs, partial
           outputs. Anything the executor cannot place is "unlisted"
       (b) move — never delete, never edit — every file of an earlier attempt into
           p_konum_plus/quarantine/f3_step2_r2_attempt_files_<date>/ ; this includes the directory
           p_konum_plus/calibration/.r2_checkpoint_2026-09-07 with everything in it. After the move, re-hash
           the moved tree and compare it with the manifest of (a). Objects already under
           p_konum_plus/quarantine/, the CI-01 objects among them, stay where they are. Unlisted objects are
           listed and left untouched. Reuse nothing
       (c) custody writes: missing sidecars (§2.2 A item 19 ; §2.2 B R-11) ; record-class imports (v6 X-15,
           extended by §2.4) ; byte-exact copies of D-1 and D-2 (if they were handed over), D-3 and D-4 into
           p_konum_plus/prompts/
  W-2  prepare the r3 harness and the r3 fixture generator and write the r3 fixture manifest — the manifest is
       written and hashed BEFORE any run. <date> in every r3 file name is the ISO date on which W-1 starts; it
       is fixed then and does not change if the cycle runs over several days
  W-3  compute the SHA256 of harness, generator and manifest and write the pre-execution custody record. It
       names the exact bytes that will be executed and contains: the results of P-1 … P-4 ; the seven values of
       D-2 as read ; S-R2-1 and T-R2-2 as read, with the hash of D-4 ; restart layer present / absent ; the
       statement that no W-4 process has yet been started under these three hashes
  W-4  the run: each attempt is one process (§8.1); after an interruption or a defect a new attempt starts from
       the beginning (§8.2); units computed by different processes are combined only under §8.3
  W-5  the remaining deliverables: register, correction report, sidecars (§9)
  A file prepared in W-2 is not executed before its hash is recorded in W-3. If the harness, the generator or
  the manifest changes after W-3 for any reason — a defect found in a run included — then, before anything
  runs again: the superseded bytes of the changed file(s) and the superseded W-3 record are copied into the
  quarantine folder of that attempt (§8.2; the record is renamed with the suffix _superseded_<n>), W-3 is
  repeated with a new record, and the report names every superseded record and file with its hash and gives
  every changed expectation column of the manifest with its value before and after.
```

---

# 4. Relation to prompt v6 — what stays and what is replaced

| v6 part | in the r3 cycle |
|---|---|
| header, revision-response tables, §16 | historical; not instructions |
| §0 Purpose | replaced by §0 here |
| §1 state block | replaced by §1 here; the firewall list of v6 §1 stands |
| §2.1 ; §2.2 ; surrogate rule ; repository-state rule | stand (restated in §2 here); §2.2 is extended by the r2 package |
| §2.3 | replaced by §2.3 and §2.4 here. Where v6 says "§2.3 item 24" read D-2, where it says "item 25" read D-3 |
| §3 (P-1 … P-4, write order, STOP report) | replaced by §3 here. The stage names W-1 … W-5 are kept; what each stage contains is what §3 here says |
| §4.1, §4.2 (definitions of S-1, S-2, T-1 … T-5) | stand as the definitions of the seven values ratified in D-2. No field is PENDING. They are not re-decided and not re-interpreted |
| §4.3 (PI-ratified content; verbatim rule; PI_RATIFIED tags) | stands; the file is D-2. The two new fields of this cycle live in D-4 (§5 here) |
| §4.4 ; §4.5 | stand. Under the ratified combination every path is enabled; the only NOT_RUN by authorization that can occur in this cycle are the one §5 names for S-R2-1 = DEFERRED_THIS_CYCLE and T-SINGLE-PROCESS when units of the deliverables came from more than one process under T-R2-2 = AUTHORIZE_RESTART (T-RESTART-PROVENANCE then takes its place, Y-01) |
| §5 X-01 … X-20 | stand as the specification of the corrections. §6 here says which of them the r2 package did not deliver and what must change. X-02, X-07 and X-09 are AMENDED by Y-04, Y-02 and Y-03; X-05 is TIGHTENED by Y-21 |
| test contracts of v6 §5 | stand, except: T-EXC-CAPTURE and fixture INJ-EXC-CAPTURE are REPLACED by the tests and fixtures of Y-04 and §7, and every mention of them in v6 (§4.5, §7, §11.2, §14) reads so ; the first half of T-FINITE-DP04 is REPLACED (Y-03 (iv)), and the v6 §14 row "excluded at U-construction in D-P04 (INJ-NAN-STAT)" takes its evidence from UT-USET-CONSTRUCTION ; the second half of UT-PROBE-DECOUPLE depends on S-R2-1 (§5) ; the tag expected by T-P03-STATUS-A is the one Y-19 names ; T-ACF-RESIDUAL runs on the RUN1 series of Y-21 |
| §6 architecture | stands |
| §7 fixture manifest | stands, with the changes of §7 here |
| §8 rerun scope, NR gates, determinism | stands in full — the rerun is never reduced — and is tightened by §8 here; where units of the deliverables came from more than one process, the determinism wording is the one of §8.3 |
| §9 prohibitions | stand |
| §10 exactness-finding protocol | stands. EXACT-01 and EXACT-02 are taken; EXACT-03 is reserved by §5; the next free number is EXACT-04 |
| §11 register | stands; the r3 register is a child of the r2 register (R-09) |
| §12 deliverables | replaced by §9 here. The content list of v6 §12 item 10 remains the specification of the correction report |
| §13 roles ; end-state computation | stand, with `F3_STEP2_r3_status` in place of `F3_STEP2_r2_status` and the additions of §10 here |
| §14 end-state fields and response table | stand, with the additions of §10 here. The v6 rows on §2 custody, §3 preconditions, the write order and "r1 files byte-unchanged" are replaced by the rows of §10 here; deliverables 11 and 12 are added to the hash line block |
| §15 independent audit after return | stands, with the additions of §11 here |

---

# 5. PI fields of this cycle (nothing is selected by this draft)

The seven values S-1 … T-5 are closed in D-2 and carried unchanged. Two fields are new. They are filled by the PI
in the dispatch record D-4, not by the executor and not by this draft.

```text
S-R2-1  MANDATORY — the C4b statistic of a trajectory for which both probes of a fitter succeed but that fitter
        has no full-data reference (the state that v6 X-04 made representable; audit finding R2A-02 (b))
        the state  for a fitter f (P-01, P-02 or the spline) and a trajectory i: both probe-success flags of f
                   are true and f has no eligible / valid full-data fit at i. It is read from the procedural
                   flags — in the decision-layer grammar `pL`, `pR` and `full` — on the real path and in the
                   fixtures alike, never from the presence or absence of an RMSE_edge value
        gap        frozen r4 §3-C4b / §9.2 define V4 and U4 by probe success; content §2.4 says the "existing
                   full-data reference eligibility requirements for C4b pairing remain unchanged"; freeze
                   record §3 item 4.2 has, under the heading "Mathematics (provenance only; NOT a floor)", that
                   every consulted common-valid set is the intersection of the two candidates' P03 valid sets;
                   freeze record §4 (K-05, headed "informational; scientific_change = false") has U4_s ⊆ V4_s.
                   The r2 harness leaves such a trajectory out of V4 but keeps it in U4, and D-P04 then
                   resolves level 4b on NaN. Why a decision is needed (§6.1): read on its own, r4 keeps such a
                   trajectory in V4_s by its probe success, and its C4b statistic is then undefined; content
                   §2.4 keeps full-data reference requirements for C4b pairing. The frozen text does not say
                   which governs this state
        allowed    ALREADY_BINDING   the PI regards the texts above as already binding for this state: the
                                     trajectory is absent from every V4_s whose definition names that fitter
                                     (the spline is named in both families' V4_s) and hence from U4_s;
                                     denominators retained. Implemented as an X correction (Y-02, Y-03); the
                                     register cites D-4 (path and hash) as the basis
                   PI_RULE           the PI writes the rule, verbatim, in D-4; implemented verbatim, tagged
                                     PI_RATIFIED with the hash of D-4. On any ambiguity: record
                                     F3-STEP2-EXACT-03 and wire the state as under DEFERRED_THIS_CYCLE
                   DEFERRED_THIS_CYCLE   nothing is decided: wherever the state occurs, P03 C4b of the family
                                     concerned (of both families if the fitter is the spline) returns
                                     STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-03) for that sex; dependent outcomes
                                     follow v6 X-08. This holds wherever the state occurs, also where the
                                     trajectory fails another V4 condition. No numeric outcome is ever
                                     produced on an absent value. EXACT-03 stays in open_findings and
                                     S-R2-1 in deferred_decisions (v6 §13). The second half of
                                     UT-PROBE-DECOUPLE (v6 X-04: "probe absent from the C4b paired set") is
                                     then NOT_RUN(S-R2-1 DEFERRED); its first half runs. Under PI_RULE that
                                     second half follows the rule text
T-R2-2  OPTIONAL — restart mechanism for the run (audit finding R2A-01)
        NOT_AUTHORIZED      (a blank means the same; not PENDING) the r3 harness contains no restart,
                   checkpoint or caching layer of any kind; each W-4 attempt is one process that starts from
                   the beginning (§8.1, §8.2)
        AUTHORIZE_RESTART   a restart layer is PERMITTED, not required: the run is first attempted as one
                   process without it, and the layer is introduced only after an interruption, under the
                   conditions of §8.3. The value permits a narrower evidence contract (v6 §8 asks for
                   same-process determinism); like T-2b / T-4b in v6 §13 it is listed in narrowed_evidence by
                   value, whether or not a restart layer comes to be used; the report says which (§10)
        The dispatch-record template v2 carries AUTHORIZE_RESTART, entered at the PI's instruction of
        2026-09-21; the executor applies the value that stands in D-4
```

---

# 6. Corrections of this cycle — finding → correction → verification test → evidence (binding)

Every test: deterministic, tolerance-free, RNG-free; every result is an executor claim. Frozen engine functions
are REUSED for every predicate, never re-typed. Line numbers are those of the r2 harness (R-01) and are pointers,
not limits: correct the behaviour wherever it occurs. No verification test aborts the run process: a failed test
or a failed expectation is recorded and the run continues (§8.2).

```text
Y-01  R2A-01 (global blocker)  clean execution; no undisclosed restart layer
      defect       the r2 harness contains a pickle-based "restart checkpointing" layer (lines 70–106; used at
                   420, 562–573, 685–704, 1614–1625, 1632, 1641–1655, 1692–1715) that report and register do
                   not mention; its keys are bound neither to the harness / generator / engine bytes nor to
                   the input vector; the delivered files were assembled from objects computed by earlier
                   processes, at least one of them by a different byte-version of the harness; the process
                   that wrote the deliverables recorded 60 optimizer calls while RUN1 alone reports 4,380
                   executed spline modes
      correction   (a) the r2 layer is not carried over as it is. Under NOT_AUTHORIZED the r3 harness has no code
                   path that reads a previously written intermediate result. Under AUTHORIZE_RESTART such a
                   path may exist only as §8.3 specifies, and only after an interruption (§8.2); the code of
                   the r2 layer (lines 70–106) may be its starting point, changed as little as §8.3 requires;
                   nothing the r2 layer stored is ever read (W-1 (b) quarantines it)
                   (b) every W-4 process records pid, start and end time, command line, interpreter path, and
                   the three W-3 hashes it re-computed from the files it actually loaded
                   (c) every object of deliverables 5–8 — exception captures, telemetry rows, unit-test
                   records, residual series — carries or is covered by the pid and start time of the process
                   that computed it
                   (d) the report discloses the attempt history of the r2 cycle (§9 item 13) and every process
                   of this cycle (§9 item 12)
      test         T-SINGLE-PROCESS — when one process computed every object of deliverables 5–8: all of them
                   carry or are covered by the same pid and process start time, and the W-3 hashes equal the
                   hashes that process computed at start; T-RESTART-PROVENANCE is then NOT APPLICABLE(one
                   process). When units came from more than one process (only under AUTHORIZE_RESTART)
                   T-SINGLE-PROCESS is NOT_RUN(units from <k> processes) and T-RESTART-PROVENANCE takes its place:
                     (1) for every unit read from the store, the identity stored with it (§8.3 keys) equals the
                         identity the reading process computed for that unit
                     (2) no RUN2 unit was read from a unit computed for RUN1, and no test read a unit computed
                         for another test (checked from run label and test id)
                     (3) every process that computed a unit of deliverables 5–8 is in the attempt log and ran
                         under the final W-3 hashes
                   T-CALLCOUNT: the recording wrapper of T-4a keeps one counter per phase (NR-SPL, unit tests,
                   RUN1, RUN2, residual-series export) and per process; a unit read from the store brings its
                   counters and telemetry rows, tagged with the pid that computed them. Reported per phase: the
                   total over every contributing process and its split by process. For RUN1 the number of
                   per-call spline telemetry rows equals the RUN1 total; the RUN2 total equals the RUN1 total;
                   the residual-series export total is 0 (Y-21)
      evidence     results JSON `process` block; pre-execution custody record; attempt log; report

Y-02  R2A-02  PIN-U-SETS — common-valid supports (amends v6 X-07)
      defect       run_dp04 (lines 1075–1104) builds the consulted sets from finite-ness alone and ignores the
                   frozen valid-set membership; the retained fixture INJ-DP04-C2-DIVERGE therefore resolves for
                   P-02 on |U2| = 10 where its manifest predeclares P-01 on |U2| = 8; no assertion noticed
      correction   (a) membership first, finiteness second. An observation belongs to U2, U3 or U5 if and only
                   if it meets the frozen valid-set rule of that criterion for every fitter the frozen
                   definition names (v6 X-07 quotes r4 §9.2) AND each of those statistics is finite. U4: as v6
                   X-07 has it, from the ratified probe-success conjunction, with an observation excluded at
                   construction if the C4b statistic of any fitter the U4 definition names is non-finite; the
                   trajectory without a full-data reference per S-R2-1 (§5). Membership is procedural (freeze
                   record §6, DISC-F3-03: a result is invalid "only through the frozen failure taxonomy" and
                   "never through the magnitude of a finite statistic")
                   (b) expose the construction of each U_j as a pure function of the decision-layer records,
                   so that it can be tested directly (§7, UT-USET-CONSTRUCTION)
                   (c) EVERY fixture — new and retained — carries machine-readable expectations in the manifest
                   (§7), and the harness checks them after evaluation. A fixture whose outcome differs from
                   its expectation is reported EXPECTATION_FAIL, never re-described
      test         T-EXPECT-ALL: checks run == checks declared AND EXPECTATION_FAIL = none
                   T-U2-MEMBERSHIP: INJ-DP04-C2-DIVERGE shows RESOLVED at C2 for P-01 on |U2| = 8 (share 0.8)
                   T-U-FLAG-VS-FINITE: INJ-U-CCFALSE-FINITE (§7)
                   the five test contracts of v6 X-07, with the constructions of §7
      evidence     register PIN-U-SETS; per-level disclosure blocks with the membership lists

Y-03  R2A-03  PIN-UNDEFINED-FLAGS — finite validity in P03, guard in D-P04 (amends v6 X-09)
      defect       (a) a NaN C4b statistic fails P03 through a numeric comparison with `undefined = False`
                   and can produce a RESOLVED level; (b) CONTRACT_VIOLATION_INCONSISTENT_U is emitted from the
                   test flag alone (lines 1107–1110), not from the data; (c) the P03 valid sets drop an
                   observation whose statistic is invalid (lines 854–860), so that INJ-NAN-STAT passes C2 with
                   `undefined = False` although T-FINITE-P03 and the fixture's own predeclared description
                   require "undefined = True and C2 not passed"; the register reports PASS; no exactness
                   finding was recorded
      rule         v6 X-09 stands: "an invalid statistic is undefined (flag True) and follows §8.1 governance in
                   P03"; T-FINITE-P03 stands. The route is the one the v5 §4 pins give (v6 §6: "v5 §4 pins
                   unchanged"); quoted from the PIN prompt v5, lines 343–344, 350, 377–379, 401, 407, 411–412:
                     "an undefined statistic is represented by an explicit validity flag (`valid = False`) — a
                      NaN is never treated as a valid value"
                     "V2_s = { i : family cc AND spline cc }"
                     "removed from V3_s and U3_s, denominator n_s retained (CL-F3-04); §8.1 at sex level only"
                     "V3_s = { i : family eligible full-data fit AND spline valid full-data fit AND phi defined
                      for both }"
                     "V4_s = { i : family LEFT and RIGHT successful AND spline LEFT and RIGHT successful }"
                     "valid set = crossfit-complete trajectories of the family"
                     "§8.1: an undefined REQUIRED sex-level statistic ⇒ that criterion not passed"
      correction   (i) P03, criteria C2, C4b, C5: membership of the valid set is decided by the frozen
                   membership rule alone (flags; for C4b also S-R2-1). If the required statistic of ANY member —
                   the family's or, for a spline-relative criterion, the spline's — is invalid (None or
                   non-finite), the sex-level statistic is undefined: `undefined = True`, `passed = False`, the
                   offending (fitter, observation) pairs are recorded, and neither a median nor a comparison
                   is evaluated. For C4b the member statistic is r_i = max(RMSE_edge_LEFT_i, RMSE_edge_RIGHT_i);
                   it is invalid if EITHER side is invalid, so both sides are validated before they are combined
                   (Python's built-in max returns its first argument when the second is NaN; the r2 harness
                   combines with it, lines 929–935, 1041, 1096). C3: as CL-F3-04 binds it — the observation
                   leaves V3_s and U3_s, n_s is retained, §8.1 at sex level only. C1, C4a, C6: unchanged.
                   Sources: §6.1 — for C2, C4b and C5 a direct application of frozen r4 §2 and §3
                   (ii) D-P04: exclusion at construction per Y-02 (a). After a consulted set has been built and
                   immediately before the scalars are computed, re-validate the required statistics of every
                   member FROM THE DATA; any invalid one ⇒ CONTRACT_VIOLATION_INCONSISTENT_U. A test may
                   inject the invalid value after construction; it may not inject the STOP. The hook that
                   lets a test do so is a TEST_ONLY branch and is disclosed as Y-19 says
                   (iii) comparator: a level outcome is computed only from two valid scalars; otherwise
                   CONTRACT_VIOLATION_INCONSISTENT_U. No RESOLVED and no EQUIVALENT is ever produced on NaN
                   (iv) prompt-origin defect, recorded in audit DRAFT r5 §1.4: v6 asks for the P03 outcome
                   above (T-FINITE-P03) and, in T-U2-RHO-INVALID-EXCLUDE, T-U5-SST-INVALID-EXCLUDE,
                   T-U5-INDEPENDENT-OF-C2 and T-FINITE-DP04, for an exclusion at a consulted D-P04 level, i.e.
                   with P03 passed, without saying how such an invalid statistic is produced. With the r2
                   constructions (None or NaN at a crossfit-complete observation of P-01) no P03 rule that
                   treats an absent and a non-finite value alike — as X-09's `valid()` does — meets both. §7
                   fixes the constructions for this cycle. The first half of T-FINITE-DP04 ("the same NaN at a
                   consulted level") is REPLACED: under rule (i) that NaN never passes the P03 gate; the
                   exclusion of a NaN at construction is shown at function level by UT-USET-CONSTRUCTION
      test         T-FINITE-P03 (INJ-NAN-STAT, unchanged construction): P-01 C2 `undefined = True`,
                   `passed = False` in both sexes; P-01 p03 = FAIL; mechanism = ONLY_P02_PASSES; D-P04 not
                   entered
                   T-FINITE-P03-C4B, T-FINITE-P03-C5, T-FINITE-P03-SPL: the same for a NaN C4b edge statistic
                   (RIGHT side), a NaN C5 statistic and a NaN spline rho at a member (§7)
                   T-U-POST-CONSTRUCTION-INVALID: the STOP fires from the data-driven check of (ii)
                   T-COMPARATOR-NAN: function-level — a level evaluation handed a NaN scalar returns
                   CONTRACT_VIOLATION_INCONSISTENT_U
      evidence     register PIN-UNDEFINED-FLAGS; fixtures and unit tests of §7

Y-04  R2A-04  PIN-SOLVER-B-UNVERIFIABLE (S-2 = α) — the ratified boundaries (amends v6 X-02)
      defect       the effect of α is implemented correctly, the boundaries of content §3.1 / §3.3 are not:
                   a broad `except RuntimeError` around solver_config (lines 696–702) records nothing and
                   invalidates the mode; the accept wrapper (lines 355–369) catches by class only; the test
                   injection fired inside SCEN-A, in RUN1 only, was not in the manifest, and its stage assertion
                   was relaxed to `stage in (1, 2)` (line 1680); the wrappers are never restored; no test
                   covers stage 2 by design or an unrelated exception
      correction   implement content §3 as written; register rows that quote it are tagged VERBATIM and quote
                   it exactly (Y-10). Content §3.1: "The covered event is a `RuntimeError` raised by the
                   `nnls(A[act].T, g)` invocation in frozen `kkt_res(c, z, O, A)` while that invocation is
                   being used by `accept(c, z, O, A)` to compute the KKT-existence certificate for a SOLVER-B
                   stage-1 or stage-2 acceptance check." This prompt adds no condition on the exception class
                   (DRAFT v1 had added one; withdrawn). What follows is this prompt's implementation and test
                   specification — engineering, not ratified text; register rows that state it are tagged
                   SUMMARY and point to content §3:
                   (a) call site and stage are established from the call stack / traceback frames, not from the
                   class or the message alone: the exception comes from the `nnls` call inside the loaded
                   `kkt_res` while `kkt_res` serves `accept`. The stage is the ordinal of the `accept` call
                   within one SOLVER-B `solver_config` call (frozen source: first call stage 1, second call
                   stage 2)
                   (b) any other exception inside the spline solver is NOT converted into "not accepted" and
                   NOT into "mode invalid". A catch at mode level is permitted for two purposes only: to write
                   a capture record with kind = UNRELATED (same fields), and to route the event to the existing
                   protocol (v6 §10): F3-STEP2-EXACT-nn, the spline fit of that context returns
                   STOP_EXACTNESS_PENDING(<id>), dependent statistics PENDING, every unaffected context
                   continues. Every capture record of a manifest-declared injection is tagged TEST_ONLY. An
                   UNRELATED exception produced by such an injection stops its path as
                   STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED) and is NOT entered into the exactness findings
                   or open_findings; a natural UNRELATED event is entered
                   (c) the test injections are manifest-declared fixtures of their own (§7), never placed
                   inside SCEN-A or SCEN-B, identical in RUN1 and RUN2. The mode on which an injection lands
                   cannot be predeclared: frozen `accept` returns before `kkt_res` when the feasibility check
                   fails, and `kkt_res` skips `nnls` for an empty active set. Predeclared instead is the ARMING
                   RULE: the context (fixture, sex, trajectory, mask) and "the first `nnls` call that is
                   reached inside `kkt_res` while it serves the stage-k `accept`, modes in enumeration order".
                   The landing mode is recorded and must be the same in RUN1 and RUN2. An injection that is
                   never reached is INJECTION_NOT_REACHED = FAIL
                   (d) every runtime wrapper is installed for its declared scope and restored afterwards; the
                   restoration is asserted (the namespace objects are the originals again)
      test         (counts refer to TEST_ONLY-tagged records; a natural covered event in the same context is
                   recorded besides them and fails no test)
                   T-EXC-CAPTURE-S1: a stage-1 injection ⇒ exactly one record, stage = 1, kind = COVERED; the
                   chain of that mode enters stage 2
                   T-EXC-CAPTURE-S2: a stage-1 and a stage-2 injection, each firing once at the first call it
                   can reach ⇒ one record with stage = 1 and one with stage = 2 (the landing modes are recorded
                   and may coincide); after the stage-2 record the chain of that mode enters stage 3
                   T-EXC-UNRELATED: (1) unit tests on a TEST_CONSTANT case, calling the loaded `reference`
                   function, never inside NR-SPL: (1a) a RuntimeError raised by the `nnls` call inside
                   `reference` itself — neither `kkt_res` nor `accept` is on the call stack; (1b) a
                   RuntimeError raised by the `nnls` call inside `kkt_res` while `reference` calls it —
                   `kkt_res` is on the stack, `accept` is not. Both ⇒ the classifier of (a) says UNRELATED, the
                   exception is not converted and reaches the test.
                   (2) fit context — a ValueError raised at the covered site at stage 1 ⇒ kind = UNRELATED, not
                   converted; that context STOPs as in (b); the other contexts continue.
                   (The frozen `polish` calls no `nnls` — it uses numpy.linalg.lstsq — so the example of
                   content §3.1 cannot be built as a test; nothing is reopened by saying so)
                   T-WRAPPER-RESTORE: assertion of (d)
                   RUN1 and RUN2 contain the capture records identically
      evidence     telemetry rows; `solver_exceptions` block; register PIN-EXC-CAPTURE and
                   PIN-SOLVER-B-UNVERIFIABLE

Y-05  R2A-05  PIN-A5-SUPPORT (S-1 = (a)) — tests and violation handling
      defect       predicate and wiring conform to content §2; T-A5-SUPPORT is absent; none of the test
                   obligations of content §9 was executed; the TRUE branch of condition (i) was never
                   exercised; on an invalid reference the code raises a bare ValueError that aborts the run,
                   where content §2.3 says: "Record the context and stop the affected evaluation path"
      correction   T-A5-SUPPORT on TEST_CONSTANT vectors, asserting at least: threshold equality is included
                   and the next float below is excluded; disconnected components are united; support partly
                   observed versus fully masked, for both edges; a finite constant reference gives S = G and
                   condition (i) false for both masks; missing, non-finite and wrong-length references are
                   contract violations. A violation writes a record CONTRACT_VIOLATION_A5_REFERENCE with
                   fixture, sex, trajectory and reason; the C4a / C4b determination that needs that support
                   returns that STOP record — it is not turned into a C4 pass or fail (content §2.3); in the
                   family status rule of v6 X-08 such a criterion counts as PENDING — and everything that does
                   not depend on it continues. One real-path fixture exercises the TRUE
                   branch (§7, FIX-A5-TRUE)
      evidence     test-evidence JSON; register PIN-A5-SUPPORT

Y-06  R2A-06  fixture fidelity — v6 X-10 as specified
      defect       the fidelity counters are constants (lines 1771–1773); the execution-site evidence dict
                   returned by run_one_start is discarded; SCEN-B's five declared injection sites have no
                   executed-key evidence; T-FIDELITY does not exist
      correction   implement v6 X-10 as written: executed_construction_key from execution-site evidence only;
                   construction_audit per fixture; counts <implemented>/<declared> ; <executed>/<declared>;
                   a mismatch ⇒ FIDELITY_FAIL
      test         T-FIDELITY

Y-07  R2A-07  telemetry, reporting fields, canonical document — v6 X-11 and T-4a as specified
      defect       4,382 spline telemetry rows carry nit = nfev = njev = -1 and wall time 0.0; the per-call
                   records are collected (line 385) and only counted (line 1790); FIX-STARTS-* write no
                   telemetry; the canonical document is the r1-shaped one; the §6 fields other than the
                   DISC-F3-03 complements and the per-side medians are missing; `sexes` is {}; T-SCHEMA absent
      correction   implement v6 X-11 (a) … (f) and content §7 as written: one telemetry row per trust-constr
                   and per SLSQP call with its fit / mode / stage context; a metric that cannot be obtained is
                   written as the string UNAVAILABLE with a reason, never as a number; FIX-STARTS-* write their
                   rows; the canonical document is enlarged as X-11 (d) says; the §6 fields exist; T-CANON and
                   T-SCHEMA run
      test         T-CANON ; T-SCHEMA ; T-CALLCOUNT (Y-01)

Y-08  R2A-08  end-state fields — computed, not declared
      correction   the harness computes the test-based inputs of the six fields of v6 §13 from the results of
                   this run (which tests ran, which passed, which expectations held, which coverage rows are
                   evidenced). The executor finalizes the six fields in the report, adding the document checks
                   of Y-09 … Y-19, each of which has a named check in the response table (§10). A correction
                   counts as complete only if its test or check RAN and PASSED

Y-21  AUD-07 / v6 X-05 (added in DRAFT v2)  the residual series are RUN1's own
      defect       v6 X-05 applies PIN-ACF clause (a) to "every full-data residual series r = z − ĝ produced in
                   RUN1". The r2 harness exports something else: under the comment "recompute on real
                   scenarios" (R-01 line 1686) it re-fits every real scenario in a separate pass — mask ids
                   `<sex><trajectory>:full:acfexport`, cached under `acfexport_<fixture>`, with a throwaway
                   telemetry list and without the declared injections (lines 1691–1716) — and exports the
                   residuals of those re-fits. The export therefore contains a series RUN1 did not produce
                   (SCEN-B M0 SPL, whose RUN1 spline fit is an injected failure), and in the auditor's clean run
                   of the r2 bytes the optimizer counter rose from 10,548 after RUN2 to 11,139 after the export
                   (audit DRAFT r1 §4 R2A-01 and §7.4; auditor tier). DRAFT v1 of this prompt carried X-05 over
                   as closed, following the closure-map row AUD-07 of audit DRAFT r1, although §7.4 of that
                   record notes the separate re-fit pass; that row is not relied on
      correction   (a) the series are taken from the RUN1 fit objects themselves: for every (fitter, fixture,
                   sex, trajectory) at which RUN1 computes phi_i from a completed full-data fit (family:
                   eligible; spline: valid), whether or not phi_i is finite and whether or not i enters V3_s,
                   RUN1 records r = z − ĝ from the ĝ that this computation uses. A fit that did not complete
                   has no ĝ and no series. Decision-layer fixtures, and real-fit contexts without a C3
                   computation (FIX-STARTS-*, FIX-A5-TRUE, the injection contexts), have none: v6 X-05 covers
                   the residual series produced in RUN1, and none is formed there — as in r2, whose export
                   covered SCEN-A and SCEN-B only. No fit of any fitter is run for the export
                   (b) with each series RUN1 records the fit identity (fitter, fixture, sex, trajectory, mask
                   id of the RUN1 fit, pid) and the SHA256 of the float64 little-endian bytes of the exact
                   array passed to the C3 computation. RUN1 writes these link records into the test-evidence
                   JSON (deliverable 8), block `residual_link` — outside the canonical document, as v6 X-05
                   keeps the test layer outside it; deliverable 7 carries the same keys
                   (c) under §8.3 a RUN1 unit read from the store brings its series with it; a series is never
                   re-created by a new fit
      test         T-ACF-RESIDUAL (v6, unchanged) on the exported series, and T-RESIDUAL-LINK: (1) every
                   exported series hashes to the value in `residual_link`; (2) the exported keys equal the keys
                   of (a) — none more and none fewer; (3) no fit of any fitter runs in the export phase: the
                   entry counts of the family fit driver and of the spline fit driver for that phase are 0,
                   and so is the export total of T-CALLCOUNT
      evidence     deliverable 7 ; `acf_verification` block ; `residual_link` block of deliverable 8
```

Cleanup items (each is a correction of this cycle; "as specified" means as v6 already specifies it). Each is
checked by the executor against the delivered file and reported as a row of the response table.

```text
Y-09  R2A-09   report wording: P-4 is evidenced by the PI dispatch record D-4 (§3)
Y-10  R2A-10   register rows tagged "PI_RATIFIED, VERBATIM" quote the ratified text exactly; anything else is
               tagged SUMMARY and points to the section of D-2. No binding clause is left out of a VERBATIM row
Y-11  R2A-11   the coverage row on the K-05 invariant reads as T-3 authorizes (content §6), in the coverage
               matrix as well as in the register
Y-12  R2A-12   v6 X-18 (required in this cycle): the opened-file list is recorded unfiltered — absolute and
               relative paths, normalized — and split into: declared inputs ; the three W-3 files and the W-3
               record ; interpreter, standard-library and site-packages files ; anything else. "Anything else"
               must be empty or explained
Y-13  R2A-13   v6 X-01: one hash entry per executed node under a unique key (the r2 file has 67 entries for
               73 executed nodes, because 5 Import and 3 ImportFrom nodes collapse onto two keys); the
               I/O-free assertion covers ALL executed nodes; the register has the row PIN-EXC-CAPTURE
               (v6 §11.1)
Y-14  R2A-14   v6 X-12 in full: spline zero-variance predicate stated exactly; constant table split;
               "byte-identical source segments" statement
Y-15  R2A-15   v6 X-19: T-MASK-FULL-EXT runs (stride test on the two F2 benign targets)
Y-16  R2A-16   coverage matrix: every row's status is derived from what ran and passed in this run. One
               vocabulary: `covered` (evidence of the class the row names) ; `covered_injection_only`
               (decision-layer injection only; no reachability claim) ; `UNCOVERED(<reason>)`. Only UNCOVERED
               rows enter uncovered_coverage_rows. A row names only fixtures that exercise it; a row that only
               the FALSE branch or only a unit test exercises says so. Two rows need real work or an honest
               UNCOVERED: "A.5 (iii) inadmissible refit" — UT-A5-III must exercise clause (iii) itself, a refit
               that completes numerically and is inadmissible under the frozen taxonomy, which r2's test does
               not; and "F2 failure codes reachable through wrapper" — only evidence that went through the
               wrapper counts, not the engine's own suite replayed by NR-01 (i). If no construction is
               possible without touching frozen code, the row is UNCOVERED with that reason. The r2 check of
               "unconsulted levels not recomputed" (lines 1732–1736) reads the D-P04 block of INJ-DP04-C1
               and must not assume that D-P04 ran (§7, S-R2-1 = DEFERRED); the row then takes its evidence
               from a fixture that does reach D-P04, for example INJ-DP04-C2-DIVERGE
Y-17  R2A-17   v6 X-14: the early return in the consulted-level code (r2 lines 1144–1148: it returns
               STOP_CONTRACT_VIOLATION_EMPTY_U without a `stops` record) is removed, or made consistent with the
               two STOP returns before it (lines 1118–1133), which write one. The requirement concerns returns
               whose mechanism outcome is a STOP; a return with any other outcome (RESOLVED, EQUIVALENT,
               terminal fallback) writes no `stops` record
Y-18  R2A-18   the report is complete as v6 §12 item 10 and §14 require: custody table with OBSERVED hashes
               (item 13 included), precondition results, per-finding table, NR results, coverage matrix,
               fidelity counts, findings, determinism hashes, environment, opened-file list, end state, the
               response table. Nothing is delegated to "the dispatch-turn conversation record"
Y-19  R2A-23   TEST_ONLY branches inside the production evaluator — `force_c4_pending` and the
               post-construction hook of Y-03 (ii) — are disclosed in the register, or moved out of the
               evaluator. The mechanism tag that `force_c4_pending` produces is
               MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING); v6's T-P03-STATUS-A names
               F3-STEP2-EXACT-01, which S-1 has closed; the manifest expectation carries the TEST_ONLY tag
Y-20  OBS-2    optional: record the SHA256 of the `mixed_trig` test vector (146 float64, little-endian) next to
               its ACF deviation value, so that the value is comparable across environments
```

Carried over unchanged. Corrections of v6 that the audit found closed in r2 (audit DRAFT r1 §5) are carried into
the r3 harness as they are and re-verified by their v6 tests in the r3 run: X-03, X-06, X-08, X-13, X-16
(labels, subject to Y-16), X-17, the probe-success half of X-04 (its C4b-pairing half follows S-R2-1), and the
parts of X-01 and X-02 that Y-13 and Y-04 do not change. Do not re-design them. X-05 is not among them: Y-21.

## 6.1 Source map for Y-03 (i) — an invalid statistic at a member of a P03 valid set

"Invalid" means None or non-finite (v6 X-09: valid(value) ⇔ value is not None ∧ math.isfinite(value)). Frozen r4
states the governing rule once, for every P03 criterion, and each criterion defines its valid set by flags and its
sex-level statistic as a median over that set:

```text
r4 §2, lines 73–78   "§8.1 propagation (binding in P03):" a statistic required by a P03 criterion that is
                     undefined for a family "means that family cannot pass that criterion"; "No imputation, no
                     sentinel, anywhere."
r4 §3, lines 90, 92  "sex-level aggregation = `numpy.median`" ; "undefined-statistic behavior per D-P03-7 §8.1"
r4 §9, lines 484–486 "an undefined required quantity means the family did not pass P03 (§8.1)"
v5 §4, lines 343–344 "an undefined statistic is represented by an explicit validity flag (`valid = False`) — a
                     NaN is never treated as a valid value"
v5 §4, lines 411–412 "§8.1: an undefined REQUIRED sex-level statistic ⇒ that criterion not passed"
```

| criterion | valid set (membership by flags) | sex-level statistic | an invalid statistic at a member | binding sources | class |
|---|---|---|---|---|---|
| C2 | V2_s = {i : family crossfit-complete AND spline crossfit-complete} | M_F,s = numpy.median over V2_s of rho_cv,i ; M_S,s the same for the spline on the same V2_s | the sex-level median over V2_s is undefined (NaN for a non-finite value; not computable for an absent one), so C2 is not passed; an invalid spline value makes M_S,s undefined, which both families' pass rule needs, so C2 is not passed for both | r4 §2 ; r4 §3 ; r4 §3-C2 (lines 123–124, 131–132, 137–140) ; r4 §9 ; v5 lines 343–344, 350, 353, 411–412 ; v6 X-09 with T-FINITE-P03 | direct application |
| C4b, full-data reference present | V4_s = {i : family LEFT and RIGHT probes both successful AND spline LEFT and RIGHT probes both successful} | C4b_F,s = numpy.median over V4_s of r_i^F with r_i = max(RMSE_edge_LEFT_i, RMSE_edge_RIGHT_i) ; C4b_S,s on the same V4_s | r_i is undefined if either side is; then as for C2 — C4b not passed, for both families if the value is the spline's | r4 §2 ; r4 §3 ; r4 §3-C4b (lines 265, 273–274, 278–282) ; r4 §9 ; v5 lines 343–344, 400–402, 411–412 ; v6 X-09 | direct application |
| C4b, both probes of a fitter successful, no full-data reference | read on its own, r4 keeps the trajectory in V4_s by probe success, and its RMSE_edge (defined against the full-data reference, r4 line 254) is undefined; content §2.4 keeps full-data reference requirements for C4b pairing | as above | not determined by the frozen text: the two readings differ | r4 §3-C4b ; content §2.4 ; freeze record §3 item 4.2 (provenance only) and §4 K-05 (informational) | PI field S-R2-1 (§5) |
| C5 | crossfit-complete trajectories of the family (absolute; no pairing) | median s_stab over that set (median pin: numpy.median) | the median is undefined, so C5 is not passed | r4 §2 ; r4 §3 ; r4 §3-C5 (lines 317–322) ; r4 §9 ; v5 lines 343–344, 406–408, 411–412 ; v6 X-09 | direct application |
| C3, for comparison | V3_s = {i : family eligible full-data fit AND spline valid full-data fit} | median of the absolute lag-1 ACF over V3_s | the trajectory leaves V3_s and U3_s; n_s is retained; §8.1 at sex level only | freeze record CL-F3-04 ; v5 lines 376–379 | binding exception, unchanged |

Notes. (1) That v6 tests only the C2 case (T-FINITE-P03) does not limit the rule: r4 §2 and §3 state it for every
P03 criterion. The C2 bullet "undefined behavior" (r4 lines 139–140) names only an empty V2_s and a share below
the floor; it is silent on an invalid member statistic (audit DRAFT r5 §1.2), which the general rule decides.
v6 X-09's sentence "an invalid statistic is undefined (flag True) and follows §8.1 governance in
P03" is general. DRAFT v1 (§12 item 1) called the extension to an absent value, to C4b, to C5 and to the spline's
statistic the drafter's composition; that description is withdrawn. (2) Removing an invalid member from the set
instead — what the r2 harness did — would change a set the frozen text defines by flags. The frozen text does this
for C3 alone (CL-F3-04); for any other criterion it would need a PI rule and is not part of this prompt. (3)
Consequence, disclosed: if an invalid statistic at a member ever occurred in a real execution, the family would
fail that criterion on that one value; audit r4 (AUD-24) calls a NaN rho at a crossfit-complete observation
"practically excluded, not structurally". (4) A state these sources do not determine, other than S-R2-1: record the
next free exactness finding (F3-STEP2-EXACT-04 onward, v6 §10); that criterion returns STOP_EXACTNESS_PENDING(<id>)
for the family and sex concerned, dependent outcomes follow v6 X-08, and all other work continues. Dispatch does not
settle such a state (§12 A).

---

# 7. Fixture manifest r3 — predeclared before any run (changes against v6 §7 and the r2 manifest)

Create `p_konum_plus/calibration/f3_step2_fixture_manifest_r3_<date>.csv` in W-2 (child of R-03, which stays
byte-unchanged). Columns: those of r2 plus the machine-readable expectation columns of Y-02 (c), at least
`expected_p03` (both families), `expected_mechanism_outcome`, `expected_resolved_level`, `expected_U_sizes`
(per consulted subset-defined level and sex), `expected_stops`, `expected_undefined` (criterion, family, sex). A
real-fit fixture whose outcome is "as computed" declares that, together with the structural expectations it does
have (start counts, FEATURE_START_REJECTED, capture records). Expectations are written as flags, counts, labels
and set sizes; no decimal literal of a median is asserted. `parent_fixture_id` of a retained or re-built fixture
is its r2 id; a re-built fixture gets a new `implemented_construction_key`.

Decision-layer grammar as in the r2 generator (lines 165–186): per fitter `full`, `cc`, `rho`, `phi`, `pL`, `pR`,
`rL`, `rR`, `sst`; n_s = 10 per sex; "equalized" means the r2 helper `_equalize` (P-02 := the P-01 baseline).

```text
retained           every r2 fixture id is retained, UT-PROBE-DECOUPLE included (it was missing from the r2
                   manifest). The decision-layer fixtures keep their constructions; their expectations are the
                   outcomes their r2 manifest rows state, written into the new columns without changing them —
                   EXCEPT the three re-built rows below and the rows named under "S-R2-1 and retained
                   fixtures". Where an r2 row is silent on a new column, the value is the one that follows
                   from the construction under Y-02 / Y-03: for the retained D-P04 fixtures every consulted
                   subset-defined level has |U| = 10, except INJ-DP04-C2-DIVERGE (|U2| = 8) and
                   INJ-DP04-EMPTY-U (forced empty); INJ-C3-PHI-UNDEF: the two observations leave V3
                   (CL-F3-04), the C3 floor fails at share 0.8, and the sex-level `undefined` flag is False
INJ-NAN-STAT       construction unchanged (P-01 rho = NaN at observation 0, the observation crossfit-complete,
                   both sexes; not equalized). Expectation: Y-03 T-FINITE-P03
INJ-U2-RHO-INVALID       RE-BUILT: the invalid C2 statistic is produced through the frozen valid-set rule — the
                   SPLINE is not crossfit-complete at observation 0 (its cc flag false, its rho absent), both
                   sexes; everything else valid; equalized. Expectation: P03 PASS + PASS (V2 share 0.9);
                   |U2| = 9, |U3| = |U4| = |U5| = 10 in both sexes; every level EQUIVALENT; no STOP;
                   TERMINAL_FALLBACK_MECHANISM_P01 (v6 T-U2-RHO-INVALID-EXCLUDE: "one fitter's required C2
                   statistic invalid for observation i, all other statistics valid, P03 entry conditions
                   satisfied")
INJ-U5-C2-INDEPENDENT    RE-BUILT: as the row above, at observation 3. Expectation: |U5| = 10 while |U2| = 9,
                   both sexes; the disclosure block of level C5 names its basis — C5-statistic validity of P-01
                   and P-02 — and lists the members; TERMINAL_FALLBACK_MECHANISM_P01
INJ-U5-SST-INVALID       RE-BUILT: P-01 is not crossfit-complete at observation 0 in F (cc flag false; rho and
                   sst absent there); equalized. Expectation: P03 PASS + PASS (shares 0.9); F: |U2| = 9,
                   |U5| = 9 with both medians on those same nine; M: |U2| = |U5| = 10; |U3| = |U4| = 10 in both
                   sexes; no STOP; TERMINAL_FALLBACK_MECHANISM_P01
INJ-U-POST-CONSTRUCTION-INVALID   contract unchanged; the injection alters a member's statistic AFTER the set is
                   built and BEFORE the data-driven check of Y-03 (ii); the STOP comes from that check
INJ-U-CCFALSE-FINITE     NEW: equalized; P-01 cc flag false at observation 0 in F while a finite rho and a
                   finite sst are left in place (a decision-layer state). Expectation: P03 PASS + PASS; the
                   observation is outside V2 and the C5 valid set of P-01 and outside U2 and U5 — F: |U2| =
                   |U5| = 9, M: 10; TERMINAL_FALLBACK_MECHANISM_P01. Membership decides, not finiteness
INJ-NAN-STAT-C4B   NEW: not equalized; P-01 rR = NaN at observation 0 with rL finite — the RIGHT side, where an
                   order-dependent max would drop the NaN (Y-03 (i)) — both sexes, both probes successful, the
                   reference present. Expectation: P-01 C4b `undefined = True`, `passed = False`; no comparison
                   evaluated; ONLY_P02_PASSES
INJ-NAN-STAT-C5    NEW: not equalized; P-01 sst = NaN at the crossfit-complete observation 0, both sexes.
                   Expectation: P-01 C5 undefined, not passed; ONLY_P02_PASSES
INJ-NAN-STAT-SPL   NEW: the SPLINE's rho = NaN at the crossfit-complete observation 0, both sexes. Expectation:
                   C2 undefined and not passed for BOTH families (the benchmark statistic is required by
                   both); STOP_BOTH_FAIL_REDESIGN
INJ-C4B-NOREF      NEW (the auditor's case T1 of audit DRAFT r1 §4): equalized; all probes successful; P-01 has
                   no full-data reference at observation 0 and P-02 none at observation 1 (there: `full` flag
                   false, phi and RMSE_edge absent), both sexes; the spline complete. Expectation per S-R2-1:
                   ALREADY_BINDING ⇒ P03 PASS + PASS (C1 0.9 ; V3 and V4 shares 0.9); observation 0 outside
                   V4 of P-01, observation 1 outside V4 of P-02, both outside U3 and U4: |U3| = |U4| = 8,
                   |U2| = |U5| = 10; every level EQUIVALENT; TERMINAL_FALLBACK_MECHANISM_P01; no NaN anywhere
                   PI_RULE ⇒ derived from the rule text in D-4 and predeclared before the run
                   DEFERRED_THIS_CYCLE ⇒ C4b = STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-03) for both families;
                   MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-03)
S-R2-1 and retained fixtures   three retained fixtures contain the S-R2-1 state. On the real path, SCEN-B:
                   its declared injection makes the spline's full-data fit fail at trajectory M0 while both
                   spline probes succeed — ALREADY_BINDING: M0 is absent from both families' V4 in M, V4 is
                   empty, C4b is undefined and not passed (as in r2); DEFERRED: C4b in M is PENDING for both
                   families, both still FAIL on their definite failures, the mechanism stays
                   STOP_BOTH_FAIL_REDESIGN, and the real-path evidence for "C4b fail" is PENDING.
                   In the decision layer, two fixtures (a `full` flag false while both probe flags are true,
                   with a finite RMSE_edge left in place):
                   INJ-C1-FAIL (P-01, observations 0–2, F) — ALREADY_BINDING: those observations are also
                   outside V4 of P-01 (C4b floor fails, in addition to C1 and the C3 floor); DEFERRED: P-01 C4b
                   is PENDING in F. In both cases P-01 p03 = FAIL with first failure C1 and the mechanism
                   stays ONLY_P02_PASSES
                   INJ-DP04-C1 (P-02, observation 9, both sexes) — ALREADY_BINDING: V3 and V4 shares of P-02
                   are 0.9, PASS + PASS, RESOLVED at C1 for P-01 as before; DEFERRED: P-02 C4b is PENDING ⇒
                   P-02 p03 = PENDING ⇒ MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-03), and the
                   coverage row "D-P04 resolve at C1" is UNCOVERED(S-R2-1 DEFERRED). PI_RULE: both derived
                   from the rule text and predeclared before the run
UT-USET-CONSTRUCTION     NEW, unit tests (evidence class unit_test) on the pure construction functions of
                   Y-02 (b), called directly. They are function-level evidence: they produce no fixture
                   outcome and no mechanism outcome, and they claim no reachability. Inputs are the
                   decision-layer counterexamples of audit r4 (AUD-18, AUD-24), which cannot pass the P03 gate
                   under Y-03 (i):
                   (a) all crossfit-complete, P-01 rho = None at observation 0 ⇒ |U2| = 9 and |U5| = 10
                   (b) P-01 sst = None at a crossfit-complete observation ⇒ |U5| = 9; both medians on the nine
                   (c) P-01 rho = NaN at a crossfit-complete observation ⇒ excluded from U2 at construction
                   (d) P-01 rR = NaN with rL finite and both probes successful ⇒ excluded from U4 at
                   construction
                   (e) P-01 cc flag false with a finite rho and sst in place ⇒ outside U2 and U5
INJ-EXC-CAPTURE-S1, INJ-EXC-CAPTURE-S2, INJ-EXC-UNRELATED-TYPE
                   NEW, replacing the single INJ-EXC-CAPTURE of v6 §7: each is a manifest row of its own with
                   its own real-fit spline context on a TEST_CONSTANT trajectory (not SCEN-A, not SCEN-B): a
                   full-data spline fit is enough, no folds and no probes; no P03 status is evaluated for
                   these contexts. `injection_sites` states the arming rule of Y-04 (c); active identically in
                   RUN1 and RUN2. SCEN-A and SCEN-B are injection-free apart from SCEN-B's declared failure
                   injections
UT-EXC-UNRELATED-REFERENCE     NEW, the two unit tests of Y-04 T-EXC-UNRELATED (1a) and (1b)
FIX-A5-TRUE        NEW: real-fit fixture on TEST_CONSTANT trajectories whose half-range support lies wholly
                   inside the LEFT mask {0..14} (one trajectory) and wholly inside the RIGHT mask {131..145}
                   (one trajectory). It needs the full-data fits and the two probes of P-01, P-02 and the
                   spline; no folds, and therefore C4a / C4b structural expectations only — no P03 status and
                   no mechanism outcome is evaluated for it. Expectation (content §2.2, §2.4): condition (i)
                   true for that side ⇒
                   the probe fails C4a (numerator excluded, denominator retained) and is absent from the C4b
                   paired-valid set, for P-01, P-02 and the spline; condition (i) recorded separately;
                   conditions (ii) / (iii) marked not evaluated where fitting was skipped
```

Everything else of v6 §7 stands: `interpretation = PATH_COVERAGE_ONLY`; no fixture derived from, resembling by
construction, or calibrated to any real F1 trajectory; RNG only in manifest-declared fixture generation with
recorded seeds; FIX-STARTS-FULL and FIX-STARTS-DUP; the C4 real rows; the NR rows.

---

# 8. Run rules (tighten v6 §8; the rerun scope of v6 §8 stands in full)

## 8.1 One process (the default, and the first attempt in every case)

```text
Every W-4 attempt is ONE operating-system process, started after the W-3 record exists; it spawns no child
process that computes. It executes NR-01 (i) first, then the other non-regression gates and the loader test,
the unit tests, the fixtures, RUN1 and RUN2, and it writes deliverables 5–8 (§9); the residual series it writes
are the ones RUN1 recorded (Y-21) — no fit is run for them. As in r2, every real-fit fixture whose objects enter
the canonical document is computed in RUN1 and again, from scratch, in RUN2; the manifest column `run_scope`
says for every fixture and test whether it runs once or in both.
It reads the declared inputs (§2), the three W-3 files and the W-3 record, and nothing else of this project
(under §8.3, also the restart store).
At start it records pid, start time, command line and interpreter, re-computes the W-3 hashes from the files it
loaded, and compares them with the W-3 record; a difference ⇒ it exits without computing anything.
Its last action is to write `process.end` into the results JSON and the log line RUN_COMPLETE <pid> — the end
marker. Thread pins, environment record and the determinism wording are those of v6 §8 (where units came from
more than one process: §8.3).
```

The time limit of a single tool call is NOT a reason to split the run. Start the process in the background — the
Bash tool's background execution, or on Windows for example PowerShell `Start-Process` with redirected output —
let it write a progress log, and poll that log from later tool calls until the end marker appears. For
orientation only, not a requirement: in the auditor's Linux environment one clean process of the r2 harness —
unit tests, FIX-STARTS-*, RUN1, RUN2 and the export, without the NR gates — took about 32 minutes; the r3 run is
longer (NR gates, FIX-A5-TRUE, three injection contexts).

## 8.2 Interrupted runs, failed tests, defects

```text
A failed verification test or expectation does not end the process: it is recorded and the run continues.
Only three things end the process early: the W-3 hash re-check, a non-regression gate that RUNS and FAILS
  (⇒ STOP, v6 §8), and a custody failure.
A harness defect (an unhandled Python exception) is a defect, not an interruption: quarantine what the
  process wrote, as below ; fix the defect, which changes the harness, so W-3 is repeated (§3) ; start a new
  attempt.
An INTERRUPTION is an end without end marker caused by the environment (session teardown, kill, power). Then:
  move every file the process wrote into p_konum_plus/quarantine/f3_step2_r3_attempt_<n>_<date>/ (never
  delete) ; append the attempt to the attempt log (§9 item 12): n, pid, start, end, the three W-3 hashes it
  ran under, how it ended, what was moved ; re-verify the three W-3 hashes ; start W-4 again FROM THE
  BEGINNING in a new process. Nothing a
  previous attempt computed is read by a later one (once a restart layer exists under AUTHORIZE_RESTART, the
  store is kept and §8.3 governs what a later process reads).
If the environment cannot keep one process alive to the end (the r2 harness names "environment/session
  teardown" as the reason for its checkpoint layer):
  under NOT_AUTHORIZED: do NOT add a restart layer. After the second interruption STOP, deliver the attempt
  log, and leave T-R2-2 to the PI;
  under AUTHORIZE_RESTART: after the first interruption the executor may introduce a restart layer (§8.3); if it
  does not, the rule for NOT_AUTHORIZED applies.
Every attempt — interrupted, defective or complete — is in the attempt log.
```

## 8.3 Only if T-R2-2 = AUTHORIZE_RESTART

The authorization permits a restart layer; it does not require one. Attempt 1 runs without it (§8.1). A restart
layer is introduced only after an attempt has ended by an INTERRUPTION (§8.2), and the report names that
interruption as the reason. Introducing it changes the harness, so the rule of §3 applies: the files of the
interrupted attempt are quarantined, W-3 is repeated, and nothing the interrupted attempt computed is used.

```text
A restart layer may exist under ALL of these conditions:
  keys        a unit is stored under a key over its full identity — code: the three W-3 hashes and the hashes
              of the frozen F2 engine and the frozen spline harness; input: the SHA256 of the input vector
              bytes; environment: interpreter version, numpy and scipy versions, platform string and the thread
              pins of v6 §8; unit: fixture, sex, trajectory, mask, family or mode, stage, run label, test id.
              The identity record is stored with the unit
  store       one directory, created EMPTY by the first attempt that has the layer, named in the W-3 record,
              listed with a manifest (path, size, SHA256) in the report. If the harness changes later (a defect
              fixed, §8.2), the store goes into the quarantine folder of that attempt and the next attempt
              starts with an empty store
  provenance  every stored unit carries the pid and start time of the process that computed it, and its call
              counters and telemetry rows (Y-01 T-CALLCOUNT); the results JSON reports, per run label, the
              units computed by the final process and the units read from the store, with their pids
  separation  RUN2 never reads a unit computed for RUN1, and no test reads a unit computed for another test;
              the residual series of RUN1 travel with their RUN1 units (Y-21)
  interruption once the layer exists, an INTERRUPTION is handled as in §8.2 except that the store stays in
              place and its manifest is recorded in the attempt log; every other file the process wrote goes
              to the quarantine folder of that attempt. The next process repeats the start checks of §8.1;
              everything else, the NR gates included, is a unit that it computes or reads under the
              conditions above
  check       T-RESTART-PROVENANCE (Y-01) in place of T-SINGLE-PROCESS whenever units came from more than one
              process
  progress    a process that completes no new unit is recorded as such in the attempt log; after two such
              processes in a row: STOP, deliver the attempt log, report to the PI
  wording     if every object of deliverables 5–8 was computed by one process, the determinism wording of v6 §8
              stands; otherwise it reads "RUN1 == RUN2 canonical SHA256, same bytes, <k> processes", k being the
              number of processes that computed units of deliverables 5–8, and never "same-process"
  status      T-R2-2 stays in narrowed_evidence whether or not the layer was introduced (§5, §10)
Without AUTHORIZE_RESTART none of this exists in the harness. Under AUTHORIZE_RESTART without an interruption none
of it exists either: the run is one process and T-SINGLE-PROCESS applies.
```

---

# 9. Deliverables (r3 child revisions; r1 and r2 files byte-unchanged; external sidecars; no self-hash)

```text
 1. p_konum_plus/calibration/f3_step2_adequacy_harness_r3_<date>.py          parent R-01
 2. p_konum_plus/calibration/f3_step2_fixture_generator_r3_<date>.py         parent R-02
 3. p_konum_plus/calibration/f3_step2_fixture_manifest_r3_<date>.csv         parent R-03 (W-2: before any run)
 4. p_konum_plus/provenance/f3_step2_r3_preexecution_custody_<date>.md       W-3
 5. p_konum_plus/calibration/f3_step2_telemetry_r3_<date>.csv                W-4 process
 6. p_konum_plus/calibration/f3_step2_results_r3_<date>.json                 W-4 process; LF; canonical document
                                                                             per v6 X-11; `process` block (Y-01)
 7. p_konum_plus/calibration/f3_step2_residual_series_r3_<date>.json         W-4; the RUN1 series (Y-21)
 8. p_konum_plus/calibration/f3_step2_test_evidence_r3_<date>.json           W-4 process
 9. p_konum_plus/calibration/f3_step2_class_c_pin_register_r3_<date>.md      parent R-09
10. p_konum_plus/provenance/f3_step2_correction_report_r3_<date>.md          complete (Y-18); every result
                                                                             labelled "executor claim;
                                                                             independent verification pending"
11. p_konum_plus/provenance/f3_step2_r3_start_state_inventory_<date>.md      W-1 (a), with its manifest CSV(s)
12. p_konum_plus/provenance/f3_step2_r3_attempt_log_<date>.md                every W-4 process start of this
                                                                             cycle, including the successful one
                                                                             (under §8.3 with the units each
                                                                             process computed)
13. attempt history of the r2 cycle, as a section of item 10: what ran when, which harness byte-versions
    existed, what the checkpoint directory held, whether a dispatch-precondition STOP report was written.
    Each statement names its source (a file with hash, a transcript with path and hash, a file timestamp).
    What cannot be established is written as NOT RECONSTRUCTIBLE. Nothing is inferred and nothing is invented
14. external .sha256 sidecars for 1–12 and for the manifest CSV(s) of item 11
15. at the end: re-hash every item of §2.1, §2.2 A and §2.2 B and report the values (parents unchanged)
<date> = the ISO date on which W-1 starts (§3), dashes; a STOP report written before W-1 carries the date on
which it is written. commit = false.
```

---

# 10. End state and response format (additions to v6 §13 and §14)

The six status fields and the computation of `F3_STEP2_r3_status` are those of v6 §13. For this cycle:
`deferred_decisions` contains S-R2-1 if its value is DEFERRED_THIS_CYCLE; `narrowed_evidence` contains T-R2-2 if
its value is AUTHORIZE_RESTART, whether or not a restart layer came to be used (§5); `open_findings` contains every
EXACT / ENG finding open at the end (TEST_ONLY injected events are not findings, Y-04 (b)); `corrections_complete`
covers Y-01 … Y-19 and Y-21 (Y-20 is optional) and the v6 corrections carried over.

Add to the end-state block of v6 §14:

```text
PI_dispatch_record_hash     = <observed> ; S-R2-1 and T-R2-2 as read (verbatim)
process                     = pid(s) ; start ; end ; attempts in this cycle = <n> (interruptions = <m>) ;
                              restart layer = absent / present ; processes that computed units of
                              deliverables 5–8 = <k> ; units read from the store = <count per run label>
expectation_checks          = <ran> / <declared> ; EXPECTATION_FAIL = [ids] or none
parents_unchanged           = true/false (§9 item 15)
```

Add to the response table of v6 §14 one row per Y-01 … Y-19 and Y-21, each with the executor claim (PASS / FAIL /
NOT_RUN(reason) / NOT APPLICABLE(reason) / STOP) and the evidence (path / hash / test id or document check), and
these rows, which replace the v6 rows on §2 custody, §3 preconditions, the write order and "r1 files
byte-unchanged":

| Check | executor claim | evidence |
|---|---|---|
| §2 custody: §2.1, §2.2 A, §2.2 B, §2.3 exact; §2.4 recorded; no surrogate used | | |
| §3 preconditions P-1 … P-4; P-4 evidenced by the PI dispatch record | | |
| W-1 start-state inventory written; earlier-attempt files moved, not deleted, and re-hashed; CI-01 objects listed apart | | |
| W-3 record written before the first W-4 process started; hashes re-computed by every W-4 process and equal | | |
| deliverables 5–8 from one W-4 process (T-SINGLE-PROCESS) or, under §8.3, from processes whose units pass T-RESTART-PROVENANCE; T-CALLCOUNT | | |
| every fixture expectation checked (T-EXPECT-ALL) | | |
| attempt history of the r2 cycle disclosed with sources | | |
| r1 and r2 files byte-unchanged at the end | | |

Document checks for the cleanup items (Y-08). The executor performs each on the delivered files and reports it
as its row of the response table:

```text
Y-09  the report names D-4 (path and hash) as the evidence of P-4
Y-10  every register row tagged VERBATIM is a byte-substring of D-2 or D-4; no other row carries that tag
Y-11  the coverage row on the K-05 invariant equals the wording of content §6, in register and coverage matrix
Y-12  the opened-file list is present and unfiltered; its class "anything else" is empty or explained
Y-13  number of node-hash entries == number of executed nodes; the I/O-free assertion ran over all of them;
      the register row PIN-EXC-CAPTURE is present
Y-14  the three items of v6 X-12 are present in the register
Y-15  T-MASK-FULL-EXT ran and passed
Y-16  the coverage statuses were derived by the harness from this run (no pre-run constant); one vocabulary
Y-17  every return of the consulted-level code whose mechanism outcome is a STOP writes a `stops` record; no
      return with another outcome writes one
Y-18  the report contains every part that v6 §12 item 10 and v6 §14 list
Y-19  the TEST_ONLY branches of the evaluator are disclosed in the register
```

The hash line block of v6 §14 additionally lists deliverables 11 and 12; sidecars and "no self-hash" are reported
as in v6. Classification vocabulary, claim labelling and the prohibition of "verified" / "QUALIFIED" wording:
v6 §14.

---

# 11. Independent audit after return (addition to v6 §15; do NOT perform it yourself)

In addition to v6 §15 the auditor will: compare the pid and the call counters of the `process` block with the
telemetry; check the line numbers in every captured traceback against the delivered harness bytes; regenerate
the manifest from the generator; re-evaluate every decision-layer fixture and every unit test of §7 with the
delivered harness; diff every VERBATIM register row against D-2 and D-4; read the start-state inventory and the
attempt log against the file lists; check every exported residual series against the RUN1 link records (Y-21);
under §8.3, read the store manifest and the unit provenance against the attempt log. F3_STEP2 = QUALIFIED can be
declared only by the PI after that audit.

---

# 12. Dispatch readiness (PI view)

A. Scientific readings this prompt applies, with their sources. `read_and_accepted` does NOT accept them; they are
either direct applications of binding text or left to the PI:

```text
A-1  an invalid statistic (None or non-finite) at a member of the C2, C4b or C5 valid set makes the sex-level
     statistic undefined and the criterion not passed (Y-03 (i)): a direct application of frozen r4 §2 and §3,
     with the v5 §4 pins and v6 X-09 — the map is §6.1. No new reading is made
A-2  C3: CL-F3-04 as the freeze record binds it; unchanged
A-3  the C4b state in which both probes of a fitter succeed and that fitter has no full-data reference: not
     determined by the frozen text (§6.1); PI field S-R2-1 (§5). This prompt selects no value
A-4  any further state the sources do not determine: an exactness finding (EXACT-04 onward, v6 §10); only the
     affected criterion is PENDING, and dispatch settles nothing of it
```

B. Engineering and test-design choices of the drafter — not S / T options; listed so that they can be reviewed or
changed before dispatch. `read_and_accepted = YES` in D-4 accepts these, and only these:

```text
 1. constructions of the exclusion fixtures (§7): invalidity produced through the frozen valid-set rule (a
    fitter that is not crossfit-complete), plus function-level unit tests for the decision-layer states that
    cannot pass the P03 gate. This replaces the first half of v6's T-FINITE-DP04 and re-builds three r2 fixtures
 2. the S-R2-1 state is read from the procedural flags (`pL`, `pR`, `full`), not from the presence of a value
    (§5). Under DEFERRED_THIS_CYCLE, at least: the outcome of INJ-DP04-C1 changes; C4b is PENDING in
    INJ-C1-FAIL and in SCEN-B (M); the coverage rows "D-P04 resolve at C1" and real-path "C4b fail" lose their
    evidence (§7); EXACT-03 is reserved for it; half of UT-PROBE-DECOUPLE is NOT_RUN
 3. restart: one process without a restart layer by default. Under AUTHORIZE_RESTART a layer only after an
    interruption and only as §8.3 says (keys over code, input and environment identity; an empty store; unit
    provenance; RUN1 / RUN2 and test separation; counters over all processes; T-RESTART-PROVENANCE in place of
    T-SINGLE-PROCESS; STOP after two processes without progress). Under NOT_AUTHORIZED: STOP after the second
    interruption
 4. machine-readable expectations for every fixture, transcribed or derived by the executor and checked by the
    harness; EXPECTATION_FAIL is reported, never re-described
 5. three exception-injection fixtures and two unit tests in place of v6's single INJ-EXC-CAPTURE (content §9
    asks for the distinctions); an arming rule in place of a predeclared mode; an unrelated natural exception is
    routed to an exactness finding, a TEST_ONLY injected one is not; call site and stage are established from
    the call stack. The exception-class condition is content §3.1's, with nothing added
 6. the r2 checkpoint directory is moved into quarantine; executor transcripts may be cited as sources of the
    attempt history
 7. v6 X-18 (opened-file list) is required, not optional (Y-12)
 8. the three injection contexts and FIX-A5-TRUE add real-fit contexts to the canonical document
 9. the residual series are recorded by RUN1 where it computes C3 and are linked by hash (Y-21, T-RESIDUAL-LINK)
10. INJ-NAN-STAT-C4B and UT-USET-CONSTRUCTION (d) place the NaN on the RIGHT side, where Python's built-in max
    would drop it (Y-03 (i))
11. two coverage rows may honestly come out UNCOVERED (Y-16); with any UNCOVERED row, any deferred decision, any
    narrowed evidence (AUTHORIZE_RESTART included) or any open finding the status of the cycle is
    PARTIAL_PENDING_PI by v6 §13
```

No longer in this list, compared with DRAFT v1: "a missing sidecar of an r2 deliverable is a STOP" (the rule of
item 19 now applies to the r2 sidecars as well, §2.2 B R-11) and the reading of "RuntimeError" as the class itself
(withdrawn, Y-04). DRAFT v1's item 1 is now §12 A with the map of §6.1.

What this draft still needs before dispatch:

| item | kind | status | what makes it ready |
|---|---|---|---|
| S-R2-1 | PI scientific decision (MANDATORY) | PENDING | exactly one value from §5 written into the PI dispatch record; a blank stops the executor before it starts (§3 P-3) |
| T-R2-2 | task-scope authorization (OPTIONAL) | AUTHORIZE_RESTART, given by the PI on 2026-09-21 and entered in the template | read from D-4; the PI may change it before dispatch |
| T-R2-1 | statement about the r2 dispatch (audit register) | open | optional §6 of the dispatch-record template; a later statement, not contemporaneous evidence; it does not condition this cycle |
| PI dispatch record (D-4) | PI-owned file | MISSING | f3_step2_r3_pi_dispatch_record_TEMPLATE_v2.md, filled in by the PI (external sidecar recommended; §2.3 D-4) |
| SHA256 of this file | dispatch-class | n/a until dispatch | computed by the PI on the exact file handed over and written into D-4 |
| prompt v6 (D-1) and content file (D-2) | dispatch-class | not verified by the drafter | in p_konum_plus/prompts/, or handed over byte-exact with the dispatch |
| record-class attachments (§2.4) | transmission | optional | attach what is at hand; absence is NOT_LOCATED, never a STOP |
| external review of this draft | workflow | not reviewed | a document review is not an independent verification of implementation adequacy |

```text
This draft selects no option, ratifies nothing, authorizes nothing and starts nothing.
F2 = CLOSED ; F3_STEP1 = FROZEN ; F3_STEP2_audit_verdict = NOT PASSED ; F3_STEP2_qualification = WITHHELD
F3_EXECUTION_READY = false ; real_SSA_execution = prohibited ; new_methodology_review = false ; commit = false
```
