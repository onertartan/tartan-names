# Correction note — independent audit (claude-fable-5-1) findings P-1..P-7

- Trigger: `f3_step2_r3_independent_audit_claude-fable-5-1_PREFLIGHT_2026-09-23.md`, an
  auditor preflight on a partial (7-file) package. No verdict was reached (audit could not
  start without the harness/generator/manifest), but its `§4 Preliminary observations`
  identified real defects independently confirmed against the harness/generator source
  below — not accepted on the auditor's word alone.
- Scope: this note covers the SECOND correction round on top of the already-quarantined
  attempt-1 (interruption) and attempt-2/3 (exception-classification bug) supersessions.
  The harness/generator/manifest/custody/all four RUN1-RUN2 outputs from attempt 5 (the
  last clean, fully-verified run before this round) are quarantined here, alongside the
  full pre-round restart store (23,738 entries, all orphaned once the harness hash below
  changes; kept for provenance, not reused).

## Findings and fixes

**P-1 (residual export bypasses injmap).** Confirmed by re-reading the harness: the
RUN1 residual-series export called `fit_spline`/`fit_family` in a SEPARATE pass that never
consulted `injmap`, so an injected failure RUN1 itself correctly recorded (e.g.
SCEN-B:M0:SPL) silently re-succeeded in the export and was written as if valid — exactly
what produced a residual-series file byte-identical to the r2 parent despite r3's own
corrections. Fixed: `run_real_scenario` now captures the FULL-mask fit (ghat + validity +
x) it already computes, injection-aware, into `full_mask_fits`; the export reads those
captured values directly and makes zero fit_family/fit_spline calls (asserted:
`spline_telemetry_calls_by_phase["residual_export"] == 0`).

**P-2 (process provenance incomplete / undisclosed process boundary).** `nr_gates` and
`unit_tests` counters were declared but never incremented; no phase or pid tag existed on
per-call telemetry; the attempt-4 interruption (revision-3's first launch, before attempt
5 resumed it) was never recorded in any file, only in chat. Fixed: `CURRENT_PHASE` tags
every `SPLINE_TELEMETRY_CALLS` row with phase+pid+start_iso (preserved across restart-store
replay); NR gates and the unit-test block are now coarse-cached units with proper
computed/read-from-store counting; the attempt log (deliverable 12, written separately)
now names all process launches including the previously-undisclosed one.

**P-3 (per-call telemetry captured, never written).** `SPLINE_TELEMETRY_CALLS` held 6,856
real optimizer-call records; nothing serialized them, and the mode-level summary rows
pointed to "per-call rows" that existed nowhere. Fixed: written to
`f3_step2_spline_percall_telemetry_r3_2026-09-22.csv`, phase/pid-tagged; asserted
RUN1 per-call total == RUN2 per-call total (T-CALLCOUNT).

**P-4 (S2 exception test never exercised stage 2).** Confirmed by reading SOLVER-B's own
`solver_config` (`f3_spline_solver_qualification_harness_r2_2026-09-03.py:384-396`): stage
2 is only attempted if stage 1's `accept()` returns False, so forcing stage-1 failure
correctly reaches stage 2 -- but `NNLS_FAIL_TARGET` deactivated itself after its single
firing, so nothing was armed by the time the solver got there; the test asserted only
`count>=1`, which passed regardless. Fixed: `NNLS_FAIL_TARGET` now holds a set of target
stages, each firing exactly once within one `fit_spline` call; the assertion requires
exactly stages `[1, 2]`.

**P-5 (undefined flag ignores the spline side).** Confirmed against the generator's own
construction comment for `INJ-NAN-STAT-SPL` ("C2 undefined ... for BOTH families -- the
benchmark statistic is required by both"): `undefined` was `mf is None` (family side only),
so a spline-only corruption left `undefined=False` while `passed=False`. Fixed for C2 and
C4b (the two criteria with a spline-benchmark term): `undefined = (mf is None or ms is
None)`. C5 is unchanged (no spline term; family-absolute by design).

**P-6 / Y-08 (expectation_checks / T-EXPECT-ALL unimplemented).** The manifest had the
`expected_*` column headers but only `expected_mechanism_outcome` was ever populated,
and nothing in the harness read or checked them -- `results.json` had no end-state block
at all. Fixed: all 32 injection fixtures' `expect=` dicts extended with `p03`,
`resolved_level`, `U2..U5` (int or per-sex dict), `stops`, `undefined`, transcribed from
each fixture's own already-written construction prose (not fabricated after the fact).
SCEN-B got a construction-derived expectation (n_s=1 makes both families' failure
deterministic regardless of the non-injected sex's real numeric outcome -- reasoning
in the generator comment, not copied from a prior run). SCEN-A deliberately has none: a
genuinely emergent real-fit result with no injections has nothing to transcribe from.
`check_expectations()` now compares every declared field against the actual evaluation
and reports `EXPECTATION_FAIL` (never silently dropped); `results.json` gained
`expectation_checks` and a `end_state` block (the six v6 S13 status fields plus
`F3_STEP2_r3_status`).

**P-7 cleanup.**
- (a) the "C4b pass/fail (real)" coverage row claimed SCEN-B evidence that is actually
  PENDING under S-R2-1; corrected to name SCEN-A only, with the PENDING caveat stated.
- (d) fidelity was measuring trajectories processed (always 4/4) rather than SCEN-B's five
  DECLARED injection sites actually reached and recognized; redesigned around
  `(fixture_id, traj, family, context)` tuples read from `sc["injections"]` and confirmed
  live at each `injmap` consultation site.
- (b) no code change: Y-09 (naming D-4 path+hash as P-4's evidence) is a correction-report
  wording item, addressed there.
- (c) searched local files for the "no additional document types" PI instruction the
  auditor attributed to 2026-09-21; found only a different 2026-09-21 statement (frozen
  content preservation: v11/F2/F3 STEP-1/ratified decisions). Not resolved here -- flagged
  to the user/PI rather than guessed at further; the transmittal note stays, labelled
  NON-NORMATIVE, pending that clarification.

## Quarantined, byte-verified

- harness: `f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py`
  sha256 = `f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5`
- generator: `f3_step2_fixture_generator_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py`
  sha256 = `cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8`
- custody: `f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.md`
  sha256 = `e67bd9d79eed56f78092b460a54a586195ab72703ed937489872935c815d5905`
- manifest: `f3_step2_fixture_manifest_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.csv`
  sha256 = `4544ff7565165f7541c0264b886bc2692374caf2ee875ec65a877c1a2909ec33`
- results/telemetry/residual_series/test_evidence: `*_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.*`
  sha256 = `06210546d4d1053d33c229d30bd50a7b0eb65b2c879f5cb98e42ea1d62379b17` /
  `858eaf3b181d61a8cf0ee966f82d9e5ea4fbe3afdf98856806828cb100d01179` /
  `f28bd6a02978154d1ba71d83a8ffe42cdc5e95d12a26c43b886439cca19b94f5` /
  `f74459354d8526eefaaf6608e51c6caa5f69005a2525ec35f4299a8df36cd1c9`
- restart store: `r3_restart_store_2026-09-22_ATTEMPT1-5_PRE_AUDIT_P1-P7_CORRECTIONS/`
  (23,738 entries, moved whole; all orphaned once the harness/generator hashes below
  change -- kept for provenance, not because any entry is reusable)

`commit = false`.
