# p_konum_plus — F3 STEP-2 r4 — PI dispatch record — 2026-09-24

> Bu kayıt D-4'ün (f3_step2_r3_pi_dispatch_record_2026-09-22.md, 4e623536…) child'ıdır; TEMPLATE v2 yapısını
> korur. PI'nın 2026-09-24 tarihli talimatıyla ("buna göre Pycharm'da Claude Code'a ileteceğim dosyaları ver")
> Claude tarafından dolduruldu. Her değerin dayanağı yanında yazılıdır. Kayıt PI'ya aittir; dispatch'ten önce her
> değer değiştirilebilir (bir değer değişirse sidecar yeniden hesaplanır). İçine kendi hash'i yazılmaz; hash'i
> ayrı bir `.sha256` dosyasında durur.

```text
record                = f3_step2_r4_pi_dispatch_record_2026-09-24.md
record_class          = PI-owned dispatch record for the r4 correction cycle (dispatch-class custody item; child
                        of D-4 4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865)
template              = f3_step2_r3_pi_dispatch_record_TEMPLATE_v2.md
                        409b3b991e1ccd46fb5abf4e25f18a5257a991f9da7d768694c826979c3f24af
PI                    = Öner
date_time_local       = 2026-09-24, UTC+3
prepared_by           = filled in by Claude (Cowork session) at the PI's written instruction of 2026-09-24 in
                        that session. Claude drafted D-3 and the r4 instruction, wrote the r3 audit and will be
                        the independent auditor of the r4 package (prior exposure disclosed). The scientific
                        value of §3 (S-R2-1 = PI_RULE and its rule text) is the PI's: the PI chose PI_RULE on
                        2026-09-24; the rule text was reviewed externally and finalised in the Cowork session; the PI's
                        instruction to prepare the dispatch files is taken as approval of it (editable before
                        dispatch); Claude assembled the text
what_this_record_is   = the PI's instruction to Claude Code to execute the standing prompt D-3 together with
                        the r4 instruction file, both identified by name and SHA256, with the PI fields those
                        instruments ask for. It is the P-4 reference of D-2 §10 for this cycle and the source
                        (path and hash) that the PI_RATIFIED tag of the S-R2-1 implementation cites
what_this_record_is_not = not a qualification, not an acceptance of any audit record, not a scientific approval
                        of anything in the prompt, not a change to any frozen or ratified text, not a
                        retroactive change to the r3 package or to the r3 audit
```

## 1. The dispatched instruments

```text
standing prompt (D-3)
file_name             = Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
sha256_expected       = 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
sha256_computed_by_PI = 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
values_equal          = YES
r4 instruction (child of D-3)
file_name             = Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md
sha256_expected       = e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387
sha256_computed_by_PI = e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387
values_equal          = YES
how_computed          = computed FOR the PI, not by the PI: sha256sum (GNU coreutils 9.4), run by Claude in
                        the Cowork session on the delivered files on 2026-09-24, at the PI's instruction; not
                        recomputed on the PI's machine. If a file changes on its way to Claude Code, the
                        executor's P-4 check (observed hash = this value) fails and it stops before writing
                        anything
parent_instrument     = Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
                        17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376
                        (unchanged; part of the instruction, as D-3 says)
input, not directive  = f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md
                        11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6
                        (the r3 audit; the r4 instruction §3 adopts its closure actions; the record itself
                        decides nothing and is not rewritten)
```

## 2. PI-ratified content — carried unchanged

```text
file                  = f3_step2_pi_ratified_content_2026-09-07.md
sha256                = da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498
statement             = The seven values recorded in that file stand unchanged for the r4 cycle:
                        S-1 = (a) ; S-2 = α ; T-1 = AUTHORIZE ; T-2 = T-2a ; T-3 = AUTHORIZE ; T-4 = T-4a ;
                        T-5 = CONFIRM_WITHIN_SCOPE.
confirmed             = YES
basis (informational) = the PI's statement of 2026-09-21: "Frozen v11, F2 FREEZE, F3 STEP-1 ve mevcut ratified
                        PI kararları korunacak."; carried from D-4 at the PI's instruction of 2026-09-24
```

## 3. The two PI fields (D-3 §5)

