# p_konum_plus - F3 STEP-2 r3 - Auditor Transmittal Note

```text
artifact_role = non-normative summary / navigation aid for the r3 deliverable package
status        = NON-NORMATIVE (nothing here overrides the hashed artifacts it points to)
date          = 2026-09-22
scope         = F3 STEP-2 adequacy evaluation, correction cycle r3
```

## 1. What r3 is

r3 closes the findings of an independent audit of the r2 package (Y-01..Y-21 of
`Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md` §6), on top of the v6
corrections r2 already carried (X-01..X-20). PI-ratified content (S-1, S-2, T-1..T-5) is
unchanged from D-2. Two new PI decisions specific to this cycle, read from D-4:

- `S-R2-1 = DEFERRED_THIS_CYCLE` — the "C4b criterion with no full-data reference" edge case
  is explicitly deferred (finding `F3-STEP2-EXACT-03`), not silently resolved either way.
- `T-R2-2 = AUTHORIZE_RESTART` — permits (does not require) introducing a checkpoint/restart
  layer, but only after a genuine execution interruption, and only with a fresh, disclosed
  pre-execution custody record once introduced.

## 2. Reading order

| # | File | Role |
|---|---|---|
| 1 | `provenance/f3_step2_r3_start_state_inventory_2026-09-22.md` | What existed before r3 started (W-1) |
| 2 | `prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md` (+`.sha256`) | The PI decisions that authorized this cycle |
| 3 | **this file** | Navigation + headline state |
| 4 | `provenance/f3_step2_r3_preexecution_custody_2026-09-22.md` | W-3: exact bytes executed (harness/generator/manifest hashes), written before any test ran |
| 5 | `calibration/f3_step2_adequacy_harness_r3_2026-09-22.py` + `f3_step2_fixture_generator_r3_2026-09-22.py` + `f3_step2_fixture_manifest_r3_2026-09-22.csv` | The code and frozen fixture list actually executed |
| 6 | `quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md` | Incident 1 (interruption) — see §3 |
| 7 | `quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md` | Incident 2 (classification defect) — see §3 |
| 8 | `calibration/f3_step2_results_r3_2026-09-22.json` | Final evaluation outcomes, all 34 fixtures |
| 9 | `calibration/f3_step2_telemetry_r3_2026-09-22.csv`, `..._residual_series_...json`, `..._test_evidence_...json` | Supporting evidence |

## 3. Two incidents occurred during execution. Both are disclosed, not hidden, and both are why the harness reached three source revisions before the results below were produced.

**Incident 1 — genuine external interruption (not a harness defect).** The first execution
attempt was terminated by the host process itself exiting mid-run, outside the harness's
control. No partial results existed (execution had not reached the results-writing stage), so
nothing was lost or reused incorrectly. A restart/checkpoint layer — pre-authorized by
`T-R2-2` but until this point unused, per design, since a restart layer may only be
introduced after a real interruption — was then activated, with a fresh, disclosed W-3
custody record. Full account: `quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md`.

**Incident 2 — a real defect, found by review before results were reported, not by the
auditor.** After a full run completed (exit 0, RUN1==RUN2 determinism confirmed), reviewing
its own output before reporting it turned up a genuine natural (non-injected) solver
exception whose classification looked wrong given its traceback shape. Root cause: the
covered-vs-unrelated classifier used `inspect.stack()` from inside an `except` block, which
in CPython only sees the call stack *after* the raising frames have already unwound — so it
could never actually detect the covered call site, for any exception. Verified empirically
(isolated repro) before touching the harness, fixed with a traceback-based classifier, then
verified again on both the positive and negative case in isolation, and finally on the real
natural exception in a fresh run. That run's harness, custody record, and all four output
artifacts were quarantined byte-verified rather than left looking valid. Full account:
`quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md`.

**Checkable fact, not an assertion:** the pre-fix and post-fix runs produced an *identical*
`RUN1_CANONICAL_SHA256` (`943d14abab4c4dd96425a502057fed3cbf2dc04a36232e37619d34a8646907ce`
in both). The misclassified mode was never the RSS-winning mode for that fit either way, so
this specific defect did not change any P03/mechanism conclusion in this run — but the
classification itself was still wrong and needed fixing on its own terms (§3.1 of the
PI-ratified content is exactness-critical by design, independent of whether any single run
happens to be numerically sensitive to it).

## 4. Headline results (from the final, verified run)

- **Non-regression gates:** NR-01(i)/(ii) PASS, spline non-regression PASS (30/30 rows),
  loader node-hash check PASS (73/73), masked-objective pins PASS.
- **Determinism:** RUN1 and RUN2 canonical hashes are equal
  (`943d14abab4c4dd96425a502057fed3cbf2dc04a36232e37619d34a8646907ce`).
- **Fidelity:** 4/4 declared units executed (no silent skips).
- **The two real (non-synthetic) scenarios:**
  - `SCEN-A` -> `RESOLVED_MECHANISM_P01`
  - `SCEN-B` -> `STOP_BOTH_FAIL_REDESIGN`
  - Neither real scenario hit the S-R2-1 deferred state — it only appears in the synthetic
    fixtures built specifically to exercise that code path (next bullet).
- **34 total evaluated fixtures** (2 real scenarios + 32 synthetic/injection fixtures that
  exercise individual criteria, edge cases, and contract checks): 7 resolved P-01, 13
  resolved P-02, 5 terminal-fallback P-01, 6 stopped (redesign or contract-violation), 3
  PENDING.
- **The 3 PENDING fixtures** — all synthetic, none are real-data findings:
  - `INJ-DP04-C1`, `INJ-C4B-NOREF` -> `MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-03)`
    — these two exist specifically to prove the S-R2-1 deferral fires correctly; they are the
    intended behavior of a deliberately deferred PI decision, not an unresolved bug.
  - `INJ-P03-C4PENDING-C5FAIL` -> `..._PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING)` — a
    test-only fixture that force-injects a pending state to verify the pending-propagation
    logic itself; not related to S-R2-1.
- **Open item carried forward:** `F3-STEP2-EXACT-03` (the C4b/no-full-data-reference state)
  remains formally deferred by `S-R2-1`. It is not resolved by r3 and is not claimed to be.

## 5. What the auditor can independently re-verify

- `sha256sum` every file in §2 against the hashes recorded in the W-3 custody record (item 4)
  and in `results.json`'s own hash-of-itself printed at run end — every value in this note is
  a direct quote of one of those, not a re-derivation.
- `RUN1_CANONICAL_SHA256 == RUN2_CANONICAL_SHA256` inside `results.json` — the determinism
  claim in §4.
- The quarantined pre-fix artifacts (`quarantine/*_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG_*`)
  are available for direct diff against the final ones, to confirm the canonical-hash-equality
  claim in §3 independently rather than taking it on trust.

`commit = false`.
