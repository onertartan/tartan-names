# p_konum_plus — F3 STEP-2 — r4-1 Quarantine Label Annotation Note (R4A-10(ii))

```text
artifact_role = annotation note: reconciles the QUARANTINE LABELS of the r3
                superseded harness/generator files against the harness/generator
                bytes NAMED by the r3 custody records. It RENAMES NOTHING and
                MOVES NOTHING (D-6 §3 drafter choice (3); user constraint: no r3,
                r4 or quarantine file is modified, renamed or moved). It only
                records, in one place, which quarantine-filed bytes do and do not
                match the bytes their label implies.
status        = NON-NORMATIVE
date          = 2026-09-29
revision      = r4-1 (correction revision inside the r4 cycle)
authority     = A-2/A-3 R4A-10, as scoped by D-6 §3; cross-referenced by the
                r4-1 attempt log ERRATUM-2 and the r4-1 start-state inventory §3/§4
```

## 1. Method

`sha256sum` was run on 2026-09-29 on each file that carries an r3 supersession
label in `p_konum_plus/quarantine/`. The "named" column is the harness /
generator / manifest sha256 that the corresponding r3 custody record records
(see the r4-1 start-state inventory §3, whose five `code_env_fingerprint`
values all recompute exactly from the named triples). "match" compares the
bytes actually filed under the label against the bytes the label's own attempt
custody record names.

## 2. r3 harness files under quarantine labels

| quarantine file (label) | bytes OBSERVED under the label | bytes NAMED by that attempt's custody | match |
|---|---|---|---|
| f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py | 6ddcc26d… | 6ddcc26d… (ATTEMPT1) | **yes** |
| f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py | 891574fc… | 891574fc… (ATTEMPT2-3) | **yes** |
| f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py | **f882b922…** | **d67e097d… (ATTEMPT5)** | **NO** |
| f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py | **99f895c1…** | **390f42b7… (ATTEMPT8)** | **NO** |

## 3. r3 generator / manifest files under quarantine labels

| quarantine file (label) | bytes OBSERVED under the label | bytes NAMED by the custody records | match |
|---|---|---|---|
| f3_step2_fixture_generator_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py | **cc23c9b5…** | **e35c2bf0…** (generator named by ATTEMPT1/2-3/5) | **NO** |
| f3_step2_fixture_manifest_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.csv | 4544ff75… | 4544ff75… (manifest named by ATTEMPT1/2-3/5) | **yes** |

The quarantined generator `cc23c9b5…` is the r3 FINAL / ATTEMPT8 generator (the
r3 final and ATTEMPT8 custody records both name `cc23c9b5…`), filed under an
ATTEMPT5 label. The generator `e35c2bf0…` that the ATTEMPT1/2-3/5 custody
records name for attempts 1–5 is not present under any quarantine label.

## 4. Consequence (three named-but-unfiled r3 bytes)

Three harness/generator byte-strings named by r3 custody records are **NOT
PRESERVED** anywhere in the repository or quarantine (searched 2026-09-29;
the two restart-store directories excluded — they hold pickled units, not
harness/generator source):

| hash | what the custody record calls it | result |
|---|---|---|
| d67e097dc158c4909276b026ce66533f33dfab7a94d800e57342eb86e76f58ff | r3 ATTEMPT5 harness | **NOT_PRESERVED** |
| e35c2bf06ee4087bac97bd5b6e81d35d079ff1dddf8d2e68555c6c7d18859638 | r3 attempts-1–5 generator | **NOT_PRESERVED** |
| 390f42b72971030033c6964731d699358a1547bf9093b8e949c0e338e6bc0336 | r3 ATTEMPT8 harness | **NOT_PRESERVED** |

## 5. Scope of impact — none on any delivered output

This is a labelling / disclosure defect only. It touches no delivered result:
the r3 FINAL run executed under harness `5fea165c…` / generator `cc23c9b5…`
(fingerprint `1ba561da…`) and the r4 run under harness `5ef61a41…`; no unit
under the r3 store's foreign prefix `548ae790…` (the recomputed fingerprint of
the ATTEMPT8 custody triple, harness `390f42b7…`) was ever readable by either
run. The foreign entries are listed, unchanged, in
`r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv`.

## 6. Correction carried into the r4-1 report

The r4 report §8(c) statement that `d67e097d…` is "present in quarantine" is
**incorrect** and is corrected in the r4-1 correction report: the bytes filed
under the ATTEMPT5 harness label are `f882b922…`, and `d67e097d…` is not
present. This note and the r4-1 attempt log ERRATUM-2 are the record of that
correction; the r4 report itself is historical and is not edited.

```text
renames_or_moves = NONE
real_data_access = false
commit = false
```
