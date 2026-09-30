# p_konum_plus — F3 STEP-1 PI Ratification & Freeze Record — r1

## §0 Identity block

```text
artifact_id     = ART-F3-STEP1-FREEZE
artifact_role   = F3_STEP1_PI_RATIFICATION_FREEZE_RECORD
date            = 2026-09-05
status          = SUPERSEDED_BY_r1_FOR_READING (historical)
record_revision = r1_2026-09-05
parent_record   = f3_step1_pi_ratification_freeze_record_2026-09-05.md
parent_sha256   = bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f
record_audit    = f3_step1_freeze_record_independent_audit_2026-09-05.md (PASS; 99b615d2…)
r1_correction   = C-R1-01 cross-reference key only; every verbatim block of the parent is
                  byte-unchanged; scientific_change = false; PI_decision_change = 0
status          = PI_RATIFIED_RECORD_AUDIT_PASS_r1_PENDING_NARROW_REAUDIT

ratified_candidate =
p_konum_plus/calibration/f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md
SHA256 = 5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad

ratification_basis =
p_konum_plus/provenance/f3_step1_r4_independent_audit_2026-09-05.md
SHA256 = 84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea   (PASS)

decision_basis =
p_konum_plus/provenance/f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md
observed SHA256 = 34862e56e6db46d0a8b07c21dea66d149cb9fa3a0d91ab21c88f12f48e2ad892

execution_prompt =
Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
(dispatched from repository custody:
 p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md)
observed SHA256 = 679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09

execution_prompt_lineage (all superseded revisions retained as lineage; v5 is the
sole dispatch candidate) =
  v1  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md
      SHA256 da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7
  v2  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_2026-09-05.md
      SHA256 2860fade8d34e74b8ea77d22d469fa0c9b29e05eaf27310b407a45031a626243
  v3  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v3_2026-09-05.md
      SHA256 4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7
  v4  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_2026-09-05.md   (parent)
      SHA256 bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458
  v5  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md   (execution prompt)
      SHA256 = the value recorded in the execution_prompt field above
      (all superseded revisions lineage only)
```

```text
PI_ATTESTATION (self-contained; dispatch-based)
  attested_by       = Öner (PI)
  attested_on       = 2026-09-05
  attestation       = By dispatching the execution prompt
                      Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
                      to Claude Code, the PI attests that every decision in its
                      §3–§8 is his own binding decision, in particular:
    (1) all r4 §10 rows ACCEPT as recommended, EXCEPT
    (2) D-P04_COMMON_SUPPORT_FLOOR = MODIFY -> the r4 bounded alternative
        (no additional D-P04 floor; same-set recomputation; mandatory
        common-support disclosure), with the r4 failure-action row
        consequently NOT_APPLICABLE
    (3) 6B companion = ADOPTED as a separately governed, report-only,
        winner-ineligible diagnostic outside the F3 STEP-1 packet
        (PI scientific SCOPE decision)
  attestation_mode  = dispatch of that execution prompt by the PI to Claude Code
                      constitutes the PI's ratification act for every decision in
                      its §3–§8;
                      no prior advisory, review or chat document is load-bearing
                      for this status — such documents are provenance only and
                      confer no PI authority
  PI_confirmation   = CONFIRMED_BY_DISPATCH

DECISION_HISTORY (informational; non-load-bearing; not to be verified as a gate)
  The decisions were formed after the r4 independent audit PASS (84c24165…), a
  row-by-row comparison with the r2 synthesis (34862e56…), and four external
  reviews of the execution prompt's revisions (c12b2752…, 07c33063…, 90051cb7…,
  8b04f83e…) whose cleanup points are incorporated with no change of decision
  content.
```

```text
CROSS-REFERENCE KEY (binding reading rule for section numbers inside the verbatim
blocks of §0, §2–§8 and §10, which retain the execution prompt's numbering):
  prompt §3.0            -> this record §0 PI_ATTESTATION
  prompt §3.1            -> this record §2 (register)
  prompt §4 (4.1–4.4)    -> this record §3
  prompt §5              -> this record §4 (K-05)
  prompt §6              -> this record §5 (CL-F3-01..05)
  prompt §7              -> this record §6 (DISC-F3-01..05)
  prompt §8              -> this record §7 (6B companion)
  prompt §9              -> this record §8 (findings closure)
  prompt §14             -> this record §10
References to "r4 §…" are unaffected (they address the ratified candidate).
```

