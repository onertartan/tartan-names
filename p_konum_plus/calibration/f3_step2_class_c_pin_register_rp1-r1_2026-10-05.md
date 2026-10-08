# p_konum_plus — F3 real-data preparation rp1-r1 — CLASS_C Pin Register (2026-10-05)

```text
artifact_role = CLASS_C implementation-pin register for the rp1-r1 B-correction cycle
                (deliverable 9, rp1-r1 instruction §7; carries RP1A-04's record part)
status        = NON-NORMATIVE
parent        = f3_step2_class_c_pin_register_rp1_2026-10-04.md
                dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066
frozen_contract = r4 5e594136 AS RATIFIED BY freeze record r1 7055f186 ; v11 wins (unchanged)
harness       = f3_step2_adequacy_harness_rp1-r1_2026-10-05.py
                cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb (attempt 2)
                child of the rp1 harness 39c733a3…, itself the child of r4-2 b988e962…
generator     = f3_step2_fixture_generator_r4-1_2026-09-29.py — REUSED UNCHANGED
                68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
manifest      = f3_step2_fixture_manifest_r4-1_2026-09-29.csv — REUSED UNCHANGED
                5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
PI dispatch record (D-12) = f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md
                2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364
S-R2-1 source (D-5)       = 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
PI fields (D-12 §2) = PI-a RP1A-01/02/03 = B ; PI-b family in every real-mode (fixture_id,
                mask_id) ; PI-c consumer change only at trajectory/mask-id intake ;
                PI-d RP1A-04+06 ride along. Carried: T-RP-1 ACTIVE_FROM_START ; S-e ; S-f
scientific_freedom in every row = none ; new scientific literal additions by executor = 0
Every row is stated against the rp1-r1 attempt-2 run (pid 34588, 2026-10-07→08, exit 0;
RUN1 == RUN2 canonical 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77,
unchanged since r4-1; results e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb);
result = executor claim, independent verification pending (rp1-r1 instruction §10).
```

## Retained from rp1 unchanged (re-verified against the rp1-r1 attempt-2 run)

Every pin of the rp1 register ran and passed in the rp1-r1 run and is implemented as its
parent row describes, EXCEPT the rows amended/added below. rp1-r1 touches ONLY R-1…R-5 and
the cycle wiring (both delivered diffs show every hunk labelled; the vs-rp1 diff contains
no C-item hunk, as expected). Retained unchanged: PIN-S-R2-1-RULE, PIN-USET-PURE-FUNCTIONS,
PIN-EXC-CAPTURE, PIN-A5-SUPPORT-CONTRACT, PIN-CANON-DOC, PIN-CALLCOUNT-PROVENANCE,
PIN-TESTONLY-EVALUATOR-BRANCHES, PIN-COVERAGE-DERIVED, PIN-NONREGRESSION-VS-R4,
PIN-NONREGRESSION-VS-R4-1, PIN-GUARDED-COMPARATOR, PIN-SPLINE-PENDING-ROUTING,
PIN-SPLINE-PENDING-TAG-SCOPE, PIN-SPL-PENDING-REALPATH-STUBS, PIN-CUSTODY-PER-ATTEMPT,
PIN-REVALIDATION-INCONSISTENT-U, PIN-STORE-READ-ACCOUNTING (amended by R-5 below),
PIN-KEY-NAMESPACE-SCOPING (amended below), PIN-F1-SYNTHETIC-LOADER (amended by R-2 below),
PIN-CONTEXT-ID-UNIQUE (REPLACED by R-1 below), PIN-INADMISSIBLE-OBSERVABLE,
PIN-RESTART-ACTIVE-FROM-START, and all earlier loader/masks/statistics pins.
Evidence: 39/39 recorded tests passed; `T-EXPECT-ALL` 36/36; `DETERMINISM=True`;
`T-NONREG-R4` 0 findings; `T-NONREG-R4-1` 37/0; `T-NONREG-R4-2` s=0/e=2114/u=0.

## RP1A-04 (record part) — T-KEY-NAMESPACE table: every key family, its fields, the counts and conversions

