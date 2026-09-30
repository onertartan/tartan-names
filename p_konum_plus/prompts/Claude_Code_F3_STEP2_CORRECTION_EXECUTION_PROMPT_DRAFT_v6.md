# DRAFT — NOT FOR EXECUTION DISPATCH

# Claude Code Prompt — F3 STEP-2 — Correction Execution (r2 cycle) — DRAFT v6
## Corrections and re-qualification of the STEP-2 r1 adequacy-evaluation harness after the independent audit · child revisions only · no real SSA data · no 6B content · no QUALIFIED declaration by the executor

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`
**Date of draft:** 2026-09-07
**Task class:** CLASS_C implementation correction + synthetic path-coverage re-qualification (the STEP-2 r2 cycle)
**Authority:** Claude Code is execution/provenance authority only; NOT methodology authority, NOT PI authority, NOT an independent auditor
**Status:** DRAFT v6 — NOT FOR EXECUTION DISPATCH. Every MANDATORY field marked `<PENDING>` must be filled by the PI (the optional T-5 may stay blank, §3 P-2), and every dispatch precondition of §3 must hold, before this prompt may be dispatched

```text
prompt_id                  = Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
status                     = DRAFT — NOT FOR EXECUTION DISPATCH
addressee / author         = addressed TO Claude Code (the future executor); DRAFTED BY Claude
                             (chat; independent/advisory auditor and prompt author). The
                             `Claude_Code_…` file-name prefix denotes the addressee, never the
                             author; nothing in this lineage was produced or executed by Claude Code
draft_revision             = v6 (child revision; v1 … v5 retained byte-unchanged as historical)
parent_draft               = Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v5.md
                             a0fbbb1b3c0ba33654ea50f9241c655b4af8e1e98274355ae255cda81e6c8866
draft_lineage              = v1 a1b8a2e62b3ae300f639e02aa206b9a53d55a413dd0a167e1dd9a76d4b59c1cd
                             -> v2 3c10b9fe… -> v3 72f26d31… -> v4 4549c909… -> v5 a0fbbb1b…
                             -> this v6
v5 -> v6 revision_reason   = §16 feedback (Claude_Chat_F3_STEP2_v5_section16_feedback.md, ChatGPT,
                             721243ff7fce42f539db0bc3fa895059e427120538772d72aa05e9f5789995cd),
                             items S16-01 / S16-02: five §16 rows were in the wrong group or stated
                             a readiness condition §2 / §3 do not impose, and the review-history row
                             was stale. §16 now summarises §2 / §3 without adding, relaxing or
                             inventing any execution rule. DOCUMENT_ONLY, diff limited to §16, this
                             revision note and the version / lineage fields; the audit r6 and
                             reconciliation r5 candidates are unchanged and still referenced by the
                             same hashes; no S / T option selected, no PENDING field resolved, no
                             test run, no implementation executed
v4 -> v5 revision_reason   = narrow feedback on the v4 package (Claude_Chat_F3_STEP2_v4_narrow_
                             feedback.md, ChatGPT, 84e46b7cf2cc30af3a3413eb61f1d703b42cbaac8d7fa41530d5055518c9cf54):
                             C-02 — the source-hierarchy line read "accepted audits", which would
                             have covered the editorial correction candidates listed under it;
                             plus the current pointers to the audit r6 / reconciliation r5
                             candidates, the recorded Kimi v4 review (reported, not observed here),
                             the explicit authorship line above, and the §16 split of contract-
                             mandatory items from record / transmission items. DOCUMENT_ONLY: no
                             S / T option selected, no PENDING field resolved, no requirement added
                             or relaxed, no test run, no implementation executed
v3 -> v4 revision_reason   = U-set correction instruction (Claude_Code_F3_STEP2_v3_Uset_correction_
                             instruction.md, f37d3310c868a1a62493714499f6f40a4c085da3e4774de976810ee87a642f1a),
                             items D-01 … D-05. D-01/D-02: X-07 and its test contracts returned to
                             the FROZEN criterion-valid common supports of r4 §9.2 as ratified by
                             record r1 §3 item 4.1 — the v3 "U5 from completion flags only" wording
                             (inherited from the audit finding AUD-18 and, before that, from §5 of
                             the dispatched v5 prompt) misstated the frozen rule and is withdrawn;
                             D-04: the F2 non-regression replay start bank bound explicitly to each
                             F2 fixture's own declared construction; D-05: narrow provenance and
                             narrative corrections. DOCUMENT_ONLY: no S / T option selected, no
                             PENDING field resolved, no test run, no implementation executed
v2 -> v3 revision_reason   = document-correction instruction (Claude_Code_F3_STEP2_DRAFT_v2_to_v3_
                             document_correction.md, ChatGPT), items V3-01 … V3-06: two execution
                             contradictions (write order vs the pre-execution custody record;
                             PIN-EXC-CAPTURE applicability under T-1 = REFUSE) and four text
                             inconsistencies (§4.3 field schema, the version label, the P-1 sidecar
                             exception, the NR-SPL reporting vocabulary). DOCUMENT_ONLY: no S / T
                             option selected, no PENDING field resolved, no scope added or removed,
                             no implementation executed
v1 -> v2 revision_reason   = external review of v1 (Claude_Chat_F3_STEP2_DRAFT_v1_feedback_for_v2.md,
                             ChatGPT, d5a0eef1db139ee716a44a7aab7f302ca5a3d88db230288176f350bf1a7888e6),
                             items R-01 … R-06 — internal-consistency corrections only; no new
                             scientific content, no S / T option selected, no scope added
predecessor (executed)     = Claude_Code_F3_STEP2_CLASS_C_IMPLEMENTATION_PIN_PROMPT_v5_2026-09-06.md
                             1532a5e481946d7c64d2ac5025ef16372b1f6530ab4fbc8aa5567392f18cf0af
                             (produced the STEP-2 r1 package now under correction; retained as lineage)
basis (audit tier)         = f3_step2_independent_audit_DRAFT_r4_2026-09-07.md
                             54e641e48b2d00c59520f27339427a21b024408dae1bd5b5fbe233cdd4b67427
                             f3_step2_cross_auditor_reconciliation_r3_2026-09-07.md
                             85c21bd3c86c8da9281fa696d33a110db4faca7f5b2ef660ee8f2e7061634331
                             + the EDITORIAL CORRECTION CANDIDATES that correct AUD-18 and its
                             reachability wording (cited as candidates, NOT as accepted audits, and
                             load-bearing for nothing beyond the D-01 / C-01 wording):
                             f3_step2_independent_audit_DRAFT_r6_editorial_correction_candidate.md
                             12c1532216f3da9e4b64b51b1e5426d9d77d13de9d6fa6cb44fa43374667ed94
                               (current; review status: NOT yet reviewed by any external auditor)
                             f3_step2_cross_auditor_reconciliation_r5_editorial_correction_candidate.md
                               (current companion; review status: NOT yet reviewed) — hash in §2.3 item 27
                             f3_step2_independent_audit_DRAFT_r5_editorial_correction_candidate.md
                             7a67de9f080d95132dc44c87238cfaf6819f75e92afdcdd7ed7b9a83bba29647
                             f3_step2_cross_auditor_reconciliation_r4_editorial_correction_candidate.md
                             0359bb9b938bdbbf119af6e48c101ce18b8a65dcfd587f53cf740f18ddf769aa
                               (parents of the two above; covered by the reported Kimi v4 review and
                                the ChatGPT v4 feedback — reviewed, NOT accepted, NOT independently
                                requalified)
                             (audit tier: these records identify defects and options; they are NOT
                              normative and do not replace v11, the frozen gate artifacts or the
                              ratified F3 STEP-1 contract. Where any audit-tier record and the
                              frozen contract disagree, the frozen contract governs — the D-01
                              correction of this revision is an instance of exactly that.)
source hierarchy           = v11 → F2 FINAL FREEZE r1 + accepted F2 execution artifacts → r4 as
                             ratified by freeze record r1 → audit records, INCLUDING editorial
                             correction candidates (each with its actual review and acceptance
                             status recorded in the basis block; citation of a candidate implies no
                             formal acceptance and no independent verification) → this prompt →
                             historical provenance. Historical or superseded material never
                             overrides a frozen artifact; on any conflict v11 wins.
