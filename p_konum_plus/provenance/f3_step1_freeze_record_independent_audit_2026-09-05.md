# p_konum_plus — F3 STEP-1 PI Ratification & Freeze Record — Independent Record Audit

```text
artifact_role = independent audit of the F3 STEP-1 PI ratification & freeze record
                (deliverable 1 of the v5 freeze-record task) and its provenance report
                (deliverable 2); transcription-exactness audit per prompt v5 §15
status        = NON-NORMATIVE; advisory to the PI
date          = 2026-09-05
auditor       = Claude (chat) — independent/advisory auditor; NOT PI authority

audited_record   = p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md
                   sidecar SHA256 = bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f
                   observed SHA256 (auditor) = identical ; 497 lines (as reported)
audited_report   = p_konum_plus/provenance/f3_step1_ratification_provenance_report_2026-09-05.md
                   sidecar SHA256 = 2c746625acee73e610e09179ed00c1dc90c0dddc905c1c05d7dcf5c91c1ad1fc
                   observed SHA256 (auditor) = identical
execution_prompt = Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
                   SHA256 679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09
                   (the auditor's own copy; the record's execution_prompt field cites the same value)

audit_result:
  GLOBAL_BLOCKER        = none
  GATE_SPECIFIC_BLOCKER = none
  cleanup               = 1  (C-R1-01: section cross-reference numbering offset inside verbatim blocks)
  informational         = 5  (I-R1-01 .. I-R1-05)
  F3_STEP1_FREEZE_RECORD_AUDIT = PASS
```

---

## 1. Custody (v5 §15 items 1–2)

