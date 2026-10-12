# F3 rp1-r1 independent technical audit — GPT-6 / Codex — DRAFT r1


## Identity and prior exposure


[A-S] Auditor: Codex, based on GPT-6; exact deployment/model variant is not exposed in this session. Session identification: workspace `G:\PycharmProjects\rp1r1_audit`, start `2026-10-09T16:42:26.314607+00:00`, independent harness pid `18956`. This session did not draft or execute the executor’s rp1/rp1-r1 packages and had no project exposure earlier in the provided conversation. It read historical audit material as input during this audit; no claim is made about model training exposure. No subagents were used. Audit completed at 2026-10-10T05:02:33.310670+00:00.


## Verdict


**NOT PASSED.** [A]/[A-S] Open B findings affect R-1, R-2, R-3, custody and accounting; K items on dependent code remain open. The current list’s historical hash mismatch is corrected and independently closed as IR1-01. A matching full rerun does not close defects in the gates. This report does not bind bytes, declare QUALIFIED/READY, or decide for the PI.


Evidence tiers: [A] checked on delivered commit bytes; [A-S] independently executed/measured in this audit; [X] executor/process-history claim not independently verified. Every negative determination below uses these tiers; absence of evidence is not an inferred scientific difference.


## Custody (§1)


[A-S] Audit instruction SHA256: `82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e`, equals supplied sidecar. Source working tree was clean at HEAD `d9a5e9905e25c634ad3132aae85c6c346e5ead30`. Audited target is exclusively `9035df0831d8646cca7f1e73937161a3d2d7d018`, extracted using Git object reads without checkout/commit/push. Later addendum bytes at HEAD are outside this audit’s governing commit.

[A] Parent diff b6d2483→9035df0: 1104 additions, all under p_konum_plus, no modified/deleted parent file. 63d4846→9035df0: exactly four additions (r1 list, disclosure, their sidecars). There are 38 added sidecars (36 at 63d4846 plus two), all correct. Both lists’ tables differ only in report hash and self-reference rows. The 33 current-list file/standing pins all match their named file bytes and sidecars; the list itself is pinned by its external sidecar, without a self-hash. The rp1 table’s 43 file rows all match. The report’s 29 full-hash file rows match. Three new standing sidecars are correct; F1 input-table sidecar stays deferred and was not created.

[A] Named dispatch/standing pins, reused generator/manifest, r4-2 baseline files, and previous inventory are independently hashed; start inventory previous hash is a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d. [A-S] Own W-3 wrote successfully and the unchanged harness verified custody/fingerprint and all 31 dispatch pins. [A] No committed restart store or transport ZIP is delivered. Store manifest/read log are record evidence, not direct verification of absent executor pickle payloads.

[A-S] Limited hash-column read only: 217 F1 input hashes; 1023 synthetic fixture files (1021 .txt plus manifest and sidecar), 298 distinct synthetic hashes, zero intersection. Neither eligible manifest nor any named real input was opened. [A] Helper and nine quarantined outputs are preserved; the raw-fixture sidecar exception lacks the explicit rationale requested by §1.1 (IR1-19).

[A] Expanded hash trace checks reproduce 108 full-hash occurrences in the original eight executor documents and 148 when r1 is added. Matching against an arbitrary file was used only to locate candidates; each named-file association was then checked with source context, report/list tables, dispatch aliases, baseline names and preserved attempt outputs. 104 original occurrences match named files, two canonical hashes were recomputed from evaluations/stops/pins, one is the disclosed historical mismatch, one is deleted dry custody [X]. Current r1 has no incorrect current named-file pin; wrong hash occurs only in its erratum and the superseded row. Generating-script-at-write-time provenance cannot be established from hash equality alone. ZIP/dry custody remain [X], not verified (IR1-14).


## Code (§2)


[A] Final harness SHA256 cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb equals attempt-2 W-3 pin. Both delivered diffs independently applied to their pinned rp1/r4-2 baselines reproduce the target exactly, with 36 labelled hunks each. Python difflib chooses different blank-line context than GNU diff; applying and verifying every old/context line establishes content equality without treating that formatting difference as a mismatch.

[A] Consumer changes take loader arrays, create family-qualified IDs, and guard scenario intake; fitting/evaluator arithmetic outside this intake is unchanged. All six mid() call changes concern IDs and satisfy PI-c scope; their S5-WIRING annotations are inaccurate. Independent hunk mapping and annotation deficiencies are in the appendix and IR1-16. No unauthorized scientific literal change was found in these diffs.

[A]/[A-S] Attempt1→2 executable changes consist of supersession/attempt metadata plus three R-3 changes. (a) COUNT double-canonicalization is a representation defect correction: declared transition is unchanged. (b) Removing bare exc_injection_fixtures restores recursion and the existing leaf ADDITION; undeclared differing leaves still become U, so this does not relax the content gate. Only that EXPECTATIONS_E entry was removed; the three capture EQUAL entries remain. (c) Extending provenance stripping to three capture lists removes false pid/time differences but strips entire traceback, a gate relaxation broader than safe path normalization (IR1-08). Actual paths-only normalization is unequal; mapping verified unchanged source lines makes all three lists equal across all three pairs. Thus no present change in exception-raising statements is observed, while the gate still permits one.

[A] EXPECTATIONS_E has 78 exact string keys with kinds {'MAY_DIFFER': 29, 'EQUAL': 38, 'ADDITION': 10, 'COUNT': 1}; capture multiplicities are explicitly declared as 8/1/1 in reasons and enforced by normalized-list equality against the pinned baseline. “Exact path” keys nevertheless stop dictionary recursion and can cover subtrees. Existing r4-2 tests retain equal ran/passed in delivered results; mandatory-count check and independent rerun comparison follow below. IR1-06/07 prevent closure of RP1A-03.


## Re-execution and environment (§3)


[A-S] Unchanged harness ran with F3_REPO_ROOT=G:\PycharmProjects\rp1r1_audit\rerun_9035df0_launch2, F3_RP1R1_LAUNCH=2, all three thread pins=1. Both executor custody records and their sidecars were moved outside p_konum_plus; store was absent at launch. Delivered metadata/code only was copied; the two real F1 manifests and all external real data were omitted. Writer exit=0; harness pid=18956, start=2026-10-09T17:44:35.459699+00:00, finish=2026-10-10T05:01:30.472076+00:00, exit=0. Copied executor outputs were excluded unless their process.pid equals the auditor pid. The writer hardcodes first launch=2: incorrect for auditor launch1 (IR1-18), coincidentally equal for launch2. No writer/harness edit was made.

| field | binding/executor | auditor | difference |
|---|---|---|---|

| platform | Windows-10-10.0.19045-SP0 | Windows-10-10.0.19045-SP0 | none |

| python | 3.11.7 | 3.11.7 | none |

| numpy | 1.26.4 | 1.26.4 | none |

| scipy | 1.14.1 | 1.14.1 | none |

| OMP | 1 | 1 | none |

| OPENBLAS | 1 | 1 | none |

| MKL | 1 | 1 | none |

[A-S] Auditor launch1 stopped early with observed exit1 at 2026-10-09T17:27:07.423485+00:00 after approximately44 minutes. Its parent runner did not record completion; the independent monitor observed the child exit. The logs contain no Python traceback or reported scientific STOP at that point; the termination cause is not established. The initial partial DRAFT r1 and SHA256 remain preserved; this report supersedes that partial audit output. Launch2 used a new disposable root and EMPTY store, preserving the original root, all original store units, logs, status and prior report. Both auditor harness invocations used the unchanged delivered source. Previous status/evidence: {
  "started": "2026-10-09T16:42:49.619384+00:00",
  "root": "G:\\PycharmProjects\\rp1r1_audit\\rerun_9035df0",
  "launch": 1,
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
  "writer_exit": 0,
  "harness_sha256": "cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb",
  "pid": 24476,
  "harness_started": "2026-10-09T16:42:50.215801+00:00",
  "state": "FINISHED",
  "exit_code": 1,
  "finished": "2026-10-09T17:27:07.423485+00:00",
  "exit_recorded_by": "independent process monitor; runner did not record completion"
}; evidence snapshot G:\PycharmProjects\rp1r1_audit\audit_history\auditor_launch1_early_exit. The second runner was launched independently with hidden Start-Process, rather than attached to a foreground tool session.


[A-S] Independent S comparison: 37 objects; differences=[]. RUN1=556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77; RUN2=556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77; determinism=True; residual=3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f. Mandatory tests: 38, failures=[]. Frozen-baseline gate: {
  "baseline": "p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json",
  "baseline_sha256": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
  "e_declared": 2114,
  "pass_": true,
  "s_findings": [],
  "telemetry_baseline": "p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv",
  "test_evidence_baseline": "p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json",
  "test_evidence_baseline_sha256": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf",
  "u_findings": []
}.

[A-S] Auditor versus executor NR CSV path/class comparison: rows [2115, 2115], row/class differences=[]. Values containing pid, paths and wall time differ by declared provenance and are retained in own outputs. S equality is required regardless of environment. No S STOP was observed.


## Non-regression and accounting (§4)


[A] Delivered CSV has 2115 rows (1 S, 2114 E), columns path/classification/reason/r4_2/rp1. There is no declaration ID or held field; kind/held were calculated internally and discarded. Equal declared fields are not printed. Results and test evidence use declared subtree stop points rather than every-leaf recursion. IR1-06/07 therefore apply despite reported s=0/u=0. Scientific comparison is independently reconstructed: all 37 evaluations and stop records match r4-2; canonical hash recomputes to 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77; residual bytes hash to 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f.

[A] Three stale end_state CSV values are a real ordering effect: T-NONREG-R4-2 has not yet been recorded when compared. Lines 5665 onward refresh tests_run, mandatory flags and completeness before writing results. Delivered final values are corrections_complete=true, mandatory_tests_all_run=true, mandatory_tests_missing=[]; the stale CSV values are not a final-results mismatch.

[A-S] Independent plan derivation used frozen generator/start-grid and feature admissibility helpers only; no optimizer or algorithm×CVI evaluator was called. Enumerated all expected family start keys including conditional feature rejection, rather than copying register counts. Exactly 49787 expected onestart keys match the 49787 manifest keys: zero missing/unexpected. This comprises base 2081 and handoff 47706. Handoff: 48 P-01 contexts×731 grid starts +48 features; 48 P-02 contexts×261 grid starts +42 features (6 duplicate feature rejections) =47706.

| scope/family | independently derived stored units | delivered manifest |
|---|---:|---:|
| base onestart | 2081 | 2081 |
| base splmode | (2×2×8 + 2×(2×8−2) +4)×146 =9344 | 9344 |
| realscen / nrgates_all / unittests_all | 4 /1 /1 | 4 /1 /1 |
| excpass1 /excpass2 splmode | 3×146 each=438 each | 438 /438 |
| handoff onestart /splmode | 47706 /6×8×146=7008 | 47706 /7008 |
| cold /warm splmode | 146 each | 146 /146 |
| total | 67313 | 67313 |

[A] Store-read plan: cold fit2+verification=2×146=292; warm fit1+fit2+verification=3×146=438; total730. Log agrees, all writer/reader pid34588, no other scope. Per-call delivered rows: 22217=21725 fresh+492 replay; replay=164 cold fit2 +164 warm fit1 +164 warm fit2. Five T-STORE fits (cold2,warm3) each have164 optimizer records: 328 fresh+492 replay. Per-mode primary/fallback cardinality is conditional; optimizer rows and stored units are not interchangeable. Global phases nr_gates9283, unit_tests1602, run1/run2 each5256, t_store_read_accounting820. Handoff’s actual SPL count is9223 and optimizer time1523.6454776009778s, correcting register’s8895.

[A]/[X] Executor replay-vs-payload equality is recorded by its tests but original payloads are not delivered; this audit does not pretend to read absent stores. [A-S] Auditor replay is compared to its actual stored bytes independently in the output appendix. Coarse replay source and real restart cold condition remain K defects even if the fresh rerun passes. The handoff phase error and key-family error are K, never T (IR1-11).

[A] Missing handoff family rows do not prevent deriving and matching the start-unit plan. They do prevent full optimizer-event/timing accounting on delivered bytes: 47706 starts can take primary/fallback routes whose telemetry is discarded from exported records. This blocks the package accounting pass condition (IR1-12). A real-data instruction needs persistent per-phase/sex/trajectory/family/context/start/optimizer-stage records, fresh/replay provenance, counts by key family, and measured phase boundaries. No new fit/threshold rule is proposed. [X] ~10h handoff, ~95% family cost, 9h44 standalone elapsed and per-trajectory1.5–1.8h lack delivered timestamp evidence; only SPL1523.645s and total primary start/end interval are traceable. The ~3.6day/~62day extrapolations are informational estimates, not a proved range for real trajectories.


## Item-by-item (§5)


| item | independent result |
|---|---|
| R-1 handoff | [A] consumer uses real_x and family-qualified IDs; derived keys match loader arrays and all144 dry contexts. Shared builder, real-mode missing-field STOP and byte-manifest gate remain deficient (IR1-02–04). |
| R-2 QC | [A] all21 delivered got/expected pairs agree; exact partial denominator21146 independently derived. Direct guard tests cover NaN/Inf, negative share, post-z nonfinite, std/norm; derivations recorded in register. Two constant ok cases remain (IR1-05). |
| R-3 full comparison | [A]/[A-S] scientific bytes match; equality bypass, subtree stopping, CSV declaration reporting and traceback normalization remain open (IR1-06–08). |
| R-4 isolation | [A-S] separate root/custody/store/output, unchanged source; own W-3 and dispatch checks passed; final execution comparison as §3. Writer first-launch field incorrect (IR1-18). |
| R-5 source/accounting | [A] source exists; cold/warm rows under own phase; fine replay records consistent. Cold resume and coarse replay source defects remain (IR1-09/10); actual own payload check in appendix. |
| R-6 records | [A] full key-field/register table, corrected realscen meaning, unit/call/read distinction, response rows and three sidecars delivered. Diff annotations and ledger wording need correction (IR1-16/17). |
| Start inventory | [A] previous inventory hash correct; all carried rows identify class/closure/status; executor marks none of this package’s audit-only items CLOSED. Later deferred sidecar item omitted (IR1-17). |
| Attempts/starts | [A] primary attempt1/launch1 pid34228 and attempt2/launch2 pid34588 supported by logs; precondition premature-copy event and deleted dry runs are [X]. Standalone pre-verification provenance missing (IR1-13). |
| Firewall | [A] REAL_DATA_MODE=False asserted at each logged main start; delivered opened audit excludes real manifests/raw paths. [A-S] auditor own opened audit checked in §3/appendix. No algorithm×CVI computation performed in audit scripts. |


F1 frozen operation mapping [A]: §8.1 steps1–2 → f1_load_raw_dir format/semantic/floor guards; step3 → national yob layout assumption (caller must supply national-only source, no independent state-file-content discriminator); step4 →1880–2025 annual axis; steps5–6 → full support and eligible filter; step7 → all-published-names denominator and _f1_share; step8 → duplicate/positive denominator/pre-z finite/nonnegative; step9 → zero-variance guard; step10 → mean/std ddof0 normalization; step11/§8.2 → f1_post_z_qc finite, mean,std,norm against1e-8. Freeze §7’s14-field manifest representation is not reproduced by f1_repro_gate. REAL_DATA_MODE guards this cycle; constants naming real manifests are never opened by the harness. Auditor’s separate hash-column read is expressly allowed by audit §0.


## Ledger closure (§6)


| item | auditor status | verified evidence / remaining reason |
|---|---|---|
| RP1A-01 | OPEN | handoff array intake verified, but IR1-02/03/04 leave required R-1 behavior missing |
| RP1A-02 | OPEN | 21 observed outcomes agree; constant ok violates R-2 (IR1-05) |
| RP1A-03 | OPEN | matching S does not establish the required full gate; IR1-06/07/08 |
| RP1A-04 | OPEN | fine source/read records verified; coarse replay/cold restart/attribution defects IR1-09/10/11 |
| RP1A-05 | OPEN | both informational lines delivered and scaling arithmetic independently checked; line 1 uses MINI_BANK despite the inherited full-bank description, and line 2 timing/family basis is not delivered (IR1-12/15); the claimed real-data interval is not established |
| RP1A-06 | OPEN | sidecars/response rows/diff content verified, but one-item-per-hunk labels not accurate (IR1-16) |

| RP1A-07 | CLOSED | unchanged full rerun completed with matching S and all mandatory tests; independent isolation/custody comparison; writer record defect IR1-18 remains a separate K |

| R42A-03 (b) | OPEN | independent fine read records and replay content checked; R-5 remains deficient on resumed cold test/coarse replay (IR1-09/10) |


New findings retain their own statuses below. The PI owns D-9 binding and A.5(iii) rule decision; neither is closed here. F1 input-table sidecar remains OPEN/T with closure at real-data step1, and no real-data sidecar was produced.


## Findings table


| id | v6 | D-11 §5 | status | file:line | evidence/reason | closure action |
|---|---|---|---|---|---|---|

| IR1-01 | gate-specific blocker | B | CLOSED (current-list byte correction only) | provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:37 | [A] Wrong report hash and false OBSERVED claim; [X] invention mechanism is executor disclosure. Current r1 has the correct named-file hash and sidecar. Historical B(iii) custody defect; correction independently verified. | Preserve superseded list; use corrected r1. This closes the mismatch, not the historical process claim. |

| IR1-02 | gate-specific blocker | B | OPEN | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:2118 | [A-S] Removing real_x or real_mask_ids from an F1 scenario produces TypeError, not F1ContractGap. Only four legacy fields are guarded; real-mode intake requirements are omitted. R-1(iii) remains unmet. | Require the real-mode fields and test their named F1ContractGap outcomes without changing the synthetic path. |

| IR1-03 | gate-specific blocker | B | OPEN | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:2142 | [A] mid() builds the ID at 2146 and f1_context_id_table builds it independently at 3001. Matching literals and a passing current set comparison do not supply the ONE builder required by R-1(ii). | Introduce one shared ID builder used by both consumers; independently verify the diff and unchanged S objects. |

| IR1-04 | gate-specific blocker | B | OPEN | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:2944 | [A] Reproduction gate compares sorted (sex,name) tuples, not the frozen 14-column eligible-manifest bytes. The changed-manifest test removes one tuple at 3326; it does not change one byte. No synthetic hash-table or eligible-manifest deliverable is exported. R-1(iv) and §7 remain unmet. | Implement the frozen manifest schema/serialization and byte comparison; deliver synthetic tables and generator with sidecars; test one-byte change and missing/extra/hash-change cases. |

| IR1-05 | gate-specific blocker | B | OPEN | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:3065 | [A] z_qc_pass and gate_pass retain literal ok=True at 3065/3072 inside the loader test changed by this package. R-2 explicitly covers all cases of this test. Delivered got=True does not make the assertion computed. | Set each ok from its observed got and expectation; verify every loader branch. The exact partial denominator now correctly compares 21146 to 21146. |

| IR1-06 | gate-specific blocker | B | OPEN | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:5463 | [A] Recursive flattening stops at declared dictionaries, including MAY_DIFFER counter maps and atomic test blocks. This is not every-leaf full depth. Capture counts 8/1/1 are declared in reasons and preserved by normalized list equality against the pinned baseline. CSV at 5638 drops kind, held, and a declaration ID. R-3 deliverable and gate requirements remain unmet. | Compare/report leaves with exact declarations and retain declaration ID/kind/held in every relevant CSV row including equal declared fields. |

| IR1-07 | gate-specific blocker | B | OPEN | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:5514 | [A-S] a_val==b_val continues before expectation evaluation. Wrong equal COUNT values and an ADDITION already present in both files both return zero U findings. B(iii): the required gate is not enforced. | Evaluate declared expectations even on equal values; traverse declarations absent from both documents; verify failure cases without changing the S comparison. |

| IR1-08 | cleanup | K | OPEN; before dependent computation | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:5446 | [A-S] A changed exception raise location is accepted after the whole traceback is removed. Actual delivered traces differ by path AND verified unchanged-line shifts; source-line mapping shows no present semantic stack change. The current comparator nevertheless hides future stack changes. | Normalize only verified path/source-coordinate changes and compare the remaining traceback; preserve frame/function/statement identity. |

| IR1-09 | cleanup | K | OPEN; before dependent computation | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:3544 | [A-S] The aggregate test requires cold.fit1_reads==0 although the helper allows a valid read from a prior process. Simulating both helpers passing with 146 resumed reads makes the aggregate fail. R-5 says first fit need not be fresh. | Remove the fresh-first assumption while preserving independently verified cold/warm coverage and replay-versus-stored checks. |

| IR1-10 | cleanup | K | OPEN; before dependent computation | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:4181 | [A] Coarse nrgates_all/unittests_all/realscen replay paths append saved rows without changing source to replay (also 4312,4407). Only fine splmode replay was repaired. A restart can therefore label stored optimizer rows fresh. | Apply replay provenance consistently to every cache restoration path and verify the three coarse paths. |

| IR1-11 | cleanup | K | OPEN; before dependent computation | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:4211 | [A] Handoff optimizer rows carry nr_gates rather than a handoff phase. _key_family at 235 omits f1handoff__, so code-produced family display is f1handoff instead of onestart/splmode. Both fixes change code-produced records and cannot be T under D-11 §5. | Use accurate phase and family attribution; independently check accounting and non-regression after the code correction. |

| IR1-12 | gate-specific blocker | B | OPEN | calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:3225 | [A] Handoff discards run_real_scenario returned family telemetry. Independent plan matches all 47706 handoff start-unit identities, but delivered bytes cannot reconcile their actual primary/fallback optimizer records or timing. §9(6) full computation accounting is not established. | Deliver phase/key-linked family telemetry, including start and optimizer-call counts, fallback events, fresh/replay identity, and section timing. Manifest-level count equality alone is insufficient for optimizer-level accounting. |

| IR1-13 | gate-specific blocker | B | OPEN | provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:85 | [A] A 9h44 standalone pre-verification is disclosed outside the two primary attempts. [X] Its executed code hash, launch/custody record, output paths, and evidence excluding its outputs from deliverables/attempt-2 store are not supplied. Audit §5.7 cannot be satisfied. No scientific difference or real-data access is inferred from this absence. | Supply the original code/custody/launch/output records and trace segregation. PI addresses the missing custody evidence; do not reconstruct or invent it. |

| IR1-14 | cleanup | T | OPEN | provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:125 | [X] Historical transport ZIP bytes and deleted dry-copy custody bytes are absent. The 108-occurrence self-scan has 106 independently traceable occurrences, one known historical mismatch, and one deleted custody value that remains unverified; 107 verified is not established. | Correct verification wording; provide originals if verification is required. Mark unavailable values X, never verified. |

| IR1-15 | cleanup | T | OPEN | calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:77 | [A] Register states 8895 handoff SPL rows; delivered per-call CSV has 9223 (all F3-REAL). Inventory states 11 upstream files while listing 12. Report says the external W-3 writer verified 31 preconditions; its INSTR list has 20 (the harness separately verifies 31). The estimate says 42k+ warning records; delivered stderr contains 33013 warning records (66026 lines), including 28 RuntimeWarnings. The older SCEN-A estimate describes full banks, but its family telemetry comes from MINI_BANK; this scope mismatch must be disclosed. | Correct the narrative counts from named bytes; do not edit the historical records in this audit. |

| IR1-16 | cleanup | T | OPEN | calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff:356 | [A] Both patches apply exactly to the delivered target, but labels are generated by keyword matches. Hunks 11–16 change family arguments to mid() and are falsely described as header/comment-only S5-WIRING; 19 changes ID construction (R-1), and 20 changes denominator comparison (R-2). The vs-r4-2 C-3 hunk includes R-1/R-2 changes. | Relabel the actual changes and split mixed-purpose hunks so each maps to one authorized item. Code scope itself is traceable; annotation repair is a record change. |

| IR1-17 | cleanup | T | OPEN | provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:90 | [A] First ledger omits the already-known deferred F1 input-table sidecar item. Record-only rows use OPEN→closes on delivery rather than the instruction’s pending-verification status. New code-produced display issue is later classified T. | Carry every item with class, closure point, and consistent status; use K for code-produced record corrections. Auditor closure remains item by item. |

| IR1-18 | cleanup | K | OPEN; procedure correction before reuse | calibration/_w3_writer_rp1-r1_tmp.py:52 | [A-S] Unchanged writer sets first launch number from ATTEMPT_NUMBER=2. Auditor procedure requests first auditor launch 1; own custody thus incorrectly says first launch=2 while actual launch=1. Harness accepts it because it checks hashes/fingerprint, not that declaration. | Have the external writer record the actual intended launch and verify it. This audit preserves the delivered writer and discloses its incorrect field. |

| IR1-19 | cleanup | T | OPEN | calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/SYNTH_FIXTURE_MANIFEST.json:2 | [A] 1021 added synthetic .txt files have neither individual sidecars nor per-file hashes in the manifest (filenames only). Their generator and actual disjointness are independently checked, but audit §1.1’s explicit reason for omitting each sidecar is absent. | State the package’s manifest-based custody exception explicitly or supply per-file hashes/sidecars. Preserve the delivered fixtures. |


B assignments are under D-11 §5(iii): a package defect leaves a named gate precondition unmet. K assignments concern code/record production and close before dependent computation. T assignments are documentary corrections with code/outputs otherwise preserved. IR1-01 is historically B, corrected on current delivered list bytes. No class is lowered from an executor/PI assignment by this report; code-produced records previously called T are raised to K.


## NOT PERFORMED


- [X] Original standalone pre-verification code/custody/launch/path/output-segregation verification: original records absent.
- [X] Deleted executor dry-copy custody hash and launches: bytes/logs absent.
- [X] Original/rebuilt transport ZIP verification: neither ZIP supplied.
- [X] Direct comparison of executor replay to executor pickle payloads: stores absent by delivery design; manifest/log checked as records.
- [X] Generator script executing at transmission-list write time and premature-copy creation/deletion history: only post-event narrative supplied.
- [X] Exact executor handoff/trajectory elapsed and95% family-cost attribution: timing/family telemetry absent.
- Real-data reproduction/eligible-manifest/raw reads and algorithm×CVI execution: prohibited/out of scope; not attempted.


## Scripts run and observed output


Commands used the existing Python3.11.7 interpreter. Scripts are outside the source repository. Pure-function AST probes are independent diagnostic executions; they are not edited-harness reruns. The sole full-harness invocation used the original delivered source hash. Initial probe invocation failed on the auditor script’s invalid encoding spelling utf8-sig, corrected to utf-8-sig before the successful probe; no harness edit or optimizer occurred in that failed probe. Intermediate audit-script extraction/counting errors were corrected before relying on their results.

Read-only setup commands: Get-FileHash/Get-Content on supplied instruction/sidecar; git status --porcelain, rev-parse, ls-tree, cat-file --batch, diff --name-status, and selected metadata/code reads. Derived outputs and scripts are embedded below, with raw-evidence file hashes for the larger files; no real raw file was read. Source final git status: ''


### Setup output
```json
{
  "commit": "9035df0831d8646cca7f1e73937161a3d2d7d018",
  "source_head": "d9a5e9905e25c634ad3132aae85c6c346e5ead30",
  "source_status": "",
  "time": "2026-10-09T16:42:26.314607+00:00",
  "environment": {
    "python": "3.11.7",
    "numpy": "1.26.4",
    "scipy": "1.14.1",
    "platform": "Windows-10-10.0.19045-SP0"
  },
  "copied_files": 2477,
  "excluded_unopened": [
    "p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv",
    "p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv"
  ]
}
```


