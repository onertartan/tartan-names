# p_konum_plus — rp1-r2 — PI decision record on the stopped audit (AUDITOR-SCOPE-01) (D-15) — 2026-10-12

> Child of D-13. Governed by D-11 r1 §5–§6 and Ek-1 r1. Prepared by Claude (Claude Code cloud session) at the
> PI's request. The record is the PI's; every value may be changed before signature, and the sidecar is then
> recomputed. It carries no hash of itself. **Signed by the PI's approval of 2026-10-12 (§6); decision = B.**

```text
record                = f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_2026-10-12.md   (D-15)
drafts                = …_DRAFT_r2_2026-10-12.md 7320e0f1f311effa8abbe141881c51eab41ebb2aec3361912eb27ad116168484 (r2,
                        the approved content; changes to this final text in §9) ;
                        …_DRAFT_r1_2026-10-12.md ed0baedf90600a3c8135e44c4566cc836b0d19ee2e1346df394f3a6dcfdee7db (r1;
                        changes r1 → r2 in §8, made at the PI's direction before signature) ;
                        …_DRAFT_2026-10-12.md bb79d1763f10370dd25098f90737747f316e2a0e1a751bce213ec5f32f7d2f91 (first draft;
                        changes → r1 in §8, the one review round of D-11 r1 §6)
status                = SIGNED (PI approval, 2026-10-12; §6)
parent                = D-13 f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md  6b9ae30e…
subject               = AUDITOR-SCOPE-01 in the stopped rp1-r2 audit record
                        f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md  f3f24b6a…
                        (verdict "NOT PASSED — AUDIT STOPPED / INCOMPLETE"), audit instruction
                        F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md  25eb0e16…
what_this_record_is   = the PI's classification of an auditor-side reading-scope incident, the sequence by which the
                        PI settles its firewall question, and the operating rules of a repeated audit
what_this_record_is_not = not a finding on the rp1-r2 package; not a closure of any ledger item; not a binding;
                        not QUALIFIED; not a real-data authorization; not a change to the audit instruction or to
                        its pass criterion
```

## 1. Facts

```text
(1) the auditor (GPT-6 / Codex, directory G:\PycharmProjects\rp1r2_audit) meant to search one file, the rp1-r2
    harness; the search ran over both clones (ref, run) of the whole repository. Its output showed non-hash
    columns of p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv, lines 207–218 (audit instruction §0
    permits the hash column only). Which files the search opened and the argv it received are NOT OBSERVED.
    The auditor stopped before any launch, probe or re-execution, wrote nothing into either clone, and classed
    the incident STOP for its session, not a package defect (audit record, findings table)
(2) the checks the auditor completed before the stop all passed: instruction hash, clone HEAD and status,
    the 2,298 transmission-list rows (0 failures, 4,598 added files), 25 cited hashes, 3 dependency pins
    (audit record, §1–§2; [A] / [A-S] there)
(3) scope of what the search could have displayed, established by the PI on 2026-10-12 with a count-only
    command over the delivered commit (no line content shown). Command and output as run and relayed by the PI:
      $ git -C G:/PycharmProjects/rp1r2_audit/ref grep -c -E 'write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY' 25c7d51 -- data p_konum_plus/manifests results
      25c7d51:p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv:12
      25c7d51:results/result_plotter_KMeans_KMedoids.py:2
      25c7d51:results/result_plotter_Spectral.py:2
      25c7d51:results/results_plotter_GMM.py:3
    what this establishes: for the INTENDED pattern, at commit 25c7d51, under data/, p_konum_plus/manifests/
    and results/, matching lines exist only in the four files listed — 12 lines of the input hash table (the
    count equals the 12 lines 207–218 the auditor reported, which is consistent with the intended pattern
    having been in effect for that file) and lines of three plotting scripts (code); none in data/ (which
    holds the real SSA files data/raw/names-usa/…), none in the F1 eligible manifest, none in a result file
    what this does NOT establish: the stopped search's effective pattern and paths (its argv is NOT OBSERVED),
    the files it opened, or everything it displayed; the directories not checked (e.g. notebooks/); and a
    file with no matching line may still have been opened. The check narrows the question; it does not
    answer it
(4) the drafting session's own contribution: audit instruction §0 forbade data/raw/… but did not say that the
    repository root also holds real data and application results outside p_konum_plus/, nor forbid a recursive
    search over the clones. That gap is the drafter's
(5) a hypothesis on the effective argv, NOT yet verified (the drafter's simulation, command and output in §7):
    in Windows PowerShell 5.1 a native-program argument that contains no space is passed verbatim, embedded
    double quotes included; rg parses its command line by the MSVC rules, under which the `"` in `\.open\("`
    opens a quoted section that runs to the end of the line. rg would then receive one pattern argument that
    swallows the path, and NO path, and would search its working directory G:\PycharmProjects\rp1r2_audit
    recursively, i.e. both clones — which matches the auditor's observation. Effective pattern under this
    hypothesis (E):
      write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
    E differs from the intended pattern in two alternatives, so the check of (3) is not a check of E. If the
    hypothesis holds: every non-ignored file under that directory was opened (rg reads a file to search it);
    content reached the session only as lines matching E, printed with line numbers (rg -n), and of those
    only the part not cut off by the tool's output truncation
(6) protocol classification (calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md, §5 evidence firewall
    matrix and §9 STOP register): raw SSA trajectory data (EV-01) and the F1 inventory are evidence classes
    allowed before F12; their exposure breaks the audit instruction's reading rule, not the outcome firewall.
    The outcome firewall prohibits new-project algorithm × CVI outcomes before F12 (EV-17, which must not exist
    yet; exposure is logged, STOP-15) and the use of legacy outcome results to justify or tune a calibration
    pin (EV-13 … EV-16; a violation that contaminates a pin is STOP-16, with its recovery sequence). The
    repository holds application results outside p_konum_plus/ (results/, possibly notebook outputs) whose
    class the drafter has not established; exposure of their content to the stopped session cannot be
    excluded by (3)
```

