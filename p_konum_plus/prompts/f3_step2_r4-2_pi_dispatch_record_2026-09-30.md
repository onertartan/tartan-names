# p_konum_plus — F3 STEP-2 r4-2 — PI dispatch record — 2026-09-30

> Bu kayıt D-6'nın (f3_step2_r4-1_pi_dispatch_record_2026-09-29.md, a92a0518…) child'ıdır. PI'nın 2026-09-30
> tarihli talimatıyla ("bu maddeler için Claude Code talimatını hazırla" ve aynı oturumdaki iki seçim) Claude
> tarafından dolduruldu. Her değerin dayanağı yanında yazılıdır. Kayıt PI'ya aittir; dispatch'ten önce her değer
> değiştirilebilir (bir değer değişirse sidecar yeniden hesaplanır). İçine kendi hash'i yazılmaz; hash'i ayrı bir
> `.sha256` dosyasında durur.

```text
record                = f3_step2_r4-2_pi_dispatch_record_2026-09-30.md
record_class          = PI-owned dispatch record for the r4-2 correction revision inside the r4 cycle
                        (dispatch-class custody item; child of D-6
                        a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0)
PI                    = Öner
date_time_local       = 2026-09-30, UTC+3
prepared_by           = filled in by Claude (Cowork session; configured model identifier claude-opus-5-5) at the
                        PI's instruction of 2026-09-30. Claude drafted D-3 and the r4, r4-1 and r4-2 instructions,
                        filled D-4 … D-6, wrote the r3, r4 and r4-1 audits and will audit the r4-2 package (prior
                        exposure disclosed). The scope of §3 is the PI's (two selections made in the Cowork
                        session on 2026-09-30 from options Claude presented); the form of §3 follows the PI's
                        request read with the form the PI chose for r4-1 and may be changed before dispatch
what_this_record_is   = the PI's instruction to Claude Code to execute the r4-2 instruction, identified by name and
                        SHA256, under the standing instruments and the PI fields of D-5, which are carried
                        unchanged. It is the P-4 reference for this revision and the value end_state
                        PI_dispatch_record_hash must carry (r4-2 instruction §3 R41A-03)
what_this_record_is_not = not a qualification, not an acceptance of any audit record, not a scientific approval,
                        not a decision on the narrowed evidence of T-R2-2 or on the row A.5 (iii), not a change to
                        any frozen or ratified text or to S-R2-1, not a retroactive change to the r3, r4 or r4-1
                        packages or to any audit record
```

## 1. The dispatched instrument

```text
r4-2 instruction (child of the r4-1 instruction)
file_name             = Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
sha256_expected       = d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe
how_computed          = computed FOR the PI, not by the PI: sha256sum (GNU coreutils), run by Claude in the
                        Cowork session on the delivered file on 2026-09-30. If the file changes on its way to
                        Claude Code, the executor's precondition check fails and it stops before writing anything
standing instruments  = r4-1 instruction 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330
                        r4 instruction   e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387
                        D-3              5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
                        D-1 (v6)         17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
                        D-2              da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
                        D-5              0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
                        D-6              a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0
                        (all unchanged)
input, not directive  = r4-1 audit DRAFT r1 (A-4)
                        ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82
```

## 2. PI fields — carried unchanged from D-5 (through D-6)

```text
S-R2-1                = PI_RULE with the rule text of D-5 §3, unchanged; the PI_RATIFIED tag keeps citing D-5
T-R2-2                = AUTHORIZE_RESTART, unchanged
PI-ratified content   = D-2, the seven values unchanged
read_and_accepted     = YES for the list of D-3 §12 B, as in D-5 §4
```

## 3. The PI's choices for this revision (2026-09-30)

```text
scope                 = the six cleanup findings of A-4: R41A-01, R41A-02, R41A-03, R41A-04, R41A-05, R41A-06.
                        R41A-08 (optional) is not applied
                        basis (informational): the PI's selections "6 temizlik maddesinin hepsi (Önerilen)" and
                        "Hayır, dışarıda kalsın (Önerilen)"
form                  = a second correction revision inside the r4 cycle, deliverables tagged r4-2; no new draft
                        cycle; a code change and a full re-run are required (R41A-01, R41A-03)
                        basis (informational): the PI's request "bu maddeler için Claude Code talimatını hazırla",
                        read with the form chosen for r4-1 (D-6 §3) and the PI's instruction of 2026-09-24
                        ("Yeni taslak döngüsü açmadan mevcut kapsam içindeki düzeltmeleri ve doğrulamaları
                        tamamla.")
drafter choices       = the r4-2 instruction adds engineering choices of its drafter, none a scientific value:
                        (1) the real-path evidence for R41A-01 is a unit test with TEST_ONLY stubs of the two fit
                        engines (T-SPL-PENDING-REALPATH), not a manifest fixture; (2) when a sex has both a natural
                        and an injected pending event, F3-STEP2-EXACT-04 is used; (3) non-regression against r4-1
                        with no whitelist, expecting the RUN1 canonical document and the residual series unchanged;
                        (4) the generator and the manifest are reused unchanged, not copied; (5) custody files and
                        launch logs get attempt- and launch-numbered names; (6) the auditor folder is also delivered
                        as one zip, for transport only.
                        accepted_with_this_record = YES
```

## 4. What is handed over to Claude Code

```text
MANDATORY — without these the executor stops before it starts:
  1. the r4-2 instruction (d6680338…) with its sidecar
  2. this record with its sidecar
  3. the r4-1 audit DRAFT r1 (ad222936…) with its sidecar — input, not directive

ALREADY IN THE REPOSITORY — checked by hash, not attachments: the r4-1 instruction, D-6, D-5, the r4 instruction,
  D-3, v6, D-2, the frozen upstream files, the r3, r4 and r4-1 packages. A file that is missing or differs from its
  printed hash stops the executor. A missing sidecar does not stop it: it is recorded and created
```

## 5. End state

```text
decisions_in_this_record   = scope and form of §3 ; nothing else. S-R2-1 and T-R2-2 as in D-5
not_decided_here           = whether the narrowed evidence of T-R2-2 is acceptable ; whether the uncovered row
                             "A.5 (iii) inadmissible refit" is accepted as a recorded limitation (PI decisions,
                             open)
expected status            = PARTIAL_PENDING_PI (T-R2-2 in narrowed_evidence; the coverage row
                             "A.5 (iii) inadmissible refit" uncovered)
nothing_else_is_instructed = true
F2 = CLOSED ; F3_STEP1 = FROZEN ; F3_STEP2 = QUALIFIED is NOT declared by this record
F3_EXECUTION_READY = false ; commit = false
```