```text
decision_class legend:
  TRANSCRIPTION                 = §2 register rows (PI per-row decisions)
  CLEANUP_WORDING               = CL-F3-01 .. CL-F3-05 (§5)
  DISCLOSURE                    = DISC-F3-01 .. DISC-F3-05 (§6)
  PI_SCIENTIFIC_SCOPE_DECISION  = 6B companion (§7)

normative_authority = none
normative_source    = v11 (d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3)
v11_wins            = true
```

Precedence sentence: "r4 as ratified; this record's MODIFY / retirement /
binding wording take precedence over the corresponding r4 recommended text;
on any conflict v11 wins."

## §1 Scientific content frozen BY REFERENCE

The full F3 STEP-1 scientific/operational contract is incorporated by reference
and hash from the ratified candidate r4 (`5e594136…`), NOT rewritten:

```text
r4 §1  D-P03-2 sex / reference population
r4 §2  D-P03-7 completeness gate (Option A; §8.1 propagation)
r4 §3  D-P03-1 standalone criterion contracts C1–C6
       (incl. C4a/C4b chain, A.5 edge rule, D-C3-ACF-ESTIMATOR packet,
        SEPARATE-status bullet)
r4 §4  D-P03-3 literal inventory
r4 §5  D-P03-4 spline benchmark + SOLVER-B pin
       (r2 qualification bundle e71ce030… / b31e5a6b… / ffda04b0…)
r4 §6  D-P03-5 consolidated C4 row
r4 §7  D-P03-6 WC-ALC scope (6A)
r4 §8  D-P05 cross-fit scheme
r4 §9  D-P04 rule + §9.1 consulted-level semantics + §9.2 common-valid supports
       (+ §9.3/§9.4 superseded by this record's §3; §9.5 K-05 superseded by §4)
```

Upstream frozen inputs unchanged: v11 (`d136502f…`, sole normative source);
F2 FINAL FREEZE r1 (`ee2cb99d…`, F2 = CLOSED).

## §2 PI decision register (BINDING INPUT, transcribed exactly)

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

Literals ratified unchanged:

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

## §3 Ratified D-P04 common-support contract text (replaces r4 §9.3 "recommended"; retires §9.4)

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
      overlap requirement; two individually adequate candidates should not be
      declared non-comparable solely because their invalid sets differ, absent
      an independently justified overlap requirement (differing failure patterns
      remain scientifically informative and are disclosed under DISC-F3-03, not
      used as a comparability gate). The same-set
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
  Degenerate case: an empty CONSULTED common-valid set is mathematically excluded
  under the ratified literals (a theorem, not a rarity claim: the bound in 4.2 is
  > 0 for every c_complete > 0.5, and D-P04 is entered only after both families
  pass the P03 completeness floors).
  Should it nevertheless occur, it is a contract-consistency violation, not a
  scientific branch: STOP, provenance investigation, no automated winner, no
  imputation, no sentinel (existing no-silent-skip principle; no new rule).

4.4 Prohibited on every CONSULTED subset-defined level (unchanged)
  candidate-specific-set P-01-vs-P-02 comparison ; imputation ; numerical
  sentinel ; post-hoc support substitution ; threshold relaxation.
```

## §4 Canonical K-05 disclosure — ratified branch

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

Denominator declaration: C4a denominator = 2·n_s per sex ; C4b completeness-share
denominator = n_s per sex ; D-P04 C4b common-support-share denominator = n_s per
sex, with |U4_s| as the common-valid support count (|U4_s| <= |V4_s| <= n_s; no
equality with n_s is required or implied).

Every trajectory in the D-P04 common set U4_s also satisfies the LEFT/RIGHT success
requirements, but no additional C4a completeness implication is derived from
|U4_s|, because no D-P04 common-support floor is ratified (U4_s ⊆ V4_s may be
smaller than V4_s; the K-05 implication rests on the P03 quantity |V4_s|/n_s only).
No literal is changed by K-05.
```

## §5 Binding freeze wording — audit cleanup fold-ins (r4 is NOT edited)

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
  undefined, e.g. an empty set). Identical for family and spline. Reachability:
  an eligible fit has finite residuals and |phi| <= 1 whenever the denominator is
  positive; the denominator is zero only for an exact fit (ghat == z on all 146
  grid points). This case is expected to be extremely rare but is not excluded by
  the frozen eligibility taxonomy; it is explicitly governed here for exactness.

CL-F3-05  D-P03-3 registry additions (classification per v6 §12):
  C3 lag-1 ACF convention (classical) = PI-owned interpretive choice ;
  D-P04 common-support treatment (same-set recomputation; no additional floor;
  mandatory share disclosure) = PI-owned interpretive choice.
  No new numeric literal.