## 2. Decision — the PI chose B (§6); A and C are kept as presented

```text
common to every option
   - AUDITOR-SCOPE-01 is recorded as an auditor-side reading-scope incident. The information available shows no
     defect of the rp1-r2 package: no B, no K and no correction round is opened for the executor (D-11 r1 §6 is
     not engaged)
   - firewall: this record makes NO finding that no firewall-relevant content was seen, and none that it was.
     It records two things separately:
       (a) DISPLAYED, as reported by the stopped auditor: non-hash columns of the F1 input hash table, lines
           207–218 (a file inventory; protocol §5 places the F1 inventory among evidence allowed before F12)
       (b) OPENED, scope not established: the files the search read (under §1 (5), every non-ignored file of the
           audit directory) and any matching line beyond (a) that reached the session
   - the stopped session, and any session that has read its transcript, takes no further role in p_konum_plus
     (audit, drafting, execution or review). Its record (f3f24b6a…) is kept; its checks are claims to redo

A  CONTAINMENT: settle the firewall question now, without B's scope check, on three grounds the PI accepts:
   (i) the stopped session set no calibration pin, made no scientific choice and produced no package output;
   (ii) it, and any session that has read its transcript, takes no further role in p_konum_plus; (iii) this
   record is the provenance entry of the incident (protocol §9). The repeated audit then starts under §3
B  SCOPE FIRST, THEN DECIDE                                                                    [recommended]
   B-1 effective command. The PI (or a session named by the PI, other than the stopped one) establishes the argv
       the stopped command produced, WITHOUT reading any file: in the same shell type and version the stopped
       session used, run an argv-printing program with exactly the submitted arguments, e.g. in Windows
       PowerShell
         $PSVersionTable.PSVersion
         python -c "import sys; print(sys.argv[1:])" -n 'write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY' 'ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
       and record the output verbatim. Where it is available, add from the stopped session: the shell and
       version it used, the command string exactly as its tool call carried it, and the list of file paths and
       line numbers in its retained tool output — paths and line numbers only, no line content
   B-2 scope check. Count-only checks over the WHOLE commit (no pathspec), output file:count only, one with the
       effective pattern of B-1 and one with the intended pattern, e.g. in Git Bash
         git -C G:/PycharmProjects/rp1r2_audit/ref grep -c -E '<pattern>' 25c7d51
       (git grep reads the tracked files at the commit; both clones were clean at that commit, and both are
       clones of it, so one run covers both). No line content is printed, copied or republished
   B-3 PI evaluation. The PI evaluates B-1 and B-2 in a further signed PI record: the set of files whose lines
       could have reached the session; the protocol §5 class of each (raw SSA trajectory data EV-01, F1
       inventory, application code, application results whose class is to be established, …); and the
       consequence under protocol §9 (none; STOP-15 log; STOP-16 recovery). That record either finds the
       suspicion settled and opens the repeated audit under §3, or applies C
   until that record is signed: no repeated audit starts
C  STOP: no repeated audit until the PI has settled the firewall suspicion by a further record. C applies in
   any case if B-3 does not settle it. C does not cancel the project and does not mean the package is defective
```

