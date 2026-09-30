# Defect note — post-hoc exception classification always returns UNRELATED

- Found: during independent review of attempt 3's completed RUN1/RUN2 output (exit 0,
  RUN1==RUN2 determinism confirmed), one natural (non-injected) `RuntimeError` occurred —
  SCEN-A, sex F, trajectory 0, mask `run1:F0:full`, mode 113, stage 2, scipy `nnls`:
  "Maximum number of iterations reached." Traceback: `wrapped_accept -> accept -> kkt_res ->
  nnls -> wrapped_nnls(x2) -> scipy._nnls.nnls`. Classified `"kind": "UNRELATED"`. That
  traceback shape is exactly the PI-ratified §3.1 covered-event pattern (`accept` invoking
  `kkt_res`, whose own `nnls(A[act].T, g)` call raises), so an UNRELATED classification here
  was suspicious enough to check rather than accept.
- Root cause: `_classify_call_site()` was reused for two structurally different jobs — (1)
  live, pre-raise, inside `wrapped_nnls`, deciding whether to *inject* a fault (correct: at
  that point the real stack still contains `kkt_res`/`accept`, `inspect.stack()` sees them);
  and (2) post-hoc, inside `wrapped_accept`'s `except RuntimeError` block, deciding whether an
  *already-caught* exception is covered. (2) is broken: by the time an `except` clause runs,
  CPython has already unwound the frames between the raise point and the catch point off the
  live call stack — `kkt_res` and everything below it are gone. `inspect.stack()` called from
  the except block can therefore never see `kkt_res`, so `covered` was **always** `False`
  there, for every exception, injected or natural.
- Empirically verified (not just reasoned about) with an isolated repro before touching the
  harness — `inspect.stack()` from inside an except block shows `['classify', 'accept_like',
  '<module>']` (kkt_res_like/nnls_like already gone); the live pre-raise call from inside the
  raising function shows the full `['classify', 'nnls_live', 'kkt_res_live', 'accept_like2',
  '<module>']` chain. Confirmed `exc.__traceback__` frame order via `traceback.extract_tb`:
  outermost (catch point) first, innermost (raise point) last — `['accept_like',
  'kkt_res_like', 'nnls_like']`.
- Why the existing tests did not catch it: `T-EXC-CAPTURE-S1`/`-S2` only assert capture
  *count* and *stage* (`len(caps)==1 and caps[0]["stage"]==1`), which are appended
  unconditionally before the covered/uncovered branch — they never asserted `kind ==
  "COVERED"`. `UT-EXC-UNRELATED-REFERENCE` tests cases 1a/1b (no `accept` frame at all,
  correctly propagate) but never tested the *positive* case (genuinely covered, should
  convert) end-to-end through the except-handler path. Gap in test coverage, not just in the
  classifier.
- Fix: added `_classify_covered_from_traceback(tb)`, which walks `traceback.extract_tb(tb)`
  (the exception's own frame history, not the live post-unwind stack) and checks for the
  adjacent pair `"accept"` immediately followed by `"kkt_res"` — sufficient and precise per
  the frozen `kkt_res` source (`p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py:300-306`):
  its only call capable of raising `RuntimeError` is `nnls(A[act].T, g)`, so `accept` directly
  calling `kkt_res` is itself sufficient evidence the eventual `RuntimeError` (whatever depth
  of wrapper it passed through below `kkt_res`) originated at the covered site.
  `wrapped_accept` now calls this instead of `_classify_call_site()`. The live/pre-raise
  classifier (`_classify_call_site`, used only to decide *whether to inject*) is unchanged —
  that usage was already verified correct.
- Blast radius: this is a logic change (which caught exceptions get converted to "not
  accepted, continue searching" vs. propagate to "mode unverifiable"), not a cosmetic one — it
  can change which spline mode wins for any (fixture, mask, trajectory) pair that hits a
  natural or injected SOLVER-B exception. Exactly one such pair existed in the attempt-3
  output (cited above); everything else is far more likely than not unaffected, but that is
  not something to assert from reasoning about it — a full, honest re-run under the corrected
  classifier is required, not a hand patch of the one known-affected row.
- Action: attempt 2/3's harness, its W-3 custody record, and all four RUN1/RUN2 output
  artifacts (results, telemetry, residual series, test evidence) are quarantined byte-exact
  (verified via `sha256sum` before and after copy) under `*_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG`
  names in this directory — nothing produced under the pre-fix classifier is treated as valid
  and nothing is deleted.
  - harness  sha256 = `891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd`
  - custody  sha256 = `a4c7d65c8d778277b92e83e14a31a90a51b6e5e1df18f2c8da815d7ce00de0c0`
  - results  sha256 = `52e430aaae48be73e716fdf04d9a9b349978c9f5bd961332b366774533073972`
  - telemetry sha256 = `931a9640cb0feaa8e3a6c1ea2de9a2b126d25b5db2200a442124deaf89f313b4`
  - residual_series sha256 = `f28bd6a02978154d1ba71d83a8ffe42cdc5e95d12a26c43b886439cca19b94f5`
  - test_evidence sha256 = `14edaaa57eb3fce19bbb6d8158611ab70c3ad434169486266d3b090998282efc`
- Restart store: `p_konum_plus/calibration/.r3_restart_store_2026-09-22/` is left in place
  (not purged). Its ~7,943 entries are keyed under the pre-fix code/environment fingerprint;
  once the harness is edited its own hash changes, so the fingerprint changes, so every new
  key the corrected harness computes is disjoint from the old entries — they become inert,
  unreachable dead weight, not a source of silent contamination. Not worth the time to sweep.
- `commit = false`.
