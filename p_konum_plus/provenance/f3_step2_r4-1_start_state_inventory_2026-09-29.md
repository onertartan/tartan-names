# p_konum_plus - F3 STEP-2 r4-1 - Start-State Inventory (deliverable 11, W-1(a))

```text
artifact_role = start-state inventory for the r4-1 correction revision (D-3 §9 item 11, W-1(a);
                R4A-04(i)); taken BEFORE the first r4-1 write
status        = NON-NORMATIVE
date          = 2026-09-29
scope         = the state the r4-1 revision opens from: the audited r4 package (read-only under
                non-retroactivity), the r3 package and every quarantined file
```

## 1. Instruments verified before this inventory (r4-1 instruction §1)

Every value OBSERVED (sha256sum on the delivered files on 2026-09-29); all EQUAL to their sidecar / D-6 §1:

| instrument | sha256 | source of the pin |
|---|---|---|
| r4-1 instruction | 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330 | D-6 §1 |
| D-6 (r4-1 dispatch record) | a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0 | its sidecar |
| A-2 (r4 audit DRAFT r1) | b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a | its sidecar / D-6 §1 |
| A-3 (r4 audit DRAFT r2) | 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9 | its sidecar / D-6 §1 |
| r4 instruction (standing) | e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 | D-6 §1 |
| D-3 (standing) | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 | D-6 §1 |
| D-1 v6 (standing) | 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 | D-6 §1 |
| D-2 content (standing) | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 | D-6 §1 |
| D-5 (parent) | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 | r4-1 instruction |

## 2. The r4 package (read-only; non-retroactivity check PASS)

Every file at the hash the r4-1 instruction's non-retroactivity block prints (OBSERVED 2026-09-29):

| # | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1 | calibration/f3_step2_adequacy_harness_r4_2026-09-24.py | 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c |
| 2 | calibration/f3_step2_fixture_generator_r4_2026-09-24.py | 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c |
| 3 | calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv | c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 |
| 4 | provenance/f3_step2_r4_preexecution_custody_2026-09-24.md | 0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f |
| 5 | calibration/f3_step2_telemetry_r4_2026-09-24.csv | 11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 |
| 6 | calibration/f3_step2_results_r4_2026-09-24.json | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 |
| 7 | calibration/f3_step2_residual_series_r4_2026-09-24.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 | calibration/f3_step2_test_evidence_r4_2026-09-24.json | 118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 |
| 9 | calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md | 0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4 |
| 10 | provenance/f3_step2_correction_report_r4_2026-09-27.md | 5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848 |
| 12 | provenance/f3_step2_r4_attempt_log_2026-09-24.md | 8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69 |
| A | calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv | d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 |
| B | calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv | f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 |

r4-1 does not overwrite, rename or move any of these; every r4-1 deliverable is a new file with the r4-1 tag.

## 3. r3 per-revision triples (R4A-04(ii)) — from the custody records, recomputed

Each row is one r3 custody record: its named (harness, generator, manifest), its recorded
`code_env_fingerprint`, and the fingerprint recomputed here from the named triple + the frozen F2/spline
hashes + the executor environment (py 3.11.7, numpy 1.26.4, scipy 1.14.1, Windows-10, threads=1). All five
recompute exactly. **The named bytes are NOT in every case the bytes filed under the matching quarantine label
— see the r4-1 attempt log ERRATUM-2 and the quarantine annotation note (R4A-10).**

| custody record | H (named) | G (named) | M (named) | recorded fp | recomputed fp | match |
|---|---|---|---|---|---|---|
| r3 final (provenance) | 5fea165c… | cc23c9b5… | 9c944543… | 1ba561daefb48b2e | 1ba561daefb48b2e | yes |
| r3 ATTEMPT1 | 6ddcc26d… | e35c2bf0… | 4544ff75… | 2cf50b2f18cfb34e | 2cf50b2f18cfb34e | yes |
| r3 ATTEMPT2-3 | 891574fc… | e35c2bf0… | 4544ff75… | d505bf76994abf60 | d505bf76994abf60 | yes |
| r3 ATTEMPT5 | d67e097d… | e35c2bf0… | 4544ff75… | 6f4e29ccc903bce6 | 6f4e29ccc903bce6 | yes |
| r3 ATTEMPT8 | 390f42b7… | cc23c9b5… | 9c944543… | 548ae790f6ac756a | 548ae790f6ac756a | yes |

The r3 store's foreign prefix `548ae790f6ac756a` is the recomputed fingerprint of the ATTEMPT8 custody
triple (harness `390f42b7…`) — identifying A-1's open T-R3-2 and confirming A-3 §5.2 [A on this executor's
own recompute]. Conflicts (label vs named bytes vs the r3/r4 logs) are enumerated in ERRATUM-2.

## 4. R4A-10(iii) hash search — the three named-but-unfiled r3 harness/generator bytes

Searched the repository and quarantine (source files; the two restart-store directories excluded as they
hold pickled units, not harness/generator source):

| hash | what it is | result |
|---|---|---|
| d67e097dc158c4909276b026ce66533f33dfab7a94d800e57342eb86e76f58ff | r3 attempt-5 harness (named by the ATTEMPT5 custody record) | **NOT_PRESERVED** |
| e35c2bf06ee4087bac97bd5b6e81d35d079ff1dddf8d2e68555c6c7d18859638 | r3 attempts 1-5 generator (named by four r3 custody records) | **NOT_PRESERVED** |
| 390f42b72971030033c6964731d699358a1547bf9093b8e949c0e338e6bc0336 | r3 attempt-8 harness (named by the ATTEMPT8 custody record) | **NOT_PRESERVED** |

None is in the repository. The r4 report §8(c) statement that `d67e097d…` is "present in quarantine" is
therefore corrected in the r4-1 report: the bytes filed under the ATTEMPT5 label are `f882b922…`, not
`d67e097d…`. This is a labelling/disclosure defect touching no delivered output (final r3 ran under
`1ba561da…`, r4 under `5ef61a41…`; no `548ae790…` unit was ever readable by either).

## 5. Quarantined files carried forward (read-only)

The five r3 quarantine notes, the superseded r3 harness/custody pairs (ATTEMPT1/2-3/5/8), the r4
supersession chain (revisions 1-4 notes/bytes/logs), the r3 and r4 final restart stores (quarantined
whole), and the T-R3-2 foreign-entry listing — all remain in `p_konum_plus/quarantine/` unchanged. r4-1
adds a quarantine ANNOTATION note (R4A-10(ii)); it renames and moves nothing.

`real_data_access = false ; commit = false`