### W-3 output
```text
W3_WRITTEN = p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md
attempt = 2 ; launch = env-driven (F3_RP1R1_LAUNCH; first launch of this attempt = 2) ; restart_layer = True
harness_sha256 = cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb
generator_sha256 = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 (reused)
manifest_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe (reused; regen equal)
code_env_fingerprint = 29de608948a06cf2
custody_sha256 = dc81a8cf1f900b5d091766cf9d31530420e243ec4fd8b0f7aa10f036f03f6be1

```


### Independent probes
```json
{
  "equal_wrong_COUNT_skipped": [
    [],
    []
  ],
  "missing_both_ADDITION_skipped": [
    [],
    []
  ],
  "equal_wrong_ADDITION_skipped": [
    [],
    []
  ],
  "traceback_location_change_accepted": [
    [
      {
        "path": "exc_captures",
        "classification": "E",
        "kind": "EQUAL(content)",
        "held": true,
        "reason": "a natural COVERED event's own provenance (pid/start_iso/traceback file path) differs per process; content verified identical after stripping those fields",
        "r4_2": "[{\"pid\": 1, \"start_iso\": \"a\", \"traceback\": \"raised at ORIGINAL site\", \"type\": \"RuntimeError\"}]",
        "rp1": "[{\"pid\": 2, \"start_iso\": \"b\", \"traceback\": \"raised at DIFFERENT site\", \"type\": \"RuntimeError\"}]"
      }
    ],
    []
  ],
  "bad_capture_count_accepted_when_both_2": [
    [],
    []
  ],
  "whole_subtree_stop_points": [
    "process.units_computed_this_process",
    "process.spline_telemetry_calls_by_phase",
    "key_namespace_table",
    "f1_loader_synth",
    "f1_handoff_synth",
    "a5"
  ],
  "declaration_count": 78,
  "declared_kind_counts": {
    "MAY_DIFFER": 29,
    "EQUAL": 38,
    "ADDITION": 10,
    "COUNT": 1
  },
  "traceback_source_line_mapping": [
    {
      "pair": "r4-2 -> attempt1",
      "key": "exc_captures",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "r4-2 -> attempt1",
      "key": "exc_captures_run2",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "r4-2 -> attempt1",
      "key": "exc_captures_unit_phase",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "attempt1 -> attempt2",
      "key": "exc_captures",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "attempt1 -> attempt2",
      "key": "exc_captures_run2",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "attempt1 -> attempt2",
      "key": "exc_captures_unit_phase",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "r4-2 -> attempt2",
      "key": "exc_captures",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "r4-2 -> attempt2",
      "key": "exc_captures_run2",
      "equal_after_verified_source_line_mapping": true
    },
    {
      "pair": "r4-2 -> attempt2",
      "key": "exc_captures_unit_phase",
      "equal_after_verified_source_line_mapping": true
    }
  ],
  "hash_disjoint": {
    "real_hash_column_entries": 217,
    "synthetic_files": 1023,
    "unique_synthetic_hashes": 298,
    "intersection_count": 0
  },
  "hash_occurrences_original8": 108,
  "hash_occurrences_bothlists_total": 148,
  "hash_occurrences_without_matching_file": [
    {
      "document": "provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md",
      "line": 9,
      "hash": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
      "matching_byte_paths": []
    },
    {
      "document": "provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md",
      "line": 37,
      "hash": "ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260",
      "matching_byte_paths": []
    },
    {
      "document": "calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md",
      "line": 25,
      "hash": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
      "matching_byte_paths": []
    },
    {
      "document": "provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md",
      "line": 95,
      "hash": "892076fc696e583feaff312e1b330ede888ff1fd149bd11139bc4591ba680f51",
      "matching_byte_paths": []
    },
    {
      "document": "provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md",
      "line": 14,
      "hash": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
      "matching_byte_paths": []
    },
    {
      "document": "provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md",
      "line": 33,
      "hash": "ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260",
      "matching_byte_paths": []
    },
    {
      "document": "provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md",
      "line": 125,
      "hash": "8b560d88ac36ce24a385e4d21975082acc3177bf005b730b962fe80ab99350c8",
      "matching_byte_paths": []
    }
  ],
  "recomputed_canonical_sha256": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
  "resumed_cold_helper_success_but_aggregate_fail": {
    "cold": {
      "pass_": true,
      "fit1_reads": 146
    },
    "warm": {
      "pass_": true,
      "fit1_reads": 146
    },
    "pass_": false
  },
  "loader_constant_ok_locations": [
    {
      "line": 3065,
      "value": true
    },
    {
      "line": 3072,
      "value": true
    }
  ]
}
```


### Derived plan
```json
{
  "grid_sizes": {
    "P-01": 731,
    "P-02": 261
  },
  "family_fit_context_counts": {
    "|FIX-P01-BENIGN|P-01": 1,
    "|FIX-P02-BENIGN|P-02": 1,
    "|UT-A5-II|P-01": 1,
    "|UT-A5-III|P-02": 1,
    "|UT-PROBE-DECOUPLE|P-01": 2,
    "|SCEN-A|P-01": 32,
    "|SCEN-A|P-02": 32,
    "|SCEN-B|P-01": 32,
    "|SCEN-B|P-02": 32,
    "|FIX-STARTS-FULL|P-01": 1,
    "|FIX-STARTS-FULL|P-02": 1,
    "|FIX-STARTS-DUP|P-02": 2,
    "|FIX-A5-TRUE|P-01": 4,
    "|FIX-A5-TRUE|P-02": 4,
    "f1handoff__|F3-REAL|P-01": 48,
    "f1handoff__|F3-REAL|P-02": 48
  },
  "conditional_feature_counts": {
    "|FIX-P01-BENIGN|P-01|accepted": 1,
    "|FIX-P02-BENIGN|P-02|accepted": 1,
    "|UT-A5-II|P-01|TEST_ONLY_INJECTION": 1,
    "|UT-A5-III|P-02|accepted": 1,
    "|UT-PROBE-DECOUPLE|P-01|accepted": 2,
    "|SCEN-A|P-01|accepted": 32,
    "|SCEN-A|P-02|accepted": 32,
    "|SCEN-B|P-01|accepted": 32,
    "|SCEN-B|P-02|accepted": 30,
    "|SCEN-B|P-02|TEST_ONLY_INJECTION": 2,
    "|FIX-STARTS-FULL|P-01|accepted": 1,
    "|FIX-STARTS-FULL|P-02|accepted": 1,
    "|FIX-STARTS-DUP|P-02|DUPLICATE": 2,
    "|FIX-A5-TRUE|P-01|accepted": 4,
    "|FIX-A5-TRUE|P-02|accepted": 4,
    "f1handoff__|F3-REAL|P-01|accepted": 48,
    "f1handoff__|F3-REAL|P-02|DUPLICATE": 6,
    "f1handoff__|F3-REAL|P-02|accepted": 42
  },
  "expected_onestart_units": 49787,
  "observed_onestart_units": 49787,
  "missing_keys": [],
  "unexpected_keys": [],
  "expected_spline_units": {
    "base": 9344,
    "excpass1": 438,
    "excpass2": 438,
    "f1handoff": 7008,
    "cold": 146,
    "warm": 146
  },
  "expected_coarse_units": {
    "realscen": 4,
    "nrgates_all": 1,
    "unittests_all": 1
  },
  "partial_denominator": 21146,
  "dry_context_rows": 144,
  "real_mode_contract_gap_probes": [
    {
      "removed": "real_x",
      "exception": "TypeError",
      "message": "SeedSequence expects int or sequence of ints for entropy not F_Zq00",
      "required_F1ContractGap": false
    },
    {
      "removed": "real_mask_ids",
      "exception": "TypeError",
      "message": "'NoneType' object is not subscriptable",
      "required_F1ContractGap": false
    }
  ]
}
```


### Additional documentary checks
```json
{
  "delivered_stderr": {
    "path": "calibration\\f3_step2_rp1-r1_launch2_stderr_2026-10-05.log",
    "sha256": "afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b",
    "lines": 66026,
    "warning_records": 33013,
    "warning_types": {
      "UserWarning": 32985,
      "RuntimeWarning": 28
    }
  },
  "rp1_SCEN_A_cost": [
    {
      "sex": "F0",
      "family_rows": 64,
      "starts_by_family": {
        "P-01": [
          "feature",
          "grid[0]",
          "grid[365]",
          "grid[730]"
        ],
        "P-02": [
          "feature",
          "grid[0]",
          "grid[130]",
          "grid[260]"
        ]
      },
      "family_seconds": 44.1551831997931,
      "spline_rows": 1409,
      "spline_seconds": 304.19523109926376,
      "total_seconds": 348.35041429905687
    },
    {
      "sex": "M0",
      "family_rows": 64,
      "starts_by_family": {
        "P-01": [
          "feature",
          "grid[0]",
          "grid[365]",
          "grid[730]"
        ],
        "P-02": [
          "feature",
          "grid[0]",
          "grid[130]",
          "grid[260]"
        ]
      },
      "family_seconds": 41.26255800022045,
      "spline_rows": 1371,
      "spline_seconds": 290.11038210080005,
      "total_seconds": 331.3729401010205
    }
  ],
  "sex_split_scaled_seconds": 307609.0850076704,
  "sex_split_scaled_hours": 85.44696805768622,
  "sex_split_scaled_days": 3.560290335736926,
  "new_scaling_from_asserted_1_65h": {
    "hours": 1494.8999999999999,
    "days": 62.287499999999994,
    "measurement_basis": "X: per-trajectory section timestamps are not delivered"
  },
  "capture_count_probe_limitation": "Both-files-have-2 probe is hypothetical; the real frozen baseline has 1/1/8 captures. Normalized-list equality preserves this cardinality. It is not evidence of a count defect against that pinned baseline."
}
```


### Custody sidecar segregation
```json
{
  "time": "2026-10-09T17:14:14.472509+00:00",
  "moved": [
    {
      "source": "G:\\PycharmProjects\\rp1r1_audit\\rerun_9035df0\\p_konum_plus\\provenance\\f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md.sha256",
      "kept_aside": "G:\\PycharmProjects\\rp1r1_audit\\kept_aside\\f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md.sha256",
      "sha256": "26c8ae0f06ee0ab32b1833af6a3c10e01ddda0892f19e3920f3f333457e94ae5"
    },
    {
      "source": "G:\\PycharmProjects\\rp1r1_audit\\rerun_9035df0\\p_konum_plus\\provenance\\f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md.sha256",
      "kept_aside": "G:\\PycharmProjects\\rp1r1_audit\\kept_aside\\f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md.sha256",
      "sha256": "bc00b9226a1a5cbb2892d22b6ed66c431c33951758a067b1d602bd0f0773d37e"
    }
  ],
  "own_custody_sha256": "3d42995fd45589d4b03b2752f6d78abe7b18ce5670e573368463322460f1e87c",
  "own_sidecar": "G:\\PycharmProjects\\rp1r1_audit\\audit_evidence\\auditor_w3.sha256"
}
```


### Static checks output
```text
{
  "parent_diff": {
    "files": 1104,
    "only_additions_under_p": true,
    "final_commit_diff": "A\tp_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md\nA\tp_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md.sha256\nA\tp_konum_plus/provenance/pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md\nA\tp_konum_plus/provenance/pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md.sha256\n"
  },
  "new_sidecars": {
    "count": 38,
    "failures": []
  },
  "added_without_sidecars": [
    "p_konum_plus/calibration/_w3_writer_rp1-r1_tmp.py",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_residual_series_rp1-r1_2026-10-05.json",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_rp1-r1_nonregression_vs_r4-1_2026-10-05.csv",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_rp1-r1_nonregression_vs_r4_2026-10-05.csv",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_rp1-r1_store_read_log_2026-10-05.csv",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_telemetry_rp1-r1_2026-10-05.csv",
    "p_konum_plus/quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_test_evidence_rp1-r1_2026-10-05.json"
  ],
  "lists": {
    "provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md": {
      "checked": 33,
      "failures": [
        {
          "line": 37,
          "target": "p_konum_plus/provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md",
          "pin": "ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260",
          "observed": "ebc28df8a94bd3b2249389caba08c35e8071afd0a7766f48f984c78a2d78ec40",
          "equal": false
        }
      ]
    },
    "provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md": {
      "checked": 33,
      "failures": []
    },
    "provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md": {
      "checked": 43,
      "failures": []
    },
    "provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md": {
      "checked": 29,
      "failures": []
    }
  },
  "list_table_diff": [
    "--- ",
    "+++ ",
    "@@ -10,7 +10,7 @@",
    " | 7  residual (byte-identical to r4-2/r4-1/r4/r3) | calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |",
    " | 8  test evidence | calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json | 97f75c83e4057f4d31b4310602124b536a2badd6c04555ee24d87ec2872ea0f9 |",
    " | 9  register (child of dbf25669\u2026; RP1A-04 table) | calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md | 4d5de5a776e7cd4a336b0dfc5f50aae378bdf6c3a780ff887a2a414389a5fe63 |",
    "-| 10 correction report | provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md | ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260 |",
    "+| 10 correction report | provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md | ebc28df8a94bd3b2249389caba08c35e8071afd0a7766f48f984c78a2d78ec40 |",
    " | 11 start-state inventory (incl. FIRST ledger, D-11 r1 \u00a77) | provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md | dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286 |",
    " | 12 attempt log (incl. \u00a70 disclosure, dry-check record) | provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md | ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b |",
    " | A  per-call telemetry (22,217 rows + header; `source` column, R-5) | calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv | d9d1c2564c9a24cddf55f31f662f09a40d453308536d5fcbbfa0dcfdfe1f000a |",
    "@@ -25,7 +25,7 @@",
    " | G2 labelled diff vs r4-2 (36 hunks; C-/R-/wiring labels) | calibration/f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff | c4cb5fae14545e7e66b52b0b93e05eddc153ff7a9e9f7b974c95836df97124a0 |",
    " | P  auditor re-run procedure (R-4; \u00a74 = the executor dry check as performed) | provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md | f7b5baf11f89d8aec68e81e48b0f4ab9fb1998576376ca5cf023c87f8556a8b4 |",
    " | H  \u00a77 estimate, two labelled lines (RP1A-05) | provenance/f3_realdata_prep_rp1-r1_size_estimate_2026-10-05.md | 97c2684cb3216f3b0bb6f6b7edae5436aaffa5a1935fb27efc0a5b8b1dc86875 |",
    "-| T  this list | provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md | (its sidecar) |",
    "+| T  this list (r1) | provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md | (its sidecar) |",
    " | item | file (p_konum_plus/) | sha256 |",
    " |---|---|---|",
    " | launch 1 stdout (quarantined) | quarantine/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log | f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7 |"
  ],
  "diffs": {
    "rp1": {
      "equal_hunks": true,
      "hunks": 36,
      "labels": [
        "#HUNK 1 LABEL R-4 (keywords:1)",
        "#HUNK 2 LABEL S5-WIRING (keywords:28)",
        "#HUNK 3 LABEL R-1 (keywords:3)",
        "#HUNK 4 LABEL S5-WIRING (keywords:48)",
        "#HUNK 5 LABEL S9-WIRING (keywords:15)",
        "#HUNK 6 LABEL R-5 (keywords:1)",
        "#HUNK 7 LABEL R-1 (keywords:3)",
        "#HUNK 8 LABEL R-5 (keywords:1)",
        "#HUNK 9 LABEL R-1 (keywords:20)",
        "#HUNK 10 LABEL R-1 (keywords:5)",
        "#HUNK 11 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 12 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 13 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 14 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 15 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 16 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 17 LABEL R-1 (keywords:6)",
        "#HUNK 18 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 19 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 20 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 21 LABEL R-2 (keywords:4)",
        "#HUNK 22 LABEL R-2 (keywords:35)",
        "#HUNK 23 LABEL R-1 (keywords:22)",
        "#HUNK 24 LABEL R-5 (keywords:25)",
        "#HUNK 25 LABEL S5-WIRING (keywords:3)",
        "#HUNK 26 LABEL S9-WIRING (keywords:20)",
        "#HUNK 27 LABEL R-1 (keywords:14)",
        "#HUNK 28 LABEL R-5 (keywords:1)",
        "#HUNK 29 LABEL S9-WIRING (keywords:17)",
        "#HUNK 30 LABEL S9-WIRING (keywords:9)",
        "#HUNK 31 LABEL S9-WIRING (keywords:15)",
        "#HUNK 32 LABEL R-3 (keywords:39)",
        "#HUNK 33 LABEL R-3 (keywords:20)",
        "#HUNK 34 LABEL R-3 (keywords:14)",
        "#HUNK 35 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 36 LABEL S5-WIRING (keywords:4)"
      ]
    },
    "r4-2": {
      "equal_hunks": true,
      "hunks": 36,
      "labels": [
        "#HUNK 1 LABEL R-4 (keywords:1)",
        "#HUNK 2 LABEL S5-WIRING (keywords:19)",
        "#HUNK 3 LABEL C-2 (keywords:11)",
        "#HUNK 4 LABEL C-2 (keywords:7)",
        "#HUNK 5 LABEL C-2 (keywords:1)",
        "#HUNK 6 LABEL R-1 (keywords:3)",
        "#HUNK 7 LABEL S5-WIRING (keywords:48)",
        "#HUNK 8 LABEL S9-WIRING (keywords:20)",
        "#HUNK 9 LABEL C-6 (keywords:2)",
        "#HUNK 10 LABEL R-5 (keywords:1)",
        "#HUNK 11 LABEL R-1 (keywords:3)",
        "#HUNK 12 LABEL C-5 (keywords:3)",
        "#HUNK 13 LABEL C-5 (keywords:3)",
        "#HUNK 14 LABEL C-5 (keywords:3)",
        "#HUNK 15 LABEL R-5 (keywords:1)",
        "#HUNK 16 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 17 LABEL C-5 (keywords:5)",
        "#HUNK 18 LABEL R-1 (keywords:20)",
        "#HUNK 19 LABEL R-1 (keywords:5)",
        "#HUNK 20 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 21 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 22 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 23 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 24 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 25 LABEL S5-WIRING (no keyword match; header/comment-only wiring)",
        "#HUNK 26 LABEL C-3 (keywords:64)",
        "#HUNK 27 LABEL C-2 (keywords:14)",
        "#HUNK 28 LABEL C-3 (keywords:4)",
        "#HUNK 29 LABEL S9-WIRING (keywords:23)",
        "#HUNK 30 LABEL R-1 (keywords:13)",
        "#HUNK 31 LABEL R-5 (keywords:1)",
        "#HUNK 32 LABEL C-1 (keywords:13)",
        "#HUNK 33 LABEL S9-WIRING (keywords:10)",
        "#HUNK 34 LABEL S9-WIRING (keywords:7)",
        "#HUNK 35 LABEL C-6 (keywords:4)",
        "#HUNK 36 LABEL R-3 (keywords:71)"
      ]
    }
  },
  "scientific_delivered": {
    "evaluation_count": 37,
    "evaluations_equal": true,
    "stops_equal": true,
    "canonical": {
      "run1_canonical_sha256": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
      "run2_canonical_sha256": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
      "determinism": true
    },
    "residual_hash": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f"
  },
  "nr_csv": {
    "rows": 2115,
    "fields": [
      "path",
      "classification",
      "reason",
      "r4_2",
      "rp1"
    ],
    "classes": {
      "S": 1,
      "E": 2114
    },
    "end_state_rows": [
      {
        "path": "end_state.PI_dispatch_record_hash",
        "classification": "E",
        "reason": "rp1-r1's own dispatch record is D-12, not D-7",
        "r4_2": "\"a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb\"",
        "rp1": "\"2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364\""
      },
      {
        "path": "end_state.PI_dispatch_record_path",
        "classification": "E",
        "reason": "rp1-r1's own dispatch record path",
        "r4_2": "\"p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md\"",
        "rp1": "\"p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md\""
      },
      {
        "path": "end_state.corrections_complete",
        "classification": "E",
        "reason": "stale at comparison time -- T-NONREG-R4-2 (this check) is not yet recorded in TESTS_RUN; refreshed immediately after, before the results file is written",
        "r4_2": "true",
        "rp1": "false"
      },
      {
        "path": "end_state.mandatory_tests_all_run",
        "classification": "E",
        "reason": "stale at comparison time, same reason",
        "r4_2": "true",
        "rp1": "false"
      },
      {
        "path": "end_state.mandatory_tests_missing",
        "classification": "E",
        "reason": "stale at comparison time, same reason",
        "r4_2": "[]",
        "rp1": "[\"T-NONREG-R4-2\"]"
      },
      {
        "path": "end_state.narrowed_evidence",
        "classification": "E",
        "reason": "rp1 instruction C-6, carried into rp1-r1: T-RP-1 enters narrowed_evidence by value",
        "r4_2": "[\"T-R2-2\"]",
        "rp1": "[\"T-R2-2\", \"T-RP-1\"]"
      }
    ]
  },
  "synthetic_fixture_count": 1021
}
Detailed evidence: audit_evidence/static_checks.json

```


### Final rerun comparison
```json
{
  "exit_code": 0,
  "harness_unchanged": true,
  "s_differences": [],
  "mandatory_failures": [],
  "environment": {
    "MKL": "1",
    "OMP": "1",
    "OPENBLAS": "1",
    "numpy": "1.26.4",
    "platform": "Windows-10-10.0.19045-SP0",
    "python": "3.11.7",
    "scipy": "1.14.1"
  },
  "process": {
    "attempt_log_path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md",
    "attempt_number": 2,
    "command_line": "G:\\PycharmProjects\\rp1r1_audit\\rerun_9035df0_launch2\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r1_2026-10-05.py",
    "end": "2026-10-10T08:01:27.888460",
    "executor_models": "claude-opus-4-8[1m]; see r4-1 report",
    "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    "launch_number": 2,
    "launch_stderr_path": "p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log",
    "launch_stdout_path": "p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log",
    "percall_telemetry_path": "p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv",
    "pid": 18956,
    "restart_layer_active": true,
    "spline_telemetry_call_total": 22217,
    "spline_telemetry_calls_by_phase": {
      "nr_gates": 9283,
      "run1": 5256,
      "run2": 5256,
      "t_store_read_accounting": 820,
      "unit_tests": 1602
    },
    "spline_telemetry_calls_by_phase_pid": {
      "nr_gates/18956": 9283,
      "run1/18956": 5256,
      "run2/18956": 5256,
      "t_store_read_accounting/18956": 820,
      "unit_tests/18956": 1602
    },
    "start": "2026-10-09T20:44:35.915481",
    "store_manifest_path": "p_konum_plus/calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv",
    "store_manifest_sha256": "583c75d9b54e9a0b6f92746141e5835bb5dc8f27cba84ed1e3bb1b90cf11e775",
    "store_rows": 67313,
    "supersedes_harness_sha256": "4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d",
    "supersedes_note_path": "p_konum_plus/quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md",
    "units_computed_this_process": {
      "nr_gates": 1,
      "residual_export": 1,
      "run1": 2,
      "run2": 2,
      "unit_tests": 1
    },
    "units_read_from_store": {
      "nr_gates": 0,
      "residual_export": 0,
      "run1": 0,
      "run2": 0,
      "unit_tests": 0
    }
  },
  "evaluation_counts": [
    37,
    37
  ],
  "residual_sha256": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f",
  "mandatory_count": 38,
  "tests_run": {
    "FIX-A5-TRUE": {
      "passed": true,
      "ran": true
    },
    "NR-01i": {
      "passed": true,
      "ran": true
    },
    "NR-01ii": {
      "passed": true,
      "ran": true
    },
    "NR-SPL": {
      "passed": true,
      "ran": true
    },
    "PIN-ACF": {
      "passed": true,
      "ran": true
    },
    "PIN-FEATURE-START-MASKED": {
      "passed": true,
      "ran": true
    },
    "PIN-MASKED-OBJECTIVE": {
      "passed": true,
      "ran": true
    },
    "T-A5-SUPPORT": {
      "passed": true,
      "ran": true
    },
    "T-CALLCOUNT": {
      "passed": true,
      "ran": true
    },
    "T-CANON": {
      "passed": true,
      "ran": true
    },
    "T-COMPARATOR-NAN": {
      "passed": true,
      "ran": true
    },
    "T-CONTEXT-ID-UNIQUE": {
      "passed": true,
      "ran": true
    },
    "T-EXC-CAPTURE-S1": {
      "passed": true,
      "ran": true
    },
    "T-EXC-CAPTURE-S2": {
      "passed": true,
      "ran": true
    },
    "T-EXC-UNRELATED-TYPE": {
      "passed": true,
      "ran": true
    },
    "T-EXPECT-ALL": {
      "passed": true,
      "ran": true
    },
    "T-F1-CONTRACT-GAP": {
      "passed": true,
      "ran": true
    },
    "T-F1-HANDOFF-SYNTH": {
      "passed": true,
      "ran": true
    },
    "T-F1-LOADER-SYNTH": {
      "passed": true,
      "ran": true
    },
    "T-F1-REPRO-GATE-SYNTH": {
      "passed": true,
      "ran": true
    },
    "T-INADMISSIBLE-OBSERVABLE": {
      "passed": true,
      "ran": true
    },
    "T-KEY-NAMESPACE": {
      "passed": true,
      "ran": true
    },
    "T-LOADER-NODES": {
      "passed": true,
      "ran": true
    },
    "T-MASK-FULL-EXT": {
      "passed": true,
      "ran": true
    },
    "T-NONREG-R4": {
      "passed": true,
      "ran": true
    },
    "T-NONREG-R4-1": {
      "passed": true,
      "ran": true
    },
    "T-NONREG-R4-2": {
      "passed": true,
      "ran": true
    },
    "T-RESIDUAL-LINK": {
      "passed": true,
      "ran": true
    },
    "T-SCHEMA": {
      "passed": true,
      "ran": true
    },
    "T-SPL-PENDING-REALPATH": {
      "passed": true,
      "ran": true
    },
    "T-STARTS-DEFAULT": {
      "passed": true,
      "ran": true
    },
    "T-STARTS-DUP": {
      "passed": true,
      "ran": true
    },
    "T-STORE-READ-ACCOUNTING": {
      "passed": true,
      "ran": true
    },
    "T-WRAPPER-RESTORE": {
      "passed": true,
      "ran": true
    },
    "UT-A5-II": {
      "passed": true,
      "ran": true
    },
    "UT-A5-III": {
      "passed": true,
      "ran": true
    },
    "UT-EXC-UNRELATED-REFERENCE": {
      "passed": true,
      "ran": true
    },
    "UT-PROBE-DECOUPLE": {
      "passed": true,
      "ran": true
    },
    "UT-USET-CONSTRUCTION": {
      "passed": true,
      "ran": true
    }
  },
  "nonregression": {
    "baseline": "p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json",
    "baseline_sha256": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
    "e_declared": 2114,
    "pass_": true,
    "s_findings": [],
    "telemetry_baseline": "p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv",
    "test_evidence_baseline": "p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json",
    "test_evidence_baseline_sha256": "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf",
    "u_findings": []
  },
  "recomputed_canonical_sha256": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77",
  "opened_forbidden": [],
  "own_store": {
    "units": 67313,
    "manifest_byte_failures": [],
    "pids": [
      "18956"
    ],
    "percall_rows": 22217,
    "sources": {
      "fresh": 21725,
      "replay": 492
    },
    "read_rows": 730,
    "replay_matches_actual_stored_records": true,
    "replay_scope_checks": {
      "cold": {
        "stored_call_rows": 164,
        "global_contains_at_least_declared_copies": true
      },
      "warm": {
        "stored_call_rows": 164,
        "global_contains_at_least_declared_copies": true
      }
    },
    "handoff_family_optimizer_rows_recovered_from_own_store": 47706,
    "handoff_family_wall_seconds": 34911.5292614795,
    "handoff_family_stage_counts": {
      "primary": 47706
    },
    "missing_planned_keys": [],
    "unexpected_keys": []
  },
  "accounting_failures": [],
  "nonreg_csv_row_or_class_differences": [],
  "nonreg_csv_rows": [
    2115,
    2115
  ],
  "source_repository_status": ""
}
```


