# Claude Code Prompt — F3 STEP-1 PI Ratification & Freeze Record (post r4 independent audit)
## Per-row PI closure · one MODIFY (D-P04 common-support floor) · canonical K-05 · binding freeze wording · disclosures · separately governed 6B companion

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Task class:** freeze-record creation — (a) exact transcription of PI-attested per-row decisions, (b) verbatim recording of PI-adopted freeze additions (binding wording, disclosures, one PI scope decision); provenance only; bounded  
**Authority:** Claude Code is execution/provenance authority only; NOT methodology authority and NOT PI authority  
**Status:** NON-NORMATIVE execution prompt; the PI decisions inside §3–§8 are BINDING INPUT to be transcribed, not re-argued; their PI attestation is §3.0

```text
prompt_revision = v2
prompt_id = Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_2026-09-05.md
parent_prompt (v1, superseded; retained as lineage) =
  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md
  SHA256 da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7
v1 -> v2 revision_reason (external comparison review, c12b2752…; classification = cleanup):
  1. §3.0 PI attestation block added — the BINDING INPUT status of the decisions is
     documented inside the prompt, not merely asserted
  2. §4.2 floor rationale replaced: primary rationale = the additional floor would be an
     invalid-set OVERLAP requirement without independent scientific justification;
     the v1 "post-hoc STOP" sentence is withdrawn (a pre-frozen STOP trigger is not
     post-hoc; what v1 meant — that no pre-declared RESOLUTION exists after such a
     STOP — is now stated precisely as a secondary point)
  3. task-class wording and §8 labelling: the 6B companion is recorded as an explicit
     PI scientific SCOPE decision, not as transcription or cleanup
  PI decision content changed by v2 = 0 ; new literal = 0 ; new row = 0
predecessor_prompt (lineage only) =
  Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md
  SHA256 b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00
decision_basis (provenance) =
  f3_step1_r4_independent_audit_2026-09-05.md                    (audit PASS, 84c24165…)
  f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md (34862e56…)
  F3_STEP1_PI_Ratification_Freeze_Prompt_Comparison_Evaluation_2026-09-05.md    (c12b2752…)
new_methodology_review = false
F2_reopening = false
scientific_choices_made_by_Claude_Code = 0   (all choices below are PI decisions)
```

---

# 0. Purpose

The r4 candidate (`5e594136…`) passed independent audit on 2026-09-05 (GLOBAL_BLOCKER = none;
GATE_SPECIFIC_BLOCKER = none new; RATIFICATION_READY = true). The PI (Öner) has closed every
open owner row (attestation: §3.0). This task creates the **F3 STEP-1 PI ratification & freeze
record** that:

```text
TRANSCRIPTION (PI per-row decisions):
1. transcribes the PI's per-row decisions exactly (§3)
2. writes out the ONE ratified MODIFY in exact contract text
   (D-P04_COMMON_SUPPORT_FLOOR -> r4 bounded alternative; §4)
3. retires the now-inapplicable D-P04_COMMON_SUPPORT_FAILURE_ACTION row (§4.3)
4. records the canonical K-05 disclosure for the ratified branch (§5)

PI-ADOPTED FREEZE ADDITIONS (verbatim; each labelled by class):
5. binding freeze wording from the audit's five cleanup items (§6; class = cleanup wording)
6. ratification-package disclosures (§7; class = disclosure / report-only)
7. the separately governed 6B companion (§8; class = PI scientific SCOPE decision;
   specification only — not created, not executed)

CLOSURE:
8. closes the F3 STEP-1 findings and sets the post-ratification gate state (§9, §14)
```

The frozen F3 STEP-1 contract after this task is:

```text
r4 candidate 5e594136…  AS RATIFIED BY THIS RECORD
  + this record's MODIFY / retirement / binding wording take precedence over the
    corresponding r4 "recommended" text
  + on any conflict, v11 wins (v11_wins = true)
```

r4 is incorporated **by reference and hash**; it is NOT rewritten, re-derived or edited.
No F3 execution is authorized by this task.

---

# 1. Custody — verify before any write

```text
1. ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
   expected SHA256 = d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3

2. f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md
   expected SHA256 = ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43

3. f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md      (read-only provenance)
   expected SHA256 = 350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad

4. f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md      (the ratified candidate; read-only)
   expected SHA256 = 5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad

5. f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md
   expected SHA256 = 5955e86590d1c4706000e4e43e6d5cf692dd000ba867a3b26170d1c5548de877

6. f3_step1_r4_independent_audit_2026-09-05.md                        (audit PASS; gate evidence)
   expected SHA256 = 84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea
   expected location = p_konum_plus/provenance/

7. f3_step1_r1_r3_provenance_correction_report_2026-09-03.md          (historical)
   expected SHA256 = 006f6c615dd1e9bfddee739fb53d8565927ef41a2c9ab76b3cba082a96839815

8. Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md
   expected SHA256 = b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00
```

