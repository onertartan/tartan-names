# p_konum_plus — rp1-r2 — PI decision record on the independent audit outcome (D-18) — 2026-10-14

> Child of D-13 and D-17. Governed by D-11 r1 §5–§7 and Ek-1 r1. Prepared by Claude (Claude Code cloud session) at
> the PI's request. The record is the PI's; every value may be changed before signature, and the sidecar is then
> recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-14 (§6); PI-3 = A.**

```text
record                = f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md   (D-18)
draft                 = f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_DRAFT_2026-10-14.md
                        15556417e8c7e8253f27a047048cdf6099e4c96519fe54e579ea9a12639255f9 ; changes in §8
status                = SIGNED (PI approval, 2026-10-14; §6)
parent                = D-13 f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md  6b9ae30e… ;
                        D-17 f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md  25023f45…
subject               = the independent audit of rp1-r2:
                        f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md  dfa76b94…
                        (verdict NOT PASSED; "AUDITOR REVIEW COMPLETE — NOT PASSED; OPEN FINDINGS RECORDED"), under the
                        audit instruction 25eb0e16… and D-15 / D-16 / D-17
basis                 = the audit record; the drafter's check of two findings against the bytes of 25c7d51 (§1 (4)); an
                        external review relayed by the PI on 2026-10-14 (ChatGPT), whose recommendations §3 follows
what_this_record_is_not = not PASSED; not a D-9 §2 (a) binding; not QUALIFIED; not F3_EXECUTION_READY; not a
                        real-data authorization; no ledger item is closed by it except as stated in PI-2
```

## 1. Facts from the audit record

```text
(1) verdict: NOT PASSED. The auditor's independent rerun (13 Oct 08:41:43Z → 14 Oct 00:42:09Z, exit 0, about 16 h;
    the executor's attempt 2 took 10 h 05 m) and postrun review are complete
(2) scientific comparisons matched in the auditor's run: 37 = 37 evaluation objects with 0 differing and 6 = 6
    stops, against the delivered results and against r4-2; RUN1 = RUN2 = 556106e7…; residual 3ee624f3… in the run,
    the delivered package and r4-2; 50 tests ran and passed, Q results equal to the delivered ones; 67,316 store
    payloads and 22,217 calls reconciled
(3) the records are NOT all identical: 14 non-regression rows differ from the delivered CSV — 11 process ids and 3
    named output-file hashes — and the auditor reviewed and explained each by the independent process identity or
    the actual file bytes; stderr is equal only after normalising the source-directory prefix
(4) open findings (audit record, findings table); the drafter checked the first and the fourth against 25c7d51:
      IR1-08  K  Q6 traceback signature keeps only the last non-empty traceback line (gate_tools:242), so
                 different exception types or multi-line messages can share a signature; due in this package
                 [drafter: confirmed on the code]
      IR2-01  K  the Q4 static guard misses the spelling row['ok']=True; the delivered loader cases are correct
      IR2-02  K  the delivered Q5 negative deep_not_hidden fails for two reasons at once; the comparator itself
                 handles the target correctly
      IR2-03  B (iii) proposed  the Q10 per-trajectory clock reads and timing append (harness 2235–2236,
                 2375–2379) lie in run_real_scenario outside D-12 PI-c [drafter: confirmed; the lines read the clock
                 and append to a module-level list, and no computed value changes]
      IR1-16, IR2-04, IR2-05, IR2-06  T  labels, rerun procedure, stale R42A-09 reason, a MAY_DIFFER reason text
      IR2-07  T  outside-W3 external outputs, comparator script and inventories not delivered; claims [X]
(5) ledger after the audit: the auditor closed IR1-02 … 07, 09 … 12, 14, 15, 17, 18, 19, RP1A-02, 04, 05,
    R42A-03 (b) and R42A-09. Open: RP1A-01 (pending IR2-03), RP1A-03 (inherited B, pending IR1-08), RP1A-06
    (pending IR1-16), IR1-08, IR1-16, IR2-01 … 07, IR1-13 (OPEN / B, RECORDED_LIMITATION under D-14), the D-9
    §2 (a) binding of rp1 / rp1-r1 bytes, A.5 (iii), the F1 input-hash-table sidecar
(6) origin of IR2-03: the rp1-r2 instruction (bf53e1e9…) asked in Q10 for a per-trajectory timing table but stated
    in §2 that PI-c was unchanged with only Q1 and Q2 inside it, and the audit instruction §2.2 made a consumer
    hunk outside PI-c a finding. The conflict lies in the drafter's instructions, not in the executor's work
```