### All hash occurrence traces

| document:line | full SHA256 | independently traced target/result |
|---|---|---|

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:9 | 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 | [A-S] recomputed canonical document |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:27 | cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:28 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | [A] p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:29 | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | [A] p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:30 | 162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:31 | dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:32 | 29e3e4101c479c1354ae212dabb10597ecfac889436d8f113d8661f298be6435 | [A] p_konum_plus/calibration/f3_step2_telemetry_rp1-r1_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:33 | e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb | [A] p_konum_plus/calibration/f3_step2_results_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:34 | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | [A] p_konum_plus/calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:35 | 97f75c83e4057f4d31b4310602124b536a2badd6c04555ee24d87ec2872ea0f9 | [A] p_konum_plus/calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:36 | 4d5de5a776e7cd4a336b0dfc5f50aae378bdf6c3a780ff887a2a414389a5fe63 | [A] p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:37 | ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260 | [A] historical wrong hash |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:38 | dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:39 | ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:40 | d9d1c2564c9a24cddf55f31f662f09a40d453308536d5fcbbfa0dcfdfe1f000a | [A] p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:41 | f64e0aa9344f7b2187d91a113cdc83c0f006bfd288fef8f86060ce9ab3f39da5 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:42 | 92b3af34f8c63347f839a7c0f1826e1bb566072cb25d40da17ad3bbd55939d7d | [A] p_konum_plus/calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:44 | 4fb207b79432a326fc436287e56fd237573bf2aed594d4b7a166f4c53fbebb98 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:45 | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-1_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:46 | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:47 | f08d7167e034da39fcb218db0f8864976ab83672eef96b1910eb95bfed78c7d2 | [A] p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/SYNTH_FIXTURE_MANIFEST.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:48 | ce7624ea27653c8e3d2efaa83b5c177d14c238a4a707d13b3837be69a4d89227 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:49 | c4cb5fae14545e7e66b52b0b93e05eddc153ff7a9e9f7b974c95836df97124a0 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:50 | f7b5baf11f89d8aec68e81e48b0f4ab9fb1998576376ca5cf023c87f8556a8b4 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:51 | 97c2684cb3216f3b0bb6f6b7edae5436aaffa5a1935fb27efc0a5b8b1dc86875 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_size_estimate_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:58 | f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7 | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:59 | fdf8c410faa5ff104eb1519e4a831b113000490ed51ae980550ecff2181308ff | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stderr_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:60 | d26b2898c580aae762af8a824851e9ea5c1e9cd8bd9c72424052d58ec83c6630 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:61 | afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:62 | 7772e17d4c775f14b0d67a90911876e06c8e99f2aca2d415dcf0b6d07d27e3fd | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:63 | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d | [A] p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:73 | 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 | [A] p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:74 | b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d | [A] p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:75 | 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0 | [A] p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:144 | cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:145 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | [A] p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:146 | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | [A] p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:147 | 162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:148 | dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:149 | 29e3e4101c479c1354ae212dabb10597ecfac889436d8f113d8661f298be6435 | [A] p_konum_plus/calibration/f3_step2_telemetry_rp1-r1_2026-10-05.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:150 | e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb | [A] p_konum_plus/calibration/f3_step2_results_rp1-r1_2026-10-05.json |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:151 | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | [A] p_konum_plus/calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:152 | 97f75c83e4057f4d31b4310602124b536a2badd6c04555ee24d87ec2872ea0f9 | [A] p_konum_plus/calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:153 | 4d5de5a776e7cd4a336b0dfc5f50aae378bdf6c3a780ff887a2a414389a5fe63 | [A] p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:154 | dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:155 | ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:156 | d9d1c2564c9a24cddf55f31f662f09a40d453308536d5fcbbfa0dcfdfe1f000a | [A] p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:157 | f64e0aa9344f7b2187d91a113cdc83c0f006bfd288fef8f86060ce9ab3f39da5 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:158 | 92b3af34f8c63347f839a7c0f1826e1bb566072cb25d40da17ad3bbd55939d7d | [A] p_konum_plus/calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:159 | 4fb207b79432a326fc436287e56fd237573bf2aed594d4b7a166f4c53fbebb98 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:160 | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-1_2026-10-05.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:161 | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4_2026-10-05.csv |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:162 | d26b2898c580aae762af8a824851e9ea5c1e9cd8bd9c72424052d58ec83c6630 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:163 | afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:164 | f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7 | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:165 | fdf8c410faa5ff104eb1519e4a831b113000490ed51ae980550ecff2181308ff | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stderr_2026-10-05.log |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:166 | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d | [A] p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:167 | 7772e17d4c775f14b0d67a90911876e06c8e99f2aca2d415dcf0b6d07d27e3fd | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:168 | f08d7167e034da39fcb218db0f8864976ab83672eef96b1910eb95bfed78c7d2 | [A] p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/SYNTH_FIXTURE_MANIFEST.json |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:169 | ce7624ea27653c8e3d2efaa83b5c177d14c238a4a707d13b3837be69a4d89227 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:170 | c4cb5fae14545e7e66b52b0b93e05eddc153ff7a9e9f7b974c95836df97124a0 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:171 | f7b5baf11f89d8aec68e81e48b0f4ab9fb1998576376ca5cf023c87f8556a8b4 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md |

| provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md:172 | 97c2684cb3216f3b0bb6f6b7edae5436aaffa5a1935fb27efc0a5b8b1dc86875 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_size_estimate_2026-10-05.md |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:8 | dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066 | [A] p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1_2026-10-04.md |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:11 | cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:14 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | [A] p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:16 | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | [A] p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:18 | 2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364 | [A] p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:19 | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 | [A] p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:25 | 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 | [A-S] recomputed canonical document |

| calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:26 | e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb | [A] p_konum_plus/calibration/f3_step2_results_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:19 | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:34 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | [A] p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:35 | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | [A] p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:40 | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d | [A] p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:43 | dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:48 | f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7 | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:48 | fdf8c410faa5ff104eb1519e4a831b113000490ed51ae980550ecff2181308ff | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stderr_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:54 | cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:57 | 162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:63 | d26b2898c580aae762af8a824851e9ea5c1e9cd8bd9c72424052d58ec83c6630 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:63 | afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:63 | e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb | [A] p_konum_plus/calibration/f3_step2_results_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:95 | 892076fc696e583feaff312e1b330ede888ff1fd149bd11139bc4591ba680f51 | [X] unavailable custody/ZIP bytes |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:19 | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:32 | 2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364 | [A] p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:36 | 2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d | [A] p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:38 | 0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639 | [A] p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:39 | 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 | [A] p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:40 | 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34 | [A] p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:41 | a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5 | [A] p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:42 | 2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989 | [A] p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:45 | aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef | [A] p_konum_plus/prompts/RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:48 | 858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:51 | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:53 | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | [A] p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:54 | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d | [A] p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:55 | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | [A] p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:70 | 0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639 | [A] p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:71 | 2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364 | [A] p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:72 | 2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d | [A] p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:73 | 2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989 | [A] p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:74 | aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef | [A] p_konum_plus/prompts/RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:111 | a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d | [A] p_konum_plus/provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md |

| quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md:15 | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d | [A] p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py |

| quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md:101 | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d | [A] p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py |

| quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md:114 | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d | [A] p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py |

| quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md:115 | dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:5 | 99c5d103640540de5a012d9000b425ccbbdbf02bd081c44c93c6f1102231d59b | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:14 | 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 | [A-S] recomputed canonical document |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:31 | 99c5d103640540de5a012d9000b425ccbbdbf02bd081c44c93c6f1102231d59b | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:33 | ebc28df8a94bd3b2cfe25da5f23c66ea0c06cdf90c33317c82a1a3a4a4035260 | [A] historical wrong hash |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:34 | ebc28df8a94bd3b2249389caba08c35e8071afd0a7766f48f984c78a2d78ec40 | [A] p_konum_plus/provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:42 | c446395e497bb42baa179d9c756c8b2664ea92ebbe6f80b064c5bb8ba6d63444 | [A] p_konum_plus/provenance/pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:51 | cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb | [A] p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:52 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | [A] p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:53 | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | [A] p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:54 | 162dea604bf573e4a80470724824f1c98dc224e535e26cfde54ffc57d096f2ca | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:55 | dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d | [A] p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:56 | 29e3e4101c479c1354ae212dabb10597ecfac889436d8f113d8661f298be6435 | [A] p_konum_plus/calibration/f3_step2_telemetry_rp1-r1_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:57 | e5ea4f07b5bae9fe176720434512a62a69fb3350b4ee8921c2718042f38960cb | [A] p_konum_plus/calibration/f3_step2_results_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:58 | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | [A] p_konum_plus/calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:59 | 97f75c83e4057f4d31b4310602124b536a2badd6c04555ee24d87ec2872ea0f9 | [A] p_konum_plus/calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:60 | 4d5de5a776e7cd4a336b0dfc5f50aae378bdf6c3a780ff887a2a414389a5fe63 | [A] p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:61 | ebc28df8a94bd3b2249389caba08c35e8071afd0a7766f48f984c78a2d78ec40 | [A] p_konum_plus/provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:62 | dd18ce3d84d1119850054ede4a8d62753d1d57cf1f91f813bef1d6e430e47286 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:63 | ba465fc56fa2bcf0e97db9ddaa1fcdee32518e692a4f2fb6be6022a54a75624b | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:64 | d9d1c2564c9a24cddf55f31f662f09a40d453308536d5fcbbfa0dcfdfe1f000a | [A] p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:65 | f64e0aa9344f7b2187d91a113cdc83c0f006bfd288fef8f86060ce9ab3f39da5 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:66 | 92b3af34f8c63347f839a7c0f1826e1bb566072cb25d40da17ad3bbd55939d7d | [A] p_konum_plus/calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:68 | 4fb207b79432a326fc436287e56fd237573bf2aed594d4b7a166f4c53fbebb98 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:69 | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-1_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:70 | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | [A] p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4_2026-10-05.csv |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:71 | f08d7167e034da39fcb218db0f8864976ab83672eef96b1910eb95bfed78c7d2 | [A] p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/SYNTH_FIXTURE_MANIFEST.json |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:72 | ce7624ea27653c8e3d2efaa83b5c177d14c238a4a707d13b3837be69a4d89227 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:73 | c4cb5fae14545e7e66b52b0b93e05eddc153ff7a9e9f7b974c95836df97124a0 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_harness_diff_vs_r4-2_2026-10-05.diff |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:74 | f7b5baf11f89d8aec68e81e48b0f4ab9fb1998576376ca5cf023c87f8556a8b4 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:75 | 97c2684cb3216f3b0bb6f6b7edae5436aaffa5a1935fb27efc0a5b8b1dc86875 | [A] p_konum_plus/provenance/f3_realdata_prep_rp1-r1_size_estimate_2026-10-05.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:82 | f3079d5e998dc4cf52058bc44d428b1d573b34ad7af6aa30a88a78cb2b1af2a7 | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stdout_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:83 | fdf8c410faa5ff104eb1519e4a831b113000490ed51ae980550ecff2181308ff | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_launch1_stderr_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:84 | d26b2898c580aae762af8a824851e9ea5c1e9cd8bd9c72424052d58ec83c6630 | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:85 | afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b | [A] p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:86 | 7772e17d4c775f14b0d67a90911876e06c8e99f2aca2d415dcf0b6d07d27e3fd | [A] p_konum_plus/quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:87 | 4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d | [A] p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:97 | 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 | [A] p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:98 | b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d | [A] p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:99 | 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0 | [A] p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md |

| provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:125 | 8b560d88ac36ce24a385e4d21975082acc3177bf005b730b962fe80ab99350c8 | [X] unavailable custody/ZIP bytes |


### Hunk mapping


[A] Vs-rp1 independent mapping: 1 R-4; 2 §5 wiring; 3 R-1; 4 §5 wiring; 5 §9 wiring; 6 R-5; 7 R-1; 8 R-5; 9–19 R-1 (18 comment, 19 executable); 20–22 R-2; 23 R-1; 24 R-5; 25 §5 wiring (mode/launch guard); 26 §9 wiring; 27 R-1; 28 R-5; 29–31 §9 wiring; 32–36 R-3 (35/36 output/gate wiring for R-3). Delivered labels are preserved in static output; discrepancies are IR1-16.

[A] Vs-r4-2 hunk families: 1 R-4; 2 §5 wiring; 3–5 C-2; 6 R-1; 7 §5 wiring; 8 §9 wiring; 9 C-6; 10 R-5; 11 R-1; 12–14 C-5; 15 R-5; 16 C-5 bookkeeping; 17 C-5; 18–25 R-1 ID intake/calls; 26 mixes C-3/R-1/R-2/R-5 and requires splitting; 27 C-2; 28 C-3; 29 mixes §9 wiring with new R-1/R-5 invocations and requires splitting; 30 R-1; 31 R-5; 32 C-1; 33/34 §9 wiring; 35 C-6; 36 mixes R-3 with new code-record/result fields and requires splitting. These annotations do not identify any new unauthorized science computation.


### Recomputed attempt diff
```diff
--- quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py
+++ calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py
@@ -129,23 +129,40 @@
 # (not just a name), the store is one disclosed, empty-at-first directory,
 # and every stored unit carries the pid/start-time of the process that
 # computed it -- this is what Y-01 corrects relative to r2's layer.
-# rp1-r1 attempt 1 (T-RP-1 = ACTIVE_FROM_START, carried from D-10 §2 into
-# D-12/rp1-r1 instruction §4): the restart layer stays ACTIVE from the first
-# attempt of THIS cycle too -- this is a child of the rp1 harness
-# (39c733a3...), itself the child of r4-2 (b988e962...). rp1-r1 is the FIRST
-# B-correction cycle of rp1 (D-11 r1 §6 counts from here), closing RP1A-01/
-# 02/03 (R-1/R-2/R-3) with RP1A-04/05/06 riding along (PI-d) and RP1A-07's
-# auditor-only evidence-limit procedure (R-4). D-11 r1 governs this cycle's
-# review-and-audit discipline.
-# The rp1-r1 store is its own directory, EMPTY at attempt 1's first launch;
+# rp1-r1 attempt 2 (T-RP-1 = ACTIVE_FROM_START, carried from D-10 §2 into
+# D-12/rp1-r1 instruction §4): the restart layer stays ACTIVE -- this is a
+# child of the rp1 harness (39c733a3...), itself the child of r4-2
+# (b988e962...). rp1-r1 is the FIRST B-correction cycle of rp1 (D-11 r1 §6
+# counts from here), closing RP1A-01/02/03 (R-1/R-2/R-3) with RP1A-04/05/06
+# riding along (PI-d) and RP1A-07's auditor-only evidence-limit procedure
+# (R-4). D-11 r1 governs this cycle's review-and-audit discipline.
+# Attempt 1 (pid 34228) ran the ENTIRE computation successfully --
+# T-F1-LOADER-SYNTH (21/21 cases incl. the 8 new R-2 branches),
+# T-F1-HANDOFF-SYNTH (144/144 real-mode contexts), T-CONTEXT-ID-UNIQUE,
+# DETERMINISM=True, residual series unchanged -- then STOPPED at
+# T-NONREG-R4-2 with s_findings=[] and 6 U findings, all three BUGS IN THE
+# R-3 COMPARISON LOGIC ITSELF, not in any computation: (a) the COUNT kind
+# re-canonicalized an already-canonicalized leaf string, so it could never
+# match; (b) a bare "exc_injection_fixtures" EQUAL declaration (meant only
+# for test_evidence.json's copy) collided with results.json's copy of the
+# same key, stopping recursion before results.json's own
+# exc_injection_fixtures.pass_key_namespaces_disjoint ADDITION leaf was
+# reached; (c) three new test_evidence.json capture-record fields
+# (exc_captures, exc_captures_run2, exc_captures_unit_phase) were declared
+# EQUAL instead of provenance-stripped, the same shape solver_exceptions
+# already handles. Fixed for attempt 2; none of the three touched any
+# computation -- see
+# quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md.
+# The rp1-r1 store is its own directory, EMPTY at attempt 2's first launch;
 # the rp1/r4-2/r4-1/r4 stores stay where they are, untouched and unread.
 RESTART_LAYER_ACTIVE = True
 
-# rp1-r1 attempt 1 supersedes nothing within this cycle.
-SUPERSEDES_HARNESS_SHA256 = None
-SUPERSEDES_CUSTODY_SHA256 = None
-SUPERSEDES_NOTE_PATH = None
-ATTEMPT_NUMBER = 1
+# rp1-r1 attempt 2 supersedes the attempt-1 harness (the three R-3
+# comparison-logic fixes).
+SUPERSEDES_HARNESS_SHA256 = "4bffb33aec4bfee48e2ed57bf3546988d809a4b49f2fe830e7e691713640114d"
+SUPERSEDES_CUSTODY_SHA256 = "dc10e08c48ee5dcf74fcf1202a324fdcfce097fd61530e9eced5d5f3b9bf612d"
+SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md"
+ATTEMPT_NUMBER = 2
 # R41A-02(c): every launch writes its OWN stdout/stderr pair with a
 # launch-numbered name; no log file is ever overwritten. The launch number
 # comes from the ENVIRONMENT (F3_RP1R1_LAUNCH, set by the caller alongside
@@ -5397,7 +5414,6 @@
         "a5_contract_violations": ("EQUAL", "unchanged"),
         "acf": ("EQUAL", "unchanged"),
         "comparator_nan": ("EQUAL", "unchanged"),
-        "exc_injection_fixtures": ("EQUAL", "unchanged"),
         "fix_a5_true": ("EQUAL", "unchanged"),
         "io_free_assertion": ("EQUAL", "unchanged"),
         "loader_node_hashes": ("EQUAL", "unchanged"),
@@ -5416,12 +5432,18 @@
         "wrapper_restore_ok": ("EQUAL", "unchanged"),
     }
 
-    def _solver_exceptions_content_equal(a_list, b_list):
-        """solver_exceptions: a natural COVERED event reproduces identically
-        under unchanged frozen code+data, but its OWN provenance (pid,
-        start_iso, the traceback's file path -- which names the harness
-        file, different between r4-2 and rp1-r1) legitimately differs every
-        run. Compare with those three fields stripped; a difference in
+    # R-3 (rp1-r1): every list-of-capture-records path whose records carry
+    # their OWN per-process provenance (pid, start_iso, and traceback,
+    # which names the harness file by path) and therefore legitimately
+    # differ every run regardless of content. solver_exceptions
+    # (results.json) and the three INJ-EXC capture lists (test_evidence.json)
+    # all share this shape.
+    _PROVENANCE_STRIPPED_LIST_PATHS = {
+        "solver_exceptions", "exc_captures", "exc_captures_run2",
+        "exc_captures_unit_phase"}
+
+    def _provenance_stripped_content_equal(a_list, b_list):
+        """Compare with pid/start_iso/traceback stripped; a difference in
         anything else is content, not provenance, and is a real finding."""
         def strip(rec):
             return {k: v for k, v in rec.items()
@@ -5467,8 +5489,14 @@
         if kind == "ADDITION":
             return a_val == "<ABSENT>" and b_val != "<ABSENT>"
         if kind == "COUNT":
+            # a_val/b_val are ALREADY _cn()-canonicalized strings (they come
+            # straight out of _flatten_leaves); canonicalize only the
+            # declared literals, never re-canonicalize an already-canon
+            # string (that double application was attempt-1's bug: it
+            # compared json.dumps(canon("<a cn string>")) against
+            # json.dumps(canon(<raw list>)), which can never match).
             _, exp_a, exp_b, _reason = kind_tuple
-            return _cn(a_val) == _cn(exp_a) and _cn(b_val) == _cn(exp_b)
+            return a_val == _cn(exp_a) and b_val == _cn(exp_b)
         return False
 
     def _diff_full(a_doc, b_doc, exclude_keys):
@@ -5484,8 +5512,8 @@
             b_val = fb.get(path, "<ABSENT>")
             if a_val == b_val:
                 continue
-            if path == "solver_exceptions":
-                if _solver_exceptions_content_equal(
+            if path in _PROVENANCE_STRIPPED_LIST_PATHS:
+                if _provenance_stripped_content_equal(
                         json.loads(a_val) if a_val != "<ABSENT>" else [],
                         json.loads(b_val) if b_val != "<ABSENT>" else []):
                     e_rows_.append(dict(

```


### audit_completion_setup.py
```python
"""Prepare the auditor's report generator and segregate copied stale sidecars."""
from pathlib import Path
import hashlib, json, datetime

BASE = Path(__file__).resolve().parent
p = BASE / 'audit_finalize.py'
s = p.read_text(encoding='utf8')
changes = {
    'Capture counts 8/1/1 occur in reason strings, without numeric count assertions. ': 'Capture counts 8/1/1 are declared in reasons and preserved by normalized list equality against the pinned baseline. ',
    'Compare/report leaves with exact declarations, add machine count expectations, and retain': 'Compare/report leaves with exact declarations and retain',
    'numeric capture counts are explanatory text, not enforced literals.': 'capture multiplicities are explicitly declared as 8/1/1 in reasons and enforced by normalized-list equality against the pinned baseline.',
    'CSV declarations and unasserted numeric capture counts remain open': 'CSV declaration reporting and traceback normalization remain open',
    'calibration/_w3_writer_rp1-r1_tmp.py:39': 'calibration/_w3_writer_rp1-r1_tmp.py:52',
    'The only complete harness process used the original delivered source hash.': 'The sole full-harness invocation used the original delivered source hash.',
    'Complete derived byte/hash/diff outputs are embedded below;': 'Derived outputs and scripts are embedded below, with raw-evidence file hashes for the larger files;',
    'two scoped informational estimate lines delivered; arithmetic checked;': 'two scoped informational estimate lines delivered; informational arithmetic independently checked;'
}
for old,new in changes.items():
    assert old in s, old
    s=s.replace(old,new)
s=s.replace('(the harness separately verifies 31).', '(the harness separately verifies 31). The estimate says 42k+ warning records; delivered stderr contains 33013 warning records (66026 lines), including 28 RuntimeWarnings. The older SCEN-A estimate describes full banks, but its family telemetry comes from MINI_BANK; this scope mismatch must be disclosed.')
s=s.replace("for script in ('audit_setup.py'", "for script in ('audit_completion_setup.py','audit_setup.py'")
p.write_text(s,encoding='utf8',newline='\n')

# The original .md files were moved before launch. Their copied sidecars must
# travel with them, rather than appear to pin the auditor's replacement record.
provenance=BASE/'rerun_9035df0/p_konum_plus/provenance'
kept=BASE/'kept_aside'
records=[]
for attempt in (1,2):
    name=f'f3_step2_rp1-r1_preexecution_custody_attempt{attempt}_2026-10-05.md'
    side=provenance/(name+'.sha256')
    target=kept/side.name
    if side.exists():
        assert not target.exists()
        digest=hashlib.sha256(side.read_bytes()).hexdigest()
        side.rename(target)
        records.append({'source':str(side),'kept_aside':str(target),'sha256':digest})
own=provenance/'f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md'
digest=hashlib.sha256(own.read_bytes()).hexdigest()
external=BASE/'audit_evidence/auditor_w3.sha256'
external.write_text(digest+'  '+str(own)+'\n',encoding='utf8')
(BASE/'audit_evidence/stale_custody_sidecars.json').write_text(json.dumps({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'moved':records,'own_custody_sha256':digest,'own_sidecar':str(external)},indent=2),encoding='utf8')
print('Report evidence wording corrected; two copied executor sidecars preserved outside rerun provenance; own W-3 pinned externally.')

```


### audit_setup.py
```python
"""Extract allowed delivered blobs without modifying the source repository."""
from pathlib import Path
import subprocess, hashlib, json, datetime, shutil, platform
import numpy, scipy

BASE = Path(__file__).resolve().parent
REPO = BASE / 'repo'
EVIDENCE = BASE / 'audit_evidence'
DELIVERED = BASE / 'delivered_9035df0'
RERUN = BASE / 'rerun_9035df0'
COMMIT = '9035df0831d8646cca7f1e73937161a3d2d7d018'
def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def main():
    assert not DELIVERED.exists() and not RERUN.exists(), 'Never overwrite an audit copy'
    EVIDENCE.mkdir(exist_ok=True)
    tree = git('ls-tree', '-r', COMMIT, '--', 'p_konum_plus').decode().splitlines()
    denied = {'p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv',
              'p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv'}
    allowed = []
    for row in tree:
        meta, path = row.split('\t')
        if path in denied: continue
        assert 'data/raw/' not in path and '/.rp1-r1_restart_store' not in path
        allowed.append((meta.split()[2], path))
    proc = subprocess.Popen(['git', '-C', str(REPO), 'cat-file', '--batch'],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    hashes = {}
    for oid, path in allowed:
        proc.stdin.write((oid+'\n').encode()); proc.stdin.flush()
        header = proc.stdout.readline().decode().split()
        size = int(header[2]); data = proc.stdout.read(size)
        assert proc.stdout.read(1) == b'\n'
        dst = DELIVERED / path; dst.parent.mkdir(parents=True, exist_ok=True); dst.write_bytes(data)
        hashes[path] = hashlib.sha256(data).hexdigest()
    proc.stdin.close(); assert proc.wait() == 0
    shutil.copytree(DELIVERED, RERUN)
    aside = BASE / 'kept_aside'; aside.mkdir(exist_ok=True)
    for attempt in (1, 2):
        name = f'f3_step2_rp1-r1_preexecution_custody_attempt{attempt}_2026-10-05.md'
        src = RERUN / 'p_konum_plus/provenance' / name
        shutil.move(str(src), str(aside / name))
    assert not (RERUN / 'p_konum_plus/calibration/.rp1-r1_restart_store_2026-10-05').exists()
    setup = {'commit':COMMIT, 'source_head':git('rev-parse','HEAD').decode().strip(),
             'source_status':git('status','--porcelain').decode(),
             'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'environment':{'python':platform.python_version(), 'numpy':numpy.__version__,
                            'scipy':scipy.__version__, 'platform':platform.platform()},
             'copied_files':len(hashes), 'excluded_unopened':sorted(denied)}
    (EVIDENCE / 'delivered_hashes.json').write_text(json.dumps(hashes,indent=2), encoding='utf8')
    (EVIDENCE / 'setup.json').write_text(json.dumps(setup,indent=2), encoding='utf8')
    (EVIDENCE / 'parent_diff.tsv').write_bytes(git('diff','--name-status','b6d2483',COMMIT))
    (EVIDENCE / 'final_commit_diff.tsv').write_bytes(git('diff','--name-status','63d4846',COMMIT))
    print(json.dumps(setup,indent=2))
if __name__ == '__main__': main()

```


