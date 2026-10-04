# p_konum_plus — F3 real-data preparation rp1 — PI dispatch record (D-10) — 2026-10-02

> Child of D-9 (`f3_step2_qualification_pi_decision_record_2026-10-02.md`, `1ab17e44…`). Prepared by Claude
> (Claude Code cloud session) at the PI's request of 2026-10-02. The record is the PI's; every value may be changed
> before dispatch, and the sidecar is then recomputed. It carries no hash of itself. **Signed by the PI's approval
> of 2026-10-02 (§5).** All four PI fields of §2 are the PI's (2026-10-02).

```text
record                = f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md   (D-10)
drafts                = f3_realdata_prep_rp1_pi_dispatch_record_DRAFT_r1_2026-10-02.md
                        b4758c1e2b73bca4f7ccf7c2125d556462afd44f75a80d682c3407076bff3819 ; DRAFT b7ef5125… (unchanged)
status                = SIGNED (PI approval, 2026-10-02; §5)
record_class          = PI-owned dispatch record for the F3 real-data preparation cycle rp1 (dispatch-class custody
                        item; child of D-9 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3)
PI                    = Öner
what_this_record_is   = the PI's instruction to Claude Code to execute the rp1 instruction, identified by name and
                        SHA256, with the PI fields of §2; the P-4 reference of this cycle
what_this_record_is_not = not a real-data authorization (real_data_access stays false); not QUALIFIED for any new
                        bytes; not F3_EXECUTION_READY; not a change to D-1 … D-9 or any frozen text; not a 6B
                        specification
```

## 1. The dispatched instrument

```text
file_name        = Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
sha256_expected  = a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5
how_computed     = sha256sum, run by Claude in the cloud session on the delivered file on 2026-10-02 (§6). If
                   the file changes on its way to Claude Code, the precondition check fails and the executor
                   stops before writing anything
standing         = D-9 1ab17e44… ; D-8 aadf2840… ; D-3 5b0e19ea… ; D-1 17187d31… ; D-2 da0c4064… ;
                   r4-2 instruction d6680338… (all unchanged)
input, not directive = A-5 9111bc71…
```

## 2. PI fields

```text
T-RP-1  restart layer       = ACTIVE_FROM_START
                              basis: PI, 2026-10-02 ("sıradaki işlerdeki 2 ve 3. adımları senin önerdiğin gibi
                              onaylıyorum"; S-b: layer used, R42A-03 closed). Replaces for rp1 only D-3 §8.3
                              "Attempt 1 runs without it"; T-RP-1 enters narrowed_evidence by value
S-c     code form           = CHILD_HARNESS_OF_R4-2
                              basis: PI, 2026-10-02 (S-c). Bound by D-9 §2 (a): non-regression against r4-2 and
                              an independent audit before the bytes count as qualified
S-e     F1 loader validation = SYNTHETIC_ONLY_IN_RP1
                              basis: PI, 2026-10-02 ("S-e — Yalnız yapay"). rp1 tests the F1 pipeline only on
                              generated raw-format files; real_data_access stays false; the byte-exact
                              reproduction of the F1 manifest (8a6034eb…, 906 rows) is step 1 of the later
                              real-data execution cycle, which needs its own PI authorization (D-8 §3)
S-f     6B implementation   = EXCLUDED_FROM_RP1
                              basis: PI, 2026-10-02 ("S-f — 6B rp1'e girmesin"). No 6B code in rp1; after the 6B
                              specification is ratified, a narrow child (rp2) adds it under D-9 §2 (a)
                              (non-regression + audit)
```

## 3. What is handed over to Claude Code

```text
MANDATORY: the rp1 instruction with its sidecar ; this record (signed) with its sidecar
ALREADY IN THE REPOSITORY (checked by hash): D-9 (committed at fadf771), D-8, A-5, D-3, D-1, D-2, the r4-2
  instruction, the r4-2 package and every earlier package, the F1 freeze record
```

## 4. End state

```text
decisions_in_this_record  = §2 ; nothing else
F3_STEP2 = QUALIFIED (D-9, unchanged) ; rp1 bytes not qualified until audited and bound by a PI record
real_data_access = false ; F3_EXECUTION_READY = false ;
commit = false
```

## 5. Signature

```text
PI                    = Öner
signature / approval  = APPROVED. The PI's message of 2026-10-02, verbatim:
                        «Push bitti. D-10'u onaylıyorum»
                        The approved content is DRAFT r1 (b4758c1e…) with the four fields of §2; the final text
                        differs from it only in the title and in §1, §3, §5 and §6 (§7). This final text was
                        delivered to the PI; the PI's forwarding it to the executor adopts it
date_time_local       = 2026-10-02, UTC+3
```

## 6. Hashes (computed in this session; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
fadf771c75396a0d242f75f0c3ce7f3f0f4ed7e7	refs/heads/p_konum_plus
$ git show origin/p_konum_plus:p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md | sha256sum
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  -
$ sha256sum Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5  Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
```

## 7. Changes from DRAFT r1 (b4758c1e…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, header | DRAFT r1 → signed; drafts and status lines | PI approval |
| 2 | §1 | final instruction file name and SHA256 | P-4 reference |
| 3 | §3 | D-9 committed at fadf771 | push verified (§6) |
| 4 | §5 | approval message verbatim, date | PI approval |
