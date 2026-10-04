# p_konum_plus — F3 real-data preparation rp1 — Correction Report

```text
artifact_role = correction report (deliverable 10, rp1 instruction §8 item 10)
status        = NON-NORMATIVE narrative over the hashed artifacts it cites
date          = 2026-10-04 (cycle opened 2026-10-02; attempts 2026-10-03/2026-10-04)
```

No wording in this report asserts "verified", "QUALIFIED", or "audit PASS" about the
executor's own output. rp1 instruction §9: neither `rp1_status` value (below) binds
the rp1 bytes under D-9 §2(a) — that happens only after an independent audit, by a PI
record (rp1 instruction §10).

## 1. The PI's dispatch, verbatim

The rp1 cycle itself was dispatched by D-10
(`f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md`,
`4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34`) together with the
rp1 instruction (`Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md`,
`a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5`), both delivered as
attachments and verified EQUAL before the first write (start-state inventory §3(e)).

The operative instruction for the attempt-4→5 correction (the B' deliverable fix,
this session), verbatim:

```text
Onaylıyorum, şu koşullarla:
(a) Deneme 5'ten önce rp1 talimatı §8'deki her teslim dosyasını ve §4–§9'da adı geçen
her sonuç alanını koda karşı tara: her biri için onu yazan satırı göster. Başka bir
eksik varsa onu da aynı düzeltmeye kat. Taramanın sonucu deneme günlüğüne girsin.
(b) Düzeltme dar olsun: STORE_READ_LOG satırlarını (key family, key, writer pid,
reader pid) CSV'ye yaz. Ayrıca CSV satır sayısının total_rows ve fine_counts
toplamıyla eşit olduğunu doğrulayan bir assert ekle.
(c) Deneme 4'ün çıktılarını ve deposunu karantinaya al, silme. Deneme 4 harness'ının
kopyası karantinada dursun. Yeni W-3 kaydı yaz, SUPERSEDES alanını doldur. Boş depo
kullan, launch numarası 5 olsun. Hiçbir log'un üzerine yazma.
(d) E beyanlarını yeni harness hash'ine göre deneme 5 başlamadan güncelle. Beyan
dosyasının hash'ini ve yazılma zamanını kaydet.
(e) Ortam deneme 4 ile aynı olsun; farklıysa alan alan raporla.
(f) "ctx 22" düzeltmesi: deneme-3 notunu değiştirme. Deneme günlüğüne kanıtlı bir
erratum satırı yaz; istersen ayrı bir düzeltme notu da ekle.
Sonra task #58'deki sırayla devam et; belgeler deneme 5'in verisine dayansın, deneme
1–5 günlükte geçmiş olarak yer alsın. Gerçek veri okuma, commit yapma.
```

All six conditions were carried out: (a) the scan is attempt log §2 (found the B'
omission plus one dead-code observation, `EXPECTATIONS_E_PATH`); (b) the fix is
exactly the CSV write + the three-way row-count assert, nothing else touched; (c)
attempt 4's store/outputs/launch-4 logs are quarantined whole (not deleted), its
harness copy verified byte-exact before quarantining, custody attempt5 written with
`supersedes_harness_sha256`/`supersedes_custody_sha256` filled, the store started
empty, launch number 5 used, no log overwritten; (d) `EXPECTATIONS_E`'s shape was
re-checked against the new hash (unchanged — only additive sub-fields under an
already-fully-declared prefix), its declaration-file hash/mtime recorded and shown to
predate attempt 5's start (attempt log §6b); (e) environment compared field-by-field,
identical (attempt log §6); (f) the ctx-22 correction is attempt log §7, with
forensic evidence, the attempt-3 note left unmodified, and a separate note was also
written for the attempt-4 defect itself (not ctx-22 — ctx-22 needed no code fix, only
the note).

## 2. Custody (rp1 instruction §1; every value OBSERVED)

