# p_konum_plus — rp1-r3 — PI decision record on the attempt-1 W-3 writer STOP (D-20) — 2026-10-16

> Child of D-19. Governed by D-11 r1 and its Ek-1 r1. Prepared by Claude (Claude Code cloud session) at the PI's
> request of 2026-10-16. The record is the PI's; every value may be changed before signature, and the sidecar is then
> recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-16 (§6); decision = B.**

```text
record                = f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_2026-10-16.md   (D-20)
drafts                = f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_DRAFT_r1_2026-10-16.md
                        ffc6a42b467a1181fd0dc93cdcac4160c81d9e8ac661e1ce511f08dfbe07a477 (approved; changes in §9) ;
                        f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_DRAFT_2026-10-16.md  1849f7ef…
                        (r1 applies the single review round relayed by the PI on 2026-10-16; §8)
status                = SIGNED (PI approval, 2026-10-16; §6) ; decision = B
parent                = D-19 f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md  10b35433…
instrument            = Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md  f84069a0…
subject               = the executor's STOP report f3_realdata_prep_rp1-r3_ilerleme_STOP_2026-10-16_100213_UTC.md
                        0061eeb8… (equal to its sidecar), relayed by the PI on 2026-10-16
what_this_record_is   = the PI's disposition of a wiring defect that stopped rp1-r3 attempt 1 before the harness
                        started, and the exact scope of the correction allowed in attempt 2
what_this_record_is_not = not a change to the rp1-r3 instruction, its scope or its pass criterion; not a finding on
                        the rp1-r2 package; not a closure of any ledger item; not a binding; not QUALIFIED; not a
                        real-data authorization
```

## 1. Facts

```text
(1) as reported by the executor (STOP report; the drafter has not seen the executor's worktree):
    - the W-3 writer of attempt 1, launch 1 ran 2026-10-15T19:19:13.446643Z → 19:19:15.686860Z and exited 1 with
      FileNotFoundError in its dispatch-pin verification; writer record 5c966104…; rp1-r3 harness 53145cdd…
    - 4 pinned paths do not exist (expected hash in brackets):
        p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-15.md   [bf53e1e9…]
        p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-15.md                [6b9ae30e…]
        p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-15.md [f3a6f369…]
        p_konum_plus/prompts/f3_realdata_prep_rp1-r3_IR1-13_pi_decision_record_2026-10-15.md          [a0ec71cb…]
    - no harness start record, no W-3 custody record, no attempt store; no change, retry, commit or push after the
      stop; no real SSA / F1 input read
    - before the launch: §5 (a1) passed with 0 new traceback differences; §5 (a2) Q4 10/10, Q5 51/51, Q6 23/23,
      RRS 2/2, 0 U in results and test_evidence; the 2,298 rp1-r2 deliverables re-hashed
(2) checked by the drafter against 25c7d51 (§7):
    - the rp1-r2 harness 4d2e3db0…, line 123, holds RP2_DISPATCH_PINS, 9 entries; every entry matches the bytes of
      25c7d51. The 4 expected hashes above are entries 1, 2, 3 and 9 — the rp1-r2 instruction, D-13, the rp1-r1
      audit record and D-14 — whose true paths end in 2026-10-10 and contain "rp1-r2" or "2026-10-10"
    - replacing "rp1-r2" by "rp1-r3" and "2026-10-10" by "2026-10-15" in the 9 paths yields exactly the 4 reported
      paths and leaves entries 4 – 8 unchanged
    - reading (an inference; the rp1-r3 code is not seen): the list was carried by a text substitution that
      changed paths and kept rp1-r2's hashes. Restoring the 4 paths alone would let the writer pass while pinning
      rp1-r2's incoming set; rp1-r3's own incoming set (instrument r1, D-19, D-15 … D-18, the two audit records,
      the rp1-r2 audit instruction) would not be pinned at all
    - the rp1-r2 harness, lines 5159 – 5163, reads and asserts the cycle's dispatch record by path and pinned hash
      (D-13, 6b9ae30e…) for the end state; the rp1-r2 gate tools, lines 21 – 22, pin D-14 by path and hash. The same
      substitution would break or misdirect both. Rp1 §9 and instrument R3-4 require the end state to name this
      cycle's own record, D-19
(3) rule: the instrument carries rp1-r2 §0 unchanged — after an observed failure only a defect in an expectation
    or declaration may be corrected, in a new attempt, disclosed in the attempt log. A dispatch pin is §8 wiring
    (instrument R3-5), not an expectation or a declaration, so the executor could not correct it on its own. The
    STOP was the required behaviour
```