Scope prefix = the `KEY_SCOPE` value folded into every key written while set (C-2); the
fingerprint prefix (`29de608948a06cf2`) precedes everything. The rule T-KEY-NAMESPACE
checks: two DIFFERENT computations never share a key; a declared re-read of the SAME
computation is legal only inside the declaring test's own scope and is counted by C-1.

| scope | key family | identity fields inside the key name | units written (attempt 2, store manifest) | what one unit holds |
|---|---|---|---|---|
| `(base)` | `onestart` | fixture_id, family (P-01/P-02), mask_id (carries run label run1/run2 + sex + per-sex trajectory index + context), start_id (grid[i]/feature), inject flag, input-vector hash | 2,081 | one family START's (canonical, cls, tel) triple |
| `(base)` | `splmode` | fixture_id, mask_id (as above), mode 0–145, input-vector hash | 9,344 | one spline MODE's (valid, rss, c, src, pst, cap_recs, tel_calls, inad) tuple |
| `(base)` | `realscen` | fixture_id (SCEN-A/SCEN-B), run label | 4 | one SCEN-A/B **synthetic** scenario's coarse per-run checkpoint — the strata_recs/telemetry bundle `run_real_scenario` returns for the SYNTHETIC fixtures (the name is historical, from r2's layer; it has never named a real-data unit — RP1A-04's corrected description) |
| `(base)` | `nrgates_all` | — (one coarse unit) | 1 | the NR-gate phase's complete result bundle |
| `(base)` | `unittests_all` | — (one coarse unit) | 1 | the unit-test phase's complete result bundle |
| `excpass1__` / `excpass2__` | `splmode` | test id (INJ-EXC fixture), context, mode, input hash | 438 + 438 | C-2(i): the two INJ-EXC passes as two EXECUTIONS under disjoint keys |
| `f1handoff__` | `onestart` | as `(base)` `onestart`, with real-mode mask ids `real:<sex><ti>:<traj id>:<family>:<ctx>` (PI-b: family inside the mask id) | 47,706 | R-1: the handoff's family starts on the 6 synthetic-F1 trajectories (FULL_LATTICE banks) |
| `f1handoff__` | `splmode` | as `(base)` `splmode`, real-mode mask ids | 7,008 | R-1: the handoff's spline modes (6 traj × 8 ctx × 146 modes) |
| `f1gap__` | — | — | 0 | T-F1-CONTRACT-GAP STOPs at the missing-key check before any fit; the scope exists so that IF a fit were ever reached it could not collide — writing 0 units is the test passing |
| `tstoreread_cold__` / `tstoreread_warm__` | `splmode` | T-STORE-READ test context, mode, input hash | 146 + 146 | R-5: the cold and warm accounting cases under disjoint scopes |
| **total** | | | **67,313** | = store manifest rows, all pid 34588 |

