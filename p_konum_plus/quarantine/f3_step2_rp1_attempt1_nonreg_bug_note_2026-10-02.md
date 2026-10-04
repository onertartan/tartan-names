# p_konum_plus — F3 real-data preparation rp1 — Attempt-1 Supersession Note (T-NONREG-R4-2 bookkeeping bug)

```text
artifact_role = supersession note for rp1 attempt 1. Records a bug in the T-NONREG-R4-2
                SELF-CHECK (not in any computation), its fix, and the whole-store
                quarantine the harness change requires. RENAMES/MOVES nothing outside
                rp1's own attempt artifacts.
status        = NON-NORMATIVE
date          = 2026-10-02
revision      = rp1 (F3 real-data preparation cycle, inside the r4 lineage)
```

## 1. What attempt 1 did and where it stopped

rp1 attempt 1 (pid 11116, harness `08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2`)
ran the ENTIRE computation successfully: 25/25 preconditions EQUAL;
`T-F1-LOADER-SYNTH`, `T-CONTEXT-ID-UNIQUE`, `T-INADMISSIBLE-OBSERVABLE`,
`T-STORE-READ-ACCOUNTING` all passed in-run; `T-EXPECT-ALL 36/36`;
`EXC_CAPTURES_RUN1_EQ_RUN2 = True`; `DETERMINISM = True`
(RUN1 == RUN2 == `556106e7...`, the r4-1/r4-2 value, unchanged);
residual series `3ee624f3...` (unchanged); `COVERAGE_DERIVED = 64 rows,
downgraded = []`; `NONREGRESSION_VS_R4_1 = 37 compared, 0 findings`.

It then **raised `AssertionError` at the `T-NONREG-R4-2` self-check** (D-9 §2(a)
binding) and exited before writing results/residual/test-evidence. The
assertion's own printed detail already showed `s_findings=[]` — the
**scientific content was already byte-identical to r4-2, no whitelist** — and
exactly 4 `U` (unexpected) findings, all representational:

```text
end_state.corrections_complete        : r4-2=true  rp1=false
end_state.mandatory_tests_all_run      : r4-2=true  rp1=false
end_state.mandatory_tests_missing      : r4-2=[]    rp1=["T-KEY-NAMESPACE", "T-NONREG-R4-2"]
solver_exceptions                      : r4-2=[{...pid 10412...}]  rp1=[{...pid 11116...}]
```

## 2. Root cause — three representation/bookkeeping bugs in the CHECK, not in any computation

1. **`T-KEY-NAMESPACE` was never recorded.** It was added to `MANDATORY_TESTS`
   (rp1 instruction §4 C-2(ii)) but no `record_test("T-KEY-NAMESPACE", ...)`
   call existed anywhere in the harness — only the underlying
   `assert pass_keys_disjoint` ran (and passed), with no test-registry entry.
   `mandatory_tests_all_run` was therefore false by construction, regardless
   of anything else.
2. **Three `end_state` fields are computed from `TESTS_RUN` *before*
   `T-NONREG-R4-2` records itself** (the dict literal that builds `results`,
   including `end_state`, runs to completion before the non-regression
   check that comes after it). At the moment `T-NONREG-R4-2` compares
   `results` against r4-2, those three fields read a necessarily-stale
   snapshot (`T-NONREG-R4-2` cannot yet be `ran=True` in its own precondition
   for running). Harness's `main()` already refreshes these three fields
   immediately after recording the test and before writing `results.json` —
   but the *live comparison* has no way to see that future state, so it
   needs an explicit declaration that this staleness is expected.
3. **`solver_exceptions` was diffed as a whole value.** It holds one
   natural `COVERED` optimizer event (`SCEN-A F0 full mode 113`,
   `"Maximum number of iterations reached."`) that reproduces byte-identically
   under the unchanged frozen engines — except for its own provenance
   (`pid`, `start_iso`, and the `traceback` string, which names the harness
   file by path and therefore differs between `f3_step2_adequacy_harness_r4-2_...py`
   and `f3_step2_adequacy_harness_rp1_...py`). The blanket top-level diff
   does not strip those fields before comparing, so it reported a `U`
   finding on a provenance-only difference.

None of the three bugs touches any evaluation, stop, canonical document,
residual series, or determinism result — `s_findings` was `[]` in attempt 1
and remains the authoritative evidence that the scientific content did not
move.

## 3. Fix (attempt 2 harness)

1. `record_test("T-KEY-NAMESPACE", pass_keys_disjoint)` added at the one
   point in the harness where two *different* executions of the same
   fixture ids run in one process (the two INJ-EXC passes, C-2(i)).
2. `EXPECTATIONS_E` gains three declared paths —
   `end_state.corrections_complete`, `end_state.mandatory_tests_all_run`,
   `end_state.mandatory_tests_missing` — each reasoned as "stale at
   comparison time by construction; refreshed immediately after, before the
   results file is written". Declaring them `E` does not change what is
   *delivered* (the refresh logic was already correct and unchanged); it
   only lets the live comparison treat their necessary staleness as
   expected rather than unexpected.
3. `solver_exceptions` is now compared via `_solver_exceptions_content_equal`:
   both sides have `pid`/`start_iso`/`traceback` stripped before the
   canon-sorted comparison. A genuine content change (fixture, mode,
   exception type, message, stage, sex, mask_id, phase, `s2_rule`) still
   surfaces as a real `U` finding; only the three provenance fields are
   exempted.

## 4. Whole-store quarantine (harness-change invariant)

Changing the harness changes its sha256 and therefore the
`code_env_fingerprint` that keys the restart store. Per the standing
"quarantine-whole-on-harness-change" rule, attempt 1's store is quarantined
in full and attempt 2 starts from an EMPTY store.

| quarantined artifact | what it is |
|---|---|
| `f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py` | attempt-1 harness bytes (sha256 `08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2`; recovered by reverting the three edits above and verified byte-exact against the W-3 custody hash — no edit was made without a prior quarantine copy of what preceded it, this note being that copy, produced retroactively and hash-proven) |
| `rp1_restart_store_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG/` | attempt-1 restart store, 12,453 units, fingerprint `64b35e0777fdbb52` |
| `f3_step2_rp1_launch1_stdout_2026-10-02.log` | attempt-1 stdout (full run; the four printed `U` findings) |
| `f3_step2_rp1_launch1_stderr_2026-10-02.log` | attempt-1 stderr (scipy warnings + the `T-NONREG-R4-2` `AssertionError` traceback) |

## 5. Response — attempt 2 (D-3 §8.3)

```text
harness attempt 2        = fixed T-NONREG-R4-2 bookkeeping (3 fixes above)
RESTART_LAYER_ACTIVE     = True (unchanged; T-RP-1 = ACTIVE_FROM_START applies to
                           every attempt of this cycle, not just the first)
ATTEMPT_NUMBER           = 2
supersedes_harness_sha256 = 08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2
supersedes_note_path      = this note
```

A fresh W-3 custody record (written outside the run process) names the
attempt-2 harness/generator/manifest hashes and the new fingerprint before
attempt 2 runs. No r3, r4, r4-1, r4-2, or pre-existing quarantine file is
modified, renamed or moved.

```text
deliverable_affected = NONE (attempt 1 wrote no results)
real_data_access = false
commit = false
```