## 2. Classification and decision — the PI chose B (§6); A and C are kept as presented

```text
classification  not decided in this record. D-11 r1 §5 defines B on bytes "teslim edilen baytlarda gözlenen ya da
                yeniden üretilen"; the attempt-1 code is not delivered, and the class of a finding is the auditor's
                ("Denetçinin sınıfı geçerlidir"). That no computation started does not by itself exclude B (iii).
                The defect is recorded in the attempt log (§3 C-4); the rp1-r3 auditor classes it. If the auditor
                proposes B, the PI decides under D-11 r1 §6 as for any new B after the second B correction, and
                the ledger follows that decision; this record does not pre-empt it
change class    the §3 changes are HESAPLAMA corrections within R3-5 (§8 wiring; instrument §9 block)
basis           the authorization below is the PI's bounded retry authorization for this instrument; it does not
                rest on a claim that D-11 r1 §6 cannot apply
A  ATTEMPT 2 WITH THE BOUNDED CORRECTION OF §3
   attempt 2 may change exactly what §3 lists, and nothing else
B  as A, with a hold point before launch                                                       [recommended]
   after §3 C-1 … C-5 the executor stops BEFORE launch 1 of attempt 2 and sends the PI, as files with sidecars:
     - the C-3 listing
     - the C-5 results with their code hashes
     - the attempt-1 → attempt-2 diff of every changed file, one label per hunk ("R3-5 (D-20 C-n)")
     - the SHA256 of the attempt-2 harness and of every other file attempt 2 changed
   launch only on a PI message naming the attempt-2 harness hash and those file hashes. A byte change after the
   hold point ⇒ a new hold point. Reason for B: the root cause in §1 (2) is an inference from rp1-r2 code; the
   rp1-r3 code has not been seen, and the substitution may reach beyond the 4 paths (end state, D-14)
C  STOP rp1-r3 pending a further PI review
```

## 3. Correction allowed in attempt 2 (binding with this record under A or B)