Items 1–6 mismatch ⇒

```text
STOP = true
classification = global blocker
artifact_mutation = prohibited
return observed path + observed SHA256 + expected SHA256
```

Items 7–8 mismatch ⇒ record observed vs expected, classification = cleanup, continue.

Decision-basis provenance (record; NOT a STOP condition):

```text
9. f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md
   auditor-observed SHA256 (copy received in the audit channel) =
   34862e56e6db46d0a8b07c21dea66d149cb9fa3a0d91ab21c88f12f48e2ad892
   if the project copy differs: record both values (cleanup); decisions are
   transcribed from THIS prompt, never from that document

10. f3_step1_r3_to_r4_independent_regenerated_diff_2026-09-05.txt   (auditor's diff; optional)
    auditor-observed SHA256 =
    9b070d4b1302ca5acbe19a8c69b2a67e17f823d5936f187ff47ff69405de2273

11. F3_STEP1_PI_Ratification_Freeze_Prompt_Comparison_Evaluation_2026-09-05.md
    (external comparison review of prompt v1; decision-basis provenance only)
    observed SHA256 =
    c12b275291c7341b3bd7b27618c8a25a91ad36af91ac60261e4195fdf3c73777

12. Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md
    (superseded parent prompt; lineage only)
    SHA256 = da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7
```

Source hierarchy: v11 → accepted/frozen gate artifacts → independently accepted audits →
this prompt's PI decisions → historical provenance.

---

# 2. Governance state (treat as current)

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false
new_methodology_review = false

F3_STEP1_r4_independent_audit = PASS   (84c24165…)
RATIFICATION_READY = true              (audit-conditioned; consumed by this task)

F3_EXECUTION_READY = false ; F3_started = false
candidate_specific_fit = false ; crossfit_execution = false ; C4_probe_execution = false
P03_threshold_measurement = false ; adequacy_measurement = false
generator_selected = false ; F4_started = false
algorithm_x_CVI_outcome_access = prohibited
```

---

# 3. PI decision register — BINDING INPUT (transcribe exactly)

## 3.0 PI attestation (copy verbatim into the freeze record §0; gate for this task)

```text
PI_ATTESTATION
  decided_by        = Öner (PI)
  decided_on        = 2026-09-05
  decision_channel  = Claude chat session (advisory/audit channel), after the r4
                      independent audit PASS (84c24165…) and after a row-by-row
                      comparison of the r4 recommendations with the r2 synthesis
                      (34862e56…); prompt v1 subsequently reviewed by an external
                      comparison evaluation (c12b2752…) whose three cleanup points
                      are incorporated in v2 with no change of decision content
  explicit PI statements recorded in that channel:
    (1) all r4 rows ACCEPT as recommended, EXCEPT
    (2) D-P04_COMMON_SUPPORT_FLOOR = MODIFY -> r4 bounded alternative
        (no additional D-P04 floor; same-set recomputation; mandatory
        common-support disclosure) — chosen by the PI over the r4 recommended
        floor, with the r4 failure-action row consequently NOT_APPLICABLE
    (3) 6B companion = ADOPTED as a separately governed, report-only,
        winner-ineligible diagnostic outside the F3 STEP-1 packet — an explicit
        PI scientific SCOPE decision, answered by the PI to a direct question
  attestation_mode  = dispatch of this prompt by the PI to Claude Code constitutes
                      the PI's ratification act for every decision in §3–§8
  PI_confirmation   = CONFIRMED_BY_DISPATCH
