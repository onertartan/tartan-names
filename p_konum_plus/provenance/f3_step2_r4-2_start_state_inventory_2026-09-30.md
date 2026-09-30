# p_konum_plus — F3 STEP-2 r4-2 — Start-State Inventory (deliverable 11)

```text
artifact_role = start-state inventory for the r4-2 correction revision (D-3 §9 item 11;
                r4-2 instruction §5 item 11); taken BEFORE the first r4-2 write
status        = NON-NORMATIVE
date          = 2026-09-30
scope         = the state the r4-2 revision opens from: the audited r4-1 package and the r4
                package (both read-only under non-retroactivity), every r3 file and every
                quarantined file
```

## 1. Instruments verified before this inventory (r4-2 instruction §1)

Every value OBSERVED (sha256sum on the delivered files, 2026-09-30); all EQUAL to their
sidecar and to the hash the naming instrument prints. The cross-pins hold: D-7 §1 names the
instruction at `d6680338…` and the instruction's own sidecar agrees; the instruction and D-7
both name A-4 at `ad222936…`; D-7's own hash stands only in its sidecar (no self-hash).

| instrument | sha256 | source of the pin |
|---|---|---|
| r4-2 instruction | d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe | D-7 §1 + sidecar |
| D-7 (r4-2 dispatch record) | a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb | its sidecar |
| A-4 (r4-1 audit DRAFT r1; input, not directive) | ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82 | instruction + D-7 §1 + sidecar |
| r4-1 instruction (standing) | 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330 | instruction + D-7 §1 |
| r4 instruction (standing) | e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 | instruction + D-7 §1 |
| D-3 (standing) | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 | instruction + D-7 §1 |
| D-1 v6 (standing) | 17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376 | instruction + D-7 §1 |
| D-2 content (standing) | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 | instruction + D-7 §1 |
| D-5 (S-R2-1 source) | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 | instruction + D-7 §1 |
| D-6 (parent of D-7) | a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0 | instruction + D-7 §1 |

No mismatch, blank or template residue was found, so §1's STOP condition did not arise.

## 2. The r4-1 package (read-only; non-retroactivity check PASS)

Every file at the hash the r4-2 instruction's non-retroactivity block prints
(OBSERVED 2026-09-30, all EQUAL):

| # | file (p_konum_plus/) | sha256 |
|---|---|---|
| 1 | calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py | 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f |
| 2 | calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 |
| 3 | calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe |
| 4 | provenance/f3_step2_r4-1_preexecution_custody_2026-09-29.md | 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d |
| 6 | calibration/f3_step2_results_r4-1_2026-09-29.json | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 |
| 8 | calibration/f3_step2_test_evidence_r4-1_2026-09-29.json | f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd |
| 9 | calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md | 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 |
| 10 | provenance/f3_step2_correction_report_r4-1_2026-09-29.md | e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e |
| 11 | provenance/f3_step2_r4-1_start_state_inventory_2026-09-29.md | fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 |
| 12 | provenance/f3_step2_r4-1_attempt_log_2026-09-29.md | ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 |
| F | provenance/f3_step2_r4-1_transmission_list_2026-09-29.md | 31b27c28383cd4ffb6e3f10b32c8502adf5eda2dc517854074a9f071911949e1 |
| F-2 | provenance/f3_step2_r4-1_transmission_supplement_2026-09-30.md | 0b3f4358c1eac53d8652cbc6de95d50f6640913308ada6213372934c8265ba06 |

The r4 package was re-checked at the same time (harness `54274b4e…`, results `a15b7eff…`):
EQUAL. r4-2 overwrites, renames or moves none of these; every r4-2 deliverable is a new file
with the r4-2 tag, **except the generator and the manifest, which are REUSED unchanged**
(instruction §5 items 2 and 3): the r4-1 generator `68d126cf…` is named by path and hash in
every r4-2 custody record and is not copied; the manifest `5c09c4f0…` is regenerated in
memory by the run and verified equal to the delivered r4-1 file.

## 3. What this revision opens from — the r4-1 end state

The audited r4-1 run (results `6dd4185b…`) ended PARTIAL_PENDING_PI with
`corrections_complete = true`, `open_findings = []`, `deferred_decisions = []`,
`narrowed_evidence = ["T-R2-2"]`, `uncovered_coverage_rows = ["A.5 (iii) inadmissible refit"]`,
`determinism = true` (RUN1 == RUN2 = `556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77`),
expectation checks 36/36, 28/28 tests passed. A-4 confirmed the decision layer reproduces
35/35 evaluation objects byte for byte on an independent environment and opened six cleanup
findings, of which D-7 §3 puts R41A-01 … R41A-06 in scope and leaves R41A-08 out.

Because R41A-01 changes only which events set a pending flag on the REAL path, and no
REAL_SCENARIOS entry carries an UNRELATED injection (A-4 §5.2), the r4-2 run is expected to
reproduce the r4-1 evaluations and stops exactly — the RUN1 canonical document
`556106e7…` and the residual series `3ee624f3…` are expected unchanged. That expectation is
tested, not assumed: T-NONREG-R4-1 compares all 37 evaluation objects and every stop record
with no whitelist (instruction §3 R41A-01 (d)).

## 4. Carried-forward custody defects this revision repairs (A-4 R41A-02)

The three r4-1 custody defects the executor disclosed in the r4-1 supplement
(`0b3f4358…`) are repaired here by construction, from the first write:
per-attempt custody file names with `SUPERSEDES_CUSTODY_SHA256` filled; the harness copied to
quarantine BEFORE any superseding edit (so no reconstruction is needed or accepted); one
launch-numbered stdout/stderr pair per launch, never overwritten. Nothing about the r4-1
records is rewritten — they stay as delivered, with their disclosure intact.

## 5. Quarantined files carried forward (read-only)

Every quarantine artifact of the r2, r3, r4 and r4-1 revisions remains in
`p_konum_plus/quarantine/` unchanged, including the r4-1 attempt-1/attempt-2 harness
snapshots, the attempt-1/attempt-2 log pairs, the three r4-1 notes, and the r3, r4 and r4-1
attempt-2 restart stores. r4-2 adds its own quarantine copies and notes if it supersedes any
attempt of its own; it renames and moves nothing. The r4-1 and r4 store directories stay
where they are (instruction §4, settling A-4 R41A-07 in favour of §7).

`real_data_access = false ; commit = false`
