# p_konum_plus — F3 real-data preparation rp1-r1 — Start-State Inventory (deliverable 11)

```text
artifact_role = start-state inventory for the rp1-r1 B-correction cycle (rp1-r1 instruction §3);
                taken before the first rp1-r1 write; carries the FIRST ledger (D-11 r1 §7)
status        = NON-NORMATIVE
date          = 2026-10-05
revision      = rp1-r1 (B-correction cycle of rp1, inside the r4 lineage; D-11 r1 governs)
```

## 0. Process-error disclosure (before §1 was fully verified)

Before the §1 preconditions were completely re-verified (specifically, before the PI delivered the
two "input, not directive" files §1 item 2 requires — the rp1 independent audit (GPT Codex,
`2fa28e2a…`) and the review of the rp1-r1 DRAFT (GPT Codex, `aa9fcaa9…`)), the executor copied
`p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py` to
`p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py` (created 2026-10-05, local
machine time ~19:54; content byte-identical to the rp1 harness,
`39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09` — no R-1…R-5 edit had yet been
made). This was a precondition-discipline error (D-11 r1 §3: "düzeltme ve doğrulama ayrı bir
pakette ya da aynı paketin hazırlık aşamasında yapılabilir [ama] madde, bağımlı hesaplama başlamadan
önce kapanır" — and more directly, no write precedes a completed §1). Per the PI's instruction, the
copy was deleted before any further action; nothing was computed, keyed, or derived from it, and no
other file was touched while it existed. Disclosed here and in the attempt log.

## 1. §1 preconditions — full re-verification (after the two input files arrived)

All five items of the rp1-r1 instruction §1, verified by this inventory's own commands:

```text
1. D-12 (f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md) OBSERVED = SIDECAR =
   2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364; every PI field of §2
   (PI-a, PI-b, PI-c, PI-d) is filled with an explicit value, none blank or template residue.
   The instrument it names, Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md,
   OBSERVED = SIDECAR = D-12 §1's pinned value =
   2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d
2. standing instruments, OBSERVED = pinned value in both D-12 and the rp1-r1 instruction:
   D-11 r1   0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639
   D-9       1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3
   D-10      4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34
   rp1 instr a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5
   audit (GPT Codex)  2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989
     (placed p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md,
      sidecar re-verified in place: OK)
   review (GPT Codex)  aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef
     (placed p_konum_plus/prompts/RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md,
      sidecar re-verified in place: OK)
3. every file of the rp1 transmission list (858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9):
   43/43 table rows re-hashed from disk -- OBSERVED = printed-in-list value = sidecar value, for
   every row, 0 mismatches, 0 missing sidecars (checked programmatically, not spot-checked).
   rp1 harness OBSERVED = 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09
4. r4-2 baselines, OBSERVED = pinned:
   results   f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba
   telemetry ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d
   test evid c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf
5. frozen upstream (rp1 instruction §1 item 4 = D-3 §2.1 items 1-11 + F1 freeze record), all 11 files
   re-hashed from disk, OBSERVED = pinned, 0 mismatches:
   v11 d136502f… ; F2 gen spec FINAL FREEZE r1 ee2cb99d… ; F2 engine 01714752… ;
   F2 fixture manifest daa5fd08… ; F2 start-grid manifest c39fb519… ; F2 exact-init packet 8ff70a64… ;
   F2 feasibility telemetry cd7218b1… ; F3 STEP-1 r1 candidate 5e594136… ; F3 STEP-1 freeze r1 7055f186… ;
   F3 STEP-1 freeze (parent) bef216e3… ; spline harness r2 b31e5a6b… ; F1 freeze record 5eceb198…
```

**ALL PASS. No STOP. §1 fully satisfied; R-1…R-5 may begin.**

## 2. (b) D-11 r1, D-12 and the audit record, hashes as found

| instrument | path | sha256 (as found) |
|---|---|---|
| D-11 r1 | p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md | 0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639 |
| D-12 | p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md | 2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364 |
| rp1-r1 instruction (DRAFT r2, final by D-12 signature) | p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md | 2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d |
| rp1 independent audit (GPT Codex) | p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md | 2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989 |
| review of rp1-r1 DRAFT (GPT Codex) | p_konum_plus/prompts/RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md | aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef |

D-12's hash re-computed against its own sidecar: OK (matches `2c23130d…` exactly).

## 3. (a) rp1 deliverables re-verified against the rp1 transmission list

43/43 EQUAL (see §1 item 3 above for the method). No DIFFERENT, no MISSING. The rp1 package at
commit `b6d2483` is confirmed byte-identical to what it claims to be.

## 4. (c) LEDGER — first ledger (D-11 r1 §7)

Opened per D-11 r1 §7: "the first ledger opens in the first package's inventory after the rp1
audit, with whatever K and T items are open at that time." Source for every row below is named;
items the rp1 independent audit (GPT Codex, `2fa28e2a…`) raised carry both labels (v6/A-5 vocabulary
and the D-11 r1 class D-12 §9 assigns). No item below is UNCLASSIFIED; none required a STOP-report.

| id | source | class (D-11 r1 / v6) | closure point | status | closing package | evidence |
|---|---|---|---|---|---|---|
| RP1A-01 | rp1 audit 2fa28e2a…, finding RP1A-01 | HESAPLAMA (D-12 §9: R-1); B under D-11 r1 §5(iii) per PI-a | this package (R-1), CLOSED only by the independent audit | OPEN → IMPLEMENTED_PENDING_VERIFICATION once R-1 lands | rp1-r1 | T-F1-HANDOFF-SYNTH, T-CONTEXT-ID-UNIQUE, T-F1-CONTRACT-GAP RAN/PASSED |
| RP1A-02 | rp1 audit, finding RP1A-02 | HESAPLAMA (R-2); B per PI-a | this package (R-2), audit-closed | OPEN → IMPLEMENTED_PENDING_VERIFICATION | rp1-r1 | T-F1-LOADER-SYNTH full-branch cases RAN/PASSED |
| RP1A-03 | rp1 audit, finding RP1A-03 | HESAPLAMA (R-3); B per PI-a | this package (R-3), audit-closed | OPEN → IMPLEMENTED_PENDING_VERIFICATION | rp1-r1 | T-NONREG-R4-2 full-depth, 0 U, every declared E held |
| RP1A-04 | rp1 audit, finding RP1A-04 | HESAPLAMA code part (R-5) + KAYIT record part (R-6); PI-d ride-along | this package, audit-closed | OPEN → IMPLEMENTED_PENDING_VERIFICATION | rp1-r1 | register T-KEY-NAMESPACE table with field mapping; source column |
| RP1A-05 | rp1 audit, finding RP1A-05 | KAYIT (R-6); PI-d ride-along | this package, next-inventory-level closure (D-11 r1 §2 KAYIT row) | OPEN → closes on delivery | rp1-r1 | §7 estimate, two labelled lines |
| RP1A-06 | rp1 audit, finding RP1A-06 | KAYIT (R-6); PI-d ride-along | this package, next-inventory-level closure | OPEN → closes on delivery | rp1-r1 | report response table, two labelled diffs, 3 new sidecars |
| RP1A-07 | rp1 audit, finding RP1A-07 (evidence limit) | HESAPLAMA (R-4) | this package delivers the procedure; CLOSED only by the auditor's actual re-run | OPEN (stays OPEN after this package; executor cannot close it) | — (auditor) | auditor re-run procedure doc; executor's own dry run in a second directory (not an audit) |
| R42A-03 (b) | A-5 C-31 FAIL / D-8 PI-3 (code item bound before real-data fitting); rp1 delivered the code (C-1) | HESAPLAMA (re-verified by R-5) | re-verified this package; CLOSED only by audit | IMPLEMENTED_PENDING_VERIFICATION (carried from rp1, re-verified) | rp1-r1 | T-STORE-READ-ACCOUNTING own phase + replay-vs-stored-unit assert, cold and warm |
| R42A-09 | A-5, informational/latent (fit_spline tag derivation from any same-fixture/mask-id capture) | HESAPLAMA (re-verified/strengthened by R-1(ii), family-qualified ids) | re-verified this package | IMPLEMENTED_PENDING_VERIFICATION (carried from rp1 T-CONTEXT-ID-UNIQUE, now replaced) | rp1-r1 | T-CONTEXT-ID-UNIQUE (replaces rp1's) on real ids actually passed |
| D-9 §2(a) binding of rp1/rp1-r1 bytes | D-9 §2(a); rp1 report §9 ("rp1 bytes NOT bound"); D-12 §4 | BİLİMSEL-a-adjacent gate (PI authority) | a PI record after the rp1-r1 independent audit confirms RP1A-01…03 | OPEN | — (PI) | D-11 r1 §6 model: B-correction audit, then PI decides |
| A.5 (iii) inadmissible refit | carried from D-7 / rp1 report §8 uncovered_coverage_rows | BİLİMSEL-a (D-11 r1 §5: a rule-reading or PI-authority finding) | a PI decision; no code change scheduled | OPEN, untouched by this package | — (PI) | rp1 report §8; rp1-r1 does not reopen it |

Everything else A-5 raised (R42A-01, R42A-02, R42A-04…R42A-08, R42A-10) is CLOSED or required no
action per A-5's own verdict column, and is not carried into this ledger (D-11 r1 §7 opens with
items open AT THIS TIME, not the full historical list).

## 5. (d) Previous inventory

```text
previous_inventory_sha256 = a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d
                            (f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md, rp1)
```

```text
real_data_access = false ; commit = false (separate PI instruction required)
```