frozen contract            = r4 5e594136… AS RATIFIED BY record r1 7055f186… ; v11 d136502f…
PI decisions embedded      = 0            S / T options selected by this draft = none
new_scientific_literal_by_executor = 0    (PI-ratified content is separate: §4.3)
F2_reopening = false ; F3_STEP1_reopening = false ; new_methodology_review = false
```

---

## Revision response — §16 feedback items S16-01 / S16-02 (deliverable of the v6 revision)

| item | finding (v5) | changed section | correction | remaining open |
|---|---|---|---|---|
| S16-01 | five §16 rows sat in the wrong group or implied a condition §2 / §3 do not impose: the r1 §15 end-of-task table and the ADDENDUM A r1 / v2–v4 prompt imports were listed as mandatory although they are record-class; the dispatch-time prompt hash was in the record group although P-4 makes it a precondition; T-5 sat inside the mandatory table; the missing r1 sidecars read as an unconditional pre-dispatch delivery | §16 (A / B tables and the intro) | rows regrouped to match §2 / §3 exactly: record-class items moved to B with their import / recording work preserved; the prompt-hash row moved to A and restated as the P-4 equality check; T-5 moved out of the mandatory table into its own optional-field note; the sidecar row rewritten around the §2.2 item 19 / P-1 exception (a MISSING sidecar is not a STOP and is created only in the permitted-write stage; a PRESENT sidecar that disagrees with its file is a mismatch and fails P-1) | none — §16 imposes no requirement of its own and relaxes none |
| S16-02 | the review-history row still read "this v4" / "further review … as v5" | §16 group B | the row records the actual history: v4 package reviewed by the Kimi v4 review (reported) and the ChatGPT narrow feedback; v5 applied C-01 / C-02 and their closure was checked by the §16 feedback; v6 is this §16 classification correction. A document review is not an independent verification of implementation adequacy, and no new audit round or PI approval is requested by it | none |

---

## Revision response — v4 feedback items C-01 / C-02 (retained from the v5 revision)

| item | finding (v4 package) | changed section(s) | correction | remaining open |
|---|---|---|---|---|
| C-01 | the audit candidate's AUD-18 evidence block inferred categorical unreachability through the fitting path from "rho and sst are produced only for crossfit-complete trajectories" | (outside this prompt) audit r6 candidate 12c1532216f3da9e4b64b51b1e5426d9d77d13de9d6fa6cb44fa43374667ed94 ; reconciliation r5 candidate | the paragraph now states that the counterexamples are decision-layer injections whose reachability through the actual fitting path was NOT verified, and that they establish neither reachability nor unreachability — only compliance with the criterion-specific common-set contract. AUD-18's substance and its gate-specific-blocker classification are unchanged | none — no run was started to settle reachability, and none is requested |
| C-02 | the `source hierarchy` line said "accepted audits (above)" while the block above it also lists editorial correction candidates awaiting independent review | this §0 header (source hierarchy, basis block) ; §2.3 items 27–28 ; §16 | the line now reads "audit records, including editorial correction candidates", each with its actual review / acceptance status, and states that citation implies no acceptance; v11 and the frozen / ratified contract keep precedence over the whole audit tier | none — the favourable findings of the narrow reviews are not converted into any qualification approval |

---

## Revision response — U-set correction items D-01 … D-05 (retained from the v4 revision)

| item | finding (v3) | changed section(s) | basis | correction | remaining open |
|---|---|---|---|---|---|
| D-01 | X-07 defined the consulted common supports by fold-fit completion ("U5 from completion flags only"), which is not the frozen rule | §5 X-07 ; §6 STOP labels ; §8 row label | r4 §9.2 (5e594136…) as ratified by freeze record r1 §3 item 4.1 / 4.2 (7055f186…), quoted verbatim in X-07 | each consulted subset-defined level builds ONE criterion-specific common-valid set from the validity of THAT level's required statistic for the fitters the frozen definition names (U2, U3, U4, U5), and both candidates' statistics are computed on that same set; construction-time exclusion of an invalid observation is the frozen construction, never a STOP and never an imputation; the empty-U STOP and the post-construction inconsistency STOP stay distinct and narrow; P03 entry conditions are unaffected | none — no completion-based alternative is designed, no new validity rule, tolerance or threshold is introduced |
| D-02 | the dependent test expectations, fixture names and reporting rows carried the same error (one of them expected a STOP for an ordinary exclusion) | §5 X-07 tests ; X-09 ; X-14 ; §7 fixtures ; §11 register ; §14 rows | same as D-01 | five distinguishable test contracts with explicit names: C2 rho-invalid exclusion, C5 independence from C2, C5 sst-invalid exclusion (|U5| = 9 for both candidates, no STOP), post-construction inconsistency (contract-consistency STOP), empty consulted set (existing degenerate STOP); old → new fixture names mapped in §7 | none — the tests are contracts for the future run; none was executed by this revision |
| D-03 | the audit finding AUD-18 and the reconciliation rows that justified the v3 wording | (outside this prompt) | same as D-01 | corrected in two separate child candidates: `f3_step2_independent_audit_DRAFT_r5_editorial_correction_candidate.md` and `f3_step2_cross_auditor_reconciliation_r4_editorial_correction_candidate.md` — both EDITORIAL CORRECTION CANDIDATES, independent review pending; cited in this prompt as candidates, never as accepted audits | independent review of both candidates |
| D-04 | T-2a / T-2b and X-03 did not bind the start bank used by an F2 non-regression replay | §4.2 T-2 ; §5 X-03 | F2 FREEZE r1 fixture constructions; v5 §3.1 | an F2 replay fixture uses the start bank of its OWN declared F2 construction (composition, order, feature-start behaviour), passed explicitly; the F3 FULL_LATTICE default is never applied implicitly to an F2 replay; a similar result obtained with a different bank does not satisfy an exact replay | none — no claim is made about whether the T-2a adapter will succeed, and no NR result is declared |
| D-05 | stale review-lineage sentence in §16; §15 wording about the auditor environment; review-file provenance | §2.3 ; §15 ; §16 | — | §16 records the real v1 → v2 → v3 → v4 history; §15 states "auditor-environment consistency check; no claim of reproducing executor hashes" and makes no unevidenced assumption about environment identity; the Kimi v3 review is recorded as referenced-but-not-provided with no invented hash, and "not provided" is kept distinct from "absent from the repository" | the Kimi v3 review file itself (and any earlier Kimi review files) — to be hashed when supplied |

---

## Revision response — v2 review items V3-01 … V3-06 (retained from the v3 revision)

| item | finding (v2) | changed section(s) | correction | remaining open |
|---|---|---|---|---|
| V3-01 | §3 put the pre-execution custody record before "the remaining deliverables", but §12 item 4 requires that record to carry the NEW harness hash — the harness was in the later group | §3 write order ; §12 items 1–4 | write order restated as five dependency-ordered stages: read-only checks → permitted sidecar / import writes → prepare harness, generator and manifest → hash them and write the pre-execution custody record → first test / run, then results and report. The manifest is still written and hashed BEFORE any run, and the custody record now names the exact harness bytes that will be executed | none — the order is documented only; no step is executed by this task |
| V3-02 | §4.5 stated that PIN-EXC-CAPTURE "runs under every S-2 value", while T-1 = REFUSE removes the loaded spline namespace the test needs | §4.5 (S-2 and T-1 blocks) ; §5 X-02 ; §7 ; §14 | applicability split: under T-1 = AUTHORIZE the exception-capture test applies for every S-2 value including DEFERRED; under T-1 = REFUSE the test and its injection fixture are NOT_RUN(T-1 REFUSE), never PASS, and the evidence gap stays visible; tests without a spline dependency are unaffected | none — no T-1 or S-2 value is selected |
| V3-03 | §4.3 required a value "for each of S-1, S-2, T-1 … T-5", contradicting P-2 / P-3 where T-5 may be blank | §4.3 | schema aligned: S-1, S-2, T-1 … T-4 mandatory; T-5 optional, blank permitted with the status-quo meaning of §4.2, creating neither a PENDING nor a new approval requirement | none |
| V3-04 | the front-matter Status line still read "DRAFT v1" | title ; Status line ; prompt_id / draft_revision / parent / lineage | version fields consistent at v3 with v2 as the direct parent; historical v1 / v2 references and the R-01 … R-06 response retained unchanged | none |
| V3-05 | P-1 said "every §2.1 and §2.2 item present and exact", which read across the item-19 sidecar exception | §3 P-1 (with §2.2 item 19 and the §2 STOP scope) | P-1 states the exception explicitly: a MISSING r1 sidecar is recorded NOT_LOCATED and created later in the permitted-write stage; a PRESENT sidecar that disagrees with its file is a mismatch and STOPs. No other mandatory check is relaxed | none |
| V3-06 | §14 offered only PASS/FAIL for NR-SPL although §8 allows NOT_RUN(T-1 REFUSE) | §14 fields and response table | NR-SPL (and every NR field / row) reports PASS / FAIL / NOT_RUN(reason); the response-table result column accepts NOT_RUN(reason) so that a test which did not run is never forced into PASS or FAIL | none |

---

## Revision response — v1 review items R-01 … R-06 (retained from the v2 revision)

| item | finding (v1) | changed section(s) | correction | remaining open |
|---|---|---|---|---|
| R-01 | optional T-5 (blank allowed) contradicted P-2 / P-3, which turned every blank field into PENDING ⇒ STOP | §3 P-2 / P-3 ; §4.2 T-5 ; §4.3 schema | MANDATORY decision fields (S-1, S-2, T-1 … T-4) separated from the single OPTIONAL field (T-5); a blank T-5 is a permitted value with the status-quo meaning defined in §4.2, is not PENDING and never STOPs on its own; a missing MANDATORY value is PENDING and STOPs | none — the meaning of a blank T-5 is unchanged (status quo), not a new approval |
| R-02 | custody STOP scope swept in record-class files; item 19 created sidecars before the preconditions allowed any write; the PI decision file was record-class yet mandatory in §3 | §2.2 item 19 ; §2.3 (dispatch-class added) ; §2 tail ; §3 write order | STOP scope limited to §2.1, §2.2 and the dispatch-class items; historical record-class absence ⇒ NOT_LOCATED only; §2 verification is read-only; permitted writes begin only after P-1 … P-4 pass (STOP report is the sole exception); a sidecar created now is contemporaneous custody of current bytes, never retrospective verification of the r1 run | none |
| R-03 | REFUSE / DEFERRED options could stop paths that §8 nevertheless required unconditionally | new §4.5 dependency table ; §8 | per-option table: paths enabled / stopped (with finding id) / tests applicable / tests NOT_RUN(authorized reason) / rerun scope / status effect; NOT_RUN ≠ FAIL ≠ PASS; unaffected work continues; global STOP scope restated; S-1 alone does not make the C4 paths runnable (family and, for C4b, spline paths must also be enabled) | none — no combination is selected here |
| R-04 | X-08 collapsed family P03 status and mechanism outcome ("PENDING only if no family has a definite failure") | §5 X-08 ; §7 fixtures | two separate rules: family P03 status (FAIL on any definite failure, PENDING only without one) and mechanism outcome from the two family statuses, where ANY PENDING ⇒ MECHANISM_UNDETERMINED_PENDING_EXACTNESS(<ids>) — a definite FAIL in one family never establishes the other's PASS; recorded as a STEP-2 mode label, not a new scientific rule | none |
| R-05 | the boundary between CORRECTED_PENDING_INDEPENDENT_AUDIT and PARTIAL_PENDING_PI was fuzzy (PI-deferred findings excepted) | §13 ; §14 | deterministic, mutually exclusive status computation from six separately reported fields (corrections_complete, mandatory_tests_all_run, deferred_decisions, narrowed_evidence, uncovered_coverage_rows, open_findings); engineering completion is reported separately from gate scope; deferral / refusal / narrowing / NOT_RUN never support a claim that the original scope was met | none |
| R-06 | wrong internal references (§12 = Deliverables cited for the S-2 deferred wiring; §13 cited for the exactness protocol) | §1 ; §4.3 ; §4.4 ; §5 X-02 ; §7 ; §14 | references corrected to §4.1 (S-2 DEFERRED wiring) and §10 (exactness protocol); external "v5 §12" references left unchanged (they point to the dispatched v5 prompt) | none |

---

# 0. Purpose

Apply, to the STEP-2 r1 harness, (i) the PI-ratified content of §4.3 (only what the PI has
explicitly ratified; absent ⇒ PENDING), (ii) the task-scope authorizations of §4.2 (only those
the PI has explicitly authorized), and (iii) the exact engineering corrections of §5; then re-run
the synthetic qualification with the dependency-scoped coverage of §8 and deliver r2 child
revisions of every STEP-2 artifact (§12). Fixture outcomes remain `interpretation =
PATH_COVERAGE_ONLY`. The executor records findings and STOPs where the contract is silent; it
never chooses. The executor does not audit its own output and never declares QUALIFIED (§14).

---

# 1. Starting state and firewall (binding)

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false
F3_STEP1 = FROZEN (r4 5e594136… as ratified by record r1 7055f186…) ; F3_STEP1_open_PI_rows = 0
F3_STEP2 r1 package        = audited ; audit verdict = NOT PASSED (audit DRAFT r4)
F3_STEP2_status            = PARTIAL_PENDING_PI (executor r1 claim, confirmed by the auditor)
F3_STEP2 = QUALIFIED       = NOT declared
F3_EXECUTION_READY = false ; F3_started = false
real_data_fit = false ; adequacy_measurement = false ; generator_selected = false
P03_threshold_values = NOT_COMPUTED (must remain so)
6B_companion = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED (separately governed; not in this task)
```

Prohibited throughout this task (firewall; any breach ⇒ STOP, global blocker):

```text
real SSA / F1 trajectory access (no read, no path, no import, no "resemblance by construction")
P03 empirical threshold computation on real data ; adequacy measurement ; generator comparison /
  selection ; F4 refit ; algorithm × CVI outcome access
6B companion content (spec, code, fixtures, fields, statistics)
modification of any frozen artifact: F2 engine 01714752…, spline r2 harness b31e5a6b…, r4, record r1,
  the r1 STEP-2 files (§2.2 — they are read-only parents)
any new SCIENTIFIC literal, tolerance, threshold, definition or rule by the executor
any scientific choice (§10) ; any RNG outside manifest-declared fixture generation (recorded seeds)
any surrogate / reconstructed / "closest" file standing in for a custody item (§3)
declaring QUALIFIED, PASS-as-verified, or any independent-verification wording (§14)
```

---

# 2. Custody — verify before any write

## 2.1 STOP-class (mismatch or absent ⇒ `STOP = true ; global blocker ; artifact_mutation = prohibited ; report observed vs expected`)

```text
 1. ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md    d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3
 2. f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md          ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43
 3. f2_step2_feasibility_harness_r3_2026-09-01.py   (frozen F2 engine)          01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077
 4. f2_step2_fixture_manifest_2026-09-01.csv                                   daa5fd08f44420ec8eed728c6c5e3e4adcbac1a9a8b19f891aacf0f38251979b
 5. f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv                     c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666
 6. f2_d_f2_09_exact_initialization_decision_packet_2026-08-30.md              8ff70a64b8425d283d2cda52668583fffeb3ae5901da0877b02a83b7d0f0f9f6
 7. f2_step2_feasibility_telemetry_r3_2026-09-01.csv                           cd7218b14e883d3befefcdce01681989d4596a8c083976ee0a6ed5a20424ee49
 8. spline qualification bundle r2: manifest e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32
                                    harness  b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d
                                    results  ffda04b01abb1dd5399e7fb6434c006616723bf6ba7d95bfc697baeb6dd40484
 9. f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md              5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad
10. f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md                    7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460
11. f3_step1_pi_ratification_freeze_record_2026-09-05.md  (parent; historical) bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f
```

## 2.2 STOP-class — the STEP-2 r1 package (read-only parents of every r2 deliverable; byte-unchanged at the end of the task)

```text
12. p_konum_plus/calibration/f3_step2_adequacy_harness_r1_2026-09-06.py        a95ad152b1ebcca6ff8b9ccfd34d122b9d6225a44d51254f4621fd4776a5b12f
13. p_konum_plus/calibration/f3_step2_fixture_generator_r1_2026-09-06.py       <PENDING — hash never delivered to the auditor; record the observed value>
14. p_konum_plus/calibration/f3_step2_fixture_manifest_2026-09-06.csv          d9fb75f8c643f53a67032e4b65a5bec1af85ccbdf1cb47c58577c1d3f23b565b
15. p_konum_plus/calibration/f3_step2_telemetry_r1_2026-09-06.csv              3ee208e72cc9d4f83b5d7d696f7252499c971480bc75e9aaabf6f51dbe0b08e0
16. p_konum_plus/calibration/f3_step2_results_r1_2026-09-06.json               e32de3f7ae43d39c87a21384a46fe84c42c940d7a48bd2cdb83fe2d4d29f06eb
17. p_konum_plus/calibration/f3_step2_class_c_pin_register_r1_2026-09-06.md    03486232ac62206b1eed52c2355e465364ec10fc02fb13d62dd32e2dfd50f9ca
18. p_konum_plus/provenance/f3_step2_synthetic_qualification_report_r1_2026-09-06.md 413283efd5f5212d3c5bb0b5a5a0be3c22adc2fad41c6a4ab142733fbdde2b95
19. external .sha256 sidecars of 12–18: VERIFY each present sidecar against its file (read-only,
    during the §2 checks); a missing sidecar is recorded NOT_LOCATED here and is CREATED later, as a
    permitted write after the §3 preconditions pass (§3 write order), as a custody action only:
    it attests the CURRENT bytes of an r1 file; it is NOT retrospective evidence about the r1 run
    and is never presented as independent verification (external file; no self-hash; parents untouched)
```