## 3. Operating rules of the repeated audit (binding on the auditor with this record; they govern how files are read, not what is checked)

```text
O-0 these rules take effect only when the PI record of §2 B-3 (or, under A, this record) opens the repeated
    audit; that record may amend them
O-1 auditor: a NEW session in a NEW directory, e.g. G:\PycharmProjects\rp1r2_audit2; not the stopped session, not
    any session that has read its transcript, not the rp1-r1 auditor session, not the executor or the drafter.
    G:\PycharmProjects\rp1r2_audit is not used
O-2 clones: new clones at 25c7d51a0d14e8935f464a7a52d6a49ef4383e2b, made and recorded by the auditor
      ref\  SPARSE: only .gitattributes and p_konum_plus/ are checked out (non-cone patterns), so that data/,
            results/, notebooks/ and the application code are absent from the working tree. The root
            .gitattributes is kept because it checks out p_konum_plus/** with EOL conversion disabled. Commands
            (forward slashes and no leading "/" in the patterns, so that they work unchanged in PowerShell and in
            Git Bash, whose path conversion rewrites arguments that start with "/"):
              git clone --no-checkout --branch p_konum_plus https://github.com/onertartan/tartan-names.git G:/PycharmProjects/rp1r2_audit2/ref
              git -C G:/PycharmProjects/rp1r2_audit2/ref sparse-checkout set --no-cone .gitattributes p_konum_plus/
              git -C G:/PycharmProjects/rp1r2_audit2/ref checkout --detach 25c7d51a0d14e8935f464a7a52d6a49ef4383e2b
            expected: the working tree holds .gitattributes and p_konum_plus/ only; git status says "You are in a
            sparse checkout"; the transmission list and the harness have their listed hashes. (Drafter's test on
            a Linux clone of the same commit: 7,080 of 8,083 tracked files present, the only file outside
            p_konum_plus/ being .gitattributes; transmission list e48f5f6b…, harness 4d2e3db0….) Patterns
            without "/" match at any depth; the commit has no other directory named p_konum_plus and one other
            .gitattributes, p_konum_plus/.gitattributes, which is inside the kept tree anyway
      run\  FULL clone at the same commit, so that the re-run sees the same tree as the executor's worktree.
            run\ is executed in and compared by explicit path; it is never searched
    custody (audit instruction §1.1) is unaffected: the transmission list covers p_konum_plus/ only, and
    git diff reads objects, not the working tree
O-3 no recursive search and no directory-wide content read anywhere. Every command that reads or searches file
    content names its files explicitly. Run such reads from a Python script with argv lists (no shell
    expansion); before opening a path the script asserts that it lies in one of the allowed places below and
    not under any p_konum_plus\manifests\. Listing file NAMES is allowed. Allowed places:
      (a) ref\p_konum_plus\ and run\p_konum_plus\
      (b) probe\: the third copy of audit instruction §3.8, made like ref\ (sparse, O-2) — reads and probes
          inside probe\p_konum_plus\ only; the bans of this rule and of audit instruction §0 hold there too
      (c) inputs\: the files the PI hands over (§4), each with its sidecar, by name
      (d) audit_support\: the auditor's own scripts, evidence files and record drafts
      (e) git objects of commit 25c7d51 by named path (git show 25c7d51:<path>, git diff, git ls-tree names) for
          paths under p_konum_plus/ other than p_konum_plus/manifests/
      (f) the one named exception of O-4
    the Python interpreter's own library loading and the delivered programs' own reads are not auditor content
    reads (O-5). No regex or other argument containing a double quote is passed to a native program from
    Windows PowerShell 5.1 (§1 (5)); use a Python subprocess argv list
O-4 the one named exception to the manifests ban: the hash-column read of audit instruction §0 / §5.12 is done
    once, by one script that reads the input hash
    table with `git show 25c7d51:p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv`, selects the single
    column whose header names the hash, keeps only the set of hashes and prints only counts (entries,
    synthetic files, intersection). Its source goes into the audit record. No other read of
    p_konum_plus/manifests/ by the auditor
O-5 the rules bind the auditor's own reads. The harness, launcher and writer run as delivered; what they open
    is evidence through their own opened-file audit (audit instruction §5.13)
O-6 if any output shows content from outside the allowed places of O-3, or from p_konum_plus/manifests/ other
    than O-4's counts: stop, record path and line numbers without the content, report to the PI — as the
    stopped auditor did
```