25 preconditions verified EQUAL by the external W-3 writer AND re-verified at every
launch (`DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS … 25 verified`): D-3, r4 instruction,
D-5, A-1, D-2, r4-1 instruction, D-6, A-2, A-3, r4-2 instruction, D-7, A-4, the reused
generator, the reused manifest, the r4-1 results baseline, the **rp1 instruction
`a57b6fca…`, D-10 `4c89577b…`, D-9 `1ab17e44…`, D-8 `aadf2840…`, A-5 `9111bc71…`**,
the r4-2 results/telemetry/test-evidence baseline, and the **F1 freeze record
`5eceb198…`**.

## 3. Execution (full detail in the attempt log)

5 attempts, 5 launches, 2026-10-03 → 2026-10-04. Attempts 1–4 each stopped on a
defect found either by the run itself (attempt 1: 3 `T-NONREG-R4-2` bookkeeping bugs)
or by the executor's own post-run verification (attempt 2: missing `T-RP-1` in
`narrowed_evidence`; attempt 3: a launch-log-truncation process error plus a
resume-robustness bug in `T-STORE-READ-ACCOUNTING`; attempt 4: a PI-ordered scan
finding the B' deliverable, `STORE_READ_LOG`, declared by path and never written).
**Attempt 5** (harness `39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09`,
pid 33100, 2026-10-04T15:09:42 → exit 0) ran uninterrupted: one process computed
**all 12,453 store units and every result object — T-SINGLE-PROCESS applies and
holds** (store manifest: one pid, 33100, one `start_iso`; `units_read_from_store`
all 0). None of the four defects in attempts 1–4 touched any scientific content —
`s_findings=[]`/`0` in every attempt that reached the comparison.

## 4. `rp1_status` (rp1 instruction §9 — computed here; NOT the harness's legacy `F3_STEP2_r4_status` field)

rp1 instruction §9 defines `rp1_status` by five conditions, all evaluated against
attempt 5:

| condition | observed (attempt 5) | met? |
|---|---|---|
| every mandatory test of §4–§5 RAN and PASSED | all 35 entries of `MANDATORY_TESTS` show `{"ran": true, "passed": true}` in `tests_run` (§5 table below) | yes |
| non-regression shows no S difference | `T-NONREG-R4-2 s_findings=0` | yes |
| every E difference matches its declaration | `u_findings=0` (any E mismatch would itself surface as a U finding by construction — zero U proves every E matched) | yes |
| no U difference | `u_findings=0` | yes |
| `open_findings = []` | `end_state.open_findings = []` (refreshed block) | yes |

**`rp1_status = PREPARED_PENDING_INDEPENDENT_AUDIT`.**

This is distinct from `results.json`'s `F3_STEP2_r4_status` field
(`"PARTIAL_PENDING_PI"`), which is a legacy field computed by harness code inherited
unchanged from the r4 lineage's own status logic (gated on `narrowed_evidence` being
empty, which it is not — `["T-R2-2","T-RP-1"]` — a PI decision about the r4 cycle's
history, not about rp1's own preparation completeness). The two fields answer
different questions; neither harness computation nor this report conflates them.

## 5. Mandatory-test table (§4–§5; RAN/PASSED + evidence file)

Every entry of `MANDATORY_TESTS`, attempt 5, all `{"ran": true, "passed": true}`:

