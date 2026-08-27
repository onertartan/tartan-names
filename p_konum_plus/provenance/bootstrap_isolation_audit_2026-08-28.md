# p_konum_plus — Bootstrap / Isolation Execution Audit

- **Audit type:** NO-SCIENTIFIC-RUN bootstrap/isolation execution audit
- **Date:** 2026-08-28
- **Worktree:** `G:/PycharmProjects/pkp-worktree`
- **Branch:** `p_konum_plus`
- **Base HEAD:** `96412eee9d16dd426d4dc99fde0c05c40c576220`
- **Normative source:** `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md`
- **Scope:** read-only audit — no writes, no commits, no calibration, no scientific runs performed during the audit itself.

---

## 1. Bootstrap identity audit — PASS

- **Repository root:** `G:/PycharmProjects/pkp-worktree` — matches expected.
- **Branch:** `p_konum_plus` — matches expected.
- **HEAD:** `96412eee9d16dd426d4dc99fde0c05c40c576220` ("extension_decision_freeze_v0: FROZEN") — matches expected base.
- **Worktree layout:** `git worktree list` shows the legacy worktree `G:/PycharmProjects/tartan-names` on `main` and this worktree on `p_konum_plus`, both at `96412ee`. The legacy worktree was not entered or modified.
- **git status:** exactly one entry — staged new file `p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md` (status `A `, meaning the staged content equals the on-disk content). Zero modified paths, zero untracked paths (checked with `-uall`); `.idea/` exists but is gitignored.
- **Observation, not a failure:** the normative source is staged but not yet committed, so its content is currently pinned only by this audit's hash check, not by git history. The empty new directories do not appear in `git status` simply because git does not track empty directories — they are not ignored.

## 2. Normative-source hash audit — PASS

The file exists and its SHA256 is exactly
`d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` — a byte-exact match to the expected pin. It is treated as the sole normative methodology source for `p_konum_plus`.

## 3. Namespace-isolation audit — PASS

All six expected new-project namespaces exist: `p_konum_plus/protocol/` (one file — the v11 document), and `p_konum_plus/src/`, `p_konum_plus/calibration/`, `p_konum_plus/manifests/`, `p_konum_plus/provenance/`, `results/p_konum_plus/` — all empty. The literal paths `protocol_v5_3/`, `protocol_v5_3_analysis/`, `results/protocol_v5_3/`, `results/protocol_v5_3_analysis/`, and `faz1_*` do not exist in this worktree; the legacy material actually lives under `protocol/` (e.g. `01_kosum_protokolu_v5_3.md`, the S01–S07 deviation annex, the hash table, `run_matrix_v4.csv`) and `results/{experiment,turkiye,usa}/` — enumerated by name only. The new namespaces are fully disjoint from every legacy path, no new-project path writes into any of them, and `git status` confirms no legacy path was renamed, moved, copied, cleaned, or rewritten.

## 4. Implicit-dependency / contamination audit — PASS

The new-project namespace contains exactly one artifact — the v11 protocol document. There is no code, configuration, manifest, or notebook, hence no import or runtime dependency on anything. Specifically: `run_driver.py` exists only in legacy `modules/experimental/`; no `faz1*` file exists anywhere in this worktree; and a case-insensitive scan for `run_driver|faz1|protocol_v5_3|S-06|winner|robustness|deployment` across `p_konum_plus/` yields 38 hits, all inside the v11 document itself. On inspection these are governance and firewall clauses — `winner_privilege = false`, `winner_eligible = false`, the prohibition list (e.g. "treat old Ward+CH as new scientific prior/winner" listed as forbidden), the F-gate table, and the §29 terminal statement declaring `n_per_cluster` "not inherited from the historical C block". They prohibit legacy inheritance rather than depend on it. No legacy frozen result table, S-06 table, winner report, or calibration/deployment output is referenced as an input. No reuse-repinning decision has been made, consistent with *code reuse ≠ normative inheritance*.

## 5. Information-firewall status — INTACT

`calibration/`, `manifests/`, `provenance/`, and `results/p_konum_plus/` are all empty: no value for generator-family calibration, generator thresholds, `n_per_cluster`, `Q_CD`, `B*`, `H*`, geometry strata, `epsilon`/`delta`, `Delta_eq`, the precision target, scenario/seed allocation, or BANK-SENS implementation has been recorded anywhere in the new namespace. The v11 document leaves these as open pins bound to future gates (e.g. `n_per_cluster` at F5, BANK-SENS procedures at F11, `Delta_eq` fixed from scientific relevance before outcomes). Each can therefore still be determined independently of legacy performance outcomes. No value was selected in this task and no legacy winner, diagnostic, robustness, or deployment result was consulted — no FIREWALL VIOLATION observed or committed.

## 6. Outcome-firewall status — PASS

No legacy performance result file was opened or summarized; legacy result areas were touched only at the level of directory and file names for the isolation check. The current bootstrap state requires neither reading nor generating any algorithm × CVI performance outcome, consistent with the v11 contract's F12 gate ("No algorithm×CVI outcome may be read before F12"). The project is pre-F1; nothing outcome-bearing has been produced or read.

## 7. Verdict — GO

All checks pass. The next permitted scientific-governance artifact is `yeni_proje_empirik_kalibrasyon_protokolu_v0.md`. It was **not** created in this task; no methodological decisions were made, no calibration pins filled, no legacy results reinterpreted. No writes, no commits, no calibration, no scientific runs were performed during the audit.
