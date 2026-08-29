# p_konum_plus — F1 r4a Provenance Cleanup — End-of-Task Response (verbatim)

- **Report type:** end-of-task response of the r4a cleanup pass (cleanup/provenance only; NO F2, NO scientific F1 change, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Relationship:** companion to the in-task artifact `f1_r4a_provenance_cleanup_report_2026-08-28.md` (same pass; this file archives the end-of-task chat response verbatim, including grep evidence and final git status). No supersession of any kind.
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `a26098a4eac480a4156d8acfa9783954f007fb26`
- **Subject artifact:** `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` — r4 `d44075385634bdd16d76d85ddb9aa3876013c5235867d0edf4d06bc12dfa079c` → r4a `5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0`

---

## 1. Precheck / hash results — PASS

Root ✓, branch `p_konum_plus` ✓, HEAD `a26098a4…`. All exact before editing: ART-F1 r4 `d4407538…`, eligible manifest `8a6034eb…`, input hash table `aa86f1ea…`, v11 `d136502f…`, v0 `b6b4ed83…`, ART-F0 `56fa5093…`. No STOP; nothing auto-repaired.

## 2. Exactly three ART-F1 cleanup items changed — CONFIRMED

1. **Title/revision:** `FINAL (r3)` → `FINAL (r4a)`; `record_revision = r4a_provenance_cleanup_2026-08-28`; `r4_sha256` appended to the preserved r1/r2/r3 lineage; statement added: "r4a changes provenance/metadata only. No scientific F1 decision or data-derived result changed."
2. **§1 parent row:** stale `ART-F1 r2 (pre-pass state)` (`667801dc…`) → `ART-F1 r4 (pre-cleanup state)` (`d4407538…`); §0 lineage untouched.
3. **§4 attribution:** now "independent external review outside Claude Code using official SSA webpages; findings supplied to Claude Code on 2026-08-28" — not attributed to the PI. Retained: `current_SSA_record_vintage = March_2026`, `birth_year_2025_officially_supported = true`, `right_edge_2025_blocker = false`, pre-1937 limitation.

Grep confirms no `FINAL (r3)`, `pre-pass state`, or `performed by the PI` remains.

## 3. OD-1..OD-10 scientific content unchanged — CONFIRMED

No OD entry, contract line, operation order, z-convention, or QC result was touched; OD-7 remains exactly the r4 corrected semantics (`published => count >= 5`; converse NOT established; no [0,4] restoration; treatment = `exclude_via_complete_support_eligibility`).

## 4. Eligible counts unchanged — CONFIRMED

F = 435, M = 471.

## 5. Eligible-manifest SHA256 (byte-identical)

```text
8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32
```

## 6. Input-hash-table SHA256 (byte-identical)

```text
aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac
```

## 7. Old ART-F1 r4 SHA256

```text
d44075385634bdd16d76d85ddb9aa3876013c5235867d0edf4d06bc12dfa079c
```

## 8. New ART-F1 r4a SHA256

```text
5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0
```

## 9. Superseding cleanup report created

`p_konum_plus/provenance/f1_r4a_provenance_cleanup_report_2026-08-28.md` — contains the required block: `supersedes_for_cleanup_only = f1_r4_source_semantics_correction_report_2026-08-28.md`, `scientific_supersession = false`, `scientific_F1_content_changed = false`, plus the three changes and old/new hashes.

## 10. Historical r4 report NOT modified — CONFIRMED

`f1_r4_source_semantics_correction_report_2026-08-28.md` hashes identically before and after the pass: `05a5b1f17abd4316ece05c93e31db62d902151c29857ccb3f4fefe0233188e9b`.

## 11. Files changed/created

Changed: `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` (three cleanups → r4a). Created: the r4a cleanup report. Nothing else; no `.sha256` sidecar (F12-only). F1 status stands: `F1_status = COMPLETE`, `F1_complete = true`, `F2_allowed = true`; project remains `methodology_contract_status = draft_pre_F12`.

## 12. Firewall confirmation

```text
legacy_performance_content_access = false
algorithm_CVI_outcome_access = false
generator_fit = false
generator_adequacy = false
Q_CD_created = false
B_star_created = false
H_star_created = false
F2_started = false
```

## 13. `git status --short --untracked-files=all` (at end of cleanup pass)

```text
?? p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
?? p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv
?? p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
?? p_konum_plus/provenance/f1_execution_report_2026-08-28.md
?? p_konum_plus/provenance/f1_final_freeze_report_2026-08-28.md
?? p_konum_plus/provenance/f1_r4_source_semantics_correction_report_2026-08-28.md
?? p_konum_plus/provenance/f1_r4a_provenance_cleanup_report_2026-08-28.md
?? p_konum_plus/provenance/f1_refinement_report_2026-08-28.md
```

Nothing staged, nothing committed.

## 14. Verdict

```text
F1_R4A_PROVENANCE_CLEANUP_COMPLETE_READY_FOR_INDEPENDENT_AUDIT
```