### audit_run.py
```python
"""Run delivered W-3 writer and unchanged harness in the disposable root."""
from pathlib import Path
import subprocess, os, json, datetime, hashlib, sys
BASE=Path(__file__).resolve().parent
ROOT=BASE/'rerun_9035df0'
OUT=BASE/'audit_evidence'
env=os.environ.copy()
env.update(F3_REPO_ROOT=str(ROOT), F3_RP1R1_LAUNCH='1', PYTHONUNBUFFERED='1',
           OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
status={'started':now(), 'root':str(ROOT), 'launch':1, 'interpreter':sys.executable}
def save(): (OUT/'rerun_status.json').write_text(json.dumps(status,indent=2),encoding='utf8')
save()
writer=ROOT/'p_konum_plus/calibration/_w3_writer_rp1-r1_tmp.py'
with (OUT/'w3_stdout.log').open('wb') as out, (OUT/'w3_stderr.log').open('wb') as err:
    done=subprocess.run([sys.executable,str(writer)],cwd=ROOT,env=env,stdout=out,stderr=err)
status['writer_exit']=done.returncode; save()
if done.returncode: sys.exit(done.returncode)
harness=ROOT/'p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py'
status['harness_sha256']=hashlib.sha256(harness.read_bytes()).hexdigest()
cal=ROOT/'p_konum_plus/calibration'
with (cal/'f3_step2_rp1-r1_launch1_stdout_2026-10-05.log').open('xb') as out, \
     (cal/'f3_step2_rp1-r1_launch1_stderr_2026-10-05.log').open('xb') as err:
    proc=subprocess.Popen([sys.executable,str(harness)],cwd=ROOT,env=env,stdout=out,stderr=err)
    status.update(pid=proc.pid,harness_started=now(),state='RUNNING');save()
    print('Harness launched: '+json.dumps(status),flush=True)
    code=proc.wait()
status.update(exit_code=code,finished=now(),state='FINISHED');save()
print(json.dumps(status),flush=True)
sys.exit(code)

```


### audit_run_detached.py
```python
"""Auditor launch2 in a new empty-store copy, started as a hidden Windows process.

Preserves interrupted launch1 and its partial report. No source edits or real data.
"""
from pathlib import Path
import subprocess, os, json, datetime, hashlib, sys, shutil
BASE=Path(__file__).resolve().parent
E=BASE/'audit_evidence'
ROOT=BASE/'rerun_9035df0_launch2'
H='p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(status):
    temp=E/'rerun_status.json.tmp'
    temp.write_text(json.dumps(status,indent=2),encoding='utf8');temp.replace(E/'rerun_status.json')
def main():
    history=BASE/'audit_history/auditor_launch1_early_exit'
    assert not ROOT.exists() and not history.exists()
    history.mkdir(parents=True)
    shutil.copytree(E,history/'audit_evidence')
    shutil.copytree(BASE/'audit_delivery',history/'audit_delivery')
    old=json.loads((E/'rerun_status.json').read_text(encoding='utf8'))
    assert old['state']=='FINISHED'
    shutil.copytree(BASE/'delivered_9035df0',ROOT)
    kept=history.parent/'auditor_launch2_kept_aside';kept.mkdir()
    for attempt in (1,2):
        name=f'f3_step2_rp1-r1_preexecution_custody_attempt{attempt}_2026-10-05.md'
        for suffix in ('','.sha256'):
            path=ROOT/'p_konum_plus/provenance'/(name+suffix)
            path.rename(kept/path.name)
    assert not (ROOT/'p_konum_plus/calibration/.rp1-r1_restart_store_2026-10-05').exists()
    status=dict(started=now(),root=str(ROOT),launch=2,interpreter=sys.executable,state='PREPARING',runner_pid=os.getpid(),previous_auditor_launch=old,previous_evidence=str(history))
    save(status)
    env=os.environ.copy();env.update(F3_REPO_ROOT=str(ROOT),F3_RP1R1_LAUNCH='2',PYTHONUNBUFFERED='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
    writer=ROOT/'p_konum_plus/calibration/_w3_writer_rp1-r1_tmp.py'
    with (E/'w3_stdout.log').open('wb') as out,(E/'w3_stderr.log').open('wb') as err:
        done=subprocess.run([sys.executable,str(writer)],cwd=ROOT,env=env,stdout=out,stderr=err)
    status['writer_exit']=done.returncode;save(status)
    if done.returncode:raise RuntimeError('Unchanged writer failed: '+str(done.returncode))
    own=ROOT/'p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md'
    digest=hashlib.sha256(own.read_bytes()).hexdigest()
    (E/'auditor_w3_launch2.sha256').write_text(digest+'  '+str(own)+'\n',encoding='utf8')
    harness=ROOT/H
    status['harness_sha256']=hashlib.sha256(harness.read_bytes()).hexdigest()
    assert status['harness_sha256']=='cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb'
    cal=ROOT/'p_konum_plus/calibration'
    with (cal/'f3_step2_rp1-r1_launch2_stdout_2026-10-05.log').open('wb') as out,(cal/'f3_step2_rp1-r1_launch2_stderr_2026-10-05.log').open('wb') as err:
        proc=subprocess.Popen([sys.executable,str(harness)],cwd=ROOT,env=env,stdout=out,stderr=err)
        status.update(pid=proc.pid,harness_started=now(),state='RUNNING');save(status)
        # The runner itself is outside the tool's foreground process session.
        code=proc.wait()
    status.update(exit_code=code,finished=now(),state='FINISHED');save(status)
    print(json.dumps(status),flush=True)
if __name__=='__main__':main()

```


### audit_checks.py
```python
"""Independent byte, diff, trace, and accounting checks; no real data opened."""
from pathlib import Path
import json, hashlib, csv, re, difflib, ast, collections, math
BASE=Path(__file__).resolve().parent
ROOT=BASE/'delivered_9035df0'
OUT=BASE/'audit_evidence'
P=ROOT/'p_konum_plus'
hashes=json.loads((OUT/'delivered_hashes.json').read_text())
def txt(path): return (P/path).read_text(encoding='utf8')
def js(path): return json.loads(txt(path))
def rows(path): return list(csv.DictReader(txt(path).splitlines()))
def sha(path): return hashlib.sha256((P/path).read_bytes()).hexdigest()
H='calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py'
source=txt(H);tree=ast.parse(source)
results=js('calibration/f3_step2_results_rp1-r1_2026-10-05.json')
r42=js('calibration/f3_step2_results_r4-2_2026-09-30.json')
te=js('calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json')
te42=js('calibration/f3_step2_test_evidence_r4-2_2026-09-30.json')
summary={}
added=[r.split('\t',1)[1] for r in (OUT/'parent_diff.tsv').read_text().splitlines()]
summary['parent_diff']={'files':len(added), 'only_additions_under_p':all(r.startswith('A\tp_konum_plus/') for r in (OUT/'parent_diff.tsv').read_text().splitlines()),'final_commit_diff':(OUT/'final_commit_diff.tsv').read_text()}
sidecars=[]
for path in added:
    if path.endswith('.sha256'):
        data=(ROOT/path).read_text(encoding='utf8').strip()
        pin=re.search(r'\b[0-9a-f]{64}\b',data).group()
        target=path[:-7];sidecars.append({'path':path,'pin':pin,'observed':hashes.get(target),'equal':pin==hashes.get(target)})
summary['new_sidecars']={'count':len(sidecars),'failures':[r for r in sidecars if not r['equal']]}
(OUT/'new_sidecar_checks.json').write_text(json.dumps(sidecars,indent=2))
summary['added_without_sidecars']=[p for p in added if not p.endswith('.sha256') and p+'.sha256' not in hashes and '_f1_synth_fixtures_' not in p]
def table_check(path):
    checked=[]
    for ln,line in enumerate(txt(path).splitlines(),1):
        if not line.startswith('|'):continue
        h=re.findall(r'\b[0-9a-f]{64}\b',line)
        cols=line.split('|')
        for pin in h:
            matches=re.findall(r'(?:p_konum_plus/)?(?:calibration|provenance|prompts|quarantine)/[^\s`|()]+',line)
            targets=[m.rstrip('.,') for m in matches]
            if targets:
                target=targets[0]; target=target if target.startswith('p_konum_plus/') else 'p_konum_plus/'+target
                if target.endswith('.sha256'):target=target[:-7]
                observed=hashes.get(target)
                checked.append({'line':ln,'target':target,'pin':pin,'observed':observed,'equal':pin==observed})
    return checked
old='provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md'
new='provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md'
summary['lists']={}
for path in (old,new,'provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md','provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md'):
    check=table_check(path); summary['lists'][path]={'checked':len(check),'failures':[r for r in check if not r['equal']]}
    (OUT/(Path(path).stem+'_table_checks.json')).write_text(json.dumps(check,indent=2))
oldtable=[l for l in txt(old).splitlines() if l.startswith('|')]
newtable=[l for l in txt(new).splitlines() if l.startswith('|')]
summary['list_table_diff']=list(difflib.unified_diff(oldtable,newtable,lineterm=''))
summary['diffs']={}
for tag,baseline in [('rp1','calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py'),('r4-2','calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py')]:
    delivered=txt(f'calibration/f3_step2_rp1-r1_harness_diff_vs_{tag}_2026-10-05.diff').splitlines()
    clean=[l for l in delivered if not l.startswith('#')]
    recomputed=list(difflib.unified_diff(txt(baseline).splitlines(),source.splitlines(),lineterm=''))
    # GNU diff and difflib can choose different context around blank lines.
    # Apply the delivered unified hunks and require exact resulting content.
    original=txt(baseline).splitlines(); produced=[];cursor=0; idx=2
    while idx<len(clean):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',clean[idx])
        assert m, clean[idx]
        start=int(m[1])-1;produced.extend(original[cursor:start]);cursor=start;idx+=1
        while idx<len(clean) and not clean[idx].startswith('@@'):
            line=clean[idx]; idx+=1
            if line.startswith('\\ No newline'):continue
            if line[0] in ' -':assert original[cursor]==line[1:], (cursor,line);cursor+=1
            if line[0] in ' +':produced.append(line[1:])
    produced.extend(original[cursor:]);ok=produced==source.splitlines()
    labels=[l for l in delivered if l.startswith('#HUNK')]
    summary['diffs'][tag]={'equal_hunks':ok,'hunks':len(labels),'labels':labels}
    (OUT/f'recomputed_vs_{tag}.diff').write_text('\n'.join(recomputed)+'\n')
att1='quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py'
attemptdiff=list(difflib.unified_diff(txt(att1).splitlines(),source.splitlines(),fromfile=att1,tofile=H,lineterm=''))
(OUT/'attempt1_to_attempt2.diff').write_text('\n'.join(attemptdiff)+'\n')
canonnode=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='canon')
ns={'np':__import__('numpy'),'math':math,'json':json}
exec(compile(ast.Module(body=[canonnode],type_ignores=[]),H,'exec'),ns)
canon=ns['canon']
def cn(v):return json.dumps(canon(v),sort_keys=True)
summary['scientific_delivered']={'evaluation_count':len(results['evaluations']),'evaluations_equal':cn(sorted(results['evaluations'],key=lambda x:x['fixture_id']))==cn(sorted(r42['evaluations'],key=lambda x:x['fixture_id'])),'stops_equal':sorted(cn(v) for v in results['stops'])==sorted(cn(v) for v in r42['stops']),'canonical':{k:results[k] for k in ('run1_canonical_sha256','run2_canonical_sha256','determinism')},'residual_hash':sha('calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json')}
summary['results_keys']=list(results)
summary['process']=results['process'];summary['environment']=results['environment'];summary['tests']=results['tests_run'];summary['end_state']=results['end_state'];summary['nonreg']=results['nonregression_vs_r4_2']
def normalize_tb(s):
    return re.sub(r'(File ")[^"]*f3_step2_adequacy_harness[^"\n]*\.py(")',r'\1<HARNESS>\2',s)
capture={}
te1=js('quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_test_evidence_rp1-r1_2026-10-05.json')
for key in ('exc_captures','exc_captures_run2','exc_captures_unit_phase'):
    checks=[]
    for tag,a,b in [('r42_to_attempt1',te42[key],te1[key]),('attempt1_to_attempt2',te1[key],te[key]),('r42_to_attempt2',te42[key],te[key])]:
        strip=lambda r:{k:v for k,v in r.items() if k not in ('pid','start_iso','traceback')}
        equal=sorted(cn(strip(v)) for v in a)==sorted(cn(strip(v)) for v in b)
        ta=sorted(normalize_tb(v['traceback']) for v in a);tb=sorted(normalize_tb(v['traceback']) for v in b)
        diff='\n'.join(difflib.unified_diff('\n'.join(ta).splitlines(),'\n'.join(tb).splitlines(),lineterm=''))
        checks.append({'pair':tag,'counts':[len(a),len(b)],'stripped_equal':equal,'path_normalized_traceback_equal':ta==tb,'traceback_diff':diff})
    capture[key]=checks
summary['captures']=capture
nr=rows('calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv')
summary['nr_csv']={'rows':len(nr),'fields':list(nr[0]),'classes':dict(collections.Counter(r['classification'] for r in nr)),'end_state_rows':[r for r in nr if r['path'].startswith('end_state.')]}
per=rows('calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv')
store=rows('calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv')
reads=rows('calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv')
tel=rows('calibration/f3_step2_telemetry_rp1-r1_2026-10-05.csv')
summary['accounting']={}
for tag,rs in [('percall',per),('store',store),('reads',reads),('telemetry',tel)]:
    cols=list(rs[0]);counters={c:dict(collections.Counter(r[c] for r in rs)) for c in cols if c in ('source','phase','pid','scope','key_family','fixture','fitter')}
    summary['accounting'][tag]={'rows':len(rs),'fields':cols,'counters':counters,'sample':rs[:2]}
def decode_key(r):
    name=r.get('path',r.get('key',r.get('key_name','')))
    name=name.split('__',1)[1] if '__' in name else name
    for scope in ('f1handoff','f1gap','excpass1','excpass2','tstoreread_cold','tstoreread_warm'):
        if name.startswith(scope+'__'):return scope,name[len(scope)+2:].split('_',1)[0]
    return 'base',name.split('_',1)[0]
summary['accounting']['decoded_store_families']={'|'.join(k):v for k,v in collections.Counter(decode_key(r) for r in store).items()}
summary['f1_test_evidence']={k:results[k] for k in ('f1_loader_synth','f1_handoff_synth','context_id_unique','f1_contract_gap','f1_repro_gate_synth','store_read_accounting','key_namespace_table')}
summary['opened_audit']={'paths':results['opened_files_audit_derived'],'forbidden_matches':[s for s in results['opened_files_audit_derived'] if 'data/raw/' in s.replace('\\','/') or 'f1_input_hash_table_2026-08-28.csv' in s or 'f1_eligible_trajectory_manifest_2026-08-28.csv' in s]}
fixtures=list((P/'calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05').rglob('*.txt'))
summary['synthetic_fixture_count']=len(fixtures)
summary['synthetic_total_files']=len(list((P/'calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05').rglob('*')))-len([p for p in (P/'calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05').rglob('*') if p.is_dir()])
(OUT/'static_checks.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
print(json.dumps({k:summary[k] for k in ('parent_diff','new_sidecars','added_without_sidecars','lists','list_table_diff','diffs','scientific_delivered','nr_csv','synthetic_fixture_count')},indent=2))
print('Detailed evidence: audit_evidence/static_checks.json')

```


### audit_probes.py
```python
"""Independent structural probes of delivered comparison helpers, no harness edit."""
from pathlib import Path
import ast,json,math,re,difflib,csv,subprocess,hashlib,collections
import numpy as np
BASE=Path(__file__).resolve().parent;P=BASE/'delivered_9035df0/p_konum_plus';OUT=BASE/'audit_evidence'
H=P/'calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py'
source=H.read_text(encoding='utf8');tree=ast.parse(source)
main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
functions=['_provenance_stripped_content_equal','_flatten_leaves','_classify_e_typed','_expectation_held','_diff_full']
nodes=[n for n in main.body if isinstance(n,ast.FunctionDef) and n.name in functions]
assigns=[n for n in main.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('EXPECTATIONS_E','_PROVENANCE_STRIPPED_LIST_PATHS') for t in n.targets)]
canonnode=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='canon')
ns={'np':np,'math':math,'json':json};exec(compile(ast.Module(body=[canonnode],type_ignores=[]),str(H),'exec'),ns)
ns['_cn']=lambda x:json.dumps(ns['canon'](x),sort_keys=True)
exec(compile(ast.Module(body=assigns+nodes,type_ignores=[]),str(H),'exec'),ns)
probe={}
probe['equal_wrong_COUNT_skipped']=ns['_diff_full']({'end_state':{'narrowed_evidence':['T-R2-2']}},{'end_state':{'narrowed_evidence':['T-R2-2']}},set())
probe['missing_both_ADDITION_skipped']=ns['_diff_full']({}, {},set())
probe['equal_wrong_ADDITION_skipped']=ns['_diff_full']({'f1_handoff_synth':{}},{'f1_handoff_synth':{}},set())
probe['traceback_location_change_accepted']=ns['_diff_full']({'exc_captures':[{'pid':1,'start_iso':'a','traceback':'raised at ORIGINAL site','type':'RuntimeError'}]},{'exc_captures':[{'pid':2,'start_iso':'b','traceback':'raised at DIFFERENT site','type':'RuntimeError'}]},set())
probe['bad_capture_count_accepted_when_both_2']=ns['_diff_full']({'exc_captures':[{},{}]},{'exc_captures':[{},{}]},set())
probe['whole_subtree_stop_points']=[k for k in ns['EXPECTATIONS_E'] if k in ('f1_handoff_synth','f1_loader_synth','key_namespace_table','process.spline_telemetry_calls_by_phase','process.units_computed_this_process','a5')]
probe['declaration_count']=len(ns['EXPECTATIONS_E'])
probe['declared_kind_counts']=dict(collections.Counter(v[0] for v in ns['EXPECTATIONS_E'].values()))
# Source-line mapping: verify path-only differences, then account for verified unchanged lines.
sources={
 'r4-2':(P/'calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py').read_text(),
 'attempt1':(P/'quarantine/f3_step2_adequacy_harness_rp1-r1_2026-10-05_ATTEMPT1_NONREG_E_DECLARATION_BUGS.py').read_text(),
 'attempt2':source}
tes={
 'r4-2':json.loads((P/'calibration/f3_step2_test_evidence_r4-2_2026-09-30.json').read_text()),
 'attempt1':json.loads((P/'quarantine/ATTEMPT1_NONREG_E_DECLARATION_BUGS_f3_step2_test_evidence_rp1-r1_2026-10-05.json').read_text()),
 'attempt2':json.loads((P/'calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json').read_text())}
trace=[]
for a,b in [('r4-2','attempt1'),('attempt1','attempt2'),('r4-2','attempt2')]:
    old=sources[a].splitlines();new=sources[b].splitlines();mapping={}
    for tag,i,j,k,l in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes():
        if tag=='equal':mapping.update({x+1:k+(x-i)+1 for x in range(i,j)})
    def norm(s,remap):
        def repl(m):
            line=int(m[1]);line=mapping.get(line,-line) if remap else line
            return 'File "<HARNESS>", line '+str(line)
        return re.sub(r'File "[^"\n]*f3_step2_adequacy_harness[^"\n]*\.py", line (\d+)',repl,s)
    for key in ('exc_captures','exc_captures_run2','exc_captures_unit_phase'):
        va=sorted(norm(r['traceback'],True) for r in tes[a][key]);vb=sorted(norm(r['traceback'],False) for r in tes[b][key])
        trace.append({'pair':a+' -> '+b,'key':key,'equal_after_verified_source_line_mapping':va==vb})
probe['traceback_source_line_mapping']=trace
# Allowed, limited hash-column read ONLY. Neither eligible manifest nor any named input opened.
raw=subprocess.check_output(['git','-C',str(BASE/'repo'),'show','9035df0:p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv'])
reader=csv.DictReader(raw.decode('utf-8-sig').splitlines())
hashcol=[c for c in reader.fieldnames if 'sha256' in c.lower() or c.lower()=='hash']
assert len(hashcol)==1,hashcol
realhash={r[hashcol[0]] for r in reader};del raw
fixture=P/'calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05'
synthhash={hashlib.sha256(p.read_bytes()).hexdigest() for p in fixture.rglob('*') if p.is_file()}
probe['hash_disjoint']={'real_hash_column_entries':len(realhash),'synthetic_files':sum(p.is_file() for p in fixture.rglob('*')),'unique_synthetic_hashes':len(synthhash),'intersection_count':len(realhash&synthhash)}
# Every executor-written full hash occurrence, retained with source context for adjudication.
docnames=[
 'provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md',
 'provenance/f3_step2_correction_report_rp1-r1_2026-10-05.md',
 'calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md',
 'provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md',
 'provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md',
 'provenance/f3_realdata_prep_rp1-r1_auditor_rerun_procedure_2026-10-05.md',
 'provenance/f3_realdata_prep_rp1-r1_size_estimate_2026-10-05.md',
 'quarantine/f3_step2_rp1-r1_attempt1_nonreg_e_declaration_bugs_note_2026-10-06.md']
hashes=json.loads((OUT/'delivered_hashes.json').read_text());byhash=collections.defaultdict(list)
for p,h in hashes.items():byhash[h].append(p)
occ=[]
for doc in docnames+['provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md']:
    lines=(P/doc).read_text(encoding='utf8').splitlines()
    for ln,line in enumerate(lines,1):
        for h in re.findall(r'\b[0-9a-f]{64}\b',line):
            occ.append({'document':doc,'line':ln,'hash':h,'matching_byte_paths':byhash[h], 'context':'\n'.join(lines[max(0,ln-3):ln+2])})
probe['hash_occurrences_original8']=sum(r['document'] in docnames for r in occ)
probe['hash_occurrences_bothlists_total']=len(occ)
probe['hash_occurrences_without_matching_file']=[{k:v for k,v in r.items() if k!='context'} for r in occ if not r['matching_byte_paths']]
run=json.loads((P/'calibration/f3_step2_results_rp1-r1_2026-10-05.json').read_text())
doc=dict(evals=run['evaluations'],stops=run['stops'],pins=dict(mask_full=run['tests_run']['PIN-MASKED-OBJECTIVE']['passed'],fs=run['tests_run']['PIN-FEATURE-START-MASKED']['passed']))
probe['recomputed_canonical_sha256']=hashlib.sha256(json.dumps(doc,sort_keys=True).encode()).hexdigest()
# The source's aggregate cold condition rejects a valid same-attempt resumed read.
storetest=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='t_store_read_accounting')
probe_ns={'_t_store_read_accounting_case':lambda spl,scope,prime_first:dict(pass_=True,fit1_reads=146)}
exec(compile(ast.Module(body=[storetest],type_ignores=[]),str(H),'exec'),probe_ns)
probe['resumed_cold_helper_success_but_aggregate_fail']=probe_ns['t_store_read_accounting'](None)
# Record exact locations of constant ok fields, including explicit negative branches.
loader=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='t_f1_loader_synth')
probe['loader_constant_ok_locations']=[dict(line=n.lineno,value=n.value.value) for n in ast.walk(loader) if isinstance(n,ast.keyword) and n.arg=='ok' and isinstance(n.value,ast.Constant)]
(OUT/'hash_occurrences_with_context.json').write_text(json.dumps(occ,indent=2),encoding='utf8')
(OUT/'probe_checks.json').write_text(json.dumps(probe,indent=2),encoding='utf8')
print(json.dumps(probe,indent=2))

```


### audit_plan.py
```python
"""Derive checkpoint plan without calling any optimizer or outcome evaluator."""
from pathlib import Path
import os,sys,ast,importlib.util,math,json,csv,hashlib,collections,types
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
import numpy as np
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parent;P=BASE/'delivered_9035df0/p_konum_plus';OUT=BASE/'audit_evidence'
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,P/path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
f2=load('plan_f2','calibration/f2_step2_feasibility_harness_r3_2026-09-01.py')
gen=load('plan_gen','calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py')
source=(P/'calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py').read_text()
tree=ast.parse(source)
names=['feature_start_validity','feature_start_masked','f1_load_raw_dir','_f1_share','f1_normalize','f1_post_z_qc','f1_build_scenarios','f1_context_id_table','_ckpt_safe_name']
nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
classes=[n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='F1QCFailure']
ns={'os':os,'np':np,'math':math,'T':146,'F1_T':146,'F1_YEAR_MIN':1880,'F1_YEAR_MAX':2025,'F1_POST_Z_TOLERANCE':1e-8,'SEXES':['F','M'],'hashlib':hashlib,'_CKPT_UNSAFE':str.maketrans({c:'_' for c in '<>:"/\\|?*[]'})}
exec(compile(ast.Module(body=classes+nodes,type_ignores=[]),'delivered helper functions','exec'),ns)
grids={f:f2.build_grid(f)[1] for f in ('P-01','P-02')}
contexts={'full':np.arange(146),**{'fold%d'%i:np.setdiff1d(np.arange(146),np.arange(b,e)) for i,(b,e) in enumerate(zip([0,29,58,87,116],[29,58,87,116,146]))},'probeL':np.arange(15,146),'probeR':np.arange(0,131)}
# Read the actual frozen fold boundaries, without executing the harness.
for n in tree.body:
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FOLD_BOUNDS' for t in n.targets):
        ns['np']=np;bounds=eval(compile(ast.Expression(n.value),'fold bounds','eval'),ns)
        for i in range(5):contexts['fold%d'%i]=np.setdiff1d(np.arange(146),np.arange(bounds[i],bounds[i+1]))
expected=[];feature_stats=collections.Counter();fitstats=collections.Counter()
def add_fit(scope,fid,fam,x,obs,mask,bank,inj=False,fs_reject=False):
    inds=range(len(grids[fam])) if bank=='FULL_LATTICE' else f2.mini_bank_indices(len(grids[fam]))
    starts=[('grid[%d]'%i,grids[fam][i]) for i in inds]
    feature,_,_=ns['feature_start_masked'](f2,fam,x,obs)
    ok,why=ns['feature_start_validity'](f2,fam,feature)
    if fs_reject:ok=False;why='TEST_ONLY_INJECTION'
    if ok and tuple(float(v) for v in feature) in [tuple(float(v) for v in st) for _,st in starts]:ok=False;why='DUPLICATE'
    if ok:starts.append(('feature',feature))
    feature_stats[scope+'|'+fid+'|'+fam+'|'+('accepted' if ok else str(why))]+=1
    fitstats[scope+'|'+fid+'|'+fam]+=1
    xh=hashlib.sha256(np.asarray(x,dtype=np.float64).tobytes()).hexdigest()[:16]
    for sid,_ in starts:expected.append(scope+'onestart_%s_%s_%s_%s_%s_%s'%(fid,fam,mask,sid,inj,xh))
u0=72.0/145.0;k_mid=math.sqrt(4*f2.K_MAX)
for fid,fam,theta in [('FIX-P01-BENIGN','P-01',(u0-1/8,u0+1/8,k_mid,k_mid)),('FIX-P02-BENIGN','P-02',(u0,0.32057672965544004,0.32057672965544004,math.sqrt(6)))]:
    stable=f2.p01_stable if fam=='P-01' else f2.p02_stable
    status,_,x=f2.zero_variance_rule(stable(theta));assert status=='OK'
    add_fit('',fid,fam,x,contexts['full'],'nr01ii:'+fid,'MINI_BANK')
