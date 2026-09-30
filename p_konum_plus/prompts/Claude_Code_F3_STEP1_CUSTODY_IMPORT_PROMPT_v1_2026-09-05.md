# Claude Code Prompt — F3 STEP-1 Custody Import (pre-condition for the v5 freeze-record task)

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Task class:** byte-exact custody import of provenance artifacts; no content authoring; no scientific content  
**Authority:** Claude Code is execution/provenance authority only  
**Status:** NON-NORMATIVE execution prompt

```text
prompt_id = Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v1_2026-09-05.md
reason    = the v5 freeze-record task STOPped on §1 item 6 (audit record absent from
            p_konum_plus/provenance/) — see f3_step1_freeze_record_task_stop_report_2026-09-05.md
pattern   = identical to the earlier STEP-2 r3 / STEP-3 r1 custody-import tasks
scientific_change = false ; F2_reopening = false ; F3_execution = prohibited
```

---

# 1. Rule

For every file listed in §2: copy the attached file byte-exactly to the target path under
the **canonical file name** (ISO date with dashes, `2026-09-05`; the attached copies may
carry the download variant `20260905` — rename, never edit), then recompute SHA256 at the
target and compare with the expected value.

```text
REQUIRED item mismatch or absent  ⇒ STOP ; classification = global blocker ;
                                      report observed vs expected ; import nothing else
RECORD item mismatch              ⇒ do NOT copy that item ; classification = cleanup ;
                                      report observed vs expected ; continue
RECORD item absent from attachments ⇒ report NOT_ATTACHED ; continue
any existing repository file modified ⇒ prohibited
commit                            ⇒ only if separately requested
```

Do not open, reformat, normalize line endings, or otherwise touch file contents. Do not
self-hash anything into any file body.

# 2. Import list

```text
REQUIRED (the item that triggered the STOP):

I-01  f3_step1_r4_independent_audit_2026-09-05.md
      target   = p_konum_plus/provenance/f3_step1_r4_independent_audit_2026-09-05.md
      expected = 84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea

RECORD (complete the freeze-record custody table; each is a v5 §1 item):

I-02  f3_step1_r3_to_r4_independent_regenerated_diff_2026-09-05.txt          (v5 §1 item 10)
      target   = p_konum_plus/provenance/f3_step1_r3_to_r4_independent_regenerated_diff_2026-09-05.txt
      expected = 9b070d4b1302ca5acbe19a8c69b2a67e17f823d5936f187ff47ff69405de2273

I-03  f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md   (v5 §1 item 9)
      (attached copy may be named 3_claude.md — rename to the canonical name above)
      target   = p_konum_plus/provenance/f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md
      expected = 34862e56e6db46d0a8b07c21dea66d149cb9fa3a0d91ab21c88f12f48e2ad892
                 (auditor-observed; a differing PI copy is recorded, not rejected — v5 §1 item 9 rule)

I-04  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md      (item 12)
      expected = da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7
I-05  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_2026-09-05.md      (item 13)
      expected = 2860fade8d34e74b8ea77d22d469fa0c9b29e05eaf27310b407a45031a626243
I-06  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v3_2026-09-05.md      (item 15)
      expected = 4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7
I-07  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_2026-09-05.md      (item 17)
      expected = bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458
I-08  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md      (execution prompt)
      expected = 679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09
      target for I-04 .. I-08 = the directory that holds v5 §1 item 8
                 (Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md)

I-09  F3_STEP1_PI_Ratification_Freeze_Prompt_Comparison_Evaluation_2026-09-05.md      (item 11)
      expected = c12b275291c7341b3bd7b27618c8a25a91ad36af91ac60261e4195fdf3c73777
I-10  F3_STEP1_PI_Ratification_Freeze_Prompt_v2_Review_2026-09-05.md                  (item 14)
      expected = 07c3306339eabb86fce0f24578ee5e539d0fb85fb06e3e181a22cf0e3a0bb842
I-11  F3_STEP1_PI_Ratification_Freeze_Prompt_v3_Review_2026-09-05.md                  (item 16)
      expected = 90051cb702d63d506213c04f38fac6c77d4651ddc812bb0733cd01bef346db0d
I-12  F3_STEP1_PI_Ratification_Freeze_Prompt_v4_Review_2026-09-05.md                  (item 18)
      expected = 8b04f83e439b786afce1ad969dfd12028ccc02a344e34e26e6f217aa343bac55
      target for I-09 .. I-12 = p_konum_plus/provenance/

I-13  f3_step1_freeze_record_task_stop_report_2026-09-05.md   (the STOP report; provenance of this import)
      target   = p_konum_plus/provenance/f3_step1_freeze_record_task_stop_report_2026-09-05.md
      expected = none pre-stated ; record observed SHA256
```

# 3. Required response

| item | canonical target path | expected SHA256 | observed SHA256 at target | result (EXACT / MISMATCH / NOT_ATTACHED) |
|---|---|---|---|---|

Then:

```text
REQUIRED item I-01 = EXACT / STOP
existing files modified = 0
commit = false
next action = re-dispatch Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
              UNCHANGED (its §1 item 6 now resolves); no prompt edit, no v6
```

Final classification vocabulary only: `global blocker` / `gate-specific blocker` / `cleanup` /
`informational`.
