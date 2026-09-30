# p_konum_plus — F3 STEP-1 Freeze Record r1 — Report

```text
artifact_role = r1 child-revision report (deliverable 2 of the r1 cross-reference-key task)
status        = NON-NORMATIVE
date          = 2026-09-05
correction    = C-R1-01 only (cross-reference key + I-R1-04 import-provenance rows)
scientific_change = false ; PI_decision_change = 0 ; new_literal = 0
execution_prompt = Claude_Code_F3_STEP1_FREEZE_RECORD_r1_CROSSREF_KEY_PROMPT_v1_2026-09-05.md
```

## 1. Custody table (all exact; no STOP)

| artifact | expected | observed | status |
|---|---|---|---|
| parent record `p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md` | `bef216e3…` | `bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f` | EXACT (read-only; re-verified byte-unchanged AFTER the r1 write) |
| audit record (custody-imported byte-exact this task to `p_konum_plus/provenance/f3_step1_freeze_record_independent_audit_2026-09-05.md`) | `99b615d2…` | `99b615d2c3ee0c94815af7793e1d8be669a29ef5d070891224d457305864a4dc` | EXACT (source and target identical) |
| r4 candidate | `5e594136…` | `5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad` | EXACT (untouched) |
| v5 prompt | `679b5e32…` | `679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09` | EXACT (untouched) |
| custody-import prompt v2 (for the `<observed>` lineage cell) | observed-only | `09df38443346229fc2dac0afb795e6c5cd6b621fe1e4e6756316c43416e96f65` | recorded |

## 2. Parent → r1 diff hunk list (git diff --no-index, zero-context)

```text
@@ -1 +1 @@            (a) title: "… Freeze Record" -> "… Freeze Record — r1"
@@ -9 +9,8 @@          (b) status value -> SUPERSEDED_BY_r1_FOR_READING (historical);
                            inserted revision block ending with the new status line
                            PI_RATIFIED_RECORD_AUDIT_PASS_r1_PENDING_NARROW_REAUDIT
@@ -75,0 +83,15 @@     (c) CROSS-REFERENCE KEY block inserted immediately before the
                            decision_class legend block (verbatim per the prompt)
@@ -417,0 +440 @@      (e) findings closure: appended line "C-R1-01 = CLOSED_BY_r1_KEY"
@@ -445,0 +469,7 @@    (d) lineage table: seven import-provenance rows appended
                            (v2 import prompt <observed> = 09df3844…)
@@ -456 +486 @@        (e) §10: F3_STEP1_FREEZE_RECORD =
                            CREATED_PENDING_INDEPENDENT_RECORD_AUDIT ->
                            AUDIT_PASS_r1_PENDING_NARROW_REAUDIT
```

The hunk list shows ONLY the (a)–(e) changes. The eleven verbatim blocks
(§0 attestation + DECISION_HISTORY; §2 register table and literals; §3; §4;
§5; §6; §7 block; §8 list; §10 end-state and next action) are byte-identical
to the parent, except exactly the two single-line modifications that (e)
itself mandates (the appended C-R1-01 line in §8 and the one changed
F3_STEP1_FREEZE_RECORD line in §10) — no other byte inside any verbatim block
changed, so the parent audit's byte comparisons remain valid for r1.

## 3. Post-write re-verification

```text
parent bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f = byte-unchanged
r4     5e594136…                                                        = untouched
audit  99b615d2…                                                        = as imported
r1     7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460
r1 sidecar = f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md.sha256 (external; no self-hash)
commit = false ; no F3 execution ; no statistic computed
```