## 4. Hand-over

```text
to the new auditor   : into inputs\ (O-3 (c)): the audit instruction (25eb0e16…) with its sidecar ; this record,
                       signed, with its sidecar ; optionally the stopped audit record (f3f24b6a…) with its sidecar
to the executor      : nothing now. This record and the audit records are placed in p_konum_plus/prompts/ with the
                       next dispatch record, as D-13 §3 did for the rp1-r1 audit
not handed over      : the drafter's handover note, earlier drafts, review comments
```

## 5. End state

```text
rp1-r2 status = PARTIAL_PENDING_PI (executor), audit NOT PASSED (stopped, incomplete) ; no ledger item changes ;
IR1-13 OPEN / B under D-14 ; firewall question open until the record of §2 B-3 (under B) ; no repeated audit before
it ; real_data_access = false ; F3_EXECUTION_READY = false ; commit = false
```

## 6. Signature

```text
PI                    = Öner
decision              = B  SCOPE FIRST, THEN DECIDE (§2 B-1 … B-3), as written in DRAFT r2
signature / approval  = APPROVED. The PI's message of 2026-10-12, verbatim (the opening quotation mark is part of
                        the message as received; it has no closing mark):
                        “D-15 DRAFT r2'yi B ile onaylıyorum
                        The approved content is DRAFT r2 (7320e0f1…); this final text differs from it only in the
                        title, the header lines, the §2 heading and §6 (§9). This final text was delivered to the
                        PI; the PI's forwarding it adopts it
date_time_local       = 2026-10-12 21:57, UTC+3 — the time the drafting session recorded the PI's message (command
                        output: `TZ=Europe/Istanbul date` → 2026-10-12 21:57 +03; UTC 2026-10-12T18:57:34Z). The
                        message's own send time is NOT OBSERVED by the drafter
```

## 7. Hashes and the argv simulation (computed in this session by script; command and output)

```text
$ git ls-remote origin refs/heads/p_konum_plus
25c7d51a0d14e8935f464a7a52d6a49ef4383e2b	refs/heads/p_konum_plus
$ sha256sum <files>  (repository files from git archive 25c7d51; others as named)
6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md
a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7  p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md
b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280  p_konum_plus/calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md
e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75  p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv
4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md
bb79d1763f10370dd25098f90737747f316e2a0e1a751bce213ec5f32f7d2f91  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_DRAFT_2026-10-12.md
ed0baedf90600a3c8135e44c4566cc836b0d19ee2e1346df394f3a6dcfdee7db  f3_realdata_prep_rp1-r2_AUDITOR-SCOPE-01_pi_decision_record_DRAFT_r1_2026-10-12.md
f3f24b6a7b889e0fa348d208ff7ec7f3478c97e1299059350adcf3b846628a72  f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-12.md

$ python3 ps51_argv_sim.py   (source below; a simulation of the hypothesis of §1 (5), not an observation of the stopped run)
command line: -n write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
argv[1] = -n
argv[2] = write_text|write_bytes|\.open\([wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py
```

