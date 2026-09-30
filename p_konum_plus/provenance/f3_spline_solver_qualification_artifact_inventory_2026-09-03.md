# p_konum_plus — F3 Spline Solver Qualification — Artifact Inventory for External Independent Audit

```text
artifact_role = custody/provenance inventory only (Output 3 of the 2026-09-03
                narrow exactness correction task)
status        = NON-NORMATIVE
date          = 2026-09-03
rerun_performed = false
underlying_artifacts_modified = false
```

## Inventory

| # | role | path | SHA256 | bytes | tracked | modified_during_this_task |
|---|---|---|---|---|---|---|
| A | qualification fixture manifest (written and hashed before execution by the harness's phase-1 code path) | `p_konum_plus/calibration/f3_spline_solver_qualification_manifest_2026-09-02.csv` | `522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883` | 8850 | untracked | false |
| B | qualification harness actually executed (custody-imported byte-identically this task from its execution location `C:/Users/Neo/AppData/Local/Temp/f3_spline_qual.py`; source SHA256 = destination SHA256) | `p_konum_plus/calibration/f3_spline_solver_qualification_harness_2026-09-02.py` | `ecda07d0fee36d8988c82c31aeb8e231b812e7a4df400af9c6a80676e4cf5917` | 12876 | untracked | false (content); new repo path created this task as custody import |
| C | case-level results (per-case table: RSS_ref, abs_err, err/tol ratio, max violation, endpoint source, A/B passes, reference certification actN/rank/KKT residual; plus aggregate flags) — recorded verbatim inside §1 of the r1 end-of-task record | `p_konum_plus/provenance/f3_step1_r1_corrected_ratification_candidate_2026-09-02.md` | `6e7b56348f9a1ffe144d776b48bc559baf2cbf71fb02c84ff37cba11203992c6` | — | untracked | false |
| D | qualification report / provenance record (same artifact as C; no separate report exists) | same as C | same as C | — | untracked | false |
| E | manifest-before-execution ordering evidence: (i) harness control flow — phase 1 writes and SHA256-hashes the manifest and prints the hash before any solve in phase 2 (statically verifiable from artifact B); (ii) recorded stdout inside artifact C showing `MANIFEST_WRITTEN_BEFORE_EXECUTION = true` and the manifest hash printed above the case table | artifacts B and C | as above | — | untracked | false |

## Custody notes

1. **Manifest custody:** actual SHA256 equals the value claimed in the r1
   candidate (`522d3508…`) — verified this task; byte-unchanged.
2. **Harness custody:** the executed script resided at
   `C:/Users/Neo/AppData/Local/Temp/f3_spline_qual.py`. It was copied
   byte-identically into the repository this task solely to make the audit
   bundle repository-resident (hash equality verified pre- and post-copy:
   `ecda07d0…`). Its content was not modified; no rerun occurred.
3. **Case-level telemetry:** no standalone machine-readable case-level
   telemetry file was produced by the original run; the per-case results
   exist as the hash-anchored table inside artifact C. Nothing was
   regenerated (a regeneration would require the forbidden rerun).
4. **Manifest-before-execution classification (base §5.3):**
   `SUPPORTED_BUT_NOT_INDEPENDENTLY_PROVABLE_FROM_REPO_ARTIFACTS` — the
   harness's deterministic control flow and the recorded stdout support the
   ordering; repository artifacts alone cannot independently prove the
   historical temporal ordering of the actual run.
5. **Claim boundary (base §5.4):**
   `spline_solver_qualification_claim = REPORTED_PASS`;
   `external_independent_acceptance = PENDING`. This inventory is custody
   exposure, not an independent acceptance audit.
6. `QUALIFICATION_AUDIT_INPUT_READY = true` — the auditor's minimum bundle
   (manifest CSV, executed harness/code, case-level result record) is fully
   identified and hash-anchored above; item 3 discloses the form of the
   case-level evidence.
```