x=np.zeros(146);x[70]=3;x=(x-x.mean())/x.std(ddof=0)
add_fit('','UT-A5-II','P-01',x,contexts['probeL'],'ut','MINI_BANK',True,True)
add_fit('','UT-A5-III','P-02',x,contexts['probeR'],'ut','MINI_BANK',True,False)
x=gen.make_traj('bump_a',20260912,.10)
add_fit('','UT-PROBE-DECOUPLE','P-01',x,contexts['full'],'ut:full','MINI_BANK',True)
add_fit('','UT-PROBE-DECOUPLE','P-01',x,contexts['probeL'],'ut:probeL','MINI_BANK')
for run in ('run1','run2'):
    for sc in gen.REAL_SCENARIOS:
        injection={(i['traj'],i['family'],i['context']):i['mode'] for i in sc['injections']}
        for sex in ('F','M'):
            for ti,(kind,seed,sigma) in enumerate(sc['strata'][sex]):
                x=gen.make_traj(kind,seed,sigma)
                for fam in ('P-01','P-02'):
                    for ctx,obs in contexts.items():
                        inj=injection.get(((sex,ti),fam,ctx))
                        add_fit('',sc['fixture_id'],fam,x,obs,f'{run}:{sex}{ti}:{ctx}',sc['start_bank'],inj=='F2_FAULT_INJECTION',inj=='TEST_ONLY_INJECTION')
traj=gen.STARTS_FULL_TRAJ;x=gen.make_traj(traj['kind'],traj['seed'],traj['sigma'])
for fam in ('P-01','P-02'):add_fit('','FIX-STARTS-FULL',fam,x,contexts['full'],'full:'+fam,'FULL_LATTICE')
for direction,tag in (('down','index0'),('up','index145')):add_fit('','FIX-STARTS-DUP','P-02',gen.make_monotone(direction),contexts['full'],'dup:'+tag,'FULL_LATTICE')
for side,probe in (('left','probeL'),('right','probeR')):
    x=gen.make_step(side)
    for fam in ('P-01','P-02'):
        add_fit('','FIX-A5-TRUE',fam,x,contexts['full'],f'a5true:{side}:full','MINI_BANK')
        add_fit('','FIX-A5-TRUE',fam,x,contexts[probe],f'a5true:{side}:{probe}','MINI_BANK')
shares,denom=ns['f1_load_raw_dir'](str(P/'calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/good'))
z=ns['f1_normalize'](shares);sc=ns['f1_build_scenarios'](z)[0]
for sex in ('F','M'):
    for ti in range(len(sc['strata'][sex])):
        x=sc['real_x'][(sex,ti)];base=sc['real_mask_ids'][(sex,ti)]
        for fam in ('P-01','P-02'):
            for ctx,obs in contexts.items():add_fit('f1handoff__','F3-REAL',fam,x,obs,f'real:{base}:{fam}:{ctx}','FULL_LATTICE')
store=list(csv.DictReader((P/'calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv').read_text().splitlines()))
observed={r['path'] for r in store if '__onestart_' in r['path']}
planned={'29de608948a06cf2__'+ns['_ckpt_safe_name'](key)+'.pkl' for key in expected}
# _ckpt_safe_name receives full key (fp included), important for truncation.
planned={ns['_ckpt_safe_name']('29de608948a06cf2__'+key)+'.pkl' for key in expected}
plan={'grid_sizes':{k:len(v) for k,v in grids.items()},'family_fit_context_counts':dict(fitstats),'conditional_feature_counts':dict(feature_stats),'expected_onestart_units':len(planned),'observed_onestart_units':len(observed),'missing_keys':sorted(planned-observed),'unexpected_keys':sorted(observed-planned),'expected_spline_units':{'base':(2*2*8+2*(2*8-2)+4)*146,'excpass1':3*146,'excpass2':3*146,'f1handoff':6*8*146,'cold':146,'warm':146},'expected_coarse_units':{'realscen':2*2,'nrgates_all':1,'unittests_all':1},'partial_denominator':denom[(1949,'F')], 'dry_context_rows':len(ns['f1_context_id_table']([sc]))}
# A contract intake probe stops before any optimizer. No evaluator is called.
realnode=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='run_real_scenario')
gapclass=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='F1ContractGap')
def never_fit(*args,**kwargs):raise AssertionError('optimizer stub reached unexpectedly')
ns.update(sys=types.SimpleNamespace(modules={'plan_gen':gen}),GEN_MODULE_NAME='plan_gen',
          RUN_REAL_SCENARIO_REQUIRED_KEYS=['fixture_id','strata','start_bank','injections'],
          FIDELITY_DECLARED=[],REAL_MODE_IDS_PASSED=[],FAM_KEYS={'P-01':'P01','P-02':'P02'},
          FULL_O=np.arange(146),a5_support_safe=lambda *args:([0],None),
          a5_condition_i=lambda *args:False,fit_family=never_fit)
exec(compile(ast.Module(body=[gapclass,realnode],type_ignores=[]),'delivered consumer intake','exec'),ns)
plan['real_mode_contract_gap_probes']=[]
for key in ('real_x','real_mask_ids'):
    broken=dict(sc);del broken[key]
    try:ns['run_real_scenario'](f2,None,grids,broken,'audit_intake',[]);exc='NO FAILURE';message=''
    except Exception as e:exc=type(e).__name__;message=str(e)
    plan['real_mode_contract_gap_probes'].append({'removed':key,'exception':exc,'message':message,'required_F1ContractGap':exc=='F1ContractGap'})
(OUT/'derived_plan.json').write_text(json.dumps(plan,indent=2),encoding='utf8')
print(json.dumps(plan,indent=2))

```


### audit_additional_checks.py
```python
"""Trace additional documentary counts and estimate arithmetic without fitting."""
from pathlib import Path
import csv, collections, json, re, hashlib
BASE=Path(__file__).resolve().parent
P=BASE/'delivered_9035df0/p_konum_plus'
E=BASE/'audit_evidence'
def rows(name):
    with (P/'calibration'/name).open(encoding='utf8',newline='') as f:return list(csv.DictReader(f))
err=P/'calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log'
lines=err.read_text(encoding='utf8',errors='replace').splitlines()
warning_lines=[x for x in lines if re.search(r'\b\w*Warning:',x)]
warnings=collections.Counter(re.search(r'\b(\w*Warning):',x)[1] for x in warning_lines)
family=rows('f3_step2_telemetry_rp1_2026-10-02.csv')
spl=rows('f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv')
cost=[]
for sex in ('F0','M0'):
    fr=[r for r in family if r['fixture']=='SCEN-A' and r['fitter'] in ('P-01','P-02') and r['mask_id'].startswith('run1:'+sex+':')]
    sr=[r for r in spl if r['fixture']=='SCEN-A' and r['mask_id'].startswith('run1:'+sex+':')]
    fw=sum(float(r['wall_clock_seconds']) for r in fr)
    sw=sum(float(r['wall_clock_seconds']) for r in sr)
    cost.append(dict(sex=sex,family_rows=len(fr),starts_by_family={f:sorted(set(r['start_id'] for r in fr if r['fitter']==f)) for f in ('P-01','P-02')},family_seconds=fw,spline_rows=len(sr),spline_seconds=sw,total_seconds=fw+sw))
scaled=435*cost[0]['total_seconds']+471*cost[1]['total_seconds']
answer={'delivered_stderr':{'path':str(err.relative_to(P)),'sha256':hashlib.sha256(err.read_bytes()).hexdigest(),'lines':len(lines),'warning_records':len(warning_lines),'warning_types':dict(warnings)},'rp1_SCEN_A_cost':cost,'sex_split_scaled_seconds':scaled,'sex_split_scaled_hours':scaled/3600,'sex_split_scaled_days':scaled/86400,'new_scaling_from_asserted_1_65h':{'hours':906*1.65,'days':906*1.65/24,'measurement_basis':'X: per-trajectory section timestamps are not delivered'},'capture_count_probe_limitation':'Both-files-have-2 probe is hypothetical; the real frozen baseline has 1/1/8 captures. Normalized-list equality preserves this cardinality. It is not evidence of a count defect against that pinned baseline.'}
(E/'additional_checks.json').write_text(json.dumps(answer,indent=2),encoding='utf8')
print(json.dumps(answer,indent=2))

