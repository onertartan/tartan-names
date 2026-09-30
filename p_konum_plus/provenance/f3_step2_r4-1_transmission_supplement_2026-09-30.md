# p_konum_plus — F3 STEP-2 r4-1 — Transmission SUPPLEMENT (deliverable F-2)

```text
artifact_role = supplement to the r4-1 transmission list, covering four items requested by
                the PI on 2026-09-30 AFTER the main list was issued. It ADDS to, and does
                NOT replace or modify, the main list
                (provenance/f3_step2_r4-1_transmission_list_2026-09-29.md,
                sha256 31b27c28383cd4ffb6e3f10b32c8502adf5eda2dc517854074a9f071911949e1).
status        = NON-NORMATIVE
date          = 2026-09-30
delivered to  = the auditor folder, subdirectory "Ek"
preservation vocabulary = PRESERVED (the bytes exist and are delivered) /
                PRESERVED_BY_HASH_PROVEN_RECONSTRUCTION (the bytes were rebuilt and their
                sha256 equals the value recorded for them BEFORE the loss; the rebuild route
                is disclosed) / NOT_PRESERVED (the bytes do not exist anywhere and cannot be
                proven; nothing is reconstructed or claimed)
```

## Summary

| # | requested item | verdict | delivered file |
|---|---|---|---|
| 1 | attempt-3 launch-1 (pid 22616) stdout + stderr | **NOT_PRESERVED** | none (§1) |
| 2 | attempt-1 harness bytes (b22708d2…) | **PRESERVED_BY_HASH_PROVEN_RECONSTRUCTION** | f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py (§2) |
| 3 | attempt-1 and attempt-2 W-3 custody records | **NOT_PRESERVED** (both) | none (§3) |
| 4 | quarantined attempt-2 store: path, size, sha256 listing | **PRESERVED** | f3_step2_r4-1_attempt2_store_listing_2026-09-30.csv (§4) |

## 1. attempt-3 launch-1 (pid 22616) stdout and stderr — NOT_PRESERVED

**Cause.** Both r4-1 launches of attempt 3 were run with the SAME redirection targets
(`calibration/f3_step2_r4-1_run_stdout_2026-09-29.log` and `..._stderr_...log`) using `>`,
which truncates. When launch 1 (pid 22616, start 2026-09-29T22:14:16) was interrupted by a
host teardown and launch 2 (pid 7972) resumed from the store, launch 2 overwrote both files.
Launch 1's own console output was not copied anywhere first. The delivered logs therefore
contain launch 2 ONLY — the delivered stdout's single `PID = ` line reads 7972.

This is an executor process defect (the per-attempt copies were taken for attempts 1 and 2
before each rerun, but not for the intra-attempt resume). It is recorded here rather than
repaired; nothing is reconstructed.

**What DOES survive about pid 22616, in delivered, hashed files:**

| evidence | where | value |
|---|---|---|
| per-(phase, pid) optimizer-call split | delivered stdout `T_CALLCOUNT per phase/pid`, and results.process.spline_telemetry_calls_by_phase_pid | `nr_gates/22616 = 60`, `unit_tests/22616 = 1602`, `run1/22616 = 5256` |
| per-unit provenance | deliverable B, restart-store manifest (11,869 rows) | 7,271 rows carry `pid = 22616`, `start_iso = 2026-09-29T22:14:16.468915` |
| launch row (start, stop point, units) | deliverable 12, attempt log, Attempt-3 table row 3 | interrupted; NR gates + unit tests + RUN1 complete; 7,271 units persisted |
| per-call telemetry rows | deliverable A (12,174 rows) | the 6,918 rows tagged pid 22616 |

So launch 1's *console text* is lost; its *computational provenance* is intact and
independently checkable in four delivered artifacts. T-RESTART-PROVENANCE condition 3 rests
on those artifacts, not on the console log.

## 2. attempt-1 harness bytes (b22708d2…) — PRESERVED_BY_HASH_PROVEN_RECONSTRUCTION

Delivered: `f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py`
(also filed in `p_konum_plus/quarantine/`).

```text
sha256 of the delivered file = b22708d2fd7e1a68c5c471285d58d5398992bcde36690e5b04dc94321f6d9841
sha256 recorded for attempt 1 = b22708d2fd7e1a68c5c471285d58d5398992bcde36690e5b04dc94321f6d9841
values_equal = EQUAL (byte-exact)
```

**Why a reconstruction was needed.** The attempt-1 → attempt-2 and attempt-2 → attempt-3
transitions were made by editing the harness IN PLACE; no snapshot was taken before the
first edit. (The attempt-2 snapshot already in the main transmission set was recovered the
same way and is likewise byte-exact.)

**Reconstruction route (disclosed in full).** Starting from the delivered attempt-3 harness
(`4e0dc8cf…`), exactly two textual blocks were substituted back, both of which are the
complete, contiguous blocks that the two edits had replaced:
1. the R4A-01(f) non-regression comparison block → its pre-fix form (the attempt-1/attempt-2
   form: raw `!=` comparison, `json.dumps(..., default=str)` columns);