## 2.3 Dispatch-class (items 24, 25: mandatory — absence or mismatch ⇒ STOP via §3) and record-class (items 20–23, 26: mismatch ⇒ cleanup; absent ⇒ import byte-exact from the PI attachment if attached, else NOT_LOCATED — never a STOP)

```text
20. f3_step2_independent_audit_DRAFT_r4_2026-09-07.md                          54e641e48b2d00c59520f27339427a21b024408dae1bd5b5fbe233cdd4b67427
21. f3_step2_cross_auditor_reconciliation_r3_2026-09-07.md                     85c21bd3c86c8da9281fa696d33a110db4faca7f5b2ef660ee8f2e7061634331
22. ADDENDUM_A_r1_to_Claude_Code_F3_STEP1_r1_v6_NARROW_EXACTNESS_CORRECTION_PROMPT_2026-09-03.md
                                                                               cc4f97b488f88e7c3f4542a9b8e51ef33ff222b048a8ff44453baa8742a7258b
                                                                               (r1 custody item 17 NOT_LOCATED — import to p_konum_plus/prompts/ ; AUD-13)
23. Claude_Code_F3_STEP2_CLASS_C_IMPLEMENTATION_PIN_PROMPT_v2/v3/v4_2026-09-06.md
                                                                               7928820b… / 05e0afe9… / 3465ee9b…  (import if attached; AUD-13)
24. [DISPATCH-CLASS] f3_step2_pi_ratified_content_<date>.md   (PI-owned; §4.3)   <PENDING — supplied by the PI at dispatch; observed hash recorded>
25. [DISPATCH-CLASS] this prompt — record its observed SHA256 from the dispatched file (canonical
    name, dashes; a download variant renamed byte-unchanged before dispatch)
26. audit lineage (historical; hashes recorded, not re-audited): audit drafts af073c9b… / 0ffb57b0… /
    a664fc40… / d79f5214… / 54e641e4… ; reconciliations 64392840… / 9f4233d2… / 4e3c1892… /
    85c21bd3… ; preflight 1c6618bd… ; external audits eddb056f… (ChatGPT) / 107eb40a… (Kimi) ;
    feedback 7a2495d9… / 9e38f768… / 00b11398… / d5a0eef1… ; U-set correction instruction f37d3310…
27. editorial correction candidates (cited as candidates, never as accepted audits):
    CURRENT — audit r6 candidate 12c1532216f3da9e4b64b51b1e5426d9d77d13de9d6fa6cb44fa43374667ed94 ;
    reconciliation r5 candidate 377d70405d975daaa5f486cbe2298863b43e74e3a7ea100772ae2b6afcd68b15  (both: independent review PENDING, not reviewed by
    any external auditor)
    PARENTS — audit r5 candidate 7a67de9f080d95132dc44c87238cfaf6819f75e92afdcdd7ed7b9a83bba29647 ;
    reconciliation r4 candidate 0359bb9b938bdbbf119af6e48c101ce18b8a65dcfd587f53cf740f18ddf769aa
    (reviewed by the reported Kimi v4 review and the ChatGPT v4 feedback; reviewed ≠ accepted)
28. external reviews of this prompt lineage — record-class provenance, never a dispatch condition:
    Kimi review of prompt DRAFT v4 (`f3_step2_correction_prompt_draft_v4_review_2026-09-07.md`),
    hash REPORTED by the v4 feedback as
    ef71acdccf2ecb7eb32d105b50e1a2a9f6dc41126da85bbb09dd051a9061757a — NOT provided to the drafting
    session and therefore NOT observed here; re-observe when the file is supplied. Reported outcome:
    no global blocker, no gate-specific blocker, no cleanup for v4; five informational items;
    U-set and replay-bank objections closed — a document/artifact review, not a test run.
    Kimi review of prompt DRAFT v3 — referenced by the U-set correction instruction; not provided;
    no hash observed or invented. Earlier Kimi review files (v1 / v2 review, audit r2) — likewise
    not provided, not hashed. ChatGPT feedback records: d5a0eef1… (v1 review), 9e38f768… (v2→v3),
    84e46b7c… (v4 narrow feedback). "Not provided" is not a claim that a file is absent from the
    repository, and no file transfer to any party is claimed
```

Surrogates are prohibited: no reconstructed, regenerated or "equivalent" file may be used in place
of any item above, for any purpose, including tests.

STOP scope (exact): absence or hash mismatch of any item of §2.1, §2.2 or of the dispatch-class
items 24 / 25 ⇒ STOP with the item named. Absence of a record-class item (20–23, 26) ⇒ record
NOT_LOCATED (with the import action of X-15 where applicable) and continue — a historical
record-class file never STOPs the task. A missing sidecar under item 19 is likewise not a STOP.

Repository state: record root / branch / HEAD and `git status` at start; preserve every existing
user modification; `commit = false`.

---

# 3. Dispatch preconditions (binding; evaluated by the executor at start, before any implementation)

```text
P-1  every §2.1 and §2.2 item present and exact (no surrogate); §2.2 item 13 hash recorded.
     Sidecar exception (§2.2 item 19; §2 STOP scope): a MISSING r1 sidecar does NOT fail P-1 — it
     is recorded NOT_LOCATED and created later, in the permitted-write stage of the write order;
     a PRESENT sidecar whose value disagrees with its file IS a mismatch and fails P-1. No other
     mandatory check of §2.1 / §2.2 is relaxed by this exception
P-2  the PI-ratified content file (§2.3 item 24) present and hash recorded, containing:
       MANDATORY fields — S-1, S-2, T-1, T-2, T-3, T-4: each with an explicit value from its
         allowed set (an explicit DEFERRED / REFUSE counts as a value); missing or blank = PENDING
       OPTIONAL field — T-5: may be present with a value OR blank/absent; blank is a permitted
         value whose meaning is fixed in §4.2 (status quo: the r1 rebinding mechanism is retained);
         a blank T-5 is NOT PENDING and never causes a STOP
P-3  no MANDATORY field of §4.1 / §4.2 remains PENDING after reading item 24
P-4  the observed hash of this prompt equals the value the PI recorded at dispatch
write order (binding; dependency-ordered): every §2 custody check and every §3 evaluation is
     READ-ONLY; no file is created or modified before P-1 … P-4 all pass. The single exception is
     the STOP report below. After they pass, the stages are:
       W-1  permitted custody writes: missing r1 sidecars (§2.2 item 19, custody action only) and
            record-class imports (X-15)
       W-2  prepare the r2 harness and the r2 fixture generator (§12 items 1 and 2) and write the
            r2 fixture manifest (§12 item 3) — the manifest is written and hashed BEFORE any run
       W-3  compute the SHA256 of the prepared harness, generator and manifest and write the
            pre-execution custody record (§12 item 4); it must name the exact harness bytes that
            will be executed, so it is written AFTER W-2 and BEFORE any test or run
       W-4  first test / run: NR-01 (i), then the other applicable non-regression gates (§8), then
            RUN1 and RUN2
       W-5  the remaining deliverables: telemetry, results, residual series, test evidence,
            register, correction report, and their external sidecars (§12 items 5–11)
     A file prepared in W-2 is not executed before its hash is recorded in W-3; a deliverable of
     W-5 is never hashed into the W-3 record.
if any of P-1 … P-4 fails:  STOP before any implementation ; report the failing precondition, the
     observed vs expected values and the PENDING MANDATORY fields ; write nothing except the STOP
     report (p_konum_plus/provenance/f3_step2_r2_dispatch_precondition_stop_report_<date>.md)
```

---

# 4. S / T / X register — decision fields (nothing is selected by this draft)

Legend. **S** = PI scientific decision (bounded options only). **T** = task-scope authorization
by the PI as dispatcher (no scientific content; some options NARROW the evidence contract and are
labelled so). **X** = exact engineering correction by the executor under this task, no further
authorization. Classification of the underlying finding, gate effect, closure action and
authority are in audit DRAFT r4 §3; they are not re-argued here.

## 4.1 S — PI scientific decisions (both fields MANDATORY at dispatch, §3 P-2)

```text
S-1  F3-STEP2-EXACT-01 — A.5 condition (i): "the trajectory's entire Kural-S support region"
     gap        no frozen data-level definition (audit r4 AUD-01; ADDENDUM A r1 states the outcome
                only; F2 Kural S is defined on stabilized fitted curves)
     decision   = <PENDING>
     allowed    (a) PI supplies an operational data-level definition, verbatim, incl. equality /
                    empty / multi-part support and mask-containment semantics, outcome-blind
                (b) PI designates the fitted curve on which (i) is evaluated (which fitter's
                    curve, which fit) and the containment semantics, verbatim
                (c) PI removes condition (i) — NOT implementable in this cycle: it alters the
                    ratified r4 §3 text and requires a ratification cycle; if chosen, the C4 paths
                    stay STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-01) in this cycle
                DEFERRED_THIS_CYCLE — the r1 wiring stays (C4a / C4b / D-P04 4a-4b real paths
                    PENDING; A.5 (ii)/(iii) unit-tested only; no C4 fixture outcome)
     wiring if (a) or (b): PIN-A5-SUPPORT implemented VERBATIM from §4.3, with test T-A5-SUPPORT
                (§5); the C4 real paths are re-enabled and covered (§7, §8)
     note       candidates a1 / b1 listed in audit r4 AUD-01 are observations, not accepted text;
                c1 was withdrawn; nothing here pre-empts the PI's choice

S-2  F3-STEP2-EXACT-02 — SOLVER-B behaviour when the KKT-existence certificate cannot be computed
     gap        frozen r4 §5 / r2 harness silent on an nnls RuntimeError inside accept(); the r1
                harness implemented "mode invalid, chain aborted" (audit r4 AUD-02)
     decision   = <PENDING>
     allowed    α  unverifiable acceptance at stage k ⇒ NOT accepted at stage k; the frozen chain
                   continues (stage 2 expansion, then stage 3 SLSQP whose acceptance needs no KKT
                   term) — requires a disclosed runtime wrapper around the loaded accept(); no
                   file edit
                β  mode numerically invalid, excluded from equivalent_mode_set (the r1 behaviour)
                γ  spline_fit_status = FAILURE for the trajectory fit
                δ  STOP with provenance investigation (no automated continuation)
                DEFERRED_THIS_CYCLE — v5 §12 wiring: on the event the spline fit for that context
                   returns STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-02) (not FAILURE, not "invalid
                   mode"); every dependent statistic of that context is PENDING; the r1
                   continue-rule is REMOVED
     wiring     in every case: PIN-EXC-CAPTURE (§5 X-02) records stage, exception type, message
                and traceback per event; the chosen rule is implemented VERBATIM from §4.3
```

## 4.2 T — task-scope authorizations (PI as dispatcher; no scientific content)
T-1 … T-4 are MANDATORY fields; T-5 is the single OPTIONAL field (§3 P-2).

