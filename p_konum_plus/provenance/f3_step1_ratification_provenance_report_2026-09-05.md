# p_konum_plus — F3 STEP-1 Ratification — Provenance Report

```text
artifact_role = provenance report for the F3 STEP-1 PI ratification & freeze
                record (deliverable 2 of the v5 freeze-record task)
status        = NON-NORMATIVE
date          = 2026-09-05
freeze_record = p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md
execution_prompt = p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
                   observed SHA256 = 679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09
```

## 1. Custody table (§1 items 1–18)

| # | artifact (repo path) | expected | observed | status |
|---|---|---|---|---|
| 1 | v11 FINAL NORMATIVE | `d136502f…` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | EXACT (STOP-class) |
| 2 | F2 FINAL FREEZE r1 | `ee2cb99d…` | `ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43` | EXACT (STOP-class) |
| 3 | r3 candidate (read-only) | `350bc15e…` | `350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad` | EXACT (STOP-class) |
| 4 | r4 ratified candidate (read-only) | `5e594136…` | `5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad` | EXACT (STOP-class) |
| 5 | r3→r4 correction report | `5955e865…` | `5955e86590d1c4706000e4e43e6d5cf692dd000ba867a3b26170d1c5548de877` | EXACT (STOP-class) |
| 6 | r4 independent audit (`p_konum_plus/provenance/`) | `84c24165…` | `84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea` | EXACT (STOP-class; PASS evidence) |
| 7 | r3 provenance correction report (historical) | `006f6c61…` | `006f6c615dd1e9bfddee739fb53d8565927ef41a2c9ab76b3cba082a96839815` | EXACT (recorded) |
| 8 | r3→r4 exactness prompt v4 (`p_konum_plus/prompts/`) | `b5ce12c3…` | `b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00` | EXACT (recorded) |
| 9 | r2 synthesis (decision basis) | auditor-observed `34862e56…` | `34862e56e6db46d0a8b07c21dea66d149cb9fa3a0d91ab21c88f12f48e2ad892` | EXACT (recorded; project copy = auditor copy) |
| 10 | auditor regenerated diff | auditor-observed `9b070d4b…` | `9b070d4b1302ca5acbe19a8c69b2a67e17f823d5936f187ff47ff69405de2273` | EXACT (recorded) |
| 11 | comparison evaluation (v1 review) | `c12b2752…` | `c12b275291c7341b3bd7b27618c8a25a91ad36af91ac60261e4195fdf3c73777` | EXACT (recorded) |
| 12 | freeze prompt v1 (lineage) | `da5a0a13…` | `da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7` | EXACT (recorded) |
| 13 | freeze prompt v2 (lineage) | `2860fade…` | `2860fade8d34e74b8ea77d22d469fa0c9b29e05eaf27310b407a45031a626243` | EXACT (recorded) |
| 14 | v2 review | `07c33063…` | `07c3306339eabb86fce0f24578ee5e539d0fb85fb06e3e181a22cf0e3a0bb842` | EXACT (recorded) |
| 15 | freeze prompt v3 (lineage) | `4f2b6492…` | `4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7` | EXACT (recorded) |
| 16 | v3 review | `90051cb7…` | `90051cb702d63d506213c04f38fac6c77d4651ddc812bb0733cd01bef346db0d` | EXACT (recorded) |
| 17 | freeze prompt v4 (lineage, parent) | `bfa9b7d8…` | `bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458` | EXACT (recorded) |
| 18 | v4 review | `8b04f83e…` | `8b04f83e439b786afce1ad969dfd12028ccc02a344e34e26e6f217aa343bac55` | EXACT (recorded) |

No STOP condition; attestation gate PASS (`PI_confirmation = CONFIRMED_BY_DISPATCH`;
the §3.0 block names the dispatched file exactly and was copied verbatim).

## 2. Decision-transcription check (every §3 row → freeze-record location)

The freeze record is 497 lines. The full §3.1 register (16 rows incl. the three
D-P03-5 sub-rows, the conditional-dependency row and the K-05 row) is
transcribed exactly once as the table in freeze record §2, lines 118–135
(one table row per register row, in the prompt's order; no row added, dropped
or re-worded; exactly one MODIFY — D-P04_COMMON_SUPPORT_FLOOR, line 129 — and
exactly one NOT_APPLICABLE — D-P04_COMMON_SUPPORT_FAILURE_ACTION, line 130).
The ratified-literals list is verbatim at lines 137–149.

## 3. Verbatim-block check (prompt § → record location)

| prompt block | freeze-record location (lines) | status |
|---|---|---|
| §3.0 PI_ATTESTATION + DECISION_HISTORY | §0, 44–75 | verbatim |
| §3.1 register table + literals | §2, 116–149 | verbatim |
| §4 D-P04_COMMON_SUPPORT ratified contract text (4.1–4.4) | §3, 151–220 | verbatim |
| §5 canonical K-05 disclosure | §4, 222–254 | verbatim |
| §6 CL-F3-01 .. CL-F3-05 | §5, 256–286 | verbatim |
| §7 DISC-F3-01 .. DISC-F3-05 | §6, 288–349 | verbatim |
| §8 6B companion block + decision-class paragraph | §7, 351–401 | verbatim; labelled PI_SCIENTIFIC_SCOPE_DECISION; not created; not executed |
| §9 findings closure | §8, 403–421 | verbatim |
| §13 identity/lineage requirements | §0 (3–90), §9 (423–448) | present |
| §14 end-state + next action | §10, 450–497 | verbatim |

Spot confirmations of the audit-mandated wordings: §4.3 uses "mathematically
excluded … a theorem, not a rarity claim"; CL-F3-04 uses "extremely rare but is
not excluded"; K-05 carries no a-fortiori claim on U4_s and declares |U4_s| <=
|V4_s| <= n_s; DISC-F3-04 contains no independence approximation and uses
"valid / paired-valid set"; §7 6B block contains no numeric reporting literal
and carries the deferred-pin list (summary statistics / undefined-ratio
behaviour / identical objective and grid); precedence sentence present (line
88–90) with v11_wins = true.

## 4. Post-write byte-unchanged re-verification

Recomputed AFTER writing the freeze record and this report:

```text
r3           = 350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad  unchanged
r4           = 5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad  unchanged
audit record = 84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea  unchanged
correction report = 5955e86590d1c4706000e4e43e6d5cf692dd000ba867a3b26170d1c5548de877  unchanged
```

(Verified in the end-of-task run; no tracked file modified; no commit.)

## 5. End-state block (§14)

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false

F3_STEP1_PI_RATIFICATION   = RECORDED
F3_STEP1_FREEZE_RECORD     = CREATED_PENDING_INDEPENDENT_RECORD_AUDIT
F3_STEP1_open_PI_rows      = 0
PI_attestation             = CONFIRMED_BY_DISPATCH (§3.0)
prior_PI_choice_overwrites = 0
PI_MODIFY_count            = 1   (D-P04_COMMON_SUPPORT_FLOOR)
PI_NOT_APPLICABLE_count    = 1   (D-P04_COMMON_SUPPORT_FAILURE_ACTION)
PI_scope_decision_count    = 1   (6B companion adoption; packet-external)
new_numeric_literal_count  = 0

RATIFICATION_READY         = consumed (historical)
F3_EXECUTION_READY         = false
F3_started                 = false
6B_companion               = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED
P03_threshold_values       = NOT_COMPUTED
generator_selected         = false ; commit = false
```
