# p_konum_plus — F3 STEP-2 r4-2 — Correction Report

```text
artifact_role = correction report (deliverable 10, r4-2 revision inside the r4 cycle)
status        = NON-NORMATIVE narrative over the hashed artifacts it cites
date          = 2026-09-30 (revision tag; launches 2026-09-30)
```

No wording in this report asserts "verified", "QUALIFIED", or "audit PASS" about the
executor's own output. `F3_STEP2 = QUALIFIED` can be declared only by the PI after an
independent audit, which this report does not perform.

## 1. The PI's dispatch messages, verbatim

Dispatch of the r4-2 revision (2026-09-30; attachment tokens as received):

```text
Ekteki r4-2 talimatını ve D-7 dispatch kaydını uygula. Kapsam D-7 §3'te: R41A-01 … 06; R41A-08 kapsam dışı.
S-R2-1 ve T-R2-2 D-5'teki gibi. r3, r4, r4-1 ve karantina dosyalarının hiçbirini değiştirme, yeniden adlandırma
veya taşıma. Her düzeltmeyi yalnız ilgili test gerçekten çalışıp geçtiğinde kapat. Custody kayıtlarını ve
log'ları hiçbir zaman üzerine yazma. Sonunda teslim klasörünü eksiksiz, ayrıca tek bir zip olarak hazırla.
Commit yapma.@C:\Users\Neo\Downloads\Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md.sha256 @C:\Users\Neo\Downloads\f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md.sha256 @C:\Users\Neo\Downloads\f3_step2_r4-2_pi_dispatch_record_2026-09-30.md.sha256
```

(Only the three sidecars arrived with that message; the executor STOPPED before any write
and requested the three .md instruments, which the PI then supplied as a bundle. All were
verified EQUAL before the first write.)

Mid-revision message accepting the R41A-01(b) reading (2026-09-30):

```text
R41A-01 (b) için kriter bazındaki okuman kabul; register satırında ve raporda açıkça yaz. Devam et.
```

Both were carried out: the scope applied is exactly D-7 §3 (R41A-01 … R41A-06; R41A-08 NOT
applied); every correction was closed only on a test that ran and passed (§5); no custody
record and no log was overwritten — per-attempt custody names and per-launch log names made
that structural (§3); no r3/r4/r4-1/quarantine file was modified, renamed or moved; the
delivery folder and the single zip are described in the transmission list; the accepted
per-criterion reading is stated in §4 below and in the register row
PIN-SPLINE-PENDING-TAG-SCOPE. On committing: the dispatch said "Commit yapma" and no commit
was made during the revision; after completion the PI separately directed the p_konum_plus
branch to be committed and pushed to the project repository — that action is outside the
r4-2 package and recorded in §8's process note.

## 2. Custody (r4-2 instruction §1; every value OBSERVED)

15 preconditions verified EQUAL by the external W-3 writer AND re-verified by every launch
("DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS … 15 verified"): D-3, r4 instruction, D-5, A-1,
D-2, r4-1 instruction, D-6, A-2, A-3, **r4-2 instruction `d6680338…`, D-7 `a3e70509…`,
A-4 `ad222936…`** (input, not directive), the **reused generator `68d126cf…`**, the
**reused manifest `5c09c4f0…`** (also regenerated in memory and proven byte-equal, twice),
and the **r4-1 results baseline `6dd4185b…`**. The r4-1 and r4 packages re-hash at their
non-retroactivity values (start-state inventory §2). P-4 evidence = D-7 (child of D-6).

## 3. Execution (D-3 §8; full detail in the attempt log)

2 attempts, 2 launches, 2026-09-30. Attempt 1 / launch 1 (harness `9e4d2803…`, layer OFF)
passed every gate — including T-SPL-PENDING-REALPATH 9/9 in-run — and was interrupted
externally at SPL ctx 13 with no error and **no store unit** (correct §8.1 behaviour).
R41A-02 was applied AT the transition: the attempt-1 bytes were copied to quarantine
**before** the edit (copy hash == custody-named `9e4d2803…` — preserved bytes, no
reconstruction); attempt 2 got its own custody record with
`supersedes_custody_sha256 = ae0f0768…` filled; both launch log pairs remain on disk.
Attempt 2 / launch 2 (harness `b988e962…`, layer ON, store empty) ran uninterrupted to
**exit 0**: one process (pid 10412, 20:38:58 → 21:36:01) computed **all 11,869 store units
and every result object** — **T-SINGLE-PROCESS applies and holds** (store manifest: one
pid; per-call split entirely pid 10412; units_read_from_store all 0).

One engineering refinement was made at the attempt-1→2 transition and is disclosed in the
attempt log: LAUNCH_NUMBER moved from a source constant to the environment variable
F3_R42_LAUNCH, because a resumed launch of one attempt must not change the harness bytes
(a source constant would have changed the fingerprint and orphaned the attempt's own
store). No fit, decision or deliverable content is affected.

