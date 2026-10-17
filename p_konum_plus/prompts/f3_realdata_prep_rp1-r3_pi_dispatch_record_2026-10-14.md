# p_konum_plus — F3 real-data preparation rp1-r3 — PI dispatch record (D-19) — 2026-10-14

> Child of D-18 and D-13; governed by D-11 r1 and its Ek-1 r1. Prepared by Claude (Claude Code cloud session) at the
> PI's request of 2026-10-14. The record is the PI's; every value may be changed before signature, and the sidecar
> is then recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-14 (§5).**

```text
record                = f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md   (D-19)
draft                 = f3_realdata_prep_rp1-r3_pi_dispatch_record_DRAFT_2026-10-14.md
                        79c13236246181678a2110cd65210794cf051cfe003a635ddb4324e36ed7e0ed ; changes in §7
status                = SIGNED (PI approval, 2026-10-14; §5)
record_class          = PI-owned dispatch record for the third, narrowly scoped rp1 correction cycle rp1-r3
parent                = D-18 f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md  fe9b2b53… (PI-3 = A) ;
                        D-13 f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md  6b9ae30e…
PI                    = Öner
what_this_record_is   = the PI's instruction to Claude Code to execute the rp1-r3 instruction (named by SHA256),
                        within the scope D-18 PI-3 A set, and the hand-over of the records D-18 PI-5 names
what_this_record_is_not = not a real-data authorization (real_data_access stays false); not a binding of any bytes
                        under D-9 §2 (a); not QUALIFIED; not F3_EXECUTION_READY; not a change to any frozen text;
                        not a closure of any ledger item
```

## 1. The dispatched instrument

```text
file_name        = Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md
sha256_expected  = f84069a060c806355676a259bd07b437a7f81ae0600b90fef5ab9baa6f73881a
note             = dispatched under this name and these bytes; the PI's signature of §5 makes it the final
                   instruction. It is the DRAFT 4081e16a… revised by the four corrections of its single
                   review round, approved by the PI (instrument §12); the DRAFT is superseded and not dispatched
standing         = D-11 r1 0b177ee4… ; Ek-1 r1 4d43682f… ; D-9 1ab17e44… ; D-12 2c23130d… ; D-13 6b9ae30e… ;
                   D-14 a0ec71cb… ; D-18 fe9b2b53… ; the rp1, rp1-r1 and rp1-r2 instructions (a57b6fca…, 2226fc96…,
                   bf53e1e9…), each as far as the rp1-r3 instruction does not replace it by name
input, not directive = the rp1-r2 independent audit record dfa76b94… ; the stopped rp1-r2 audit record f3f24b6a… ;
                   the rp1-r2 audit instruction 25eb0e16… ; D-15 278532bf…, D-16 3e2a5fe3…, D-17 25023f45…
```

## 2. PI decisions

```text
PI-a  DISPATCH         = execute the instrument of §1 as the rp1-r3 cycle decided by D-18 PI-3 A. Scope is that of
                         D-18 PI-3 A and the instrument's §0; nothing else changes. This is the third correction cycle
                         of rp1: a new B after it goes to the PI before any further round (D-11 r1 §6)
PI-b  NAMED RECORD     = this record is the "current dispatch record" that the rp1-r3 MAY_DIFFER reasons name
      FOR R3-4           (instrument §4 R3-4); the executor writes its final file name, not its hash, into those
                         reason texts, since the record carries no hash of itself
PI-c  PRE-LAUNCH STOP  = if the historical comparison of instrument §5 (a1) shows an exception-text difference
                         against r4-2, the executor STOPs before launch 1 and reports to the PI; no declaration may
                         absorb it. A new PI record decides
carried               = D-12 PI-b (family in real-mode ids) ; D-12 PI-c (consumer scope) as extended by D-18 PI-2
                         (the Q10 timing statements of run_real_scenario only) ; D-13 PI-b = B (CONTENT_RE-DERIVATION) ;
                         D-14 (IR1-13 OPEN / B, RECORDED_LIMITATION) ; D-18 PI-1, PI-4 ; T-RP-1, S-c (child of the
                         rp1-r2 harness), S-e, S-f
```

## 3. What is handed over to Claude Code

```text
MANDATORY, to be placed in p_konum_plus/prompts/ unchanged, each with its sidecar (D-18 PI-5):
  the rp1-r3 instruction (§1)
  this record, signed
  D-15 f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md
  D-16 f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md
  D-17 f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md
  D-18 f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md
  the stopped rp1-r2 audit record  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
  the rp1-r2 audit record          f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md
  the rp1-r2 audit instruction     F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
  (the two audit records keep the auditor's sidecars as delivered; every other file the drafter's sidecar)
ALREADY IN THE REPOSITORY (checked by hash, instrument §1): D-9, D-11 r1, Ek-1 r1, D-12, D-13, D-14, the rp1, rp1-r1
  and rp1-r2 instructions and packages, the r4-2 baselines
NOT handed over: earlier drafts, the drafter's handover note, review comments, the count files and the line
  classification of D-17 (it is reproduced verbatim inside D-17 §8.4)
```

## 4. End state

```text
decisions_in_this_record = §2 ; nothing else
F3_STEP2 = QUALIFIED (D-9, unchanged) ; no rp1, rp1-r1 or rp1-r2 bytes bound ; rp1-r3 bytes bound only after their
  independent audit, by one line in the dependent package's dispatch record ; the 6B companion specification remains
  a separate open precondition of F3_EXECUTION_READY
real_data_access = false ; F3_EXECUTION_READY = false ; commit = false
```

