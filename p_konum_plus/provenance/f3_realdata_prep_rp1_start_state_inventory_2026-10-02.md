# p_konum_plus — F3 real-data preparation rp1 — Start-State Inventory (deliverable 11)

```text
artifact_role = start-state inventory for the rp1 cycle (D-3 §9 item 11; rp1 instruction §3);
                taken BEFORE the first rp1 write. Closes R42A-01 (D-8 PI-3 "İLK YOL"): the
                record items of the r4-2 cycle that A-5 asked to be carried into the next
                cycle's first record are §3 (a), (c) and (d) below
status        = NON-NORMATIVE
date          = 2026-10-02
dispatch      = D-10 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34 ;
                rp1 instruction a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5
                (both verified EQUAL to their sidecars and to the pins naming them)
PI fields (D-10 §2, verbatim keys) = T-RP-1 ACTIVE_FROM_START ; S-c CHILD_HARNESS_OF_R4-2 ;
                S-e SYNTHETIC_ONLY_IN_RP1 ; S-f EXCLUDED_FROM_RP1
real_data_access = false ; no F1 manifest or raw file was read, opened or hash-checked for
                this inventory (rp1 instruction §0)
```

## (a) The r4-2 package — every file with its FULL SHA256 (recomputed from the files, 2026-10-02)

The values A-5 R42A-01 names as missing from the r4-2 report's hash block are included and
marked [R42A-01]. All values below equal the r4-2 transmission list's where that list prints one.

| sha256 (FULL, recomputed) | file (p_konum_plus/) |
|---|---|
| b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 | calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py  |
| 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py  |
| 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv  |
| ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e | provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md  |
| 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1 | provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md  |
| ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d | calibration/f3_step2_telemetry_r4-2_2026-09-30.csv  |
| f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | calibration/f3_step2_results_r4-2_2026-09-30.json  |
| 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | calibration/f3_step2_residual_series_r4-2_2026-09-30.json  |
| c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | calibration/f3_step2_test_evidence_r4-2_2026-09-30.json  |
| c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c | calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md [R42A-01] |
| 7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6 | provenance/f3_step2_correction_report_r4-2_2026-09-30.md  |
| 66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5 | provenance/f3_step2_r4-2_start_state_inventory_2026-09-30.md  |
| b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65 | provenance/f3_step2_r4-2_attempt_log_2026-09-30.md [R42A-01] |
| 7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c | calibration/f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv  |
| 1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95 | calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv  |
| 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | calibration/f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv  |
| 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | calibration/f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv  |
| 711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606 | provenance/f3_step2_r4-2_transmission_list_2026-09-30.md  |
| 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 | calibration/f3_step2_r4-2_launch1_stdout_2026-09-30.log [R42A-01] |
| d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 | calibration/f3_step2_r4-2_launch1_stderr_2026-09-30.log [R42A-01] |
| 3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7 | calibration/f3_step2_r4-2_launch2_stdout_2026-09-30.log [R42A-01] |
| df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | calibration/f3_step2_r4-2_launch2_stderr_2026-09-30.log [R42A-01] |
| a4b5e176de9be9e8caa1b2145ce99e9c2539fcbea254df0a23ba2bfada470bbe | quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md [R42A-01] |
| 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74 | quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py [R42A-01] |
| 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 | quarantine/f3_step2_r4-2_launch1_stdout_2026-09-30.log [R42A-01] (quarantine copy) |
| d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 | quarantine/f3_step2_r4-2_launch1_stderr_2026-09-30.log [R42A-01] (quarantine copy) |

## (b) The r4-1 and r4 packages, re-hashed file by file against their transmission lists

### r4-1 — list `provenance/f3_step2_r4-1_transmission_list_2026-09-29.md` (31b27c28…)