```text
T-1  PIN-SPLINE-LOADER retain rule (audit r4 AUD-03 / AUD-23)
     decision   = <PENDING>      allowed: AUTHORIZE | REFUSE
     AUTHORIZE  the retain rule is widened, for the frozen file b31e5a6b… only, to the explicit
                node list: v5 §3.3 classes (Import / ImportFrom / FunctionDef / ClassDef /
                constant Assign) PLUS the definitional-support nodes lexically before the
                orchestration marker "# ---------------- steps 1-3": U, KNOTS, TC_OPTS,
                SLSQP_OPTS, B, the two asserts on B, D1 and its for-loop, C_INT, C_DEC, C_INC,
                C_RIGHT, MASKS, COEF_MAP, CFG_FIELDS, the docstring Expr, the thread-env loop
                and the three path strings — exactly the 21 prelude nodes recorded in the r1
                results JSON; nothing else; every retained and prelude node hashed (§5 X-01)
     REFUSE     F3-STEP2-ENG-02 recorded; the spline path is STOP for this cycle; every
                spline-dependent statistic PENDING; no re-implementation of the solver
     evidence scope: unchanged (the spline non-regression remains the acceptance test)

T-2  NR-01 wrapper qualification (audit r4 AUD-08)
     decision   = <PENDING>      allowed: T-2a | T-2b | DEFERRED
     T-2a       a fixture-type-dispatching qualification adapter: the two fitting fixtures
                FIX-P01-BENIGN / FIX-P02-BENIGN through fit_family(mask = FULL); every other F2
                fixture through its frozen construction unchanged; the assembled canonical
                document must equal 6f197b74… in the executor environment. Start-bank binding
                (D-04): each replayed F2 fixture uses the start bank of its OWN declared F2
                construction — composition, order and feature-start behaviour — passed explicitly;
                the F3 FULL_LATTICE default of X-03 is never applied implicitly to a replay
                fixture, and a similar result obtained with a different bank does not satisfy the
                exact-replay requirement. Evidence scope: unchanged (v5 §3.1 wording satisfied
                literally). Satisfiability is to be DEMONSTRATED by the executor; if it cannot be,
                record F3-STEP2-ENG-03 and STOP the wrapper-qualification path (do not fall back to
                T-2b without authorization). This prompt makes no prediction about whether that
                demonstration will succeed
     T-2b       restatement: frozen-suite replay through the loaded engine (hash 6f197b74…) +
                FIX-P01-BENIGN / FIX-P02-BENIGN through fit_family(mask = FULL) with
                terminal_endpoint_hex equality to the frozen FAMILY_SELECTED records. Start-bank
                binding (D-04) as in T-2a: each benign fixture is replayed with the start bank of
                its own declared F2 construction, passed explicitly — the F3 default is not applied
                to it, and endpoint equality obtained under a different bank does not satisfy the
                check. Evidence scope: NARROWED — the wrapper-assembled canonical document is
                dropped; engine identity + wrapper fitting equivalence on the two fitting fixtures
                are kept. Choosing T-2b is an instruction change and is recorded as such.
     DEFERRED   NR-01 (ii) remains NOT PERFORMED; AUD-08 stays open; NR-01 (i) still mandatory

T-3  v5 §7 K-05 coverage-row wording (audit r4 AUD-21)
     decision   = <PENDING>      allowed: AUTHORIZE | REFUSE
     AUTHORIZE  the coverage row reads: "K-05 invariant: C4b completeness PASS ⇒ C4a PASS; the
                excluded combination is C4b-completeness-PASS + C4a-FAIL; C4b-completeness-FAIL +
                C4a-PASS is a legitimate case (INJ-C4B-FLOOR-FAIL)". Evidence scope: unchanged.

T-4  spline telemetry (audit r4 AUD-09a)
     decision   = <PENDING>      allowed: T-4a | T-4b | DEFERRED
     T-4a       one row per optimizer call via a disclosed, behaviour-neutral recording wrapper
                around scipy.optimize.minimize in the loaded spline namespace (a library
                function, not a frozen function): per trust-constr and per SLSQP call — status,
                message, nit, nfev, njev, wall time, objective. Evidence scope: unchanged (v5 §8
                as written).
     T-4b       per-mode rows with the primary call's nit/nfev and an SLSQP-invocation flag.
                Evidence scope: NARROWED — separate rows for the conditional SLSQP call, per-call
                wall time and direct optimizer-call counting are lost. Choosing T-4b is an
                instruction change that reduces the evidence contract and is recorded as such.
     DEFERRED   spline telemetry stays as in r1; AUD-09a stays open for the spline rows

T-5  OPTIONAL (the only optional field) — reading of v5 §3.1 "may NOT alter any F2 function …
     branch" with respect to the runtime rebinding of f2.make_objective_and_x for non-FULL masks
     (audit r4 AUD-04)
     decision   = <blank permitted>   allowed: CONFIRM_WITHIN_SCOPE | REQUIRE_ALTERNATIVE | blank
     blank      permitted value, not PENDING (§3 P-2): the mechanism is retained exactly as
                disclosed in r1 (status quo; no change, no new approval, no scientific content);
                the executor records "T-5 = blank (status quo)" and proceeds
     CONFIRM_WITHIN_SCOPE  same behaviour as blank, recorded as an explicit confirmation
     REQUIRE_ALTERNATIVE  F3-STEP2-ENG-01 recorded; masked fitting STOP for this cycle (no
                re-implementation of the optimizer chain) — consequences in §4.5
```

## 4.3 PI-ratified content (separate file; the executor implements only what is here)

```text
file      = p_konum_plus/prompts/f3_step2_pi_ratified_content_<date>.md   (PI-owned; §2.3 item 24)
content   = MANDATORY fields S-1, S-2, T-1, T-2, T-3, T-4: for each, the decision value from its
            allowed set (an explicit DEFERRED / REFUSE counts as a value) and, where a rule or
            definition is chosen, its VERBATIM text.
            OPTIONAL field T-5: may be present with a value or omitted entirely; an omitted or blank
            T-5 means the status quo of §4.2 (the r1 rebinding mechanism is retained) — it is not
            PENDING, requires no further approval and never blocks dispatch (§3 P-2).
            Any numeric literal the PI ratifies is listed with its role — it is PI-ratified content,
            never an executor literal
rule      new_scientific_literal_by_executor = 0. The executor transcribes §4.3 content into the
          harness and the register verbatim, tagged PI_RATIFIED with the file's hash; it adds no
          definition, literal, tolerance or rule of its own; on any ambiguity in §4.3 text ⇒
          F3-STEP2-EXACT-nn and STOP that path (§10), never an interpretation
```

## 4.4 X — exact engineering corrections (executor; §5)

X-01 … X-20 below. None requires or creates a scientific decision; if implementing any of them
turns out to require one, §10 applies.

## 4.5 Decision → work-plan dependency table (binding; no combination is selected here)

Every allowed value of every field maps to a defined work plan. Result vocabulary for a test:
`PASS` / `FAIL` (it ran) ; `NOT_RUN(<authorized reason>)` (it did not run for a reason authorized
by a §4 value) ; `NOT APPLICABLE(<reason>)` (the pin or path does not exist under that value).
A NOT_RUN or NOT APPLICABLE test is NEVER counted as PASS and never closes a coverage row.

```text
S-1 = (a) or (b)
  enabled   PIN-A5-SUPPORT (verbatim, §4.3) and the real C4a determination — ONLY IF the family
            path is enabled (T-5) and, for C4b additionally, the spline path is enabled (T-1);
            S-1 alone does NOT make the C4 paths runnable
  tests     T-A5-SUPPORT applicable; §7 real C4 rows required
  stopped   none by S-1 itself
S-1 = (c) or DEFERRED
  stopped   real C4a / C4b determination -> STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-01) (r1 wiring)
  tests     A.5 (ii)/(iii) unit tests only; T-A5-SUPPORT NOT APPLICABLE(no pin); real C4 rows
            UNCOVERED(PENDING S-1)
  scope     D-P04 levels 4a / 4b unreachable on real fixtures; decision-layer INJ C4 fixtures still run

S-2 = α | β | γ | δ
  enabled   the chosen rule is implemented verbatim; the spline path runs (subject to T-1)
S-2 = DEFERRED
  enabled   the spline path still runs; on an unverifiable-acceptance event the affected spline fit
            context returns STOP_EXACTNESS_PENDING(F3-STEP2-EXACT-02) (§4.1 wiring)
  scope     if no event occurs in RUN1 the spline scope is fully covered; if one occurs, that
            context's spline statistic and every dependent criterion for that fixture / sex /
            trajectory are PENDING and appear as such in the coverage matrix
  note      occurrence is not predictable in advance; the executor reports whether it occurred
  always    under T-1 = AUTHORIZE, PIN-EXC-CAPTURE (X-02) and its test T-EXC-CAPTURE apply for
            every S-2 value, DEFERRED included (the capture is behaviour-neutral and independent of
            which rule is then applied); under T-1 = REFUSE they are NOT_RUN(T-1 REFUSE) — see the
            T-1 block

T-1 = AUTHORIZE
  enabled   spline fitting in every context; X-01; T-LOADER-NODES; NR-SPL
T-1 = REFUSE
  stopped   spline path -> F3-STEP2-ENG-02 recorded; every spline-dependent statistic PENDING
  tests     NR-SPL NOT_RUN(T-1 REFUSE) ; T-LOADER-NODES NOT APPLICABLE ; X-01 NOT APPLICABLE ;
            T-EXC-CAPTURE NOT_RUN(T-1 REFUSE) and the INJ-EXC-CAPTURE fixture NOT_RUN(T-1 REFUSE)
            — the test needs the loaded spline namespace; neither counts as PASS, and the
            exception-evidence gap (PIN-EXC-CAPTURE unexercised) stays visible in the coverage
            matrix and in open_findings; no test without a spline dependency is stopped by this
  scope     C2 and C3 (both spline-relative) and C4b cannot be evaluated on real fixtures ⇒ those
            coverage rows UNCOVERED(T-1 REFUSE); real-fixture P03 for C2 / C3 is PENDING; D-P04
            levels C2 / C3 / C4b unreachable on real fixtures; DISC-F3-03 complements uncovered;
            family-only paths (C1, C5, C4a subject to S-1 / T-5) and every decision-layer INJ
            fixture still run
  status    §13: PARTIAL_PENDING_PI (mandatory scope unmet)

T-2 = T-2a   enabled: the adapter; NR-01 (ii) applicable. If the adapter cannot be built without a
             prohibited modification: F3-STEP2-ENG-03, wrapper-qualification path STOP, NR-01 (ii)
             NOT_RUN(ENG-03) — do NOT fall back to T-2b (that would be selecting a T value)
T-2 = T-2b   enabled: the restated check; NR-01 (ii) applicable in its NARROWED scope, recorded as
             narrowed_evidence (§13)
T-2 = DEFERRED   NR-01 (ii) NOT_RUN(T-2 DEFERRED); AUD-08 stays open; NR-01 (i) remains mandatory

T-3 = AUTHORIZE  coverage-row wording corrected (X-20).   T-3 = REFUSE  row unchanged; AUD-21 open

T-4 = T-4a   per-call spline telemetry (v5 §8 scope)
T-4 = T-4b   per-mode rows; recorded as narrowed_evidence (§13)
T-4 = DEFERRED   spline telemetry stays r1-shaped; the AUD-09a spline row stays open; the other §6
             / §8 corrections of X-11 (family rows, DISC-F3-03, K-05 field, canonical document)
             are applied regardless

T-5 = blank or CONFIRM_WITHIN_SCOPE
  enabled   masked family fitting (5 folds, 2 probes) and every family-dependent statistic
T-5 = REQUIRE_ALTERNATIVE
  stopped   masked family fitting -> F3-STEP2-ENG-01; folds and probes stop
  enabled   full-data family fits (mask = FULL requires no rebinding) ⇒ C1 and the C3 family side
            still run; NR-01 (i) and NR-01 (ii) unaffected (both are FULL-mask); T-MASK-FULL-EXT
            applicable
  tests     per-fit L_O <= L_FULL assertions NOT_RUN(no masked fits); UT-PROBE-DECOUPLE
            NOT_RUN(ENG-01); C2 / C5 / C4 real rows UNCOVERED(ENG-01)
  scope     D-P04 levels C2 / C5 / C4a / C4b unreachable on real fixtures; decision-layer INJ
            fixtures still run
  status    §13: PARTIAL_PENDING_PI

invariant across every combination
  - NR-01 (i) is mandatory and runs in every combination (it needs only PIN-F2-LOADER)
  - the decision-layer INJ fixtures (U5, NaN, P03 status, D-P04 levels, EMPTY_U, K-05) are
    independent of the fitting paths and run in every combination — the evaluation-layer
    corrections X-07 / X-08 / X-09 are therefore always exercised
  - work on every unaffected path continues; a stopped path never stops an unaffected one
  - no combination authorizes choosing another S / T value to make a path runnable: an unrunnable
    path is recorded (finding + UNCOVERED row), never repaired by a choice (§13 role boundary)
  - global STOP remains limited to: §2 custody failure (STOP scope), a §3 precondition failure, or
    a mandatory NR test that RAN and FAILED (§8)
```

---

# 5. Correction scope — finding → correction → verification test → evidence (binding)

Every test: deterministic, tolerance-free, RNG-free (test vectors are TEST_CONSTANTs, §11.2);
every result is an executor claim (§14). Frozen engine functions are REUSED for every predicate
(never re-typed).

