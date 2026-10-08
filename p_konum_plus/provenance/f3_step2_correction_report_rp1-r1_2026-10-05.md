# p_konum_plus — F3 real-data preparation rp1-r1 — Correction Report

```text
artifact_role = correction report (deliverable 10, rp1-r1 instruction §7; response table
                per R-1…R-6 and RP1A-01…07 with the rp1 C-1…C-6 rows split, RP1A-06)
status        = NON-NORMATIVE narrative over the hashed artifacts it cites
date          = 2026-10-05 (cycle tag; attempts 2026-10-06 → 2026-10-08)
governing     = D-11 r1 (0b177ee4…); dispatched by D-12 (2c23130d…) naming the rp1-r1
                instruction DRAFT r2 (2226fc96…) as final by signature
```

No wording in this report asserts "verified", "QUALIFIED", or "audit PASS" about the
executor's own output. Neither `rp1_status` value binds the rp1-r1 bytes under D-9
§2(a) — that happens only after the independent audit, by one line in the dependent
package's dispatch record (D-11 r1 §6).

## 1. The PI's dispatch, verbatim

```text
«D-12'ye göre rp1-r1 talimatını yürüt; commit yalnız ayrı talimatımla» (PI, 2026-10-05)
```

with, at the §1 completion gap, the PI's correction instruction of the same day:

```text
«İki girdi dosyası sidecar'larıyla ekte; hash'leri talimattaki değerlerle aynı olmalı.
§1 tamamlanmadan yazım yapılmaz, bu yüzden: Ön koşullar tamamlanmadan oluşturduğun
f3_step2_adequacy_harness_rp1-r1_2026-10-05.py kopyasını sil. Bunu (ne zaman
oluşturuldu, içeriği rp1 harness'ıyla aynıydı, silindi) attempt log'a ve başlangıç
envanterine bir satır olarak yaz. İki dosyayı adlarını değiştirmeden
p_konum_plus/prompts/ altına yerleştir ve hash'leri yeniden hesapla. Eşit değilse dur.
§1'in tamamını yeniden doğrula, §3 başlangıç envanterini al, ondan sonra R-1…R-5'e
başla. Commit yalnız ayrı talimatımla.»
```

Both carried out: the premature fork was deleted and disclosed (inventory §0, attempt
log §0); the two input files placed and re-verified (OK, equal to the instruction's
pinned values); §1 re-verified in full (31 instruments + rp1 transmission list 43/43 +
frozen upstream, all EQUAL); the start-state inventory with the FIRST ledger taken;
only then did R-1…R-5 begin.

## 2. Custody (rp1-r1 instruction §1; every value OBSERVED)

31 preconditions verified EQUAL by the external W-3 writer AND re-verified at every
launch (`DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS … 31 verified`): the 25 of rp1 plus
**D-11 r1 `0b177ee4…`, the rp1 transmission list `858091d6…`, the rp1 harness
`39c733a3…`, the rp1-r1 instruction `2226fc96…`, D-12 `2c23130d…`, the rp1 audit
`2fa28e2a…` and the rp1-r1 DRAFT review `aa9fcaa9…`** (the last two inputs, not
directives). The r4-2 baselines re-pinned (results `f2a0a4d5…`, telemetry
`ac70eaf5…`, test evidence `c156b9e0…`).

## 3. Execution (full detail in the attempt log)

2 attempts, 2 primary launches. **Attempt 1** (harness `4bffb33a…`, pid 34228) ran the
entire computation — including every new R-1/R-2/R-5 test passing — and STOPPED at
`T-NONREG-R4-2` with `s_findings=[]` and 6 U findings, all three bugs in the R-3
comparison logic ITSELF (COUNT double-canonicalization; a declaration-key collision
between the two compared files; three capture-record fields declared EQUAL instead of
provenance-stripped). Fixed, verified against the real delivered files BEFORE the
rerun, quarantined whole (note: `…attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md`).
**Attempt 2** (harness `cac93ac6…`, pid 34588, 2026-10-07T14:51:58 →
2026-10-08T03:08:36, **exit 0**): one process computed all 67,313 store units and
every result object — **T-SINGLE-PROCESS applies and holds**. The R-4 executor dry
check ran after completion in a disposable copy (writer refusal observed; copy's own
custody written; 31/31 preconditions + NR gates passed under `F3_REPO_ROOT`; stopped
deliberately; copy deleted) — attempt log, dry-check section.

## 4. `rp1-r1_status` (rp1-r1 instruction §8 — computed here; NOT the harness's legacy `F3_STEP2_r4_status` field)

