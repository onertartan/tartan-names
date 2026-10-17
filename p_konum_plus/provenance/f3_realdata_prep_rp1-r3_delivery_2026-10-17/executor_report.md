# rp1-r3 teslim raporu

rp1-r3_status = `PREPARED_PENDING_INDEPENDENT_AUDIT`

Bu rapordaki hash, sayi ve sonuc durumlari dosyalardan betikle aktarildi. Kod ve kosu ciktilari degistirilmedi. Bagimsiz denetim yapilmadi; hicbir madde icin yurutucu kapanis karari verilmedi.

## S sinifi ve kosu sonucu

```json
{
  "rp1_r3_status": "PREPARED_PENDING_INDEPENDENT_AUDIT",
  "scientific": {
    "scientific_objects": 37,
    "stop_count": 6,
    "stops": [
      {
        "fixture": "SCEN-B",
        "stop": "BOTH_FAIL_REDESIGN"
      },
      {
        "fixture": "INJ-BOTH-FAIL",
        "stop": "BOTH_FAIL_REDESIGN"
      },
      {
        "fixture": "INJ-DP04-EMPTY-U",
        "level": "C2",
        "stop": "CONTRACT_VIOLATION_EMPTY_U"
      },
      {
        "fixture": "INJ-U-POST-CONSTRUCTION-INVALID",
        "level": "C2",
        "member": 0,
        "offending_pairs": [
          {
            "fitter": "P01",
            "observation": 0,
            "sex": "F"
          },
          {
            "fitter": "P01",
            "observation": 0,
            "sex": "M"
          }
        ],
        "sex": "F",
        "stop": "CONTRACT_VIOLATION_INCONSISTENT_U"
      },
      {
        "fixture": "INJ-NAN-STAT-SPL",
        "stop": "BOTH_FAIL_REDESIGN"
      },
      {
        "fixture": "INJ-P03-BOTHFAIL-C4PENDING",
        "stop": "BOTH_FAIL_REDESIGN"
      }
    ],
    "RUN1": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
    "RUN2": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
    "determinism": true,
    "residual_sha256": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f",
    "residual_bytes_sha256": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f",
    "residual_source": "p_konum_plus/calibration/f3_step2_test_evidence_rp1-r3_2026-10-15.json:nonregression_vs_r4_1.residual_series_observed",
    "residual_source_note": "The results JSON has no residual hash leaf. This value is copied from the actual test_evidence result record and independently checked against residual bytes; no output was altered.",
    "result_source": "p_konum_plus/calibration/f3_step2_results_rp1-r3_2026-10-15.json",
    "result_sha256": "d2a52c3822c7bf94680b91482c95ea10f9c80471a5077ddb0ac4bc760531618d",
    "test_evidence_sha256": "6d00360b9d89e1eead10d96b1752724eb60f0e1b227218d6ef2af8c50d07e179"
  },
  "end_state": {
    "F3_STEP2_r4_status": "PARTIAL_PENDING_PI",
    "PI_dispatch_record_hash": "10b3543344bd9ebf9df3319cfdc0d3540888328fde8bf4e5d6e05764bb675b1a",
    "PI_dispatch_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-14.md",
    "S_R2_1_source_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851",
    "S_R2_1_source_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md",
    "corrections_complete": true,
    "deferred_decisions": [],
    "mandatory_tests_all_run": true,
    "mandatory_tests_missing": [],
    "narrowed_evidence": [
      "T-R2-2",
      "T-RP-1"
    ],
    "open_findings": [],
    "rp1_r3_open_findings": [],
    "rp1_r3_status": "PREPARED_PENDING_INDEPENDENT_AUDIT",
    "standalone_evidence_status": "NOT OBSERVED",
    "uncovered_coverage_rows": [
      "A.5 (iii) inadmissible refit"
    ]
  },
  "nonregression": {
    "baseline": "p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json",
    "baseline_sha256": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
    "e_declared": 220076,
    "pass_": true,
    "s_findings": [],
    "telemetry_baseline": "p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv",
    "test_evidence_baseline": "p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json",
    "test_evidence_baseline_sha256": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf",
    "u_findings": []
  },
  "all_recorded_tests_ran_and_passed": true,
  "recorded_tests": 51,
  "nonregression_csv_rows": 220077,
  "every_declared_expectation_held": true,
  "executor_elapsed_seconds": 35714.174677,
  "launch_end_record": "p_konum_plus/provenance/f3_step2_rp1-r3_attempt2_launch1_end_2026-10-15.json",
  "launch_end_record_sha256": "272e7a34ce309488dacd15b69142806882eccab01b305e23c79a43cfa79e9cdf",
  "IR2_07_observed": 11,
  "IR2_07_not_observed": 2262,
  "real_data_access": false,
  "commit": false,
  "push": false,
  "independent_audit_performed": false
}
```