2. the attempt-metadata block → its attempt-1 form (`RESTART_LAYER_ACTIVE = False`,
   `SUPERSEDES_HARNESS_SHA256 = None`, `SUPERSEDES_CUSTODY_SHA256 = None`,
   `SUPERSEDES_NOTE_PATH = None`, `ATTEMPT_NUMBER = 1`, with its own comment block).
Each substitution target occurred exactly once in the source (asserted, not assumed). No
other byte was touched. The resulting sha256 equals the value recorded for attempt 1 before
the edits, which is what makes this a proof rather than a claim: a single wrong byte anywhere
would produce a different digest.

**Caveat (the same one the r4 cycle disclosed for its own reconstructed revision-1 bytes).**
The delivered bytes are a rebuild whose identity is established by digest equality, not a
file continuously held since the run. The digest it is checked against is itself an executor
record (§3 explains its provenance and its weaker chain relative to the attempt-2 digest).

## 3. attempt-1 and attempt-2 W-3 pre-execution custody records — NOT_PRESERVED

**Cause.** `CUSTODY_PATH` is a fixed constant
(`provenance/f3_step2_r4-1_preexecution_custody_2026-09-29.md`). The external W-3 writer was
re-run before each attempt and **overwrote the same file** each time. The surviving file is
attempt 3's:

```text
attempt_number       = 3 (r4-1 revision, third attempt; restart layer active)
harness_sha256       = 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f
code_env_fingerprint = dc228827920a9633
sha256 of the file   = 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d
```

Nothing is reconstructed here, and deliberately so: unlike the harness bytes, **no sha256 was
ever recorded for the attempt-1 or attempt-2 custody records**, so a rebuilt document could
not be proven to be the document that was verified at run time. A plausible-looking rebuild
without a digest to check it against would be a fabrication, not a recovery. (This is also
the direct cause of `supersedes_custody_sha256 = None` in the attempt-3 harness and custody
record — a field the r4 cycle was able to fill and this revision was not.)

**Requested explanation — against which hash was the attempt-2 copy verified?**

The attempt-2 *harness* snapshot in the main transmission set was verified against
`280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2` — **not** against any
custody file (none survived). That digest's chain of custody in delivered, hashed artifacts:

| where the digest is attested | artifact | status |
|---|---|---|
| `process.supersedes_harness_sha256` | deliverable 6, results_r4-1 json (6dd4185b…) | machine-written by the attempt-3 run |
| `SUPERSEDES_HARNESS_SHA256` constant | deliverable 1, attempt-3 harness (4e0dc8cf…) | source constant, hashed |
| `supersedes_harness_sha256` line | deliverable 4, attempt-3 W-3 custody (3bc4e578…) | written externally before attempt 3 |
| narrative statements | deliverables 10, 12, the attempt-2 quarantine note | executor-written |

Its ORIGIN is the external W-3 writer, which computed it on the live attempt-2 bytes when it
wrote the (now overwritten) attempt-2 custody record; the attempt-2 run then verified that
record against the live bytes and printed `PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = true`
(delivered attempt-2 stdout, line 9 — the line confirms equality but does not print the
digest). The digest was then carried forward into the attempt-3 constants and machine-written
into the results.

**Asymmetry the auditor should note.** The attempt-1 digest `b22708d2…` has a WEAKER chain
than `280869892d…`: it appears only in executor-written narrative files (the attempt log and
the attempt-1 interruption note, both delivered with sidecars) — it is in no
machine-written results field, because attempt 3 supersedes attempt 2, not attempt 1. Both
§2's reconstruction proof and the attempt-1 launch row therefore rest, at their root, on
executor records made at the time rather than on an independently machine-written value.

## 4. Quarantined attempt-2 restart store — path / size / sha256 listing

Delivered: `f3_step2_r4-1_attempt2_store_listing_2026-09-30.csv`
(also filed in `p_konum_plus/quarantine/`; columns `path`, `size_bytes`, `sha256`).

```text
store          = p_konum_plus/quarantine/r4-1_restart_store_2026-09-29_ATTEMPT2_NONREG_CANON_BUG
units listed   = 11,869 (every file in the directory; none omitted)
distinct sha256 = 11,869 (no duplicate unit bytes)
total size     = 11,310,695 bytes
key fingerprint prefix of every unit = b6fc376b049c20e1 (the attempt-2 code+env fingerprint)
listing sha256 = 8dfbe9e6fdd52666412b5627fd97c13633783dceac59e039b885c8bc6f008fcd
```

The listing carries no `pid` / `start_iso` columns: for the attempt-2 store those values exist
only inside the pickled payloads, and this revision's machine-written store manifest
(deliverable B) covers the attempt-3 FINAL store, not this quarantined one. The attempt-2
store was never read by the attempt-3 run — its units are keyed under `b6fc376b…` while
attempt 3 computed and read under `dc228827…`, so a cross-attempt read is impossible by
construction (T-RESTART-PROVENANCE condition 1).

Per the PI's instruction, no additional artifact is provided for the r4 store.

```text
main transmission list = UNCHANGED (31b27c28…)
renames_or_moves of any r3 / r4 / pre-existing quarantine file = NONE
real_data_access = false ; commit = false
```
