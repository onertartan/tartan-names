# p_konum_plus — F3 real-data preparation rp1 — CLASS_C Pin Register (2026-10-04)

```text
artifact_role = CLASS_C implementation-pin register for the rp1 real-data preparation
                cycle (deliverable 9, rp1 instruction §8)
status        = NON-NORMATIVE
parent        = f3_step2_class_c_pin_register_r4-2_2026-09-30.md
                c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c
frozen_contract = r4 5e594136 AS RATIFIED BY freeze record r1 7055f186 ; v11 wins (unchanged)
harness       = f3_step2_adequacy_harness_rp1_2026-10-02.py
                39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 (attempt 5)
generator     = f3_step2_fixture_generator_r4-1_2026-09-29.py — REUSED UNCHANGED
                68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
manifest      = f3_step2_fixture_manifest_r4-1_2026-09-29.csv — REUSED UNCHANGED
                5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
PI dispatch record (D-10) = f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md
                4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34
S-R2-1 source (D-5)       = f3_step2_r4_pi_dispatch_record_2026-09-24.md
                0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
PI fields (D-10 §2, read verbatim) = T-RP-1=ACTIVE_FROM_START ; S-c=CHILD_HARNESS_OF_R4-2 ;
                S-e=SYNTHETIC_ONLY_IN_RP1 ; S-f=EXCLUDED_FROM_RP1
scientific_freedom in every row = none ; new scientific literal additions by executor = 0
Every row is stated against the rp1 attempt-5 run of 2026-10-04 (RUN1 == RUN2 canonical
SHA256 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 — unchanged
since r4-1; results ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882);
result = executor claim, independent verification pending (rp1 instruction §10).
Tag discipline: every C-item row below is tagged SUMMARY (engineering description, no
scientific literal).
```

## Retained from r4-2 unchanged (re-verified against the rp1 attempt-5 run)

Every pin of the r4-2 register ran and passed in the rp1 run and is implemented as its
parent row describes, EXCEPT the C-1…C-6 rows given in full below (rp1 touches nothing
else — §4, "nothing else changes: no change to the decision layer, the evaluator, the
criteria, the generator, the manifest, any expected_* value or any literal"). Retained
unchanged: PIN-S-R2-1-RULE, PIN-USET-PURE-FUNCTIONS, PIN-EXC-CAPTURE,
PIN-A5-SUPPORT-CONTRACT, PIN-CANON-DOC, PIN-CALLCOUNT-PROVENANCE,
PIN-TESTONLY-EVALUATOR-BRANCHES, PIN-COVERAGE-DERIVED, PIN-NONREGRESSION-VS-R4,
PIN-GUARDED-COMPARATOR, PIN-SPLINE-PENDING-ROUTING, PIN-SPLINE-PENDING-TAG-SCOPE,
PIN-SPL-PENDING-REALPATH-STUBS, PIN-NONREGRESSION-VS-R4-1, PIN-CUSTODY-PER-ATTEMPT,
PIN-END-STATE-DISPATCH (re-pointed at D-10, not D-7 — see PIN-END-STATE-DISPATCH-RP1
below), PIN-REVALIDATION-INCONSISTENT-U, and all r2/r3/r4/r4-1-retained loader/masks/
statistics pins. Evidence: `T-EXPECT-ALL 36/36`; 36/36 recorded tests passed;
`DETERMINISM=True`; `T-NONREG-R4` findings=0; `T-NONREG-R4-1` compared=37 findings=0;
`T-NONREG-R4-2 s_findings=0, e_declared=39, u_findings=0`.

## T-KEY-NAMESPACE table (C-2(ii), delivered here as the instruction requires)

Every key family the harness writes, by scope, from attempt 5's `results.json`
(`key_namespace_table`); the rule checked is "two DIFFERENT computations never share
a key" — `T-KEY-NAMESPACE` PASSED (`pass_key_namespaces_disjoint=true`,
`passes_identical=true`).

| scope | key families | n_keys |
|---|---|---|
| `(base)` | `nrgates_all`, `onestart`, `realscen`, `splmode`, `unittests_all` | 11,431 |
| `excpass1__` | `splmode` | 438 |
| `excpass2__` | `splmode` | 438 |
| `tstoreread__` | `splmode` | 146 |

