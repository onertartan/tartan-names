# p_konum_plus — F3 STEP-2 r4-1 — Attempt-1 Interruption Note

```text
artifact_role = interruption note for r4-1 attempt 1 (D-3 S8.2/S8.3). Records a
                genuine interruption of the run process and the introduction of
                the restart layer for attempt 2. RENAMES/MOVES nothing.
status        = NON-NORMATIVE
date          = 2026-09-29
revision      = r4-1 (correction revision inside the r4 cycle)
```

## 1. What happened

r4-1 attempt 1 ran as ONE process with the restart layer INACTIVE
(RESTART_LAYER_ACTIVE = False), per the run rules for a revision's first
attempt. It passed every precondition and pre-run gate and was progressing
through the RUN1 spline contexts when the host process exited **outside the
harness's control** (the driving session ended between turns). No Python
exception was raised; no results/residual/test-evidence file was written.

```text
attempt_number          = 1
harness_sha256          = b22708d2fd7e1a68c5c471285d58d5398992bcde36690e5b04dc94321f6d9841
                          (the RESTART_LAYER_ACTIVE = False bytes)
generator_sha256        = 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830
manifest_sha256         = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
code_env_fingerprint    = 4c776ba53e4fbe9c
pid                     = 19528
start_iso               = 2026-09-29T20:24:03.603424
interpreter             = C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe
last_progress_stdout    = "PROGRESS SPL ctx 41 SCEN-B run1:M0:probeL"
error                   = NONE (no traceback; stderr holds only the usual scipy
                          delta_grad==0.0 / invalid-value-in-power UserWarnings)
results_written         = NONE
```

Gates confirmed PASS before the interruption (from the attempt-1 stdout, now
quarantined): PIN-F2/PIN-SPLINE import hashes; PIN-SPLINE-LOADER prelude (21
nodes); W-3 custody verified; DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS (9
instruments — D-3, r4 instruction, D-5, A-1, D-2, r4-1 instruction, D-6, A-2,
A-3); NR-01(i)/(ii), NR-SPL, T-LOADER-NODES, T_MASK_FULL_EXT; unit-test
contexts (FIX-A5-TRUE, INJ-EXC-*) and RUN1 SCEN-B contexts up to ctx 41.

## 2. Quarantined artifacts (this note's siblings)

| file | what it is |
|---|---|
| f3_step2_r4-1_attempt1_stdout_2026-09-29.log | attempt-1 stdout at the interruption point (67 lines) |
| f3_step2_r4-1_attempt1_stderr_2026-09-29.log | attempt-1 stderr (1370 lines; scipy warnings only) |

These are COPIES; the live run logs under `calibration/` are overwritten by the
resumed run and the FINAL logs are the delivered ones.

## 3. Response — restart layer introduced for attempt 2 (D-3 S8.2/S8.3)

Per the run rules, a restart layer is introduced only after a recorded
interruption. This note is that record. For attempt 2 the harness is set to:

```text
RESTART_LAYER_ACTIVE    = True
ATTEMPT_NUMBER          = 2
RESTART_STORE_DIR       = p_konum_plus/calibration/.r4-1_restart_store_2026-09-29
                          (r4-1's OWN store, EMPTY at attempt 2's first launch;
                          the r4 store is left in place, untouched)
supersedes_note_path    = p_konum_plus/quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md
supersedes_harness_sha256 = b22708d2fd7e1a68c5c471285d58d5398992bcde36690e5b04dc94321f6d9841
```

Flipping RESTART_LAYER_ACTIVE changes the harness bytes, hence a NEW
code_env_fingerprint; a fresh W-3 custody record is written (outside the run
process) before attempt 2 and names the attempt-2 harness/generator/manifest
hashes. Store keys are bound to code+input+environment identity and carry each
computing process's pid/start_iso, so units from attempt 2 remain valid across
any further teardown and the run resumes rather than restarting.

```text
renames_or_moves = NONE
real_data_access = false
commit = false
```