## 5. Signature

```text
PI                    = Öner
signature / approval  = APPROVED. The PI's message of 2026-10-14, verbatim (first line; the four corrections it
                        approves follow it in the same message and are applied in instrument §12):
                        aşağıdaki önerileri onaylıyorum, buna göre düzelt ve imzala:
                        The approved content is the DRAFT (79c13236…) with the instrument replaced by its r1
                        and PI-a … PI-c as written; this final text differs from the DRAFT only as listed in §7.
                        This final text was delivered to the PI; the PI's forwarding it to the executor adopts it
date_time_local       = 2026-10-14 14:39, UTC+3 — the time the drafting session recorded the PI's message (command
                        output: `TZ=Europe/Istanbul date` → 2026-10-14 14:39 +0300; UTC 2026-10-14T11:39:59Z). The
                        message's own send time is NOT OBSERVED by the drafter
```

## 6. Hashes (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ sha256sum <repository files>   (from git archive 25c7d51)
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md
a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md
bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364  p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md
6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md
a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md
$ sha256sum <the dispatched instrument and its superseded DRAFT; PI records signed in this cycle; the rp1-r2 audit instruction>
f84069a060c806355676a259bd07b437a7f81ae0600b90fef5ab9baa6f73881a  Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md
4081e16aed557adc2277ae042f7f4976725054cc665af79f7f2948544ac83a71  Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_2026-10-14.md   (superseded DRAFT)
278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md
3e2a5fe3373ae08fc91831d7312c5f994ff332efdf3bae50818cced98d608e45  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md
25023f450dc443a8d248fc8ed662812947f098f1532042a6858f159cee39deb9  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md
fe9b2b539f55efeda94d61c77ad30bd146de2ebcbbbf4d7a203fb13a8c0dcfa0  f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md
25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
$ sha256sum <rp1-r2 audit records, as uploaded by the PI> ; cat <their auditor sidecars, as uploaded>
f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
  sidecar: f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md
  sidecar: dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md
$ sha256sum <the DRAFT of this record>
79c13236246181678a2110cd65210794cf051cfe003a635ddb4324e36ed7e0ed  f3_realdata_prep_rp1-r3_pi_dispatch_record_DRAFT_2026-10-14.md
$ python3 -I probe_q5_q6.py <gate tools ca7233e7…>   (instrument §12 corrections 1 and 2; synthetic inputs only; source below)
Q5 rows [('test.n', 'E', 'MAY_DIFFER', True, 'probe'), ('test.n.leaf', 'U_FINDING', 'UNDECLARED', False, 'undeclared differing leaf')]
Q5 failures [('test.n.leaf', 'UNDECLARED')]
sibling failures [('test.n.leaf', 'UNDECLARED')]
Q6 changed_raise: frames equal False ; exception equal True
```

`probe_q5_q6.py`:

```python
import importlib.util, sys, json
spec = importlib.util.spec_from_file_location("gt", sys.argv[1]); gt = importlib.util.module_from_spec(spec); spec.loader.exec_module(gt)
d = dict(path="n", id="deep_not_hidden", kind="MAY_DIFFER", reason="probe")
rows, fails = gt.compare_document({"n": {}}, {"n": {"leaf": 3}}, [d], "test")
print("Q5 rows", [(r["path"], r["classification"], r["kind"], r["held"], r["reason"]) for r in rows])
print("Q5 failures", [(r["path"], r["kind"]) for r in fails])
# sibling construction of DRAFT 4081e16a, for comparison
rows2, fails2 = gt.compare_document({"n": {"a": 1, "leaf": 2}}, {"n": {"a": 2, "leaf": 3}}, [dict(d, path="n.a")], "test")
print("sibling failures", [(r["path"], r["kind"]) for r in fails2])
# Q6 delivered changed_raise case: exception part equal, frames differ
text = 'def raise_site():\n    raise RuntimeError("first")\n'
trace = 'Traceback (most recent call last):\n  File "C:/a/demo.py", line 2, in raise_site\nRuntimeError: first\n'
different = text.replace('"first"', '"another_statement"')
a = json.loads(gt.traceback_signature(trace, text, "demo.py")); b = json.loads(gt.traceback_signature(trace, different, "demo.py"))
print("Q6 changed_raise: frames equal", a["frames"] == b["frames"], "; exception equal", a["exception"] == b["exception"])
```

## 7. Changes from the DRAFT (79c13236…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, banner, header | DRAFT → signed; file name without DRAFT; draft and status lines | PI approval |
| 2 | §1 | the instrument is its r1 (f84069a0…), which applies the four corrections of its single review round (instrument §12); the DRAFT 4081e16a… is superseded | PI approval of the corrections |
| 3 | §2 PI-c | "§5 (a)" → "§5 (a1)", the historical comparison, after the instrument split its pre-launch check | correction 3 |
| 4 | §5 | approval message verbatim, its referent, time of recording | PI approval |
| 5 | §6 | hashes recomputed: instrument r1 and its superseded DRAFT, this record's DRAFT; the probe of corrections 1 and 2 with its source | traceability |

No other change: PI-a, PI-b, the rest of PI-c, §3 and §4 stand as in the DRAFT.