Residual hash sonuc JSON dosyasinda bulunmuyor; yukaridaki kaynak notunda belirtildigi gibi test_evidence sonuc kaydindan aktarildi ve residual baytlariyla dogrulandi.

## Denetci icin bilinen aciklama dizgileri

Asagidaki kaynak dizgileri onaylanan kodda aynen korundu. Ucuncu tuple alani W-3 pin_checks.source alanina yazilir; operasyonel yol/hash alanlariyla karistirilmamalidir.

```text
158:   'rp1-r3 incoming Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-15.md'),
159:  ('p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md',
160:   '6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f',
161:   'rp1-r3 incoming f3_realdata_prep_rp1-r3_pi_dispatch_record_2026-10-15.md'),
162:  ('p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md',
163:   'f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913',
164:   'rp1-r3 incoming f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-15.md'),
165:  ('p_konum_plus/prompts/F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md',
166:   '82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e',
167:   'rp1-r3 incoming F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md'),
168:  ('p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py',
169:   'cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb',
170:   'rp1-r3 carried p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py'),
171:  ('p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md',
172:   '98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956',
173:   'rp1-r3 carried p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md'),
174:  ('p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md',
175:   '0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639',
176:   'rp1-r3 carried p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md'),
177:  ('p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md',
178:   '4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955',
179:   'rp1-r3 carried p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md'),
```

## Tarihsel karsilastirmanin ek satirlari

Bu liste §5(a1) tarihsel rp1-r2 karsilastirmasinin kaydindan aktarilmistir. Yeni exception-normalization farki listesiyle ayni sey degildir. Eksik-yol satiri dahil tam degerler auditor_review_notes.json icindedir.

```text
results.end_state.rp1_r2_open_findings[0]
results.end_state.rp1_r2_open_findings[10]
results.end_state.rp1_r2_open_findings[11]
results.end_state.rp1_r2_open_findings[12]
results.end_state.rp1_r2_open_findings[1]
results.end_state.rp1_r2_open_findings[2]
results.end_state.rp1_r2_open_findings[3]
results.end_state.rp1_r2_open_findings[4]
results.end_state.rp1_r2_open_findings[5]
results.end_state.rp1_r2_open_findings[6]
results.end_state.rp1_r2_open_findings[7]
results.end_state.rp1_r2_open_findings[8]
results.end_state.rp1_r2_open_findings[9]
results.end_state.rp1_r2_status
results.end_state.standalone_evidence_status
results.nonregression_vs_r4_2.baseline
results.nonregression_vs_r4_2.baseline_sha256
results.nonregression_vs_r4_2.e_declared
results.nonregression_vs_r4_2.pass_
results.nonregression_vs_r4_2.s_findings
results.nonregression_vs_r4_2.telemetry_baseline
results.nonregression_vs_r4_2.test_evidence_baseline
results.nonregression_vs_r4_2.test_evidence_baseline_sha256
results.nonregression_vs_r4_2.u_findings
results.end_state.mandatory_tests_missing[*]
```

## Kayitlar ve sinirlar

Guncel diff ve etiket otoritesi IR1-16/diff_custody.json dosyasidir. Eski attempt-1 diff/prosedur kayitlari tarihseldir. rp1-r2 duzeltilmis r1 etiket dosyalari ayri teslim edilir; onceki etiketler degistirilmez.

IR2-04 icin auditor_rerun_procedure_r1.md ve recursive dosya envanteri; IR2-05 icin kaynak denetci gerekcesiyle R42A-09 kaydi; IR2-07 icin hash eslesen adlandirilmis dosyalar ve kalan NOT OBSERVED kayitlari teslim edilir. Yokluktan kontaminasyon sonucu cikarilmadi, D-14 genisletilmedi.

IR1-13 OPEN / B olarak kalir. Onceki denetci kararlarinin atfi yeni bir executor kapanisi degildir. Guncel teslim maddeleri IMPLEMENTED_PENDING_VERIFICATION durumundadir.

ZIP, sabit parent checkout uzerine uygulanan teslim katmanidir. Restart store dizinleri, .pkl, __pycache__, onceki ZIP paketleri ve rp1r1_audit dosyalari teslim ZIPine alinmaz. Ham dis-W3 test ciktilari bu pakete veya storea alinmaz; yalniz yurutme kayitlari ve sonuc aktarma belgeleri teslim edilir. IR2-07 kapsaminda acikca adlandirilmis tarihsel provenance dosyalari ayridir.

Commit veya push yapilmadi. Tam kosu yeniden baslatilmadi.
