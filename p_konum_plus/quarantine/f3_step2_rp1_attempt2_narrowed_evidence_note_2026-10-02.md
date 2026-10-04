# p_konum_plus — F3 real-data preparation rp1 — Attempt-2 Supersession Note (narrowed_evidence defect)

```text
artifact_role = supersession note for rp1 attempt 2. Records a defect in a DELIVERED
                results field (not a provenance document), its fix, and the
                whole-store quarantine the harness change requires. RENAMES/MOVES
                nothing outside rp1's own attempt artifacts.
status        = NON-NORMATIVE
date          = 2026-10-02
revision      = rp1 (F3 real-data preparation cycle, inside the r4 lineage)
```

## 1. What attempt 2 did

rp1 attempt 2 (pid 13328, harness
`0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5`) ran the
ENTIRE computation to a **clean exit 0**: 25/25 preconditions EQUAL;
`T-EXPECT-ALL 36/36`; `EXC_CAPTURES_RUN1_EQ_RUN2 = True`;
`DETERMINISM = True` (RUN1 == RUN2 == `556106e7...`, unchanged);
residual series `3ee624f3...` (unchanged); `COVERAGE_DERIVED = 64 rows,
downgraded = []`; **`T-NONREG-R4-2` passed cleanly** (`s_findings=0,
e_declared=36, u_findings=0` — the fix from the attempt-1 note held);
36/36 recorded tests passed; `results.json` (sha256
`bdcfa38a9b92e56b67db1b2695d46d20d107d3c9e865d154865ec8dea0d2234f`) and every
other deliverable were written.

## 2. The defect found in post-run verification

Before packaging deliverables, the executor re-read the rp1 instruction's
C-6: **"T-RP-1 enters narrowed_evidence by value, as T-R2-2 did."** The
harness's own comment already stated this rule, but no code implemented it:
no `T_RP_1` constant existed, and the `narrowed_evidence` computation in the
`results = dict(...)` literal only ever added `"T-R2-2"`. The delivered
attempt-2 `results.json` therefore has
`end_state.narrowed_evidence = ["T-R2-2"]`, missing `"T-RP-1"`.

**Scope of the defect.** It does not change `F3_STEP2_r4_status`:
`narrowed_evidence` was already non-empty (`["T-R2-2"]`), so the status was
already `PARTIAL_PENDING_PI` with or without the missing value — the
`end_state` block is otherwise exactly as expected. The defect is a
disclosure gap in one delivered field, not a decision that moved. It does
**not** touch any evaluation, stop, canonical document, residual series, or
determinism result — `s_findings` was `[]` in attempt 2 and remains the
authoritative evidence that the scientific content did not move.

**Why fixed by rerun, not by an erratum note.** Unlike R4A-10/R41A-05 (which
corrected a *provenance narrative* — text describing bytes, not a field the
harness itself computes and delivers), `end_state.narrowed_evidence` is a
value the harness code **produces and writes into `results.json`**. The
precedent inside this same lineage is R41A-03 (the r4-1 harness named the
wrong dispatch record in `end_state.PI_dispatch_record_hash`), which was
fixed by a harness change and a full rerun in r4-2, not by a note alone. The
same treatment applies here.

## 3. Fix (attempt 3 harness)

1. `T_RP_1 = "ACTIVE_FROM_START"` added as a module constant, read from
   D-10 §2, mirroring `T_R2_2`.
2. `narrowed_evidence` now concatenates `["T-R2-2"]` (if `T_R2_2 ==
   "AUTHORIZE_RESTART"`) with `["T-RP-1"]` (if `T_RP_1 ==
   "ACTIVE_FROM_START"`) — the same presence-of-the-PI-value check pattern
   as `T-R2-2` already used, not a check of whether the layer was actually
   exercised this attempt (consistent with how `T-R2-2` has always been
   computed in every prior cycle since r4).
3. `EXPECTATIONS_E` gains `"end_state.narrowed_evidence"`, declared because
   rp1's two-value list is an **expected addition** over r4-2's one-value
   list, not a scientific regression.

## 4. Whole-store quarantine (harness-change invariant)

Changing the harness changes its sha256 and therefore the
`code_env_fingerprint` that keys the restart store. Per the standing
"quarantine-whole-on-harness-change" rule, attempt 2's store and its
now-superseded deliverables are quarantined in full and attempt 3 starts
from an EMPTY store.

| quarantined artifact | what it is |
|---|---|
| `f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py` | attempt-2 harness bytes (sha256 `0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5`; recovered by reverting the three fixes above and verified byte-exact against the W-3 custody hash) |
| `rp1_restart_store_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING/` | attempt-2 restart store, 12,453 units, fingerprint `d2ee833b4bad9138` |
| `f3_step2_rp1_launch2_stdout_2026-10-02.log` / `..._stderr_...log` | attempt-2's launch logs (the clean exit-0 run) |
| `ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_results_rp1_2026-10-02.json` and the other 8 now-superseded attempt-2 deliverables (residual series, test evidence, telemetry, per-call telemetry, store manifest, 3 non-regression CSVs) | the complete attempt-2 output set, preserved whole rather than deleted |

## 5. Response — attempt 3 (D-3 §8.3)

```text
harness attempt 3        = adds T_RP_1 + narrowed_evidence fix + one EXPECTATIONS_E entry
RESTART_LAYER_ACTIVE     = True (unchanged; T-RP-1 = ACTIVE_FROM_START applies to
                           every attempt of this cycle)
ATTEMPT_NUMBER           = 3
supersedes_harness_sha256 = 0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5
supersedes_note_path      = this note
```

A fresh W-3 custody record (written outside the run process) names the
attempt-3 harness/generator/manifest hashes and the new fingerprint before
attempt 3 runs. No r3, r4, r4-1, r4-2, or pre-existing quarantine file is
modified, renamed or moved.

```text
deliverable_affected = end_state.narrowed_evidence only (all other fields
                        expected unchanged, scientific content proven unchanged
                        by attempt 2's s_findings=0 before this rerun)
real_data_access = false
commit = false
```