```text
S-R2-1  (MANDATORY)
        value = PI_RULE
        basis (informational): the PI's message of 2026-09-24 ("S-R2-1 = PI_RULE"); rule text reviewed
        externally (two review notes) and finalised in the Cowork session on 2026-09-24; the PI's instruction
        to prepare the dispatch files is taken as approval of the final text (editable before dispatch)
        scope: prospective — it governs the r4 correction cycle and later runs; the r3 package (harness
        5fea165c…, results 35279164…), its DEFERRED_THIS_CYCLE wiring and the r3 audit (11cfa591…) are
        historical and are not rewritten

        rule text (verbatim; it will be implemented word for word; tagged PI_RATIFIED with the hash of this
        record):

        (1) Membership. For each sex s ∈ {F, M} and each family F ∈ {P01, P02}, the C4b paired-valid set is
            V4_s(F) = { i : pL[F,s,i] AND pR[F,s,i] AND full[F,s,i]
                            AND pL[SPL,s,i] AND pR[SPL,s,i] AND full[SPL,s,i] }
            where pL, pR are the decision-layer LEFT / RIGHT probe-success flags and full is the
            decision-layer full-data reference flag of the fitter named (P01, P02: an eligible admissible
            full-data fit under FREEZE r1; SPL: a valid full-data spline fit), exactly as recorded under the
            fields pL, pR, full and the fitter keys P01, P02, SPL. A trajectory for which a named fitter has
            no full-data reference is not a member of any V4_s whose definition names that fitter; if the
            missing reference is the spline's, it is a member of neither family's V4_s.
        (2) D-P04. The consulted common set at level C4b is U4_s = V4_s(P01) ∩ V4_s(P02), built from the same
            flags; both candidates' C4b scalars are recomputed on this same U4_s (freeze record r1 §3 items
            4.1 and 4.2). The trajectory is absent from U4_s by construction. This is a construction-time
            membership condition, not a post-construction invalidity: it never raises
            CONTRACT_VIOLATION_INCONSISTENT_U. CONTRACT_VIOLATION_EMPTY_U keeps its existing meaning. No D-P04
            common-support floor exists and no common-support failure branch exists (freeze record r1 §3
            items 4.2 and 4.3, ratified as MODIFY and NOT_APPLICABLE); under the ratified P03 completeness
            floors an empty consulted set is mathematically excluded on the real path (freeze record r1
            §4.3), and should it nevertheless occur it is a contract-consistency violation, not a scientific
            branch: STOP, provenance investigation, no automated winner, no imputation, no sentinel.
        (3) Denominators and values. n_s is retained. No imputation, sentinel, NaN-valued C4b statistic or
            numeric outcome is produced for an absent reference. After the exclusion the ratified C4b rules
            apply unchanged: the completeness floor |V4_s|/n_s >= c_complete on the reduced set; a sex-level
            statistic over an empty V4_s is undefined and follows §8.1 (C4b not passed for that sex); the
            C4b reporting rule (C4b_F,s, C4b_S,s, |V4_s|/n_s, per-side probe-failure shares) is unchanged.
        (4) Scope. C4a probe-success records, ident_F,s and their denominators are unchanged; C3 and
            CL-F3-04 are unchanged. Membership is determined from the recorded decision-layer flags on the
            real path and in the fixtures alike, never from the presence or absence of an RMSE_edge value.

        predeclared expectations under this rule (to be pinned in the r4 manifest BEFORE the run; a differing
        result is an EXPECTATION_FAIL, not a re-derivation):
          SCEN-B          M0 absent from both families' V4 in M (spline full fit fails by the declared
                          injection while both spline probes succeed); V4 empty in M; C4b undefined and not
                          passed in M for both families; both families still FAIL on their definite failures;
                          mechanism STOP_BOTH_FAIL_REDESIGN (unchanged from r3)                [D-3 §7]
          INJ-C1-FAIL     P-01: observations 0–2 outside V4 in F (C4b floor fails, in addition to C1 and the
                          C3 floor); p03 = (FAIL, PASS), first failure C1; mechanism ONLY_P02_PASSES
                          (unchanged)                                                          [D-3 §7]
          INJ-DP04-C1     P-02: V3 and V4 shares 0.9 in both sexes; p03 = (PASS, PASS); D-P04 consulted path
                          [C1]; RESOLVED at C1 for P-01; mechanism RESOLVED_MECHANISM_P01     [D-3 §7]
          INJ-C4B-NOREF   construction unchanged (equalized families; full = False at (P01, obs 0) and
                          (P02, obs 1), both sexes; pL, pR True there; spline complete): C1 coverage 0.9 /
                          0.9 for both families in both sexes; C3 share 0.9, n_valid 9; C4b share 0.9,
                          n_valid 9; every P03 criterion PASS (floors met at equality, >=); p03 =
                          (PASS, PASS); D-P04 consulted path C1 → C2 → C3 → C4a → C4b → C5 → C6, every level
                          EQUIVALENT (signed delta 0); |U2| = |U5| = 10/10, |U3| = |U4| = 8/10 per sex;
                          mechanism TERMINAL_FALLBACK_MECHANISM_P01; no stops record
                          [derived by the auditor from the rule text on a scratch copy of the r3 harness
                          with the three membership patches the rule implies; the executor derives the same
                          row from the rule text and pins it; a mismatch is a finding]

T-R2-2  (OPTIONAL)
        value = AUTHORIZE_RESTART
        basis (informational): the PI's value of 2026-09-21 ("PI tercihim: T-R2-2 = AUTHORIZE_RESTART"),
        carried from D-4. With the coverage row "A.5 (iii) inadmissible refit" uncovered, the cycle ends
        PARTIAL_PENDING_PI whatever this value is (v6 §13), as in r3; NOT_AUTHORIZED would not change the end
        status. The PI may replace the value before dispatch (then recompute the sidecar)
```

