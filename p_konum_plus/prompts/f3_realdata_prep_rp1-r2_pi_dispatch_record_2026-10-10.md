# p_konum_plus — F3 real-data preparation rp1-r2 — PI dispatch record (D-13) — 2026-10-10

> Child of D-12 and D-9; governed by D-11 r1 and its Ek-1 r1. Prepared by Claude (Claude Code cloud session) at the
> PI's request of 2026-10-10. The record is the PI's; every value may be changed before signature, and the sidecar
> is then recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-10 (§5); PI-b = B.**

```text
record                = f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md   (D-13)
drafts                = f3_realdata_prep_rp1-r2_pi_dispatch_record_DRAFT_r1_2026-10-10.md
                        ad10eb7cbd0482bc48f3fa0348bbfba0dfd7a82596f2d69040896bde03f88bb8 ;
                        f3_realdata_prep_rp1-r2_pi_dispatch_record_DRAFT_2026-10-10.md
                        d461d4da68eac44c828d92300de82b8119cda91bcbc1dc4833938f08b405cfe2
status                = SIGNED (PI approval, 2026-10-10; §5)
record_class          = PI-owned dispatch record for the second rp1 B-correction cycle rp1-r2
parent                = D-12 f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md  2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364
PI                    = Öner
what_this_record_is   = the PI's instruction to Claude Code to execute the rp1-r2 instruction (named by SHA256);
                        the PI's confirmation of the audit's B findings; the PI's choice of the F1 reproduction
                        gate form
what_this_record_is_not = not a real-data authorization (real_data_access stays false); not a binding of any bytes
                        under D-9 §2 (a); not QUALIFIED; not F3_EXECUTION_READY; not a change to any frozen text
```

## 1. The dispatched instrument

```text
file_name        = Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
sha256_expected  = bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5
note             = dispatched under this name and these bytes; the PI's signature of §5 makes it the final
                   instruction. If the instruction changes after review, this field is recomputed before signature
standing         = D-11 r1 0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639 ; Ek-1 r1 4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955 ;
                   D-12 and every instrument it lists as standing (unchanged)
input, not directive = rp1-r1 independent audit (GPT-6 / Codex) f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913 ;
                   rp1-r1 audit instruction r2 82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e
```

## 2. PI decisions

```text
PI-a  B confirmation   = IR1-02, IR1-03, IR1-04, IR1-05, IR1-06, IR1-07, IR1-12, IR1-13 are B
                         (D-11 r1 §5 (iii)), as the audit classed them; no class is lowered.
                         basis: PI, 2026-10-10, verbatim: «8 B bulgusunu kabul ediyorum; rp1-r2 talimatını ve
                         D-13'ü hazırla.»
                         This is the second B-correction cycle of rp1: a new B after it goes to the PI before any
                         further round (D-11 r1 §6)
PI-b  F1 reproduction  = B  CONTENT_RE-DERIVATION (PI's choice, 2026-10-10; §5). The options as presented:
      gate form          B  CONTENT_RE-DERIVATION (recommended): at real-data step 1 the frozen eligible manifest
                            is verified against its frozen hash, parsed with the F1 freeze record §7 field list,
                            and every field the frozen rule defines is re-derived from the verified raw files and
                            compared field by field; any difference STOPs. Fields the freeze record does not define
                            are verified by the custody hash only
                         A  BYTE_EXACT_RE-SERIALIZATION: kept as in rp1 C-3; the PI names every serialization value
                            (header, delimiter, quoting, line ending, value spellings of every field) in this record;
                            without them the executor STOPs
                         reason for the choice: the freeze record names fields, ordering, row counts and hash but
                         not the serialization, and no generator script is in the repository. Byte-level identity
                         of the frozen file is already guaranteed by its hash; B adds a field-level check of the
                         re-derived content without guessing a format
carried               = D-12 PI-b (family in real-mode ids), PI-c (consumer scope; rp1-r2 Q1 and Q2 lie inside
                         it); T-RP-1, S-c (child of the rp1-r1 harness), S-e, S-f from D-10
```

## 3. What is handed over to Claude Code

```text
MANDATORY: the rp1-r2 instruction with its sidecar ; this record (signed) with its sidecar ; the rp1-r1 audit
  record and the rp1-r1 audit instruction r2, each with a sidecar, to be placed in p_konum_plus/prompts/
  unchanged (inputs, not directives)
ALREADY IN THE REPOSITORY (checked by hash): D-11 r1, Ek-1 r1, D-12, D-9, the rp1 and rp1-r1 packages
```

## 4. End state

```text
decisions_in_this_record = §2 ; nothing else
F3_STEP2 = QUALIFIED (D-9, unchanged) ; no rp1 / rp1-r1 bytes bound ; rp1-r2 bytes bound only after their
  independent audit, by one line in the dependent package's dispatch record
real_data_access = false ; F3_EXECUTION_READY = false ; commit = false
```

## 5. Signature

```text
PI                    = Öner
PI-b choice           = B  CONTENT_RE-DERIVATION
signature / approval  = APPROVED. The PI's message of 2026-10-10, verbatim:
                        «PI-b için B’yi seçiyorum. D-13'ü onaylıyorum.»
                        The approved content is DRAFT r1 (named in the header) with PI-b = B; this final text differs
                        from it only in the title, the header lines, the PI-b line and §5 (§7). This final text was
                        delivered to the PI; the PI's forwarding it to the executor adopts it
date_time_local       = 2026-10-10, UTC+3
```

## 6. Hashes (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
d9a5e9905e25c634ad3132aae85c6c346e5ead30	refs/heads/p_konum_plus
$ sha256sum <files; repository files from the git archive of 9035df0 unless noted>
2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364  prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md
bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5  Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md (origin/p_konum_plus)
f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913  f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md (as uploaded)
82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e  F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md
```

## 7. Changes from DRAFT r1 (ad10eb7c…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, header | DRAFT r1 → signed; file name without DRAFT; drafts and status lines | PI approval |
| 2 | §2 PI-b | B CONTENT_RE-DERIVATION recorded as chosen; both options kept as presented | PI's choice |
| 3 | §5 | PI-b choice, approval message verbatim, date | PI approval |

No other change: §1 (instruction DRAFT r1, bf53e1e9…), PI-a, §3, §4 and §6 stand as in DRAFT r1.