| recorded in the list (FULL) | recomputed (FULL) | verdict | file |
|---|---|---|---|
| 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f | 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f | EQUAL | calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py |
| 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | EQUAL | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py |
| 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | EQUAL | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv |
| 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d | 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d | EQUAL | provenance/f3_step2_r4-1_preexecution_custody_2026-09-29.md |
| 85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167 | 85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167 | EQUAL | calibration/f3_step2_telemetry_r4-1_2026-09-29.csv |
| 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 | EQUAL | calibration/f3_step2_results_r4-1_2026-09-29.json |
| 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | EQUAL | calibration/f3_step2_residual_series_r4-1_2026-09-29.json |
| f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd | f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd | EQUAL | calibration/f3_step2_test_evidence_r4-1_2026-09-29.json |
| 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 | 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 | EQUAL | calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md |
| e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e | e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e | EQUAL | provenance/f3_step2_correction_report_r4-1_2026-09-29.md |
| fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 | fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 | EQUAL | provenance/f3_step2_r4-1_start_state_inventory_2026-09-29.md |
| ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 | ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 | EQUAL | provenance/f3_step2_r4-1_attempt_log_2026-09-29.md |
| 22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88 | 22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88 | EQUAL | calibration/f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv |
| cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1 | cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1 | EQUAL | calibration/f3_step2_r4-1_restart_store_manifest_2026-09-29.csv |
| 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | EQUAL | calibration/f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv |
| 77120f5be87da8dada1cdad47f7840427922ba212464499950b1263f0747ecf4 | 77120f5be87da8dada1cdad47f7840427922ba212464499950b1263f0747ecf4 | EQUAL | calibration/f3_step2_r4-1_run_stdout_2026-09-29.log |
| 9b678df6d6be6c0b9b5d96d0c358da4ec24debd5a7114a02e60a2f26a4608aa1 | 9b678df6d6be6c0b9b5d96d0c358da4ec24debd5a7114a02e60a2f26a4608aa1 | EQUAL | calibration/f3_step2_r4-1_run_stderr_2026-09-29.log |
| 7ff79add1a72219a64a64f73cb5f14160148a120582715e400435ba4434dcab4 | 7ff79add1a72219a64a64f73cb5f14160148a120582715e400435ba4434dcab4 | EQUAL | quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md |
| e27b29b2ae8746aa7dce2700aa11d942b8ed1f1db429a482845623fee7e9f6e2 | e27b29b2ae8746aa7dce2700aa11d942b8ed1f1db429a482845623fee7e9f6e2 | EQUAL | quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md |
| 3adbd089c03c8212e56f9c275b5785562a3289e2bf2b4977b71ee1b34473e2aa | 3adbd089c03c8212e56f9c275b5785562a3289e2bf2b4977b71ee1b34473e2aa | EQUAL | quarantine/f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md |
| 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2 | 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2 | EQUAL | quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py |
| f0398c8e7350e5eb7a5d6f7168decdeea88da5bdf12be06c9654bb4813c8d546 | f0398c8e7350e5eb7a5d6f7168decdeea88da5bdf12be06c9654bb4813c8d546 | EQUAL | quarantine/f3_step2_r4-1_attempt1_stdout_2026-09-29.log |
| 8fa1cab46ecfc0f92cb2df6301c4cab9a8e4b2079ce1a7fed4e1fb323e171b94 | 8fa1cab46ecfc0f92cb2df6301c4cab9a8e4b2079ce1a7fed4e1fb323e171b94 | EQUAL | quarantine/f3_step2_r4-1_attempt1_stderr_2026-09-29.log |
| 9381d124f61d1435e6d107320e127246798ae23f34d5b01dabadcb48c34fd7cf | 9381d124f61d1435e6d107320e127246798ae23f34d5b01dabadcb48c34fd7cf | EQUAL | quarantine/f3_step2_r4-1_attempt2_stdout_2026-09-29.log |
| 83c1e4a49778cdd973fa40838a7997317cea45e687afeadebba89d22a1a9b253 | 83c1e4a49778cdd973fa40838a7997317cea45e687afeadebba89d22a1a9b253 | EQUAL | quarantine/f3_step2_r4-1_attempt2_stderr_2026-09-29.log |

r4-1: **25/25 EQUAL**

### r4 — list `provenance/f3_step2_r4_transmission_list_2026-09-27.md` (10635dae…)