## 4. The R41A-01(b) reading — stated, as the PI directed

R41A-01(b) admits two readings of the mixed-tag rule. The implemented one, **put to the PI
and accepted by the PI's message quoted in §1**, is **per-criterion**: a routed criterion
carries the tag folded from the contexts *that criterion reads* (full → C3, C4b; fold →
C2; probe → C4b), the instruction's leading sentence ("the tag of the event that set the
flag") deciding the single-source case, and "F3-STEP2-EXACT-04 is used" applying where both
kinds reach the *same* criterion — inside one criterion's contexts the natural tag always
wins (`merge_pending_tags`). Concretely: an injected event in `full` and a natural one in
`probeL` of the same sex give **C3 = TEST_ONLY_INJECTED** (its only source is injected) and
**C4b = F3-STEP2-EXACT-04** (natural wins where both arrive). The natural event is never
masked — it surfaces in C4b and in the mechanism outcome. The rejected alternative
(escalating every routed criterion of the sex) would attribute a natural exactness finding
to C3, which no natural event touched. Test: T-SPL-PENDING-REALPATH case "natural and
injected, same sex", expectation written before the run; register row
PIN-SPLINE-PENDING-TAG-SCOPE.

## 5. Response table — the R41A items (scope D-7 §3)

| item | status | evidence |
|---|---|---|
| **R41A-01 (a)(b)** | **CLOSED** | TEST_ONLY clause dropped at the three flag sites; tag taken from the event's own failure string and carried by the flag; c4_source tag removed; declared spline failure stays ordinary (SCEN-B pin). Register PIN-SPLINE-PENDING-ROUTING + PIN-SPLINE-PENDING-TAG-SCOPE. Tests: T-SPL-PENDING-REALPATH 9/9; T-EXPECT-ALL 36/36; T-NONREG-R4-1 findings=0 |
| **R41A-01 (c)** | **CLOSED** | T-SPL-PENDING-REALPATH (MANDATORY): real run_real_scenario + evaluate_fixture, stubs for the two fit engines only (A-4 §5.2), expectations pre-written, stubs restored by reassignment with restoration asserted, all touched globals snapshot/restored with equality asserted, register SUMMARY row PIN-SPL-PENDING-REALPATH-STUBS. PASSED in both launches |
| **R41A-01 (d)** | **CLOSED** | T-NONREG-R4-1 (MANDATORY): 37 objects + all stops vs r4-1 (6dd4185b…), canon+sorted, **no whitelist** — findings=0, stops_equal=True; RUN1 canonical observed == named 556106e7…; residual observed == named 3ee624f3…; delivered CSV (item D). T-NONREG-R4 retained: findings=0 |
| **R41A-02** | **CLOSED** | (a) per-attempt custody files, both on disk (attempt1 ae0f0768…, attempt2 766ad7b6… with supersedes_custody filled); writer refuses existing paths; (b) copy-BEFORE-edit applied at the only transition, copy hash == custody-named hash — no reconstruction; (c) launch-numbered log pairs, both intact; launch number env-driven. Structural, verified on disk |
| **R41A-03** | **CLOSED** | end_state.PI_dispatch_record_hash = a3e70509… (D-7 **as observed**, asserted equal to the written value); S-R2-1 source (D-5 0cd87ad5…) in its own fields; distinctness asserted. Run reached exit 0 through all three assertions |
| **R41A-04** | **CLOSED** | the hash block in §6 prints every r4-2 deliverable except this report, AND the three r4-1 hashes A-4 names (register 45a10494…, inventory fedd964a…, attempt log ee5b4862…) as the correction of the r4-1 report §2 (which stays unmodified) |
| **R41A-05** | **CLOSED** | ERRATUM-3 in the r4-2 attempt log: point (d) stated with the r3-log-vs-custody conflict; the six candidate fingerprints RECOMPUTED and the r3 FINAL store COUNTED (exactly two prefixes, 1ba561da… and 548ae790…, none for f882b922…); both references named (r3 log 25316389…; r4 erratum item 3 as the statement corrected); every inference marked as an inference; the unprovable left open |
| **R41A-06** | **CLOSED** | this report and the register describe the INJ-U-POST record as delivered: **two offending pairs, (F, P01, 0) and (M, P01, 0); the record-level sex field is the first hit's (F)**. Code unchanged (byte-identical result, T-NONREG-R4-1). The r4-1 report/register stay unmodified |
| R41A-07 / -09 / -10 / -11 | no action (informational) | per D-7 §3; R41A-07's §4/§7 conflict settled by the r4-2 instruction §4 in favour of §7 (stores stay in place — applied) |
| R41A-08 | NOT APPLIED | optional; excluded by D-7 §3 |

## 6. Hash block (R41A-04): every r4-2 deliverable except this report

| # | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1 | calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py (attempt 2) | b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 |
| 2 | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py (REUSED, no copy) | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3 | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv (REUSED, no copy) | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4 | provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md (final attempt's) | 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1 |
| 4' | provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md | ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e |
| 5 | calibration/f3_step2_telemetry_r4-2_2026-09-30.csv | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d |
| 6 | calibration/f3_step2_results_r4-2_2026-09-30.json | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba |
| 7 | calibration/f3_step2_residual_series_r4-2_2026-09-30.json (byte-identical to r4-1/r4/r3) | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f |
| 8 | calibration/f3_step2_test_evidence_r4-2_2026-09-30.json | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf |
| 9 | calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md (child of 45a10494…) | (sidecar; see transmission list) |
| 11 | provenance/f3_step2_r4-2_start_state_inventory_2026-09-30.md | 66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5 |
| 12 | provenance/f3_step2_r4-2_attempt_log_2026-09-30.md (incl. ERRATUM-3) | (sidecar; see transmission list) |
| A | calibration/f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv (12,174 rows, one pid) | 7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c |
| B | calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv (11,869 rows, pid 10412) | 1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95 |
| D | calibration/f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d |
| D' | calibration/f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv (byte-identical to r4-1's) | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a |
| E | launch1/launch2 stdout+stderr; attempt-1 harness copy; interruption note | 5d58afbb… / d688ac98… / 3af46762… / df257d12… ; 9e4d2803… ; (sidecars) |

The report and the attempt log/register hashes stand only in their sidecars and in the
transmission list (no self-hash; items 9/12 were finalized after this block's other values).

**Correction of the r4-1 report (R41A-04; the r4-1 report `e7939a22…` stays unmodified):**
the three hashes its hash block left as "(sidecar)" are: register
`45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671`, start-state inventory
`fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2`, attempt log
`ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739`.

## 7. Coverage and carried-forward items

COVERAGE_DERIVED = 64 rows, downgraded = []; the only UNCOVERED row remains the authored
`A.5 (iii) inadmissible refit` (D-7 §5 anticipated it; a PI decision, not this revision's).
narrowed_evidence = [T-R2-2] (single-process THIS revision, but the narrowing concerns the
r4 cycle's history; a PI decision, not this revision's). All r4/r4-1 closures stand
(T-NONREG-R4 and T-NONREG-R4-1 both 0 findings).

## 8. Process block and end state

```text
attempts = 2 (9e4d2803 OFF -> b988e962 ON) ; launches = 2 (pids 14804, 10412)
final process = pid 10412, 2026-09-30T20:38:58 .. 21:36:01, exit 0 -- computed ALL 11,869
                units and every result object (T-SINGLE-PROCESS holds)
per-call rows = 12,174 (nr_gates 60 ; unit_tests 1602 ; run1 5256 ; run2 5256 ; export 0),
                all pid 10412
executor_models = claude-opus-4-8[1m] up to the r4-2 instrument verification; claude-fable-5
                  (Fable 5) from the r4-2 scope execution on (the session's configured
                  model changed mid-revision); the harness cannot observe the assistant
                  model -- this records what the session disclosed
commit note   = no commit during the revision (dispatch: "Commit yapma"). After completion
                the PI directed the p_konum_plus branch to be committed and pushed to
                github.com/onertartan/tartan-names (branch p_konum_plus, restart stores and
                quarantined .pkl stores excluded by .gitignore; every store unit remains
                hash-listed in the delivered store manifests). That action is a repository
                operation outside the r4-2 package; the zip and the auditor folder are the
                transmission artifacts.
real_data_access = false (throughout)

END STATE (from results f2a0a4d5..., every field computed):
PI_dispatch_record_hash  = a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb (D-7, observed)
S_R2_1_source            = D-5 0cd87ad5... in its own field ; S-R2-1 = PI_RULE ; T-R2-2 = AUTHORIZE_RESTART
corrections_complete     = true  (30/30 recorded tests, incl. the two new MANDATORY ones)
mandatory_tests_all_run  = true  (missing = [])
expectation_checks       = 36/36 ; EXPECTATION_FAIL = none
non_regression           = vs r4-1: 37 compared, 0 findings, stops equal, canonical and
                           residual at their named values ; vs r4: 0 findings
deferred_decisions = [] ; open_findings = [] ; NATURAL_UNRELATED_EVENTS = 0
narrowed_evidence = [T-R2-2] ; uncovered_coverage_rows = ["A.5 (iii) inadmissible refit"]
parents_unchanged = true ; determinism = true (RUN1 == RUN2 = 556106e7...)
F3_STEP2_r4_status = PARTIAL_PENDING_PI  (exactly the status D-7 S5 declared expected;
                     no other status is claimed; QUALIFIED is not declared by anyone)
F3_EXECUTION_READY = false ; F3_started = false
```