```


### audit_finalize.py
```python
"""Finalize independent audit after the unchanged child process ends.

No source-repository mutation, harness mutation, real-data read, or optimizer call.
"""
from pathlib import Path
import json, csv, hashlib, datetime, subprocess, sys, collections, pickle, re, os
BASE=Path(__file__).resolve().parent;E=BASE/'audit_evidence';P=BASE/'delivered_9035df0/p_konum_plus';R=BASE/'rerun_9035df0/p_konum_plus'
AUDITOR_STATUS=json.loads((E/'rerun_status.json').read_text(encoding='utf8'))
R=Path(AUDITOR_STATUS['root'])/'p_konum_plus'
AUDITOR_LAUNCH=AUDITOR_STATUS['launch']
STDOUT_NAME=f'f3_step2_rp1-r1_launch{AUDITOR_LAUNCH}_stdout_2026-10-05.log'
STDERR_NAME=f'f3_step2_rp1-r1_launch{AUDITOR_LAUNCH}_stderr_2026-10-05.log'
H='calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py'
def j(path):return json.loads(path.read_text(encoding='utf8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def csvrows(path):
    with path.open(encoding='utf8',newline='') as f:return list(csv.DictReader(f))
def pretty(obj):return json.dumps(obj,indent=2,ensure_ascii=False)

def readlog(path):
    raw=path.read_bytes()
    if raw.startswith((b'\xff\xfe',b'\xfe\xff')):return raw.decode('utf16')
    try:return raw.decode('utf8')
    except UnicodeDecodeError:
        import locale
        return raw.decode(locale.getpreferredencoding(False))
def main():
    status=j(E/'rerun_status.json');assert status.get('state')=='FINISHED', 'Never finalize a live rerun'
    static=j(E/'static_checks.json');probes=j(E/'probe_checks.json');plan=j(E/'derived_plan.json');setup=j(E/'setup.json')
    delivered=j(P/'calibration/f3_step2_results_rp1-r1_2026-10-05.json')
    outcome={'exit_code':status['exit_code'],'harness_unchanged':sha(R/H)==sha(P/H),'s_differences':[], 'mandatory_failures':[]}
    ownpath=R/'calibration/f3_step2_results_rp1-r1_2026-10-05.json'
    # A copied executor results file must NEVER be mistaken for this run's output.
    own=None
    if ownpath.exists():
        try:
            candidate=j(ownpath)
            if candidate.get('process',{}).get('pid')==status['pid']:own=candidate
        except (ValueError,OSError) as exc:
            outcome['results_read_error']=repr(exc)
    if own is not None:
        outcome['environment']=own['environment'];outcome['process']=own['process']
        ev=lambda d:{x['fixture_id']:x for x in d['evaluations']}
        outcome['evaluation_counts']=[len(delivered['evaluations']),len(own['evaluations'])]
        if len(ev(own))!=len(own['evaluations']):outcome['s_differences'].append('duplicate_evaluation_fixture_id')
        for fid in sorted(set(ev(own))|set(ev(delivered))):
            if ev(own).get(fid)!=ev(delivered).get(fid):outcome['s_differences'].append('evaluations.'+fid)
        if sorted(json.dumps(x,sort_keys=True) for x in own['stops'])!=sorted(json.dumps(x,sort_keys=True) for x in delivered['stops']):outcome['s_differences'].append('stops')
        for k in ('run1_canonical_sha256','run2_canonical_sha256','determinism'):
            if own[k]!=delivered[k]:outcome['s_differences'].append(k)
        residual=R/'calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json'
        outcome['residual_sha256']=sha(residual)
        if sha(residual)!=static['scientific_delivered']['residual_hash']:outcome['s_differences'].append('residual_series')
        # Derive mandatory names from the delivered source constant via AST.
        import ast
        tree=ast.parse((P/H).read_text(encoding='utf8'))
        mandatory=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='MANDATORY_TESTS' for t in n.targets)))
        outcome['mandatory_count']=len(mandatory)
        outcome['mandatory_failures']=[t for t in mandatory if own['tests_run'].get(t)!={'ran':True,'passed':True}]
        outcome['tests_run']=own['tests_run'];outcome['nonregression']=own['nonregression_vs_r4_2']
        canonical_document=dict(evals=own['evaluations'],stops=own['stops'],pins=dict(mask_full=own['tests_run']['PIN-MASKED-OBJECTIVE']['passed'],fs=own['tests_run']['PIN-FEATURE-START-MASKED']['passed']))
        outcome['recomputed_canonical_sha256']=hashlib.sha256(json.dumps(canonical_document,sort_keys=True).encode('utf8')).hexdigest()
        if outcome['recomputed_canonical_sha256']!=own['run1_canonical_sha256']:outcome['s_differences'].append('canonical_document_recomputation')
        forbidden=lambda x:('data/raw/' in x.replace('\\','/').lower() or 'f1_eligible_trajectory_manifest_2026-08-28.csv' in x or 'f1_input_hash_table_2026-08-28.csv' in x)
        outcome['opened_forbidden']=[x for x in own['opened_files_audit_derived'] if forbidden(x)]
        # These are the auditor's own fresh-process store bytes, never executor pickles.
        manifest=csvrows(R/'calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv')
        delivered_manifest=csvrows(P/'calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv')
        own_keys={r['path'] for r in manifest};delivered_keys={r['path'] for r in delivered_manifest}
        store_dir=R/'calibration/.rp1-r1_restart_store_2026-10-05'
        mismatches=[];replay_records=collections.defaultdict(list);family_telemetry=[]
        for row in manifest:
            path=store_dir/row['path']
            if not path.is_file():
                mismatches.append('missing:'+row['path']);continue
            if sha(path)!=row['sha256'] or path.stat().st_size!=int(row['size_bytes']):mismatches.append(row['path'])
            name=row['path']
            if '__tstoreread_' in name or '__f1handoff__onestart_' in name:
                with path.open('rb') as f:payload=pickle.load(f)
                if payload['pid']!=status['pid']:mismatches.append('writer_pid:'+name)
                if '__f1handoff__onestart_' in name:family_telemetry.extend(payload['value'][2])
                else:
                    scope='cold' if '__tstoreread_cold__' in name else 'warm'
                    replay_records[scope].extend(payload['value'][6])
        per=csvrows(R/'calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv')
        reads=csvrows(R/'calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv')
        def normalized_record(r):
            # CSV scalar values must match the source payload's actual values.
            return {k:('' if v is None else str(v)) for k,v in r.items() if k!='source'}
        replaycheck={}
        for scope in ('cold','warm'):
            rr=[x for x in per if x['source']=='replay' and x['phase']=='t_store_read_accounting']
            expected=replay_records[scope]
            expected_counts=collections.Counter(json.dumps(normalized_record(x),sort_keys=True) for x in expected)
            rr_counts=collections.Counter(json.dumps(normalized_record(x),sort_keys=True) for x in rr)
            multiplicity=1 if scope=='cold' else 2
            # Same values exist in both scopes; compare the whole global replay multiset separately below.
            replaycheck[scope]={'stored_call_rows':len(expected),'global_contains_at_least_declared_copies':all(rr_counts[k]>=multiplicity*v for k,v in expected_counts.items())}
        expected_global=[*replay_records['cold'],*replay_records['warm'],*replay_records['warm']]
        actual_global=[r for r in per if r['source']=='replay']
        expected_counter=collections.Counter(json.dumps(normalized_record(x),sort_keys=True) for x in expected_global)
        actual_counter=collections.Counter(json.dumps(normalized_record(x),sort_keys=True) for x in actual_global)
        outcome['own_store']={'units':len(manifest),'manifest_byte_failures':mismatches,'pids':sorted(set(r['pid'] for r in manifest)), 'percall_rows':len(per),'sources':dict(collections.Counter(r['source'] for r in per)),'read_rows':len(reads),'replay_matches_actual_stored_records':expected_counter==actual_counter,'replay_scope_checks':replaycheck,'handoff_family_optimizer_rows_recovered_from_own_store':len(family_telemetry),'handoff_family_wall_seconds':sum(float(r.get('wall_clock_seconds',0)) for r in family_telemetry),'handoff_family_stage_counts':dict(collections.Counter(r.get('optimizer_path','UNKNOWN') for r in family_telemetry))}
        outcome['accounting_failures']=[]
        outcome['own_store']['missing_planned_keys']=sorted(delivered_keys-own_keys)
        outcome['own_store']['unexpected_keys']=sorted(own_keys-delivered_keys)
        if own_keys!=delivered_keys:outcome['accounting_failures'].append('independently_verified_planned_keys')
        if len(own_keys)!=len(manifest):outcome['accounting_failures'].append('duplicate_manifest_key')
        if len(manifest)!=67313:outcome['accounting_failures'].append('expected_67313_units')
        if mismatches:outcome['accounting_failures'].append('stored_byte_or_pid_mismatch')
        if outcome['own_store']['pids']!=[str(status['pid'])]:outcome['accounting_failures'].append('manifest_writer_pid')
        if len(reads)!=730:outcome['accounting_failures'].append('expected_730_reads')
        if expected_counter!=actual_counter:outcome['accounting_failures'].append('replay_vs_actual_stored_rows')
        # Procedure §3.5: row presence and classifications must be compared independently.
        nr=lambda root:{r['path']:r for r in csvrows(root/'calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv')}
        da,db=nr(P),nr(R)
        outcome['nonreg_csv_row_or_class_differences']=[k for k in sorted(set(da)|set(db)) if k not in da or k not in db or da[k]['classification']!=db[k]['classification']]
        outcome['nonreg_csv_rows']=[len(da),len(db)]
    else:
        log=(R/'calibration'/STDOUT_NAME).read_text(encoding='utf8',errors='replace')
        err=(R/'calibration'/STDERR_NAME).read_text(encoding='utf8',errors='replace')
        outcome['stop_stdout_tail']=log.splitlines()[-12:];outcome['stop_stderr_tail']=err.splitlines()[-20:]
        outcome['not_performed_reason']='Unchanged harness did not write results attributable to auditor pid '+str(status['pid'])+'; copied executor results excluded.'
        outcome['partial_scientific_log_evidence']={}
        for number in (1,2):
            values=re.findall(r'^RUN'+str(number)+r'_CANONICAL_SHA256 = ([0-9a-f]{64})$',log,re.M)
            if values:
                outcome['partial_scientific_log_evidence']['run'+str(number)]=values[-1]
                if values[-1]!=delivered['run1_canonical_sha256']:outcome['s_differences'].append('partial_run'+str(number)+'_canonical')
        gate=re.findall(r'^NONREGRESSION_VS_R4_2 s_findings=(\d+) e_declared=(\d+) u_findings=(\d+)$',log,re.M)
        if gate:
            outcome['partial_scientific_log_evidence']['nonregression_counts']=list(map(int,gate[-1]))
            if int(gate[-1][0]):outcome['s_differences'].append('partial_nonregression_S_findings')
        if 'NONREGRESSION_R4_2_WRITTEN = ' in log:
            partial=csvrows(R/'calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv')
            outcome['partial_nonregression_finding_rows']=[r for r in partial if r['classification'] in ('S_FINDING','U_FINDING')]
    outcome['source_repository_status']=subprocess.check_output(['git','-C',str(BASE/'repo'),'status','--porcelain'],env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')).decode()
    (E/'rerun_comparison.json').write_text(pretty(outcome),encoding='utf8')
    generate_report(status,setup,static,probes,plan,outcome,delivered,own)

def generate_report(status,setup,static,probes,plan,outcome,delivered,own,*,write_delivery=True):
    # IDs are local to this independent audit, not PI decisions or executor classes.
    findings=[
      ('IR1-01','gate-specific blocker','B','CLOSED (current-list byte correction only)','provenance/f3_realdata_prep_rp1-r1_transmission_list_2026-10-05.md:37','[A] Wrong report hash and false OBSERVED claim; [X] invention mechanism is executor disclosure. Current r1 has the correct named-file hash and sidecar. Historical B(iii) custody defect; correction independently verified.','Preserve superseded list; use corrected r1. This closes the mismatch, not the historical process claim.'),
      ('IR1-02','gate-specific blocker','B','OPEN','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:2118','[A-S] Removing real_x or real_mask_ids from an F1 scenario produces TypeError, not F1ContractGap. Only four legacy fields are guarded; real-mode intake requirements are omitted. R-1(iii) remains unmet.','Require the real-mode fields and test their named F1ContractGap outcomes without changing the synthetic path.'),
      ('IR1-03','gate-specific blocker','B','OPEN','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:2142','[A] mid() builds the ID at 2146 and f1_context_id_table builds it independently at 3001. Matching literals and a passing current set comparison do not supply the ONE builder required by R-1(ii).','Introduce one shared ID builder used by both consumers; independently verify the diff and unchanged S objects.'),
        ('IR1-04','gate-specific blocker','B','OPEN','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:2944','[A] Reproduction gate compares sorted (sex,name) tuples, not the frozen 14-column eligible-manifest bytes. The changed-manifest test removes one tuple at 3326; it does not change one byte. No synthetic hash-table or eligible-manifest deliverable is exported. R-1(iv) and §7 remain unmet.','Implement the frozen manifest schema/serialization and byte comparison; deliver synthetic tables and generator with sidecars; test one-byte change and missing/extra/hash-change cases.'),
      ('IR1-05','gate-specific blocker','B','OPEN','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:3065','[A] z_qc_pass and gate_pass retain literal ok=True at 3065/3072 inside the loader test changed by this package. R-2 explicitly covers all cases of this test. Delivered got=True does not make the assertion computed.','Set each ok from its observed got and expectation; verify every loader branch. The exact partial denominator now correctly compares 21146 to 21146.'),
      ('IR1-06','gate-specific blocker','B','OPEN','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:5463','[A] Recursive flattening stops at declared dictionaries, including MAY_DIFFER counter maps and atomic test blocks. This is not every-leaf full depth. Capture counts 8/1/1 are declared in reasons and preserved by normalized list equality against the pinned baseline. CSV at 5638 drops kind, held, and a declaration ID. R-3 deliverable and gate requirements remain unmet.','Compare/report leaves with exact declarations and retain declaration ID/kind/held in every relevant CSV row including equal declared fields.'),
      ('IR1-07','gate-specific blocker','B','OPEN','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:5514','[A-S] a_val==b_val continues before expectation evaluation. Wrong equal COUNT values and an ADDITION already present in both files both return zero U findings. B(iii): the required gate is not enforced.','Evaluate declared expectations even on equal values; traverse declarations absent from both documents; verify failure cases without changing the S comparison.'),
      ('IR1-08','cleanup','K','OPEN; before dependent computation','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:5446','[A-S] A changed exception raise location is accepted after the whole traceback is removed. Actual delivered traces differ by path AND verified unchanged-line shifts; source-line mapping shows no present semantic stack change. The current comparator nevertheless hides future stack changes.','Normalize only verified path/source-coordinate changes and compare the remaining traceback; preserve frame/function/statement identity.'),
      ('IR1-09','cleanup','K','OPEN; before dependent computation','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:3544','[A-S] The aggregate test requires cold.fit1_reads==0 although the helper allows a valid read from a prior process. Simulating both helpers passing with 146 resumed reads makes the aggregate fail. R-5 says first fit need not be fresh.','Remove the fresh-first assumption while preserving independently verified cold/warm coverage and replay-versus-stored checks.'),
      ('IR1-10','cleanup','K','OPEN; before dependent computation','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:4181','[A] Coarse nrgates_all/unittests_all/realscen replay paths append saved rows without changing source to replay (also 4312,4407). Only fine splmode replay was repaired. A restart can therefore label stored optimizer rows fresh.','Apply replay provenance consistently to every cache restoration path and verify the three coarse paths.'),
      ('IR1-11','cleanup','K','OPEN; before dependent computation','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:4211','[A] Handoff optimizer rows carry nr_gates rather than a handoff phase. _key_family at 235 omits f1handoff__, so code-produced family display is f1handoff instead of onestart/splmode. Both fixes change code-produced records and cannot be T under D-11 §5.','Use accurate phase and family attribution; independently check accounting and non-regression after the code correction.'),
      ('IR1-12','gate-specific blocker','B','OPEN','calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py:3225','[A] Handoff discards run_real_scenario returned family telemetry. Independent plan matches all 47706 handoff start-unit identities, but delivered bytes cannot reconcile their actual primary/fallback optimizer records or timing. §9(6) full computation accounting is not established.','Deliver phase/key-linked family telemetry, including start and optimizer-call counts, fallback events, fresh/replay identity, and section timing. Manifest-level count equality alone is insufficient for optimizer-level accounting.'),
      ('IR1-13','gate-specific blocker','B','OPEN','provenance/f3_realdata_prep_rp1-r1_attempt_log_2026-10-05.md:85','[A] A 9h44 standalone pre-verification is disclosed outside the two primary attempts. [X] Its executed code hash, launch/custody record, output paths, and evidence excluding its outputs from deliverables/attempt-2 store are not supplied. Audit §5.7 cannot be satisfied. No scientific difference or real-data access is inferred from this absence.','Supply the original code/custody/launch/output records and trace segregation. PI addresses the missing custody evidence; do not reconstruct or invent it.'),
      ('IR1-14','cleanup','T','OPEN','provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md:125','[X] Historical transport ZIP bytes and deleted dry-copy custody bytes are absent. The 108-occurrence self-scan has 106 independently traceable occurrences, one known historical mismatch, and one deleted custody value that remains unverified; 107 verified is not established.','Correct verification wording; provide originals if verification is required. Mark unavailable values X, never verified.'),
      ('IR1-15','cleanup','T','OPEN','calibration/f3_step2_class_c_pin_register_rp1-r1_2026-10-05.md:77','[A] Register states 8895 handoff SPL rows; delivered per-call CSV has 9223 (all F3-REAL). Inventory states 11 upstream files while listing 12. Report says the external W-3 writer verified 31 preconditions; its INSTR list has 20 (the harness separately verifies 31). The estimate says 42k+ warning records; delivered stderr contains 33013 warning records (66026 lines), including 28 RuntimeWarnings. The older SCEN-A estimate describes full banks, but its family telemetry comes from MINI_BANK; this scope mismatch must be disclosed.','Correct the narrative counts from named bytes; do not edit the historical records in this audit.'),
      ('IR1-16','cleanup','T','OPEN','calibration/f3_step2_rp1-r1_harness_diff_vs_rp1_2026-10-05.diff:356','[A] Both patches apply exactly to the delivered target, but labels are generated by keyword matches. Hunks 11–16 change family arguments to mid() and are falsely described as header/comment-only S5-WIRING; 19 changes ID construction (R-1), and 20 changes denominator comparison (R-2). The vs-r4-2 C-3 hunk includes R-1/R-2 changes.','Relabel the actual changes and split mixed-purpose hunks so each maps to one authorized item. Code scope itself is traceable; annotation repair is a record change.'),
      ('IR1-17','cleanup','T','OPEN','provenance/f3_realdata_prep_rp1-r1_start_state_inventory_2026-10-05.md:90','[A] First ledger omits the already-known deferred F1 input-table sidecar item. Record-only rows use OPEN→closes on delivery rather than the instruction’s pending-verification status. New code-produced display issue is later classified T.','Carry every item with class, closure point, and consistent status; use K for code-produced record corrections. Auditor closure remains item by item.'),
      ('IR1-18','cleanup','K','OPEN; procedure correction before reuse','calibration/_w3_writer_rp1-r1_tmp.py:52','[A-S] Unchanged writer sets first launch number from ATTEMPT_NUMBER=2. Auditor procedure requests first auditor launch 1; own custody thus incorrectly says first launch=2 while actual launch=1. Harness accepts it because it checks hashes/fingerprint, not that declaration.','Have the external writer record the actual intended launch and verify it. This audit preserves the delivered writer and discloses its incorrect field.'),
      ('IR1-19','cleanup','T','OPEN','calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-05/SYNTH_FIXTURE_MANIFEST.json:2','[A] 1021 added synthetic .txt files have neither individual sidecars nor per-file hashes in the manifest (filenames only). Their generator and actual disjointness are independently checked, but audit §1.1’s explicit reason for omitting each sidecar is absent.','State the package’s manifest-based custody exception explicitly or supply per-file hashes/sidecars. Preserve the delivered fixtures.'),
    ]
    if outcome['s_differences']:
        findings.append(('IR1-S','gate-specific blocker','STOP','OPEN; PI required','calibration/f3_step2_results_rp1-r1_2026-10-05.json:1','[A-S] Auditor S differences: '+', '.join(outcome['s_differences']),'D-11 §5 STOP: report to PI. No environment explanation, lowering, or scientific resolution by auditor.'))
    if own is None or status['exit_code']!=0 or outcome['mandatory_failures']:
        findings.append(('IR1-RUN','gate-specific blocker','B','OPEN','auditor launch1 logs','[A-S] Rerun did not finish all mandatory tests cleanly; see exact stop/output and exit code in §3.','Investigate the unchanged harness failure in the authorized PI process; do not edit this audit’s harness to proceed.'))
    if own is not None and outcome['nonreg_csv_row_or_class_differences']:
        findings.append(('IR1-NRCSV','gate-specific blocker','B','OPEN','auditor nonregression CSV','[A-S] Procedure §3.5 row-presence/classification differences: '+str(outcome['nonreg_csv_row_or_class_differences']),'Report the U-class procedure artifact difference; independently trace the rows.'))
    if own is not None and outcome.get('opened_forbidden'):
        findings.append(('IR1-FW','global blocker','STOP','OPEN; PI required','auditor opened_files_audit_derived','[A-S] Forbidden paths observed: '+str(outcome['opened_forbidden']),'D-11 firewall STOP; report to PI.'))
    if own is not None and outcome.get('accounting_failures'):
        findings.append(('IR1-ACCT','gate-specific blocker','B','OPEN','auditor own store and read records','[A-S] Independent accounting check failures: '+str(outcome['accounting_failures']),'Trace the unchanged-run records and payloads; do not accept an unreconciled count or replay comparison.'))
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    parts=['# F3 rp1-r1 independent technical audit — GPT-6 / Codex — DRAFT r1',
      '\n## Identity and prior exposure\n',
      f'[A-S] Auditor: Codex, based on GPT-6; exact deployment/model variant is not exposed in this session. Session identification: workspace `{BASE}`, start `{setup["time"]}`, independent harness pid `{status["pid"]}`. This session did not draft or execute the executor’s rp1/rp1-r1 packages and had no project exposure earlier in the provided conversation. It read historical audit material as input during this audit; no claim is made about model training exposure. No subagents were used. Audit completed at {now}.',
      '\n## Verdict\n',
      '**NOT PASSED.** [A]/[A-S] Open B findings affect R-1, R-2, R-3, custody and accounting; K items on dependent code remain open. The current list’s historical hash mismatch is corrected and independently closed as IR1-01. A matching full rerun does not close defects in the gates. This report does not bind bytes, declare QUALIFIED/READY, or decide for the PI.',
      '\nEvidence tiers: [A] checked on delivered commit bytes; [A-S] independently executed/measured in this audit; [X] executor/process-history claim not independently verified. Every negative determination below uses these tiers; absence of evidence is not an inferred scientific difference.',
      '\n## Custody (§1)\n',
      f'[A-S] Audit instruction SHA256: `82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e`, equals supplied sidecar. Source working tree was clean at HEAD `{setup["source_head"]}`. Audited target is exclusively `9035df0831d8646cca7f1e73937161a3d2d7d018`, extracted using Git object reads without checkout/commit/push. Later addendum bytes at HEAD are outside this audit’s governing commit.',
      '[A] Parent diff b6d2483→9035df0: 1104 additions, all under p_konum_plus, no modified/deleted parent file. 63d4846→9035df0: exactly four additions (r1 list, disclosure, their sidecars). There are 38 added sidecars (36 at 63d4846 plus two), all correct. Both lists’ tables differ only in report hash and self-reference rows. The 33 current-list file/standing pins all match their named file bytes and sidecars; the list itself is pinned by its external sidecar, without a self-hash. The rp1 table’s 43 file rows all match. The report’s 29 full-hash file rows match. Three new standing sidecars are correct; F1 input-table sidecar stays deferred and was not created.',
      '[A] Named dispatch/standing pins, reused generator/manifest, r4-2 baseline files, and previous inventory are independently hashed; start inventory previous hash is a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d. [A-S] Own W-3 wrote successfully and the unchanged harness verified custody/fingerprint and all 31 dispatch pins. [A] No committed restart store or transport ZIP is delivered. Store manifest/read log are record evidence, not direct verification of absent executor pickle payloads.',
      '[A-S] Limited hash-column read only: 217 F1 input hashes; 1023 synthetic fixture files (1021 .txt plus manifest and sidecar), 298 distinct synthetic hashes, zero intersection. Neither eligible manifest nor any named real input was opened. [A] Helper and nine quarantined outputs are preserved; the raw-fixture sidecar exception lacks the explicit rationale requested by §1.1 (IR1-19).',
      '[A] Expanded hash trace checks reproduce 108 full-hash occurrences in the original eight executor documents and 148 when r1 is added. Matching against an arbitrary file was used only to locate candidates; each named-file association was then checked with source context, report/list tables, dispatch aliases, baseline names and preserved attempt outputs. 104 original occurrences match named files, two canonical hashes were recomputed from evaluations/stops/pins, one is the disclosed historical mismatch, one is deleted dry custody [X]. Current r1 has no incorrect current named-file pin; wrong hash occurs only in its erratum and the superseded row. Generating-script-at-write-time provenance cannot be established from hash equality alone. ZIP/dry custody remain [X], not verified (IR1-14).',
      '\n## Code (§2)\n',
      '[A] Final harness SHA256 cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb equals attempt-2 W-3 pin. Both delivered diffs independently applied to their pinned rp1/r4-2 baselines reproduce the target exactly, with 36 labelled hunks each. Python difflib chooses different blank-line context than GNU diff; applying and verifying every old/context line establishes content equality without treating that formatting difference as a mismatch.',
      '[A] Consumer changes take loader arrays, create family-qualified IDs, and guard scenario intake; fitting/evaluator arithmetic outside this intake is unchanged. All six mid() call changes concern IDs and satisfy PI-c scope; their S5-WIRING annotations are inaccurate. Independent hunk mapping and annotation deficiencies are in the appendix and IR1-16. No unauthorized scientific literal change was found in these diffs.',
      '[A]/[A-S] Attempt1→2 executable changes consist of supersession/attempt metadata plus three R-3 changes. (a) COUNT double-canonicalization is a representation defect correction: declared transition is unchanged. (b) Removing bare exc_injection_fixtures restores recursion and the existing leaf ADDITION; undeclared differing leaves still become U, so this does not relax the content gate. Only that EXPECTATIONS_E entry was removed; the three capture EQUAL entries remain. (c) Extending provenance stripping to three capture lists removes false pid/time differences but strips entire traceback, a gate relaxation broader than safe path normalization (IR1-08). Actual paths-only normalization is unequal; mapping verified unchanged source lines makes all three lists equal across all three pairs. Thus no present change in exception-raising statements is observed, while the gate still permits one.',
      f'[A] EXPECTATIONS_E has {probes["declaration_count"]} exact string keys with kinds {probes["declared_kind_counts"]}; capture multiplicities are explicitly declared as 8/1/1 in reasons and enforced by normalized-list equality against the pinned baseline. “Exact path” keys nevertheless stop dictionary recursion and can cover subtrees. Existing r4-2 tests retain equal ran/passed in delivered results; mandatory-count check and independent rerun comparison follow below. IR1-06/07 prevent closure of RP1A-03.',
      '\n## Re-execution and environment (§3)\n',
      f'[A-S] Unchanged harness ran with F3_REPO_ROOT={status["root"]}, F3_RP1R1_LAUNCH={status["launch"]}, all three thread pins=1. Both executor custody records and their sidecars were moved outside p_konum_plus; store was absent at launch. Delivered metadata/code only was copied; the two real F1 manifests and all external real data were omitted. Writer exit=0; harness pid={status["pid"]}, start={status["harness_started"]}, finish={status["finished"]}, exit={status["exit_code"]}. Copied executor outputs were excluded unless their process.pid equals the auditor pid. The writer hardcodes first launch=2: incorrect for auditor launch1 (IR1-18), coincidentally equal for launch2. No writer/harness edit was made.',
      '| field | binding/executor | auditor | difference |\n|---|---|---|---|']
    env=outcome.get('environment',dict(setup['environment'],OMP='1',OPENBLAS='1',MKL='1'))
    for k in ('platform','python','numpy','scipy','OMP','OPENBLAS','MKL'):
        ref=delivered['environment'][k];obs=env[k];parts.append(f'| {k} | {ref} | {obs} | {"none" if ref==obs else "DIFFERENT"} |')
    if status.get('previous_auditor_launch'):
        previous=status['previous_auditor_launch']
        parts.append('[A-S] Auditor launch1 stopped early with observed exit1 at '+previous['finished']+' after approximately44 minutes. Its parent runner did not record completion; the independent monitor observed the child exit. The logs contain no Python traceback or reported scientific STOP at that point; the termination cause is not established. The initial partial DRAFT r1 and SHA256 remain preserved; this report supersedes that partial audit output. Launch2 used a new disposable root and EMPTY store, preserving the original root, all original store units, logs, status and prior report. Both auditor harness invocations used the unchanged delivered source. Previous status/evidence: '+pretty(previous)+'; evidence snapshot '+status['previous_evidence']+'. The second runner was launched independently with hidden Start-Process, rather than attached to a foreground tool session.')
    if own is not None:
        parts += [f'\n[A-S] Independent S comparison: {len(own["evaluations"])} objects; differences={outcome["s_differences"]}. RUN1={own["run1_canonical_sha256"]}; RUN2={own["run2_canonical_sha256"]}; determinism={own["determinism"]}; residual={outcome["residual_sha256"]}. Mandatory tests: {outcome["mandatory_count"]}, failures={outcome["mandatory_failures"]}. Frozen-baseline gate: {pretty(outcome["nonregression"])}.',
        f'[A-S] Auditor versus executor NR CSV path/class comparison: rows {outcome["nonreg_csv_rows"]}, row/class differences={outcome["nonreg_csv_row_or_class_differences"]}. Values containing pid, paths and wall time differ by declared provenance and are retained in own outputs. S equality is required regardless of environment. {"STOP is reported to PI; no resolution applied." if outcome["s_differences"] else "No S STOP was observed."}']
    else:parts += ['[A-S] Procedure stopped before an auditor results document was written. Exact stdout/stderr tail and exit code are in the output appendix. Remaining mandatory tests, full S comparison, and CSV comparison are NOT PERFORMED for that reason. No edit was made to proceed.']
    parts += ['\n## Non-regression and accounting (§4)\n',
      '[A] Delivered CSV has 2115 rows (1 S, 2114 E), columns path/classification/reason/r4_2/rp1. There is no declaration ID or held field; kind/held were calculated internally and discarded. Equal declared fields are not printed. Results and test evidence use declared subtree stop points rather than every-leaf recursion. IR1-06/07 therefore apply despite reported s=0/u=0. Scientific comparison is independently reconstructed: all 37 evaluations and stop records match r4-2; canonical hash recomputes to 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77; residual bytes hash to 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f.',
      '[A] Three stale end_state CSV values are a real ordering effect: T-NONREG-R4-2 has not yet been recorded when compared. Lines 5665 onward refresh tests_run, mandatory flags and completeness before writing results. Delivered final values are corrections_complete=true, mandatory_tests_all_run=true, mandatory_tests_missing=[]; the stale CSV values are not a final-results mismatch.',
      '[A-S] Independent plan derivation used frozen generator/start-grid and feature admissibility helpers only; no optimizer or algorithm×CVI evaluator was called. Enumerated all expected family start keys including conditional feature rejection, rather than copying register counts. Exactly 49787 expected onestart keys match the 49787 manifest keys: zero missing/unexpected. This comprises base 2081 and handoff 47706. Handoff: 48 P-01 contexts×731 grid starts +48 features; 48 P-02 contexts×261 grid starts +42 features (6 duplicate feature rejections) =47706.',
      '| scope/family | independently derived stored units | delivered manifest |\n|---|---:|---:|\n| base onestart | 2081 | 2081 |\n| base splmode | (2×2×8 + 2×(2×8−2) +4)×146 =9344 | 9344 |\n| realscen / nrgates_all / unittests_all | 4 /1 /1 | 4 /1 /1 |\n| excpass1 /excpass2 splmode | 3×146 each=438 each | 438 /438 |\n| handoff onestart /splmode | 47706 /6×8×146=7008 | 47706 /7008 |\n| cold /warm splmode | 146 each | 146 /146 |\n| total | 67313 | 67313 |',
      '[A] Store-read plan: cold fit2+verification=2×146=292; warm fit1+fit2+verification=3×146=438; total730. Log agrees, all writer/reader pid34588, no other scope. Per-call delivered rows: 22217=21725 fresh+492 replay; replay=164 cold fit2 +164 warm fit1 +164 warm fit2. Five T-STORE fits (cold2,warm3) each have164 optimizer records: 328 fresh+492 replay. Per-mode primary/fallback cardinality is conditional; optimizer rows and stored units are not interchangeable. Global phases nr_gates9283, unit_tests1602, run1/run2 each5256, t_store_read_accounting820. Handoff’s actual SPL count is9223 and optimizer time1523.6454776009778s, correcting register’s8895.',
      '[A]/[X] Executor replay-vs-payload equality is recorded by its tests but original payloads are not delivered; this audit does not pretend to read absent stores. [A-S] Auditor replay is compared to its actual stored bytes independently in the output appendix. Coarse replay source and real restart cold condition remain K defects even if the fresh rerun passes. The handoff phase error and key-family error are K, never T (IR1-11).',
      '[A] Missing handoff family rows do not prevent deriving and matching the start-unit plan. They do prevent full optimizer-event/timing accounting on delivered bytes: 47706 starts can take primary/fallback routes whose telemetry is discarded from exported records. This blocks the package accounting pass condition (IR1-12). A real-data instruction needs persistent per-phase/sex/trajectory/family/context/start/optimizer-stage records, fresh/replay provenance, counts by key family, and measured phase boundaries. No new fit/threshold rule is proposed. [X] ~10h handoff, ~95% family cost, 9h44 standalone elapsed and per-trajectory1.5–1.8h lack delivered timestamp evidence; only SPL1523.645s and total primary start/end interval are traceable. The ~3.6day/~62day extrapolations are informational estimates, not a proved range for real trajectories.',
      '\n## Item-by-item (§5)\n',
      '| item | independent result |\n|---|---|\n| R-1 handoff | [A] consumer uses real_x and family-qualified IDs; derived keys match loader arrays and all144 dry contexts. Shared builder, real-mode missing-field STOP and byte-manifest gate remain deficient (IR1-02–04). |\n| R-2 QC | [A] all21 delivered got/expected pairs agree; exact partial denominator21146 independently derived. Direct guard tests cover NaN/Inf, negative share, post-z nonfinite, std/norm; derivations recorded in register. Two constant ok cases remain (IR1-05). |\n| R-3 full comparison | [A]/[A-S] scientific bytes match; equality bypass, subtree stopping, CSV declaration reporting and traceback normalization remain open (IR1-06–08). |\n| R-4 isolation | [A-S] separate root/custody/store/output, unchanged source; own W-3 and dispatch checks passed; final execution comparison as §3. Writer first-launch field incorrect (IR1-18). |\n| R-5 source/accounting | [A] source exists; cold/warm rows under own phase; fine replay records consistent. Cold resume and coarse replay source defects remain (IR1-09/10); actual own payload check in appendix. |\n| R-6 records | [A] full key-field/register table, corrected realscen meaning, unit/call/read distinction, response rows and three sidecars delivered. Diff annotations and ledger wording need correction (IR1-16/17). |\n| Start inventory | [A] previous inventory hash correct; all carried rows identify class/closure/status; executor marks none of this package’s audit-only items CLOSED. Later deferred sidecar item omitted (IR1-17). |\n| Attempts/starts | [A] primary attempt1/launch1 pid34228 and attempt2/launch2 pid34588 supported by logs; precondition premature-copy event and deleted dry runs are [X]. Standalone pre-verification provenance missing (IR1-13). |\n| Firewall | [A] REAL_DATA_MODE=False asserted at each logged main start; delivered opened audit excludes real manifests/raw paths. [A-S] auditor own opened audit checked in §3/appendix. No algorithm×CVI computation performed in audit scripts. |',
      '\nF1 frozen operation mapping [A]: §8.1 steps1–2 → f1_load_raw_dir format/semantic/floor guards; step3 → national yob layout assumption (caller must supply national-only source, no independent state-file-content discriminator); step4 →1880–2025 annual axis; steps5–6 → full support and eligible filter; step7 → all-published-names denominator and _f1_share; step8 → duplicate/positive denominator/pre-z finite/nonnegative; step9 → zero-variance guard; step10 → mean/std ddof0 normalization; step11/§8.2 → f1_post_z_qc finite, mean,std,norm against1e-8. Freeze §7’s14-field manifest representation is not reproduced by f1_repro_gate. REAL_DATA_MODE guards this cycle; constants naming real manifests are never opened by the harness. Auditor’s separate hash-column read is expressly allowed by audit §0.',
      '\n## Ledger closure (§6)\n',
      '| item | auditor status | verified evidence / remaining reason |\n|---|---|---|\n| RP1A-01 | OPEN | handoff array intake verified, but IR1-02/03/04 leave required R-1 behavior missing |\n| RP1A-02 | OPEN | 21 observed outcomes agree; constant ok violates R-2 (IR1-05) |\n| RP1A-03 | OPEN | matching S does not establish the required full gate; IR1-06/07/08 |\n| RP1A-04 | OPEN | fine source/read records verified; coarse replay/cold restart/attribution defects IR1-09/10/11 |\n| RP1A-05 | OPEN | both informational lines delivered and scaling arithmetic independently checked; line 1 uses MINI_BANK despite the inherited full-bank description, and line 2 timing/family basis is not delivered (IR1-12/15); the claimed real-data interval is not established |\n| RP1A-06 | OPEN | sidecars/response rows/diff content verified, but one-item-per-hunk labels not accurate (IR1-16) |']
    rerun_clean=own is not None and status['exit_code']==0 and not outcome['s_differences'] and not outcome['mandatory_failures'] and not outcome.get('opened_forbidden') and not outcome.get('nonreg_csv_row_or_class_differences') and not outcome.get('accounting_failures')
    parts.append('| RP1A-07 | '+('CLOSED' if rerun_clean else 'OPEN')+' | '+('unchanged full rerun completed with matching S and all mandatory tests; independent isolation/custody comparison' if rerun_clean else 'unchanged rerun did not establish all required S/mandatory conditions')+'; writer record defect IR1-18 remains a separate K |')
    parts += ['| R42A-03 (b) | OPEN | independent fine read records and replay content checked; R-5 remains deficient on resumed cold test/coarse replay (IR1-09/10) |',
      '\nNew findings retain their own statuses below. The PI owns D-9 binding and A.5(iii) rule decision; neither is closed here. F1 input-table sidecar remains OPEN/T with closure at real-data step1, and no real-data sidecar was produced.',
      '\n## Findings table\n',
      '| id | v6 | D-11 §5 | status | file:line | evidence/reason | closure action |\n|---|---|---|---|---|---|---|']
    for f in findings:parts.append('| '+' | '.join(str(x).replace('|','\\|').replace('\n',' ') for x in f)+' |')
    parts += ['\nB assignments are under D-11 §5(iii): a package defect leaves a named gate precondition unmet. K assignments concern code/record production and close before dependent computation. T assignments are documentary corrections with code/outputs otherwise preserved. IR1-01 is historically B, corrected on current delivered list bytes. No class is lowered from an executor/PI assignment by this report; code-produced records previously called T are raised to K.',
      '\n## NOT PERFORMED\n',
      '- [X] Original standalone pre-verification code/custody/launch/path/output-segregation verification: original records absent.\n- [X] Deleted executor dry-copy custody hash and launches: bytes/logs absent.\n- [X] Original/rebuilt transport ZIP verification: neither ZIP supplied.\n- [X] Direct comparison of executor replay to executor pickle payloads: stores absent by delivery design; manifest/log checked as records.\n- [X] Generator script executing at transmission-list write time and premature-copy creation/deletion history: only post-event narrative supplied.\n- [X] Exact executor handoff/trajectory elapsed and95% family-cost attribution: timing/family telemetry absent.\n- Real-data reproduction/eligible-manifest/raw reads and algorithm×CVI execution: prohibited/out of scope; not attempted.']
    if own is None:parts.append('- Full auditor S/mandatory/NR comparisons NOT PERFORMED: '+outcome['not_performed_reason'])
    parts += ['\n## Scripts run and observed output\n',
      'Commands used the existing Python3.11.7 interpreter. Scripts are outside the source repository. Pure-function AST probes are independent diagnostic executions; they are not edited-harness reruns. The sole full-harness invocation used the original delivered source hash. Initial probe invocation failed on the auditor script’s invalid encoding spelling utf8-sig, corrected to utf-8-sig before the successful probe; no harness edit or optimizer occurred in that failed probe. Intermediate audit-script extraction/counting errors were corrected before relying on their results.',
      'Read-only setup commands: Get-FileHash/Get-Content on supplied instruction/sidecar; git status --porcelain, rev-parse, ls-tree, cat-file --batch, diff --name-status, and selected metadata/code reads. Derived outputs and scripts are embedded below, with raw-evidence file hashes for the larger files; no real raw file was read. Source final git status: '+repr(outcome['source_repository_status']),
      '\n### Setup output\n```json\n'+pretty(setup)+'\n```',
      '\n### W-3 output\n```text\n'+(E/'w3_stdout.log').read_text(encoding='utf8')+'\n```',
      '\n### Independent probes\n```json\n'+pretty(probes)+'\n```',
      '\n### Derived plan\n```json\n'+pretty(plan)+'\n```',
      '\n### Additional documentary checks\n```json\n'+pretty(j(E/'additional_checks.json'))+'\n```',
      '\n### Custody sidecar segregation\n```json\n'+pretty(j(E/'stale_custody_sidecars.json'))+'\n```',
      '\n### Static checks output\n```text\n'+readlog(E/'static_checks_stdout.log')+'\n```',
      '\n### Final rerun comparison\n```json\n'+pretty(outcome)+'\n```',
      '\n### All hash occurrence traces\n\n| document:line | full SHA256 | independently traced target/result |\n|---|---|---|']
    occurrences=j(E/'hash_occurrences_with_context.json')
    for row in occurrences:
        matches=row['matching_byte_paths'];h=row['hash'];doc=row['document']
        if not matches:
            target='[A-S] recomputed canonical document' if h.startswith('556106e7') else ('[A] historical wrong hash' if h.startswith('ebc28df8a94bd3b2cfe') else '[X] unavailable custody/ZIP bytes')
        else:
            source_line=(P/row['document']).read_text(encoding='utf8').splitlines()[row['line']-1]
            named=[p for p in matches if p.removeprefix('p_konum_plus/') in source_line or Path(p).name in source_line]
            target=named[0] if named else next((p for p in matches if 'rp1-r1' in p and 'quarantine' not in p),matches[0])
            target='[A] '+target
        parts.append(f'| {doc}:{row["line"]} | {h} | {target} |')
    parts += ['\n### Hunk mapping\n',
      '[A] Vs-rp1 independent mapping: 1 R-4; 2 §5 wiring; 3 R-1; 4 §5 wiring; 5 §9 wiring; 6 R-5; 7 R-1; 8 R-5; 9–19 R-1 (18 comment, 19 executable); 20–22 R-2; 23 R-1; 24 R-5; 25 §5 wiring (mode/launch guard); 26 §9 wiring; 27 R-1; 28 R-5; 29–31 §9 wiring; 32–36 R-3 (35/36 output/gate wiring for R-3). Delivered labels are preserved in static output; discrepancies are IR1-16.',
      '[A] Vs-r4-2 hunk families: 1 R-4; 2 §5 wiring; 3–5 C-2; 6 R-1; 7 §5 wiring; 8 §9 wiring; 9 C-6; 10 R-5; 11 R-1; 12–14 C-5; 15 R-5; 16 C-5 bookkeeping; 17 C-5; 18–25 R-1 ID intake/calls; 26 mixes C-3/R-1/R-2/R-5 and requires splitting; 27 C-2; 28 C-3; 29 mixes §9 wiring with new R-1/R-5 invocations and requires splitting; 30 R-1; 31 R-5; 32 C-1; 33/34 §9 wiring; 35 C-6; 36 mixes R-3 with new code-record/result fields and requires splitting. These annotations do not identify any new unauthorized science computation.',
      '\n### Recomputed attempt diff\n```diff\n'+readlog(E/'attempt1_to_attempt2.diff')+'\n```']
    for script in ('audit_completion_setup.py','audit_setup.py','audit_run.py','audit_run_detached.py','audit_checks.py','audit_probes.py','audit_plan.py','audit_additional_checks.py','audit_finalize.py','audit_monitor.py','audit_finalizer_check.py'):
        if (BASE/script).exists():parts += ['\n### '+script+'\n```python\n'+(BASE/script).read_text(encoding='utf8')+'\n```']
    rawfiles=list(E.glob('*.json'))+list(E.glob('*.tsv'))+list(E.glob('*.diff'))+list(E.glob('*.log'))
    rawfiles += [R/'calibration'/STDOUT_NAME,R/'calibration'/STDERR_NAME]
    parts += ['\n### Raw evidence file hashes\n\n| audit-relative file | bytes | SHA256 |\n|---|---:|---|']
    for path in sorted(rawfiles):
        if path.name not in ('delivery.json','completion_status.json','monitor_stdout.log','monitor_stderr.log','finalizer_stdout.log','finalizer_stderr.log'):parts.append(f'| {path.relative_to(BASE)} | {path.stat().st_size} | {sha(path)} |')
    stdout=R/'calibration'/STDOUT_NAME
    stderr=R/'calibration'/STDERR_NAME
    parts += ['\n### Unchanged harness stdout\n```text\n'+stdout.read_text(encoding='utf8',errors='replace')+'\n```',
              '\n### Unchanged harness stderr tail (complete file pinned above)\n```text\n'+'\n'.join(stderr.read_text(encoding='utf8',errors='replace').splitlines()[-24:])+'\n```']
    diffs=[k for k in ('platform','python','numpy','scipy','OMP','OPENBLAS','MKL') if env[k]!=delivered['environment'][k]]
    parts.append('\nPI line: D-9 §2(a) preconditions are **NOT MET**: '+('executor and auditor S objects match, but this independent audit is NOT PASSED' if rerun_clean else 'auditor S/mandatory equality is not fully established and this audit is NOT PASSED')+'; environment differences: '+(', '.join(diffs) if diffs else 'none across Windows platform, Python, NumPy, SciPy, OMP, OPENBLAS and MKL')+'. PI binding remains a separate decision.\n')
    content='\n\n'.join(parts)
    if not write_delivery:return content
    delivery=BASE/'audit_delivery';delivery.mkdir(exist_ok=True)
    report_date=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).date().isoformat()
    report=delivery/f'f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_{report_date}.md'
    if report.exists():
        report=delivery/f'f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r2_{report_date}.md'
        content=content.replace('— DRAFT r1','— DRAFT r2',1)
    # Audit transmission artifacts are created once, not restamped after a live run.
    with report.open('x',encoding='utf8',newline='\n') as f:f.write(content)
    digest=sha(report)
    with Path(str(report)+'.sha256').open('x',encoding='ascii',newline='\n') as f:f.write(digest+'  '+report.name+'\n')
    (E/'delivery.json').write_text(pretty({'report':str(report),'sha256':digest,'verdict':'NOT PASSED','finished':now}),encoding='utf8')
    print('AUDIT_REPORT_WRITTEN = '+str(report));print('SHA256 = '+digest)