```text
X-01  AUD-03 / AUD-23  PIN-SPLINE-LOADER — node list and per-node source hashes
      correction   loader executes exactly the authorized node list (T-1); for every retained and
                   prelude node record name, lineno range and SHA256 of ast.get_source_segment;
                   assert the executed list == the authorized list (set and order); assert no
                   executed node contains an I/O call (open / print / write / sys.exit) — by AST
                   walk, not by substring; register lists the SOLVER-B function set explicitly
                   (run_tc, polish, accept, kkt_res, maxviol, gradf, rss_of, run_slsqp,
                   solver_config, amat) with their hashes
      test         T-LOADER-NODES: list equality + I/O-free assertion + spline non-regression
                   through the loaded solver (§8 NR-SPL)
      evidence     results JSON `spline_loader` block; register PIN-SPLINE-LOADER; PIN-LOADER-NODE-HASHES

X-02  AUD-02  PIN-EXC-CAPTURE — solver exception evidence (independent of S-2)
      correction   any exception inside solver_config for a mode is caught at the mode level ONLY to
                   record: fixture, sex, trajectory, mask_id, mode, stage (0 trust-constr / 1 polish
                   accept / 2 expansion accept / 3 SLSQP), exception type, message, full traceback;
                   then the S-2 rule (or the DEFERRED wiring of §4.1 S-2) is applied VERBATIM — no other
                   behaviour; the catch is not broadened beyond recording
      applicability applies iff T-1 = AUTHORIZE (the loaded spline namespace is required); under
                   T-1 = REFUSE: NOT_RUN(T-1 REFUSE), never PASS (§4.5)
      test         T-EXC-CAPTURE: a TEST_ONLY_INJECTION that makes the loaded namespace's `nnls`
                   raise RuntimeError on one predeclared (fixture, mode) — a runtime substitution
                   active only for that declared test context, disclosed in the manifest and the
                   register; expected: one capture record with stage = 1 and the behaviour of the
                   chosen S-2 value (or of the §4.1 S-2 DEFERRED wiring); RUN1/RUN2 must contain
                   the record identically
      evidence     telemetry rows + `solver_exceptions` block in the results JSON

X-03  AUD-05  PIN-STARTS — start bank and feature-start validity
      correction   fit_family takes an explicit start-bank parameter; DEFAULT = the frozen full
                   retained lattice (P-01 731 / P-02 261, from f2.build_grid) + the feature start;
                   a reduced bank is admissible ONLY when the fixture's manifest row declares it
                   (`start_bank` column: FULL_LATTICE | MINI_BANK[indices]); the feature start is
                   accepted iff the FROZEN validity predicate holds, evaluated with the frozen F2
                   functions: finite ∧ numerically feasible (v_p01 / v_p02 <= FEASIBILITY_ACCEPTANCE_TOL)
                   ∧ zero_variance_rule == OK ∧ scientific_domain_pass_* ∧ kural_t_pass_exact_* ∧
                   kural_s_pass_exact ∧ not a duplicate (exact tuple equality) of a bank start;
                   otherwise the frozen FEATURE_START_REJECTED record (reason field added: which
                   predicate) and the fit proceeds with the bank; start order = bank starts then
                   feature start (as the frozen orchestration; order is aggregation-neutral)
      test         T-STARTS-DEFAULT: default bank sizes 731 / 261 (+1 when the feature start is
                   valid) asserted; T-STARTS-VALIDITY: the frozen predicate reproduced on the F2
                   benign fixtures (feature start ACCEPTED, non-duplicate); T-STARTS-DUP: a
                   TEST_CONSTANT z-vector with its maximum at index 0 for P-02 ⇒ feature start ==
                   retained tuple (0.0, 0.32057672965544004, 0.32057672965544004, √6) exactly ⇒
                   FEATURE_START_REJECTED(duplicate); the same at index 145 ⇒ (1.0, …) duplicate
      evidence     register PIN-STARTS; manifest `start_bank` per fixture; telemetry start counts
      runtime note one FULL_LATTICE fixture is mandatory (§7, FIX-STARTS-FULL) to prove the
                   default; the other fixtures may declare MINI_BANK for runtime — a declared
                   construction, not a contract change
      replay note (v4, D-04) the FULL_LATTICE default is the F3 QUALIFICATION default. An F2
                   non-regression replay fixture (NR-01, either T-2 option) uses the start bank of
                   ITS OWN declared F2 construction — bank composition, start order and
                   feature-start behaviour exactly as that F2 fixture declares them — passed
                   explicitly through the start-bank parameter. The F3 default is never applied
                   implicitly to an F2 replay, and an exact replay is not satisfied by a similar
                   result obtained with a different start bank.

X-04  AUD-06  probe_success decoupled from the full-data fit
      correction   probe_success(i, side) = the truncated refit delivers >= 1 eligible admissible
                   endpoint (probe-level only); the full-data reference is required only for C4b
                   pairing (RMSE_edge); A.5 handling per S-1
      test         UT-PROBE-DECOUPLE: TEST_ONLY_INJECTION making the full-data fit ineligible while
                   the probe refit is eligible ⇒ probe_success = True (C4a numerator), probe absent
                   from the C4b paired set
      evidence     register PIN-PROBE-SUCCESS; unit-test record

X-05  AUD-07  PIN-ACF verification clause (a) on the RUN1 residual series
      correction   for every full-data residual series r = z − ĝ produced in RUN1 (P-01, P-02,
                   spline; both sexes; every trajectory): bitwise equality of acf_classical and the
                   independently written second implementation; strict inequality vs (b) phi·T/(T−1)
                   and (c) numpy.corrcoef on lagged vectors (equality on any vector reported and
                   explained); exact-rational deviation per AUD-20 (X-13); the series exported
      test         T-ACF-RESIDUAL (plus the closed-form vectors of v5 §10 unchanged)
      evidence     p_konum_plus/calibration/f3_step2_residual_series_r2_<date>.json (float.hex
                   values, keyed fitter/fixture/sex/trajectory) + `acf_verification` block; the test
                   layer stays OUTSIDE the RUN1/RUN2 canonical document (X-11)

X-06  AUD-08  NR-01 per T-2 (and NR-01 (i) in every case)
      correction   NR-01 (i): frozen-suite replay through the loaded engine, canonical hash ==
                   6f197b74…, telemetry field equality ASSERTED (not only recorded); NR-01 (ii): per
                   T-2a / T-2b / DEFERRED exactly as authorized; report wording: "frozen suite
                   reproduced through the loaded engine" for (i)
      test         NR-01 (mandatory first test); T-WRAPPER-BENIGN under T-2a / T-2b: selected
                   endpoint hex per benign fixture == frozen FAMILY_SELECTED terminal_endpoint_hex
      evidence     results JSON `nr01` block with the (i)/(ii) split and the authorized option named

X-07  AUD-18 (as corrected in the audit r5 candidate)  PIN-U-SETS — criterion-valid common supports
      frozen text  r4 §9.2, VERBATIM, as ratified unchanged by freeze record r1 §3 item 4.1:
                     U2_s = { i : P-01 has the required valid C2 statistic AND P-02 has the required
                              valid C2 statistic AND the spline benchmark has the required valid C2
                              statistic }
                     U3_s = { i : P-01 valid C3 statistic AND P-02 valid C3 statistic AND spline
                              valid C3 statistic }
                     U5_s = { i : P-01 valid C5 statistic AND P-02 valid C5 statistic }
                     C4b (ratified C4b_status = P03_GATE, AGG-L1 = WORSE):
                     U4_s = { i : P-01 LEFT and RIGHT probes successful AND P-02 LEFT and RIGHT
                              probes successful AND spline LEFT and RIGHT probes successful }
                   record r1 §3 item 4.1: BOTH candidate scalars are recomputed on the SAME
                   criterion-specific common-valid support; item 4.2: that support is the
                   intersection of the candidates' P03 valid sets, with |U_j,s|, n_s and the share
                   disclosed for that same set
      correction   crit_stats keeps three notions apart and exposes them separately: (1) fold-fit
                   completion, (2) the statistic having been computed, (3) the statistic being
                   VALID — defined under the frozen per-criterion valid-set rules AND finite (X-09).
                   Each consulted subset-defined level builds ONE common set from the
                   CRITERION-SPECIFIC validity of ITS OWN required statistic, for exactly the
                   fitters the frozen definition names:
                     U2 from C2-statistic validity of P-01, P-02 and the spline
                     U3 from C3-statistic validity of P-01, P-02 and the spline
                     U4 from the ratified probe-success conjunction (all three fitters, both sides)
                     U5 from C5-statistic validity of P-01 and P-02 — NO spline term, NO C2 / rho
                        term, NO completion-only shortcut
                   Both candidates' sex-level statistics and scalars are computed on that ONE set;
                   no per-candidate subset is used anywhere; the disclosure block reports |U_j,s|,
                   n_s and the share of that same set. An observation whose required statistic is
                   invalid is EXCLUDED while the set is built — that exclusion is the frozen
                   construction: it is never a STOP, never an imputation, never a sentinel, and it
                   never bypasses a P03 outcome (D-P04 is entered only after BOTH families pass
                   every P03 gate incl. the completeness floors). C1 and C4a (full-denominator) and
                   C6 (structural) are not recomputed (CL-F3-01). No new tolerance, threshold or
                   validity rule is introduced.
                   (v4: the v3 wording "U5 from completion flags only" is WITHDRAWN — it misstated
                   the frozen rule; see the audit r5 candidate §1–§2.)
      STOP scope   exactly two, both narrow and unchanged in substance:
                   CONTRACT_VIOLATION_EMPTY_U — an EMPTY consulted common set (record r1 §3 item 4.3)
                   CONTRACT_VIOLATION_INCONSISTENT_U — a member of a correctly built consulted set
                     later found to carry an invalid required statistic (set-construction
                     inconsistency; no silent skip, no imputation, no sentinel)
                   Neither is extended to ordinary construction-time exclusion.
      tests        (contracts for the future run; none executed by this revision)
                   T-U2-RHO-INVALID-EXCLUDE   one fitter's required C2 statistic invalid for
                     observation i, all other statistics valid, P03 entry conditions satisfied ⇒ i
                     excluded from U2; both candidates compared on the remaining common set; no STOP
                   T-U5-INDEPENDENT-OF-C2     every required C5 statistic valid for both candidates
                     on all 10 observations, one rho invalid ⇒ |U5| = 10 — the reason recorded must
                     be C5 validity for both candidates, NOT fold completion
                   T-U5-SST-INVALID-EXCLUDE   one candidate's required C5 statistic invalid on one
                     of 10 observations, both candidates valid on the other nine, P03 entry
                     conditions satisfied ⇒ |U5| = 9 and BOTH medians computed on those same nine;
                     no STOP for this exclusion
                   T-U-POST-CONSTRUCTION-INVALID   an invalid required statistic injected into a
                     member of an already-built consulted set ⇒ CONTRACT_VIOLATION_INCONSISTENT_U
                   T-U-EMPTY                  the existing degenerate case ⇒
                     CONTRACT_VIOLATION_EMPTY_U (unchanged)
      evidence     register PIN-U-SETS (quoting the frozen definitions); fixtures INJ-U2-RHO-INVALID,
                   INJ-U5-C2-INDEPENDENT, INJ-U5-SST-INVALID, INJ-U-POST-CONSTRUCTION-INVALID,
                   INJ-DP04-EMPTY-U (§7); per-level disclosure blocks in the results JSON

X-08  AUD-19  P03 family status and mechanism outcome — TWO SEPARATE RULES
      correction (i) FAMILY P03 STATUS (per family, per fixture; computed from the six criteria):
                   FAIL     iff at least one criterion fails DEFINITELY (evaluated, not PENDING) in
                            at least one sex — regardless of any earlier PENDING criterion
                   PASS     iff every criterion passes definitely in BOTH sexes
                   PENDING  iff neither holds (no definite failure exists and at least one
                            criterion is PENDING)
                   reported fields: p03_status ; c4_status (stays PENDING while its finding is
                   open — a definite failure elsewhere never closes, covers or completes C4) ;
                   first_failed_criterion = UNDETERMINED_PENDING_<criterion> when a PENDING
                   criterion precedes the first definite failure in the frozen order
                   C1→C2→C3→C4a→C4b→C5→C6, else the criterion id ; definite_failures = [ids] ;
                   pending_criteria = [ids] ; all six criteria still measured and logged
                (ii) MECHANISM OUTCOME (per fixture; a function of the two family statuses ONLY):
                   PASS + PASS   -> D-P04 mechanism path (§6 / v5 §5)
                   PASS + FAIL   -> ONLY_P01_PASSES / ONLY_P02_PASSES (naming the PASS family)
                   FAIL + FAIL   -> STOP_BOTH_FAIL_REDESIGN
                   any PENDING   -> MECHANISM_UNDETERMINED_PENDING_EXACTNESS(<open finding ids>),
                                    both family statuses reported; NO mechanism outcome is emitted,
                                    including the combination FAIL + PENDING
                   recorded rationale (not a new rule): the frozen contract knows only PASS and
                   FAIL; PENDING exists solely as this task's STOP_EXACTNESS_PENDING artifact, so
                   any combination containing PENDING is not determinable — a definite FAIL in one
                   family does NOT establish that the other family passes, and PASS + PENDING could
                   still become either D-P04 or ONLY_Px_PASSES. The label is a STEP-2 mode marker
                   (as PENDING_EXACTNESS was in r1), not an extension of the frozen rule; if the PI
                   later wants a determinate label for these combinations that is a PI decision,
                   recorded here as an observation, not requested and not invented
      test         T-P03-STATUS-A: C4 PENDING for both families, P-01 C5 definitely fails in one
                   sex, P-02 otherwise all-pass ⇒ P-01 p03 = FAIL, c4 = PENDING, first_failed =
                   UNDETERMINED_PENDING_C4a, definite_failures = [C5]; P-02 p03 = PENDING ⇒
                   mechanism = MECHANISM_UNDETERMINED_PENDING_EXACTNESS(F3-STEP2-EXACT-01)
                   T-P03-STATUS-B: no PENDING criterion (S-1 supplied and C4 evaluated), P-01 C5
                   fails definitely, P-02 passes definitely ⇒ mechanism = ONLY_P02_PASSES
                   T-P03-STATUS-C: both families have a definite failure while C4 is PENDING ⇒ both
                   p03 = FAIL ⇒ STOP_BOTH_FAIL_REDESIGN (no PENDING remains in the combination)
      evidence     register PIN-P03-STATUS ; fixtures INJ-P03-C4PENDING-C5FAIL,
                   INJ-P03-BOTHFAIL-C4PENDING (§7)

X-09  AUD-24  PIN-UNDEFINED-FLAGS — finite-valued validity
      correction   valid(value) ⇔ value is not None ∧ math.isfinite(value); an invalid statistic is
                   undefined (flag True) and follows §8.1 governance in P03. In D-P04 (read with
                   X-07): an invalid statistic is EXCLUDED while the criterion-valid common set is
                   built — not a STOP; a non-finite value found INSIDE an already-built consulted
                   set is a set-construction inconsistency ⇒ CONTRACT_VIOLATION_INCONSISTENT_U; no
                   comparison is ever evaluated on a NaN and no NaN ever produces a RESOLVED level
      test         T-FINITE-P03: decision-layer NaN rho ⇒ undefined = True and C2 not passed via
                   §8.1 (not via a failed comparison)
                   T-FINITE-DP04: the same NaN at a consulted level ⇒ the observation is excluded
                   at construction (T-U2-RHO-INVALID-EXCLUDE), and an injected post-construction
                   NaN ⇒ CONTRACT_VIOLATION_INCONSISTENT_U — never a silent RESOLVED
      evidence     register PIN-UNDEFINED-FLAGS; fixtures INJ-NAN-STAT, INJ-U-POST-CONSTRUCTION-INVALID (§7)

X-10  AUD-10  fixture fidelity — execution-site executed keys
      correction   executed_construction_key derived ONLY from evidence written at real execution
                   sites: the F2 evidence dict returned by run_one_start (validator_called,
                   optimizer_called, fallback_branch_entered, same_x0_reused, primary /
                   fallback injection flags) and the harness's own injection flags written at the
                   injection sites; construction_audit block per fixture (manifest prose →
                   implemented key → executed key → fidelity_pass); fidelity count reported as
                   <implemented>/<declared> ; <executed>/<declared>
      test         T-FIDELITY: implemented == executed for every fixture; any mismatch ⇒ the fixture
                   is reported FIDELITY_FAIL (never silently re-labelled)
      evidence     results JSON `construction_audit`

X-11  AUD-09a / AUD-09b  telemetry, reporting fields, canonical document
      correction   (a) spline telemetry per T-4; (b) family rows carry L (masked objective value of
                   the endpoint) and the endpoint's frozen predicates / failure codes; (c) §6
                   fields: DISC-F3-03 complements for C2, C3 and C4b; family-invalid counts by
                   frozen failure code per criterion / sex; per-side probe-failure shares; K-05
                   check RESULT field; double-count declaration echoed verbatim from record r1 §4;
                   (d) the canonical RUN1/RUN2 document contains, per fit: the selected endpoint
                   theta (float.hex), its masked L (hex), the start-bank size, the
                   FEATURE_START_REJECTED flag; per spline fit: winner mode, RSS (hex), the
                   equivalent-mode set, per-mode validity; the ACF / A5 / unit-test objects are
                   EXCLUDED from the canonical document and recorded in a separate test-evidence
                   document hashed on its own; (e) `sexes` removed or filled; (f) coverage row
                   "reporting fields populated" derived from a schema assertion, not declared
      test         T-CANON: RUN1 == RUN2 canonical SHA256 over the enlarged document; T-SCHEMA: every
                   §6 field present at least once (assertion, machine-checked)
      evidence     results JSON r2; telemetry r2; test-evidence JSON

X-12  AUD-11 / AUD-14 / AUD-22  register and report wording
      correction   spline zero-variance predicate stated exactly (`q.std(ddof=0) == 0.0`; exact
                   zero; no epsilon — an epsilon would be a new literal and is prohibited);
                   TEST_CONSTANT table split into "fixture construction inputs (manifest-declared;
                   enter fixture results only; PATH_COVERAGE_ONLY)" and "verification-only
                   TEST_CONSTANTs (enter no result)"; PIN-ACF row states the clause (a) scope
                   truthfully; NR-01 wording per X-06; "byte-identical source segments" stated as
                   by-construction plus the per-node hashes of X-01; no "ulp deviation 0.0"
                   generalization
      evidence     register r2; report r2

X-13  AUD-20  exact-rational deviation
      correction   deviation_ulps = |Fraction(phi) − exact| / Fraction(math.ulp(phi)) computed
                   exactly (no rounding of `exact` to float64 before differencing); informational,
                   no threshold
      test         values on the closed forms reported (expected: alternating 0.2465753424657534,
                   linear 0.2602739726027397 ulps — as computed independently by two auditors;
                   reported as executor claims)
      evidence     `acf_verification` block

X-14  AUD-12  STOP_UNDEFINED_CONSULTED_SCALAR
      correction   removed as a separate branch and replaced by the two narrow labels of X-07:
                   CONTRACT_VIOLATION_EMPTY_U and CONTRACT_VIOLATION_INCONSISTENT_U. Ordinary
                   construction-time exclusion produces NO STOP label at all; no silent branch
                   remains
X-15  AUD-13  custody imports
      correction   import ADDENDUM A r1 (cc4f97b4…) and prompts v2 / v3 / v4 from the PI
                   attachments byte-exact into p_konum_plus/prompts/; record in the custody table
X-16  AUD-15  coverage matrix labels
      correction   every row states its evidence class: real-fit / decision-layer injection /
                   unit test / assertion; injected-only rows never read as real-path coverage
X-17  AUD-16  file encodings
      correction   every text deliverable written with newline="" (LF), ascii/utf-8 declared;
                   sidecar hashes therefore platform-neutral
X-18  AUD-25  opened-file list (optional but recommended)
      correction   sys.addaudithook on the "open" event records every file opened for reading by
                   the process; the list is machine-derived and compared with the declared list
X-19  AUD-04  register wording for PIN-MASKED-OBJECTIVE (mechanism per T-5)
      correction   the row states: FULL ⇒ no rebinding (frozen path verbatim); non-FULL ⇒
                   f2.make_objective_and_x rebound to the masked factory for the duration of the
                   fit and restored; run_one_start / run_primary / run_fallback / classification /
                   aggregation execute unmodified; masked fun = frozen stable_fn + zero_variance_rule
                   + L_INVALID_PREDICTION_GUARD + Σ_{t∈O}(x_t − ĝ_t)²
      test         T-MASK-FULL-EXT: bitwise equality of the FULL-mask factory with the frozen
                   objective on the two F2 benign targets × the frozen lattice tuples at indices
                   {0, 37, 74, …} (a fixed deterministic stride; TEST_CONSTANT) — no RNG
X-20  AUD-21  v5 §7 K-05 row per T-3 (wording only; nothing in code changes)
```

