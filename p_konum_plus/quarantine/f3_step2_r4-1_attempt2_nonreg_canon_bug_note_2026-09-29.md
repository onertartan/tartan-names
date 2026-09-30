# p_konum_plus — F3 STEP-2 r4-1 — Attempt-2 Supersession Note (non-regression canon bug)

```text
artifact_role = supersession note for r4-1 attempt 2 (D-3 S8.3, harness-change).
                Records a bug in the R4A-01(f) NON-REGRESSION SELF-CHECK (not in
                any computation), its fix, and the whole-store quarantine that the
                harness change requires. RENAMES/MOVES nothing outside r4-1's own
                attempt artifacts.
status        = NON-NORMATIVE
date          = 2026-09-29
revision      = r4-1 (correction revision inside the r4 cycle)
```

## 1. What attempt 2 did and where it stopped

r4-1 attempt 2 (restart layer active; harness `280869892d…`) ran the ENTIRE
computation successfully:

```text
RUN1 and RUN2 completed (spline contexts 1..74; SCEN-A/B + all INJ fixtures)
EXC_CAPTURES_RUN1_EQ_RUN2 = True            (determinism gate: RUN1 == RUN2)
T_EXPECT_ALL = declared/ran 36/36 ; EXPECTATION_FAIL = []   (incl. the 3 new
              R4A-01 fixtures INJ-SPL-PENDING-FULL/FOLD/PROBE)
eval_level_dependent_criteria_pending: eval_level_ok = True (FULL->C3/C4b PENDING,
              FOLD->C2 PENDING, PROBE->C4b PENDING, C4a stays PASS, mechanism
              MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED))
T_SCHEMA = all fields populated ; NATURAL_UNRELATED_EVENTS = 0
```

It then **raised AssertionError at the T-NONREG-R4 self-check** (harness line
3180) and exited before writing results/residual/test-evidence. pid was
3348; start 2026-09-29T21:15:37; the run reached the assertion ~22:06 (≈51 min).

## 2. Root cause — a representation bug in the CHECK, not a regression

The R4A-01(f) non-regression check compared this run's IN-MEMORY `evals1`
(native Python floats, insertion-order dicts) against the **r4 results.json**,
which was written `json.dump(canon(results))` — i.e. floats already rendered as
`float.hex()` strings and dict keys sorted. The raw `!=` comparison therefore
flagged **33 of 34** shared fixtures as "changed" on `criteria` / `disc` /
`dp04` purely because `0.7` (float) `!=` `"0x1.6666666666666p-1"` (hex string)
and because key order differed. No decision or value actually changed:
T-EXPECT-ALL (36/36) and the determinism gate both passed in the SAME run.

Proof it is representational: applying `canon()` to BOTH sides of every one of
the 33 flagged fixtures collapses the diff to zero (checked on the attempt-2
non-regression CSV before the fix).

## 3. Fix (attempt 3 harness)

The non-regression comparison now canonicalizes BOTH sides before comparing:

```text
_cn(x) = json.dumps(canon(x), sort_keys=True)
changed = [k for k in proj if _cn(a[k]) != _cn(b[k])]
stops sorted by _cn ; CSV r4 / r4_1 columns emitted via _cn
```

Only a genuine value/decision change survives — e.g. R4A-03's INJ-U-POST
offending-pairs, which remains whitelisted as EXPECTED_R4A03. Nothing in any fit
or evaluation changed; the edit is confined to the post-computation self-check
block.

## 4. Whole-store quarantine (harness-change invariant)

Changing the harness changes its sha256 and therefore the code_env_fingerprint
that keys the restart store. Per the standing "quarantine-whole-on-harness-
change" rule, attempt 2's store is quarantined in full and attempt 3 starts from
an EMPTY store. Nothing is re-keyed; the 11,869 attempt-2 units are preserved
read-only, not reused.

| quarantined artifact | what it is |
|---|---|
| f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py | attempt-2 harness bytes (sha256 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2; recovered by reverting the single non-regression-block edit and verified byte-exact against the W-3 custody hash) |
| r4-1_restart_store_2026-09-29_ATTEMPT2_NONREG_CANON_BUG/ | attempt-2 restart store, 11,869 units, fingerprint b6fc376b049c20e1 |
| f3_step2_r4-1_attempt2_stdout_2026-09-29.log | attempt-2 stdout (RUN1/RUN2 complete; T_EXPECT 36/36; the 33-finding NONREGRESSION dump) |
| f3_step2_r4-1_attempt2_stderr_2026-09-29.log | attempt-2 stderr (scipy warnings + the T-NONREG-R4 AssertionError traceback) |

## 5. Response — attempt 3 (D-3 S8.3)

```text
harness attempt 3        = fixed non-regression check + attempt-3 metadata
RESTART_LAYER_ACTIVE     = True (retained; empty r4-1 store at attempt 3's start)
ATTEMPT_NUMBER           = 3
supersedes_harness_sha256 = 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2
supersedes_note_path      = this note
```

A fresh W-3 custody record (written outside the run process) names the attempt-3
harness/generator/manifest hashes and the new fingerprint before attempt 3 runs.
No r3, r4 or pre-existing quarantine file is modified, renamed or moved.

```text
deliverable_affected = NONE (attempt 2 wrote no results)
real_data_access = false
commit = false
```