`realscen` appears only as a key FAMILY NAME (the dry context-id construction of C-4,
on T-F1-LOADER-SYNTH's synthetic output — `REAL_DATA_MODE=False` throughout; no real
trajectory is fit). Total: 11,431 + 438 + 438 + 146 = 12,453 — matches the store
manifest row count exactly (`f3_step2_rp1_restart_store_manifest_2026-10-02.csv`,
12,453 rows, all pid 33100 — the empty-store proof, attempt log §5).

## New in rp1 (full rows, one per C-item)

| pin_id | frozen rule (pointer) | implementation (exact call / arithmetic) | verification test id | result (rp1 attempt-5 run, 2026-10-04) | tag / scientific_freedom |
|---|---|---|---|---|---|
| PIN-STORE-READ-ACCOUNTING (NEW, C-1) | rp1 instruction §4 C-1; A-5 C-31 (D-3 §8.3 asks full granularity; r4-2 reported only coarse per-phase counters) | every `ckpt_load` HIT is counted by `(scope_or_phase, key_family, reader_pid)` into `READS_FINE` and logged into `STORE_READ_LOG` with the full key and the writer's `pid`/`start_iso`; the coarse `UNITS_READ_FROM_STORE` per-phase counter is retained unchanged beside it (declared E against r4-2). The B' deliverable (`STORE_READ_LOG_PATH`) writes every logged row to CSV, with an assert that the CSV's data-row count, `len(STORE_READ_LOG)`, and `sum(READS_FINE.values())` all agree — **added for attempt 5** after attempt 4's scan found the CSV write itself missing (attempt-4 supersession note) | T-STORE-READ-ACCOUNTING (MANDATORY) | PASS: `modes=146, fit1_reads=0, served_to_fit2=146, fine_counter=146, per_read_rows_wellformed=true, fit2_equals_fit1=true`; CSV `f3_step2_rp1_store_read_log_2026-10-02.csv` (`6ae8ea00…`), 146 data rows, matching `total_rows=146` and `fine_counts` sum=146 | SUMMARY / none |
| PIN-KEY-NAMESPACE-SCOPING (NEW, C-2) | rp1 instruction §4 C-2; R42A-03 second half | `KEY_SCOPE` (a mutable one-element list) is prefixed onto every store key written while set; the second INJ-EXC pass runs under `excpass2__` (pass 1 under `excpass1__`), so pass 2 is a genuine second execution, not a replay of pass 1's cached units; `T-STORE-READ-ACCOUNTING` runs under its own `tstoreread__` scope, the only place a declared re-read of the same computation is permitted (and is the thing C-1 counts); `ckpt_save` asserts no duplicate write of one key in one process | T-KEY-NAMESPACE (MANDATORY, table above) + `exc_injection_fixtures.pass_key_namespaces_disjoint` | PASS: 4 disjoint scopes, 12,453 keys total, zero cross-scope collisions; `passes_identical=true` (pass 1 and pass 2 produce identical capture records under disjoint keys) | SUMMARY / none |
| PIN-F1-SYNTHETIC-LOADER (NEW, C-3) | rp1 instruction §4 C-3; F1 freeze record §8.1 steps 1–11, §8.2 tolerance 1e-8; D-10 §2 S-e=SYNTHETIC_ONLY_IN_RP1 | `REAL_DATA_MODE = False` (module constant), asserted at `main()` start every launch; the F1 frozen pipeline (source-format/semantics validation → national-only → 1880–2025 index → FULL-support eligibility → retain → released-record-share → denominator/duplicate/finite/nonnegative QC → zero-variance QC → row-wise z-normalization → post-normalization QC, tol 1e-8) is implemented (`f1_verify_raw_files`, `f1_load_raw_dir`, `_f1_share`, `f1_normalize`, `f1_post_z_qc`, `f1_build_scenarios`) and exercised ONLY on generated raw-format files (manifest-declared RNG, seed 20261002, small, not resembling any real F1 trajectory); F1 manifest paths/hashes are constants copied from the F1 freeze record, never read from those files in rp1; the opened-file audit (`sys.addaudithook`, X-18/Y-12) confirms no F1/SSA path is ever opened | T-F1-LOADER-SYNTH (MANDATORY) | PASS: `eligible_count=6/6, partial_excluded=true, denominator_includes_partial=true, z_qc_pass=true, gate_pass=true`, every QC failure branch (`MISSING_YEAR, DUPLICATE_KEY, ZERO_DENOMINATOR, ZERO_VARIANCE, COUNT_BELOW_PUBLICATION_FLOOR, BAD_FORMAT, RAW_FILE_HASH_MISMATCH, Z_MEAN_QC`) fires on its matching synthetic case; `opened_files_declared`/`opened_files_audit_derived` contain only rp1's own paths | SUMMARY / none |
| PIN-CONTEXT-ID-UNIQUE (NEW, C-4) | rp1 instruction §4 C-4; A-5 R42A-09 | in real mode, every `(fixture_id, mask_id)` pair is unique per sex/trajectory/family/context, so `fit_spline` cannot derive one context's tag from another's captures; a dry construction of the real-mode context list runs on T-F1-LOADER-SYNTH's synthetic output | T-CONTEXT-ID-UNIQUE (MANDATORY) | PASS: `rows=144, expected_rows=144, all_unique=true` | SUMMARY / none |
| PIN-INADMISSIBLE-OBSERVABLE (NEW, C-5) | D-8 PI-2 (iii)/(iv); frozen F2 engine `01714752…` L265–305; frozen spline harness `b31e5a6b…` L308–405 | `family_start_inadmissible_completed` / `spline_mode_completed_not_accepted` read ONLY existing frozen-engine fields (no frozen change, no new classification); `INADMISSIBLE_COMPLETED` report-only counters incremented at both the cached and fresh compute paths on both the family and spline sides; full line-cited statement delivered separately (item G) | T-INADMISSIBLE-OBSERVABLE (MANDATORY) | PASS: `witness_on_frozen_lattice=false` (no P-01/P-02 start-bank point lands in the morphology-inadmissible-only region for these fixtures — reported, not failed), all 7 negative/positive sub-cases correct; report-only counts observed this run: `family_starts=318, spline_modes=102` | SUMMARY / none |
| PIN-RESTART-ACTIVE-FROM-START (NEW, C-6) | D-10 §2, S-b; rp1 instruction §4 C-6; replaces, for rp1 only, D-3 §8.3's "attempt 1 runs without it" | `RESTART_LAYER_ACTIVE=True` from attempt 1 of this cycle onward; `T_RP_1="ACTIVE_FROM_START"` module constant, read from D-10 §2; `narrowed_evidence` concatenates `["T-R2-2"]` (if `T_R2_2=="AUTHORIZE_RESTART"`) with `["T-RP-1"]` (if `T_RP_1=="ACTIVE_FROM_START"`) — same presence-of-the-PI-value pattern `T-R2-2` already used | implicit in every mandatory test's pass_ + `end_state.narrowed_evidence` | PASS: `narrowed_evidence=["T-R2-2","T-RP-1"]`; store manifest proves the layer was active and the store was empty at attempt 5's first launch (12,453/12,453 rows pid 33100) — T-SINGLE-PROCESS holds | SUMMARY / none |
| PIN-END-STATE-DISPATCH-RP1 (AMENDED, re-pointed from r4-2's D-7 to rp1's own D-10) | rp1 instruction §9 | `end_state.PI_dispatch_record_hash` = D-10 as observed on disk during the run (re-read at end-state assembly); the S-R2-1 source stands in its own fields, still D-5 (`0cd87ad5…`), carried unchanged through D-6/D-7/D-10; distinctness asserted | the R41A-03-pattern assertions in `main()` | PASS: `PI_dispatch_record_hash=4c89577bed…` (D-10), `S_R2_1_source_dispatch_record_hash=0cd87ad5…` (D-5), distinct | SUMMARY / none |
| (no row — C-7) | S-f=EXCLUDED_FROM_RP1 | no 6B code anywhere in the harness diff (confirmed: no `6B` marker in the file) | — | N/A — nothing to test | SUMMARY / none |

## VERBATIM quotes

Unchanged from the r4-2 register (`c281e713…`): the D-5 §3 rule text
(PIN-S-R2-1-RULE), not re-transcribed here.

```text
new_scientific_literal_by_executor = 0
Every result above is bound to f3_step2_correction_report_rp1_2026-10-04.md and
f3_step2_results_rp1_2026-10-02.json (ce89fdb4…); "see report" resolves there.
commit = false
```
