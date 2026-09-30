# p_konum_plus — F3 STEP-2 r4-1 — PI dispatch record — 2026-09-29

> Bu kayıt D-5'in (f3_step2_r4_pi_dispatch_record_2026-09-24.md, 0cd87ad5…) child'ıdır. PI'nın 2026-09-29 tarihli
> talimatıyla ("şimdi Claude Code'a iletmem gerekenler ne?" ve aynı oturumdaki iki seçim) Claude tarafından
> dolduruldu. Her değerin dayanağı yanında yazılıdır. Kayıt PI'ya aittir; dispatch'ten önce her değer
> değiştirilebilir (bir değer değişirse sidecar yeniden hesaplanır). İçine kendi hash'i yazılmaz; hash'i ayrı bir
> `.sha256` dosyasında durur.

```text
record                = f3_step2_r4-1_pi_dispatch_record_2026-09-29.md
record_class          = PI-owned dispatch record for the r4-1 correction revision inside the r4 cycle
                        (dispatch-class custody item; child of D-5
                        0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851)
PI                    = Öner
date_time_local       = 2026-09-29, UTC+3
prepared_by           = filled in by Claude (Cowork session; configured model identifier claude-opus-5-5) at the
                        PI's instruction of 2026-09-29. Claude drafted D-3, the r4 instruction and the r4-1
                        instruction, filled D-4 and D-5, wrote the r3 and r4 audits and will audit the r4-1
                        package (prior exposure disclosed). The two choices of §3 are the PI's, made in the
                        Cowork session on 2026-09-29 from options Claude presented
what_this_record_is   = the PI's instruction to Claude Code to execute the r4-1 instruction, identified by name and
                        SHA256, under the standing instruments and the PI fields of D-5, which are carried
                        unchanged. It is the P-4 reference for this revision
what_this_record_is_not = not a qualification, not an acceptance of any audit record, not a scientific approval,
                        not a change to any frozen or ratified text or to S-R2-1, not a retroactive change to the
                        r3 or r4 packages or to any audit record
```

## 1. The dispatched instrument

```text
r4-1 instruction (child of the r4 instruction)
file_name             = Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md
sha256_expected       = 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330
how_computed          = computed FOR the PI, not by the PI: sha256sum (GNU coreutils), run by Claude in the
                        Cowork session on the delivered file on 2026-09-29. If the file changes on its way to
                        Claude Code, the executor's precondition check fails and it stops before writing anything
standing instruments  = r4 instruction e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387
                        D-3            5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
                        D-1 (v6)       17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
                        D-2            da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
                        (all unchanged)
inputs, not directives = r4 audit DRAFT r1 b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a
                        r4 audit DRAFT r2 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9
```

## 2. PI fields — carried unchanged from D-5

```text
S-R2-1                = PI_RULE with the rule text of D-5 §3, unchanged; the PI_RATIFIED tag keeps citing D-5
T-R2-2                = AUTHORIZE_RESTART, unchanged
PI-ratified content   = D-2, the seven values unchanged
read_and_accepted     = YES for the list of D-3 §12 B, as in D-5 §4
```

## 3. The PI's choices for this revision (2026-09-29)

```text
scope                 = the gate-specific blocker and all cleanup: R4A-01, R4A-02, R4A-03, R4A-04, R4A-10.
                        R4A-08 (optional) is not applied
                        basis (informational): the PI's selection "Blocker + tüm cleanup (Önerilen)"
form                  = a correction revision inside the r4 cycle, deliverables tagged r4-1; no new draft cycle
                        basis (informational): the PI's selection "r4 içinde düzeltme revizyonu (Önerilen)",
                        consistent with the PI's instruction of 2026-09-24 ("Yeni taslak döngüsü açmadan mevcut
                        kapsam içindeki düzeltmeleri ve doğrulamaları tamamla.")
drafter choices       = the r4-1 instruction adds three engineering choices of its drafter, none a scientific
                        value: (1) a pending spline context propagates exactly as the A.5 reference violation
                        (a5v) already does; (2) the R4A-01 fixtures cover all three spline contexts (full, fold,
                        probe); (3) affected quarantine files are annotated by a note, never renamed.
                        accepted_with_this_record = YES
```

## 4. What is handed over to Claude Code

```text
MANDATORY — without these the executor stops before it starts:
  1. the r4-1 instruction (283ac4e2…) with its sidecar
  2. this record with its sidecar
  3. the r4 audit DRAFT r1 (b7217027…) and DRAFT r2 (9c16abb5…) with their sidecars — inputs, not directives

ALREADY IN THE REPOSITORY — checked by hash, not attachments: the r4 instruction, D-5, D-3, v6, D-2, the frozen
  upstream files, the r3 and r4 packages. A file that is missing or differs from its printed hash stops the
  executor. A missing sidecar does not stop it: it is recorded and created
```

## 5. End state

```text
decisions_in_this_record   = scope and form of §3 ; nothing else. S-R2-1 and T-R2-2 as in D-5
expected status            = PARTIAL_PENDING_PI (T-R2-2 in narrowed_evidence; the coverage row
                             "A.5 (iii) inadmissible refit" uncovered unless a fixture covers it)
nothing_else_is_instructed = true
F2 = CLOSED ; F3_STEP1 = FROZEN ; F3_STEP2 = QUALIFIED is NOT declared by this record
F3_EXECUTION_READY = false ; commit = false
```
