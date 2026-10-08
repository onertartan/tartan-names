# p_konum_plus — F3 real-data preparation rp1-r1 — PI dispatch record (D-12) — 2026-10-05

> Child of D-10 (`f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md`, `4c89577b…`) and D-9 (`1ab17e44…`);
> governed by D-11 r1 (`0b177ee4…`). Prepared by Claude (Claude Code cloud session) at the PI's request of
> 2026-10-05. The record is the PI's; every value may be changed before signature, and the sidecar is then
> recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-05 (§5).**

```text
record                = f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md   (D-12)
draft                 = f3_realdata_prep_rp1-r1_pi_dispatch_record_DRAFT_2026-10-05.md
                        e771d58a3a6663321efc6098f93f45b60dd6fe1862f8589585ad37fc1b1d1831
status                = SIGNED (PI approval, 2026-10-05; §5)
record_class          = PI-owned dispatch record for the rp1 B-correction cycle rp1-r1 (dispatch-class custody item;
                        child of D-10 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34)
PI                    = Öner
what_this_record_is   = the PI's instruction to Claude Code to execute the rp1-r1 instruction, identified by name and
                        SHA256; the PI decisions PI-a … PI-d; the B confirmation D-11 r1 §5 asks the PI for
what_this_record_is_not = not a real-data authorization (real_data_access stays false); not a binding of any bytes
                        under D-9 §2 (a) (neither rp1's nor rp1-r1's); not QUALIFIED for new bytes; not
                        F3_EXECUTION_READY; not a change to D-1 … D-11 r1 or any frozen text; not a 6B specification
```

## 1. The dispatched instrument

```text
file_name        = Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
sha256_expected  = 2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d
note             = dispatched under this name and these bytes, without renaming: the PI's signature of §5 makes
                   DRAFT r2 the final instruction (no second hash for a title change)
how_computed     = sha256sum, run by Claude in the cloud session on 2026-10-05 (§6). If the file changes on its way
                   to Claude Code, the precondition check fails and the executor stops before writing anything
standing         = D-11 r1 0b177ee4… ; D-10 4c89577b… ; D-9 1ab17e44… ; rp1 instruction a57b6fca… ; and every
                   instrument the rp1 instruction lists as standing (unchanged)
input, not directive = rp1 independent audit (GPT Codex) 2fa28e2a… ; review of the rp1-r1 DRAFT (GPT Codex)
                   aa9fcaa9… and the same reviewer's second note (PI's message of 2026-10-05; instruction §14)
```

## 2. PI decisions

```text
PI-a  B classification   = RP1A-01, RP1A-02, RP1A-03 are B (D-11 r1 §5 (iii)); first B correction of rp1
PI-b  C-4 reading        = family is part of every real-mode (fixture_id, mask_id); synthetic-path ids unchanged
PI-c  consumer change    = run_real_scenario changes only where it takes a scenario's trajectory and mask ids
                           (real_x / real_mask_ids if present; otherwise the r4-2 path unchanged); nothing else in
                           the evaluator changes
PI-d  ride-along         = RP1A-04 and RP1A-06 close in this package
basis (all four)         = PI, 2026-10-05: «benim vermem kararlar için önerilerini kabul ediyorum: rp1-r1
                           talimatını hazırla»
carried over from D-10   = T-RP-1 ACTIVE_FROM_START ; S-e SYNTHETIC_ONLY ; S-f 6B EXCLUDED. S-c reads for rp1-r1:
                           child harness of the rp1 harness 39c733a3… (itself the child of r4-2 b988e962…);
                           non-regression stays against r4-2
```

## 3. What is handed over to Claude Code

```text
MANDATORY: the rp1-r1 instruction (DRAFT r2) with its sidecar ; this record (signed) with its sidecar ;
  the rp1 independent audit record and the review of the rp1-r1 DRAFT, each with a sidecar, to be placed in
  p_konum_plus/prompts/ unchanged (inputs, not directives)
ALREADY IN THE REPOSITORY (checked by hash): D-11 r1, D-10, D-9 and the rp1 package at b6d2483
```

## 4. End state

```text
decisions_in_this_record = §2 ; nothing else
F3_STEP2 = QUALIFIED (D-9, unchanged) ; rp1 bytes NOT bound ; rp1-r1 bytes bound only after their independent audit,
  by one line in the dispatch record of the dependent package (D-11 r1 §6)
real_data_access = false ; F3_EXECUTION_READY = false ; commit = false
```

## 5. Signature

```text
PI                    = Öner
signature / approval  = APPROVED. The PI's message of 2026-10-05, verbatim:
                        «D-12'yi onaylıyorum»
                        The approved content is the DRAFT named in the header; this final text differs from it
                        only in the title, the header lines and §5 (§7). This final text was delivered to the PI;
                        the PI's forwarding it to the executor adopts it
date_time_local       = 2026-10-05, UTC+3
```

## 6. Hashes (computed in this session; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
b6d2483d4bbd991167bb633d8d96647cc553bde2	refs/heads/p_konum_plus
$ sha256sum Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d  Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
$ sha256sum <uploaded audit record> <uploaded review>
2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989  f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md
aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef  RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md
```

## 7. Changes from the DRAFT (e771d58a…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, header | DRAFT → signed; file name without DRAFT; draft and status lines | PI approval |
| 2 | §5 | approval message verbatim, date | PI approval |

No other change: §1 (instruction DRAFT r2, 2226fc96…), §2 (PI-a … PI-d), §3, §4 and §6 stand as in the DRAFT.