---

# 6. Architecture requirements carried from v5 (unchanged unless §4 authorizes otherwise)

```text
F2 engine: PIN-F2-LOADER (importlib by path; hash 01714752… verified before load; __main__-guarded)
           — no copy-and-edit, no re-implementation of families, supports, rules, optimizer chain
spline:    PIN-SPLINE-LOADER per T-1; SOLVER-B stage semantics, tolerances, acceptance, expansion,
           fallback acceptance, mode comparator, reference certification — unmodified (r4 §5)
masking:   r4 §8 masked objective; z never re-standardized; ĝ = z_ddof0(g) on the FULL grid;
           admissibility / Kural T / Kural S / taxonomy on the full stabilized grid; L_INVALID_
           PREDICTION_GUARD = 585; folds [0,29,58,87,116,146]; LEFT O = {15..145}; RIGHT O = {0..130};
           observed-only feature start j*_O = min{ j ∈ O : x_j = max_O x } with the frozen D-F2-09.5
           constants; L_O <= L_FULL asserted for every eligible masked endpoint
criteria:  v5 §4 pins unchanged (C1–C6, K-05 assert, PIN-ACF sequential index-order arithmetic,
           RHOCV, RMSE-EDGE, SSTAB-W, MEDIAN, IQR); D-P04 per v5 §5 with X-07 / X-09
labelling: mechanism_outcome only; the harness refuses any winner / selected / generator_selected
           key; STOP labels: BOTH_FAIL_REDESIGN ; CONTRACT_VIOLATION_EMPTY_U ;
           CONTRACT_VIOLATION_INCONSISTENT_U ; PENDING_EXACTNESS(<id>) ;
           MECHANISM_UNDETERMINED_PENDING_EXACTNESS(<ids>) is a mechanism label, not a STOP
ratified literals: exactly v5 §2 (read-only; any deviation = STOP)
```

---

# 7. Fixture manifest r2 — predeclared before any run (F2 STEP-2 discipline)

Create `p_konum_plus/calibration/f3_step2_fixture_manifest_r2_<date>.csv` BEFORE any harness run
(child of the r1 manifest d9fb75f8…, which stays byte-unchanged); hash it; write the
pre-execution custody record; only then execute. Columns: those of r1 plus `start_bank`,
`evidence_class` (real_fit / decision_layer_injection / unit_test / assertion),
`injection_sites`, `expected_outcome`, `parent_fixture_id` (r1 id or NEW).

Required coverage (each row >= 1 fixture; a fixture may cover several; every r1 row retained):