if __name__=='__main__':main()

```


### audit_monitor.py
```python
"""Finish this audit after its unchanged harness exits; run hidden on Windows.

The monitor never launches another harness, edits delivered code, or reads real data.
"""
from pathlib import Path
import ctypes, ctypes.wintypes as wt, datetime, hashlib, json, os, subprocess, sys, time
BASE=Path(__file__).resolve().parent
E=BASE/'audit_evidence'
AUDITOR_STATUS=json.loads((E/'rerun_status.json').read_text(encoding='utf8'))
CAL=Path(AUDITOR_STATUS['root'])/'p_konum_plus/calibration'
STDOUT_NAME=f'f3_step2_rp1-r1_launch{AUDITOR_STATUS["launch"]}_stdout_2026-10-05.log'
kernel=ctypes.WinDLL('kernel32',use_last_error=True)
kernel.OpenProcess.argtypes=[wt.DWORD,wt.BOOL,wt.DWORD];kernel.OpenProcess.restype=wt.HANDLE
kernel.WaitForSingleObject.argtypes=[wt.HANDLE,wt.DWORD];kernel.WaitForSingleObject.restype=wt.DWORD
kernel.GetExitCodeProcess.argtypes=[wt.HANDLE,ctypes.POINTER(wt.DWORD)];kernel.GetExitCodeProcess.restype=wt.BOOL
kernel.CloseHandle.argtypes=[wt.HANDLE]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def readstatus():
    # Runner writes a very short JSON file; retry a partial concurrent write.
    for _ in range(20):
        try:return json.loads((E/'rerun_status.json').read_text(encoding='utf8'))
        except (OSError,ValueError):time.sleep(.1)
    raise RuntimeError('Cannot read runner status after retries')
def save(name,value):
    path=E/name;temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(value,indent=2),encoding='utf8');temp.replace(path)
def progress(state,status,detail=''):
    log=CAL/STDOUT_NAME
    lines=log.read_text(encoding='utf8',errors='replace').splitlines() if log.exists() else []
    count=sum(1 for p in (CAL/'.rp1-r1_restart_store_2026-10-05').glob('*.pkl'))
    text=('# Independent audit progress\n\n'
          f'State: **{state}**. Updated {now()}.\n\n'
          f'Target: `9035df0831d8646cca7f1e73937161a3d2d7d018`. '
          f'Unchanged harness PID: {status.get("pid")}; started {status.get("harness_started")}.\n\n'
          f'Currently {count} auditor store units. Latest stdout: `{lines[-1][:600] if lines else "none"}`.\n\n'
          'Static review identifies open B/K findings and supports **NOT PASSED**. '
          'Full rerun comparisons remain pending until the harness exits.\n\n'+detail+'\n')
    (E/'audit_progress.md').write_text(text,encoding='utf8')
def main():
    status=readstatus();handle=None
    if status.get('state')=='RUNNING':
        handle=kernel.OpenProcess(0x1000|0x100000,False,status['pid'])
        if not handle:raise ctypes.WinError(ctypes.get_last_error())
    save('completion_status.json',dict(state='MONITORING',monitor_pid=os.getpid(),started=now(),harness_pid=status.get('pid')))
    try:
        while status.get('state')!='FINISHED':
            progress('RUNNING',status)
            if handle and kernel.WaitForSingleObject(handle,0)==0:
                time.sleep(2);status=readstatus()
                if status.get('state')!='FINISHED':
                    code=wt.DWORD()
                    if not kernel.GetExitCodeProcess(handle,ctypes.byref(code)):raise ctypes.WinError(ctypes.get_last_error())
                    status.update(state='FINISHED',exit_code=code.value,finished=now(),exit_recorded_by='independent process monitor; runner did not record completion')
                    save('rerun_status.json',status)
                break
            time.sleep(30);status=readstatus()
        progress('FINALIZING',status)
        save('completion_status.json',dict(state='FINALIZING',monitor_pid=os.getpid(),harness_pid=status.get('pid'),time=now()))
        with (E/'finalizer_stdout.log').open('wb') as out,(E/'finalizer_stderr.log').open('wb') as err:
            done=subprocess.run([sys.executable,str(BASE/'audit_finalize.py')],cwd=BASE,stdout=out,stderr=err)
        if done.returncode:raise RuntimeError('Finalizer exit '+str(done.returncode)+'; see audit_evidence/finalizer_stderr.log')
        delivery=json.loads((E/'delivery.json').read_text(encoding='utf8'))
        report=Path(delivery['report']);digest=hashlib.sha256(report.read_bytes()).hexdigest()
        side=Path(str(report)+'.sha256')
        assert digest==delivery['sha256']==side.read_text(encoding='ascii').split()[0]
        save('completion_status.json',dict(state='COMPLETE',monitor_pid=os.getpid(),harness_pid=status.get('pid'),time=now(),report=str(report),sha256=digest,verdict=delivery['verdict']))
        (E/'audit_progress.md').write_text('# Independent audit completed\n\n**NOT PASSED.**\n\n'
            f'[Draft report]({report.as_posix()}) · [SHA256 sidecar]({side.as_posix()})\n\n'
            f'Rerun exit: {status["exit_code"]}. Finalized {now()}.\n\n'
            'The report contains the full rerun comparison, findings, ledger decisions, evidence and executed scripts.\n',encoding='utf8')
        print('AUDIT COMPLETE: '+str(report),flush=True)
    except Exception as exc:
        save('completion_status.json',dict(state='FINALIZER_ERROR',monitor_pid=os.getpid(),time=now(),error=repr(exc)))
        progress('FINALIZER_ERROR',status,'Error: '+repr(exc)+'. No audit-completion claim is made. See completion_status.json and finalizer_stderr.log.')
        raise
    finally:
        if handle:kernel.CloseHandle(handle)
if __name__=='__main__':main()