| check | result | evidence |
|---|---|---|
| record hash = sidecar | PASS | `bef216e3…` recomputed by the auditor from the delivered bytes |
| report hash = sidecar | PASS | `2c746625…` recomputed by the auditor |
| record contains its own hash (self-hash) | PASS (none) | grep `bef216e3` → 0 |
| every full SHA256 in the record is a known artifact | PASS | 28 occurrences, 19 distinct, 0 unknown; all 19 expected artifacts present (v11, F2 FREEZE r1, r3, r4, r3→r4 report, audit record, r3 provenance report, exactness prompt v4, r2 synthesis, regenerated diff, four reviews, prompts v1–v5) |
| v5 §1 items 1–6 EXACT; 7–18 recorded | PASS (as reported; hashes verified against the auditor's known values) | report §1 table; the auditor cannot observe the repository — I-R1-02 |
| r3 / r4 / audit record / correction report byte-unchanged after the write | PASS (as reported) | report §4 lists the four unchanged hashes; all equal the auditor's known values |
| execution prompt under repository custody | PASS | `p_konum_plus/prompts/…_v5_2026-09-05.md`, `679b5e32…` (custody-import v2 evidently executed) |

## 2. Attestation gate and identity block (v5 §15 items 2a, 9)

| check | result | evidence (record lines) |
|---|---|---|
| §3.0 PI_ATTESTATION + DECISION_HISTORY verbatim in record §0 | PASS | 45–73 byte-identical to v5 267–295 |
| `PI_confirmation = CONFIRMED_BY_DISPATCH` | PASS | line 66 |
| DECISION_HISTORY copied as provenance only, not a gate | PASS | 68–73 |
| decision_class legend present | PASS | 77–81 |
| 6B labelled PI_SCIENTIFIC_SCOPE_DECISION | PASS | 81, 356–359, 363 |
| precedence sentence + v11_wins = true | PASS | 83–90 |
| identity fields (artifact_id, role, date, status, ratified_candidate, ratification_basis, decision_basis, execution_prompt + lineage) | PASS | 6–41 |

## 3. Verbatim-block comparison (v5 §15 items 3–8) — auditor byte comparison, not the report's claim

| block | v5 lines | record lines | result |
|---|---|---|---|
| §3.1 register table (16 rows) | 317–334 | 118–135 | VERBATIM; exactly 1 MODIFY (D-P04_COMMON_SUPPORT_FLOOR, 130), exactly 1 NOT_APPLICABLE (D-P04_COMMON_SUPPORT_FAILURE_ACTION, 131); no row added, dropped or re-worded |
| ratified-literals list | 339–347 | 140–148 | VERBATIM; `new_numeric_literal_count = 0` |
| §4 D-P04 common-support contract text (4.1–4.4) | 364–429 | 154–219 | VERBATIM; 0.80 bound stated as mathematics only; §4.3 "mathematically excluded … a theorem, not a rarity claim" |
| §5 canonical K-05 | 437–465 | 225–253 | VERBATIM; consistent with the ratified branch (P03_GATE, WORSE, 0.90, 0.85); no a-fortiori claim; denominator declaration exact |
| §6 CL-F3-01 .. CL-F3-05 | 473–499 | 259–285 | VERBATIM; CL-F3-04 "extremely rare but is not excluded" |
| §7 DISC-F3-01 .. DISC-F3-05 | 507–564 | 291–348 | VERBATIM; no independence approximation; "valid / paired-valid set"; 906-representation sentence in r4 semantics |
| §8 6B companion block | 580–618 | 362–400 | VERBATIM; no numeric reporting literal; deferred-pin list present; ratio ≥ 1 conditional |
| §9 findings closure | 626–637 | 406–417 | VERBATIM |
| §14 end-state | 749–764 | 455–470 | VERBATIM |
| §14 next action (three separately governed steps; 6B outside CLASS_C) | 770–790 | 476–496 | VERBATIM |

Authored (non-verbatim) record text — §1 by-reference list (94–114), §9 lineage table
(425–448), §7 decision-class paragraph (353–359 — cross-reference adapted to "§0
PI_ATTESTATION (3)") — checked for content: no scientific statement, no literal, no
execution result; lineage table = 19 rows, every hash known.

## 4. Remaining v5 §15 items

| item | result | evidence |
|---|---|---|
| 10 no execution, no computed statistic, no candidate-specific number | PASS | the only numbers in the record are ratified literals, derived bounds already audited in v5, hashes, dates and line/section numbers |
| 11 end-state identical to v5 §14; F3_EXECUTION_READY = false | PASS | 455–470, 495–496 |
| 12 sidecars present; no self-hash in any body | PASS | both `.sha256` files delivered; §1 above |

## 5. Findings

### C-R1-01 — cleanup: two section-numbering systems inside the record

The verbatim blocks were (correctly) copied unchanged from the execution prompt and therefore
carry the **prompt's** section numbers (§3.0, §3.1, §4–§8, 4.1–4.4), while the record's own
headings are §0–§10 and its authored sentences use record numbering (e.g. line 110 "this
record's §3", legend lines 79/81). Concrete prompt-numbered references inside the record:

```text
line 118  "(pointer; write-outs in §4–§8)"          -> record §3–§7
line 122  "registry additions of §6"                 -> record §5 (CL-F3-05)
line 127  "6B companion … (§8)" / "DISC-F3-05 (§7)"  -> record §7 / §6
line 130  "exact ratified text in §4.2"              -> record §3, item 4.2
line 131  "exact retirement text in §4.3"            -> record §3, item 4.3
line 135  "exact text in §5"                         -> record §4
line 348  "6B companion (§8)"                        -> record §7
line 363  "(explicit; §3.0 item 3)"                  -> record §0 PI_ATTESTATION (3)
line 410  "no undefined branch remains — §4.3"       -> record §3, item 4.3
line 415  "K-05 = CLOSED_AS_DISCLOSED (§5)"          -> record §4
line 458  "PI_attestation = CONFIRMED_BY_DISPATCH (§3.0)" -> record §0
line 492  "scope per §8"                             -> record §7
```

Every reference is resolvable by name (K-05, 6B companion, CL-F3-05, 4.2/4.3), so no
decision, literal or contract semantics is affected; but a reader of the record alone who
follows a "§8" lands on "Findings closure" instead of the 6B companion. Root cause: the
execution prompt (v5 §13) mandated both verbatim copying and a different section layout
without a remap instruction — the defect is the prompt author's, not Claude Code's.

Recommended fix (narrow, non-blocking; F2 FINAL FREEZE r1 pattern): child revision
`f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md` with parent hash `bef216e3…`,
adding to §0 a reading key — no verbatim block edited, so this audit's byte comparisons
remain valid for r1:

```text
CROSS-REFERENCE KEY (binding reading rule for section numbers inside the verbatim
blocks of §0, §2–§8 and §10, which retain the execution prompt's numbering):
  prompt §3.0            -> this record §0 PI_ATTESTATION
  prompt §3.1            -> this record §2 (register)
  prompt §4 (4.1–4.4)    -> this record §3
  prompt §5              -> this record §4 (K-05)
  prompt §6              -> this record §5 (CL-F3-01..05)
  prompt §7              -> this record §6 (DISC-F3-01..05)
  prompt §8              -> this record §7 (6B companion)
  prompt §9              -> this record §8 (findings closure)
  prompt §14             -> this record §10
References to "r4 §…" are unaffected (they address the ratified candidate).
```

### Informational

```text
I-R1-01  Record §1 line 110 says r4 "§9.5 K-05 superseded by §4". Read as "specialised
         to the ratified branch": r4 §9.5 (branch-complete K-05) remains valid historical
         provenance for the non-ratified branches; the record's §4 is the binding
         disclosure for the ratified branch. No action.
I-R1-02  Repository state (items EXACT at their repo paths; post-write byte-unchanged
         re-verification) is attested by Claude Code's report; the auditor verified that
         every cited hash equals the independently known value but cannot observe the
         repository itself. Consistent with all prior audits in this project.
I-R1-03  The v5 §16 end-of-task response table was not delivered to the auditor; the
         provenance report covers its substance (custody, transcription check, block
         mapping, end state). No action unless the PI wants it archived.
I-R1-04  The record's §9 lineage table omits the custody-import prompts v1/v2, their
         end-of-task report and the STOP report (import provenance, not ratification
         provenance). Acceptable; may be added in r1 as "import provenance" rows.
I-R1-05  Repository has ~64 untracked provenance files and commit = false throughout;
         a single provenance commit at a point of the PI's choosing would close the
         custody loop (PI decision; outside this audit).
```

## 6. Gate state after this audit

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false

F3_STEP1_FREEZE_RECORD_AUDIT = PASS   (record bef216e3… ; report 2c746625…)
F3_STEP1_PI_RATIFICATION     = RECORDED_AND_AUDITED
F3_STEP1_status              = FROZEN   (r4 5e594136… as ratified by record bef216e3…;
                                         record precedence over r4 recommended text;
                                         v11 wins on any conflict)

findings (per record §8, now unconditional):
  D-P04-COMMON-SUPPORT-01      = CLOSED
  F3-STEP1-FAILBRANCH-01       = CLOSED
  F3-STEP1-C3-ACF-01           = CLOSED
  F3-STEP1-C4B-SEPARATE-P04-01 = CLOSED_NOT_APPLICABLE
  K-05                         = CLOSED_AS_DISCLOSED
  audit cleanup C-01 .. C-05   = CLOSED_BY_FREEZE_WORDING
  C-R1-01                      = OPEN (cleanup; non-blocking; r1 recommended)

F3_STEP1_open_PI_rows = 0 ; PI_MODIFY_count = 1 ; PI_NOT_APPLICABLE_count = 1
PI_scope_decision_count = 1 ; new_numeric_literal_count = 0
6B_companion = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED

F3_EXECUTION_READY = false ; F3_started = false ; generator_selected = false
P03_threshold_values = NOT_COMPUTED ; commit = false
```

## 7. Next action only

```text
1. (recommended, non-blocking) record r1 = parent bef216e3… + CROSS-REFERENCE KEY in §0
   (+ optionally I-R1-04 import-provenance rows); verbatim blocks byte-unchanged;
   narrow re-audit = hash + key text + block-unchanged check
2. F3 STEP-2 implementation-pin task (CLASS_C only; no 6B content) — separately governed
3. R-REV 6B companion specification task — separately governed
F3_EXECUTION_READY remains false until 2 and 3 (and r1, if opened) have independently passed.
No F3 execution. No F2 reopening. No PI row reopened.
```
