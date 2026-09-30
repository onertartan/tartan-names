# p_konum_plus — F3 STEP-2 r3 — PI dispatch record — 2026-09-22

> Bu kayıt TEMPLATE v2'den, PI'nın 2026-09-22 tarihli talimatıyla ("Aşağıdakileri sen yap") Claude tarafından
> dolduruldu. Her değerin dayanağı yanında yazılıdır. Kayıt PI'ya aittir; dispatch'ten önce her değer
> değiştirilebilir. İçine kendi hash'i yazılmaz; hash'i ayrı bir `.sha256` dosyasında durur.

```text
record                = f3_step2_r3_pi_dispatch_record_2026-09-22.md
record_class          = PI-owned dispatch record (dispatch-class custody item D-4 of the r3 prompt DRAFT v2)
template              = f3_step2_r3_pi_dispatch_record_TEMPLATE_v2.md
                        409b3b991e1ccd46fb5abf4e25f18a5257a991f9da7d768694c826979c3f24af
PI                    = Öner
date_time_local       = 2026-09-22 10:53, UTC+3
prepared_by           = filled in by Claude (Cowork session) at the PI's written instruction of 2026-09-22 in
                        that session. Claude also drafted the r3 prompt and will be the independent auditor of
                        the package that returns (prior exposure disclosed in the prompt header). No value below
                        is a scientific choice of Claude's; each value states its basis
what_this_record_is   = the PI's instruction to Claude Code to execute ONE prompt file, identified by name and
                        SHA256, with the PI fields that prompt asks for. It is the P-4 reference that the
                        PI-ratified content file (§10) says must exist outside that file
what_this_record_is_not = not a qualification, not an acceptance of any audit record, not a scientific approval
                        of anything in the prompt, not a change to any frozen or ratified text
```

## 1. The dispatched instrument

```text
file_name             = Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
sha256_expected       = 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
                        (computed by the drafter on the file delivered with the template; informational)
sha256_computed_by_PI = 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
values_equal          = YES
how_computed          = computed FOR the PI, not by the PI: sha256sum (GNU coreutils 9.4), run by Claude in
                        the Cowork session on the delivered file on 2026-09-22, at the PI's instruction; not
                        recomputed on the PI's machine. If the file changes on its way to Claude Code, the
                        executor's P-4 check (observed hash = this value) fails and it stops before writing
                        anything
parent_instrument     = Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
                        17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
                        (unchanged; part of the instruction, as the r3 prompt says)
```

## 2. PI-ratified content — carried unchanged

```text
file                  = f3_step2_pi_ratified_content_2026-09-07.md
sha256                = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
statement             = The seven values recorded in that file stand unchanged for the r3 cycle:
                        S-1 = (a) ; S-2 = α ; T-1 = AUTHORIZE ; T-2 = T-2a ; T-3 = AUTHORIZE ; T-4 = T-4a ;
                        T-5 = CONFIRM_WITHIN_SCOPE.
confirmed             = YES
basis (informational) = the PI's statement of 2026-09-21: "Frozen v11, F2 FREEZE, F3 STEP-1 ve mevcut ratified
                        PI kararları korunacak."; entered at the PI's instruction of 2026-09-22
```

## 3. The two PI fields of the r3 cycle (prompt §5)

```text
S-R2-1  (MANDATORY)
        value = DEFERRED_THIS_CYCLE
        rule text, ONLY if the value is PI_RULE (verbatim; it will be implemented word for word):
        not applicable
        basis (informational; not a rule text): the PI's instruction of 2026-09-21: "S-R2-1 için benim adıma
        seçim yapma. Bu kararın gerektiği bağlamları PENDING bırak; bağımsız düzeltme ve testlere devam et."
        DEFERRED_THIS_CYCLE is the value that decides nothing: the scientific question stays with the PI for
        a later cycle. Entered at the PI's instruction of 2026-09-22 to fill this field

T-R2-2  (OPTIONAL)
        value = AUTHORIZE_RESTART
        basis (informational): the PI's value of 2026-09-21 ("PI tercihim: T-R2-2 = AUTHORIZE_RESTART"), kept.
        With S-R2-1 deferred, the cycle ends PARTIAL_PENDING_PI whatever this value is (v6 §13), so
        NOT_AUTHORIZED would not change the end status
```

## 4. What `read_and_accepted` covers

```text
The r3 prompt lists in its §12 B eleven engineering and test-design choices made by its drafter (they are not
S / T options). YES accepts those eleven as part of the instruction, and nothing else. It accepts no scientific
reading: the readings the prompt applies are mapped to their binding sources in its §6.1 and §12 A, and the one
open scientific question is S-R2-1 (§3 above).
read_and_accepted     = YES
basis (informational) = entered at the PI's instruction of 2026-09-22. The eleven choices were written by the
                        same drafter who entered this value; the basis of the acceptance is the PI's
                        instruction, not a review by the drafter
```

## 5. What is handed over to Claude Code

```text
MANDATORY — without these the executor stops before it starts (prompt §2.3, §3):
  1. the prompt file of §1, byte-unchanged
  2. this record (with its sidecar)
  3. prompt v6 (17187d31…) and the content file (da0c4064…): in p_konum_plus/prompts/, or handed over
     byte-exact with the dispatch

ALREADY IN THE REPOSITORY — checked by hash, not attachments (prompt §2.1, §2.2): the frozen upstream files,
  the r1 package and the r2 package R-01 … R-10. A file that is missing or differs from its printed hash stops
  the executor. A missing sidecar does not stop it: it is recorded and created (the file itself is still
  checked)

OPTIONAL — record-class; their absence is never a STOP (prompt §2.4):
  none recorded in this record
```

## 6. Optional — statement about the r2 dispatch (audit register item T-R2-1)

```text
made      = not made
```

## 7. End state

```text
decisions_in_this_record   = S-R2-1 = DEFERRED_THIS_CYCLE ; T-R2-2 = AUTHORIZE_RESTART ; read_and_accepted = YES
                             for the list of prompt §12 B
expected status            = PARTIAL_PENDING_PI by v6 §13 (S-R2-1 in deferred_decisions, T-R2-2 in
                             narrowed_evidence), whatever the engineering outcome
nothing_else_is_instructed = true
F2 = CLOSED ; F3_STEP1 = FROZEN ; F3_STEP2 = QUALIFIED is NOT declared by this record
F3_EXECUTION_READY = false ; commit = false
```