```text
C-1 DISPATCH PINS. The dispatch-pin list is rebuilt as two named groups; each expected hash is read from the file
    bytes at prompts/ and must equal the value printed here, otherwise STOP:
      rp1-r3 incoming (D-19 §3), all under p_konum_plus/prompts/
        Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md                     f84069a0…
        f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md                                   10b35433…
        f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md                  278532bf…
        f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md 3e2a5fe3…
        f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md       25023f45…
        f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md                     fe9b2b53…
        f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md               f3f24b6a…
        f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md               dfa76b94…
        F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md                             25eb0e16…
        and this record, signed, by its sidecar value (it carries no hash of itself)
      rp1-r3 carried: the 9 entries of the rp1-r2 list at their TRUE 25c7d51 paths and hashes (§7), plus
        p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py                     4d2e3db0…
        p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv            e48f5f6b…
C-2 OWN DISPATCH RECORD. The end-state check of the dispatch record (rp1-r2 harness 5159 – 5163 and its
    successor) reads p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md and asserts
    10b35433…; the end state records D-19's path and observed hash. D-14 keeps its own path and hash wherever it is
    pinned (gate tools D14_PATH / D14_SHA256 at 25c7d51 values). R3-4 stands as written
C-3 LITERAL LISTING (inventory) AND RESTORATION (narrow). Before launch, a logged script lists every string
    constant of the rp1-r3 harness, gate tools, technical tests, launcher and W-3 writer that contains
    "p_konum_plus/", "rp1-r" or "2026-", with file, line, value, its rp1-r2 counterpart where one exists, whether
    the value names an existing file, that file's SHA256, and one class:
      NEW      a file name or path this cycle creates (rp1-r3 name, the cycle's date): exists, or is an output of
               this attempt
      PIN      an entry of C-1 or C-2
      HISTPATH a path or file name of an existing historical file; it must equal its rp1-r2 / 25c7d51 value
      TEXT     anything else (message, test input, comment-like string); listed only
    restoration is limited to HISTPATH and PIN literals that the attempt-1 substitution changed and that are shown
    wrong by the listing (the path does not exist, or names a different file than its rp1-r2 counterpart): they
    are restored to the rp1-r2 value or set by C-1 / C-2. TEXT literals are not changed under this record; one
    that looks wrong is flagged in the listing and reported (under B at the hold point), not edited. The listing
    is a new provenance file with a sidecar and is summarised in the attempt log
C-4 ATTEMPT MECHANICS (rp1 §8 rule). The attempt-1 harness and every file attempt 2 changes are copied to
    quarantine before the first edit; ATTEMPT_NUMBER = 2. No attempt-1 W-3 custody record exists: the SUPERSEDES
    field of attempt 2 names the attempt-1 writer record 5c966104… and states "no attempt-1 W-3 record"; the
    rp1-r2 chain of R3-5 is unchanged. The attempt log records the observed failure, the defect, every change and
    this record
C-5 RE-RUN BEFORE LAUNCH. §5 (a1) and §5 (a2) and T-RP1R3-RRS-UNCHANGED are re-run on the attempt-2 bytes, each
    logged with its code hashes; the W-3 writer's pin verification must pass in full
C-6 NOTHING ELSE. No change to R3-1 … R3-4 (the Q6, Q4 and Q5 behaviour and their tests), to any expectation or
    declaration, to run_real_scenario or to any scientific code. A further change found necessary ⇒ STOP and
    report to the PI
labels: the attempt-2 hunks of C-1 … C-3 are R3-5 / §8 wiring for instrument §6 IR1-16 and §9 (2), each labelled
"R3-5 (D-20 C-n)"
```

## 4. Hand-over

```text
to the executor : this record, signed, with its sidecar, to be placed in p_konum_plus/prompts/ unchanged
the executor's own STOP report stays with the executor and is recorded in its attempt log; it is not returned
not handed over : earlier drafts, review comments
```

## 5. End state

```text
rp1-r3: attempt 1 FAILED at the W-3 writer (no computation) ; attempt 2 under §3 (A or B) ; this record changes no
ledger item; the defect's class follows the rp1-r3 auditor and, if B is proposed, the PI under D-11 r1 §6 ;
IR1-13 OPEN / B under D-14 ; real_data_access = false ; F3_EXECUTION_READY = false ; commit = false
```

## 6. Signature

```text
PI                    = Öner
decision              = B — attempt 2 with the bounded correction of §3 and a hold point before launch
scope of the approval = the §3 corrections and the pre-launch checks only. The full run of attempt 2 waits for a
                        separate PI message, given after the PI has assessed the hold-point evidence, that names the
                        attempt-2 harness hash and the hashes of every other changed file (§2 B). D-19 is unchanged.
                        No commit or push is authorized
signature / approval  = APPROVED. The PI's message of 2026-10-16, verbatim:
                        D-20 DRAFT r1’i, SHA256 `ffc6a42b467a1181fd0dc93cdcac4160c81d9e8ac661e1ce511f08dfbe07a477`, mevcut içeriğiyle onaylıyorum. §2’deki **B seçeneğini** seçiyorum.

                        Bu mesajımı PI onayı olarak kayda geçir; imzalı son sürümü, yeniden hesaplanan SHA256 değerini ve sidecar’ını hazırla. D-19 değişmesin.

                        Bu onay yalnız belirtilen düzeltmeler ve ön kontroller içindir. Attempt 2’nin tam koşusu, bekleme noktası kanıtlarını değerlendirdikten sonra ilgili dosya hash’lerini adlandıran ayrı onayımı beklesin.

                        İmzalı D-20 ve sidecar’ıyla birlikte yürütücüye ileteceğim kısa mesajı da hazırla. Commit veya push yetkisi vermiyorum.
                        The approved content is DRAFT r1 (ffc6a42b…); this final text differs from it only as
                        listed in §9. This final text was delivered to the PI; the PI's forwarding it adopts it
date_time_local       = 2026-10-16 18:55, UTC+3 — the time the drafting session recorded the PI's message (command
                        output: `TZ=Europe/Istanbul date` → 2026-10-16 18:55 +0300; UTC 2026-10-16T15:55:41Z). The
                        message's own send time is NOT OBSERVED by the drafter
```