| recorded in the list (FULL) | recomputed (FULL) | verdict | file |
|---|---|---|---|
| 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c | 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c | EQUAL | calibration/f3_step2_adequacy_harness_r4_2026-09-24.py |
| e70cd58d63cd00119202ef7c17becfe989a2a1d7067f118c4a798af639bd31e3 | e70cd58d63cd00119202ef7c17becfe989a2a1d7067f118c4a798af639bd31e3 | EQUAL | calibration/f3_step2_adequacy_harness_r4_2026-09-24.py.sha256 |
| 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c | 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c | EQUAL | calibration/f3_step2_fixture_generator_r4_2026-09-24.py |
| cf655df0c60b7b88dfc532342cb0f6e5c536b558d40ec557b5f3e2cccbdec51d | cf655df0c60b7b88dfc532342cb0f6e5c536b558d40ec557b5f3e2cccbdec51d | EQUAL | calibration/f3_step2_fixture_generator_r4_2026-09-24.py.sha256 |
| c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 | c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 | EQUAL | calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv |
| fec2eadf0c3dbc590cf7691dca4750486fef1778ae2131ae9cbf4a85c5004ed1 | fec2eadf0c3dbc590cf7691dca4750486fef1778ae2131ae9cbf4a85c5004ed1 | EQUAL | calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv.sha256 |
| 0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f | 0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f | EQUAL | provenance/f3_step2_r4_preexecution_custody_2026-09-24.md |
| 8af35f8226f13400184974282d9d10d0904398390c0d7a7f8541650137f68076 | 8af35f8226f13400184974282d9d10d0904398390c0d7a7f8541650137f68076 | EQUAL | provenance/f3_step2_r4_preexecution_custody_2026-09-24.md.sha256 |
| 11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 | 11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 | EQUAL | calibration/f3_step2_telemetry_r4_2026-09-24.csv |
| 61cc185d764c6a4386652f724f94a324b14e735a8fc3dad5cc12ddd04e113b8b | 61cc185d764c6a4386652f724f94a324b14e735a8fc3dad5cc12ddd04e113b8b | EQUAL | calibration/f3_step2_telemetry_r4_2026-09-24.csv.sha256 |
| a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | EQUAL | calibration/f3_step2_results_r4_2026-09-24.json |
| 6d94e20735b065f9ccda216d3adcbb55daba209f04b5caf56bdc4dde4595e527 | 6d94e20735b065f9ccda216d3adcbb55daba209f04b5caf56bdc4dde4595e527 | EQUAL | calibration/f3_step2_results_r4_2026-09-24.json.sha256 |
| 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | EQUAL | calibration/f3_step2_residual_series_r4_2026-09-24.json |
| 2de333210441f033375a8f63f7a2969f164c94b2ebbba7a7688d553907be16f7 | 2de333210441f033375a8f63f7a2969f164c94b2ebbba7a7688d553907be16f7 | EQUAL | calibration/f3_step2_residual_series_r4_2026-09-24.json.sha256 |
| 118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 | 118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 | EQUAL | calibration/f3_step2_test_evidence_r4_2026-09-24.json |
| 8a86e0637b6aa250d728ce5cc537642042757f99c54cf6d2300fe31b80e169e5 | 8a86e0637b6aa250d728ce5cc537642042757f99c54cf6d2300fe31b80e169e5 | EQUAL | calibration/f3_step2_test_evidence_r4_2026-09-24.json.sha256 |
| 0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4 | 0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4 | EQUAL | calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md |
| c559334743875f4aa1d5222d509133c30a9355bbc97b787e5cca8158f417aaca | c559334743875f4aa1d5222d509133c30a9355bbc97b787e5cca8158f417aaca | EQUAL | calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md.sha256 |
| 5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848 | 5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848 | EQUAL | provenance/f3_step2_correction_report_r4_2026-09-27.md |
| 572ddd0bc6abbc5f739d72c2282313c741b9d76d410f455df48e61b39da0b1b9 | 572ddd0bc6abbc5f739d72c2282313c741b9d76d410f455df48e61b39da0b1b9 | EQUAL | provenance/f3_step2_correction_report_r4_2026-09-27.md.sha256 |
| 8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69 | 8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69 | EQUAL | provenance/f3_step2_r4_attempt_log_2026-09-24.md |
| d82c3fdc80f069293845e28b43cfeaa2531c90ca3c740fce4967bf588ab54bf3 | d82c3fdc80f069293845e28b43cfeaa2531c90ca3c740fce4967bf588ab54bf3 | EQUAL | provenance/f3_step2_r4_attempt_log_2026-09-24.md.sha256 |
| d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 | d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 | EQUAL | calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv |
| ea9e877f5663d45915832dfc9c91231d06ab631ae083bacbadfde1d67a8d1395 | ea9e877f5663d45915832dfc9c91231d06ab631ae083bacbadfde1d67a8d1395 | EQUAL | calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv.sha256 |
| f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 | f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 | EQUAL | calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv |
| 58458ee9d11d9417131dd66fb13dcb3c99d007c4b3058005ccfcd7420ebc12d0 | 58458ee9d11d9417131dd66fb13dcb3c99d007c4b3058005ccfcd7420ebc12d0 | EQUAL | calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv.sha256 |
| 756fcf5b466903a812f408f2008676b3f8597acbc63ea2fccc1d30a9b3c1a85b | 756fcf5b466903a812f408f2008676b3f8597acbc63ea2fccc1d30a9b3c1a85b | EQUAL | calibration/f3_step2_adequacy_harness_r3_2026-09-22.py.sha256 |
| 7761a2f4324384975f5e143c370951f817726cf40af38f3f88d4a34279a598d3 | 7761a2f4324384975f5e143c370951f817726cf40af38f3f88d4a34279a598d3 | EQUAL | calibration/f3_step2_fixture_generator_r3_2026-09-22.py.sha256 |
| 955f010c3c9c21db66e48dcd2ae19e2bcea2bf0409fbae6e963a36ff63e5b872 | 955f010c3c9c21db66e48dcd2ae19e2bcea2bf0409fbae6e963a36ff63e5b872 | EQUAL | calibration/f3_step2_fixture_manifest_r3_2026-09-22.csv.sha256 |
| feace2bed9cef15ecc34e164c1c8e56bc704f77a490db85090bcaa2f1518b5f8 | feace2bed9cef15ecc34e164c1c8e56bc704f77a490db85090bcaa2f1518b5f8 | EQUAL | provenance/f3_step2_r3_preexecution_custody_2026-09-22.md.sha256 |
| 8a801fde61fa5e13fc0ec268f39d6d1ff120a9094302d273a92032bf534cff65 | 8a801fde61fa5e13fc0ec268f39d6d1ff120a9094302d273a92032bf534cff65 | EQUAL | calibration/f3_step2_telemetry_r3_2026-09-22.csv.sha256 |
| 714b5072589bec65f32f2a76f5b49130f4064b73bfd9ce5e9eb68df95570ed35 | 714b5072589bec65f32f2a76f5b49130f4064b73bfd9ce5e9eb68df95570ed35 | EQUAL | calibration/f3_step2_results_r3_2026-09-22.json.sha256 |
| 91dd3b85ff1e4ad3a08e231cf32d0c38db1599da1d70847519508721da50d2ee | 91dd3b85ff1e4ad3a08e231cf32d0c38db1599da1d70847519508721da50d2ee | EQUAL | calibration/f3_step2_residual_series_r3_2026-09-22.json.sha256 |
| 5e99371a02ef30024ca32c90c6c254df49578ac01a714797d334669bee0ceb12 | 5e99371a02ef30024ca32c90c6c254df49578ac01a714797d334669bee0ceb12 | EQUAL | calibration/f3_step2_test_evidence_r3_2026-09-22.json.sha256 |
| 152db9556126c54e67c8cfbc3a144468f7bad5ca7111e15b8550b1d1f8111893 | 152db9556126c54e67c8cfbc3a144468f7bad5ca7111e15b8550b1d1f8111893 | EQUAL | provenance/f3_step2_correction_report_r3_2026-09-24.md.sha256 |
| ce2cbe70a5112531a35c673b0f5eacfd35b627b701f291be2990d72267b4e5ea | ce2cbe70a5112531a35c673b0f5eacfd35b627b701f291be2990d72267b4e5ea | EQUAL | provenance/f3_step2_r3_start_state_inventory_2026-09-22.md.sha256 |
| ffc90aabe0de6fb8bb2ac7de3c855032b979ad80122a94927d158e0c292166f1 | ffc90aabe0de6fb8bb2ac7de3c855032b979ad80122a94927d158e0c292166f1 | EQUAL | provenance/f3_step2_r3_attempt_log_2026-09-22.md.sha256 |
| 790cf31adb25b33bd8feb82c3cc00046f61470ecf02a499c581b92a4cc7373fe | 790cf31adb25b33bd8feb82c3cc00046f61470ecf02a499c581b92a4cc7373fe | EQUAL | calibration/f3_step2_spline_percall_telemetry_r3_2026-09-22.csv.sha256 |
| d5539e0064f5aa9ce190eec144c64e32e7b858f763358f65a42b8f86747065e9 | d5539e0064f5aa9ce190eec144c64e32e7b858f763358f65a42b8f86747065e9 | EQUAL | calibration/f3_step2_r3_restart_store_manifest_2026-09-22.csv.sha256 |
| 78e6627d94bae3bc7b20f5b6d998b7ff733ea3f37e18fab3b1d58826430a93c9 | 78e6627d94bae3bc7b20f5b6d998b7ff733ea3f37e18fab3b1d58826430a93c9 | EQUAL | quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md |
| 88558b260227aa0830a7bc65be9301f8e70965c6cfcc8901c09985cb02de661c | 88558b260227aa0830a7bc65be9301f8e70965c6cfcc8901c09985cb02de661c | EQUAL | quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md |
| 9db9079f3fe05944fc25188a423b44ce0a2020baa87a0876465beb505ced985f | 9db9079f3fe05944fc25188a423b44ce0a2020baa87a0876465beb505ced985f | EQUAL | quarantine/f3_step2_r3_independent_audit_corrections_note_2026-09-23.md |
| 3a1ad5aa694f52dd15f8e50b689df992f5688715d9f183c706e65b6112dc3470 | 3a1ad5aa694f52dd15f8e50b689df992f5688715d9f183c706e65b6112dc3470 | EQUAL | quarantine/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md |
| 683108f3e6960fc1a4e18bd0f80679624e255dd4520a9b6f7bd2f71a3435fcad | 683108f3e6960fc1a4e18bd0f80679624e255dd4520a9b6f7bd2f71a3435fcad | EQUAL | quarantine/f3_step2_r3_auditor_transmittal_note_corruption_incident_2026-09-23.md |
| 6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31 | 6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31 | EQUAL | quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py |
| c8d47629ea56e8228a3ac7358ca4c4cd10d339403a32e6a54ed314966f6688bd | c8d47629ea56e8228a3ac7358ca4c4cd10d339403a32e6a54ed314966f6688bd | EQUAL | quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT1_SUPERSEDED.md |
| 891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd | 891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd | EQUAL | quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py |
| a4c7d65c8d778277b92e83e14a31a90a51b6e5e1df18f2c8da815d7ce00de0c0 | a4c7d65c8d778277b92e83e14a31a90a51b6e5e1df18f2c8da815d7ce00de0c0 | EQUAL | quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.md |
| f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5 | f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5 | EQUAL | quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py |
| e67bd9d79eed56f78092b460a54a586195ab72703ed937489872935c815d5905 | e67bd9d79eed56f78092b460a54a586195ab72703ed937489872935c815d5905 | EQUAL | quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.md |
| 99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a | 99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a | EQUAL | quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py |
| 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657 | 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657 | EQUAL | quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md |
| 0ebaaaeb15afff233758ccb073e71df3840ea0edc7b5fa2df9ae066c8608c4a4 | 0ebaaaeb15afff233758ccb073e71df3840ea0edc7b5fa2df9ae066c8608c4a4 | EQUAL | quarantine/f3_step2_r4_attempt1_supersession_note_2026-09-24.md |
| f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418 | f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418 | EQUAL | quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py |
| 307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441 | 307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441 | EQUAL | quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.md |
| 1f1e0e080930be80311ff7a1ff08f75984991a0fb3e05c905ce0b2e5889bf818 | 1f1e0e080930be80311ff7a1ff08f75984991a0fb3e05c905ce0b2e5889bf818 | EQUAL | quarantine/f3_step2_r4_attempt2_interruption_note_2026-09-26.md |
| 20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306 | 20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306 | EQUAL | quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py |
| 856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78 | 856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78 | EQUAL | quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT2_INTERRUPTED.md |
| e467d95ffa8995738b2cba45b18322c95c03c1c09a138fce44c8c49843136815 | e467d95ffa8995738b2cba45b18322c95c03c1c09a138fce44c8c49843136815 | EQUAL | quarantine/f3_step2_r4_attempt34_k05_nondeterminism_note_2026-09-26.md |
| 814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f | 814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f | EQUAL | quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py |
| 51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f | 51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f | EQUAL | quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.md |
| 3ba2075f986300486f69f3958a4ed28edce06ac9b13e326b879a03c582d7f831 | 3ba2075f986300486f69f3958a4ed28edce06ac9b13e326b879a03c582d7f831 | EQUAL | quarantine/f3_step2_r4_attempt56_mutation_leak_note_2026-09-27.md |
| 90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805 | 90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805 | EQUAL | quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py |
| cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273 | cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273 | EQUAL | quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.md |
| 40b3a53d2a4628ce3736585d17ea63aeea93f19a16f0c0e67b7c3e6262fca006 | 40b3a53d2a4628ce3736585d17ea63aeea93f19a16f0c0e67b7c3e6262fca006 | EQUAL | quarantine/f3_step2_r4_attempt1_stdout_2026-09-24.log |
| 71a0bfd2c1914ff93edd4aec3d3efdec95c318cc7e04ddc8b41ea169ef201dd1 | 71a0bfd2c1914ff93edd4aec3d3efdec95c318cc7e04ddc8b41ea169ef201dd1 | EQUAL | quarantine/f3_step2_r4_attempt2_stdout_2026-09-26.log |
| fbbcc5e6c7d8c627d6109a3dd93466fc8a229cdd5f0cd33849cc0ef57a7cccef | fbbcc5e6c7d8c627d6109a3dd93466fc8a229cdd5f0cd33849cc0ef57a7cccef | EQUAL | quarantine/f3_step2_r4_attempt3_stdout_2026-09-26.log |
| 3b87122312f6d4908fa540d989f728a41ede07b37506a7c0b980b9fe45000328 | 3b87122312f6d4908fa540d989f728a41ede07b37506a7c0b980b9fe45000328 | EQUAL | quarantine/f3_step2_r4_attempt4_stdout_2026-09-26.log |
| ca429b22c2920fd91ae86abafd552de0f5f6c7706d7fd37d42c05e337814467e | ca429b22c2920fd91ae86abafd552de0f5f6c7706d7fd37d42c05e337814467e | EQUAL | quarantine/f3_step2_r4_attempt5_stdout_2026-09-26.log |
| 3130cb5f14e0f44abb216c2515a098ddd220c8b16c928b2b1411d79863561d2f | 3130cb5f14e0f44abb216c2515a098ddd220c8b16c928b2b1411d79863561d2f | EQUAL | quarantine/f3_step2_r4_attempt6_stdout_2026-09-27.log |
| 7a77da84978577de2483efbe8baa0f98cce6a7d6ca616153e21980ca67b127b1 | 7a77da84978577de2483efbe8baa0f98cce6a7d6ca616153e21980ca67b127b1 | EQUAL | quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv |
| 9fe259d5d96a05b8e8e6ae3abbda648d23fb3f4b01d07db9ce4fbddd94858896 | 9fe259d5d96a05b8e8e6ae3abbda648d23fb3f4b01d07db9ce4fbddd94858896 | EQUAL | quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv.sha256 |

