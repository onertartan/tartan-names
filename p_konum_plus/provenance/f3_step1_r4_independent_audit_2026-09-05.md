# p_konum_plus — F3 STEP 1 r4 — Independent Audit of the r3 → r4 Exactness Correction

```text
artifact_role = independent audit record of the Claude Code r3 -> r4
                exactness/provenance correction (prompt v4, b5ce12c3…)
status        = NON-NORMATIVE; advisory to the PI; accepts no PI-owned row
date          = 2026-09-05
auditor       = Claude (chat) — independent/advisory auditor role;
                NOT methodology authority, NOT PI authority
audit_basis   = the seven artifacts delivered to the auditor (§1); nothing
                else was available; no repository access; no execution

normative_source = ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
                   (d136502f…, v11_wins = true)
frozen_upstream  = f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md
                   (ee2cb99d…)  F2 = CLOSED ; F2_reopening = false
audited_parent   = f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md (350bc15e…)
audited_child    = f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md (5e594136…)
audited_report   = f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md (5955e865…)

classification vocabulary used (only):
  global blocker / gate-specific blocker / cleanup / informational

audit_result (summary):
  GLOBAL_BLOCKER          = none
  GATE_SPECIFIC_BLOCKER   = none new; the four active findings are correctly
                            corrected/exposed in r4 (not CLOSED — closure is
                            PI-owned, §8)
  cleanup                 = 5 items (C-01 .. C-05), none blocking
  informational           = 9 items (I-01 .. I-09)
  RATIFICATION_READY      = true   (audit-conditioned; meaning in §8)
  PI_ratification         = PENDING ; F3_EXECUTION_READY = false ; F3_started = false
```

---

## 1. Custody verification — all exact, no STOP

Every SHA256 below was recomputed by the auditor from the delivered bytes.

| artifact (delivered basename, date-dash form) | expected | observed | result |
|---|---|---|---|
| `ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` (PI) | identical | PASS |
| `f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md` | `ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43` (PI) | identical | PASS |
| `f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md` | `350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad` (PI; r4 header; report) | identical | PASS |
| `f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md` | `5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad` (report `child_sha256`) | identical | PASS |
| `f3_step1_r1_r3_provenance_correction_report_2026-09-03.md` | `006f6c615dd1e9bfddee739fb53d8565927ef41a2c9ab76b3cba082a96839815` (prompt §1.1) | identical | PASS |
| `Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md` | `b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00` (PI; report §0) | identical | PASS |
| `f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md` | none pre-stated | `5955e86590d1c4706000e4e43e6d5cf692dd000ba867a3b26170d1c5548de877` (first external observation) | RECORDED |

```text
r4 body contains its own SHA256 (self-hash)      = false   (grep 5e594136: no match)  PASS
r4 body contains "RATIFICATION_READY = true"       = false   (only the quarantine sentence
                                                            at line 28 and "= false" at 35) PASS
report asserts "changed_PI_choices = 0"            = false   (uses prior_PI_choice_overwrites
                                                            = 0 + new_PI_owned_rows)   PASS
```

Not deliverable to the auditor and therefore NOT verified here (informational, §5 I-01):
the semantic-diff text file (`a8ba561e…`), the prompt-comparison record (`afaae1eb…`),
the v3 parent prompt (`2af67777…`), any external r4 SHA256 sidecar file, and Claude
Code's §21 chat response table. The parent/child hashes plus the auditor's own
regenerated diff (§2) are the evidence this audit rests on.

## 2. Parent/child diff verification (independently regenerated)

`git diff --no-index` r3 → r4: **260 insertions, 11 deletions**, one file.
The eleven deleted r3 lines are exactly: 1 (title), 7, 8 (date, revision), 11 (parent),
14 (parent_sha256), 17–19 (revision_reason + one flag line), 23–24 (lineage), 420
(§10 D-P04 table row). Everything else is pure insertion.

Hunk map (zero-context) versus the correction report §3 regions:

