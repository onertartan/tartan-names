# p_konum_plus — F3 STEP 1 r3 — Reference-Only Provenance Correction Report

```text
artifact_role = narrow provenance-correction report (Output 2 of the r3
                reference-only correction task)
status        = NON-NORMATIVE
date          = 2026-09-03

finding_id = F3-STEP1-PROV-03
class = reference-only transcription/provenance defect

parent_r2_sha256 =
b8ce7667200787eeda6e71b6d8ede6aebc9bb4fd1b05344dc31f62f361bc399c

r3_sha256 =
350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad

old qualification anchors =
522d3508… / ecda07d0… / external_independent_acceptance=PENDING

new accepted anchors =
e71ce030… / b31e5a6b… / ffda04b0…
synthetic_solver_qualification_external_independent_acceptance=PASS

scientific_change = false
execution_change = false
methodology_change = false
F2_reopening = false
new_methodology_review = false

D-P03-4 scientific decision content changed = false
other PI decision rows changed = false
```

## 1. Custody verification (all exact; no STOP)

v11 `d136502f…` PASS · F2 FREEZE r1 `ee2cb99d…` PASS · parent r2 candidate
`b8ce7667…` PASS (and re-verified byte-unchanged AFTER the r3 write) ·
historical manifest `522d3508…` PASS · historical harness `ecda07d0…` PASS ·
r2 bundle manifest `e71ce030…` PASS · r2 bundle harness `b31e5a6b…` PASS ·
r2 bundle telemetry `ffda04b0…` PASS. External audit conclusion recorded as
given: F3-SPLINE-QUAL-MANIFEST-01 = CLOSED, F3-SPLINE-QUAL-PREDECL-02 =
CLOSED, SOLVER_A/B external acceptance PASS, SOLVER_C FAIL, no blockers.

## 2. Compact diff summary (r2 -> r3; git diff --no-index)

Exactly three change regions, all inside the allowed locations:

```text
region 1  line 1            title: "... Candidate r2 (standalone)" ->
                            "... Candidate r3 (standalone)"
region 2  lines 8-9 -> 8-24 header revision block: revision = r3, parent,
                            parent_sha256, revision_reason, the three
                            no-change flags, lineage note
region 3a lines 272-273 -> 287-288  D-P03-4/§5 solver-pin intro: stale
                            "harness ecda07d0… / manifest 522d3508…" ->
                            "accepted schema-safe r2 bundle — harness
                            b31e5a6b…, manifest e71ce030…"
region 3b lines 310-313 -> 325-353  D-P03-4/§5 qualification-status
                            paragraph -> accepted-bundle provenance block
                            (three r2 hashes, external-acceptance statuses,
                            historical bundle = HISTORICAL_SUPERSEDED_FOR_
                            EXTERNAL_ACCEPTANCE_ONLY, retained not deleted);
                            SOLVER-A bounded-alternative status, SOLVER-C
                            elimination, SOLVER-D not needed and
                            PI_action = ACCEPT / MODIFY all retained verbatim
```

```text
changed_line_ranges =
r2: 1 ; 8-9 ; 272-273 ; 310-313
r3: 1 ; 8-24 ; 287-288 ; 325-353

changed_sections =
header, D-P03-4/§5 only

scientific_literal_changes = 0
PI_choice_changes = 0
solver_semantic_changes = 0
other_ratification_row_changes = 0
```

No whitespace normalization outside the changed regions. D-P03-1/2/3/5/6/7,
D-P04, D-P05, all criterion contracts, all literals, all solver stage
semantics (trust-constr options, postpolish tolerances, expansion trigger,
SLSQP fallback semantics, reference-certification rule, mode comparator) are
byte-identical to r2. The r2 parent remains valid historical provenance.

## 3. Gate state after correction

```text
GLOBAL_BLOCKER = none
GATE_SPECIFIC_BLOCKER = none

F3-STEP1-PROV-03 = CLOSED

CONTRACT_EXACTNESS = PASS
synthetic_solver_qualification_external_independent_acceptance = PASS

RATIFICATION_READY = true

F3_EXECUTION_READY = false
P03_threshold_values = NOT_COMPUTED
candidate_specific_fit = false ; crossfit_execution = false
C4_probe_execution = false ; adequacy_measurement = false
generator_selected = false ; F3_started = false ; F4_started = false
commit = false
```

PI decisions are not accepted automatically; PI ACCEPT/MODIFY review is
performed against the single r3 artifact/hash after the independent narrow
diff/hash audit.