## 7. Hashes and checks (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ sha256sum <executor STOP report, as uploaded by the PI> ; cat <its sidecar, as uploaded>
0061eeb87567247d0bc76d3d8e1fd82bc17f162e5f73a888eb6a59ac78585390  f3_realdata_prep_rp1-r3_ilerleme_STOP_2026-10-16_100213_UTC.md
  sidecar: 0061eeb87567247d0bc76d3d8e1fd82bc17f162e5f73a888eb6a59ac78585390  f3_realdata_prep_rp1-r3_ilerleme_STOP_2026-10-16_100213_UTC.md
$ python3 -I pins_list.py <git archive 25c7d51>   (RP2_DISPATCH_PINS of the rp1-r2 harness, each entry hashed from the bytes)
1 bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5 MATCH p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md
2 6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f MATCH p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md
3 f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913 MATCH p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md
4 82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e MATCH p_konum_plus/prompts/F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md
5 cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb MATCH p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py
6 98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956 MATCH p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md
7 0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639 MATCH p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
8 4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955 MATCH p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md
9 a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7 MATCH p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md
$ python3 -I subst_check.py <rp1-r2 harness>   (replace "rp1-r2"->"rp1-r3", "2026-10-10"->"2026-10-15"; compare with the 4 reported paths)
1 changed matches_reported bf53e1e9
2 changed matches_reported 6b9ae30e
3 changed matches_reported f3a6f369
4 unchanged - 82472d63
5 unchanged - cac93ac6
6 unchanged - 98ed374d
7 unchanged - 0b177ee4
8 unchanged - 4d43682f
9 changed matches_reported a0ec71cb
$ sed -n 5159,5163p <rp1-r2 harness 4d2e3db0…>
    _d13_path = "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md"
    _d12_observed = sha256_of(_d13_path)
    assert _d12_observed == "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f", (
        "rp1-r2 STOP: D-13 observed %s != pinned %s"
        % (_d12_observed, "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f"))
$ sed -n 21,22p <rp1-r2 gate tools ca7233e7…>
D14_PATH = "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md"
D14_SHA256 = "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7"
$ sha256sum <repository files, from git archive 25c7d51>
4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7  p_konum_plus/calibration/f3_rp1-r2_gate_tools_2026-10-10.py
e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75  p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md
$ sha256sum <rp1-r3 incoming set, as delivered to the PI; each equals its sidecar>
f84069a060c806355676a259bd07b437a7f81ae0600b90fef5ab9baa6f73881a  Claude_Code_F3_REALDATA_PREP_RP1-R3_INSTRUCTION_DRAFT_r1_2026-10-14.md
10b3543344bd9ebf9df3319cfdc0d3540888328fde8bf4e5d6e05764bb675b1a  f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md
278532bff270337e7db59d4e1a47287fc3169b651d9b4f4625687beca864fb93  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md
3e2a5fe3373ae08fc91831d7312c5f994ff332efdf3bae50818cced98d608e45  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_scope_evaluation_pi_decision_record_2026-10-12.md
25023f450dc443a8d248fc8ed662812947f098f1532042a6858f159cee39deb9  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_completion_pi_decision_record_2026-10-12.md
fe9b2b539f55efeda94d61c77ad30bd146de2ebcbbbf4d7a203fb13a8c0dcfa0  f3_realdata_prep_rp1-r2_audit_outcome_pi_decision_record_2026-10-14.md
f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md
dfa76b94b3b82209ceed7587fb9f2722db07044e5ce74a14ef9daf761b760eb2  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-13.md
25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
$ values from the STOP report (NOT computed by the drafter; the files are in the executor worktree)
5c9661045c6602195296689229834c4f178fb7cab03c9ad5fe3337aa2b9bf459  p_konum_plus/provenance/f3_step2_rp1-r3_attempt1_launch1_w3_writer_2026-10-15.json
53145cdd26e1263708a90b8dca08d0a8cab95d1fe0cdc126eb878726534a44db  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r3_2026-10-15.py
```

`pins_list.py`:

```python
import ast, hashlib, pathlib, sys
root = pathlib.Path(sys.argv[1]); src = (root / 'p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py').read_text(encoding='utf-8')
pins = next(ast.literal_eval(n.value) for n in ast.parse(src).body
            if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'RP2_DISPATCH_PINS')