```

Claude Code gate: if `PI_confirmation` reads anything other than `CONFIRMED_BY_DISPATCH`, or the
attestation block is absent or edited into a conditional form, then

```text
STOP = true ; classification = global blocker (no PI ratification act)
freeze_record_creation = prohibited ; return the block as found
```

No LLM channel (including the authoring channel of this prompt) can confer the BINDING INPUT
status; only the PI's dispatch does.

## 3.1 Register

Every row of the r4 §10 ratification table, plus its sub-decisions, is closed below. `ACCEPT` means
the r4 recommended text is ratified unchanged. Exactly one row is `MODIFY`; exactly one row is
`NOT_APPLICABLE`.

| row (r4 §10 / sub-decision) | PI decision | ratified content (pointer; write-outs in §4–§8) |
|---|---|---|
| D-P03-1 — six criterion contracts C1–C6 | ACCEPT | r4 §3 as written, incl. the r4 §3-C3 estimator cross-reference and the r4 §3-C4b SEPARATE-status bullet (retained as provenance; moot under WORSE) |
| D-P03-2 — sex / reference population | ACCEPT | `sex_specific`; BOTH-sex pass; F n = 435, M n = 471 |
| D-P03-3 — literal inventory | ACCEPT + CL-F3-05 | r4 §4 + registry additions of §6 |
| D-P03-4 — spline benchmark + solver pin | ACCEPT | r4 §5: degree-3 clamped B-spline, knots [0,0,0,0,0.2,0.4,0.6,0.8,1,1,1,1], df = 8; SOLVER-B pin as written; r2 qualification bundle (e71ce030… / b31e5a6b… / ffda04b0…); SOLVER-A qualified bounded alternative; SOLVER-C eliminated |
| D-P03-5 — C4 row: `C4b_status` | ACCEPT | `C4b_status = P03_GATE` |
| D-P03-5 — C4 row: `AGG-L1` | ACCEPT | `AGG-L1 = WORSE`, `r_i = max(RMSE_edge_LEFT_i, RMSE_edge_RIGHT_i)`; SEPARATE and MEAN remain recorded bounded alternatives, NOT selected |
| D-P03-5 — C4 row: A.5 edge rule, E, delta_4_RMSE, tau_4b_RMSE | ACCEPT | A.5 verbatim; `E = 15`; `delta_4_RMSE = 0.10`; `tau_4b_RMSE = 0.02` |
| D-P03-6 — WC-ALC scope | ACCEPT | `6A`; plus the separately governed 6B companion ADOPTED outside the packet (§8) and the strengthened disclosure DISC-F3-05 (§7) |
| D-P03-7 — completeness gate | ACCEPT | `Option A`; `c_complete = 0.90` (owner literal; deliberately not an alias of c_cov); §8.1 propagation as written |
| D-P04 — lexicographic rule + consulted-level supports | ACCEPT + CL-F3-01 | r4 §9 main rule; §9.1 consulted-level semantics; §9.2 common-valid supports; order C1→C2→C3→C4a→C4b→C5→C6; `tau_1 = 0.01, tau_2 = 0.005, tau_3 = 0.01, tau_4a = 0.01, tau_4b_RMSE = 0.02, tau_5 = 0.01, tau_6 = 0`; terminal neutral fallback "P-01" < "P-02" |
| D-P04_COMMON_SUPPORT_FLOOR | **MODIFY → r4 bounded alternative** | exact ratified text in §4.2 |
| D-P04_COMMON_SUPPORT_FAILURE_ACTION | **NOT_APPLICABLE (retired)** | exact retirement text in §4.3 |
| D-C3-ACF-ESTIMATOR | ACCEPT + CL-F3-04 | recommended classical lag-1 sample ACF (full-series mean; standard/biased denominator; T = 146; identical for family and spline) + binding zero-variance/undefined rule; alternatives (b)/(c) NOT selected |
| D-P05 — cross-fit scheme | ACCEPT | r4 §8: K = 5, folds [0,29,58,87,116,146], g = 0, masked objective, observed-only feature start, `g_sens = NOT_INCLUDED` |
| conditional dependency F3-STEP1-C4B-SEPARATE-P04-01 | CLOSED_NOT_APPLICABLE | SEPARATE not selected; reactivates only if a future ratification cycle selects SEPARATE |
| K-05 | CANONICAL_DISCLOSURE_RECORDED | exact text in §5 |

Literals ratified unchanged (write this list into the record verbatim):

```text
c_cov = 0.90 ; c_complete = 0.90 ; c_ident = 0.85 ; c_stab = 0.10
delta_2 = 0.05 ; delta_3 = 0.05 ; delta_4_RMSE = 0.10
tau_1 = 0.01 ; tau_2 = 0.005 ; tau_3 = 0.01 ; tau_4a = 0.01 ; tau_4b_RMSE = 0.02 ; tau_5 = 0.01 ; tau_6 = 0
E = 15 ; K = 5 ; g = 0 ; T = 146 ; df_spline = 8 ; k_F = 4 (both families)
reference_active_set_identification_tol = 1e-8 ; postpolish_primary_active_set_tol = 1e-8
postpolish_expansion_tol = 1e-6 ; spline_kkt_stationarity_tol = 1e-8
spline_feasibility_acceptance_tol = 1e-8 ; kappa_solver = 0.1
P03_threshold_values = NOT_COMPUTED (spline-relative thresholds remain MEASUREMENT_DERIVED)
new_numeric_literal_count = 0
```

If any decision in this register cannot be mapped one-to-one onto an r4 row or sub-bullet, or
appears to conflict with r4 or v11:

```text
STOP and return the exact ambiguity to Öner. Do not resolve it.
```

---

# 4. Ratified D-P04 common-support contract text (replaces r4 §9.3 "recommended"; retires §9.4)

Write the following block into the freeze record verbatim (heading, numbering and wording).

```text
D-P04_COMMON_SUPPORT — RATIFIED CONTRACT TEXT

