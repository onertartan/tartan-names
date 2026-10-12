# rp1-r2 independent auditor rerun procedure

Use a disposable copy of this committed package, with the unchanged delivered harness and dependencies. This is a procedure, not an executor self-audit. Match the binding environment recorded in results and W-3.

Move the copy's attempt-2/launch-1 W-3 file and its sidecar, launch/controller start/end/pid/writer records, and attempt-2 stdout/stderr logs to a kept-aside directory. Preserve the originals. The writer refuses an existing custody file and the launcher refuses existing records. The copy's `.rp1-r2_attempt2_restart_store_2026-10-10` starts empty and is never the executor store.

Set F3_REPO_ROOT to the disposable copy, F3_RP1R2_LAUNCH to the actual launch number (1 for the first launch), and OMP_NUM_THREADS/OPENBLAS_NUM_THREADS/MKL_NUM_THREADS to 1. Run the delivered launcher with Python 3.11.7. It writes its own W-3 before the harness. Keep every launch pair and log every invocation under section 5(b). Outputs remain in the copy. Do not edit D-14 or bypass its fixed hash.

Compare environment, mandatory tests, S scientific objects, RUN1/RUN2 canonical hashes, complete leaf-level non-regression CSV, positive/negative Q cases, Q10 family/mode accounting, and every delivery checksum. Any S difference is a failure regardless of environment; an environment difference does not establish its cause. No real F1/SSA files or eligible/hash tables are read. Only the independent auditor or a named PI decision may close findings.