| condition (§8) | observed (attempt 2) | met? |
|---|---|---|
| every mandatory test of rp1 §4 and rp1-r1 §4 RAN and PASSED | 38/38 mandatory entries `{ran: true, passed: true}` (§5 table) | yes |
| no S difference | `T-NONREG-R4-2 s_findings=0` | yes |
| no U difference | `u_findings=0` | yes |
| every declared E expectation held | `e_declared=2114`, zero `declared_but_not_held` rows (a non-holding declaration would itself have been a U row by R-3's rule) | yes |
| `open_findings = []` | end_state (refreshed): `[]` | yes |
| every ledger item whose closure point is this package is IMPLEMENTED_PENDING_VERIFICATION with evidence named | §7 below: RP1A-01…06 + R42A-03(b) + R42A-09 all IMPLEMENTED_PENDING_VERIFICATION with their tests; RP1A-07 stays OPEN by design (auditor-only closure) with the R-4 procedure delivered and dry-checked | yes |

**`rp1-r1_status = PREPARED_PENDING_INDEPENDENT_AUDIT`.**

(`results.json`'s `F3_STEP2_r4_status = "PARTIAL_PENDING_PI"` is the legacy r4-lineage
field, gated on `narrowed_evidence` being empty — it is `["T-R2-2","T-RP-1"]` by PI
value, a decision about the lineage's history, not this cycle's completeness.)

## 5. Mandatory-test table (every entry RAN and PASSED; evidence file named)

All rp1 rows as in the rp1 report §5 (same evidence paths, now in the rp1-r1-named
files), re-run and re-passed this cycle; the rp1-r1 additions and replacements:

| test | evidence |
|---|---|
| **T-F1-HANDOFF-SYNTH** (new, R-1) | `results.json["f1_handoff_synth"]` (144/144 rows == dry table; x-hashes == loader arrays); launch-2 stdout |
| **T-CONTEXT-ID-UNIQUE** (REPLACES rp1's, R-1(ii)) | `results.json["context_id_unique"]` (on the ids actually passed; `matches_dry_table=true`) |
| **T-F1-CONTRACT-GAP** (new, R-1(iii)) | `results.json["f1_contract_gap"]` (4/4 keys, each `F1ContractGap` named) |
| **T-F1-REPRO-GATE-SYNTH** (new, R-1(iv)) | `results.json["f1_repro_gate_synth"]` (5/5 cases, each STOP reason named) |
| **T-F1-LOADER-SYNTH** (extended, R-2) | `results.json["f1_loader_synth"]` (21 cases, every `got == expected`, no constant ok) |
| **T-STORE-READ-ACCOUNTING** (extended, R-5) | `results.json` cold+warm blocks; B' CSV (730 rows); per-call `source` column (21,725 fresh / 492 replay) |
| **T-NONREG-R4-2** (comparison method replaced, R-3) | `f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv` (`4fb207b7…`); `results.json["nonregression_vs_r4_2"]` (3 baselines pinned, s=0/e=2114/u=0) |

## 6. Response table — R-1…R-6, RP1A-01…07, and the rp1 C-rows split (RP1A-06)

| item | status | evidence |
|---|---|---|
| **R-1 / RP1A-01** (B, PI-a) | **IMPLEMENTED_PENDING_VERIFICATION** | consumer handoff per PI-c (only the trajectory/mask-id intake changed; byte-identical behaviour without `real_x` proved by R-3's S class); family-qualified ids per PI-b (one string rule for dry table AND consumer); contract-gap STOP; deferred F1 repro gate. Tests: the four §5 rows |
| **R-2 / RP1A-02** (B, PI-a) | **IMPLEMENTED_PENDING_VERIFICATION** | 8 new QC branches (2 public-pipeline, 6 direct-guard with unreachability derivations in the register); computed expected denominator; no constant ok |
| **R-3 / RP1A-03** (B, PI-a) | **IMPLEMENTED_PENDING_VERIFICATION** | full-depth three-file comparison; typed EXACT-path E declarations (source constant, custody-fixed before launch); per-test ran/passed equality; capture lists provenance-stripped; s=0/e=2114/u=0 |
| **R-4 / RP1A-07** | **procedure DELIVERED + dry-checked; item stays OPEN (auditor-only closure)** | `F3_REPO_ROOT` in harness+writer (default = executor behaviour); procedure doc (`f7b5baf1…`); executor dry check done 2026-10-08 (attempt log); the S-equality-whatever-the-environment rule stated as D-12/§14 requires |
| **R-5 / RP1A-04 (code)** | **IMPLEMENTED_PENDING_VERIFICATION** | `source` fresh/replay column; own phase label; cold AND warm cases every run; replay rows equal stored telemetry row-for-row |
| **R-6 / RP1A-04 (record)** | delivered | register's T-KEY-NAMESPACE table: every key family → fields, corrected `realscen` row, counts in units with the three-counter conversion |
| **R-6 / RP1A-05** | delivered | the two-line ESTIMATE (`97c2684c…`): line 1 scope-labelled (SCEN-A smooth), line 2 measured on F1-shaped synthetics (~1.65 h/trajectory full-lattice; interval reading stated) |
| **R-6 / RP1A-06** | delivered | this response table; the TWO labelled diffs (vs rp1 `ce7624ea…`, 36 hunks, only R-/wiring labels; vs r4-2 `c4cb5fae…`, 36 hunks, C-/R-/wiring labels); 3 sidecars created (F2 engine, spline harness, F1 freeze record); the F1 input hash table NOT opened/hashed — ledger item T, closure at real-data step 1 |
| rp1 C-1 (split row) | re-verified this cycle | B' store-read log present (`92b3af34…`, 730 rows, assert held); fine counts consistent |
| rp1 C-2 (split row) | re-verified | 7 disjoint scopes incl. the new f1handoff/f1gap/cold/warm; `pass_key_namespaces_disjoint=true`; `passes_identical=true` |
| rp1 C-3 (split row) | re-verified + extended (R-2) | 21-case loader test; REAL_DATA_MODE=False asserted every launch; opened-file audit shows no F1 path |
| rp1 C-4 (split row) | REPLACED by R-1(ii) | uniqueness now proven on actually-passed, family-qualified ids |
| rp1 C-5 (split row) | re-verified | T-INADMISSIBLE-OBSERVABLE passed; counters report-only (this cycle observed family_starts=318 base-scope equivalents per rp1 + handoff-scope events reported in results) |
| rp1 C-6 (split row) | re-verified | `narrowed_evidence=["T-R2-2","T-RP-1"]`; layer active from attempt 1; store empty at each attempt's first launch (manifest one-pid proof) |
| **Process error — premature fork before §1 complete** | **disclosed, corrected per PI instruction** | inventory §0 + attempt log §0 (created ~19:54 2026-10-05, byte-identical to the rp1 harness, deleted before any further action) |
| **Observation — handoff phase label** | disclosed (register) | handoff SPL rows carry phase `nr_gates` (tests run before the unit-test phase switch); identifiable by `fixture=F3-REAL`; no invariant affected |
| **Observation — `key_namespace_table` coarse family for f1handoff scope** | disclosed (register, T-class ledger carry) | true split derived from the store manifest (47,706 onestart + 7,008 splmode); no count wrong, one display coarse |

## 7. Ledger end-state (D-11 r1 §7; start state in the inventory, end state here)

| id | status at package end | evidence |
|---|---|---|
| RP1A-01 | IMPLEMENTED_PENDING_VERIFICATION | §5/§6 R-1 rows |
| RP1A-02 | IMPLEMENTED_PENDING_VERIFICATION | §5/§6 R-2 rows |
| RP1A-03 | IMPLEMENTED_PENDING_VERIFICATION | §5/§6 R-3 rows |
| RP1A-04 | IMPLEMENTED_PENDING_VERIFICATION (code) + record part delivered | R-5/R-6 rows |
| RP1A-05 | delivered (KAYIT; closes at the next inventory per D-11 r1 §2) | estimate `97c2684c…` |
| RP1A-06 | delivered (KAYIT; same closure) | diffs + sidecars + this table |
| RP1A-07 | OPEN (auditor-only closure by design) | R-4 procedure + dry check |
| R42A-03 (b) | IMPLEMENTED_PENDING_VERIFICATION (re-verified) | R-5 cold+warm + B' |
| R42A-09 | IMPLEMENTED_PENDING_VERIFICATION (strengthened) | family-qualified ids, R-1(ii) |
| D-9 §2(a) binding of rp1/rp1-r1 bytes | OPEN (PI, after audit) | D-11 r1 §6 |
| A.5 (iii) inadmissible refit | OPEN (PI), untouched | rp1 report §8 |
| F1 input hash table sidecar | OPEN (T), closure = real-data step 1 | instruction §6 |
| NEW (this report): f1handoff key_namespace_table display | T, closure = next package's inventory | §6 observation row |

## 8. Hash block: FULL SHA256 of every rp1-r1 deliverable except this report

| # | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1 | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py (attempt 2) | cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb |
| 2 | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py (REUSED) | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3 | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv (REUSED) | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4 | provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md (final) | 162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca |
| 4a | provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md | dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d |
| 5 | calibration/f3_step2_telemetry_rp1-r1_2026-10-05.csv | 29e3e4101c479c1354ae212dabb10597ecfac889436d8f113d8661f298be6435 |
| 6 | calibration/f3_step2_results_rp1-r1_2026-10-05.json | e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb |
| 7 | calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json (byte-identical to r4-2's) | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 | calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json | 97f75c83e4057f4d31b4310602124b536a2badd6c04555ee24d87ec2872ea0f9 |
| 9 | calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md | 4d5de5a776e7cd4a336b0dfc5f50aae378bdf6c3a780ff887a2a414389a5fe63 |
| 11 | provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md (incl. first ledger) | dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286 |
| 12 | provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md | ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b |
| A | calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv (22,218 rows incl. header; `source` column) | d9d1c2564c9a24cddf55f31f662f09a40d453308536d5fcbbfa0dcfdfe1f000a |
| B | calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv (67,313 rows, pid 34588) | f64e0aa9344f7b2187d91a113cdc83c0f006bfd288fef8f86060ce9ab3f39da5 |
| B' | calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv (730 rows) | 92b3af34f8c63347f839a7c0f1826e1bb566072cb25d40da17ad3bbd55939d7d |
| D | calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv | 4fb207b79432a326fc436287e56fd237573bf2aed594d4b7a166f4c53fbebb98 |
| D' | calibration/f3_step2_rp1-r1_nonregression_vs_r4-1_2026-10-05.csv | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d |
| D'' | calibration/f3_step2_rp1-r1_nonregression_vs_r4_2026-10-05.csv | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| E1 | calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log (final) | d26b2898c580aae762af8a824851e9ea5c1e9cd8bd9c72424052d58ec83c6630 |
| E1' | calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log (final) | afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b |
| E2 | quarantine/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log | f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7 |
| E2' | quarantine/f3_step2_rp1-r1_launch1_stderr_2026-10-05.log | fdf8c410faa5ff104eb1519e4a831b113000490ed51ae980550ecff2181308ff |
| E3 | quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d |
| E4 | quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md | 7772e17d4c775f14b0d67a90911876e06c8e99f2aca2d415dcf0b6d07d27e3fd |
| F1 | calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/SYNTH_FIXTURE_MANIFEST.json (dir name carries the rp1 prefix with this cycle's date — a naming carry-over, disclosed; contents regenerated identically by the manifest-declared RNG) | f08d7167e034da39fcb218db0f8864976ab83672eef96b1910eb95bfed78c7d2 |
| G1 | calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff (36 hunks, labelled) | ce7624ea27653c8e3d2efaa83b5c177d14c238a4a707d13b3837be69a4d89227 |
| G2 | calibration/f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff (36 hunks, labelled) | c4cb5fae14545e7e66b52b0b93e05eddc153ff7a9e9f7b974c95836df97124a0 |
| P | provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md | f7b5baf11f89d8aec68e81e48b0f4ab9fb1998576376ca5cf023c87f8556a8b4 |
| H | provenance/f3_realdata_prep_rp1-r1_size_estimate_2026-10-05.md | 97c2684cb3216f3b0bb6f6b7edae5436aaffa5a1935fb27efc0a5b8b1dc86875 |
| S1 | calibration/f2_step2_feasibility_harness_r3_2026-09-01.py.sha256 (NEW sidecar, RP1A-06) | (sidecar of 01714752…; its own bytes in the transmission list) |
| S2 | calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py.sha256 (NEW sidecar) | (sidecar of b31e5a6b…) |
| S3 | calibration/f1_input_freeze_record_2026-08-28.md.sha256 (NEW sidecar) | (sidecar of 5eceb198…) |

The attempt-2 store itself (`calibration/.rp1-r1_restart_store_2026-10-05/`, 67,313
units) is described unit-by-unit by item B; attempt 1's quarantined store likewise by
its directory. Item T (transmission list) and item Z (zip) are produced after this
report and cite this report's hash in turn.

```text
real_data_access = false throughout ; REAL_DATA_MODE = False in both launches ;
F3_EXECUTION_READY = false ; F3_started = false ; commit = false
```