```text
retained from r1   SCEN-A, SCEN-B (start_bank declared), all INJ-* decision-layer fixtures with
                   their r1 expectations (re-run under the corrected evaluation layer)
FIX-STARTS-FULL    one real-fit trajectory per family with start_bank = FULL_LATTICE (731 / 261 +
                   feature): proves the default bank; telemetry start count asserted
FIX-STARTS-DUP     P-02 real-fit trajectory with its maximum at index 0 (and one at 145):
                   FEATURE_START_REJECTED(duplicate) exercised on the real path
INJ-U2-RHO-INVALID   decision layer (was part of the v3 INJ-U5-RHO-UNDEF): one fitter's required
                   C2 statistic invalid on one observation ⇒ that observation excluded from U2, the
                   remaining common set compared, no STOP (X-07 T-U2-RHO-INVALID-EXCLUDE)
INJ-U5-C2-INDEPENDENT   decision layer (was INJ-U5-RHO-UNDEF): every required C5 statistic valid
                   for both candidates, one rho invalid ⇒ |U5| = n_s = 10, justified by C5 validity
                   and not by completion (X-07 T-U5-INDEPENDENT-OF-C2)
INJ-U5-SST-INVALID   decision layer (was INJ-U5-SST-VIOL; EXPECTATION CORRECTED in v4): one
                   candidate's required C5 statistic invalid on one of ten observations ⇒ |U5| = 9
                   with both medians on those same nine; NO STOP (X-07 T-U5-SST-INVALID-EXCLUDE)
INJ-U-POST-CONSTRUCTION-INVALID   decision layer (new in v4): an invalid required statistic injected
                   into a member of an already-built consulted set ⇒ CONTRACT_VIOLATION_INCONSISTENT_U
                   (X-07 T-U-POST-CONSTRUCTION-INVALID) — kept distinct from ordinary exclusion
INJ-NAN-STAT       decision layer: NaN rho ⇒ undefined flag and P03 §8.1 treatment (X-09
                   T-FINITE-P03); its D-P04 consequence is exclusion at construction, with the
                   post-construction case covered by INJ-U-POST-CONSTRUCTION-INVALID
INJ-P03-C4PENDING-C5FAIL   REAL-type evaluation with C4 PENDING and a definite C5 failure in one
                   family ⇒ family FAIL / c4 PENDING / UNDETERMINED_PENDING_C4a fields and
                   MECHANISM_UNDETERMINED_PENDING_EXACTNESS (T-P03-STATUS-A)
INJ-P03-BOTHFAIL-C4PENDING   both families with a definite failure while C4 is PENDING ⇒
                   STOP_BOTH_FAIL_REDESIGN (T-P03-STATUS-C); and, when C4 is evaluated (S-1
                   supplied), the T-P03-STATUS-B combination
INJ-EXC-CAPTURE    the T-EXC-CAPTURE injection context (X-02); expected capture record + the
                   behaviour of the chosen S-2 value (or the §4.1 DEFERRED wiring); declared only
                   when T-1 = AUTHORIZE — under T-1 = REFUSE the row is NOT_RUN(T-1 REFUSE)
UT-PROBE-DECOUPLE  unit test (X-04)
C4 rows            if S-1 = (a) or (b): real C4a pass & fail, A.5 (i) fires / does not fire on
                   TEST_CONSTANT trajectories, A.5 (ii)/(iii), C4b pass & fail on the real path,
                   D-P04 4a / 4b consulted on real fits; if S-1 = DEFERRED / (c): rows stay
                   PENDING(F3-STEP2-EXACT-01) and are listed as such
NR rows            NR-01 (i) ; NR-01 (ii) per T-2 ; spline NR through the loaded solver
```

Fixture outcomes carry `interpretation = PATH_COVERAGE_ONLY`. No fixture may be derived from,
resemble by construction, or be calibrated to any real F1 trajectory. RNG only in manifest-declared
fixture generation with recorded seeds.

---

# 8. Rerun scope — dependency-scoped (binding; NOT a C4-only rerun)

```text
change (§5)                       dependent paths                                   rerun
X-03 start bank / validity        every family fit: full-data, 5 folds, 2 probes    all family-dependent statistics (C1, C2, C3, C5; C4 if enabled)
X-01 loader hashes; S-2; X-02     every spline fit (146-mode enumeration)           all spline-dependent statistics (C2, C3 benchmark side; C4b if enabled; DISC-F3-03)
X-07 U-sets (criterion-valid) ;   D-P04 consulted levels; P03 validity flags        every D-P04 fixture; every P03 evaluation
X-09 finite validity
X-08 P03 status fields            evaluation layer                                  every fixture
X-04 probe_success ; S-1          C4a / C4b (real) if enabled                       C4 fixtures (real) if S-1 supplied; unit tests otherwise
X-10 fidelity ; X-11 telemetry /  all                                               RUN1 + RUN2 regenerated from scratch
     canonical document
⇒ full synthetic qualification rerun of every ENABLED path (§4.5): RUN1 (telemetry + results) and
  RUN2 (determinism), preceded by the non-regression gates below. The rerun is never reduced to the
  C4 paths, and never reduced below the paths that the chosen combination leaves enabled.

non-regression gates and their applicability (§4.5 governs; NOT_RUN is not FAIL and not PASS)
  NR-01 (i)   frozen-suite replay through the loaded engine, canonical hash == 6f197b74…,
              telemetry field equality asserted — MANDATORY in every combination; first test
  NR-01 (ii)  wrapper qualification per T-2: T-2a (full wording) / T-2b (narrowed) /
              NOT_RUN(T-2 DEFERRED) / NOT_RUN(ENG-03 if the T-2a adapter proves impossible)
  NR-SPL      spline non-regression through the loaded SOLVER-B (the 30 r2 rows reproduced
              field-for-field, ffda04b0… content, executor environment) — MANDATORY iff
              T-1 = AUTHORIZE; under T-1 = REFUSE it is NOT_RUN(T-1 REFUSE) and the
              spline-dependent scope is UNCOVERED (§4.5), which is a scope shortfall recorded in
              §13, not a STOP
  a gate that RUNS and FAILS ⇒ STOP (gate-specific blocker); no partial rerun of that path
  a gate that is NOT_RUN for a §4-authorized reason ⇒ recorded with the reason; its coverage rows
  stay UNCOVERED; the run continues on the enabled paths
```

Determinism, telemetry, environment: as v5 §8 — same-process, thread-pinned (OMP / OPENBLAS / MKL
= 1), same code, same inputs; RUN1 == RUN2 canonical SHA256 over the enlarged document (X-11);
cross-process / cross-platform bitwise reproducibility NOT claimed and NOT to be claimed; Python,
numpy, scipy versions and thread pins recorded.

---

# 9. Prohibited (firewall) — see §1; in addition for this cycle

```text
resolving any S / T field by inference from the audit text or from "what the PI probably wants"
implementing a §4.3 rule with any deviation from its verbatim text
treating an auditor's exploratory / surrogate check as evidence for anything
re-labelling r1 files, editing r1 files, or writing an r2 deliverable over an r1 path
writing "verified", "independently confirmed", "QUALIFIED" or "audit PASS" about own output
```

---

# 10. Exactness-finding protocol (v5 §12, carried; binding)

```text
If implementing any rule requires a choice the frozen contract and §4.3 do not determine:
  record F3-STEP2-EXACT-nn (next free number; EXACT-01 and EXACT-02 are taken): rule pointer ;
  the exact gap ; the bounded options observed ; classification (gate-specific blocker / cleanup)
  — never resolve it, never pick an option ; implement the affected path as
  STOP_EXACTNESS_PENDING(<id>) so the harness cannot run it silently ; continue every unaffected path
If a required computation is impossible without modifying a frozen artifact:
  record F3-STEP2-ENG-nn (ENG-01 masked fitting, ENG-02 spline loader, ENG-03 wrapper adapter are
  reserved by §4) ; STOP that path ; do not modify
Global STOP only for custody failure (§2), a §3 precondition failure, or NR failure (§8).
Do NOT read, paraphrase or "reconstruct" any real-data property to fill a gap.
```

---

# 11. CLASS_C pin register r2 (deliverable; child of the r1 register 03486232…)

## 11.1 Rows

Every r1 row re-verified and re-stated (result column = executor claim with the r2 test id),
plus the new pins: PIN-STARTS ; PIN-PROBE-SUCCESS ; PIN-EXC-CAPTURE ; PIN-P03-STATUS ;
PIN-LOADER-NODE-HASHES ; PIN-TELEMETRY (per T-4) ; PIN-CANON-DOC ; PIN-A5-SUPPORT (only if S-1 =
(a) or (b); VERBATIM from §4.3, tagged PI_RATIFIED) ; PIN-SOLVER-B-UNVERIFIABLE (only if S-2 ∈
{α, β, γ, δ}; VERBATIM from §4.3, tagged PI_RATIFIED). Every row: `scientific_freedom = none`;
a row that would require a choice is not a pin (§10).

## 11.2 Constant tables (AUD-22)

```text
fixture construction inputs   manifest-declared values (bump parameters, sigma, seeds, injected
                              statistic values, start_bank indices): enter FIXTURE results only,
                              PATH_COVERAGE_ONLY; never a scientific literal
verification-only TEST_CONSTANTs   closed-form ACF vectors, T-MASK-FULL-EXT stride and thetas,
                              T-STARTS-DUP vectors, the T-EXC-CAPTURE injection context: enter no
                              result, statistic, gate or comparator
PI_RATIFIED content           any definition / literal from §4.3, listed with the §4.3 file hash
scientific literal registry additions by the executor = 0
```

---

# 12. Deliverables (r2 child revisions; r1 files byte-unchanged; external sidecars; no self-hash)

```text
 1. p_konum_plus/calibration/f3_step2_adequacy_harness_r2_<date>.py          parent a95ad152…
 2. p_konum_plus/calibration/f3_step2_fixture_generator_r2_<date>.py         parent = r1 generator (hash recorded, §2.2 item 13)
 3. p_konum_plus/calibration/f3_step2_fixture_manifest_r2_<date>.csv         parent d9fb75f8… (W-2: written and hashed BEFORE any run)
 4. p_konum_plus/provenance/f3_step2_r2_preexecution_custody_<date>.md       W-3: SHA256 of the prepared harness (item 1), generator (item 2) and
                                                                             manifest (item 3), plus the §3 precondition results and the S / T
                                                                             values as read — written AFTER those three files exist and BEFORE the
                                                                             first test or run; it defines the exact bytes that are then executed
 5. p_konum_plus/calibration/f3_step2_telemetry_r2_<date>.csv                RUN1
 6. p_konum_plus/calibration/f3_step2_results_r2_<date>.json                 RUN1 (+ RUN2 hash); LF; canonical document per X-11
 7. p_konum_plus/calibration/f3_step2_residual_series_r2_<date>.json         X-05
 8. p_konum_plus/calibration/f3_step2_test_evidence_r2_<date>.json           ACF / A5 / unit-test objects (outside the canonical document)
 9. p_konum_plus/calibration/f3_step2_class_c_pin_register_r2_<date>.md      parent 03486232…
10. p_konum_plus/provenance/f3_step2_correction_report_r2_<date>.md          custody table (§2) ; §3 precondition results ; per-finding
                                                                             correction ↔ test ↔ evidence table (§5) ; NR results ; coverage
                                                                             matrix with evidence classes ; fidelity counts ; exactness /
                                                                             engineering findings ; determinism hashes ; environment ; the
                                                                             machine-derived opened-file list ; end state (§14) — every result
                                                                             labelled "executor claim; independent verification pending"
11. external .sha256 sidecars for 1–10 (and for the r1 files if absent, §2.2 item 19)
12. quarantine: if any file from an interrupted r2 attempt exists at start, move it (never delete)
    to p_konum_plus/quarantine/f3_step2_r2_aborted_<date>/ and list it; reuse nothing
<date> = ISO date of the run, dashes. commit = false.
```

---

# 13. Roles and acceptance boundary (binding)

```text
Claude Code   = execution / provenance ; implements only §4.3 (verbatim) and §5 ; records and STOPs
                on every gap (§10) ; produces r2 child revisions ; labels every result an executor
                claim ; performs NO independent audit ; declares NO QUALIFIED / PASS-as-verified
Claude (chat) = independent / advisory auditor ; audits the r2 package after return (§15) ; labels
                independent verification ; recommends no option
Öner (PI)     = sole decision authority ; supplies §4.3 ; ratifies or withholds after the audit
F3_EXECUTION_READY stays false in every outcome; no F3 execution, no real fit
```

End-state computation (deterministic; the executor COMPUTES the status from these fields and never
chooses it; the six fields are reported SEPARATELY in §14 and none of them implies another):

```text
corrections_complete      = every X correction that the chosen combination leaves applicable (§4.5)
                            was applied AND its verification test RAN and PASSED
mandatory_tests_all_run   = NR-01 (i) PASS, and every other test the §4.5 table marks applicable
                            under the chosen combination RAN and PASSED
deferred_decisions        = [ every S / T field whose value is DEFERRED, REFUSE or
                            REQUIRE_ALTERNATIVE ]   (a blank T-5 is NOT a deferral)
narrowed_evidence         = [ T-2b and / or T-4b, if chosen ]
uncovered_coverage_rows   = [ every coverage row not covered, each with its reason ]
open_findings             = [ every EXACT / ENG finding open at the end, INCLUDING PI-deferred ones ]

F3_STEP2_r2_status =
  CORRECTED_PENDING_INDEPENDENT_AUDIT   iff corrections_complete = true
                                        AND mandatory_tests_all_run = true
                                        AND deferred_decisions = []
                                        AND narrowed_evidence = []
                                        AND uncovered_coverage_rows = []
                                        AND open_findings = []
  PARTIAL_PENDING_PI                    in every other case, with each non-empty list reported

The two statuses are mutually exclusive and exhaustive: the same conditions can never yield both.
Engineering completion (corrections_complete) is reported separately from gate scope and NEVER
implies it. A deferral, a refusal, a narrowed evidence scope (T-2b / T-4b) or a NOT_RUN test never
supports a claim that the original scope was met; the shortfall stays visible in the status fields,
in the coverage matrix and in the report. Neither status is QUALIFIED, neither is "verified", and
neither yields F3_EXECUTION_READY = true.
```

---

# 14. Required end-state logic and response format

