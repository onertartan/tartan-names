# p_konum_plus — F3 STEP-2 r3 — Start-State Inventory (W-1 (a))

```text
artifact_role = start-state inventory (deliverable 11 of the r3 cycle; prompt DRAFT v2 §3 W-1 (a))
status        = NON-NORMATIVE ; every value below is an executor claim
written        = 2026-09-22, before any W-2/W-3/W-4 action
scope          = every file/directory under p_konum_plus/ whose name contains "f3_step2" or
                 "checkpoint" (find, case-sensitive glob), UNION every path
                 `git status --porcelain -uall -- p_konum_plus` reports at this moment
repository     = G:/PycharmProjects/pkp-worktree ; branch p_konum_plus ; HEAD 3e4daf4
commit         = false
```

## Result of the scan

No path under `p_konum_plus/` matches "checkpoint" in either input set. The directory
`p_konum_plus/calibration/.r2_checkpoint_2026-09-07` that the r2 harness wrote does not exist. It
was deleted (not moved to quarantine) by the executor at the end of the r2 cycle, in the same
conversation that produced the r2 deliverables, before this r3 prompt existed — disclosed at the
time only in a chat message to the PI, not in any r2 deliverable file. This is the defect Y-01
names. There is therefore nothing for W-1 (b) to move: **the "file of an earlier attempt" class
is empty by inspection, not by exclusion** — its would-be contents were destroyed before this
task began. Per the firewall ("no reconstruction of a missing file from memory, a transcript or
a cache"), the checkpoint directory's original contents are NOT reconstructed here. What can be
established about it (that it existed, its approximate size, and when it was removed) is stated
in the correction report's attempt-history section (deliverable 10, item 13), sourced from the
executor's own chat record of that turn, cited as a transcript statement, not invented.

132 paths were found (union of both input sets, deduplicated). Every one resolved to an existing
regular file; none is a directory and none is missing. Classification counts:

```text
frozen (section 2.1)                 15  (13 distinct items + 2 of their sidecars)
r1 package (item 12-18 + sidecars)   14
r2 package (R-01..R-10 + sidecars)   20
prompt / PI file (D-1..D-4 + sidecars) 7
CI-01 object                          2
record-class C-5 (r2 stop report)     1
bytecode cache                        4
other (F0/F1/F2/F3-STEP1 provenance; unrelated to this task) 68
file of an earlier attempt            0  (see note above)
unlisted                              0
```

Two items noted, neither acted on:
- `p_konum_plus/prompts/Claude_Chat_F3_STEP2_v5_section16_feedback.md` is git-staged (`A`, in the
  index) — not something this task staged; not unstaged, not touched, per "preserve every
  existing user modification."
- The four `.pyc` files under `p_konum_plus/calibration/__pycache__/` are leftover bytecode
  caches from earlier `python` invocations that did not use `-B`. They are not computed objects
  of any cycle. From this task's W-4 process onward, the interpreter is started with `-B` so no
  new ones are written; the existing four are left in place (not a custody item, not moved).

## Full table (path, class, size in bytes, last-modified, SHA256)

Every SHA256 below was computed directly against the file on disk at inventory time; it is not
copied from any sidecar or from any other document. Frozen, r1-package and r2-package rows were
cross-checked against the hashes printed in prompt DRAFT v2 §2.1/§2.2 before this file was
written (§3 P-1) and matched exactly — this table is that same evidence in inventory form, not a
separate claim.

| path | class | size | modified | sha256 |
|---|---|---|---|---|
| p_konum_plus/calibration/__pycache__/f3_step2_adequacy_harness_r1_2026-09-06.cpython-311.pyc | bytecode cache (not a computed object per this prompt; python -B going forward) | 81923 | 2026-09-06 17:12:58 | 3d9081dec5f16d72373255817e03bbbd39818d26cb75cebe4fd4f17825b96c64 |
| p_konum_plus/calibration/__pycache__/f3_step2_adequacy_harness_r2_2026-09-07.cpython-311.pyc | bytecode cache (not a computed object per this prompt; python -B going forward) | 135386 | 2026-09-08 23:53:56 | ff0da64663c2f07b1158621c38d1852c740a8f68c94faf0cfaa9fd7ef34a4976 |
| p_konum_plus/calibration/__pycache__/f3_step2_fixture_generator_r1_2026-09-06.cpython-311.pyc | bytecode cache (not a computed object per this prompt; python -B going forward) | 23297 | 2026-09-06 17:15:08 | d72aabff12379b3b7595eb54b6ce63ad2bd9537de3dc1f619d8fa11b09c47573 |
| p_konum_plus/calibration/__pycache__/f3_step2_fixture_generator_r2_2026-09-07.cpython-311.pyc | bytecode cache (not a computed object per this prompt; python -B going forward) | 34606 | 2026-09-09 00:00:00 | 8f809f47b33d6d1de7679e6c394ec717888037e02420516d8018e34272fcb729 |
| p_konum_plus/calibration/f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md | frozen (section 2.1, item 6) | 19570 | 2026-08-30 23:38:52 | 8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6 |
| p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv | frozen (section 2.1, item 5) | 372015 | 2026-08-30 23:36:31 | c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666 |
| p_konum_plus/calibration/f2_generator_specification_record_2026-08-29.md | other (F0-F2/STEP1 historical; unrelated) | 29253 | 2026-08-29 17:56:24 | d6f4aaf1ea2e43cfe94b5bd22fddd7bec0ac69c398d5ddba9caa2a8942d039b7 |
| p_konum_plus/calibration/f2_generator_specification_record_FINAL_FREEZE_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 12497 | 2026-09-02 11:46:40 | 2f191f0b0b24d962dfb0356be0daf201810ae9cb85d46b4164907cc43cce91f6 |
| p_konum_plus/calibration/f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md | frozen (section 2.1, item 2) | 14802 | 2026-09-02 12:34:15 | ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43 |
| p_konum_plus/calibration/f2_generator_specification_record_r2_2026-08-31.md | other (F0-F2/STEP1 historical; unrelated) | 35201 | 2026-08-31 22:47:14 | d5dd001df36360823d9d61fecd2f3ce85130dd106a51d110e4bf3aa377db22e4 |
| p_konum_plus/calibration/f2_generator_specification_record_r2a_2026-09-01.md | other (F0-F2/STEP1 historical; unrelated) | 19759 | 2026-09-01 01:08:05 | 2bc141c270a5ec730b6e20772ec0a36f1ec339348979246370f786bd42c708a2 |
| p_konum_plus/calibration/f2_step2_feasibility_harness_2026-09-01.py | other (F0-F2/STEP1 historical; unrelated) | 38186 | 2026-09-01 14:51:42 | 45b426447803ceb0cf6c029393ca606d89a5fb006d5ab34ce4b43ca4160f86db |
| p_konum_plus/calibration/f2_step2_feasibility_harness_r2_2026-09-01.py | other (F0-F2/STEP1 historical; unrelated) | 53514 | 2026-09-01 17:26:16 | 3b2555508e4b731ab3349a040a03a3d266fe068d72cd13427107a998622610bc |
| p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py | frozen (section 2.1, item 3 -- frozen F2 engine) | 57611 | 2026-09-02 00:06:24 | 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 |
| p_konum_plus/calibration/f2_step2_feasibility_telemetry_2026-09-01.csv | other (F0-F2/STEP1 historical; unrelated) | 1323 | 2026-09-01 14:52:00 | 144a3b09776e05dff3c490725fda1bc17b07bd759a48033be338778889fa62f6 |
| p_konum_plus/calibration/f2_step2_feasibility_telemetry_r2_2026-09-01.csv | other (F0-F2/STEP1 historical; unrelated) | 1321 | 2026-09-01 17:26:37 | d688a16bfd131ee1e1cfe8715a011009b782a78a1ac897c5589cc68af3b8dabb |
| p_konum_plus/calibration/f2_step2_feasibility_telemetry_r3_2026-09-01.csv | frozen (section 2.1, item 7) | 1572 | 2026-09-02 00:06:51 | cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49 |
| p_konum_plus/calibration/f2_step2_fixture_manifest_2026-09-01.csv | frozen (section 2.1, item 4) | 8904 | 2026-09-01 14:47:48 | daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b |
| p_konum_plus/calibration/f3_spline_solver_qualification_harness_2026-09-02.py | other (F0-F2/STEP1 historical; unrelated) | 12876 | 2026-09-03 15:03:56 | ecda07d0fee36d8988c82c31aeb8e231b812e7a4df400af9c6a80676e4cf5917 |
| p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py | frozen (section 2.1, item 8 -- harness) | 23196 | 2026-09-03 17:18:48 | b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d |
| p_konum_plus/calibration/f3_spline_solver_qualification_manifest_2026-09-02.csv | other (F0-F2/STEP1 historical; unrelated) | 8850 | 2026-09-03 12:14:19 | 522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883 |
| p_konum_plus/calibration/f3_spline_solver_qualification_manifest_r2_2026-09-03.csv | frozen (section 2.1, item 8 -- manifest) | 54388 | 2026-09-03 17:18:58 | e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32 |
| p_konum_plus/calibration/f3_spline_solver_qualification_results_r2_2026-09-03.csv | frozen (section 2.1, item 8 -- results) | 12744 | 2026-09-03 17:19:07 | ffda04b01abb1dd5399e7fb6434c006616723bf6ba7d95bfc697baeb6dd40484 |
| p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md | frozen (section 2.1, item 11) | 31981 | 2026-09-05 22:55:34 | bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f |
| p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md.sha256 | frozen (item 11 sidecar) | 119 | 2026-09-05 22:56:27 | 4a1ff40e9b50afa94661ea00a1565775ea70a28c8e910bc63389db21c2152188 |
| p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md | frozen (section 2.1, item 10) | 34595 | 2026-09-05 23:44:35 | 7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460 |
| p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md.sha256 | frozen (item 10 sidecar) | 122 | 2026-09-05 23:44:41 | 63959f655c39b83776307de319f658bf368b8fd9408239d7fda3aac39d58ea5a |
| p_konum_plus/calibration/f3_step1_r1_corrected_ratification_candidate_r2_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 22639 | 2026-09-03 15:07:17 | b8ce7667200787eeda6e71b6d8ede6aebc9bb4fd1b05344dc31f62f361bc399c |
| p_konum_plus/calibration/f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 23581 | 2026-09-03 17:52:42 | 350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad |
| p_konum_plus/calibration/f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md | frozen (section 2.1, item 9) | 35973 | 2026-09-05 02:58:01 | 5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad |
| p_konum_plus/calibration/f3_step2_adequacy_harness_r1_2026-09-06.py | r1 package (item 12) | 47742 | 2026-09-06 18:36:25 | a95ad152b1ebcca6ff8b9ccfd34d122b9d6225a44d51254f4621fd4776a5b12f |
| p_konum_plus/calibration/f3_step2_adequacy_harness_r1_2026-09-06.py.sha256 | r1 package sidecar (item 19) | 109 | 2026-09-06 19:16:10 | b5acfcb7f2d4f149749cfabe999a77fba2b9f225b44147aea30850345ba7033b |
| p_konum_plus/calibration/f3_step2_adequacy_harness_r2_2026-09-07.py | r2 package (R-01) | 89935 | 2026-09-08 23:53:13 | 78b6210ace605fe9b43a3b15716535df28b8a25a11a072f68484e9cb7ad12776 |
| p_konum_plus/calibration/f3_step2_adequacy_harness_r2_2026-09-07.py.sha256 | r2 package sidecar (R-11) | 109 | 2026-09-09 00:04:50 | 907e229d0c3814f120ebd3ff882c0edc04cc84999dc9da5cfb0bb183b302efe4 |
| p_konum_plus/calibration/f3_step2_class_c_pin_register_r1_2026-09-06.md | r1 package (item 17) | 9907 | 2026-09-06 19:14:23 | 03486232ac62206b1eed52c2355e465364ec10fc02fb13d62dd32e2dfd50f9ca |
| p_konum_plus/calibration/f3_step2_class_c_pin_register_r1_2026-09-06.md.sha256 | r1 package sidecar (item 19) | 113 | 2026-09-06 19:16:10 | 10e0665874a8b4ee3306e4880fd1454ac2f9b09c56ce6636f8da5780292303ca |
| p_konum_plus/calibration/f3_step2_class_c_pin_register_r2_2026-09-07.md | r2 package (R-09) | 14010 | 2026-09-09 00:03:09 | f263eaceffb94a458f331fb80258e779f0a740634d2420e696406b191a7142d5 |
| p_konum_plus/calibration/f3_step2_class_c_pin_register_r2_2026-09-07.md.sha256 | r2 package sidecar (R-11) | 113 | 2026-09-09 00:04:50 | fda591f9140a1b693a5ea655100433f3a357af6e18a31018d6ba58f37a7a6231 |
| p_konum_plus/calibration/f3_step2_fixture_generator_r1_2026-09-06.py | r1 package (item 13 -- hash observed, not compared) | 18059 | 2026-09-06 17:15:01 | 03f3ac07e354342f41493b3ed771cdef10e3ba373d3bde92020ec6a730cdcdc3 |
| p_konum_plus/calibration/f3_step2_fixture_generator_r1_2026-09-06.py.sha256 | r1 package sidecar (item 19) | 110 | 2026-09-06 19:16:10 | e6f97967a54e86de5bc8ecd0001cfd29e08af0e2b2b77e69a9fbe809753b49d1 |
| p_konum_plus/calibration/f3_step2_fixture_generator_r2_2026-09-07.py | r2 package (R-02) | 30822 | 2026-09-08 23:59:53 | a1e6068c0868e7594242fcc6d588cc255f3b0f4bdf21d1e93851e5bafcf98e25 |
| p_konum_plus/calibration/f3_step2_fixture_generator_r2_2026-09-07.py.sha256 | r2 package sidecar (R-11) | 110 | 2026-09-09 00:04:50 | c9cdff8ddfd1e58a3a2e272197743acb3ffd5bc4bde068aa763d40d46aae4f8c |
| p_konum_plus/calibration/f3_step2_fixture_manifest_2026-09-06.csv | r1 package (item 14) | 5657 | 2026-09-06 18:36:33 | d9fb75f8c643f53a67032e4b65a5bec1af85ccbdf1cb47c58577c1d3f23b565b |
| p_konum_plus/calibration/f3_step2_fixture_manifest_2026-09-06.csv.sha256 | r1 package sidecar (item 19) | 107 | 2026-09-06 19:16:10 | d8a72c8cd591ccf3293bf0c3ebb4049b7ad42ae57cc1bd77f586fa30dc61b088 |
| p_konum_plus/calibration/f3_step2_fixture_manifest_r2_2026-09-07.csv | r2 package (R-03) | 12229 | 2026-09-09 00:00:13 | 807f49b30ac453e95259d39b546515acff8f93c2d6b7bebf81cd4a44621e3beb |
| p_konum_plus/calibration/f3_step2_fixture_manifest_r2_2026-09-07.csv.sha256 | r2 package sidecar (R-11) | 110 | 2026-09-09 00:04:50 | 307f50ca1f36ca8adf10a1b8c6e42888834dc6f9498f6aa74a964ed603e27f09 |
| p_konum_plus/calibration/f3_step2_residual_series_r2_2026-09-07.json | r2 package (R-07) | 46709 | 2026-09-09 00:00:28 | f28bd6a02978154d1ba71d83a8ffe42cdc5e95d12a26c43b886439cca19b94f5 |
| p_konum_plus/calibration/f3_step2_residual_series_r2_2026-09-07.json.sha256 | r2 package sidecar (R-11) | 110 | 2026-09-09 00:04:50 | 4ae68b8bddccf3b4f105253f627e0901e02c4e59183932c075efbfc10dd065cc |
| p_konum_plus/calibration/f3_step2_results_r1_2026-09-06.json | r1 package (item 16) | 187128 | 2026-09-06 19:13:42 | e32de3f7ae43d39c87a21384a46fe84c42c940d7a48bd2cdb83fe2d4d29f06eb |
| p_konum_plus/calibration/f3_step2_results_r1_2026-09-06.json.sha256 | r1 package sidecar (item 19) | 102 | 2026-09-06 19:16:10 | 9fb167269a408882c44afcb430c13de14e1d4f283f13f44a9b993681eff59b44 |
| p_konum_plus/calibration/f3_step2_results_r2_2026-09-07.json | r2 package (R-06) | 280750 | 2026-09-09 00:00:29 | 7b78b7ba64ded891fdd5098d3a35556938d1314c5d712a7dc6ee6046b7a26ed2 |
| p_konum_plus/calibration/f3_step2_results_r2_2026-09-07.json.sha256 | r2 package sidecar (R-11) | 102 | 2026-09-09 00:04:50 | 24c4d07fe53c68c678b6d56cebf016e12089fef0c66e8932f41a4f91935d5581 |
| p_konum_plus/calibration/f3_step2_telemetry_r1_2026-09-06.csv | r1 package (item 15) | 406106 | 2026-09-06 19:13:42 | 3ee208e72cc9d4f83b5d7d696f7252499c971480bc75e9aaabf6f51dbe0b08e0 |
| p_konum_plus/calibration/f3_step2_telemetry_r1_2026-09-06.csv.sha256 | r1 package sidecar (item 19) | 103 | 2026-09-06 19:16:10 | de0696c5f6f10c6258c56e451177a8cf8496c2b42f45c0580f20736c3866c8ed |
| p_konum_plus/calibration/f3_step2_telemetry_r2_2026-09-07.csv | r2 package (R-05) | 429714 | 2026-09-09 00:00:28 | 0459344f2b518531d5732577b98f031684ca29e3815c0e51af75b857be60155a |
| p_konum_plus/calibration/f3_step2_telemetry_r2_2026-09-07.csv.sha256 | r2 package sidecar (R-11) | 103 | 2026-09-09 00:04:50 | b34a022eb815bc276a76631049dcfe071d388c041de674aaeace1a69264b40ec |
| p_konum_plus/calibration/f3_step2_test_evidence_r2_2026-09-07.json | r2 package (R-08) | 18938 | 2026-09-09 00:00:28 | 109ca273fbaf2e47800c048a87e72e9064c576642ecbe2a7e9e1331cf9426c0b |
| p_konum_plus/calibration/f3_step2_test_evidence_r2_2026-09-07.json.sha256 | r2 package sidecar (R-11) | 108 | 2026-09-09 00:04:50 | e4c1f7f5de953688b58b1a1ae65336031f1d9070065662b5a91bc2627945f10c |
| p_konum_plus/prompts/Claude_Chat_F3_STEP2_v5_section16_feedback.md | other (historical v6-lineage feedback; git-staged A; not touched) | 5428 | 2026-09-07 16:34:16 | 721243ff7fce42f539db0bc3fa895059e427120538772d72aa05e9f5789995cd |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v1_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 5664 | 2026-09-05 22:47:50 | adb59f60e7c1a72b6e901b86d1958a874f09c1301003b32c4884816fe43ab792 |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v2_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 4145 | 2026-09-05 22:47:50 | 09df38443346229fc2dac0afb795e6c5cd6b621fe1e4e6756316c43416e96f65 |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 31498 | 2026-09-05 22:47:49 | da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7 |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 37947 | 2026-09-05 22:47:49 | 2860fade8d34e74b8ea77d22d469fa0c9b29e05eaf27310b407a45031a626243 |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v3_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 42589 | 2026-09-05 22:47:49 | 4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7 |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 46252 | 2026-09-05 22:47:50 | bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458 |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 49570 | 2026-09-05 22:47:49 | 679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09 |
| p_konum_plus/prompts/Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 32666 | 2026-09-05 22:47:49 | b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00 |
| p_konum_plus/prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md | prompt / PI file (D-1) | 105334 | 2026-09-07 16:36:39 | 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 |
| p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md | prompt / PI file (D-3, this prompt) | 102410 | 2026-09-22 11:03:46 | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 |
| p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md.sha256 | prompt / PI file sidecar (D-3) | 130 | 2026-09-22 11:03:47 | a5399a0967885a7a5c25df2f0e0390dfae750892b7b54ee2a2eee1b77ea78abe |
| p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md | prompt / PI file (D-2) | 17235 | 2026-09-07 21:58:09 | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 |
| p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md.sha256 | prompt / PI file sidecar (D-2) | 109 | 2026-09-07 21:58:20 | c2acbf840f4a15c7b3b68b0b53db8994c4415c538520cce9655ccf1dacf52795 |
| p_konum_plus/prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md | prompt / PI file (D-4) | 6848 | 2026-09-22 10:54:57 | 4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865 |
| p_konum_plus/prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md.sha256 | prompt / PI file sidecar (D-4) | 111 | 2026-09-22 10:54:58 | 9de7a3ac49add24707a92912504686fa0622e78f8dcd25b9069eb56f8bffe9ee |
| p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_Comparison_Evaluation_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 9775 | 2026-09-05 22:28:13 | c12b275291c7341b3bd7b27618c8a25a91ad36af91ac60261e4195fdf3c73777 |
| p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_v2_Review_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 11248 | 2026-09-05 22:28:13 | 07c3306339eabb86fce0f24578ee5e539d0fb85fb06e3e181a22cf0e3a0bb842 |
| p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_v3_Review_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 9791 | 2026-09-05 22:28:13 | 90051cb702d63d506213c04f38fac6c77d4651ddc812bb0733cd01bef346db0d |
| p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_v4_Review_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 6686 | 2026-09-05 22:28:13 | 8b04f83e439b786afce1ad969dfd12028ccc02a344e34e26e6f217aa343bac55 |
| p_konum_plus/provenance/f2_d09_exact_enumeration_packet_2026-08-30.md | other (F0-F2/STEP1 historical; unrelated) | 8485 | 2026-08-30 22:14:17 | 2a7558abe37187fd424ea3c1adba8f47605359520326efd6c01fc602ec45d453 |
| p_konum_plus/provenance/f2_d09_packet_endoftask_report_2026-08-30.md | other (F0-F2/STEP1 historical; unrelated) | 8127 | 2026-08-31 17:42:46 | 272012120a59ebf2e44f04fda92a782275881b04bf97bd9c3915f4c3efe7dab6 |
| p_konum_plus/provenance/f2_owner_decision_packet_report_2026-08-29.md | other (F0-F2/STEP1 historical; unrelated) | 7317 | 2026-08-29 17:57:50 | 979de1074bd204d80afc506c238954f52fee0c6145d98470c75fcf1d505d82cd |
| p_konum_plus/provenance/f2_r2_correction_ratification_report_2026-08-31.md | other (F0-F2/STEP1 historical; unrelated) | 11556 | 2026-08-31 22:48:19 | acaf02e2f49f509d940ee266d0ceaf637e6f7316b153aa8d7f0bdc61569a73a2 |
| p_konum_plus/provenance/f2_r2a_step1_5_class_c_correction_report_2026-09-01.md | other (F0-F2/STEP1 historical; unrelated) | 11157 | 2026-09-01 01:09:09 | bf6fb60c2c520356ecd3321fa25a0ee15a3572522044bf8e6723196a0f2e1296 |
| p_konum_plus/provenance/f2_reconciliation_source_check_report_2026-08-29.md | other (F0-F2/STEP1 historical; unrelated) | 4655 | 2026-08-29 22:19:57 | 6ea2cd576cdb494a994b41f5fb7a2234abd6844d57399e7e739002de0afc6aed |
| p_konum_plus/provenance/f2_step2_r2_correction_endoftask_report_2026-09-01.md | other (F0-F2/STEP1 historical; unrelated) | 8315 | 2026-09-01 22:47:33 | 5f27aa850dd5b4e98d6d2ff0e9677fcf74315d9a1be6ebaad0649730338774fc |
| p_konum_plus/provenance/f2_step2_r3_independent_audit_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 8206 | 2026-09-02 00:31:45 | f4f2cc2702efdc1e6b0eb0804c847e93420e439c2425961810304eefb9b3048c |
| p_konum_plus/provenance/f2_step2_synthetic_analytic_feasibility_report_2026-09-01.md | other (F0-F2/STEP1 historical; unrelated) | 17072 | 2026-09-01 14:54:36 | 9850075ea011fc0cad6740353abe138f6ed01acb2763803e72e5af5fe56a6d83 |
| p_konum_plus/provenance/f2_step2_synthetic_analytic_feasibility_report_r2_2026-09-01.md | other (F0-F2/STEP1 historical; unrelated) | 21173 | 2026-09-01 17:28:50 | 9d5bf074b099cf597009218a0c16cdba68dabcdd00ee4313165c7c59c165b445 |
| p_konum_plus/provenance/f2_step2_synthetic_analytic_feasibility_report_r3_2026-09-01.md | other (F0-F2/STEP1 historical; unrelated) | 20224 | 2026-09-02 00:09:12 | afd02531cf80fa441ad2d6e3b990583783963fc6042b87c98f0108af0629abf5 |
| p_konum_plus/provenance/f2_step3_final_freeze_endoftask_report_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 4335 | 2026-09-02 11:56:54 | 132271e3e90f925b37808d1adad52ccd59a5adac61fb5e015199649fd10e00ed |
| p_konum_plus/provenance/f2_step3_final_freeze_independent_audit_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 3989 | 2026-09-02 12:32:24 | 8bd0fb33f7c507829ec4ca253dd0a2cb2a5f7a05c65601a2c6f9f74de71e5630 |
| p_konum_plus/provenance/f2_step3_final_freeze_r1_correction_report_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 5650 | 2026-09-02 12:32:53 | 6ed8b0a263892b718fbe664143900a1af052fb9535f44740100b5d29ec6abcb7 |
| p_konum_plus/provenance/f2_step3_final_freeze_r1_independent_acceptance_audit_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 5116 | 2026-09-02 14:47:40 | 8402bb68a924ccaae34d6923f6f5b8de8277a13c4af4e7478bcd94f062076dfa |
| p_konum_plus/provenance/f2_step3_final_freeze_report_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 11546 | 2026-09-02 00:36:13 | 41c7ce03558d8ab6cd4e8c7aa6c088cf52763288eb57029dad095a33c882f3f1 |
| p_konum_plus/provenance/f2_step3_r1_acceptance_audit_custody_endoftask_report_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 1782 | 2026-09-02 14:50:05 | 293966809157956c2e2e1a283cb135d7782f46304c2808da86bdbbfd9cf201f7 |
| p_konum_plus/provenance/f2_step3_r1_correction_endoftask_report_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 3067 | 2026-09-02 14:00:34 | 0ba7931ea8add09dede3949ffa3e68946e9af123ffae9a6b3bfeed274241dd85 |
| p_konum_plus/provenance/f2_worksheet_updated3_verification_report_2026-08-29.md | other (F0-F2/STEP1 historical; unrelated) | 4445 | 2026-08-29 23:42:38 | 70d4787ade226bdf23551dbfc7222cc7bf4bc4df2987a2eb1880e5d0dc7c5267 |
| p_konum_plus/provenance/f3_preflight_endoftask_report_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 19970 | 2026-09-02 16:04:29 | 262f8e4170b2613a10b7f9361b2ae2f20f090eba7528ccebd5f45f0ae2d2e7a6 |
| p_konum_plus/provenance/f3_spline_qualification_r2_endoftask_report_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 3949 | 2026-09-03 17:22:01 | 82f5571db0a61b42b28ef7df39d2329e67e44422c06dd8bc319ab37429aef36c |
| p_konum_plus/provenance/f3_spline_solver_qualification_artifact_inventory_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 3808 | 2026-09-03 15:07:44 | cb349a191a7afafb0b5052bcc1a3dc29061873becca844eeeb2c7c9b524c8af7 |
| p_konum_plus/provenance/f3_spline_solver_qualification_artifact_inventory_r2_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 2963 | 2026-09-03 17:20:07 | d5a0382101013a9cf33442dad02055d07d701ce5fcc4a4a21e805c18385a6d09 |
| p_konum_plus/provenance/f3_spline_solver_qualification_preexecution_custody_r2_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 1456 | 2026-09-03 17:18:58 | cb182713ce037d1a29f4d9de6937030364124f143d162b1fad75e753baca4283 |
| p_konum_plus/provenance/f3_spline_solver_qualification_report_r2_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 5540 | 2026-09-03 17:19:46 | 5679c3bd3064b08804f360c80c7437425f3d69cad30d9f472524e3f86f890c1c |
| p_konum_plus/provenance/f3_step1_custody_import_endoftask_report_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 3924 | 2026-09-05 22:37:01 | 9d79ec5697e897d90ce88d663354e8bd2a3453cf77f990c21a9fb7b80801df23 |
| p_konum_plus/provenance/f3_step1_decision_packet_endoftask_report_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 22964 | 2026-09-02 16:17:11 | 143651a7ee1d0bc3b738057b4e0c8aa28253ace6c1432115e64e2c190a279c17 |
| p_konum_plus/provenance/f3_step1_freeze_record_independent_audit_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 11921 | 2026-09-05 23:43:45 | 99b615d2c3ee0c94815af7793e1d8be669a29ef5d070891224d457305864a4dc |
| p_konum_plus/provenance/f3_step1_freeze_record_r1_endoftask_report_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 3036 | 2026-09-06 02:26:21 | a10c32c4170575748dcfe1a332a995b405f4f3cf888d5bde1e1301597de940d6 |
| p_konum_plus/provenance/f3_step1_freeze_record_r1_narrow_reaudit_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 4307 | 2026-09-06 17:07:12 | 5470d1eccc8b80627c7032a940e0dac99a50be57ab3392aeb442b5ccf09cd4b8 |
| p_konum_plus/provenance/f3_step1_freeze_record_r1_report_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 3583 | 2026-09-05 23:45:09 | a48c516b7976cd4559f3825f124cf91e266f7107dfd1c5962c7a8249d43a08d2 |
| p_konum_plus/provenance/f3_step1_freeze_record_task_stop_report_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 3234 | 2026-09-05 22:02:02 | 57c92d2df6f2b923fedbb1cef3671238ca3020f8ac02cc16eb553eaa9026e969 |
| p_konum_plus/provenance/f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md | other (F0-F2/STEP1 historical; unrelated) | 25774 | 2026-09-05 22:28:22 | 34862e56e6db46d0a8b07c21dea66d149cb9fa3a0d91ab21c88f12f48e2ad892 |
| p_konum_plus/provenance/f3_step1_r1_corrected_ratification_candidate_2026-09-02.md | other (F0-F2/STEP1 historical; unrelated) | 29883 | 2026-09-03 12:22:15 | 6e7b56348f9a1ffe144d776b48bc559baf2cbf71fb02c84ff37cba11203992c6 |
| p_konum_plus/provenance/f3_step1_r1_r3_provenance_correction_report_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 4219 | 2026-09-03 17:53:18 | 006f6c615dd1e9bfddee739fb53d8565927ef41a2c9ab76b3cba082a96839815 |
| p_konum_plus/provenance/f3_step1_r1_v6_exactness_correction_report_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 15245 | 2026-09-03 15:05:21 | 8cb73e2f3c0e23289d596a46229c4f737a9730ac7888d855da3c99caee5596fa |
| p_konum_plus/provenance/f3_step1_r3_endoftask_report_2026-09-03.md | other (F0-F2/STEP1 historical; unrelated) | 2268 | 2026-09-03 18:32:31 | ad1351d03880d13fd6380b658afd1a25797bcc68b1118581081a20b6d6b2dcc3 |
| p_konum_plus/provenance/f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 8805 | 2026-09-05 02:59:06 | 5955e86590d1c4706000e4e43e6d5cf692dd000ba867a3b26170d1c5548de877 |
| p_konum_plus/provenance/f3_step1_r3_to_r4_independent_regenerated_diff_2026-09-05.txt | other (F0-F2/STEP1 historical; unrelated) | 16653 | 2026-09-05 22:28:12 | 9b070d4b1302ca5acbe19a8c69b2a67e17f823d5936f187ff47ff69405de2273 |
| p_konum_plus/provenance/f3_step1_r3_to_r4_semantic_diff_2026-09-05.txt | other (F0-F2/STEP1 historical; unrelated) | 14744 | 2026-09-05 02:58:08 | a8ba561e6ff61f0d2d401c9b58598205a7c3a9282786e5892527d48e26c6a043 |
| p_konum_plus/provenance/f3_step1_r4_independent_audit_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 26267 | 2026-09-05 22:28:12 | 84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea |
| p_konum_plus/provenance/f3_step1_ratification_provenance_report_2026-09-05.md | other (F0-F2/STEP1 historical; unrelated) | 6991 | 2026-09-05 22:56:19 | 2c746625acee73e610e09179ed00c1dc90c0dddc905c1c05d7dcf5c91c1ad1fc |
| p_konum_plus/provenance/f3_step1_ratification_provenance_report_2026-09-05.md.sha256 | other (F0-F2/STEP1 historical; unrelated) | 120 | 2026-09-05 22:56:27 | 403bd6b693dee7d30a72a649eced6726f57f0c4f939483c6c7505533f178e6c0 |
| p_konum_plus/provenance/f3_step2_correction_report_r2_2026-09-07.md | r2 package (R-10; CI-01 restored value) | 14695 | 2026-09-20 02:12:38 | af5b9151ebe4fc66e897899c1bc977f3cf7b3c0222da04601610affbb02c851b |
| p_konum_plus/provenance/f3_step2_correction_report_r2_2026-09-07.md.sha256 | r2 package sidecar (R-11) | 110 | 2026-09-09 00:04:50 | 005d66674726a01a363f1a5837f0d914b01d4b5924ff798ae4ca4dbf51f1b038 |
| p_konum_plus/provenance/f3_step2_r2_dispatch_precondition_stop_report_2026-09-07.md | record-class C-5 | 2828 | 2026-09-07 17:03:03 | 5065cefb4df88662a3dc29fc5a88eaefea3bbb9beb490c0dbbef2b513736f7cb |
| p_konum_plus/provenance/f3_step2_r2_preexecution_custody_2026-09-07.md | r2 package (R-04) | 1342 | 2026-09-09 00:00:13 | afddfb590b78caea08dcde0ca28141e31835a8b3857af973b30a6a5eeff8a743 |
| p_konum_plus/provenance/f3_step2_r2_preexecution_custody_2026-09-07.md.sha256 | r2 package sidecar (R-11) | 113 | 2026-09-09 00:04:50 | 05569bf233fe7f57ab302b15a7aad8dde931499441d0d00122262db16ae4f7a0 |
| p_konum_plus/provenance/f3_step2_synthetic_qualification_report_r1_2026-09-06.md | r1 package (item 18) | 11916 | 2026-09-06 19:15:59 | 413283efd5f5212d3c5bb0b5a5a0be3c22adc2fad41c6a4ab142733fbdde2b95 |
| p_konum_plus/provenance/f3_step2_synthetic_qualification_report_r1_2026-09-06.md.sha256 | r1 package sidecar (item 19) | 123 | 2026-09-06 19:16:11 | 8bb38341726b4a7c501d4a815b1a201305a637b5c5665a48a904bcde80d00b2c |
| p_konum_plus/provenance/nonnormative/claude_p_konum_plus_iki_v10_degerlendirme_ve_sentez_v11_TERMINAL_2026-08-26.md | other (F0-F2/STEP1 historical; unrelated) | 40235 | 2026-08-31 22:44:42 | 29c073ba5105a14299a0ea9427d8443c1a29d40960f7fed355ef49b2bae67c5a |
| p_konum_plus/provenance/nonnormative/ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md | other (F0-F2/STEP1 historical; unrelated) | 31410 | 2026-08-31 22:44:42 | 3bd9e7cfdbdfe9358f91792db12447594d86956cd1c1b185552cb2da4d94b787 |
| p_konum_plus/quarantine/f3_step2_correction_report_corruption_incident_note_2026-09-20.md | CI-01 object (executor's incident note) | 1100 | 2026-09-20 02:12:57 | 0de72545392a71e1b8c8ff4c10aa055ff2b26b629eb088b0d5235331fb7647b5 |
| p_konum_plus/quarantine/f3_step2_correction_report_r2_2026-09-07.md | CI-01 object (the modified copy) | 14699 | 2026-09-20 01:54:00 | 6b8cf801c66e15356dd4fa138b3f2bbc7e26c4b2a02d61599349d32dd487d94d |

## W-1 (b): quarantine action taken

None. There is no file of an earlier r3 attempt (this is attempt 1) and no r2-cycle checkpoint
directory or other earlier-attempt file remains to move (see "Result of the scan" above). The
CI-01 objects were already in `p_konum_plus/quarantine/` before this task and stay there
unmoved, per the rule that objects already under quarantine are left in place.

## W-1 (c): custody writes taken

None needed. Every sidecar of items 12-18 (r1) and R-01..R-10 (r2) is present and was verified
against its file before this inventory was written (§3 P-1). No record-class item was attached
at dispatch to import. D-1, D-2, D-3 and D-4 are already at their required paths under
`p_konum_plus/prompts/` (D-3 and D-4 were delivered there directly; nothing to copy).
