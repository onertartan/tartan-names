# p_konum_plus — F0 Provenance Correction — End-of-Task Report

- **Report type:** F0 provenance/execution correction report (NOT a methodology review cycle; NO F1, NO calibration, NO outcome access)
- **Status:** NON-NORMATIVE operational provenance record
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **Subject artifact:** `p_konum_plus/provenance/f0_project_identity_provenance_record_2026-08-28.md` (ART-F0)
- **ART-F0 r1 SHA256 (pre-correction):** `cdc14bb626e295f6dab8091f12ade37e3d4d3a9738c6e346c627d6a53f6b0846`
- **ART-F0 r2 SHA256 (post-correction):** `56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8`
- **Parent normative source:** `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md`
- **Parent SHA256 (re-verified this task):** `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3`

---

## 1. Old ART-F0 SHA256 (r1, pre-correction)

```text
cdc14bb626e295f6dab8091f12ade37e3d4d3a9738c6e346c627d6a53f6b0846
```

(Re-verified at task start before editing.)

## 2. Exact changes

- **§0:** added `record_revision = r2_provenance_correction_2026-08-28` and `r1_sha256 = cdc14bb6…`, with a note that r2 is byte-layer clarification only and changes no scientific content.
- **§7.3 (correction 1):** the old table — which CR-stripped the new-worktree renderings and called them "PASS (exact)" — was replaced with per-artifact records carrying the six mandated fields (`normative_ledger_sha256`, `new_worktree_on_disk_sha256`, `canonical_legacy_worktree_on_disk_sha256`, `repo_blob_sha256`, `canonical_verification_layer`, `verification_result`). Verification is now carried **only** by the canonical legacy-worktree layer (`canonical_legacy_hash_verification = PASS_EXACT`); the two mismatching `.md` renderings are recorded as `NON_CANONICAL_EOL_RENDERING`, `new_worktree_on_disk_hash_match = false`, `new_worktree_difference_reason = checkout_EOL_rendering` — no normalized stream is counted as an on-disk match anywhere. The explicit STOP rule (absent canonical file, or canonical mismatch) is stated; `.gitattributes` outside `p_konum_plus/` untouched.
- **§8 (correction 2):** the `EXTERNAL_SELF_SHA256_OF_ART_F0` placeholder was removed. `panel_source_ledger_hash` now holds the actual section-7 canonical hash, with `panel_source_ledger_hash_scope = canonical_UTF8_LF_bytes_of_SECTION_7_only`, `self_hash = false`, a precise payload definition (heading 7 inclusive → heading 8 exclusive, CR-stripped, LF-terminated), and the reproduction command. The hash is stored in §8, outside the hashed §7 payload — no self-reference. No `.sha256` sidecar was created (F12-only).
- **§11 (correction 3):** QC re-run; rows 23 (`legacy_hash_QC`) and 24 (`panel_source_ledger_hash_QC`) added — now "All 24 checks PASS (r2)".
- Nothing else changed: research question, estimand, K, sex scope, A-APP winner source, claim boundary, design-weight semantics, Ward+CH role, open pins, F0–F12 sequence, and outcome firewall are byte-identical to r1.

## 3. Canonical legacy-worktree exact SHA checks (recomputed this task)

| artifact | canonical legacy worktree on-disk SHA256 | v11 pin | result |
|---|---|---|---|
| `protocol/01_kosum_protokolu_v5_3.md` | `cf8b453f0a05e2e6fed0c8b73692c2a5361fdfe60a22b3c9fe8c612e0e13db67` | same | **PASS_EXACT** |
| `protocol/kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md` | `99c17c42711fd27dd2e55baf55f5ed41388b14a39a29e196f8eb1def34a5d0a7` | same | **PASS_EXACT** |
| `protocol/run_matrix_v4.csv` | `34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64` | same | **PASS_EXACT** |

3/3 exact — the STOP condition did not trigger. No legacy file altered.

## 4. New-worktree EOL-rendering hashes (recorded separately, NOT called PASS)

- `protocol/01_kosum_protokolu_v5_3.md`: `1f5dd374fc777b4a6da7a41f2ceec0fb823b7a2308a8449fe30beda3a441c80a` — `NON_CANONICAL_EOL_RENDERING`, `new_worktree_on_disk_hash_match = false`
- `protocol/kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md`: `e2a06560d571936361f6e5c6b39cc4ecbe6da6ab3ef5ae6ae745820158cca3db` — `NON_CANONICAL_EOL_RENDERING`, `new_worktree_on_disk_hash_match = false`
- `protocol/run_matrix_v4.csv`: `34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64` — `new_worktree_on_disk_hash_match = true`

## 5. Final `panel_source_ledger_hash`

```text
761cfdda49f62cabf20d2b5dc41f3a56721314d78c3ad81f038e1a96a923a69f
```

## 6. Independent recomputation

The section-7 canonical payload was re-extracted and re-hashed **after** all §8/§11 edits:
`761cfdda49f62cabf20d2b5dc41f3a56721314d78c3ad81f038e1a96a923a69f` — **identical**, confirming the stored value recomputes exactly and that the §8/§11 edits did not disturb the hashed payload.

## 7. New ART-F0 SHA256 (r2)

```text
56fa5093a594d083e225cf753a1617950abb5622c77b423d78ad1e18254a6aa8
```

## 8. F0 QC — all 24 checks PASS

Rows 1–22 as before (v11 and v0 hashes freshly recomputed exact this task), plus: **23** `legacy_hash_QC` PASS (canonical legacy worktree = v11 pins, `PASS_EXACT` 3/3, no normalized stream counted); **24** `panel_source_ledger_hash_QC` PASS (actual §7 hash populated and independently recomputed exactly). `F0_status = COMPLETE` therefore stands.

## 9. Confirmations

```text
F1_started = false
calibration_started = false
algorithm_CVI_outcome_access = false
legacy_performance_content_access = false
```

(Legacy files touched as SHA256 custody only; no content read; no SSA data inspected; no v11 decision changed; nothing committed.)

## 10. `git status --short --untracked-files=all` (at end of correction task)

```text
?? p_konum_plus/provenance/f0_project_identity_provenance_record_2026-08-28.md
```

Exactly the one F0 artifact, untracked and uncommitted.

## 11. Verdict

```text
F0_COMPLETE_READY_FOR_INDEPENDENT_AUDIT
```