```text
observed hunk                 r4 lines     report §3 claim            match
@@ -1 +1 @@                   1            region 1: 1                yes
@@ -7,2 +7,2 @@               7-8          region 1: 7-8              yes
@@ -11 +11 @@                 11           region 1: 11               yes
@@ -14 +14 @@                 14           region 1: 14               yes
@@ -17,3 +17,8 @@             17-24        region 1: 17-24 -> 17-39   yes (r3 20-22 unchanged;
@@ -23,2 +28,12 @@            28-39                                   range stated coarsely, I-02)
@@ -138,0 +154,59 @@          154-212      region 2: 138 -> 154-212   yes (insertion after 138)
@@ -222,0 +297,11 @@          297-307      region 3: 222 -> 297-307   yes (insertion after 222)
@@ -408,0 +494,155 @@         494-648      region 4: 408 -> 494-648   yes (insertion after 408)
@@ -420 +660,4 @@             660-663      region 5: 420 -> 660-663   yes
@@ -422,0 +666,6 @@           666-671      region 5: 422 -> 666-671   yes
```

Byte-identical to r3 (no hunk touches them): §1 D-P03-2; §2 D-P03-7; §3 C1, C2, C4
(probe construction, C4a, all r3 C4b bullets incl. WORSE/SEPARATE/MEAN alternatives
and the P04-scalar bullet), C5, C6; §4 D-P03-3 inventory; §5 D-P03-4 spline + SOLVER-B
pin + qualification provenance; §6; §7 D-P03-6; §8 D-P05; §9 main paragraph (r4
475–492); §10 rows D-P03-1 .. D-P03-7 and D-P05; `main_risk`; closing statement.

```text
changed_F2_content = 0          (no F2 literal, formula, bound, optimizer option touched)
changed_solver_semantics = 0    (§5 byte-identical)
new_generator_count = 0
new_diagnostic_count = 0        (K-05 is a disclosure; |U|/n_s disclosure is reporting)
delta/tau/c_cov/c_ident/c_stab/E/K/g/knots/df literals changed = 0
parent_r3_preserved = true      (350bc15e… re-verified from delivered bytes)
```

