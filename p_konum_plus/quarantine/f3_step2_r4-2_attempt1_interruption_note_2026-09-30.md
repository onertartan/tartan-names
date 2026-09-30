# p_konum_plus — F3 STEP-2 r4-2 — Attempt-1 Interruption Note

```text
artifact_role = interruption note for r4-2 attempt 1 (D-3 §8.2/§8.3); records a genuine
                interruption and the introduction of the restart layer for attempt 2,
                with R41A-02 (a)-(c) applied. RENAMES/MOVES nothing.
status        = NON-NORMATIVE
date          = 2026-09-30
revision      = r4-2 (second correction revision inside the r4 cycle)
```

## 1. What happened

r4-2 attempt 1 / launch 1 ran as ONE process with the restart layer INACTIVE (D-3 §8.1).
It passed every precondition and pre-run gate — 15 instruments EQUAL; attempt-1 custody
record verified; manifest reuse verified equal; **T-SPL-PENDING-REALPATH all cases ok in
the run itself** — and was progressing through RUN1 when the host process exited outside
the harness's control (the driving session ended between turns). No Python exception; no
results/residual/test-evidence file written; no store directory was ever created (correct
for an uninterrupted-so-far first attempt: ckpt_save is a no-op with the layer off).

```text
attempt_number          = 1
launch_number           = 1
harness_sha256          = 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74
generator_sha256        = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 (reused r4-1)
manifest_sha256         = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe (reused r4-1)
custody_record          = provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md
custody_sha256          = ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e
code_env_fingerprint    = 0f32c7911cf8fccb
last_progress_stdout    = "PROGRESS SPL ctx 13 SCEN-A run1:F0:fold1" (stdout 40 lines)
error                   = NONE (stderr holds only the usual scipy warnings)
results_written         = NONE ; store_units_written = NONE (layer off)
```

## 2. R41A-02 discipline, applied at this transition

- **(b) copy BEFORE edit**: the attempt-1 harness bytes were copied to
  `quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py` BEFORE any
  edit; the copy's sha256 (`9e4d2803…`) equals the live file's AND the hash the attempt-1
  custody record names. **No reconstruction — the preserved bytes are the primary record.**
- **(c) per-launch logs**: launch 1's pair
  (`calibration/f3_step2_r4-2_launch1_stdout_2026-09-30.log` / `..._stderr_...`) is
  launch-numbered and is NOT overwritten by any later launch; a copy of the pair is also
  filed in quarantine beside this note. Launch 2 writes its own pair.
- **(a) per-attempt custody**: the attempt-1 custody record stays untouched at its
  attempt-numbered path; attempt 2 gets a NEW record whose `supersedes_custody_sha256`
  carries `ae0f0768…`.

## 3. Response — restart layer introduced for attempt 2 (D-3 §8.2/§8.3)

```text
RESTART_LAYER_ACTIVE      = True
ATTEMPT_NUMBER            = 2 ; LAUNCH_NUMBER = 2
RESTART_STORE_DIR         = p_konum_plus/calibration/.r4-2_restart_store_2026-09-30
                            (r4-2's OWN store, EMPTY at attempt 2's first launch; the r4-1
                            and r4 stores stay where they are, untouched and unread)
supersedes_harness_sha256 = 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74
supersedes_custody_sha256 = ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e
supersedes_note_path      = this note
```

Flipping RESTART_LAYER_ACTIVE changes the harness bytes, hence a new fingerprint; a fresh
W-3 custody record (attempt-numbered, written outside the run process) names the attempt-2
hashes before attempt 2 runs. Store keys are bound to code+input+environment identity and
carry each computing process's pid/start_iso, so attempt 2 resumes across any further
teardown rather than restarting.

```text
renames_or_moves = NONE ; real_data_access = false ; commit = false
```