```

## §6 Disclosures DISC-F3-01 .. DISC-F3-05 (report-only where stated; no P03/P04/P05 consumption)

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
  percentile band of the full distribution (for the ratified literal,
  q = 1 − c_complete = 0.10 ⇒ [45, 55]; a derived bound, not a frozen literal,
  threshold or decision parameter). This bound is assumption-free: no
  independence or equal-success-probability assumption across sub-fits is made
  or needed. Qualitative disclosure: the completeness requirement is imposed
  jointly on all sub-fits that define a criterion's valid / paired-valid set, whose
  number differs across criteria (C2: 10 sub-fits per trajectory pair — 5 folds
  each for family and spline; C4b: 4 probes — LEFT/RIGHT each for family and
  spline; C5: 5 folds), so the uniform literal is not equally strict across
  criteria — disclosed, not corrected. c_complete is an owner literal
  independent of c_cov (equal value, separate role) and was chosen without
  reference to any family-specific property.

DISC-F3-05  Strengthened 6A disclosure: the F3 adequacy claim is relative adequacy
  within the frozen WC-ALC shape-constrained benchmark architecture; it is not
  morphology validation. All 906 eligible trajectories remain represented in the
  F3 adequacy governance: C1 uses the full stratum denominator; subset-defined
  criteria (C2, C3, C4b, C5) compute their statistics on the frozen valid /
  paired-valid sets while retaining n_s as the completeness denominator; no
  morphology-based exclusion is permitted. Spline-relative criteria and
  paired-valid completeness are blind to common-mode morphology misspecification;
  representativeness of the single-wave architecture is addressed under R-REV
  governance and by the separately governed 6B companion (§8), never by exclusion.
```

## §7 6B companion — ADOPTED, separately governed, OUTSIDE the F3 STEP-1 packet (specification only)

This record records the companion's scope and prohibitions; it does **not** create
the companion artifact and does **not** execute anything.

Decision class: **PI scientific SCOPE decision** — explicit, attested in
§0 PI_ATTESTATION (3); NOT transcription of an r4 row, NOT cleanup, NOT
provenance. It does not alter D-P03-6 = 6A (which is ratified unchanged) and
cannot be re-labelled as cleanup by any later revision.

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
  statistic       = per trajectory: RMSE_constrained_i / RMSE_unconstrained_i, per sex
                    (when both fits are valid and RMSE_unconstrained_i > 0, the ratio
                    is >= 1 by construction: the constrained problem is a restriction
                    of the same convex least-squares problem; RMSE = sqrt(RSS/T),
                    T = 146, same z-space objective for both fits; the
                    RMSE_unconstrained_i = 0 / invalid-fit cases are pinned in the
                    companion specification, see report)
  report          = sex-specific distributional summaries of the ratio, with counts;
                    no threshold; no label; no per-family quantity.
                    The exact reporting design is NOT pinned here (this freeze
                    records existence, scope, timing and prohibitions only); it is
                    pinned outcome-blind in the separately governed 6B companion
                    specification, which must fix at least:
                      - the exact summary statistics / quantile set
                      - the exact behaviour when RMSE_unconstrained_i = 0
                        (ratio undefined) or either fit is invalid
                      - the identical z-space objective and grid for both fits
                    new numeric literal introduced by this record for 6B = 0
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