```python
"""Simulate Windows PowerShell 5.1 native-argument passing, then MSVC-rule command-line parsing."""
pattern = r'write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY'
path = 'ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
def ps51_join(args):  # arguments without spaces are passed verbatim, embedded quotes included
    return ' '.join(('"%s"' % a) if (' ' in a or a == '') else a for a in args)
def msvc_split(s):    # backslashes literal unless before '"'; '"' toggles quoting
    out, cur, inq, i, have = [], [], False, 0, False
    while i < len(s):
        c = s[i]
        if c == '\\':
            j = i
            while j < len(s) and s[j] == '\\': j += 1
            n = j - i
            if j < len(s) and s[j] == '"':
                cur.append('\\' * (n // 2)); have = True
                if n % 2: cur.append('"'); i = j + 1
                else: i = j
            else:
                cur.append('\\' * n); have = True; i = j
            continue
        if c == '"':
            inq = not inq; have = True; i += 1; continue
        if c in ' \t' and not inq:
            if have: out.append(''.join(cur)); cur = []; have = False
            i += 1; continue
        cur.append(c); have = True; i += 1
    if have: out.append(''.join(cur))
    return out
line = ps51_join(['-n', pattern, path])
print('command line:', line)
for k, a in enumerate(msvc_split(line)): print('argv[%d] = %s' % (k + 1, a))
```

## 8. Changes

Changes from DRAFT r1 (ed0baedf…), made at the PI's direction before signature (the PI's message of 2026-10-12
relaying a recommendation; not a second review round)

| # | where | change | reason |
|---|---|---|---|
| 1 | §2 | the classification of the incident and the two-part firewall record (displayed / opened, scope not established) are common to all options; B no longer builds on A: B-1 effective command → B-2 whole-commit count-only checks → B-3 PI evaluation in a further record → repeated audit or C; no repeated audit before that record | DRAFT r1's B read "as A" and so inherited A's containment disposition and immediate audit |
| 2 | §1 (5) new, §7 | hypothesis on the effective argv (Windows PowerShell 5.1 passing + MSVC parsing), with the simulation's source and output; marked unverified | the stopped command's argv is NOT OBSERVED; the hypothesis explains the recursive search and gives B-1 a concrete test |
| 3 | O-0, O-1, O-3, §5, §6 | rules take effect only when a PI record opens the repeated audit; sessions that read the stopped transcript excluded; no double-quoted native argument from Windows PowerShell 5.1; end state and signature fields as for B | consequences of 1 and 2 |

Changes from the first DRAFT (bb79d176…) (section numbers as in DRAFT r1; r1's §1 (5) is r2's §1 (6)) — review relayed by the PI on 2026-10-12 (ChatGPT; the one review round of D-11 r1 §6)

| # | where | change | reason |
|---|---|---|---|
| 1 | §1 (3), new §1 (5), §2 | §1 (3) states only what the count-only check establishes and what it does not; §1 (5) places the exposed classes in the protocol's evidence firewall matrix; §2 A no longer finds that no firewall-relevant content was seen, but rests on containment (i)–(iii), which the PI must accept, else C applies; B is a narrowing check, not proof; C is defined | the DRAFT drew a firewall conclusion from a later, three-directory check of the intended pattern, while the stopped search's argv and opened files are NOT OBSERVED |
| 2 | O-3, O-4, O-6, §4, §6 | named, bounded exceptions: the third copy for probes (sparse, same bans), the PI's input files, the auditor's own support files, git objects by named path; O-4 marked as the one exception to the manifests ban | the DRAFT's O-3 also forbade reads that audit instruction §3.8 and the audit itself require |

No other change.

## 9. Changes from DRAFT r2 (7320e0f1…)

| # | where | change | reason |
|---|---|---|---|
| 1 | title, header | DRAFT r2 → signed; file name without DRAFT; drafts and status lines | PI approval |
| 2 | §2 heading | records that the PI chose B; A and C kept as presented | PI approval |
| 3 | §6 | decision B, approval message verbatim, time of recording | PI approval |

No other change: §1, §2 body, §3 – §5, §7 and §8 stand as in DRAFT r2.