## 2. Decisions — the PI adopted PI-1 … PI-5 as written and chose option A of PI-3 (§6); B, C, D are kept as presented

```text
PI-1  AUDIT OUTCOME
      the PI adopts the verdict NOT PASSED. The rp1-r2 bytes are not bound under D-9 §2 (a); nothing is QUALIFIED;
      F3_EXECUTION_READY stays false. The supported statement on the rerun is: the scientific comparisons matched
      and the listed process differences were reviewed by the auditor (§1 (2), (3)) — not that every record is
      identical
PI-2  IR2-03 (Q10 timing inside run_real_scenario)
      class: B (iii) as proposed by the auditor (D-11 r1 §5); this record is the PI record that names it
      decision: a NEW, explicit PI authorization, effective from this record; it does not claim that D-12 PI-c or
      D-13 already covered the change. PI-c is extended by exactly this:
        inside run_real_scenario, (i) reading the process clock and the wall clock at the start and at the end of
        each trajectory section, and (ii) appending one timing record per trajectory to the module-level
        HANDOFF_TRAJECTORY_TIMINGS list, when real_x is present — as at harness 4d2e3db0…, lines 2235–2236 and
        2375–2379, and the same statements in its successors
      nothing else in run_real_scenario or in any scientific computation or decision path is authorized by this
      extension. The rp1-r2 deviation is recorded as made before this authorization existed
      closure: IR2-03 is disposed by this record; the next independent audit verifies that the only
      run_real_scenario changes beyond PI-c are these. RP1A-01 stays OPEN until that audit
PI-3  D-11 r1 §6 — a new B (IR2-03) after the second B-correction round of rp1, and an inherited B still open
      (RP1A-03, through IR1-08); the PI decides before any further round:
      A  CONTINUE with one narrowly scoped correction package, rp1-r3                          [recommended]
         this is the third correction cycle of rp1, limited to:
           K  IR1-08 (Q6: keep the full exception type and message; independent multi-line and type negatives),
              IR2-01 (Q4: include constant subscript assignments; test the spelling), IR2-02 (Q5: isolate the
              intended defect; assert the target path and reason) — RP1A-03 closes with IR1-08
           T  IR1-16 (one label per hunk or per-label ranges), IR2-04 (full list of outputs the rerun overwrites,
              and preservation steps), IR2-05 (current R42A-09 evidence), IR2-06 (the MAY_DIFFER reason text);
              IR2-07: deliver permitted, named custody evidence of the outside-W3 records where it exists,
              otherwise keep each claim NOT OBSERVED; no contamination is inferred from the absence, and D-14 is
              not extended to these records
         nothing else changes: no scientific code, no frozen literal, no declaration widened, no S object expected
         to change. Whitelist-free non-regression against r4-2 and an independent TEKNİK audit with a re-run are
         kept (D-9 §2 (a), D-11 r1 §4); the T items ride in the same package and audit, with no separate cycle
      B  CONTINUE, folding the same K and T items into the preparation phase of the next code package (e.g. rp2,
         the 6B code), verified by that package's non-regression and audit (D-11 r1 §3); saves one run and one
         audit but holds the real-data step until that package
      C  RECORDED LIMITATION for IR1-08 / RP1A-03 (D-11 r1 §6): the items stay OPEN / B in the ledger and the gate
         passes only by a later PI record naming them
      D  STOP
PI-4  LEDGER
      the auditor's dispositions are taken over as written (§1 (5)); the PI closes nothing beyond PI-2's disposal
      of IR2-03. IR1-13 stays OPEN / B, RECORDED_LIMITATION under D-14; RP1A-03 stays OPEN (inherited B); the D-9
      binding, A.5 (iii) and the F1 sidecar keep their closure points. No item is closed in bulk
PI-5  RECORDS
      the stopped audit record (f3f24b6a…), D-15, D-16, D-17, this record and the audit record (dfa76b94…) go into
      p_konum_plus/prompts/ with the next dispatch record, each with its sidecar
```

## 3. What follows

```text
under PI-3 A: the drafter prepares the rp1-r3 instruction and its dispatch record (D-19) within the scope above,
  with the D-11 r1 §8 block, a requirement map (requirement → code → positive / negative test), and run-time
  planning from the measured durations (10 h 05 m executor, about 16 h auditor). Independent audit as for rp1-r2,
  in a new session and directory, under the D-15 §3 reading rules
under PI-3 B: the items are entered in the start inventory of the next code package with closure point "before
  dependent computation"; no rp1-r3
under C or D: as written there
in every case: the 6B companion specification remains a separate open precondition of F3_EXECUTION_READY
```