for i, (p, h, name) in enumerate(pins, 1):
    obs = hashlib.sha256((root / p).read_bytes()).hexdigest()
    print(f"{i} {h} {'MATCH' if obs == h else 'DIFF'} {p}")
```

`subst_check.py`:

```python
import ast, pathlib, sys
src = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
pins = next(ast.literal_eval(n.value) for n in ast.parse(src).body
            if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'RP2_DISPATCH_PINS')
reported = {
 "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-15.md",
 "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-15.md",
 "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-15.md",
 "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_IR1-13_pi_decision_record_2026-10-15.md"}
for i, (p, h, name) in enumerate(pins, 1):
    q = p.replace("rp1-r2", "rp1-r3").replace("2026-10-10", "2026-10-15")
    print(i, "changed" if q != p else "unchanged", "matches_reported" if q in reported else "-", h[:8])
```

```text
$ sha256sum <the drafts of this record>
ffc6a42b467a1181fd0dc93cdcac4160c81d9e8ac661e1ce511f08dfbe07a477  f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_DRAFT_r1_2026-10-16.md
1849f7ef7c4b1165dee7f084bd2c3650f137e68c4302d692fcd20600676455f4  f3_realdata_prep_rp1-r3_attempt1_STOP_pi_decision_record_DRAFT_2026-10-16.md
```

## 8. Changes from the DRAFT (1849f7ef…)

| # | where | change | reason |
|---|---|---|---|
| 1 | §2 | the DRAFT's ruling "not a B; D-11 r1 §6 is not engaged" removed; the class is left to the rp1-r3 auditor, with the B definition of D-11 r1 §5 cited; the retry rests on the PI's bounded authorization; the change class (HESAPLAMA within R3-5) stated | review: "computation had not started" does not by itself exclude B (iii), and the class is the auditor's |
| 2 | §2 | B recommended instead of A; the hold-point package adds the attempt-1 → attempt-2 diff and the hashes of every changed file; a byte change after the hold point needs a new hold point | review: the root cause is an inference until the rp1-r3 code is seen |
| 3 | §3 C-3 | the listing stays broad (inventory); restoration narrowed to HISTPATH and PIN literals shown wrong; a new TEXT class is listed only and never edited under this record | review: a broad "restore unless NEW or PIN" rule could undo a correct change |
| 4 | §3 C-6 | names the Q6, Q4 and Q5 behaviour and their tests explicitly | review |
| 5 | §5 | end state: the ledger follows the auditor's class and, if B, the PI's §6 decision | follows #1 |

No other change: §1, C-1, C-2, C-4, C-5, §4, §6 and §7 stand as in the DRAFT.

## 9. Changes from DRAFT r1 (ffc6a42b…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, banner, header | DRAFT r1 → signed; file name without DRAFT; drafts and status lines; decision = B | PI approval |
| 2 | §2 heading | records the PI's choice of B; A and C kept as presented | PI approval |
| 3 | §6 | decision, scope of the approval, approval message verbatim, time of recording | PI approval |
| 4 | §7 | the hash of DRAFT r1 added beside the DRAFT | traceability |

No other change: §1, the body of §2, §3, §4, §5 and §8 stand as in DRAFT r1.