```text
F3_STEP2_r2_harness_created = true/false
dispatch_preconditions      = P-1..P-4 results (PASS / STOP); mandatory vs optional fields distinguished
PI_ratified_content_hash    = <observed>   ; S-1 / S-2 / T-1..T-4 values as read (verbatim);
                              T-5 value or "blank (status quo)"
work_plan_applied           = the §4.5 rows selected by those values: paths enabled / stopped,
                              tests applicable / NOT_RUN(reason) / NOT APPLICABLE(reason)
NR-01 (i)                   = executor claim PASS / FAIL, hash (mandatory in every combination)
NR-01 (ii)                  = executor claim PASS / FAIL / NOT_RUN(<reason: T-2 DEFERRED | ENG-03>),
                              with the T-2 option named and, for T-2b, the narrowed scope recorded
NR-SPL                      = executor claim PASS / FAIL / NOT_RUN(T-1 REFUSE) (30 rows when run)
corrections X-01..X-20      = applied / NOT APPLICABLE(<S or T value>) ; test ids and results as
                              PASS / FAIL / NOT_RUN(reason) — never PASS for a test that did not run
fixture fidelity            = <implemented>/<declared> ; <executed>/<declared> (execution-site keys)
coverage_complete           = true/false (uncovered rows listed with the reason: PENDING(S-1) / DEFERRED(T-x) / other)
exactness / engineering findings = list or none (none resolved by Claude Code)
determinism                 = RUN1 == RUN2 canonical SHA256 (true/false) over the X-11 document
real_data_access = false ; opened-file list (machine-derived) ; generator_selected = false
P03_threshold_values = NOT_COMPUTED ; new_scientific_literal_by_executor = 0
status fields (§13, reported separately, none implying another):
  corrections_complete = ; mandatory_tests_all_run = ; deferred_decisions = ;
  narrowed_evidence = ; uncovered_coverage_rows = ; open_findings =
F3_STEP2_r2_status          = computed per §13 (CORRECTED_PENDING_INDEPENDENT_AUDIT | PARTIAL_PENDING_PI)
F3_EXECUTION_READY = false ; F3_started = false ; commit = false
```

Response table:

| Check | executor claim (PASS / FAIL / NOT_RUN(reason) / NOT APPLICABLE(reason) / STOP) | evidence (path / hash / test id) |
|---|---|---|
| §2 custody items 1–19 exact; 20–26 recorded; no surrogate used | | |
| §3 preconditions P-1..P-4 (mandatory fields complete; blank T-5 accepted as status quo) | | |
| §3 write order W-1 … W-5 respected; pre-execution custody record written after the harness / generator / manifest exist and before the first run | | |
| §4.5 work plan recorded: enabled / stopped paths, NOT_RUN(reason) tests, uncovered rows | | |
| §4.3 content transcribed verbatim; PI_RATIFIED tags; executor literals = 0 | | |
| T-1 node list executed == authorized; per-node hashes; I/O-free assertion | | |
| S-2 rule (or §4.1 DEFERRED wiring) + PIN-EXC-CAPTURE (stage, message, traceback) — NOT_RUN(T-1 REFUSE) if the spline path is refused | | |
| PIN-STARTS: default full lattice; frozen validity/dedup; FIX-STARTS-FULL; FIX-STARTS-DUP | | |
| probe_success decoupled (UT-PROBE-DECOUPLE) | | |
| PIN-ACF clause (a) on every RUN1 residual series; series exported; exact ulp metric | | |
| NR-01 (i) 6f197b74… (mandatory) | | |
| NR-01 (ii) per T-2 (PASS / FAIL / NOT_RUN(reason)) | | |
| NR-SPL 30 rows through the loaded solver (PASS / FAIL / NOT_RUN(T-1 REFUSE)) | | |
| U-sets from criterion-specific validity (U2/U3/U4/U5, frozen definitions quoted); one common set per consulted level for both candidates; construction-time exclusion ≠ STOP; EMPTY_U and INCONSISTENT_U STOPs distinct (INJ-U2-RHO-INVALID, INJ-U5-C2-INDEPENDENT, INJ-U5-SST-INVALID, INJ-U-POST-CONSTRUCTION-INVALID, INJ-DP04-EMPTY-U) | | |
| finite-valued validity: NaN ⇒ undefined in P03 (§8.1) and excluded at U-construction in D-P04 (INJ-NAN-STAT) | | |
| P03 family status rule and mechanism-outcome rule separated (T-P03-STATUS-A / B / C) | | |
| fidelity: execution-site executed keys; construction_audit; counts | | |
| telemetry per T-4; family rows with L / failure codes; §6 fields; K-05 field; DISC-F3-03 C2/C3/C4b | | |
| canonical document enlarged (X-11); RUN1 == RUN2 | | |
| coverage matrix with evidence classes; C4 rows per S-1 | | |
| register r2 rows; constant tables split; wording items X-12 | | |
| custody imports (X-15); LF outputs; opened-file list machine-derived | | |
| r1 files byte-unchanged; r2 child revisions; sidecars for 1–10; no self-hash | | |
| status computed per §13 from the six separately reported fields | | |
| no QUALIFIED / verified wording; F3_EXECUTION_READY = false | | |

Then the hash line block: harness / generator / manifest / custody record / telemetry / results /
residual series / test evidence / register / report — path and SHA256 each; RUN1 and RUN2 canonical
SHA256; NR-01 (i)/(ii); NR-SPL; findings; F3_STEP2_r2_status.

Final classification vocabulary only: `global blocker` / `gate-specific blocker` / `cleanup` /
`informational` — for findings; executor results are claims, never verifications.

---

# 15. Independent audit after return (do NOT perform it yourself)

The auditor will re-hash every deliverable and parent; re-run the loaders, NR-01 (i) and NR-SPL in
the auditor environment (labelled an auditor-environment consistency check; no claim of reproducing
the executor hashes, and no assumption — in either direction — that the two environments are
identical or different without evidence); re-execute PIN-ACF clause (a) on the exported residual series with an independent
implementation; re-run the decision-layer counterexamples (U5, NaN, P03 status) and the
start-validity tests against the frozen predicate; check the executed-key derivation against the
telemetry evidence; check every §4.3 transcription against the PI file byte-for-byte; check that no
S / T value was inferred; verify the firewall, labelling, 6B absence and the opened-file list;
classify findings; label independent verification separately from executor claims; recommend no
option. F3_STEP2 = QUALIFIED can be declared only by the PI after that audit.

---

# 16. Dispatch readiness — what this draft still needs (PI view)

Two groups, kept apart: **A. mandatory under the current contract** — the PI decision file, the
mandatory S / T fields and the STOP-class / dispatch-class custody items, each with the checks
already defined in §2 and §3, including the existing sidecar exception; **B. record and transmission
items** — record-class historical files and informational transmission notes, which are provenance
work and do NOT become execution blockers merely by appearing in an informational record. No
reviewer's list is adopted wholesale as a mandatory checklist; nothing in the frozen contract or in
the existing dispatch rules is relaxed, and no new mandatory condition is added.

This section SUMMARISES §2 and §3; it creates no execution rule of its own. Where a row and §2 / §3
could be read differently, §2 / §3 govern. (v6, S16-01: the row grouping was corrected against
those sections; the optional field T-5 is stated separately from the mandatory table.)

## A. Mandatory under the current contract (dispatch cannot proceed without these)

| item | kind | status | what makes it ready |
|---|---|---|---|
| S-1 A.5(i) definition | PI scientific decision (MANDATORY) | PENDING | value ∈ {(a) text, (b) text, (c) → C4 stays pending, DEFERRED} written verbatim into the §4.3 file |
| S-2 SOLVER-B unverifiable acceptance | PI decision, ratified-pin amendment (MANDATORY) | PENDING | value ∈ {α, β, γ, δ, DEFERRED} written verbatim into the §4.3 file |
| T-1 loader retain rule | task-scope authorization (MANDATORY) | PENDING | AUTHORIZE (node list as in §4.2) or REFUSE |
| T-2 NR-01 wrapper qualification | task-scope authorization (MANDATORY) | PENDING | T-2a (scope unchanged) / T-2b (scope NARROWED — declared) / DEFERRED |
| T-3 K-05 row wording | task-scope authorization (MANDATORY) | PENDING | AUTHORIZE / REFUSE |
| T-4 spline telemetry | task-scope authorization (MANDATORY) | PENDING | T-4a (scope unchanged) / T-4b (scope NARROWED — declared) / DEFERRED |
| §4.3 PI-ratified content file | PI-owned file | MISSING | `f3_step2_pi_ratified_content_<date>.md` with all values; its hash recorded in §2.3 item 24 |
| fixture generator r1 (`f3_step2_fixture_generator_r1_2026-09-06.py`) | real file + hash | MISSING to the auditor; hash unrecorded in §2.2 item 13 | deliver to the auditor; record hash |
| sidecars of the r1 deliverables 1–6 (§2.2 item 19) | custody check, with the §3 P-1 exception | PRESENT sidecars: verified read-only; MISSING sidecars: recorded NOT_LOCATED | a PRESENT sidecar that disagrees with its file is a mismatch and fails P-1; a MISSING sidecar does NOT fail P-1 and is NOT required before dispatch — it is created in the permitted-write stage W-1 as a custody action. Supplying them earlier only lets the auditor cross-check them |
| custody items 5 and 6 (D-F2-09 manifest c39fb519…, packet 8ff70a64…) | STOP-class custody (§2.1) | present in the executor repository per §2.1; not yet seen by the auditor | mandatory for the run through the §2.1 check; delivering them to the auditor additionally removes the surrogate basis of the auditor's NR-01 reference |
| dispatch-time observed hash of this prompt (§2.3 item 25) | dispatch-class precondition | n/a until dispatch | §3 P-4: the observed SHA256 of the dispatched file must EQUAL the value the PI recorded at dispatch — recording alone is not sufficient |

Optional field, stated separately from the mandatory table (§3 P-2): **T-5 rebinding reading** —
blank or absent is a PERMITTED value carrying the status-quo meaning of §4.2; it is not PENDING, it
needs no approval and it never blocks dispatch on its own. A value of CONFIRM_WITHIN_SCOPE or
REQUIRE_ALTERNATIVE may be given instead; only the latter changes the work plan (§4.5).

## B. Record and transmission items (provenance work; not execution blockers by themselves)

| item | kind | status | note |
|---|---|---|---|
| Kimi review of prompt DRAFT v4 (`…v4_review_2026-09-07.md`) | record-class | hash REPORTED (ef71acdc…), file not provided to the drafting session | re-observe the hash when supplied; a reported hash is never treated as verified |
| Kimi review of prompt DRAFT v3, earlier Kimi review files | record-class | not provided, not hashed | record when supplied; absence here is not absence in the repository |
| the trigger instructions and feedback records (f37d3310…, 84e46b7c…, d5a0eef1…, 9e38f768…, 00b11398…) | record-class | observed and hashed | custody import under X-15 |
| editorial correction candidates (audit r6, reconciliation r5) | record-class | independent review PENDING | reviewed ≠ accepted; citation implies no acceptance |
| historical label wording / cosmetic items noted informationally by reviewers | record-class | no correction opened | historical records stand unchanged |
| v5 §15 end-of-task table of the r1 run | record-class (historical) | not provided to the auditor | lineage / provenance only; its absence is not a dispatch blocker. Deliver for the record and for the auditor's §15 check |
| ADDENDUM A r1 (cc4f97b4…) and prompts v2–v4 (§2.3 items 22–23) | record-class | in PI custody; NOT_LOCATED in the repository | attach so they can be imported byte-exact under X-15 and recorded in the custody table; absence yields NOT_LOCATED, never a STOP |
| audit record finalization | auditor | DRAFT r4 (pending the missing files) | may add findings once E-1 … E-5 are closed; this draft must then be re-checked against the final record |
| external review of this draft lineage | workflow | v1 review → v2 ; v2 document-correction review → v3 ; v3 U-set correction (Kimi objection, relayed) → v4 ; v4 package reviewed by the reported Kimi v4 review and the ChatGPT narrow feedback → v5 applied C-01 / C-02 ; the §16 feedback confirmed that closure → this v6 (§16 classification only) | any further review round is folded in as v7 … before dispatch. A document review is never an independent verification of implementation adequacy, and none of these rounds requests a new audit cycle or a PI approval |

```text
This draft selects no option, ratifies nothing, authorizes nothing and starts nothing.
F2 = CLOSED ; F3_STEP1 = FROZEN ; F3_STEP2_audit_verdict = NOT PASSED ; F3_STEP2_qualification = WITHHELD
F3_EXECUTION_READY = false ; real_SSA_execution = prohibited ; new_methodology_review = false ; commit = false
```