## 4. End state

```text
rp1-r2: audit NOT PASSED (adopted) ; bytes not bound ; IR2-03 disposed by PI-2 (verification in the next audit) ;
open: IR1-08, IR2-01, IR2-02 (K), RP1A-01, RP1A-03, RP1A-06, IR1-16, IR2-04 … 07, IR1-13 (OPEN / B, D-14), D-9
binding, A.5 (iii), F1 sidecar ; real_data_access = false ; F3_EXECUTION_READY = false ; commit = false
```

## 5. Hand-over

```text
to the executor: nothing now. Under PI-3 A the rp1-r3 instruction and D-19 carry the records of PI-5
to an auditor: nothing now
```

## 6. Signature

```text
PI                    = Öner
decisions             = PI-1, PI-2, PI-4, PI-5 as written ; PI-3 = A (rp1-r3, the third, narrowly scoped
                        correction cycle of rp1, within the scope of PI-3 A)
signature / approval  = APPROVED. The PI's message of 2026-10-14, verbatim:
                        önerileri kabul ediyorum, buna göre imzala ve gerekli çıktıları hazırla
                        "önerileri" refers to the drafter's recommendations of the DRAFT (15556417…): PI-1 … PI-5 as
                        written and option A of PI-3, which follow the review relayed by the PI the same day. The
                        approved content is that DRAFT; this final text differs from it only as listed in §8. This
                        final text was delivered to the PI; the PI's forwarding it adopts it
date_time_local       = 2026-10-14 14:18, UTC+3 — the time the drafting session recorded the PI's message (command
                        output: `TZ=Europe/Istanbul date` → 2026-10-14 14:18 +03; UTC 2026-10-14T11:18:23Z). The
                        message's own send time is NOT OBSERVED by the drafter
```

## 7. Hashes (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ sha256sum <files>  (repository files from git archive 25c7d51; records and uploads as named)
6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md
2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364  p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md
a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md
bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md
4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7  p_konum_plus/calibration/f3_rp1-r2_gate_tools_2026-10-10.py
25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md
3e2a5fe3373ae08fc91831d7312c5f994ff332efdf3bae50818cced98d608e45  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md
25023f450dc443a8d248fc8ed662812947f098f1532042a6858f159cee39deb9  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md
dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md
f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
$ cat <audit record sidecar, as uploaded by the PI>
dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md
$ timing of the auditor rerun (from the audit record: launcher start 2026-10-13T08:41:43.699357Z, controller end 2026-10-14T00:42:09.836277Z)
elapsed 16:00:26.136920
$ sed -n 2235,2236p; 2375,2379p  <harness 4d2e3db0…>   (the statements PI-2 names)
            _trajectory_start = _time.perf_counter()
            _trajectory_start_iso = _dt.datetime.now().isoformat()
            if real_x is not None:
                _trajectory_end = _time.perf_counter()
                HANDOFF_TRAJECTORY_TIMINGS.append(dict(phase=CURRENT_PHASE[0], sex=sx, trajectory=ti,
                    start_iso=_trajectory_start_iso, end_iso=_dt.datetime.now().isoformat(),
                    start_clock=_trajectory_start, end_clock=_trajectory_end, elapsed_seconds=_trajectory_end - _trajectory_start))
$ sed -n 242,243p <gate_tools ca7233e7…>   (IR1-08)
    tail = next((line for line in reversed(trace.splitlines()) if line.strip()), "")
    return json.dumps(dict(frames=frames, exception=tail), sort_keys=True, ensure_ascii=True)
$ python3 (fields read from the audit record dfa76b94…: S_vs_r4_2.run1_canonical_sha256 and residual_sha256)
run1_canonical_sha256 reference(r4-2) 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 rerun 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77
residual_sha256 run 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f ref 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f r4_2 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f
```

## 8. Changes from the DRAFT (15556417…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, banner, header | DRAFT → signed; file name without DRAFT; draft and status lines | PI approval |
| 2 | §2 heading | records the PI's adoption of PI-1 … PI-5 and the choice of PI-3 A; B, C, D kept as presented | PI approval |
| 3 | §6 | decisions, approval message verbatim with its referent, time of recording | PI approval |

No other change: §1, the body of §2, §3, §4, §5 and §7 stand as in the DRAFT.
