# Claude Code Prompt — F3 STEP-1 Custody Import v2 (execution prompts into repository custody)

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Task class:** byte-exact custody import; no content authoring; no scientific content  
**Status:** NON-NORMATIVE execution prompt

```text
prompt_id      = Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v2_2026-09-05.md
parent         = Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v1_2026-09-05.md
                 SHA256 adb59f60e7c1a72b6e901b86d1958a874f09c1301003b32c4884816fe43ab792
v1 outcome     = I-01 .. I-03, I-08 .. I-13 EXACT ; I-04 .. I-07 NOT_ATTACHED
                 (f3_step1_custody_import_endoftask_report_2026-09-05.md, observed 9d79ec56…)
reason for v2  = (a) the v1 "directory that holds item 8" resolved to C:/Users/Neo/Downloads/,
                     i.e. the execution prompts are NOT under repository custody; a freeze
                     record must cite an execution_prompt path inside the repository
                 (b) lineage prompts v1–v4 are now attached
scientific_change = false ; F2_reopening = false ; F3_execution = prohibited
```

# 1. Rule (identical to v1)

Copy each attached file byte-exactly to the target path under its canonical name (ISO date with
dashes; rename download variants `20260905` → `2026-09-05`, never edit), recompute SHA256 at the
target, compare. Mismatch of a REQUIRED item ⇒ STOP (global blocker). Existing repository files
are never modified; the Downloads copies are left untouched (not deleted, not moved). Create the
directory `p_konum_plus/prompts/` if absent. Commit only if separately requested.

# 2. Import list — all targets `p_konum_plus/prompts/`

```text
REQUIRED
P-01  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md   (execution prompt)
      expected = 679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09
      source   = the canonical-name copy already verified in Downloads (v1 item I-08) or the attachment
P-02  Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md   (v5 §1 item 8)
      expected = b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00
      source   = the Downloads copy verified EXACT in the STOP report

RECORD (lineage; v5 §1 items 12, 13, 15, 17)
P-03  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md
      expected = da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7
P-04  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_2026-09-05.md
      expected = 2860fade8d34e74b8ea77d22d469fa0c9b29e05eaf27310b407a45031a626243
P-05  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v3_2026-09-05.md
      expected = 4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7
P-06  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_2026-09-05.md
      expected = bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458

RECORD (this import's own provenance)
P-07  Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v1_2026-09-05.md
      expected = adb59f60e7c1a72b6e901b86d1958a874f09c1301003b32c4884816fe43ab792
P-08  Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v2_2026-09-05.md   (this prompt; observed hash only)
P-09  f3_step1_custody_import_endoftask_report_2026-09-05.md  → p_konum_plus/provenance/
      expected = 9d79ec5697e897d90ce88d663354e8bd2a3453cf77f990c21a9fb7b80801df23
      (skip with "already at target" if present and EXACT)
```

# 3. Required response

| item | canonical target path | expected SHA256 | observed SHA256 at target | result |
|---|---|---|---|---|

```text
REQUIRED P-01, P-02 = EXACT / STOP
existing files modified = 0 ; Downloads copies untouched = true ; commit = false
next action = dispatch Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
              UNCHANGED from p_konum_plus/prompts/ ; the freeze record's execution_prompt field
              then cites that repository path
```

Final classification vocabulary only: `global blocker` / `gate-specific blocker` / `cleanup` /
`informational`.
