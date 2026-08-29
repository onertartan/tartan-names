# p_konum_plus — F1 r4a Provenance Cleanup — Report

- **Report type:** cleanup/provenance-only report (NOT a methodology review cycle; NO F2, NO scientific F1 change, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **HEAD at execution:** `a26098a4eac480a4156d8acfa9783954f007fb26`

```text
supersedes_for_cleanup_only =
  f1_r4_source_semantics_correction_report_2026-08-28.md

scientific_supersession =
  false

scientific_F1_content_changed =
  false
```

The historical r4 correction report was NOT modified: its SHA256 is
`05a5b1f17abd4316ece05c93e31db62d902151c29857ccb3f4fefe0233188e9b` both
before and after this cleanup pass.

---

## 1. Precheck / hash results — PASS

All required hashes verified exact before editing: ART-F1 r4
`d44075385634bdd16d76d85ddb9aa3876013c5235867d0edf4d06bc12dfa079c`; eligible
manifest `8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32`;
input hash table
`aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac`; v11
`d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3`; v0
`b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280`; ART-F0
`56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8`. Root,
branch, and HEAD as expected. No STOP.

## 2. Exactly three ART-F1 cleanup corrections

1. **Title / revision consistency:** title changed from `FINAL (r3)` to
   `FINAL (r4a)`; `record_revision = r4a_provenance_cleanup_2026-08-28`;
   `r4_sha256 = d4407538…` appended to the preserved r1/r2/r3 lineage; the
   statement "r4a changes provenance/metadata only. No scientific F1 decision
   or data-derived result changed." added to §0.
2. **Governing-hash table parent:** stale row `ART-F1 r2 (pre-pass state)`
   (`667801dc…`) replaced with `ART-F1 r4 (pre-cleanup state)`
   (`d4407538…`), making the immediate parent of r4a explicit; §0 lineage
   metadata untouched.
3. **External-verification attribution:** §4 attribution reworded to
   "independent external review outside Claude Code using official SSA
   webpages; findings supplied to Claude Code on 2026-08-28" — no longer
   attributed specifically to the PI. Retained unchanged:
   `current_SSA_record_vintage = March_2026`,
   `birth_year_2025_officially_supported = true`,
   `right_edge_2025_blocker = false`, and the pre-1937 limitation.

## 3. OD-1..OD-10 scientific content unchanged — CONFIRMED

OD-1 national_only · OD-2 146 raw yob files · OD-3 released_record_share ·
OD-4 1880..2025 (T=146) · OD-5 FULL-support eligibility · OD-6
complete-support restriction, no imputation · OD-7 corrected disclosure
semantics (published => count >= 5; converse NOT established; count not
identified; `exclude_via_complete_support_eligibility`; no [0,4] restoration)
· OD-8 11-step order · OD-9 no additional pre-z transform · OD-10 mean /
population sd ddof=0. No QC result altered.

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

This file: `p_konum_plus/provenance/f1_r4a_provenance_cleanup_report_2026-08-28.md`
(supersedes the r4 report for cleanup narrative only; scientific_supersession = false).

## 10. Historical r4 report NOT modified — CONFIRMED

`f1_r4_source_semantics_correction_report_2026-08-28.md` SHA256 identical
before and after: `05a5b1f17abd4316ece05c93e31db62d902151c29857ccb3f4fefe0233188e9b`.

## 11. Files changed/created

Changed: `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md`
(three cleanup corrections, → r4a). Created: this report. Nothing else
touched; no `.sha256` sidecar created (F12-only).

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

## 13. F1 status

```text
F1_status = COMPLETE
F1_complete = true
F2_allowed = true
methodology_contract_status = draft_pre_F12
```

## 14. Verdict

```text
F1_R4A_PROVENANCE_CLEANUP_COMPLETE_READY_FOR_INDEPENDENT_AUDIT
```