## §8 Findings closure (states conditional on this record's own audit)

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
C-R1-01 = CLOSED_BY_r1_KEY
```

After the record's independent audit PASS these states become CLOSED with no
further action.

## §9 Lineage table

| artifact | SHA256 | role |
|---|---|---|
| `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` | normative |
| `p_konum_plus/calibration/f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md` | `ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43` | frozen upstream |
| `p_konum_plus/calibration/f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md` | `350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad` | historical provenance (read-only parent) |
| `p_konum_plus/calibration/f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md` | `5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad` | ratified candidate |
| `p_konum_plus/provenance/f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md` | `5955e86590d1c4706000e4e43e6d5cf692dd000ba867a3b26170d1c5548de877` | historical provenance |
| `p_konum_plus/provenance/f3_step1_r4_independent_audit_2026-09-05.md` | `84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea` | audit (ratification basis; PASS) |
| `p_konum_plus/provenance/f3_step1_r1_r3_provenance_correction_report_2026-09-03.md` | `006f6c615dd1e9bfddee739fb53d8565927ef41a2c9ab76b3cba082a96839815` | historical provenance |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md` | `b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00` | prompt (predecessor; lineage only) |
| `p_konum_plus/provenance/f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md` | `34862e56e6db46d0a8b07c21dea66d149cb9fa3a0d91ab21c88f12f48e2ad892` | decision basis |
| `p_konum_plus/provenance/f3_step1_r3_to_r4_independent_regenerated_diff_2026-09-05.txt` | `9b070d4b1302ca5acbe19a8c69b2a67e17f823d5936f187ff47ff69405de2273` | audit evidence (auditor's diff) |
| `p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_Comparison_Evaluation_2026-09-05.md` | `c12b275291c7341b3bd7b27618c8a25a91ad36af91ac60261e4195fdf3c73777` | decision-basis provenance |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md` | `da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7` | prompt (superseded; lineage only) |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_2026-09-05.md` | `2860fade8d34e74b8ea77d22d469fa0c9b29e05eaf27310b407a45031a626243` | prompt (superseded; lineage only) |
| `p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_v2_Review_2026-09-05.md` | `07c3306339eabb86fce0f24578ee5e539d0fb85fb06e3e181a22cf0e3a0bb842` | decision-basis provenance |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v3_2026-09-05.md` | `4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7` | prompt (superseded; lineage only) |
| `p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_v3_Review_2026-09-05.md` | `90051cb702d63d506213c04f38fac6c77d4651ddc812bb0733cd01bef346db0d` | decision-basis provenance |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_2026-09-05.md` | `bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458` | prompt (superseded parent; lineage only) |
| `p_konum_plus/provenance/F3_STEP1_PI_Ratification_Freeze_Prompt_v4_Review_2026-09-05.md` | `8b04f83e439b786afce1ad969dfd12028ccc02a344e34e26e6f217aa343bac55` | decision-basis provenance |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md` | `679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09` | prompt (execution prompt) |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v1_2026-09-05.md` | `adb59f60e7c1a72b6e901b86d1958a874f09c1301003b32c4884816fe43ab792` | import provenance |
| `p_konum_plus/prompts/Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v2_2026-09-05.md` | `09df38443346229fc2dac0afb795e6c5cd6b621fe1e4e6756316c43416e96f65` | import provenance |
| `p_konum_plus/provenance/f3_step1_freeze_record_task_stop_report_2026-09-05.md` | `57c92d2df6f2b923fedbb1cef3671238ca3020f8ac02cc16eb553eaa9026e969` | import provenance (STOP report) |
| `p_konum_plus/provenance/f3_step1_custody_import_endoftask_report_2026-09-05.md` | `9d79ec5697e897d90ce88d663354e8bd2a3453cf77f990c21a9fb7b80801df23` | import provenance |
| `p_konum_plus/provenance/f3_step1_ratification_provenance_report_2026-09-05.md` | `2c746625acee73e610e09179ed00c1dc90c0dddc905c1c05d7dcf5c91c1ad1fc` | provenance report (deliverable 2) |
| `p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md` | `bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f` | parent record (superseded for reading; historical) |
| `p_konum_plus/provenance/f3_step1_freeze_record_independent_audit_2026-09-05.md` | `99b615d2c3ee0c94815af7793e1d8be669a29ef5d070891224d457305864a4dc` | independent record audit (PASS) |

Only v11 is normative. Everything else in this table is custody, precursor,
provenance, audit, decision-basis or acceptance material.

## §10 Gate transition and next action

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false

F3_STEP1_PI_RATIFICATION   = RECORDED
F3_STEP1_FREEZE_RECORD     = AUDIT_PASS_r1_PENDING_NARROW_REAUDIT
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

After that audit PASS, two separately governed tasks (order between them not fixed here):

2. F3 STEP-2 implementation-pin task — CLASS_C only:
   - ACF library/API call verified against the ratified formula (numpy.corrcoef /
     pearsonr on lagged vectors implement alternative (c), NOT the ratified
     convention, and are prohibited as its implementation)
   - spline solver implementation pins (SOLVER-B as ratified)
   - probe-mask implementation exactness (E = 15, LEFT/RIGHT)
   - fold-scheme implementation exactness (K = 5 boundaries as ratified)
   - synthetic qualification only; no real SSA fit until its own gate
   - contains NO 6B content

3. Separately governed R-REV 6B companion specification task:
   - separate artifact, separate provenance, separate independent audit
   - specification only (scope per §8; pins the deferred reporting design and
     undefined-ratio behaviour); no 6B execution

F3_EXECUTION_READY remains false until all required pre-execution governance
closures (1, 2 and 3 above) have independently passed.
```