```


### audit_finalizer_check.py
```python
"""Check report-rendering branches using labeled simulation in memory only.

Does not change rerun status, create a deliverable, or claim the audit completed.
"""
from pathlib import Path
import json, copy, sys
sys.dont_write_bytecode=True
import audit_finalize as f
def j(name):return json.loads((f.E/name).read_text(encoding='utf8'))
status=dict(j('rerun_status.json'),state='FINISHED',exit_code=0,finished='SELF-CHECK SIMULATION ONLY')
delivery_before={str(p):f.sha(p) for p in (f.BASE/'audit_delivery').glob('*') if p.is_file()}
setup=j('setup.json');static=j('static_checks.json');probes=j('probe_checks.json');plan=j('derived_plan.json')
delivered=f.j(f.P/'calibration/f3_step2_results_rp1-r1_2026-10-05.json')
outcome={'s_differences':[],'mandatory_failures':[],'nonreg_csv_row_or_class_differences':[],'nonreg_csv_rows':[2115,2115], 'residual_sha256':static['scientific_delivered']['residual_hash'],'mandatory_count':38,'nonregression':delivered['nonregression_vs_r4_2'],'environment':delivered['environment'],'source_repository_status':''}
passed=f.generate_report(status,setup,static,probes,plan,outcome,delivered,delivered,write_delivery=False)
assert '**NOT PASSED.**' in passed and '| RP1A-07 | CLOSED |' in passed
assert '| RP1A-05 | OPEN |' in passed
assert all(('## '+x) in passed for x in ['Identity and prior exposure','Verdict','Custody','Code','Re-execution','Non-regression','Item-by-item','Ledger closure','Findings table','NOT PERFORMED','Scripts run'])
failed=dict(outcome,not_performed_reason='SELF-CHECK SIMULATION: no attributable output',stop_stdout_tail=['self-check'],stop_stderr_tail=['self-check'])
failure=f.generate_report(dict(status,exit_code=1),setup,static,probes,plan,failed,delivered,None,write_delivery=False)
assert '| RP1A-07 | OPEN |' in failure and 'IR1-RUN' in failure
diff=dict(outcome,s_differences=['SELF-CHECK S difference'],nonreg_csv_row_or_class_differences=['SELF-CHECK changed CSV row'],opened_forbidden=['SELF-CHECK forbidden path'],accounting_failures=['SELF-CHECK payload mismatch'])
stopped=f.generate_report(status,setup,static,probes,plan,diff,delivered,delivered,write_delivery=False)
assert all(x in stopped for x in ['IR1-S','IR1-NRCSV','IR1-FW','IR1-ACCT'])
assert delivery_before=={str(p):f.sha(p) for p in (f.BASE/'audit_delivery').glob('*') if p.is_file()}, 'A simulation must not change a deliverable'
checks={'kind':'in-memory rendering simulation; not rerun evidence','success_failure_STOP_branches':'PASS','success_render_characters':len(passed),'failure_render_characters':len(failure),'stop_render_characters':len(stopped),'real_rerun_state_unchanged':j('rerun_status.json')['state'],'deliverable_created':False}
(f.E/'finalizer_selfcheck.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
print(json.dumps(checks,indent=2))

```


### Raw evidence file hashes

| audit-relative file | bytes | SHA256 |
|---|---:|---|

| audit_evidence\additional_checks.json | 1952 | 39f2921db8038afe2b62e9e3fad22cb0a37a08a17d888f7edcaec4caddc6d050 |

| audit_evidence\additional_checks_stderr.log | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

| audit_evidence\additional_checks_stdout.log | 3910 | d485dca319d2cbc2957f74c0690a9e8bfe90d3304872579adb515ebc7d2a0583 |

| audit_evidence\attempt1_to_attempt2.diff | 6955 | 539a39101bde91c6d1633b98f0e24058e09ca28beea04d67e204f6b9c1149119 |

| audit_evidence\delivered_hashes.json | 407090 | c1de4c9d6666dc5563730330a38673b68ed8dc28210bea80a93ac2f45bd65a1b |

| audit_evidence\derived_plan.json | 2226 | 0366894be219b8c1ce2db74ea1ea10745bef85a5ebb34eb2b851cbd79a2c3773 |

| audit_evidence\f3_realdata_prep_rp1-r1_transmission_list_2026-10-05_table_checks.json | 10128 | 7c4fcc531d78dff1f7de61eb7d50953822c11cf186e2fefec1148fcf7923de37 |

| audit_evidence\f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08_table_checks.json | 10127 | a19fd76a58f50ec98c2f84d29eb881db706dfbad75204fae3db8a94678cd4018 |

| audit_evidence\f3_realdata_prep_rp1_transmission_list_2026-10-04_table_checks.json | 13176 | 14ceec17b07d78cc8d1d5f5c534c5eda5a1c8512a32af4f6ee45476b8f5e16ee |

| audit_evidence\f3_step2_correction_report_rp1-r1_2026-10-05_table_checks.json | 8950 | c466b1762fe9afae86ad43723ba199826d1a3653569706ca9fb968c6aebcf155 |

| audit_evidence\final_commit_diff.tsv | 324 | d3db1b2b87ecc62d0e0a37b7e9061b303c9cc18f6d8cdaa372a7812a3371a95e |

| audit_evidence\finalizer_selfcheck.json | 306 | dd54d3c5c718768eabe0f56331df0a015caa336297a8d2aea760a45a61d19f2d |

| audit_evidence\hash_occurrences_with_context.json | 157307 | 90219d8e063169bf507784467b069ca0541425bbf8237b212ec89fa5fc1c5595 |

| audit_evidence\new_sidecar_checks.json | 11247 | 43227954265f7a81c785c56eb2b4036810e707a1752b7fbf165937ecc4f76142 |

| audit_evidence\parent_diff.tsv | 104601 | 185d334c242261e2066f8f7f039d8c37caa57ada92ba69c5a26885b86cf2135c |

| audit_evidence\plan_stderr.log | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

| audit_evidence\plan_stdout.log | 4458 | 0f9ea3f03065fc675fcd1afc8cabf3bc2fb51986c40fd19d1015d9a462329edc |

| audit_evidence\probe_checks.json | 5031 | 62c1614bde35137cbf84a1bfc616b3e9e2c91fc4550461f5338c113387c1685f |

| audit_evidence\probe_stderr.log | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

| audit_evidence\probe_stdout.log | 10068 | 997014792cc9edd4c3a904bc4df04cc000db42897bd6694e8a789486605bfcf3 |

| audit_evidence\recomputed_vs_r4-2.diff | 115607 | f79aef76ccabfaa0743e47c8701b1a233511e5891e1fd66a9896899cdfd733bc |

| audit_evidence\recomputed_vs_rp1.diff | 86226 | b7d62a3790bc7972a0ccecf8118a3352ae1241e989efc836492ccca7b7df141a |

| audit_evidence\rerun_comparison.json | 7314 | 6eedf23f25625a7ee5549f7ecd4e6004944972d0857a603a603ead11a9d3cfc3 |

| audit_evidence\rerun_status.json | 1287 | 7308cf748902fd40ff2c8554889e23bb35d361d991f46b0e4c1ba9369c91eaa9 |

| audit_evidence\setup.json | 537 | fe43d8f4c6fd2550cd8457f7f2aa5eadbb04285329c8f9d183bed39741a8f470 |

| audit_evidence\stale_custody_sidecars.json | 1047 | 3976e0443417a0a14a4ce999f08b2a70e96f99ff67e89340c640b4023dbcdbff |

| audit_evidence\static_checks.json | 23905047 | d1eeb35f17a50de541d987667d90f83ec6060de946bb020d9429440a91da0810 |

| audit_evidence\static_checks_stderr.log | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

| audit_evidence\static_checks_stdout.log | 23922 | 1c2625a9cacaee0b1343f17b7da75386b5f7aa4bd6e77484b4394759af68d740 |

| audit_evidence\w3_stderr.log | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

| audit_evidence\w3_stdout.log | 615 | 5f58cd2f797a93aaf1a39397b46f322d9f57e9c7ec9eda942b15a49511ff9212 |

| rerun_9035df0_launch2\p_konum_plus\calibration\f3_step2_rp1-r1_launch2_stderr_2026-10-05.log | 13034898 | 0be33d8b58cee1494c2bf52d1c6dbd076fb2e33a6a6100a3f8663d6ac16355e5 |

| rerun_9035df0_launch2\p_konum_plus\calibration\f3_step2_rp1-r1_launch2_stdout_2026-10-05.log | 33323 | ef349d0e86952c801df4a07a43d43c0cb8d69b1d389aaf7577ce9669982b9d77 |


### Unchanged harness stdout
```text
LAUNCH_NUMBER = 2 ; logs = p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stdout_2026-10-05.log / p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log
REAL_DATA_MODE = False
PIN-F2-IMPORT-HASH = 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077
PIN-SPLINE-IMPORT-HASH = b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d
PIN-SPLINE-LOADER prelude nodes = 21 (authorized list match: True)
PID = 18956 ; START = 2026-10-09T20:44:35.915481 ; CMDLINE = G:\PycharmProjects\rp1r1_audit\rerun_9035df0_launch2\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1-r1_2026-10-05.py ; INTERPRETER = C:\Users\Neo\AppData\Local\Programs\Python\Python311\python.exe
RESTART_LAYER_ACTIVE = True
GRID_SIZES = P-01 731 ; P-02 261
FIXTURE_MANIFEST_SHA256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
MANIFEST_REUSED_UNCHANGED_FROM_R4_1 = true (regenerated in memory and verified equal; file not rewritten)
PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = true (p_konum_plus/provenance/f3_step2_rp1-r1_preexecution_custody_attempt2_2026-10-05.md)
DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS (observed hashes equal pins; 31 verified: D-3, r4 instruction, D-5, A-1, D-2, r4-1 instruction, D-6, A-2, A-3, r4-2 instruction, D-7, A-4, reused generator, reused manifest, r4-1 results baseline, rp1 instruction, D-10, D-9, D-8, A-5, r4-2 results/telemetry/test-evidence baseline, F1 freeze record, D-11 r1, rp1 transmission list, rp1 harness, rp1-r1 instruction, D-12, rp1 audit, rp1-r1 DRAFT review)
NR-01(i) = True (hash 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403; telemetry-fields True)
NR-01(ii) [T-2a] = True (hybrid_canonical 6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403)
SPLINE_NONREGRESSION (NR-SPL) = True (30 rows)
T-LOADER-NODES = PASS (node-list equality asserted at load time; 73 node_hashes entries for 73 executed nodes)
T_MASK_FULL_EXT = {"pass_": true}
T_F1_LOADER_SYNTH = {"eligible_count": {"expected": 6, "got": 6, "ok": true}, "partial_excluded": {"expected": true, "got": true, "ok": true}, "denominator_includes_partial": {"expected": 21146, "got": 21146, "ok": true}, "z_qc_pass": {"expected": true, "got": true, "ok": true}, "gate_pass": {"expected": true, "got": true, "ok": true}, "MISSING_YEAR": {"expected": "MISSING_YEAR", "got": "MISSING_YEAR", "ok": true}, "DUPLICATE_KEY": {"expected": "DUPLICATE_KEY", "got": "DUPLICATE_KEY", "ok": true}, "ZERO_DENOMINATOR": {"expected": "ZERO_DENOMINATOR", "got": "ZERO_DENOMINATOR", "ok": true}, "ZERO_VARIANCE": {"expected": "ZERO_VARIANCE", "got": "ZERO_VARIANCE", "ok": true}, "COUNT_BELOW_PUBLICATION_FLOOR": {"expected": "COUNT_BELOW_PUBLICATION_FLOOR", "got": "COUNT_BELOW_PUBLICATION_FLOOR", "ok": true}, "BAD_FORMAT": {"expected": "BAD_FORMAT", "got": "BAD_FORMAT", "ok": true}, "BAD_SEMANTICS": {"expected": "BAD_SEMANTICS", "got": "BAD_SEMANTICS", "ok": true}, "RAW_FILE_HASH_MISMATCH": {"expected": "RAW_FILE_HASH_MISMATCH", "got": "RAW_FILE_HASH_MISMATCH", "ok": true}, "RAW_FILE_MISSING": {"expected": "RAW_FILE_MISSING", "got": "RAW_FILE_MISSING", "ok": true}, "NONFINITE_PRE_Z_NAN": {"expected": "NONFINITE_PRE_Z", "got": "NONFINITE_PRE_Z", "ok": true}, "NONFINITE_PRE_Z_INF": {"expected": "NONFINITE_PRE_Z", "got": "NONFINITE_PRE_Z", "ok": true}, "NEGATIVE_SHARE": {"expected": "NEGATIVE_SHARE", "got": "NEGATIVE_SHARE", "ok": true}, "NONFINITE_POST_Z": {"expected": "NONFINITE_POST_Z", "got": "NONFINITE_POST_Z", "ok": true}, "Z_STD_QC": {"expected": "Z_STD_QC", "got": "Z_STD_QC", "ok": true}, "Z_NORM_QC": {"expected": "Z_NORM_QC", "got": "Z_NORM_QC", "ok": true}, "TOLERANCE_BREACH": {"expected": "Z_MEAN_QC", "got": "Z_MEAN_QC", "ok": true}, "pass_": true}
PROGRESS SPL ctx 1 F3-REAL real:F0:F_Zq00:SPL:full
PROGRESS SPL ctx 2 F3-REAL real:F0:F_Zq00:SPL:fold0
PROGRESS SPL ctx 3 F3-REAL real:F0:F_Zq00:SPL:fold1
PROGRESS SPL ctx 4 F3-REAL real:F0:F_Zq00:SPL:fold2
PROGRESS SPL ctx 5 F3-REAL real:F0:F_Zq00:SPL:fold3
PROGRESS SPL ctx 6 F3-REAL real:F0:F_Zq00:SPL:fold4
PROGRESS SPL ctx 7 F3-REAL real:F0:F_Zq00:SPL:probeL
PROGRESS SPL ctx 8 F3-REAL real:F0:F_Zq00:SPL:probeR
PROGRESS SPL ctx 9 F3-REAL real:F1:F_Zq01:SPL:full
PROGRESS SPL ctx 10 F3-REAL real:F1:F_Zq01:SPL:fold0
PROGRESS SPL ctx 11 F3-REAL real:F1:F_Zq01:SPL:fold1
PROGRESS SPL ctx 12 F3-REAL real:F1:F_Zq01:SPL:fold2
PROGRESS SPL ctx 13 F3-REAL real:F1:F_Zq01:SPL:fold3
PROGRESS SPL ctx 14 F3-REAL real:F1:F_Zq01:SPL:fold4
PROGRESS SPL ctx 15 F3-REAL real:F1:F_Zq01:SPL:probeL
PROGRESS SPL ctx 16 F3-REAL real:F1:F_Zq01:SPL:probeR
PROGRESS SPL ctx 17 F3-REAL real:F2:F_Zq02:SPL:full
PROGRESS SPL ctx 18 F3-REAL real:F2:F_Zq02:SPL:fold0
PROGRESS SPL ctx 19 F3-REAL real:F2:F_Zq02:SPL:fold1
PROGRESS SPL ctx 20 F3-REAL real:F2:F_Zq02:SPL:fold2
PROGRESS SPL ctx 21 F3-REAL real:F2:F_Zq02:SPL:fold3
PROGRESS SPL ctx 22 F3-REAL real:F2:F_Zq02:SPL:fold4
PROGRESS SPL ctx 23 F3-REAL real:F2:F_Zq02:SPL:probeL
PROGRESS SPL ctx 24 F3-REAL real:F2:F_Zq02:SPL:probeR
PROGRESS SPL ctx 25 F3-REAL real:M0:M_Zq00:SPL:full
PROGRESS SPL ctx 26 F3-REAL real:M0:M_Zq00:SPL:fold0
PROGRESS SPL ctx 27 F3-REAL real:M0:M_Zq00:SPL:fold1
PROGRESS SPL ctx 28 F3-REAL real:M0:M_Zq00:SPL:fold2
PROGRESS SPL ctx 29 F3-REAL real:M0:M_Zq00:SPL:fold3
PROGRESS SPL ctx 30 F3-REAL real:M0:M_Zq00:SPL:fold4
PROGRESS SPL ctx 31 F3-REAL real:M0:M_Zq00:SPL:probeL
PROGRESS SPL ctx 32 F3-REAL real:M0:M_Zq00:SPL:probeR
PROGRESS SPL ctx 33 F3-REAL real:M1:M_Zq01:SPL:full
PROGRESS SPL ctx 34 F3-REAL real:M1:M_Zq01:SPL:fold0
PROGRESS SPL ctx 35 F3-REAL real:M1:M_Zq01:SPL:fold1
PROGRESS SPL ctx 36 F3-REAL real:M1:M_Zq01:SPL:fold2
PROGRESS SPL ctx 37 F3-REAL real:M1:M_Zq01:SPL:fold3
PROGRESS SPL ctx 38 F3-REAL real:M1:M_Zq01:SPL:fold4
PROGRESS SPL ctx 39 F3-REAL real:M1:M_Zq01:SPL:probeL
PROGRESS SPL ctx 40 F3-REAL real:M1:M_Zq01:SPL:probeR
PROGRESS SPL ctx 41 F3-REAL real:M2:M_Zq02:SPL:full
PROGRESS SPL ctx 42 F3-REAL real:M2:M_Zq02:SPL:fold0
PROGRESS SPL ctx 43 F3-REAL real:M2:M_Zq02:SPL:fold1
PROGRESS SPL ctx 44 F3-REAL real:M2:M_Zq02:SPL:fold2
PROGRESS SPL ctx 45 F3-REAL real:M2:M_Zq02:SPL:fold3
PROGRESS SPL ctx 46 F3-REAL real:M2:M_Zq02:SPL:fold4
PROGRESS SPL ctx 47 F3-REAL real:M2:M_Zq02:SPL:probeL
PROGRESS SPL ctx 48 F3-REAL real:M2:M_Zq02:SPL:probeR
T_F1_HANDOFF_SYNTH = {"ran_without_exception": true, "exception": null, "captured_rows": 144, "dry_rows": 144, "actual_rows_equal_dry_table": true, "xhashes_match_loader": true, "pass_": true}
T_CONTEXT_ID_UNIQUE = {"rows": 144, "expected_rows": 144, "all_unique": true, "matches_dry_table": true, "pass_": true}
T_F1_CONTRACT_GAP = {"cases": {"fixture_id": {"raised": true, "key_named": "fixture_id", "ok": true}, "strata": {"raised": true, "key_named": "strata", "ok": true}, "start_bank": {"raised": true, "key_named": "start_bank", "ok": true}, "injections": {"raised": true, "key_named": "injections", "ok": true}}, "pass_": true}
T_F1_REPRO_GATE_SYNTH = {"cases": {"complete": {"raised": false, "reason": null, "ok": true}, "missing_file": {"raised": true, "reason": "F1_REPRO_GATE_MISSING_FILE ['yob9999_NONEXISTENT.txt']", "ok": true}, "extra_file": {"raised": true, "reason": "F1_REPRO_GATE_EXTRA_FILE ['yob2025.txt']", "ok": true}, "hash_changed": {"raised": true, "reason": "F1_REPRO_GATE_HASH_MISMATCH yob1880.txt observed=cb7a3ce1f47026a74a6a3fe0f6946f76c87a7ed1e0e2a09c7e9c39e69b66b115 expected=0b7a3ce1f47026a74a6a3fe0f6946f76c87a7ed1e0e2a09c7e9c39e69b66b115", "ok": true}, "eligible_manifest_changed": {"raised": true, "reason": "F1_REPRO_GATE_ELIGIBLE_MISMATCH observed=[('F', 'Zq00'), ('F', 'Zq01'), ('F', 'Zq02'), ('M', 'Zq00'), ('M', 'Zq01'), ('M', 'Zq02')] expected=[('F', 'Zq00'), ('F', 'Zq01'), ('F', 'Zq02'), ('M', 'Zq00'), ('M', 'Zq01')]", "ok": true}}, "pass_": true}
T_INADMISSIBLE_OBSERVABLE = {"family": {"witness_found": false, "witness": null, "eligible_not_counted": true, "nonconverged_not_counted": true, "infeasible_not_counted": true}, "spline": {"clean_not_accepted_counted": true, "accepted_stage1_not_counted": true, "accepted_primary_not_counted": true, "dirty_return_not_counted": true}, "witness_on_frozen_lattice": false, "pass_": true}
PROGRESS SPL ctx 49 T-STORE-READ tsr:full
PROGRESS SPL ctx 50 T-STORE-READ tsr:full
PROGRESS SPL ctx 51 T-STORE-READ tsr:full
PROGRESS SPL ctx 52 T-STORE-READ tsr:full
PROGRESS SPL ctx 53 T-STORE-READ tsr:full
T_STORE_READ_ACCOUNTING = {"cold": {"modes": 146, "fit1_reads": 0, "resumed_warm_start": false, "served_to_fit2": 146, "fine_counter": 146, "per_read_rows_wellformed": true, "fit2_equals_fit1": true, "fit2_replay_rows": 164, "fit2_replay_rows_tagged_replay": true, "replay_matches_stored_telemetry": true, "pass_": true}, "warm": {"modes": 146, "fit1_reads": 146, "resumed_warm_start": true, "served_to_fit2": 146, "fine_counter": 292, "per_read_rows_wellformed": true, "fit2_equals_fit1": true, "fit2_replay_rows": 164, "fit2_replay_rows_tagged_replay": true, "replay_matches_stored_telemetry": true, "pass_": true}, "pass_": true}
T_SPL_PENDING_REALPATH = {"cases": [{"case": "baseline", "expected": {}, "got": {}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["FAIL", "FAIL"], "mechanism": "STOP_BOTH_FAIL_REDESIGN"}, {"case": "natural full", "expected": {"P01:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "got": {"P01:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04)"}, {"case": "natural fold", "expected": {"P01:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "got": {"P01:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C2:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["FAIL", "FAIL"], "mechanism": "STOP_BOTH_FAIL_REDESIGN"}, {"case": "natural probe", "expected": {"P01:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "got": {"P01:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["FAIL", "FAIL"], "mechanism": "STOP_BOTH_FAIL_REDESIGN"}, {"case": "injected full", "expected": {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}, "got": {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}, {"case": "injected fold", "expected": {"P01:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}, "got": {"P01:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C2:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["FAIL", "FAIL"], "mechanism": "STOP_BOTH_FAIL_REDESIGN"}, {"case": "injected probe", "expected": {"P01:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}, "got": {"P01:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:M": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)"}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["FAIL", "FAIL"], "mechanism": "STOP_BOTH_FAIL_REDESIGN"}, {"case": "declared spline failure", "expected": {}, "got": {}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["FAIL", "FAIL"], "mechanism": "STOP_BOTH_FAIL_REDESIGN"}, {"case": "natural and injected, same sex", "expected": {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "got": {"P01:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P01:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)", "P02:C3:F": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "P02:C4b:F": "STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-04)"}, "ok": true, "pending_cells_with_a_verdict": [], "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-04)"}], "all_cases_ok": true, "restored": {"fit_family": true, "fit_spline": true, "fidelity_declared": true, "fidelity_executed": true, "telemetry": true, "exc_captures": true, "progress_counter": true, "phase": true}, "pass_": true}
PIN-MASKED-OBJECTIVE full == frozen: True ; L_O<=L_FULL: True ; PIN-FEATURE-START-MASKED: True
PROGRESS SPL ctx 54 FIX-A5-TRUE a5true:left:full
PROGRESS SPL ctx 55 FIX-A5-TRUE a5true:left:probeL
PROGRESS SPL ctx 56 FIX-A5-TRUE a5true:right:full
PROGRESS SPL ctx 57 FIX-A5-TRUE a5true:right:probeR
PROGRESS SPL ctx 58 INJ-EXC-CAPTURE-S1 exc:s1
PROGRESS SPL ctx 59 INJ-EXC-CAPTURE-S2 exc:s2
PROGRESS SPL ctx 60 INJ-EXC-UNRELATED-TYPE exc:unrel
PROGRESS SPL ctx 61 INJ-EXC-CAPTURE-S1 exc:s1
PROGRESS SPL ctx 62 INJ-EXC-CAPTURE-S2 exc:s2
PROGRESS SPL ctx 63 INJ-EXC-UNRELATED-TYPE exc:unrel
T_A5_SUPPORT = {"threshold_equality_included": true, "next_float_below_excluded": true, "disconnected_components_united": true, "inside_left_true_L": true, "inside_left_false_R": true, "middle_false_both": true, "constant_reference_S_equals_G": true, "nan_reference_violates": true, "wrong_length_violates": true, "inf_reference_violates": true, "pass_": true}
A5_UNIT_TESTS = {"UT_A5_II_pass": true, "UT_A5_III_pass": true, "note": "unit tests; A.5(i) is exercised on the real path (S-1=(a)); these two probe A.5(ii)/(iii) directly"}
UT_PROBE_DECOUPLE = {"UT_PROBE_DECOUPLE_pass": true, "full_eligible": false, "probe_eligible": true, "probe_success_c4a": true, "rmse_computable": false, "second_half_v4_membership": [], "second_half_pass": true, "note": "first half: probe_success is probe-level only (X-04). second half RUNS this cycle (S-R2-1 = PI_RULE, D-5 S4(d)): the no-full-data-reference trajectory is absent from V4 by flag membership, checked through the real crit_stats + uset_c4b product path"}
UT_USET_CONSTRUCTION = {"a": {"ok": true, "U2": 9, "U5": 10, "expect": {"U2": 9, "U5": 10}}, "b": {"ok": true, "U5": 9, "expect": {"U5": 9}}, "c": {"ok": true, "U2": [1, 2, 3, 4, 5, 6, 7, 8, 9], "expect": {"U2_excludes": 0}}, "d": {"ok": true, "U4": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "revalidation_flags_member": true, "expect": {"U4_includes": 0, "revalidation_flags_member": 0}}, "e": {"ok": true, "U2": [1, 2, 3, 4, 5, 6, 7, 8, 9], "U5": [1, 2, 3, 4, 5, 6, 7, 8, 9], "expect": {"U2_excludes": 0, "U5_excludes": 0}}}
T_COMPARATOR_NAN = {"guard_refuses_nan": true, "guard_refuses_none": true, "guard_refuses_inf": true, "guard_accepts_finite": true, "python_nan_comparison_is_resolved_like": true, "guarded_comparator_label": "STOP_CONTRACT_VIOLATION_INCONSISTENT_U", "guarded_comparator_label_is_inconsistent_u": true, "pass_": true, "note": "pass_ from the real guard's behavior AND an end-to-end run_dp04 call asserting the R4A-03 label CONTRACT_VIOLATION_INCONSISTENT_U (D-3 Y-03(iii))"}
T_STARTS_DEFAULT (FIX-STARTS-FULL) = {"P-01": {"start_bank_size": 732, "expected": 732, "pass_": true, "retained_count": 731, "feature_start_rejected": false}, "P-02": {"start_bank_size": 262, "expected": 262, "pass_": true, "retained_count": 261, "feature_start_rejected": false}}
T_STARTS_DUP (FIX-STARTS-DUP) = {"index0": {"feature_start_rejected": true, "reason": "DUPLICATE", "pass_": true}, "index145": {"feature_start_rejected": true, "reason": "DUPLICATE", "pass_": true}}
FIX_A5_TRUE = {"left": {"a5_i": true, "support_size": 15, "P-01": {"full_eligible": true, "probe_eligible": true, "probe_success_c4a": false, "excluded_from_c4a_numerator": true, "excluded_from_c4b_pair": true}, "P-02": {"full_eligible": true, "probe_eligible": true, "probe_success_c4a": false, "excluded_from_c4a_numerator": true, "excluded_from_c4b_pair": true}, "SPL": {"full_valid": true, "probe_valid": true, "probe_success_c4a": false, "excluded_from_c4a_numerator": true, "excluded_from_c4b_pair": true}, "pass_": true}, "right": {"a5_i": true, "support_size": 15, "P-01": {"full_eligible": true, "probe_eligible": true, "probe_success_c4a": false, "excluded_from_c4a_numerator": true, "excluded_from_c4b_pair": true}, "P-02": {"full_eligible": true, "probe_eligible": true, "probe_success_c4a": false, "excluded_from_c4a_numerator": true, "excluded_from_c4b_pair": true}, "SPL": {"full_valid": true, "probe_valid": true, "probe_success_c4a": false, "excluded_from_c4a_numerator": true, "excluded_from_c4b_pair": true}, "pass_": true}}
EXC_INJECTION_FIXTURES = {"S1": {"count": 1, "stages": [1], "pass_": true}, "S2": {"count": 2, "stages": [1, 2], "pass_": true}, "UNRELATED_TYPE": {"caught_not_crashed": true, "exception_type_recorded": "ValueError", "context_unverifiable": true, "eval_level_dependent_criteria_pending": {"INJ-SPL-PENDING-FULL": {"C3": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4b": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4a_stays_pass": true, "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}, "INJ-SPL-PENDING-FOLD": {"C2": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4a_stays_pass": true, "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}, "INJ-SPL-PENDING-PROBE": {"C4b": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4a_stays_pass": true, "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}}, "eval_level_ok": true, "pass_": true}, "passes_identical": true, "pass_key_namespaces_disjoint": true, "pass2": {"S1": {"count": 1, "stages": [1], "pass_": true}, "S2": {"count": 2, "stages": [1, 2], "pass_": true}, "UNRELATED_TYPE": {"caught_not_crashed": true, "exception_type_recorded": "ValueError", "context_unverifiable": true, "eval_level_dependent_criteria_pending": {"INJ-SPL-PENDING-FULL": {"C3": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4b": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4a_stays_pass": true, "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}, "INJ-SPL-PENDING-FOLD": {"C2": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4a_stays_pass": true, "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}, "INJ-SPL-PENDING-PROBE": {"C4b": {"status": "STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)", "has_passed_field": false, "pending_not_passfail": true}, "C4a_stays_pass": true, "p03": ["PENDING", "PENDING"], "mechanism": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}}, "eval_level_ok": true, "pass_": true}}}
UT_EXC_UNRELATED_REFERENCE = {"case_1a_propagated": true, "case_1b_propagated": true, "pass_": true}
PROGRESS SPL ctx 64 SCEN-A run1:F0:full
PROGRESS SPL ctx 65 SCEN-A run1:F0:fold0
PROGRESS SPL ctx 66 SCEN-A run1:F0:fold1
PROGRESS SPL ctx 67 SCEN-A run1:F0:fold2
PROGRESS SPL ctx 68 SCEN-A run1:F0:fold3
PROGRESS SPL ctx 69 SCEN-A run1:F0:fold4
PROGRESS SPL ctx 70 SCEN-A run1:F0:probeL
PROGRESS SPL ctx 71 SCEN-A run1:F0:probeR
PROGRESS SPL ctx 72 SCEN-A run1:M0:full
PROGRESS SPL ctx 73 SCEN-A run1:M0:fold0
PROGRESS SPL ctx 74 SCEN-A run1:M0:fold1
PROGRESS SPL ctx 75 SCEN-A run1:M0:fold2
PROGRESS SPL ctx 76 SCEN-A run1:M0:fold3
PROGRESS SPL ctx 77 SCEN-A run1:M0:fold4
PROGRESS SPL ctx 78 SCEN-A run1:M0:probeL
PROGRESS SPL ctx 79 SCEN-A run1:M0:probeR
PROGRESS SPL ctx 80 SCEN-B run1:F0:full
PROGRESS SPL ctx 81 SCEN-B run1:F0:fold0
PROGRESS SPL ctx 82 SCEN-B run1:F0:fold1
PROGRESS SPL ctx 83 SCEN-B run1:F0:fold2
PROGRESS SPL ctx 84 SCEN-B run1:F0:fold3
PROGRESS SPL ctx 85 SCEN-B run1:F0:fold4
PROGRESS SPL ctx 86 SCEN-B run1:F0:probeL
PROGRESS SPL ctx 87 SCEN-B run1:F0:probeR
PROGRESS SPL ctx 88 SCEN-B run1:M0:full
PROGRESS SPL ctx 89 SCEN-B run1:M0:fold0
PROGRESS SPL ctx 90 SCEN-B run1:M0:fold1
PROGRESS SPL ctx 91 SCEN-B run1:M0:fold2
PROGRESS SPL ctx 92 SCEN-B run1:M0:fold3
PROGRESS SPL ctx 93 SCEN-B run1:M0:fold4
PROGRESS SPL ctx 94 SCEN-B run1:M0:probeL
PROGRESS SPL ctx 95 SCEN-B run1:M0:probeR
PROGRESS SPL ctx 96 SCEN-A run2:F0:full
PROGRESS SPL ctx 97 SCEN-A run2:F0:fold0
PROGRESS SPL ctx 98 SCEN-A run2:F0:fold1
PROGRESS SPL ctx 99 SCEN-A run2:F0:fold2
PROGRESS SPL ctx 100 SCEN-A run2:F0:fold3
PROGRESS SPL ctx 101 SCEN-A run2:F0:fold4
PROGRESS SPL ctx 102 SCEN-A run2:F0:probeL
PROGRESS SPL ctx 103 SCEN-A run2:F0:probeR
PROGRESS SPL ctx 104 SCEN-A run2:M0:full
PROGRESS SPL ctx 105 SCEN-A run2:M0:fold0
PROGRESS SPL ctx 106 SCEN-A run2:M0:fold1
PROGRESS SPL ctx 107 SCEN-A run2:M0:fold2
PROGRESS SPL ctx 108 SCEN-A run2:M0:fold3
PROGRESS SPL ctx 109 SCEN-A run2:M0:fold4
PROGRESS SPL ctx 110 SCEN-A run2:M0:probeL
PROGRESS SPL ctx 111 SCEN-A run2:M0:probeR
PROGRESS SPL ctx 112 SCEN-B run2:F0:full
PROGRESS SPL ctx 113 SCEN-B run2:F0:fold0
PROGRESS SPL ctx 114 SCEN-B run2:F0:fold1
PROGRESS SPL ctx 115 SCEN-B run2:F0:fold2
PROGRESS SPL ctx 116 SCEN-B run2:F0:fold3
PROGRESS SPL ctx 117 SCEN-B run2:F0:fold4
PROGRESS SPL ctx 118 SCEN-B run2:F0:probeL
PROGRESS SPL ctx 119 SCEN-B run2:F0:probeR
PROGRESS SPL ctx 120 SCEN-B run2:M0:full
PROGRESS SPL ctx 121 SCEN-B run2:M0:fold0
PROGRESS SPL ctx 122 SCEN-B run2:M0:fold1
PROGRESS SPL ctx 123 SCEN-B run2:M0:fold2
PROGRESS SPL ctx 124 SCEN-B run2:M0:fold3
PROGRESS SPL ctx 125 SCEN-B run2:M0:fold4
PROGRESS SPL ctx 126 SCEN-B run2:M0:probeL
PROGRESS SPL ctx 127 SCEN-B run2:M0:probeR
EXC_CAPTURES_RUN1_EQ_RUN2 = True (run1=1, run2=1)
T_EXPECT_ALL = declared/ran 36/36 ; EXPECTATION_FAIL = []
T_SCHEMA = {"seen": {"fits.theta": true, "fits.L": true, "fits.start_bank_size": true, "fits.feature_start_rejected": true, "fits.mode": true, "fits.rss": true, "fits.equivalent_modes": true, "fits.per_mode_valid": true, "disc_f3_03_complement.C2": true, "disc_f3_03_complement.C3": true, "disc_f3_03_complement.C4b": true, "invalid_counts_by_criterion": true, "probe_failure_shares": true, "k05_result": true}, "missing": []}
EXC_CAPTURES (RUN1) = 1 record(s)
EXC_CAPTURES injected=0 natural=1
NATURAL_SOLVER_B_UNVERIFIABLE_ACCEPTANCE_EVENTS = [{"fixture": "SCEN-A", "sex": "F", "trajectory": 0, "mask_id": "run1:F0:full", "mode": 113, "stage": 2, "exception_type": "RuntimeError", "message": "Maximum number of iterations reached.", "traceback": "Traceback (most recent call last):\n  File \"G:\\PycharmProjects\\rp1r1_audit\\rerun_9035df0_launch2\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r1_2026-10-05.py\", line 831, in wrapped_accept\n    return real_accept(c, z, O, A)\n           ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py\", line 313, in accept\n    res, _ = kkt_res(c, z, O, A)\n             ^^^^^^^^^^^^^^^^^^^\n  File \"p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py\", line 304, in kkt_res\n    _, res = nnls(A[act].T, g)\n             ^^^^^^^^^^^^^^^^^\n  File \"G:\\PycharmProjects\\rp1r1_audit\\rerun_9035df0_launch2\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r1_2026-10-05.py\", line 937, in wrapped_nnls\n    return real_nnls(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\scipy\\optimize\\_nnls.py\", line 93, in nnls\n    raise RuntimeError(\"Maximum number of iterations reached.\")\nRuntimeError: Maximum number of iterations reached.\n", "kind": "COVERED", "phase": "run1", "pid": 18956, "start_iso": "2026-10-09T20:44:35.915481", "s2_rule": "alpha: NOT accepted at stage 2; chain continues"}]
NATURAL_UNRELATED_EVENTS = 0 ; exactness_findings = []
NONREGRESSION_VS_R4 shared=34 new=3 dropped=0 findings=0 real_path_spline_pending=0
NONREGRESSION_WRITTEN = p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4_2026-10-05.csv sha256=41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a
NONREGRESSION_VS_R4_1 compared=37 findings=0 stops_equal=True
NONREGRESSION_R4_1_WRITTEN = p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-1_2026-10-05.csv sha256=0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d
PIN-ACF bitwise-equal(all)=True strict-vs-(b),(c)(all)=True
RESIDUAL_SERIES_WRITTEN = p_konum_plus/calibration/f3_step2_residual_series_rp1-r1_2026-10-05.json sha256=3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f
T_RESIDUAL_LINK_KEYS = 11
INJ-C1-FAIL mechanism = ONLY_P02_PASSES (p03={'P01': 'FAIL', 'P02': 'PASS'})
INJ-DP04-C1 mechanism (S-R2-1 PI_RULE) = RESOLVED_MECHANISM_P01
UNCONSULTED_NOT_RECOMPUTED_EVIDENCE (INJ-DP04-C2-DIVERGE) = {"C1": 0, "C2": 1, "C3": 0, "C4a": 0, "C4b": 0, "C5": 0, "C6": 0}
INJ-DP04-C2-DIVERGE |U2| = 8 confirmed (Y-02 membership-first)
INJ-U-POST-CONSTRUCTION-INVALID -> CONTRACT_VIOLATION_INCONSISTENT_U confirmed
INJ-C4B-NOREF mechanism (S-R2-1 PI_RULE) = TERMINAL_FALLBACK_MECHANISM_P01
SCEN-B mechanism (S-R2-1 PI_RULE; V4 empty in M) = STOP_BOTH_FAIL_REDESIGN
FIDELITY = 5/5 (implemented) ; 5/5 (executed) [declared injection sites]
RUN1_CANONICAL_SHA256 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77
RUN2_CANONICAL_SHA256 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77
DETERMINISM = True
T_NONREG_R4_1 = {"baseline": "p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json", "baseline_sha256": "6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385", "compared": 37, "stops_equal": true, "run1_canonical_expected": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77", "run1_canonical_observed": "556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77", "run1_canonical_unchanged": true, "residual_series_expected": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f", "residual_series_observed": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f", "residual_series_unchanged": true}
T_WRAPPER_RESTORE = True
TEST_EVIDENCE_WRITTEN = p_konum_plus/calibration/f3_step2_test_evidence_rp1-r1_2026-10-05.json sha256=9d487dd5d671442902766ea558ed0dd9810c854330bde7a90a8811ea78c3dae2
PERCALL_TELEMETRY_WRITTEN = p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1-r1_2026-10-05.csv sha256=56ccbe0bc1d00a74ec68323193dc1aa030fc02865a902665429ce1fb863e99fd
PERCALL_TELEMETRY_ROWS = 22217
T_CALLCOUNT per phase = {"nr_gates": 9283, "run1": 5256, "run2": 5256, "t_store_read_accounting": 820, "unit_tests": 1602}
T_CALLCOUNT per phase/pid = {"nr_gates/18956": 9283, "run1/18956": 5256, "run2/18956": 5256, "t_store_read_accounting/18956": 820, "unit_tests/18956": 1602}
STORE_MANIFEST_WRITTEN = p_konum_plus/calibration/f3_step2_rp1-r1_restart_store_manifest_2026-10-05.csv sha256=583c75d9b54e9a0b6f92746141e5835bb5dc8f27cba84ed1e3bb1b90cf11e775 rows=67313
STORE_READ_LOG_WRITTEN = p_konum_plus/calibration/f3_step2_rp1-r1_store_read_log_2026-10-05.csv sha256=6fb704b59493b6a36f36fcb01bc870318efd63cc310262362afdafaea77a268e rows=730
COVERAGE_DERIVED = 64 rows ; downgraded_to_UNCOVERED = []
PI_DISPATCH_RECORD (D-12) observed = 2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364 ; S-R2-1 source (D-5) = 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
END_STATE = {"PI_dispatch_record_hash": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364", "PI_dispatch_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md", "S_R2_1_source_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851", "S_R2_1_source_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md", "corrections_complete": false, "mandatory_tests_all_run": false, "mandatory_tests_missing": ["T-NONREG-R4-2"], "deferred_decisions": [], "narrowed_evidence": ["T-R2-2", "T-RP-1"], "uncovered_coverage_rows": ["A.5 (iii) inadmissible refit"], "open_findings": [], "F3_STEP2_r4_status": "PARTIAL_PENDING_PI"}
F3_STEP2_r4_status = PARTIAL_PENDING_PI
NONREGRESSION_VS_R4_2 s_findings=0 e_declared=2114 u_findings=0
NONREGRESSION_R4_2_WRITTEN = p_konum_plus/calibration/f3_step2_rp1-r1_nonregression_vs_r4-2_2026-10-05.csv sha256=9e45788c864c16db4e69b69e2ded7e350fef1d4a273badc1ed79ed3c955a4579
END_STATE (refreshed after T-NONREG-R4-2) = {"PI_dispatch_record_hash": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364", "PI_dispatch_record_path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md", "S_R2_1_source_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851", "S_R2_1_source_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md", "corrections_complete": true, "mandatory_tests_all_run": true, "mandatory_tests_missing": [], "deferred_decisions": [], "narrowed_evidence": ["T-R2-2", "T-RP-1"], "uncovered_coverage_rows": ["A.5 (iii) inadmissible refit"], "open_findings": [], "F3_STEP2_r4_status": "PARTIAL_PENDING_PI"}
F3_STEP2_r4_status (refreshed) = PARTIAL_PENDING_PI
RESULTS_WRITTEN = p_konum_plus/calibration/f3_step2_results_rp1-r1_2026-10-05.json sha256=3e4c85de312aef5425cc2e18897bd134eeda71e3cb1f1fd1fdb3b2175af7fc4f
TELEMETRY_WRITTEN = p_konum_plus/calibration/f3_step2_telemetry_rp1-r1_2026-10-05.csv sha256=83ff89cced967f5d0e2f9fc0278c71ca065906e3be10ecb517f9dea6fce9a6ba
TELEMETRY_ROWS = 12298
STOPS = [{"fixture": "SCEN-B", "stop": "BOTH_FAIL_REDESIGN"}, {"fixture": "INJ-BOTH-FAIL", "stop": "BOTH_FAIL_REDESIGN"}, {"fixture": "INJ-DP04-EMPTY-U", "stop": "CONTRACT_VIOLATION_EMPTY_U", "level": "C2"}, {"fixture": "INJ-U-POST-CONSTRUCTION-INVALID", "stop": "CONTRACT_VIOLATION_INCONSISTENT_U", "level": "C2", "sex": "F", "member": 0, "offending_pairs": [{"sex": "F", "fitter": "P01", "observation": 0}, {"sex": "M", "fitter": "P01", "observation": 0}]}, {"fixture": "INJ-NAN-STAT-SPL", "stop": "BOTH_FAIL_REDESIGN"}, {"fixture": "INJ-P03-BOTHFAIL-C4PENDING", "stop": "BOTH_FAIL_REDESIGN"}]
MECHANISM_OUTCOMES = {"SCEN-A": "RESOLVED_MECHANISM_P01", "SCEN-B": "STOP_BOTH_FAIL_REDESIGN", "INJ-C1-FAIL": "ONLY_P02_PASSES", "INJ-C2-MARGIN-FAIL": "ONLY_P02_PASSES", "INJ-C2-FLOOR-FAIL": "ONLY_P02_PASSES", "INJ-C3-FAIL": "ONLY_P02_PASSES", "INJ-C3-PHI-UNDEF": "ONLY_P02_PASSES", "INJ-C4A-FAIL": "ONLY_P02_PASSES", "INJ-C4B-FAIL": "ONLY_P02_PASSES", "INJ-C4B-FLOOR-FAIL": "ONLY_P02_PASSES", "INJ-C5-FAIL": "ONLY_P02_PASSES", "INJ-SEX-SPLIT": "ONLY_P02_PASSES", "INJ-ONLY-P01": "ONLY_P01_PASSES", "INJ-BOTH-FAIL": "STOP_BOTH_FAIL_REDESIGN", "INJ-DP04-C1": "RESOLVED_MECHANISM_P01", "INJ-DP04-C2-DIVERGE": "RESOLVED_MECHANISM_P01", "INJ-DP04-C3": "RESOLVED_MECHANISM_P01", "INJ-DP04-4A": "RESOLVED_MECHANISM_P01", "INJ-DP04-4B": "RESOLVED_MECHANISM_P01", "INJ-DP04-C5": "RESOLVED_MECHANISM_P01", "INJ-DP04-TERMINAL": "TERMINAL_FALLBACK_MECHANISM_P01", "INJ-DP04-EMPTY-U": "STOP_CONTRACT_VIOLATION_EMPTY_U", "INJ-U2-RHO-INVALID": "TERMINAL_FALLBACK_MECHANISM_P01", "INJ-U5-C2-INDEPENDENT": "TERMINAL_FALLBACK_MECHANISM_P01", "INJ-U5-SST-INVALID": "TERMINAL_FALLBACK_MECHANISM_P01", "INJ-U-POST-CONSTRUCTION-INVALID": "STOP_CONTRACT_VIOLATION_INCONSISTENT_U", "INJ-NAN-STAT": "ONLY_P02_PASSES", "INJ-U-CCFALSE-FINITE": "TERMINAL_FALLBACK_MECHANISM_P01", "INJ-NAN-STAT-C4B": "ONLY_P02_PASSES", "INJ-NAN-STAT-C5": "ONLY_P02_PASSES", "INJ-NAN-STAT-SPL": "STOP_BOTH_FAIL_REDESIGN", "INJ-C4B-NOREF": "TERMINAL_FALLBACK_MECHANISM_P01", "INJ-P03-C4PENDING-C5FAIL": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING)", "INJ-P03-BOTHFAIL-C4PENDING": "STOP_BOTH_FAIL_REDESIGN", "INJ-SPL-PENDING-FULL": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)", "INJ-SPL-PENDING-FOLD": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)", "INJ-SPL-PENDING-PROBE": "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"}
REAL_DATA_ACCESS = false
RUN_COMPLETE 18956

```


### Unchanged harness stderr tail (complete file pinned above)
```text
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:316: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(self.x - self.x_prev, self.g - self.g_prev)
C:\Users\Neo\AppData\Local\Programs\Python\Python311\Lib\site-packages\scipy\optimize\_differentiable_functions.py:551: UserWarning: delta_grad == 0.0. Check if the approximated function is linear. If the function is linear better results can be obtained by defining the Hessian as zero instead of using quasi-Newton approximations.
  self.H.update(delta_x, delta_g)
G:\PycharmProjects\rp1r1_audit\rerun_9035df0_launch2\p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py:109: RuntimeWarning: invalid value encountered in power
  -(np.abs(m - U_GRID) / s_l) ** beta,
G:\PycharmProjects\rp1r1_audit\rerun_9035df0_launch2\p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py:110: RuntimeWarning: invalid value encountered in power
  -(np.abs(U_GRID - m) / s_r) ** beta,
```


PI line: D-9 §2(a) preconditions are **NOT MET**: executor and auditor S objects match, but this independent audit is NOT PASSED; environment differences: none across Windows platform, Python, NumPy, SciPy, OMP, OPENBLAS and MKL. PI binding remains a separate decision.
