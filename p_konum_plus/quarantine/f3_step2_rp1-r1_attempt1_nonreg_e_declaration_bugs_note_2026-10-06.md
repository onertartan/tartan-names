# p_konum_plus — rp1-r1 — Attempt-1 Supersession Note (R-3 E-declaration bugs)

```text
artifact_role = supersession note for rp1-r1 attempt 1. Records three bugs in the
                R-3 (RP1A-03) non-regression comparison logic ITSELF -- not in any
                computation it checks -- their fixes, and the whole-store
                quarantine the harness change requires.
status        = NON-NORMATIVE
date          = 2026-10-06
revision      = rp1-r1 (first B-correction cycle of rp1)
```

## 1. What attempt 1 did

rp1-r1 attempt 1 (pid 34228, harness `4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d`)
ran the ENTIRE computation successfully: all 31 preconditions EQUAL; `T-F1-LOADER-SYNTH`
passed all 21 cases including the 8 new R-2 branches (RAW_FILE_MISSING, BAD_SEMANTICS,
NONFINITE_PRE_Z×2, NEGATIVE_SHARE, NONFINITE_POST_Z, Z_STD_QC, Z_NORM_QC);
`T-F1-HANDOFF-SYNTH` passed (144/144 real-mode contexts, x-hashes matched the loader's
arrays); `T-CONTEXT-ID-UNIQUE` (replacing rp1's) passed on the actually-captured ids;
`DETERMINISM=True` (RUN1==RUN2, unchanged canonical hash); residual series unchanged.

It then **raised `AssertionError` at `T-NONREG-R4-2`** with `s_findings=[]` (the
scientific content was already correct) and **6 U findings**, all representational
bugs in the comparison code itself:

```text
end_state.narrowed_evidence              -- declared COUNT, not held
exc_injection_fixtures                   -- not declared (path collision)
test_evidence.exc_captures               -- declared EQUAL, not held
test_evidence.exc_captures_run2          -- declared EQUAL, not held
test_evidence.exc_captures_unit_phase    -- declared EQUAL, not held
test_evidence.exc_injection_fixtures     -- declared EQUAL, not held
```

## 2. Root cause — three bugs in the R-3 comparison logic, not in any computation

1. **COUNT kind double-canonicalization.** `_flatten_leaves` stores every leaf as an
   ALREADY-canonicalized JSON string (`_cn(obj)`). `_expectation_held`'s COUNT branch
   re-applied `_cn()` to that string (`_cn(a_val)`), which canon-dumps a STRING (just
   re-quoting it) and can never equal `_cn(exp_a)` (canon-dumps of the raw declared
   list). `end_state.narrowed_evidence` is the only COUNT-kind declaration, so this
   is the only path it affected.
2. **`exc_injection_fixtures` path collision between the two compared files.**
   `_flatten_leaves` treats any EXACT key match against `EXPECTATIONS_E` as a stop
   point (the whole subtree compared as one value). `EXPECTATIONS_E` is ONE shared
   dict for both results.json and test_evidence.json. A bare `"exc_injection_fixtures":
   ("EQUAL", ...)` entry, intended only for test_evidence.json's copy, ALSO stopped
   results.json's comparison at the same key -- so results.json's
   `exc_injection_fixtures.pass_key_namespaces_disjoint` (correctly declared ADDITION
   as its own leaf) was never reached; the whole subtree was compared as one value
   instead, which of course differs (rp1-r1 adds that one new field).
3. **`exc_captures` / `exc_captures_run2` / `exc_captures_unit_phase` declared EQUAL
   instead of provenance-stripped.** These three test_evidence.json fields hold
   capture records with their OWN per-process provenance (pid, start_iso, and a
   traceback naming the harness file by path) -- exactly the same shape
   `solver_exceptions` already has, which the harness already compares with those
   three fields stripped. The new fields were declared as a naive whole-value EQUAL,
   which fails on provenance alone even when content is identical.

None of the three bugs touched any computation, evaluation, stop, canonical
document, residual series, or determinism result -- `s_findings` was `[]`.

## 3. Fix (attempt 2 harness)

1. `_expectation_held`'s COUNT branch no longer re-canonicalizes `a_val`/`b_val`
   (already canon strings); only the declared literals `exp_a`/`exp_b` are
   canonicalized for comparison.
2. The bare `"exc_injection_fixtures": ("EQUAL", ...)` entry is REMOVED from
   `EXPECTATIONS_E` entirely (for both files' comparisons) -- it needed no
   declaration at all: with the collision gone, `_flatten_leaves` recurses into it
   normally for both files, `exc_injection_fixtures.pass_key_namespaces_disjoint`
   is reached and correctly classified ADDITION by its own leaf declaration, and
   every other sub-field (S1/S2/UNRELATED_TYPE/passes_identical/pass2/eval_level_ok/
   pass_) is unchanged content that matches silently (no declaration needed where
   nothing differs).
3. `_solver_exceptions_content_equal` generalized to
   `_provenance_stripped_content_equal`, applied to a new set
   `_PROVENANCE_STRIPPED_LIST_PATHS = {"solver_exceptions", "exc_captures",
   "exc_captures_run2", "exc_captures_unit_phase"}` instead of a single
   hard-coded path check.

All three fixes verified BEFORE the rerun, against real data, not just reasoning:
(a) reconstructed attempt-1's exact bytes by reverting the three edits and confirmed
the hash equals the custody record's pinned value (`4bffb33a…`) exactly; (b) re-ran
the corrected comparison logic standalone against the REAL delivered
`test_evidence_rp1-r1` and `test_evidence_r4-2` files: 0 U findings (was 3, plus the
collision); (c) a synthetic COUNT check (`["T-R2-2"]` → `["T-R2-2","T-RP-1"]`) now
holds; (d) a synthetic ADDITION check on `exc_injection_fixtures.pass_key_namespaces_disjoint`
now holds and is reached (collision gone).

## 4. Whole-store quarantine (harness-change invariant)

Changing the harness changes its sha256 and therefore the `code_env_fingerprint`
that keys the restart store. Per the standing "quarantine-whole-on-harness-change"
rule, attempt 1's store and every file it wrote are quarantined in full and
attempt 2 starts from an EMPTY store.

| quarantined artifact | what it is |
|---|---|
| `f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py` | attempt-1 harness bytes (sha256 `4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d`; recovered by reverting the three edits above and verified byte-exact against the custody record's pinned hash) |
| `rp1-r1_restart_store_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS/` | attempt-1 restart store (all pid 34228) |
| `f3_step2_rp1-r1_launch1_stdout_2026-10-05.log` / `..._stderr_...log` | attempt-1's launch-1 logs |
| `ATTEMPT1_NONREG_E_DECLARATION_BUGS_*` (9 files) | attempt-1's complete written output set (results.json was NOT written -- the process stopped before that write; test_evidence/residual/telemetry/percall-telemetry/store-manifest/store-read-log/3 nonregression CSVs all were) |

## 5. Response — attempt 2

```text
harness attempt 2        = three R-3 comparison-logic fixes only; no R-1/R-2/R-4/R-5
                            code touched
RESTART_LAYER_ACTIVE     = True (unchanged; T-RP-1 ACTIVE_FROM_START applies to
                            every attempt of this cycle)
ATTEMPT_NUMBER           = 2
supersedes_harness_sha256 = 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d
supersedes_custody_sha256 = dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d
supersedes_note_path      = this note
```

A fresh W-3 custody record (written outside the run process) names the attempt-2
harness/generator/manifest hashes and the new fingerprint before attempt 2 runs,
with a launch number (2) not previously used in this cycle. No rp1, r4-2, r4-1, r4,
r3, or pre-existing quarantine file is modified, renamed or moved.

```text
deliverable_affected = NONE (attempt 1 wrote no results.json)
real_data_access = false
commit = false
```