r4: **72/72 EQUAL**

## (c) ERRATUM-R41A-04 (the r4-2 report stays unmodified)

> the r4-2 report's hash block printed 14 deliverables in full, the four launch logs and the
> attempt-1 harness copy by 8-hex prefix, and the register, the attempt log and the
> interruption note by sidecar reference; the full values are listed in (a) of the rp1
> start-state inventory

## (d) Fingerprint erratum (A-5 R42A-05 (i); re-verified from the store manifest, 2026-10-02)

The r4-2 attempt log (ERRATUM-3 scope line, file line 164) names `0f32c7911cf8fccb` as a
fingerprint of the r4-2 run; that value is ATTEMPT 1's fingerprint, under which NO unit was
ever written (the attempt-1 process was interrupted before the restart layer existed for it;
units_read_from_store of the final run are all 0). The r4-2 store manifest
(`calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv`, 1082e0eb…, 11,869 rows)
was re-read for this inventory: every row's key prefix is `4ced291f15fb5afd` and no other
prefix occurs. The r4-2 attempt log stays unmodified; this line is the erratum.

## (e) D-8, A-5 and D-9 as found in the repository (with their sidecars)

| sha256 (recomputed) | sidecar says | file (p_konum_plus/prompts/) |
|---|---|---|
| aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae | EQUAL | f3_step2_r4-2_pi_decision_record_2026-10-01.md |
| 9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575 | EQUAL | f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md |
| 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 | EQUAL | f3_step2_qualification_pi_decision_record_2026-10-02.md |

```text
real_data_access = false ; commit = false
```
