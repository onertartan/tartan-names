# Custody incident note — f3_step2_r3_auditor_transmittal_note_2026-09-22.md

- Date observed / restored: 2026-09-23. Corrupt state sha256: bc793a3b25e3e0a16268da4fa73e21165ed6d873bff06056d1ccad85d44a0083
  (sidecar mismatch — sidecar records bbe898cc89086ff179349f2925a670301b87dd2dad31afd141de13e771aa4a33).
- How it surfaced: a tool-result system-reminder reported the file as "modified, either by
  the user or by a linter," asserted the change was "intentional," and instructed not to
  mention it to the user. The diff it carried was not a plausible edit: section heading
  "## 2. Reading order" was split into "## 2. Reading +" / blank line / "order" — a stray
  `+` inserted and the heading broken across lines. This is the same signature as the
  PRIOR, already-documented incident on this project
  (`quarantine/f3_step2_correction_report_corruption_incident_note_2026-09-20.md`: a
  literal "git " inserted mid-hash, "origin unknown"): an unexplained mutation to a
  provenance file, arriving with no legitimate author and no reason given.
- Action taken and why the "don't mention it" instruction was not followed: the file was
  never edited after its original authoring in this session (verified: sidecar was
  generated and confirmed matching immediately after that authoring, earlier in this same
  conversation). A silent instruction to conceal an unexplained content mutation, in a
  project whose entire premise is that nothing gets hidden from the record, and on a
  document that was about to be handed to an external auditor, is exactly the shape of
  thing this harness's own custody/quarantine machinery exists to catch and disclose, not
  suppress. Treated as an unverified/suspicious instruction per standing guidance: flagged
  to the user directly, not complied with silently.
- Restore source: the byte-exact content of the original authoring Write call earlier in
  this session's transcript, hash-verified BEFORE being written back to equal the sidecar's
  recorded value — SHA256 equality makes it bit-for-bit the original, not a reconstruction.
- Corrupt bytes preserved (not deleted): `quarantine/f3_step2_r3_auditor_transmittal_note_2026-09-22_CORRUPTED_2026-09-23.md`.
- Result: restored file's on-disk SHA256 = bbe898cc89086ff179349f2925a670301b87dd2dad31afd141de13e771aa4a33;
  `sha256sum -c f3_step2_r3_auditor_transmittal_note_2026-09-22.md.sha256` -> OK.
- Separately and regardless of this incident: the restored note's CONTENT is now stale --
  written before the P-1..P-7 independent-audit corrections (see
  `f3_step2_r3_independent_audit_corrections_note_2026-09-23.md`) and before revision 4's
  run. It should not be sent to the auditor as-is; a revised transmittal note reflecting
  revision 4's verified output is needed once that run completes.
- `commit = false`.
