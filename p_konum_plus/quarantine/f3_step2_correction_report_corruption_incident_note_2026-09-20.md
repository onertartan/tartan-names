# Custody incident note — f3_step2_correction_report_r2_2026-09-07.md

- Date observed / restored: 2026-09-20. Corrupt state SHA256: 6b8cf801c66e15356dd4fa138b3f2bbc7e26c4b2a02d61599349d32dd487d94d (sidecar mismatch).
- Diff vs original: a single insertion of the literal text "git " inside the NR-01(i) canonical hash in section 5 ("6f197b74e3d4224git 8393e..."), origin unknown (post-sidecar edit outside the executor's run).
- Action: corrupt file MOVED (not deleted) to p_konum_plus/quarantine/ under its unchanged name; no other file touched.
- Restore source: the byte-exact Write payload of the original authoring step in the session transcript (b800288b-637c-4206-9aff-fe894d0b09e7.jsonl), hash-verified BEFORE placement to equal the expected af5b9151ebe4fc66e897899c1bc977f3cf7b3c0222da04601610affbb02c851b — SHA256 equality makes it bit-for-bit the original, not a reconstruction; no manual editing performed.
- Result: restored file's on-disk SHA256 = af5b9151... ; the pre-existing, unmodified sidecar now verifies OK; sha256sum -c passes for all ten r2 deliverables. commit = false.