## 4. What `read_and_accepted` covers

```text
D-3 lists in its §12 B eleven engineering and test-design choices made by its drafter (they are not S / T
options). YES accepts those eleven as part of the instruction, and nothing else. The r4 instruction adds no
drafter choice of its own: its §3 quotes the closure actions of the r3 audit, its §4 applies §3 of this record.
read_and_accepted     = YES
basis (informational) = carried from D-4 at the PI's instruction of 2026-09-24
```

## 5. What is handed over to Claude Code

```text
MANDATORY — without these the executor stops before it starts (D-3 §2.3, §3; r4 instruction §1):
  1. D-3, byte-unchanged (5b0e19ea…)
  2. the r4 instruction file (e1283958…) with its sidecar
  3. this record with its sidecar
  4. the r3 audit DRAFT r1 (11cfa591…) with its sidecar — input, not directive
  5. prompt v6 (17187d31…) and the content file (da0c4064…): in p_konum_plus/prompts/, or handed over
     byte-exact with the dispatch

ALREADY IN THE REPOSITORY — checked by hash, not attachments (D-3 §2.1, §2.2): the frozen upstream files, the
  r1, r2 and r3 packages. A file that is missing or differs from its printed hash stops the executor. A missing
  sidecar does not stop it: it is recorded and created (the file itself is still checked)

OPTIONAL — record-class; their absence is never a STOP:
  the auditor's evidence zip of the r3 audit (85f6b6ae…); the S-R2-1 advisory note (add7dbb2…) — background
  only; nothing in them is implemented
```

## 6. Optional — statement about the r2 dispatch (audit register item T-R2-1)

```text
made      = not made
```

## 7. End state

```text
decisions_in_this_record   = S-R2-1 = PI_RULE with the rule text of §3 ; T-R2-2 = AUTHORIZE_RESTART ;
                             read_and_accepted = YES for the list of D-3 §12 B
expected status            = PARTIAL_PENDING_PI by v6 §13 (T-R2-2 in narrowed_evidence; the coverage row
                             "A.5 (iii) inadmissible refit" uncovered unless a fixture covers it);
                             deferred_decisions = [] ; F3-STEP2-EXACT-03 closed with this record as source
nothing_else_is_instructed = true
F2 = CLOSED ; F3_STEP1 = FROZEN ; F3_STEP2 = QUALIFIED is NOT declared by this record
F3_EXECUTION_READY = false ; commit = false
```
