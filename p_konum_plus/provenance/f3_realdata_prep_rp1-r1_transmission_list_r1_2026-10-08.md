# p_konum_plus — F3 real-data preparation rp1-r1 — Transmission List r1 (deliverable T, corrected)

```text
artifact_role = r1 of the rp1-r1 transmission list: supersedes
                f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md (99c5d103640540de5a012d9000b425ccbbdbf02bd081c44c93c6f1102231d59b,
                kept unchanged in place); the ONLY table change is the corrected row for
                the correction report (see Erratum below). EVERY hash in the tables below
                was recomputed from the file bytes by the generating script at write time
                (no hand-typed or truncated value); the complete transmission set for the rp1-r1 B-correction cycle
                (rp1-r1 instruction §7); every hash OBSERVED (2026-10-08). Item Z:
                one zip for transport only; its own hash given alongside the zip
status        = NON-NORMATIVE
final run      = attempt 2 / launch 2 (pid 34588), exit 0 ; DETERMINISM = True
                (RUN1 == RUN2 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77)
verdicts       = 31 preconditions EQUAL ; 39/39 recorded tests RAN+PASSED (38 mandatory) ;
                T-NONREG-R4-2 s=0 / e_declared=2114 / u=0 (full depth, 3 baselines) ;
                rp1-r1_status = PREPARED_PENDING_INDEPENDENT_AUDIT (report §4) ;
                T-SINGLE-PROCESS holds (67,313 units, one pid)
```

Every file below has an external `.sha256` sidecar (the three NEW standing-file
sidecars of RP1A-06 included). The generator and the manifest are the REUSED r4-1
files with their original sidecars; no rp1-r1 copy exists. No rp1/r4-2/r4-1/r4/r3 or
pre-existing quarantine file was modified, renamed or moved; no custody record and no
log was overwritten; `real_data_access = false` throughout. The F1 input hash table
was NOT opened or hashed (ledger item T; closure = real-data step 1).

## Erratum (r1, 2026-10-08)

The superseded list (`f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md`,
`99c5d103640540de5a012d9000b425ccbbdbf02bd081c44c93c6f1102231d59b`, committed at 63d4846 and inside the
2026-10-05 zip) carried ONE wrong value: the correction-report row stated
`ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260`, while the file and
its sidecar are `ebc28df8a94bd3b2249389caba08c35e8071afd0a7766f48f984c78a2d78ec40`. The last 48 hex digits of
the listed value were FABRICATED by the executor from a truncated 16-hex script
printout instead of being read from the bytes — the superseded list's "every hash
OBSERVED" claim was false for that row. The defect was caught by the drafting
session's independent post-push check (audit instruction §7), confirmed by the
executor, and a full self-scan of all 108 hash occurrences across the 8 delivered
rp1-r1 documents found no second instance (107 verified, 1 wrong — this one). Full
mechanism and scan record: `provenance/pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md`
(c446395e497bb42baa179d9c756c8b2664ea92ebbe6f80b064c5bb8ba6d63444). In THIS r1 list
every table hash was recomputed from the file bytes by the generating script at write
time. The report file itself and its sidecar were always consistent; only the list row
was wrong.