| test | evidence file |
|---|---|
| NR-01i, NR-01ii | `results.json["nr01"]` |
| NR-SPL | `results.json["spline_nonregression"]` |
| T-LOADER-NODES | `results.json["spline_loader_nodes"]`; launch log `PIN-SPLINE-LOADER` line |
| T-MASK-FULL-EXT | `results.json["t_mask_full_ext"]` |
| PIN-MASKED-OBJECTIVE, PIN-FEATURE-START-MASKED | launch log (`PIN-MASKED-OBJECTIVE`/`PIN-FEATURE-START-MASKED` lines); `results.json["construction_audit"]` |
| UT-A5-II, UT-A5-III | `test_evidence.json["a5"]` |
| UT-PROBE-DECOUPLE | `results.json["ut_probe_decouple"]` / `test_evidence.json["ut_probe_decouple"]` |
| UT-USET-CONSTRUCTION | `results.json["uset_construction"]` / `test_evidence.json["uset_construction"]` |
| T-COMPARATOR-NAN | `results.json["comparator_nan"]` |
| T-STARTS-DEFAULT, T-STARTS-DUP | `results.json["starts_default"]`, `["starts_dup"]` |
| FIX-A5-TRUE | `results.json["fix_a5_true"]` |
| T-A5-SUPPORT | `test_evidence.json["t_a5_support"]` |
| T-EXC-CAPTURE-S1, T-EXC-CAPTURE-S2, T-EXC-UNRELATED-TYPE | `results.json["exc_injection_fixtures"]` / `test_evidence.json["exc_injection_fixtures"]` |
| UT-EXC-UNRELATED-REFERENCE | `test_evidence.json["ut_exc_unrelated_reference"]` |
| T-SCHEMA | launch log `T_SCHEMA` line (`missing: []`) |
| T-CANON | `results.json["run1_canonical_sha256"]`/`["run2_canonical_sha256"]`/`["determinism"]` |
| T-EXPECT-ALL | `results.json["expectation_checks"]` (36/36) |
| T-CALLCOUNT | `results.json["process"]`; `f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv` |
| T-RESIDUAL-LINK | `test_evidence.json["residual_link"]`; `f3_step2_residual_series_rp1_2026-10-02.json` |
| T-WRAPPER-RESTORE | `test_evidence.json["wrapper_restore_ok"]` |
| PIN-ACF | `test_evidence.json["acf"]` |
| T-SPL-PENDING-REALPATH | `test_evidence.json["spl_pending_realpath"]` |
| T-NONREG-R4-1 | `f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv`; `test_evidence.json["nonregression_vs_r4_1"]` |
| **T-STORE-READ-ACCOUNTING** | `results.json["store_read_accounting"]`; `f3_step2_rp1_store_read_log_2026-10-02.csv` (the B' fix) |
| **T-KEY-NAMESPACE** | `results.json["key_namespace_table"]` (register, table above) |
| **T-F1-LOADER-SYNTH** | `results.json["f1_loader_synth"]`; `f3_step2_rp1_f1_synth_fixtures_2026-10-02/` |
| **T-CONTEXT-ID-UNIQUE** | `results.json["context_id_unique"]` |
| **T-INADMISSIBLE-OBSERVABLE** | `results.json["inadmissible_observable"]`/`["inadmissible_completed_counts"]`; C-5 statement (item G) |
| **T-NONREG-R4-2** | `f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv`; `results.json["nonregression_vs_r4_2"]` |

(`T-NONREG-R4` is retained but not in `MANDATORY_TESTS`; also PASSED, findings=0,
`f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv`.)

## 6. Response table — P-1…P-9 and C-1…C-6 (rp1 instruction §8 item 10)

| item | status | evidence |
|---|---|---|
| **P-1 (R42A-01)** | **CLOSED** | start-state inventory §3(a)-(e) carries D-8 PI-3's record items, the r4-2 package full-hash re-verification, ERRATUM-R41A-04, the fingerprint erratum, and D-8/A-5/D-9 with hashes |
| **P-2 (R42A-03(b))** | **CLOSED** | C-1: `STORE_READ_LOG` fine-grained accounting, now written as the B' CSV (fixed attempt 5); `T-STORE-READ-ACCOUNTING` PASS |
| **P-3 (R42A-03, 2nd half)** | **CLOSED** | C-2: `excpass1__`/`excpass2__` disjoint key scopes; `T-KEY-NAMESPACE` + `pass_key_namespaces_disjoint` PASS |
| **P-4** | **CLOSED** | C-3: `REAL_DATA_MODE=False` asserted every launch; F1 pipeline present, exercised only on synthetic files; `T-F1-LOADER-SYNTH` PASS; opened-file audit confirms no real path opened |
| **P-5 (A-5 R42A-09)** | **CLOSED** | C-4: `T-CONTEXT-ID-UNIQUE` PASS (144/144 unique) |
| **P-6 (D-8 PI-2(iii))** | **CLOSED** | C-5: observability established on both sides with frozen-engine line citations; report-only counters; `T-INADMISSIBLE-OBSERVABLE` PASS; statement = item G |
| **P-7 (T-RP-1)** | **CLOSED** | C-6: restart layer active from attempt 1 of this cycle; `narrowed_evidence=["T-R2-2","T-RP-1"]` correct since attempt 3's fix, confirmed again attempt 5 |
| **P-8 (D-9 §2(a))** | **CLOSED** | `T-NONREG-R4-2`: `s_findings=0, e_declared=39, u_findings=0` — no whitelist on the scientific objects, every E difference declared and matched |
| **P-9 (§7 estimate)** | **CLOSED (informational)** | item H: ~85.4–85.5 hours (~3.56 days), one sequential process, 906 trajectories, method stated, labelled ESTIMATE, decides nothing |
| C-1…C-6 | **CLOSED** | register (item 9), full rows |
| C-7 (6B) | **N/A — not implemented, as instructed** | S-f=EXCLUDED_FROM_RP1; no `6B` marker in the harness |
| **Deviation — attempt-3 launch-log truncation** | **disclosed, not corrected** (the loss is irreversible) | the resumed sub-process (pid 26784) reused launch number 3's log targets, truncating pid 23540's console text for its own portion of the run; the STORE provenance (pid/`start_iso` on every written unit) survives and was used to reconstruct the interruption point precisely (ctx 22, attempt log §7); this did not recur in the 4→5 transition (condition (c) above: a fresh launch number, no log overwritten) |
| **Observation — `EXPECTATIONS_E_PATH` dead code** | **not fixed (out of the narrow attempt-5 scope); reported** | attempt log §2; no §8 deliverable is omitted by it |

## 7. Hash block (A-5 R42A-01 discipline): FULL SHA256 of every rp1 deliverable except this report

| # | file (p_konum_plus/, relative to repo root unless noted) | sha256 |
|---|---|---|
| 1 | calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py (attempt 5) | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 |
| 2 | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py (REUSED, no copy) | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3 | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv (REUSED, no copy) | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4 | provenance/f3_step2_rp1_preexecution_custody_attempt5_2026-10-02.md (final attempt) | 7e2ee506a2819dc1a0f579751dbfa552d2a472d50309fef2a2e0d1731a853ae9 |
| 4a | provenance/f3_step2_rp1_preexecution_custody_attempt1_2026-10-02.md | f78966d063c9991c590ed29d14f5671d998184aa6515b8f658c0f956998183eb |
| 4b | provenance/f3_step2_rp1_preexecution_custody_attempt2_2026-10-02.md | f2d33d169c161d6d004570d7aa92c8241d136bf0bb9822e76c774adce6ec1aa4 |
| 4c | provenance/f3_step2_rp1_preexecution_custody_attempt3_2026-10-02.md | 239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a |
| 4d | provenance/f3_step2_rp1_preexecution_custody_attempt4_2026-10-02.md | 49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165 |
| 5 | calibration/f3_step2_telemetry_rp1_2026-10-02.csv | 836076827ae8b30d712191f5d3507dec6b721824acaa81bae491401d2e8f468f |
| 6 | calibration/f3_step2_results_rp1_2026-10-02.json | ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882 |
| 7 | calibration/f3_step2_residual_series_rp1_2026-10-02.json (byte-identical to r4-2/r4-1/r4/r3) | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 | calibration/f3_step2_test_evidence_rp1_2026-10-02.json | 809e9d043d136371fafcd158d5955853f61e67490db370d1d56761b7f8e6578d |
| 9 | calibration/f3_step2_class_c_pin_register_rp1_2026-10-04.md | dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066 |
| 11 | provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md | a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d |
| 12 | provenance/f3_realdata_prep_rp1_attempt_log_2026-10-04.md | d015c3cdc505cdf816764633e885605ce2b8c305fabaf4ebe9cf1406e24a458c |
| A | calibration/f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv (12,502 rows, pid 33100) | 2648cb7feeba22f54c1cb27432d23c885ff3fb0d939ef28a596779b8a5390084 |
| B | calibration/f3_step2_rp1_restart_store_manifest_2026-10-02.csv (12,453 rows, pid 33100) | ca355af467f66a05b19e82fa3e2f515ce41a253718b0120e30fae6338d96a733 |
| B' | calibration/f3_step2_rp1_store_read_log_2026-10-02.csv (146 rows — the attempt-5 fix) | 6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1 |
| D | calibration/f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv | 6b98e427a819f0464adf1ca100183905ae51f24de140cc4bd4c1a9bda42d5739 |
| D' | calibration/f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d |
| D'' | calibration/f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| E1 | quarantine/f3_step2_rp1_launch1_stdout_2026-10-02.log | 445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f |
| E1' | quarantine/f3_step2_rp1_launch1_stderr_2026-10-02.log | c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b |
| E2 | quarantine/f3_step2_rp1_launch2_stdout_2026-10-02.log | d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7 |
| E2' | quarantine/f3_step2_rp1_launch2_stderr_2026-10-02.log | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| E3 | quarantine/f3_step2_rp1_launch3_stdout_2026-10-02.log | 7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d |
| E3' | quarantine/f3_step2_rp1_launch3_stderr_2026-10-02.log | 915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45 |
| E4 | quarantine/f3_step2_rp1_launch4_stdout_2026-10-02.log | c1b286fa378def03c91035199750f6243cb501768f10852996dfdc8b4d71f698 |
| E4' | quarantine/f3_step2_rp1_launch4_stderr_2026-10-02.log | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| E5 | calibration/f3_step2_rp1_launch5_stdout_2026-10-02.log | cbd2281e5719911a997ddf9103707d50adc74e7857616aaf443f9b0dd815f715 |
| E5' | calibration/f3_step2_rp1_launch5_stderr_2026-10-02.log | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 |
| E6 | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py | 08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2 |
| E7 | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py | 0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5 |
| E8 | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py | d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d |
| E9 | quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py | 47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561 |
| E10 | quarantine/f3_step2_rp1_attempt1_nonreg_bug_note_2026-10-02.md | 2357898e6d7314a5b950fc356def73a4e78ce7d27a6e67b863b6041d7784be1b |
| E11 | quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md | 029fcc980513e74c142250cb9ccc51051a541af71a9dd9a85364aa705d20ca0c |
| E12 | quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md | 527fd2495bd4642b956ea18b760beca5a1168449cd55214bc7f6b7bb9a49a1d3 |
| E13 | quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md | 73d9040bb3ed4aaf5d72dda0fd04a6189b11c38e843429e009b4641f3a79e530 |
| F1 | calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/SYNTH_FIXTURE_MANIFEST.json | 63452ff4a8f2ad99820eac509e074fb3c3a2cfb10ea765dd0f310baa6ee387b4 |
| G | provenance/f3_realdata_prep_rp1_c5_observability_statement_2026-10-04.md | 5d36806b1036c4169870622e73a0f2c78b4c9c943c29c8902e4e83c6cd6a4d3d |
| H | provenance/f3_realdata_prep_rp1_size_estimate_2026-10-04.md | 6d8dbe067d54c50e213779e70b30c260def5ac75e516b4bfc5436cca5e9bd541 |

The store directories themselves (attempts 1–4, quarantined; attempt 5, live at
`calibration/.rp1_restart_store_2026-10-02`) are not individually hashed here — their
content is exhaustively described, path+size+sha256+pid+start_iso per unit, by item B
(and by the quarantine directory names recorded in the attempt log for attempts 1–4).
Item T (transmission list) and item Z (zip) are produced after this report and
necessarily cite this report's own hash in turn.

## 8. Coverage and carried-forward items

`COVERAGE_DERIVED = 64 rows, downgraded = []`; the only UNCOVERED row remains the
authored `A.5 (iii) inadmissible refit` (a PI decision, not this cycle's).
`narrowed_evidence = ["T-R2-2","T-RP-1"]` (T-SINGLE-PROCESS holds this cycle for
every attempt that reached exit 0; the narrowing concerns the r4/rp1 cycles' own
history — a PI decision). `T-NONREG-R4`, `T-NONREG-R4-1` and `T-NONREG-R4-2` all show
0 findings. `real_data_access = false` and `REAL_DATA_MODE = False` in every one of
the 5 launches; no SSA/F1 file was ever opened (opened-file audit, confirmed every
attempt). No commit was made during this cycle.