**Counts in units and the conversions (RP1A-04).** Three different counters, never
interchangeable: (1) **stored units** (above, 67,313) — one per computed checkpoint;
(2) **optimizer-call rows** (per-call telemetry CSV, 22,217 = 21,725 `fresh` + 492
`replay`) — SPL (spline) `minimize` calls only; one `splmode` unit holds 1–2 such rows
(primary + optional fallback stage); FAMILY fits are not row-logged in the per-call CSV
(the frozen F2 engine's optimizer is not wrapped) — their work appears only as `onestart`
units; (3) **store reads** (B' store-read log, 730 rows) — one per `ckpt_load` HIT,
all inside the two declaring T-STORE-READ scopes (292 cold + 438 warm, including each
case's 146 verification re-reads). Phase attribution note: the handoff's 8,895 fresh SPL
rows carry phase `nr_gates` (the R-1 tests run before `CURRENT_PHASE` switches to
`unit_tests`); they are exactly identifiable by `fixture == "F3-REAL"` irrespective of
phase, and T-CALLCOUNT's run1 == run2 invariant is unaffected.

**Record-level limitation, disclosed (T-class):** `results.json`'s own
`key_namespace_table` prints the f1handoff scope's key_families as `["f1handoff"]` —
`_key_family()` strips only the `excpass*`/`tstoreread*` prefixes, so the scope prefix
itself masks the underlying family split there. The TRUE split (47,706 `onestart` +
7,008 `splmode`) is derived above from the store manifest's key names, which carry the
full identity; no key collision is possible either way (the scope prefix guarantees
disjointness first). Carried to the ledger as a record item for the next cycle's
inventory; no delivered count is wrong, one delivered display is coarse.

## New/amended in rp1-r1 (full rows, one per R-item)

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result (attempt-2 run) | tag / scientific_freedom |
|---|---|---|---|---|---|
| PIN-F1-HANDOFF (NEW, R-1; PI-b, PI-c) | rp1-r1 instruction §4 R-1; RP1A-01 | (i) `run_real_scenario` consumes `sc["real_x"][(sx,ti)]` and family-qualified real mask ids built by the SAME `mid()` rule `f1_context_id_table` uses (one string rule, two consumers — divergence impossible by construction); without `real_x` the r4-2 path runs byte-for-byte (proved by R-3's S class); `gen.make_traj` is NOT called for a real_x trajectory; (iii) `RUN_REAL_SCENARIO_REQUIRED_KEYS` checked before any other read of `sc`; a missing key raises `F1ContractGap(<key>)`, never a default, never a KeyError; (iv) `f1_repro_gate` verifies the COMPLETE hash-table file list (missing/extra/mismatch = 3 named STOPs) then reproduces the eligible manifest byte-exact (mismatch = 4th named STOP) — exercised in rp1-r1 ONLY on synthetic tables built from the T-F1-LOADER-SYNTH fixtures (S-e) | T-F1-HANDOFF-SYNTH + T-F1-CONTRACT-GAP + T-F1-REPRO-GATE-SYNTH (all MANDATORY) | PASS: handoff 144/144 (fixture_id, mask_id, family) rows equal the dry table, consumer x-hashes equal the loader's array hashes, no exception; contract-gap 4/4 keys each STOPping with its own name; repro-gate 5/5 (complete passes; missing/extra/hash-changed/manifest-changed each STOPs with its own reason) | SUMMARY / none |
| PIN-CONTEXT-ID-UNIQUE (REPLACED, R-1(ii)) | rp1-r1 instruction §4 R-1(ii); PI-b | T-CONTEXT-ID-UNIQUE now runs on the ids the consumer ACTUALLY passed in T-F1-HANDOFF-SYNTH (captured by `mid()` into `REAL_MODE_IDS_PASSED` with each context's input-vector hash), not merely the dry table; mask_id is family-qualified, so uniqueness of (fixture_id, mask_id) alone implies per-family uniqueness | T-CONTEXT-ID-UNIQUE (MANDATORY, replaces rp1's) | PASS: 144 rows, all unique, equal to the dry table as a set | SUMMARY / none |
| PIN-F1-QC-FULL-BRANCHES (AMENDED, R-2) | rp1-r1 instruction §4 R-2; RP1A-02 | T-F1-LOADER-SYNTH covers every QC failure branch: 8 new cases (RAW_FILE_MISSING and BAD_SEMANTICS through the public pipeline; NONFINITE_PRE_Z(NaN) + NONFINITE_PRE_Z(Inf) + NEGATIVE_SHARE + NONFINITE_POST_Z + Z_STD_QC + Z_NORM_QC by calling the guard directly on a crafted input, each with the register-stated derivation of why the public pipeline cannot reach it from well-formed integer-count files: a share of non-negative integers is finite and non-negative; a z-normalized row's std/norm are tied to its mean by construction, so only the mean gate can fire first on real tolerance drift); `denominator_includes_partial` now computes its expected value IN THE TEST from the fixture rows (21,146 = sum of every 1949/F count incl. Partial) and requires exact equality; every case's ok = (got == expected), no constant | T-F1-LOADER-SYNTH (MANDATORY; 21 cases) | PASS: 21/21, every got == expected | SUMMARY / none |
| PIN-NONREG-FULL-DEPTH (REPLACED comparison method, R-3) | rp1-r1 instruction §4 R-3; RP1A-03; D-9 §2(a) | T-NONREG-R4-2 compares, against the three pinned r4-2 baselines: results JSON recursively to every leaf (`_flatten_leaves`, path printed), test evidence JSON recursively to every leaf, telemetry CSV row-by-row (key = fixture/fitter/mask_id/start_id) and column-by-column (only `wall_clock_seconds` declared); E declarations are EXACT paths, each with ONE kind — EQUAL / ADDITION / COUNT a→b / MAY_DIFFER — as a source constant (so the W-3 custody hash fixes them before launch 1); for every test present in r4-2 its ran/passed must be EQUAL; the INJ-EXC capture lists are compared provenance-stripped (pid/start_iso/traceback), same discipline as solver_exceptions; a declared expectation that does not hold is itself a failure; MAY_DIFFER never fails; S class (37 evaluation objects, stops, canonical, residual, RUN1==RUN2) stays whitelist-free and separate | T-NONREG-R4-2 (MANDATORY) + delivered CSV (deliverable D) | PASS: s_findings=0, e_declared=2114 (every declared expectation held), u_findings=0 | SUMMARY / none |
| PIN-AUDITOR-RERUN-PATH (NEW, R-4) | rp1-r1 instruction §4 R-4; RP1A-07 | `REPO = os.environ.get("F3_REPO_ROOT", <executor default>)` in the harness AND the W-3 writer (default keeps executor behaviour byte-for-byte); procedure document delivered stating isolation (separate root, custody records moved aside — the writer REFUSES an existing file — empty store, outputs only inside the copy), custody (auditor writes its own W-3 with the delivered writer) and compare (S equality required in the auditor run whatever the environment; environment recorded field-by-field, never accepted as cause) | executor dry check (procedure §4; NOT an audit) | DONE 2026-10-08: writer refusal observed live; copy's own custody written (same fingerprint, own hash 892076fc…); unchanged harness in the copy verified custody + 31/31 preconditions + NR gates, wrote only inside the copy; deliberately stopped after the gates; copy deleted | SUMMARY / none |
| PIN-TELEMETRY-PROVENANCE (AMENDED, R-5) | rp1-r1 instruction §4 R-5; RP1A-04 code part | per-call telemetry gains `source` ∈ {fresh, replay}: `wrapped_minimize` stamps `fresh` (a real optimizer call in THIS process); the ckpt replay path appends `dict(tc, source="replay")` (stored dict never mutated); T-STORE-READ-ACCOUNTING runs under its own phase label (`t_store_read_accounting`) and its own two scopes, cold (empty namespace) AND warm (keys primed before fit1, simulating units already present as after a restart — exercised EVERY run, not only on a real resume); in both cases fit2's rows must all be `replay` and equal, row for row (source stripped), the telemetry stored in the units read; the first fit is never required to have been fresh | T-STORE-READ-ACCOUNTING (MANDATORY; cold + warm) | PASS: cold (fit1_reads=0, served=146, 164 replay rows == stored) and warm (fit1_reads=146, served=146, 164 replay rows == stored) both pass_; global CSV: 21,725 fresh / 492 replay, the 492 exactly the three declared re-reads | SUMMARY / none |
| PIN-END-STATE-DISPATCH-RP1R1 (AMENDED) | rp1-r1 instruction §8 | `end_state.PI_dispatch_record_hash` = D-12 as observed on disk during the run; S-R2-1 source stays D-5 in its own fields; distinctness asserted | the three assertions in `main()` | PASS: D-12 `2c23130d…` observed == written; D-5 field distinct | SUMMARY / none |

## VERBATIM quotes

Unchanged from the rp1 register (`dbf25669…`) and its parents: the D-5 §3 rule text
(PIN-S-R2-1-RULE) is not re-transcribed.

```text
new_scientific_literal_by_executor = 0
Every result above is bound to f3_step2_correction_report_rp1-r1_2026-10-05.md and
f3_step2_results_rp1-r1_2026-10-05.json (e5ea4f07…); "see report" resolves there.
commit = false (separate PI instruction required)
```
