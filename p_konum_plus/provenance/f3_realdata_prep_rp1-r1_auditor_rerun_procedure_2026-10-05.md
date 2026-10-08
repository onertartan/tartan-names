# p_konum_plus — rp1-r1 — Auditor Re-Run Procedure (R-4 / RP1A-07)

```text
artifact_role = deliverable (rp1-r1 instruction §4 R-4): step-by-step procedure for an
                independent auditor to run the UNCHANGED rp1-r1 harness end to end
                against a disposable copy, closing RP1A-07's evidence limit
status        = NON-NORMATIVE procedure document
date          = 2026-10-05
applies_to    = f3_step2_adequacy_harness_rp1-r1_2026-10-05.py (attempt 1, this cycle)
binding_environment = Windows-10-10.0.19045-SP0 ; Python 3.11.7 ; numpy 1.26.4 ;
                      scipy 1.14.1 ; OMP/OPENBLAS/MKL thread pins = 1
```

## 0. What this procedure proves, and what it does not

Proves: the harness, run UNCHANGED by someone who did not write it, against a
disposable copy of the repository, reaches the SAME S-class scientific objects
(37 evaluation objects, every stop, the RUN1 canonical document, the residual
series, RUN1==RUN2) and the same mandatory-test pass/fail pattern the executor's
own run delivered. Does not prove: that the executor's environment caused any
observed difference (an environment difference is recorded, never treated as an
explanation) — see §3.

## 1. Isolation (before any run)

```text
1. Choose a separate directory, NOT the executor's working copy -- e.g.
   D:\rp1r1_audit_copy or any path outside G:\PycharmProjects\pkp-worktree.
2. Clone or copy the repository into it at the SAME commit the executor's package
   was delivered from (the rp1-r1 transmission list names the commit). Do not
   copy the executor's live restart store (p_konum_plus/calibration/.rp1-r1_restart_store_2026-10-05/)
   if it exists in the source tree at copy time -- the auditor's own store starts
   EMPTY (step 4 below); copying it would not be a fresh attempt.
3. If the executor's final-attempt custody record
   (p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md)
   is present in the copy, MOVE it out of the copy's provenance/ path into a
   kept-aside folder OUTSIDE p_konum_plus entirely (e.g. ..\kept_aside\). Do NOT
   edit it, rename it within the copy, or delete it. The W-3 writer (step 2
   below) refuses to run if a same-named custody file already exists at its
   target path -- this step is what makes the writer's refusal the auditor's
   OWN record, not an accidental overwrite of the executor's.
4. Confirm the copy's restart store directory
   (p_konum_plus/calibration/.rp1-r1_restart_store_2026-10-05/) does not exist.
   If step 2 left one behind, move it aside the same way as step 3 -- do not
   delete it (it is the executor's provenance, not the auditor's to discard).
5. Set the environment variable F3_REPO_ROOT to the ABSOLUTE path of the copy
   (R-4; rp1-r1 instruction, harness line ~94-96 and the W-3 writer's own
   REPO constant both read this variable, default unchanged). Every file the
   harness and the writer touch is then read and written INSIDE the copy only
   -- outputs never touch the executor's own directory.
```

## 2. Custody (the auditor's own W-3 record)

```text
1. With F3_REPO_ROOT pointed at the copy, run the delivered writer:
     F3_REPO_ROOT=<copy path> python p_konum_plus/calibration/_w3_writer_rp1-r1_tmp.py
   It refuses and stops if a custody file already exists at its target path
   (step 1.3 above is what prevents a false refusal here).
2. The writer re-verifies, from the COPY's own files, every standing instrument
   the rp1-r1 harness's own precondition list checks (D-11 r1, D-9, D-10, the rp1
   instruction, the rp1 harness, the rp1 transmission list, the rp1-r1
   instruction, D-12, the rp1 audit record, the rp1-r1 DRAFT review, D-3/A-1/D-2/
   D-6/A-2/A-3/D-7/A-4/D-8/A-5, the reused generator and manifest, the r4-1/r4-2
   baselines, the F1 freeze record) and STOPS on any mismatch -- a copy made from
   a different commit or with a missing file is caught here, before any run.
3. Run the harness with a launch number NOT previously used by the auditor
   (start at 1 for the auditor's own first launch; the harness's environment
   guard, line ~3618-3624, refuses to run without F3_RP1R1_LAUNCH set):
     F3_REPO_ROOT=<copy path> F3_RP1R1_LAUNCH=1 python \
       p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py \
       > <copy>/p_konum_plus/calibration/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log \
       2> <copy>/p_konum_plus/calibration/f3_step2_rp1-r1_launch1_stderr_2026-10-05.log
4. The harness's own environment-recording block (process.python/.numpy/.scipy/
   .platform/.OMP/.OPENBLAS/.MKL) runs in the auditor's process exactly as it
   does in the executor's; no additional guard is needed beyond what the
   harness already does -- the comparison in §3 reads these fields from the
   auditor's own delivered results.json.
```

## 3. Compare