4.1 Same-set recomputation (r4 §9.1 / §9.2 ratified unchanged; binding)
  For every subset-defined D-P04 level that is actually CONSULTED, BOTH candidate
  scalars are recomputed on the SAME criterion-specific common-valid support
  U_j,s (r4 §9.2: U2_s, U3_s, U5_s; U4_s under the ratified AGG-L1 = WORSE),
  per sex stratum s, with the worse-sex scalar rule of r4 §3 and the frozen tau
  literals unchanged. Full-denominator levels (C1; C4a per CL-F3-01) and the
  structural level (C6) are not subset-defined and are not recomputed.
  Unconsulted levels: r4 §9.1 (no common-support requirement, no floor, cannot
  trigger STOP, not recomputed for decision purposes).

4.2 Floor — PI decision: MODIFY to the r4 bounded alternative
  no_additional_D_P04_common_support_floor = true
  No minimum |U_j,s| / n_s is imposed at any D-P04 level.
  Mandatory disclosure for every CONSULTED subset-defined level j and both sexes s:
    |U_j,s| ; n_s ; |U_j,s| / n_s ; the two recomputed candidate sex-level
    statistics ; the two worse-sex scalars ; their signed difference ; the
    applicable tau ; the level outcome (equivalent / resolved, and which family)
  The exact consulted path (levels reached, in order) is recorded in provenance.
  Mathematics (provenance only; NOT a floor): under the ratified P03 completeness
  floors (c_complete = 0.90 on each family's own valid / paired-valid set), every
  consulted common-valid set is the intersection of the two candidates' P03 valid
  sets (spline validity is already inside both where it applies), hence
    |U_j,s| / n_s >= 2·c_complete − 1 = 0.80   (F: >= 349/435 ; M: >= 377/471).
  PI rationale (recorded):
  (a) Primary. With both candidates individually at completeness >= 0.90, an
      additional D-P04 floor |U_j,s|/n_s >= 0.90 is equivalent to
      |F_P01,s ∪ F_P02,s| <= 0.10·n_s, where F denotes a candidate's invalid
      (failure) set on that criterion: it is a requirement on how far the two
      candidates' failure sets COINCIDE, beyond each candidate's own adequacy and
      completeness. No independent scientific justification exists for such an
      overlap requirement; two individually adequate candidates whose failures
      fall on different trajectories are not less comparable. The same-set
      recomputation already resolves the comparability defect
      (D-P04-COMMON-SUPPORT-01); the P03-guaranteed lower bound of 0.80 and the
      mandatory support disclosure make the evidential basis of the comparison
      visible.
  (b) Secondary. A floor-failure STOP would be pre-frozen and outcome-blind as a
      trigger, but no pre-declared resolution exists after it (r4 §9.4: "return
      to PI governance"); the procedure would end in an undetermined governance
      state whenever the overlap condition failed. A fully pre-determined
      procedure with disclosed common support is preferred.
  (c) Symmetry. The guaranteed common support is large and symmetric: for a
      median-type statistic, removing a share q <= 0.20 of a stratum keeps the
      median within the [50 − 50q, 50 + 50q] = [40, 60] percentile band of the
      full-stratum distribution, identically for both candidates.

4.3 D-P04_COMMON_SUPPORT_FAILURE_ACTION — NOT_APPLICABLE (row retired)
  Its applicability condition ("floor ratified as apply global c_complete") is
  not met. No D-P04 common-support failure branch exists. The only D-P04 STOP is
  the v11 branch: no family passes P03 ⇒ STOP, action = redesign.
  Degenerate case: an empty CONSULTED common-valid set is structurally unreachable
  under the ratified literals (bound in 4.2; > 0 for every c_complete > 0.5).
  Should it nevertheless occur, it is a contract-consistency violation, not a
  scientific branch: STOP, provenance investigation, no automated winner, no
  imputation, no sentinel (existing no-silent-skip principle; no new rule).

4.4 Prohibited on every CONSULTED subset-defined level (unchanged)
  candidate-specific-set P-01-vs-P-02 comparison ; imputation ; numerical
  sentinel ; post-hoc support substitution ; threshold relaxation.
```

---

# 5. Canonical K-05 disclosure — ratified branch (write verbatim)

```text
K-05 — CANONICAL DISCLOSURE (informational; scientific_change = false)
ratified branch: C4b_status = P03_GATE ; AGG-L1 = WORSE ; c_complete = 0.90 ; c_ident = 0.85

Under WORSE the C4b paired-valid set V4_s contains only trajectories whose family
LEFT and RIGHT probes both succeed (and whose spline LEFT and RIGHT probes both
succeed). Therefore
  |V4_s| / n_s >= 0.90  ⇒  family successful-probe count >= 2·0.90·n_s
                        ⇒  ident_F,s >= 0.90 > c_ident = 0.85.
Consequently c_ident is structurally non-binding on the ratified path once the
C4b completeness floor passes: no family can fail C4a while passing C4b
completeness. C4a is nevertheless computed, gated in the frozen sub-level order
(4a before 4b) and logged. c_ident = 0.85 is retained unchanged as an owner
literal; it would become independently binding only under REPORT_ONLY, which is
not ratified and cannot be selected without a new ratification cycle.

Double-count declaration: a failed probe is counted once as a C4a non-success
(numerator excluded, denominator 2·n_s retained) and once as C4b incompleteness
(absent from V4_s, denominator n_s retained). Declared, not corrected.

Denominator declaration: C4a = 2·n_s per sex ; C4b completeness = n_s per sex ;
D-P04 C4b common support U4_s = n_s per sex.

The same reasoning holds a fortiori on the D-P04 common set U4_s ⊆ V4_s.
No literal is changed by K-05.
```

---

# 6. Binding freeze wording — audit cleanup fold-ins (write verbatim; r4 is NOT edited)

```text
CL-F3-01  D-P04 level classification (completes r4 §9.2; derived from r4 §3-C4a):
  C4a: full-denominator level (ident_F,s over 2·n_s); not subset-defined; no
  common-support recomputation applies.

CL-F3-02  r4 header field `correction_scope` (r4 lines 43-45) is superseded wording
  inherited from r2/r3. The binding statement of the r4 correction scope is the
  r4 `revision_reason` block (five findings). r4 is retained byte-unchanged.

CL-F3-03  D-C3-ACF-ESTIMATOR: ratified by this record; the absent
  "status = pending" line in the r4 packet is moot.

CL-F3-04  Trajectory-level undefined C3 statistic — binding reading:
  if phi_i is undefined for trajectory i (zero residual variance or non-finite
  statistic, per the ratified rule), trajectory i is removed from V3_s and from
  U3_s; the denominator n_s is retained; the D-P03-7 completeness share governs.
  §8.1 propagation applies at sex level only (the sex-level statistic itself
  undefined, e.g. an empty set). Identical for family and spline. Structurally
  unreachable under the frozen eligibility taxonomy (finite residuals;
  |phi| <= 1 whenever the denominator is positive; denominator zero only if
  ghat == z exactly); recorded for exactness.

CL-F3-05  D-P03-3 registry additions (classification per v6 §12):
  C3 lag-1 ACF convention (classical) = PI-owned interpretive choice ;
  D-P04 common-support treatment (same-set recomputation; no additional floor;
  mandatory share disclosure) = PI-owned interpretive choice.
  No new numeric literal.
```

---

# 7. Ratification-package disclosures (write verbatim; report-only where stated; no P03/P04/P05 consumption)

```text
DISC-F3-01  C4b claim boundary (binding wording; in addition to r4 §3-C4b
  disclosure and main_risk):
  C4b is a non-inferiority test against the shape-constrained adequacy benchmark
  on masked-edge self-consistency under simulated censoring. Edge self-consistency
  is necessary, not sufficient, for censored-case identifiability. C4b is blind to
  common-mode misspecification; detection of misspecification shared by family and
  benchmark is not claimed by C4b and is addressed only within the C2/C3 claim
  boundaries. The inference "C4b passes ⇒ the masked edge is predicted correctly"
  is prohibited in every report and manuscript sentence. Absolute C4b_F,s and
  C4b_S,s are reported alongside the relative comparison.

DISC-F3-02  Per-side C4b report-only statistics (new_diagnostic = false — a
  reporting decomposition of the ratified statistic; no consumption):
  for each family and for the spline, per sex: numpy.median over V4_s of
  RMSE_edge_LEFT_i and of RMSE_edge_RIGHT_i (the same V4_s as the ratified WORSE
  statistic), reported next to the per-side probe-failure shares already required
  by r4 §3-C4b. Cross-edge caveat (disclosed): under WORSE the binding edge of a
  trajectory may differ between family and spline; the comparison is of worse-edge
  behaviour, not of the same edge.

DISC-F3-03  Invalidity is procedural, closed and identical for family and spline:
  a trajectory / fold / probe result is invalid only through the frozen failure
  taxonomy (F2 FREEZE r1 failure codes; Kural T / Kural S and admissibility on the
  full stabilized grid; spline_fit_status = FAILURE per r4 §5) — never through the
  magnitude of a finite statistic. A large but finite rho_cv, phi, RMSE_edge or
  s_stab is a valid value. Report-only, per criterion and per sex: n_s; family
  valid count; spline valid count; paired-valid count and share; family-invalid
  counts by frozen failure code; and, for each spline-relative criterion
  (C2, C3, C4b) and each family, the spline's sex-level statistic on the
  complement set {spline valid AND family invalid} with its size
  (anti-gaming transparency; no consumption).

DISC-F3-04  c_complete = 0.90 rationale (recorded; outcome-blind; family-agnostic):
  adversarial-dropout bound for a median-type sex-level statistic — removing a
  share q of the stratum moves the median at most to the [50 − 50q, 50 + 50q]
  percentile band of the full distribution (q = 0.10 ⇒ [45, 55]); under Option A
  the completeness requirement compounds across sub-fits (illustrative
  independence approximation: 5 folds ⇒ ≈ 0.979 per fold; 2 probes ⇒ ≈ 0.949 per
  probe), so 0.95 is numerically over-strict and 0.85 widens the anti-selection
  band unnecessarily. The uniform literal is not equally strict across criteria
  (C2: 10 sub-fits per trajectory pair; C4b: 4 probes) — disclosed. c_complete is
  an owner literal independent of c_cov (equal value, separate role) and was
  chosen without reference to any family-specific property.

DISC-F3-05  Strengthened 6A disclosure: the F3 adequacy claim is relative adequacy
  within the frozen WC-ALC shape-constrained benchmark architecture; it is not
  morphology validation. All eligible trajectories (906) enter every criterion's
  aggregation; no morphology-based exclusion exists. Spline-relative criteria and
  paired-valid completeness are blind to common-mode morphology misspecification;
  representativeness of the single-wave architecture is addressed under R-REV
  governance and by the separately governed 6B companion (§8), never by exclusion.
```

---

# 8. 6B companion — ADOPTED, separately governed, OUTSIDE the F3 STEP-1 packet (specification only)

Write verbatim. This task records the companion's scope and prohibitions; it does **not** create
the companion artifact and does **not** execute anything.

Decision class (write into the record): **PI scientific SCOPE decision** — explicit, attested in
§3.0 (3); NOT transcription of an r4 row, NOT cleanup, NOT provenance. It does not alter
D-P03-6 = 6A (which is ratified unchanged) and cannot be re-labelled as cleanup by any later
revision.

```text
6B_COMPANION (PI decision: ADOPTED as a separately governed companion; not a packet row)
  decision_class  = PI_SCIENTIFIC_SCOPE_DECISION (explicit; §3.0 item 3)
  artifact        = a separate companion specification, to be created in a later,
                    separately governed task under R-REV governance; this record
                    ratifies only its existence, scope, timing and prohibitions
  input           = the frozen D-P03-4 shape-constrained spline benchmark full-data
                    fit (same basis, knots, df = 8, same z-space objective) and an
                    unconstrained least-squares fit with the identical basis / knots /
                    df and identical objective (no grid-unimodality constraint;
                    closed-form linear least squares)
  statistic       = per trajectory: RMSE_constrained_i / RMSE_unconstrained_i
                    (>= 1 by construction: the constrained problem is a restriction
                    of the same convex least-squares problem; RMSE = sqrt(RSS/T),
                    T = 146, same z-space objective for both fits), per sex
  report          = quantiles by sex stratum (0.05 / 0.25 / 0.50 / 0.75 / 0.95) with
                    counts; no threshold; no label; no per-family quantity
  consumption     = none in F3: no gate, no exclusion, no P03 / P04 / P05 input, no
                    eligibility effect, no tie-break input
  action rule     = null within F3; any use only via explicit PI action under the
                    existing three v11 §27 reopen triggers
  timing          = specification frozen before F3_EXECUTION_READY; executed
                    alongside the C-criteria; results quarantined from the D-P04
                    decision path and from any generator comparison
  status flags    = third_generator = false ; winner_eligible = false ;
                    R_REV_resolution = false ; new_primary_generator = false ;
                    firewall_change = false ; family_blind = true (spline-only)
  governance      = R-REV governance; separate artifact; separate independent audit
```

---

# 9. Findings closure (write as a table in the record; states are conditional on the record's own audit)

```text
D-P04-COMMON-SUPPORT-01      = CLOSED_PENDING_RECORD_AUDIT
                               (r4 §9.1/§9.2 ratified; audit PASS 84c24165…)
F3-STEP1-FAILBRANCH-01       = CLOSED_PENDING_RECORD_AUDIT
                               (floor row ratified as bounded alternative; failure-action
                                row NOT_APPLICABLE; no undefined branch remains — §4.3)
F3-STEP1-C3-ACF-01           = CLOSED_PENDING_RECORD_AUDIT
                               (D-C3-ACF-ESTIMATOR ratified; CL-F3-04)
F3-STEP1-C4B-SEPARATE-P04-01 = CLOSED_NOT_APPLICABLE
                               (SEPARATE not selected)
K-05                         = CLOSED_AS_DISCLOSED (§5)
audit cleanup C-01 .. C-05   = CLOSED_BY_FREEZE_WORDING (CL-F3-01 .. CL-F3-05)
F3-STEP1-PROV-03             = CLOSED (historical; r3)
```

After the record's independent audit PASS these states become CLOSED with no further action.

---

# 10. Content that must NOT change

```text
r3, r4, the audit record, the correction report      : byte-unchanged (re-verify after writing)
every literal in §3                                   : unchanged; new_numeric_literal_count = 0
C1–C6 roles, ordering, P03 family-vs-spline gates    : unchanged
D-P03-1 .. D-P03-7, D-P05, D-P04 rule, solver pin     : unchanged
F2 generator specifications, primary generator set    : unchanged
R-REV governance                                      : unchanged
the PI decisions of §3                                : transcribed, not re-argued, not re-opened
```

No new row. No new bounded alternative. No new generator. No 6B execution. No DTW / elastic
alignment. No empirical tuning.

---

# 11. Firewall

```text
real SSA generator fit                    = prohibited
P05 empirical cross-fit                   = prohibited
C4 empirical probe execution              = prohibited
P03 measurement-derived threshold computation = prohibited
generator comparison / selection          = prohibited
F4 full-data refit                        = prohibited
6B companion execution                    = prohibited (specification only)
synthetic adequacy execution              = prohibited
algorithm × CVI outcome access            = prohibited
new pilot execution                       = prohibited
```

No data-derived choice. No threshold retuning. No computation of any statistic.

---

# 12. Required deliverables

```text
1. p_konum_plus/calibration/
   f3_step1_pi_ratification_freeze_record_2026-09-05.md          (structure: §13)

2. p_konum_plus/provenance/
   f3_step1_ratification_provenance_report_2026-09-05.md
     custody table (§1 items 1–10, observed vs expected)
     decision-transcription check: every §3 row → record location (line range)
     verbatim-block check: §4, §5, §6, §7, §8 present unchanged (state line ranges)
     r3 / r4 / audit record re-verified byte-unchanged AFTER the write
     end-state block (§14)

3. external SHA256 sidecars (.sha256) for deliverables 1 and 2

4. end-of-task response table (§16)
```

Do NOT self-hash any deliverable body. Do NOT commit unless separately requested.

---

# 13. Required structure of the freeze record

```text
§0  Identity block
      artifact_id = ART-F3-STEP1-FREEZE ; artifact_role = F3_STEP1_PI_RATIFICATION_FREEZE_RECORD
      date ; status = PI_RATIFIED_PENDING_INDEPENDENT_RECORD_AUDIT
      ratified_candidate = r4 path + SHA256 5e594136…
      ratification_basis = independent audit path + SHA256 84c24165… (PASS)
      decision_basis     = r2 synthesis path + observed SHA256 (§1 item 9)
      execution_prompt   = this prompt's file name + observed SHA256 (computed from the dispatched file)
      execution_prompt_parent = v1 path + SHA256 da5a0a13… (superseded; lineage only)
      PI_ATTESTATION block (§3.0) verbatim, immediately after the identity fields
      decision_class legend: TRANSCRIPTION (§3.1 rows) / CLEANUP_WORDING (CL-F3-*) /
                             DISCLOSURE (DISC-F3-*) / PI_SCIENTIFIC_SCOPE_DECISION (6B)
      normative_authority = none ; normative_source = v11 (d136502f…) ; v11_wins = true
      precedence sentence: "r4 as ratified; this record's MODIFY / retirement /
      binding wording take precedence over the corresponding r4 recommended text;
      on any conflict v11 wins."
§1  Scientific content frozen BY REFERENCE (r4 §1–§9 by section list + hash; not rewritten)
§2  PI decision register (the §3 table, verbatim, plus the ratified-literals list)
§3  Ratified D-P04 common-support contract text (§4 verbatim)
§4  Canonical K-05 disclosure (§5 verbatim)
§5  Binding freeze wording CL-F3-01 .. CL-F3-05 (§6 verbatim)
§6  Disclosures DISC-F3-01 .. DISC-F3-05 (§7 verbatim)
§7  6B companion (§8 verbatim)
§8  Findings closure (§9)
§9  Lineage table: every artifact of §1 with role (normative / frozen upstream /
    ratified candidate / audit / decision basis / historical provenance / prompt)
§10 Gate transition (§14) and "next action only"
```

Only v11 is normative. Everything else in the lineage table is custody, precursor, provenance,
audit, decision-basis or acceptance material.

---

# 14. Required end-state logic

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false

F3_STEP1_PI_RATIFICATION   = RECORDED
F3_STEP1_FREEZE_RECORD     = CREATED_PENDING_INDEPENDENT_RECORD_AUDIT
F3_STEP1_open_PI_rows      = 0
PI_attestation             = CONFIRMED_BY_DISPATCH (§3.0)
prior_PI_choice_overwrites = 0
PI_MODIFY_count            = 1   (D-P04_COMMON_SUPPORT_FLOOR)
PI_NOT_APPLICABLE_count    = 1   (D-P04_COMMON_SUPPORT_FAILURE_ACTION)
PI_scope_decision_count    = 1   (6B companion adoption; packet-external)
new_numeric_literal_count  = 0

RATIFICATION_READY         = consumed (historical)
F3_EXECUTION_READY         = false
F3_started                 = false
6B_companion               = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED
P03_threshold_values       = NOT_COMPUTED
generator_selected         = false ; commit = false
```

Next action only:

```text
1. independent audit of the freeze record + provenance report (transcription exactness)
2. then a separately governed F3 STEP-2 implementation-pin task (CLASS_C pins:
   ACF library call verified against the ratified formula — numpy.corrcoef /
   pearsonr on lagged vectors implement alternative (c), NOT the ratified
   convention, and are prohibited as its implementation; spline solver; probe
   masks; fold scheme; 6B companion specification), synthetic qualification
   only, no real SSA fit until its own gate
```

---

# 15. Independent audit requirements after Claude Code returns (do NOT perform them yourself)

```text
1.  hashes of §1 items 1–6 exact ; 7–12 recorded
2.  r3 / r4 / audit record byte-unchanged after the write
2a. §3.0 PI attestation block present verbatim in the record §0 with
    PI_confirmation = CONFIRMED_BY_DISPATCH; decision_class legend present;
    6B labelled PI_SCIENTIFIC_SCOPE_DECISION
3.  every §3.1 row transcribed exactly once; no row added, dropped or re-worded
4.  exactly one MODIFY (floor) and exactly one NOT_APPLICABLE (failure action)
5.  §4 text verbatim; the 0.80 bound stated as mathematics only; no floor implied
6.  §5 K-05 text verbatim and consistent with the ratified branch
7.  CL-F3-01..05 verbatim ; DISC-F3-01..05 verbatim ; §8 companion verbatim
8.  ratified-literals list identical to §3 ; new_numeric_literal_count = 0
9.  precedence sentence present ; v11_wins = true
10. no execution, no computed statistic, no candidate-specific number anywhere
11. end-state block identical to §14 ; F3_EXECUTION_READY = false
12. sidecars present ; no self-hash in any body
```

---

# 16. Required Claude Code response format

| Check | PASS/FAIL | Evidence |
|---|---|---|
| v11 hash | | |
| F2 FREEZE r1 hash | | |
| r3 parent hash | | |
| r4 ratified-candidate hash | | |
| r3→r4 correction report hash | | |
| independent audit record hash (84c24165…) | | |
| r3 / r4 / audit record byte-unchanged after write | | |
| decision-basis synthesis hash recorded | | |
| comparison-evaluation hash (c12b2752…) and v1 parent-prompt hash (da5a0a13…) recorded | | |
| §3.0 PI attestation present; PI_confirmation = CONFIRMED_BY_DISPATCH (else STOP) | | |
| §3.1 register transcribed exactly (row count = 16 incl. sub-rows) | | |
| ratified-literals list verbatim | | |
| §4 D-P04 common-support text verbatim | | |
| failure-action row retired as NOT_APPLICABLE | | |
| §5 canonical K-05 verbatim | | |
| CL-F3-01..05 verbatim | | |
| DISC-F3-01..05 verbatim | | |
| 6B companion §8 verbatim; labelled PI_SCIENTIFIC_SCOPE_DECISION; not created; not executed | | |
| findings closure table present (§9) | | |
| precedence sentence + v11_wins present | | |
| no new literal / no new row / no re-argued decision | | |
| no forbidden execution | | |
| freeze record created | | |
| provenance report created | | |
| external SHA256 sidecars created; no self-hash | | |
| F3_EXECUTION_READY remains false | | |

Then:

```text
freeze record path =
freeze record SHA256 =

provenance report path =
provenance report SHA256 =

this prompt observed SHA256 =
v1 parent prompt SHA256 (expected da5a0a13…) =
r2 synthesis observed SHA256 =
comparison evaluation observed SHA256 (expected c12b2752…) =

PI_attestation = CONFIRMED_BY_DISPATCH / (STOP reason)
open PI rows = 0 (or list)
STOP conditions triggered = none (or list)
```

Final classification vocabulary only: `global blocker` / `gate-specific blocker` / `cleanup` /
`informational`.

---

# 17. Final instruction

Execute only the bounded freeze-record task defined above, and only if the §3.0 attestation gate
passes.

Do not reopen F2. Do not re-argue, re-open, add, drop or re-word any PI decision of §3.
Do not re-label the 6B companion as cleanup or transcription.
Do not compute any statistic. Do not create or execute the 6B companion. Do not introduce
a numeric D-P04 floor. Do not edit r3, r4 or the audit record. Do not run F3.

If any §3 decision cannot be mapped exactly onto r4, or any verbatim block conflicts with
r4 or v11:

```text
STOP and return the bounded ambiguity to Öner.
```