### Deliverables

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1  harness (attempt 2; child of rp1 39c733a3…) | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py | cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb |
| 2  generator (REUSED r4-1) | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3  manifest (REUSED r4-1) | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4  custody, attempt 2 (final) | provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md | 162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca |
| 4a custody, attempt 1 (preserved) | provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md | dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d |
| 5  telemetry | calibration/f3_step2_telemetry_rp1-r1_2026-10-05.csv | 29e3e4101c479c1354ae212dabb10597ecfac889436d8f113d8661f298be6435 |
| 6  results | calibration/f3_step2_results_rp1-r1_2026-10-05.json | e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb |
| 7  residual (byte-identical to r4-2/r4-1/r4/r3) | calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8  test evidence | calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json | 97f75c83e4057f4d31b4310602124b536a2badd6c04555ee24d87ec2872ea0f9 |
| 9  register (child of dbf25669…; RP1A-04 table) | calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md | 4d5de5a776e7cd4a336b0dfc5f50aae378bdf6c3a780ff887a2a414389a5fe63 |
| 10 correction report | provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md | ebc28df8a94bd3b2249389caba08c35e8071afd0a7766f48f984c78a2d78ec40 |
| 11 start-state inventory (incl. FIRST ledger, D-11 r1 §7) | provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md | dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286 |
| 12 attempt log (incl. §0 disclosure, dry-check record) | provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md | ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b |
| A  per-call telemetry (22,217 rows + header; `source` column, R-5) | calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv | d9d1c2564c9a24cddf55f31f662f09a40d453308536d5fcbbfa0dcfdfe1f000a |
| B  restart-store manifest (67,313 rows, pid 34588) | calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv | f64e0aa9344f7b2187d91a113cdc83c0f006bfd288fef8f86060ce9ab3f39da5 |
| B' store-read log (730 rows) | calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv | 92b3af34f8c63347f839a7c0f1826e1bb566072cb25d40da17ad3bbd55939d7d |
| C  capture records | in items 6/8: solver_exceptions + exc_captures{,_unit_phase,_run2} + run1_eq_run2=true | — |
| D  non-regression vs r4-2 (full depth) | calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv | 4fb207b79432a326fc436287e56fd237573bf2aed594d4b7a166f4c53fbebb98 |
| D' non-regression vs r4-1 (retained) | calibration/f3_step2_rp1-r1_nonregression_vs_r4-1_2026-10-05.csv | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d |
| D'' non-regression vs r4 (retained) | calibration/f3_step2_rp1-r1_nonregression_vs_r4_2026-10-05.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| F1 synthetic-fixture manifest (dir carries the rp1 prefix with this cycle's date — naming carry-over, disclosed in the report; raw files regenerated identically by the declared RNG, seed 20261002) | calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/SYNTH_FIXTURE_MANIFEST.json | f08d7167e034da39fcb218db0f8864976ab83672eef96b1910eb95bfed78c7d2 |
| G1 labelled diff vs rp1 (36 hunks; only R-/wiring labels) | calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff | ce7624ea27653c8e3d2efaa83b5c177d14c238a4a707d13b3837be69a4d89227 |
| G2 labelled diff vs r4-2 (36 hunks; C-/R-/wiring labels) | calibration/f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff | c4cb5fae14545e7e66b52b0b93e05eddc153ff7a9e9f7b974c95836df97124a0 |
| P  auditor re-run procedure (R-4; §4 = the executor dry check as performed) | provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md | f7b5baf11f89d8aec68e81e48b0f4ab9fb1998576376ca5cf023c87f8556a8b4 |
| H  §7 estimate, two labelled lines (RP1A-05) | provenance/f3_realdata_prep_rp1-r1_size_estimate_2026-10-05.md | 97c2684cb3216f3b0bb6f6b7edae5436aaffa5a1935fb27efc0a5b8b1dc86875 |
| T  this list (r1) | provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md | (its sidecar) |

### Item E — launch logs and quarantine artifacts of this cycle

| item | file (p_konum_plus/) | sha256 |
|---|---|---|
| launch 1 stdout (quarantined) | quarantine/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log | f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7 |
| launch 1 stderr (quarantined) | quarantine/f3_step2_rp1-r1_launch1_stderr_2026-10-05.log | fdf8c410faa5ff104eb1519e4a831b113000490ed51ae980550ecff2181308ff |
| launch 2 stdout (final, live) | calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log | d26b2898c580aae762af8a824851e9ea5c1e9cd8bd9c72424052d58ec83c6630 |
| launch 2 stderr (final, live) | calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log | afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b |
| attempt-1 supersession note | quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md | 7772e17d4c775f14b0d67a90911876e06c8e99f2aca2d415dcf0b6d07d27e3fd |
| attempt-1 harness bytes (== custody-pinned hash) | quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d |

Attempt 1's complete 9-file written-output set is preserved whole in `quarantine/` with
the `ATTEMPT1_NONREG_E_DECLARATION_BUGS_` prefix (listed by prefix; each file was the
live file's own printed `_WRITTEN = … sha256=…` value at attempt-1 time).

### New sidecars for standing files (RP1A-06; the files themselves unchanged)

| sidecar created | pins |
|---|---|
| calibration/f2_step2_feasibility_harness_r3_2026-09-01.py.sha256 | 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 |
| calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py.sha256 | b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d |
| calibration/f1_input_freeze_record_2026-08-28.md.sha256 | 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0 |

### Restart stores

| store | location (p_konum_plus/) | units | fingerprint |
|---|---|---|---|
| attempt 1 (quarantined) | quarantine/rp1-r1_restart_store_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS/ | 67,313 (all pid 34228) | (attempt-1 harness keyed) |
| attempt 2 FINAL (live) | calibration/.rp1-r1_restart_store_2026-10-05 | 67,313 (all pid 34588) | 29de608948a06cf2 |

### Standing instruments (in the repository; verified by hash, not re-transmitted)

rp1-r1 instruction `2226fc96…` (final by D-12 signature), D-12 `2c23130d…`, D-11 r1
`0b177ee4…`, rp1 audit `2fa28e2a…` (input), rp1-r1 DRAFT review `aa9fcaa9…` (input),
rp1 instruction `a57b6fca…`, D-10 `4c89577b…`, D-9 `1ab17e44…`, D-8 `aadf2840…`,
A-5 `9111bc71…`, the full r4-2/r4-1/r4/r3 instrument chain as in the rp1 transmission
list `858091d6…` (re-verified 43/43 this cycle), the rp1 harness `39c733a3…`, and the
F1 freeze record `5eceb198…`. The rp1 package at commit `b6d2483` and every earlier
package are historical and read-only; `parents_unchanged = true`.

### Item Z — zip

```text
f3_realdata_prep_rp1-r1_package_r1_2026-10-08.zip — one archive of every file listed
above (deliverables + item E + the three new standing sidecars + BOTH transmission
lists + the executor disclosure note, each with its sidecar), for transport only;
hash given alongside the zip. The original zip
f3_realdata_prep_rp1-r1_package_2026-10-05.zip (sha256 8b560d88ac36ce24a385e4d21975082acc3177bf005b730b962fe80ab99350c8)
stays historical; it contains the superseded list with the wrong row
```

```text
real_data_access = false ; commit = false (separate PI instruction required)
```