```text
1. S-class (MANDATORY, no exception for any environment): read
   auditor_results.json and the executor's delivered results.json side by side.
     - evaluations: every fixture_id, every field, canon-compared (order-
       independent by construction -- both sides re-key by fixture_id)
     - stops: canon-sorted list compared as a set
     - run1_canonical_sha256 == run2_canonical_sha256 == the executor's delivered
       value (determinism AND cross-process reproduction, both required)
     - residual_series: the delivered residual_series_rp1-r1_*.json, re-hashed,
       equal to the executor's
   AN S DIFFERENCE IN THE AUDITOR RUN IS A FAILURE WHATEVER THE ENVIRONMENT.
   It means T-NONREG-R4-2 itself would have failed had it run against this as
   its baseline; treat it exactly as the D-11 r1 §5 STOP behaviour for an
   undeclared scientific-object difference -- the matter goes to the PI. Do
   NOT accept "the environment differs" as a closing explanation, and do NOT
   apply D-11 r1 §6's "devam" / "kayıtlı sınırlılık" options to an S finding.
2. Mandatory tests: every entry of MANDATORY_TESTS (35 for rp1, +3 for rp1-r1 =
   38) must show {"ran": true, "passed": true} in the auditor's tests_run,
   exactly as in the executor's delivered tests_run. A test that ran but
   disagreed on passed/failed between the two runs is itself investigated as
   a possible S-adjacent finding (the test exists specifically to prove a
   scientific or structural invariant).
3. T-NONREG-R4-2 itself: the auditor's own run already compares its results
   against the SAME frozen r4-2 baseline (R4_2_RESULTS_HASH etc., pinned in the
   harness, unaffected by F3_REPO_ROOT). Confirm the auditor's own
   nonregression_vs_r4_2 shows s_findings=0 and u_findings=0, matching the
   executor's.
4. Environment: read environment.python/.numpy/.scipy/.platform/.OMP/.OPENBLAS/
   .MKL from the auditor's own results.json, side by side with both (a) the
   executor's delivered values and (b) the binding environment line at the top
   of this document. Record every field, matched or not. Running in a
   DIFFERENT environment does NOT guarantee identical S values -- if the
   auditor's environment differs from the binding one, that is recorded as a
   material fact, but it does NOT excuse an S difference (§3.1) and does NOT by
   itself invalidate a clean result (matching S values in a different
   environment is still informative, just not as strong as a matched-
   environment match). The procedure RECOMMENDS matching the binding Python /
   numpy / scipy versions before drawing conclusions from any difference; a
   report to the PI describing an environment mismatch alone never satisfies
   the equality condition of §3.1.
5. R-3's non-regression artifacts: diff the auditor's
   f3_step2_rp1-r1_nonregression_vs_r4-2_*.csv against the executor's row by
   row (same path/classification/reason/r4_2/rp1 schema); any row present in
   one and not the other, or with a different classification for the same
   path, is itself a U-class finding on this procedure's own output.
```

## 4. What the executor did with this procedure (dry check only, not an audit)

Per rp1-r1 instruction §4 R-4's own closing sentence ("The executor runs the
procedure once itself in a second directory... as a dry check that it works
end to end — not as an audit"): on 2026-10-08, AFTER attempt 2's primary run
completed, the executor ran §1 (isolation) and §2 (custody + launch) of this
procedure once, on this same machine, in a second directory
(`G:\rp1r1_dry_check\pkp-copy`, a robocopy of the working tree excluding `.git`,
the quarantined restart-store directories, the live rp1-r1 store and the rp1
zip). Observed, in order: (1) the delivered W-3 writer, with `F3_REPO_ROOT`
pointed at the copy, REFUSED to run while the executor's attempt-2 custody
record was present in the copy (the §1.3 behaviour, confirmed live); (2) after
both executor custody records were moved to a kept-aside folder outside
`p_konum_plus`, the writer wrote the copy's OWN custody record (same harness
hash `cac93ac6…`, same fingerprint `29de6089…`; its own sha256 `892076fc…`,
differing from the executor's record only through the `F3_REPO_ROOT` line);
(3) the unchanged harness, launched in the copy with `F3_RP1R1_LAUNCH` set,
VERIFIED that custody record and passed ALL 31 dispatch preconditions and the
NR-01(i)/(ii) and NR-SPL gates, writing store units and logs ONLY inside the
copy — the executor's own repository was untouched throughout (its live store
and logs unmodified). The dry-check process was then STOPPED deliberately
(SIGTERM) after the gates: the dry check validates the procedure's isolation,
custody and launch mechanics end to end; the full-length (~12 h on this
hardware, §3 of the attempt log) computation was intentionally NOT repeated,
because a second full run by the SAME executor on the SAME machine adds no
audit evidence — the full re-run is precisely the auditor's step. The copy and
the kept-aside folder were deleted afterwards (disposable, per §1); the
evidence lines are quoted in the attempt log. This dry check is NOT a
substitute for §3's comparison, which only an auditor who did not write or run
the primary attempt may perform.

```text
real_data_access = false ; commit = false
```