Regenerated diff delivered alongside this record:
`f3_step1_r3_to_r4_independent_regenerated_diff_2026-09-05.txt` (3-line context; not
expected to be byte-equal to Claude Code's semantic-diff file — different generator/format).

## 3. Upstream-absence verification — performed independently, not taken from the report

```text
F3-STEP1-C3-ACF-01
  v11:          grep -i 'autocorr|ACF|lag-1|lag 1|lag1'  -> no match.
                (v11 'phi' at lines 418/424/1145-1146/1214/1270 is the H* noise-law
                 AR parameter, unrelated to C3 residual ACF.)
  F2 FREEZE r1: same grep -> no match.
  r3:           only line 129 "phi_i = |lag-1 sample autocorrelation|" — a prose label,
                no estimator convention (mean handling / denominator / lag treatment).
  verdict:      CONFIRMED (matches report §2). D-C3-ACF-ESTIMATOR row is necessary.

F3-STEP1-C4B-SEPARATE-P04-01
  r3 'SEPARATE' occurrences: 196-197 (P03 per-side gating), 201 (V4L_s/V4R_s),
                203 (per-side completeness), 417 (table listing) — exactly the four
                the report cites. r3 219-222 defines only the single-scalar c4b P04
                quantity "max over sexes of C4b_F,s".
  verdict:      CONFIRMED — no LEFT/RIGHT -> single 4b comparison rule exists in r3;
                r4 records the conditional status without inventing one.

F3-STEP1-FAILBRANCH-01 / D-P04-COMMON-SUPPORT-01
  r3 'STOP|redesign|NOT_COMPARISON|common-support|common-valid':
                only lines 62 (D-P03-7: both families fail P03) and 394 (D-P04: none
                passes). No common-support language anywhere in r3.
  verdict:      CONFIRMED — the D-P04 floor-failure branch was NOT predeclared; r4 §9.4
                correctly exposes it as PI-owned rather than claiming predeclaration.
```

## 4. Prompt §19 audit items (21) — verdicts with evidence

| # | §19 item | verdict | evidence (r4 line refs unless stated) |
|---|---|---|---|
| 1 | r3 parent hash exact | PASS | §1 |
| 2 | r4 child hash exact | PASS | §1 |
| 3 | consulted-level lexicographic semantics exact | PASS | §9.1 (494–508): CONSULTED iff all earlier levels equivalent within tau; termination on resolution; consulted path must be recorded |
| 4 | same-set scalar recomputation exact | PASS | §9.2 (510–559): U2_s, U3_s, U5_s, U4_s (WORSE/MEAN), U4L_s/U4R_s (SEPARATE); "BOTH candidate scalars are recomputed on the SAME … support (per sex stratum s)"; worse-sex scalar rule of §3 unchanged |
| 5 | unconsulted levels cannot trigger floor/failure logic | PASS | §9.1 lines 501–505; §9.4 scoped to "a CONSULTED subset-defined common-valid set" |
| 6 | AGG-L1-MEAN preserved as existing r3 bounded alternative | PASS | r3 198 / r4 272 unchanged; r4 657 table row unchanged; §9.2 MEAN branch; r4 561–562 explicit "existing r3 … not a new r4 scientific option" |
| 7 | AGG-L1-SEPARATE preserved | PASS | r3 196–197 / r4 270–271 unchanged; §9.2 SEPARATE branch; conditional dependency recorded (297–307, 549–552, 666–670) |
| 8 | C4b REPORT_ONLY removes the D-P04 4b sub-level | PASS | r4 296 (r3 text retained), 487–489 (r3 text retained), §9.2 530–532 |
| 9 | superseded r3 RATIFICATION_READY=true not propagated | PASS | r4 28–29, 35; report §1 quarantine and §6 |
| 10 | no numeric D-P04 floor literal invented | PASS | every 0.80/0.85/0.90/0.95 occurrence (r4 71, 106, 244–245, 347, 659) is an r3-carried existing literal; 583–585 and 642–644 are explicitly conditional; "0.80" never appears as a floor; 2·c_complete−1 stated as mathematics only (580–582) |
| 11 | D-P04 floor represented as PI-owned | PASS | §9.3 (564–585): recommended / bounded alternative / PI_action / status pending; table row 661 |
| 12 | D-P04 failure action represented as PI-owned | PASS | §9.4 (587–612): applicability gated on the floor row; recommended NOT_COMPARISON_READY + STOP; bounded alternative = PI replacement rule; table row 662; not claimed predeclared (§3 of this audit) |
| 13 | C3 ACF: upstream pin proven absent AND D-C3-ACF-ESTIMATOR row exactly inserted | PASS | §3 of this audit; r4 154–212 matches prompt §10.2 literal-for-literal (r_bar full-series mean; numerator t=0..T−2; denominator t=0..T−1; T = 146; family/spline residual definitions; identical convention; alternatives (b) T/(T−1)=146/145 and (c) separately centred/scaled lagged-vector Pearson); table row 663 |
| 14 | zero-residual-variance / non-finite C3 behaviour exact | PASS (with cleanup C-04) | r4 185–191: exact-zero denominator or non-finite ⇒ phi_i undefined; D-P03-7 governance; no new tolerance; no silent substitution — matches prompt §10.3 verbatim |
| 15 | rejected residual-mean rationale absent | PASS | grep 'offset|amplitude' in r4: no match; rationale (193–209) states mean(r) = 0 under z_ddof0 and that the choice is NOT justified by a nonzero mean |
| 16 | CLASS_C library-call deferral does not alter estimator semantics | PASS | r4 206–209: formula pinned at STEP-1; library call deferred "provided it is mathematically verified to implement the PI-ratified formula exactly" (see I-07 for the concrete mapping risk) |
| 17 | SEPARATE-specific P04 rule: absence proven; conditional record without rule invention | PASS | §3 of this audit; r4 297–307 lists and refuses max/mean/lexicographic/equivalence combinations; 549–552; 666–670; no new PI row created |
| 18 | K-05 branch semantics cover WORSE, MEAN, SEPARATE, REPORT_ONLY correctly | PASS | §9.5 (614–647); implications re-derived in §6 of this audit; example 0.90 > 0.85 tied to a FUTURE ratification |
| 19 | every newly required PI row in the §10 table | PASS (with cleanup C-03) | rows 661–663 present in r3 row style; D-P04 row cross-references §9.1/§9.2; SEPARATE dependency recorded as a note, explicitly "not a PI row" (666) |
| 20 | no F2 / scientific generator drift | PASS | §2 of this audit |
| 21 | no forbidden execution | PASS (artifact-evidence only) | no fit, probe, cross-fit, threshold, telemetry or candidate-specific number appears in r4 or the report; `P03_threshold_values = NOT_COMPUTED` (r4 46, 678); report §6 flags all false. The auditor cannot observe Claude Code's runtime; only artifact evidence is attested |

Additional prompt-compliance checks: §15 semantic-diff constraint fields all reported
(report §4); §17 required report fields all present; §18 end-state block matches r4
header `current_gate_state`; §1.1 quarantine honoured; §4 parent/child discipline
honoured; §12 all three AGG branches present and none ratified.

## 5. Additional independent observations (beyond §19)

### 5.1 Cleanup (non-blocking; fold into the PI ratification/freeze record or into an r5 only if a MODIFY decision requires an r5 anyway — no cleanup-only child revision is recommended)

```text
C-01  §9.2 level enumeration omits C4a.
      r4 §9.2 classifies C1 and C6 as not subset-defined and defines U-sets for
      C2, C3, C5, C4b; the D-P04 order has seven levels (C1, C2, C3, C4a, C4b,
      C5, C6) and C4a is unmentioned. By r4 §3-C4a (lines 238-247) C4a has the
      full denominator 2·n_s, "nothing excluded from the denominator",
      ident_F,s "always defined" — so it is NOT subset-defined and no
      common-support recomputation applies. Effect: none (fixed by §3-C4a);
      exactness-completeness wording only. Suggested line for §9.2:
        "C4a: full-denominator level (ident_F,s over 2·n_s); not
         subset-defined; no common-support recomputation applies."
      Not a scientific choice: derived from the existing §3-C4a definition.

C-02  Stale header field `correction_scope` (r4 lines 43-45).
      Still reads "F3-STEP1-EXACT-01, F3-STEP1-EXACT-02, SOLVER-B exactness
      cleanup ONLY; all other r1 content carried forward unchanged in
      substance" — inherited from r2/r3; in r4 it is contradicted by the
      file's own `revision_reason` and the new §9.1-9.5 / D-C3 content.
      Provenance hygiene only; `revision_reason` (17-24) and
      `current_gate_state` (28-36) are correct.

C-03  D-C3-ACF-ESTIMATOR packet lacks the explicit line
      "status = pending until explicit PI action after independent audit"
      that §9.3 (577) and §9.4 (611) carry. Covered globally by the header
      gate state (line 32) and the closing "No PI acceptance is claimed"
      (678); row-level consistency only.

C-04  Trajectory-level undefined phi_i: reading to be made explicit.
      r4 185-189 (prompt-mandated wording): "phi_i = undefined and the
      existing D-P03-7 undefined-statistic / completeness governance
      applies." D-P03-7 contains two mechanisms — (a) valid-set membership
      + completeness share, (b) §8.1 propagation (undefined required
      statistic ⇒ family cannot pass). r3/r4 V3_s is defined by fit
      eligibility (family eligible fit AND spline valid fit), so a
      trajectory with an eligible fit but undefined phi_i is, literally,
      inside V3_s while its statistic is undefined; reading (a) would drop
      it from V3_s (share reduced), reading (b) would fail the criterion
      outright. r4 §9.2 U3_s wording ("valid C3 statistic") and the C4b
      A.5 precedent (failed probe ⇒ absent from the paired-valid set,
      denominator retained) both point to reading (a) at trajectory level,
      with §8.1 applying at sex level (e.g., empty set).
      Reachability: under the frozen taxonomy the case is structurally
      unreachable — an eligible fit has finite r_t (both z and ghat finite),
      |phi| <= 1 by Cauchy-Schwarz whenever the denominator is > 0, and the
      denominator is 0 only if r ≡ 0, i.e. ghat == z bitwise (L = 0).
      Recommendation (PI to confirm at closure, one sentence, no numeric,
      no new method): "an undefined trajectory-level phi_i removes
      trajectory i from V3_s and U3_s (denominator n_s retained;
      completeness governance applies); §8.1 applies if the sex-level
      statistic itself is undefined."

C-05  §4 D-P03-3 literal inventory (344-357) not extended with the two new
      PI-owned interpretive choices (C3 ACF convention; D-P04 common-support
      floor), although it already lists the analogous "C4 aggregation rule
      … = PI-owned interpretive choice". Registry completeness only; no new
      literal exists to inventory.
```

### 5.2 Informational (no action required unless stated)

```text
I-01  Unverified companion artifacts (not delivered): semantic-diff txt
      (a8ba561e…), prompt-comparison record (afaae1eb…), v3 prompt
      (2af67777…), external r4 sidecar, Claude Code §21 response table.
      Optional PI local check: sha256sum of the semantic-diff txt.
      This audit's diff evidence is independent (§2) and sufficient.

I-02  Report §3 region-1 r3 range "17-24" is coarse: the changed r3 lines
      are 17-19 and 23-24 (20-22 unchanged). Harmless.

I-03  r4 `governing` line (40-42) does not cite the v4 execution prompt
      (b5ce12c3…); the report §0 records the full prompt lineage
      (v4 <- v3, comparison record). r3 followed the same convention for
      its own prompt. Provenance is complete at report level.

I-04  r4 header keeps `scientific_change = false` with the qualifier "(no
      prior PI choice overwritten; new PI-owned rows exposed, not decided)".
      The finer-grained report fields (`prior_PI_choice_overwrites = 0`,
      `new_PI_owned_rows = …`) are the accurate statement and should be the
      ones carried into the freeze record; the common-support recomputation
      does change the D-P04 comparison procedure relative to r3 — that is the
      correction's purpose, not drift.

I-05  r3/r4 §3-C4b define V4_s explicitly "under WORSE" only (r4 273-275);
      under MEAN the identical set is implied because r_i needs both sides.
      Conditional cleanup only if the PI selects MEAN (not recommended).

I-06  Structural implication of the recommended floor (§9.3), for the PI's
      decision: with P03 floors passed on candidate-specific sets at
      c_complete, the CONSULTED common set is guaranteed only
      |U|/n_s >= 2·c_complete − 1 (0.80 if c_complete = 0.90). The
      recommended branch can therefore reach NOT_COMPARISON_READY / STOP
      even when both families pass every P03 gate; the bounded alternative
      (no additional floor + mandatory share disclosure) cannot. Under the
      bounded alternative the recomputed scalars are always defined,
      because 2·c_complete − 1 > 0 for every c_complete value in the
      bounded set (0.85 / 0.90 / 0.95 / Option B = 1). Neither branch is
      endorsed here.

I-07  CLASS_C mapping risk for the C3 estimator (for the implementation
      step): the three conventions map to different common calls —
      statsmodels acf(adjusted=False)[1] = recommended classical;
      acf(adjusted=True)[1] = alternative (b); numpy.corrcoef(r[:-1], r[1:])
      / scipy pearsonr on the lagged vectors = alternative (c). Numerically
      confirmed on a random mean-zero vector (no project data):
      classical 0.066085…, adjusted = classical × 146/145 exactly,
      Pearson 0.066135… ≠ classical. A silent corrcoef implementation
      would change the ratified convention.

I-08  Evaluation order at a CONSULTED subset-defined level under the
      recommended floor is outcome-determined (floor failure ⇒ "no
      automated winner"), so the floor check necessarily precedes any
      winner declaration at that level; an implementation should evaluate
      it first. No wording change needed.

I-09  RATIFICATION_READY vocabulary: r4 line 35 reads "false (pending r4
      independent audit + PI owner closure)". In the r3 cycle the flag
      denoted "ready for PI ACCEPT/MODIFY review", not "PI-closed". This
      audit uses that established meaning (§8); PI closure is a separate,
      later state (findings CLOSED / freeze record).
```

## 6. Mathematical checks recorded

```text
(a) Residual mean under the frozen convention: z and ghat are both z_ddof0
    on the full 146-grid (F2 FREEZE r1 §2, §3.4: L = 2T(1−rho) presupposes
    mean 0 / var 1 for both), hence mean(r) = 0 up to fp. r4 rationale correct.
(b) Non-equivalence of conventions: (b) = classical × T/(T−1) identically;
    (c) recentres/rescales each lagged subvector (means −r_{T−1}/(T−1) and
    −r_0/(T−1) ≠ 0 in general). Confirmed numerically (I-07).
(c) |phi_classical| <= 1 whenever the denominator > 0 (Cauchy–Schwarz over
    the two lagged subvectors, each bounded by the full sum of squares).
(d) K-05, WORSE/MEAN: |V4_s| >= c·n_s with V4_s ⊆ {family LEFT ∧ RIGHT
    success} ⇒ family successes >= 2c·n_s ⇒ ident_F,s >= c.  SEPARATE:
    |V4L_s| >= c·n_s and |V4R_s| >= c·n_s ⇒ successes >= 2c·n_s ⇒ ident >= c.
    Hence c_complete > c_ident ⇒ C4a non-binding on the P03_GATE path once
    the applicable C4b completeness passes; not so under REPORT_ONLY. r4 §9.5
    correct in all four branches.
(e) Intersection bound: |A ∩ B| >= |A| + |B| − n ⇒ |U|/n_s >= 2c − 1 (U2/U3
    are exactly V(P-01) ∩ V(P-02) because both already contain the spline
    validity condition). r4 §9.3 statement correct; no floor implied.
```

## 7. Finding classification (final vocabulary only)

```text
global blocker           = none
gate-specific blocker    = none new
  D-P04-COMMON-SUPPORT-01          audit verdict: correction exact  (status stays
                                   CORRECTED_IN_r4_PENDING… until PI closure)
  F3-STEP1-FAILBRANCH-01           audit verdict: correctly exposed as PI-owned
  F3-STEP1-C3-ACF-01               audit verdict: upstream absence proven; row exact
  F3-STEP1-C4B-SEPARATE-P04-01     conditional gate-specific blocker, unchanged;
                                   correctly recorded; blocks only a SEPARATE choice
cleanup                  = C-01 .. C-05 (non-blocking)
informational            = I-01 .. I-09 ; K-05 (informational, as classified upstream)
```

## 8. Gate state after this audit

```text
F0 = COMPLETE ; F1 = COMPLETE ; F2 = CLOSED ; F2_reopening = false
new_methodology_review = false

r3 parent  = 350bc15e…  read-only provenance, preserved
r4 child   = 5e594136…  = the single artifact the PI reviews

F3_STEP1_r4_independent_audit = PASS
  (all 21 §19 items PASS; custody exact; no rule invention; no numeric floor;
   no PI choice overwritten; no forbidden execution evidenced)

RATIFICATION_READY = true
  meaning (r3-cycle vocabulary, I-09): the audited r4 artifact/hash is ready
  for explicit PI ACCEPT / MODIFY review. It does NOT mean any row is
  accepted, any finding is CLOSED, or F3 may start.

D-P04-COMMON-SUPPORT-01      = CORRECTED_IN_r4_AUDIT_PASS_PENDING_PI_CLOSURE
F3-STEP1-FAILBRANCH-01       = EXPOSED_AS_PI_OWNED_AUDIT_PASS_PENDING_PI_CLOSURE
F3-STEP1-C3-ACF-01           = EXPOSED_AS_D_C3_ACF_ESTIMATOR_AUDIT_PASS_PENDING_PI_CLOSURE
F3-STEP1-C4B-SEPARATE-P04-01 = CONDITIONAL_PI_EXACTNESS_REQUIRED_IF_SEPARATE_SELECTED
K-05                         = INFORMATIONAL_RECORDED_WITH_BRANCH_SEMANTICS

PI_ratification    = PENDING
PI rows accepted by this audit = none
F3_EXECUTION_READY = false
F3_started         = false
generator_selected = false ; P03_threshold_values = NOT_COMPUTED
candidate_specific_fit = false ; crossfit_execution = false ; C4_probe_execution = false
commit = false
```

## 9. Open PI-owned rows — to be closed by explicit ACCEPT / MODIFY against r4 `5e594136…`

| row | current recommendation (r4) | bounded alternative(s) | PI_action |
|---|---|---|---|
| C4b_status (D-P03-5) | P03_GATE | REPORT_ONLY | ACCEPT / MODIFY |
| AGG-L1 (D-P03-5) | WORSE | SEPARATE (→ STOP for an exact D-P04 4b rule first) ; MEAN | ACCEPT / MODIFY |
| D-P03-6 | 6A | 6B diagnostic reference | ACCEPT / MODIFY |
| D-P03-7 | Option A | Option B ; reuse c_cov | ACCEPT / MODIFY |
| c_complete | 0.90 | per-literal alternatives | ACCEPT / MODIFY |
| D-P04_COMMON_SUPPORT_FLOOR | apply global c_complete to every CONSULTED subset-defined common set | no additional floor + mandatory share disclosure | ACCEPT / MODIFY |
| D-P04_COMMON_SUPPORT_FAILURE_ACTION | NOT_COMPARISON_READY + STOP to PI governance (applicable only with the floor) | PI-supplied replacement rule | ACCEPT / MODIFY |
| D-C3-ACF-ESTIMATOR | classical lag-1 ACF (full-series mean, biased denominator, T = 146) + zero-variance rule | (b) ×146/145 ; (c) lagged-vector Pearson | ACCEPT / MODIFY |

The remaining r3-era rows (D-P03-1, -2, -3, -4, D-P04 rule, D-P05) also carry
`PI_action = ACCEPT / MODIFY` and are unchanged by r4 except the D-P04 row's
cross-reference to §9.1/§9.2.

The final PI ratification/freeze record must (prompt §11, §20) contain a canonical
K-05 disclosure matching the ratified C4b_status / AGG / c_complete branch, the
explicit per-row decisions, the r4 hash, and — recommended — the C-01 .. C-05
cleanup fold-ins as wording (no scientific content).

## 10. Next action only

```text
PI review of r4 (5e594136…): explicit ACCEPT / MODIFY per row in §9.
  all ACCEPT with AGG-L1 = WORSE  -> ratification/freeze record (K-05 canonical
                                    disclosure + cleanup fold-in); then a
                                    separately governed F3 execution-readiness
                                    audit (CLASS_C pins incl. I-07)
  any MODIFY                      -> bounded r5 child from r4 (r4 read-only),
                                    narrow correction prompt, independent audit
  AGG-L1 = SEPARATE               -> STOP: PI supplies the exact D-P04 4b rule
                                    before ratification

No F3 execution. No F2 reopening. No PI row is accepted by this audit.
```
