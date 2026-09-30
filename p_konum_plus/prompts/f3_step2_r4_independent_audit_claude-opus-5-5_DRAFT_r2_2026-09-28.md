# p_konum_plus — F3 STEP-2 r4 — Independent Audit — DRAFT r2 (2026-09-28)

```text
record                  = f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md
record_class            = child revision of the r4 audit DRAFT r1 (b7217027…), which it does not rewrite. It adds
                          the verification of the transmission set the PI forwarded after DRAFT r1 (nine further
                          batches on 2026-09-28) and changes only what that verification changes (§1)
auditor                 = claude-opus-5-5 (Claude, Cowork session; the model the PI selected — the serving model may
                          differ). Not the executor. Decides nothing for the PI. Declares no QUALIFIED
reviewer_prior_exposure = as in DRAFT r1 (this session drafted D-3 and the r4 instruction, filled D-4 and D-5 at the
                          PI's written instructions, and wrote A-1 and DRAFT r1)
other auditors' records = none received; none used
executor                = Claude Code (harness 54274b4e… ; generator 39391730… ; manifest c0b38ceb…) — unchanged
parents                 = r4 audit DRAFT r1 b7217027… ; r3 audit A-1 11cfa591… ; transmission list 10635dae…
frozen upstream         = untouched: v11 ; F2 FINAL FREEZE r1 ; F3 STEP-1 (r4 as ratified by freeze record r1).
                          Nothing reopened; no scientific literal produced
evidence tiers          = [A] auditor-verified on the delivered bytes ; [A-S] auditor-environment execution of
                          delivered code ; [X] executor claim ; [E] external
honesty rule            = every hash here was computed by the auditor with the script of §8 or is quoted from a
                          named file; what could not be checked is NOT PERFORMED
sidecar                 = external .sha256 ; no self-hash
```

## 0. Verdict

```text
audit_verdict                 = NOT PASSED   (unchanged from DRAFT r1)
global blockers               = 0
gate-specific blockers        = 1   (R4A-01, unchanged — the transmission set does not touch it)
cleanup                       = 4   (R4A-02 … R4A-04 unchanged ; R4A-10 new)
informational                 = 4 open (R4A-06 … R4A-09) ; R4A-05 CLOSED
F3_STEP2_r4_status (executor) = PARTIAL_PENDING_PI — supported ; corrections_complete = true not supported (R4A-01)
F3_STEP2 = QUALIFIED          = NOT declared (PI only)
```

In plain words. The executor's transmission set is now complete for audit purposes. Of the 72 entries of the
transmission list, 71 arrived byte-identical to the listed hash. The one that did not arrive, the sidecar of the
r3 results file, is proven by reconstruction: the sidecar line built from the r3 results file the auditor audited
in A-1 hashes exactly to the listed value (§2). Every sidecar states the hash the auditor had already computed on
the file it names, for r4 and for r3, so the r3 parents stand unchanged (§3). The r4 revision chain is complete
and honest: each superseded harness is the byte string its custody record names, each recorded fingerprint
recomputes, and each code change between revisions is the one the note describes (§5.1).

One new defect is found, in the r3 history, not in r4. The r3 quarantine does not hold the bytes that ran under
two of its labels. The r3 store's foreign prefix 548ae790… — which A-1 could not identify and the r4 erratum calls
"matching no combination named in any r3 file" — is exactly the fingerprint of the triple the executor's own
attempt-8 custody record names (harness 390f42b7…). Those harness bytes were never preserved; the file filed
under the ATTEMPT8 label (99f895c1…) is different bytes, and the harness and generator filed under the ATTEMPT5
label are not the ones the attempt-5 custody record names (§5.2, R4A-10). This touches neither the final r3 output nor any r4
output; it is a labelling and disclosure defect and is classed as cleanup.

## 1. What this revision changes relative to DRAFT r1

| item | DRAFT r1 | DRAFT r2 |
|---|---|---|
| R4A-05 transmission | 14 of 72 received; sidecars, notes, superseded bytes NOT PERFORMED | CLOSED [A]: 71 of 72 received equal, 1 proven by reconstruction (§2) |
| C-29 parents unchanged | [X] — sidecars not received | PASS [A] for the 26 sidecars of the list (13 r4, 13 r3): each states the auditor's own hash of the file it names (§3). The executor's count "40/40 non-quarantine sidecars" covers files outside the list and stays [X] |
| T-R4-1 (transmission of the missing entries) | open | CLOSED |
| A-1 T-R3-2 (origin of the r3 store prefix 548ae790…) | not identified | identified [A] (§5.2) — and the identification contradicts the r4 erratum, item 3 (R4A-10) |
| R4A-10 | — | new, cleanup (§6) |
| every other section of DRAFT r1 (§2 – §9: which bytes ran, checklist, findings R4A-01 … R4A-09, repro, closure map, evidence) | — | stands unchanged; not restated |

## 2. Transmission custody [A]

Received on 2026-09-28 after DRAFT r1: nine batches (107 file instances over all ten batches including the first
delivery; 89 distinct name-and-content pairs; no name ever arrived with two different contents).

| group (transmission list) | listed | received with the listed hash |
|---|---|---|
| A — r4 deliverables and their 13 sidecars | 26 | 26 |
| B — r3 sidecars | 13 | 12 |
| C — five r3 quarantine notes | 5 | 5 |
| D — superseded r3 revisions and custody records | 8 | 8 |
| E — r4 supersession chain (notes, harnesses, custody records, stdout logs) | 18 | 18 |
| F — T-R3-2 foreign-entry listing and its sidecar | 2 | 2 |
| total | 72 | 71 |

The entry not received is `calibration/f3_step2_results_r3_2026-09-22.json.sha256` (listed 714b5072…). A sidecar
is fully determined by the file it names, so the auditor rebuilt it: the line `<hash>  <name>` with LF, built from
the r3 results file audited in A-1 (352791648b7c…), hashes to 714b5072589bec65f32f2a76f5b49130f4064b73bfd9ce5e9eb68df95570ed35,
the listed value; the CRLF form does not. So the listed sidecar states the audited r3 results hash [A by
reconstruction; the file itself not received].

Received but not on the list (§8 block [4]): the stderr logs of r4 attempts 1, 2, 4 and 6 (the attempt 3 and 5
stderr logs and the logs of the two final launches were not sent — none is required); the r3 ATTEMPT2-3 and
ATTEMPT5 output sets (results, telemetry, residual series, test evidence), each byte-equal to the hash the
executor's quarantine note gives for it; the ATTEMPT5-labelled generator and manifest (§5.2); the corrupted transmittal
note (bc793a3b…), which differs from the copy A-1 received (bbe898cc…) only by the split heading
"Reading order" the incident note describes; a 46-byte stray sidecar that names a file but carries no hash, as
its STRAY_MALFORMED label says; and the transmission list's own sidecar, which states 10635dae… (the list's hash;
it names the list, not itself).

## 3. Sidecars [A] (C-29)

All 26 listed sidecars are well formed (`<64 hex>  <name>` + LF, no CR, none names itself). The 13 r4 sidecars
state exactly the hashes of the delivered r4 files. The 13 r3 sidecars (12 received, 1 reconstructed) state
exactly the hashes A-1 recorded for the r3 files at reception on 2026-09-24 — harness 5fea165c…, generator
cc23c9b5…, manifest 9c944543…, custody a910e1b6…, telemetry 24f21811…, results 35279164…, residual 3ee624f3…,
test evidence b7d3b861…, report 80df7914…, start-state inventory 71a3f5a7…, attempt log 25316389…, per-call
telemetry 9d0c627e…, store manifest 933dcaee…. The r3 parents therefore stood unchanged when the executor wrote
these sidecars; that the repository still holds those bytes today is the executor's statement [X].

## 4. The r3 quarantine notes and output sets [A]

The five group-C notes arrived with the listed hashes. Their checkable statements hold on the bytes, except those
of §5.2:

| note | statement checked | result |
|---|---|---|
| r3 attempt-1 supersession | harness 6ddcc26d… and custody c8d47629… are the attempt-1 bytes | holds: custody names 6ddcc26d…, fingerprint 2cf50b2f18cfb34e recomputes |
| r3 exc-classification bug | ATTEMPT2-3 outputs: results 52e430aa…, telemetry 931a9640…, residual f28bd6a0…, test evidence 14edaaa5…; the natural capture was mis-classified | holds: all four hashes equal; the ATTEMPT2-3 test evidence records the natural capture as UNRELATED, the ATTEMPT5 one as COVERED |
| r3 independent-audit corrections (P-1 … P-7) | ATTEMPT5 outputs 06210546… / 858eaf3b… / f28bd6a0… / f7445935… | holds: all four equal; results carry manifest 4544ff75… and RUN1 = RUN2 = 943d14ab… (the r3 log's row 5); the residual file equals the ATTEMPT2-3 one, consistent with P-1 (residual export outside the injection map) |
| r3 attempt-8 telemetry replay | harness 99f895c1… and custody 2e55e150… are the attempt-8 bytes | does not hold — §5.2 |
| r3 transmittal corruption incident | corrupted copy bc793a3b… differs only by the split heading | holds |

## 5. Supersession chains

### 5.1 r4 [A] — consistent

| revision (attempts) | harness | custody (fingerprint recorded = recomputed) | in the r4 store | change to the next revision (non-comment lines) | run logs |
|---|---|---|---|---|---|
| 1 (1) | f137299c… | 307809c5… (e9d93b0e7e5a9834 = e9d93b0e7e5a9834) | 0 | the any_mode_unrelated fix (UNRELATED capture sets the flag; TEST_ONLY exclusion removed) + SUPERSEDES/ATTEMPT constants | stdout: EXIT_CODE=1; stderr: AssertionError at record_test("T-EXC-UNRELATED-TYPE" …) |
| 2 (2) | 20d830e0… | 856201af… (f03efb7069fa533e = f03efb7069fa533e) | 0 | RESTART_LAYER_ACTIVE False → True + constants | stderr without traceback — consistent with the external interruption the note describes |
| 3 (3–4) | 814e395a… | 51499dc4… (de4720325eb70003 = de4720325eb70003) | 0 | k05 counter reported per fixture + constants | attempt 4: RUN1 19454f65… ≠ RUN2 bfa626a6… → STOP on the canonical mismatch; both values equal the r4 attempt log |
| 4 (5–6) | 90ea0ff3… | cb2204b1… (6ec6fc2a42343433 = 6ec6fc2a42343433) | 0 | mutation saved and restored + constants | attempt 6: RUN1 777fca02… ≠ RUN2 148db2d1… → STOP on the canonical mismatch; both values equal the r4 attempt log |
| 5, delivered (7–8) | 54274b4e… | 0f1724ab… (5ef61a412c6bd76c = 5ef61a412c6bd76c) | 11,869 (all) | — | final launches: logs not transmitted |

The attempt-1 note says the revision-1 bytes were reconstructed afterwards, because the live file had been edited
before the quarantine copy was taken, and that "the equality is the proof, not the executor's word". The proof
holds: the reconstructed file hashes to f137299c…, the harness hash the attempt-1 custody record named before the
run, and the fingerprint of that triple recomputes to the recorded e9d93b0e7e5a9834. Attempt 6's RUN1 value is the
delivered RUN1 canonical hash 777fca02…, consistent with the attempt 5–6 note: RUN1 was already right and the
leaked mutation changed RUN2 only.

### 5.2 r3 [A] — two quarantine sets are not the bytes their labels name

| label | custody record names (H / G / M) | fingerprint (recorded = recomputed) | entries in the r3 final store | bytes filed under the label |
|---|---|---|---|---|
| r3 final | 5fea165c… / cc23c9b5… / 9c944543… | 1ba561daefb48b2e | 11,723 | harness 5fea165c… = named |
| ATTEMPT1 | 6ddcc26d… / e35c2bf0… / 4544ff75… | 2cf50b2f18cfb34e | 0 (earlier store quarantined whole) | harness 6ddcc26d… = named |
| ATTEMPT2-3 | 891574fc… / e35c2bf0… / 4544ff75… | d505bf76994abf60 | 0 (idem) | harness 891574fc… = named |
| ATTEMPT5 | d67e097d… / e35c2bf0… / 4544ff75… | 6f4e29ccc903bce6 | 0 (idem) | harness f882b922… ≠ named; generator cc23c9b5… ≠ named; manifest 4544ff75… = named |
| ATTEMPT8 | 390f42b7… / cc23c9b5… / 9c944543… | 548ae790f6ac756a | 11,723 | harness 99f895c1… ≠ named |

What the bytes show:

(a) The r3 store's second prefix is identified. 548ae790f6ac756a is the recorded and recomputed fingerprint of the
attempt-8 custody triple, harness 390f42b7…. The executor's foreign-entry listing equals, row for row (path,
size, sha256), the 11,723 rows of the r3 store manifest A-1 audited that carry this prefix. The r4 erratum,
item 3, says the prefix matched "no combination named in any r3 file" and attributes it to "intermediate
byte-states … whose exact bytes were not separately preserved". The first half is contradicted by the attempt-8
custody record, an r3 file; the second half is right for the harness — 390f42b7… is named by exactly one received
file, that custody record, and was not transmitted.

(b) The ATTEMPT8-labelled harness 99f895c1… is not what attempt 8 ran. No custody record names it as a harness.
With the attempt-8 generator and manifest it gives the fingerprint 327fcf82f949fc66, which no store entry carries. The r3
log's rows 9–10 name it too, and the r4 erratum, item 1, already corrects those rows to 5fea165c…. So 99f895c1… is
named in full by the r3 log, the attempt-8 note and the transmission list, and by no custody record or store
fingerprint.

(c) The ATTEMPT5-labelled set is mixed. The attempt-5 custody record names harness d67e097d… and generator
e35c2bf0…; the files filed under that label are the harness f882b922… (the r3 log's revision 4) and the generator cc23c9b5…,
which regenerates the final r3 manifest 9c944543…, not the attempt-5 manifest 4544ff75…. The attempt-5 outputs
themselves are genuine (§4). The attempt-5 harness and generator bytes were not transmitted. The r4 report §8 (c)
lists d67e097d… as present in quarantine; it is not on the transmission list [X].

(d) The r3 log says rows 6–8 ran revision 4 = f882b922…. The attempt-8 custody record, written for revision 4
(attempt_number = 4; it supersedes f882b922… and the attempt-5 custody e67bd9d7…), names 390f42b7… instead, and the
attempt-8 note says attempt 8 resumed from units attempt 6 had cached, which requires one fingerprint for both
launches. No store entry carries a fingerprint of f882b922… with any generator and manifest pair named in r3. The
auditor's reading — an inference, not a measured fact — is that attempts 6–8 ran 390f42b7… and that the
quarantine copies and the log's hash column were taken from files that had already been edited (the root cause
the r4 erratum, item 1, gives for the rows 9–10 error, and the ordering mistake the r4 attempt-1 note discloses
for its own revision 1).

None of this reaches a delivered output: the final r3 output ran under 1ba561daefb48b2e (A-1) and the r4 output
under 5ef61a412c6bd76c (DRAFT r1 §2); no 548ae790… entry was ever readable by either.

## 6. Findings (new and changed)

| id | classification | finding | gate effect | closure action | authority |
|---|---|---|---|---|---|
| R4A-05 | informational | transmission | — | CLOSED: 71 / 72 received with the listed hash; the 72nd proven by reconstruction (§2) | — |
| R4A-10 | cleanup | r3 quarantine chain (§5.2): (a) the store prefix 548ae790… is the fingerprint of the attempt-8 custody triple (harness 390f42b7…), contrary to the r4 erratum item 3, and 390f42b7… was not preserved; (b) the file filed under the ATTEMPT8 label, 99f895c1…, is named by no custody record and by no store fingerprint; (c) the ATTEMPT5-labelled harness f882b922… and generator cc23c9b5… are not the bytes the attempt-5 custody record names (d67e097d…, e35c2bf0…), neither of which was transmitted, though the r4 report §8 (c) lists d67e097d… as present; (d) the r3 log's revision 4 = f882b922… conflicts with the revision-4 custody record | none on any delivered output (final r3 1ba561da…, r4 5ef61a41…); A-1's T-R3-2 now has an answer | in the next r4 record child (the r3 files and the r4 log stay untouched): a second erratum stating (a)–(d); relabel or annotate the ATTEMPT5 and ATTEMPT8 quarantine files as bytes taken after the attempt, not the bytes run; either transmit d67e097d…, e35c2bf0… and 390f42b7… if the repository holds them, or record that they are not preserved and correct report §8 (c) | X |

R4A-01 … R4A-04 and R4A-06 … R4A-09 stand as in DRAFT r1.

## 7. Register (S / T / X) and status

```text
S  none open. S-R2-1 = PI_RULE (D-5) — implemented (DRAFT r1); nothing here reopens it
T  T-R2-2 = AUTHORIZE_RESTART (in narrowed_evidence) ; T-R4-1 CLOSED (R4A-05)
X  blocker R4A-01 ; cleanup R4A-02 … R4A-04, R4A-10 ; optional R4A-08

corrections_complete      = false in the auditor's view (R4A-01)
parents_unchanged         = true [A] for the 13 r3 files of the list (sidecars = A-1 hashes); beyond the list [X]
F3_STEP2_r4_status        = PARTIAL_PENDING_PI (agrees with the executor)
F3_STEP2 = QUALIFIED      = NOT declared ; F3_EXECUTION_READY = false ; commit = false
```

What the next step needs is unchanged from DRAFT r1, plus R4A-10: from the executor, the R4A-01 change and the
cleanup items (R4A-10 is documentation only, with no code and no re-run); from the PI, nothing scientific.

## 8. Appendix — evidence script and its verbatim output

The script reads the ten reception directories (recv = the first delivery, recv3 … recv11 = the batches after
DRAFT r1), the files A-1 audited (uploads), and A-1 itself. It writes nothing.

Script `r4_04_transmission_checks.py`:

```python
"""Evidence script 04 (F3 STEP-2 r4 independent audit, DRAFT r2; auditor claude-opus-5-5, 2026-09-28). Read-only.
Verifies the transmission batches received after DRAFT r1 (recv3 ... recv11) against the transmission list
(recv/, 10635dae...), the executor's notes, custody records and logs, and the auditor's own r3 audit (A-1).
Every value printed is computed here from bytes on disk; nothing is asserted about files that were not received."""
import hashlib, os, re, csv, io, json, collections, importlib.util, difflib
B = "/home/claude/audit_r4/"; UP = "/root/.claude/uploads/9c789a02-f865-56de-9f2f-e299f3cfca3a/"
A1 = "/mnt/user-data/outputs/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
def up(prefix):
    f = [x for x in os.listdir(UP) if x.startswith(prefix)]; assert len(f) == 1, prefix; return UP + f[0]
BATCHES = ["recv", "recv3", "recv4", "recv5", "recv6", "recv7", "recv8", "recv9", "recv10", "recv11"]
TL = B + "recv/f3_step2_r4_transmission_list_2026-09-27.md"
tl = open(TL, encoding="utf-8").read()
entries = [(m.group(1), m.group(2)) for m in re.finditer(r"^([0-9a-f]{64})  (\S+)$", tl, re.M)]
group_of = {}; g = None
for line in tl.split("\n"):
    m = re.match(r"^## ([A-F])\.", line)
    if m: g = m.group(1)
    m = re.match(r"^([0-9a-f]{64})  (\S+)$", line)
    if m: group_of[m.group(2)] = g

print("== [1] inventory of every received file (all batches), by distinct content")
files = {}   # (basename, hash) -> [batches]
paths = {}   # hash -> a path
for d in BATCHES:
    for f in sorted(os.listdir(B + d)):
        p = B + d + "/" + f
        if not os.path.isfile(p): continue
        h = sha(p); files.setdefault((f, h), []).append(d); paths.setdefault(h, p)
names_by_hash = collections.defaultdict(set)
for (f, h) in files: names_by_hash[h].add(f)
print("  received file instances:", sum(len(v) for v in files.values()), "| distinct (name, content):", len(files), "| distinct contents:", len(names_by_hash))
print("  same name with different content across batches:", [f for f, c in collections.Counter(f for f, _ in files).items() if c > 1] or "none")
notes_text = {}
for d in BATCHES:
    for f in os.listdir(B + d):
        if f.endswith((".md", ".log")) and os.path.isfile(B + d + "/" + f): notes_text[f] = open(B + d + "/" + f, encoding="utf-8", errors="replace").read()
notes_text["r3_attempt_log (A-1 upload e065f255)"] = open(up("e065f255-"), encoding="utf-8").read()

print("\n== [2] transmission list: 72 entries, by group")
got = set(h for (_, h) in files)
per_group = collections.defaultdict(lambda: [0, 0])
missing = []
first_batch = {}
for (f, h), ds in files.items(): first_batch.setdefault(h, sorted(ds, key=BATCHES.index)[0])
for h, p in entries:
    gg = group_of[p]; per_group[gg][0] += 1
    print("  %s %s… %-96s %s" % (gg, h[:8], p, ("received " + first_batch[h]) if h in got else "NOT RECEIVED"))
    if h in got and os.path.basename(p) in names_by_hash[h]: per_group[gg][1] += 1
    elif h in got: per_group[gg][1] += 1; print("  received under another name:", p, names_by_hash[h])
    else: missing.append((h, p))
for gg in sorted(per_group): print("  group %s: listed %2d | received with equal hash %2d" % (gg, *per_group[gg]))
print("  total listed:", len(entries), "| received equal:", sum(v[1] for v in per_group.values()), "| not received:", [(h[:8], p) for h, p in missing])

print("\n== [3] the entry not received: reconstruction of its bytes from the audited file it names")
r3_results = up("c67f0d5f-")   # the r3 results JSON audited in A-1
for h, p in missing:
    name = os.path.basename(p)[:-len(".sha256")]
    hr = sha(r3_results)
    lf = ("%s  %s\n" % (hr, name)).encode(); crlf = ("%s  %s\r\n" % (hr, name)).encode()
    print("  %s: named file %s audited in A-1 as %s (in A-1 text: %s)" % (p, name, hr, hr in open(A1, encoding="utf-8").read()))
    print("    sha256('<hash>  <name>\\n')   = %s == listed: %s" % (hashlib.sha256(lf).hexdigest(), hashlib.sha256(lf).hexdigest() == h))
    print("    sha256('<hash>  <name>\\r\\n') = %s == listed: %s" % (hashlib.sha256(crlf).hexdigest(), hashlib.sha256(crlf).hexdigest() == h))

print("\n== [4] received files not on the transmission list (hash, bytes, where the executor names that hash)")
listed_h = set(h for h, _ in entries)
for (f, h), ds in sorted(files.items()):
    if h in listed_h: continue
    refs = sorted(k for k, t in notes_text.items() if h in t and k != f)
    print("  %s %9d %-92s named in: %s" % (h[:16], os.path.getsize(paths[h]), f, refs or "-"))

print("\n== [5] every received sidecar: format, listed hash, and the hash it states vs the file it names")
a1 = open(A1, encoding="utf-8").read()
for (f, h), ds in sorted(files.items()):
    if not f.endswith(".sha256"): continue
    raw = open(paths[h], "rb").read(); t = raw.decode("utf-8")
    m = re.fullmatch(r"([0-9a-f]{64})  (\S+)\n", t)
    if not m:
        print("  %-80s MALFORMED (%d bytes): %r" % (f, len(raw), t)); continue
    sh, sn = m.groups()
    local = [x for (fn, x) in files if fn == sn]
    where = ("received %s: %s" % (sn, "EQUAL" if sh in local else "DIFF " + str([x[:8] for x in local]))) if local else \
            ("A-1 row with this name and hash: %s" % bool(re.search(re.escape(sn) + r".*" + sh, a1)))
    print("  %-72s listed=%-5s names %s | stated %s… | %s | CR=%d" % (f, h in listed_h, "self" if sn == f else "ok", sh[:12], where, raw.count(b"\r")))

print("\n== [6] fingerprints: every custody record received; named triple vs recorded fingerprint vs stores")
har4 = open(B + "recv/f3_step2_adequacy_harness_r4_2026-09-24.py", encoding="utf-8").read()
F2 = re.search(r'^F2_HASH = "([0-9a-f]{64})"', har4, re.M).group(1); SPL = re.search(r'^SPL_HASH = "([0-9a-f]{64})"', har4, re.M).group(1)
def fp(h, g_, m_):
    return hashlib.sha256("|".join([h, g_, m_, F2, SPL, "3.11.7", "1.26.4", "1.14.1", "Windows-10-10.0.19045-SP0", "1", "1", "1"]).encode()).hexdigest()[:16]
store_r3 = collections.Counter(r["path"].split("__")[0] for r in csv.DictReader(open(up("aa0941a1-"), newline="", encoding="utf-8")))
store_r4 = collections.Counter(r["path"].split("__")[0] for r in csv.DictReader(open(B + "recv/f3_step2_r4_restart_store_manifest_2026-09-24.csv", newline="", encoding="utf-8")))
foreign = list(csv.DictReader(open(B + "recv5/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv", newline="", encoding="utf-8")))
foreign_pref = collections.Counter(r["path"].split("__")[0] for r in foreign)
print("  r3 final store manifest (A-1 upload, %s…) prefixes: %s" % (sha(up("aa0941a1-"))[:8], dict(store_r3)))
print("  r4 store manifest prefixes:", dict(store_r4), "| foreign listing rows:", len(foreign), "prefixes:", dict(foreign_pref))
fr_sz = {r["path"].split("__", 1)[1]: r for r in foreign}
r3_548 = [r for r in csv.DictReader(open(up("aa0941a1-"), newline="", encoding="utf-8")) if r["path"].startswith("548ae790f6ac756a__")]
print("  foreign listing == the 548ae790 rows of the r3 store manifest (path, size, sha256):",
      sorted((r["path"], r["size_bytes"], r["sha256"]) for r in r3_548) == sorted((r["path"], r["size_bytes"], r["sha256"]) for r in foreign))
cust = [("r3 final (A-1 upload 0650b2af)", up("0650b2af-")),
        ("r3 ATTEMPT1_SUPERSEDED", B + "recv9/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT1_SUPERSEDED.md"),
        ("r3 ATTEMPT2-3", B + "recv7/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.md"),
        ("r3 ATTEMPT5", B + "recv7/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.md"),
        ("r3 ATTEMPT8", B + "recv7/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md"),
        ("r4 ATTEMPT1", B + "recv6/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.md"),
        ("r4 ATTEMPT2", B + "recv8/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT2_INTERRUPTED.md"),
        ("r4 ATTEMPT3-4", B + "recv5/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.md"),
        ("r4 ATTEMPT5-6", B + "recv5/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.md"),
        ("r4 final", B + "recv/f3_step2_r4_preexecution_custody_2026-09-24.md")]
qh = {"r3 ATTEMPT1_SUPERSEDED": B + "recv9/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py",
      "r3 ATTEMPT2-3": B + "recv7/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py",
      "r3 ATTEMPT5": B + "recv7/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py",
      "r3 ATTEMPT8": B + "recv7/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py",
      "r3 final (A-1 upload 0650b2af)": up("90f1b34d-"),
      "r4 ATTEMPT1": B + "recv8/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py",
      "r4 ATTEMPT2": B + "recv8/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py",
      "r4 ATTEMPT3-4": B + "recv5/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py",
      "r4 ATTEMPT5-6": B + "recv5/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py",
      "r4 final": B + "recv/f3_step2_adequacy_harness_r4_2026-09-24.py"}
gv = lambda k, t: (re.search(r"^%s = (\S+)" % k, t, re.M) or [None, None])[1]
for lab, p in cust:
    t = open(p, encoding="utf-8").read()
    hh, gg_, mm, rec = gv("harness_sha256", t), gv("generator_sha256", t), gv("manifest_sha256", t), gv("code_env_fingerprint", t)
    f_named = fp(hh, gg_, mm); qb = sha(qh[lab])
    f_q = fp(qb, gg_, mm)
    print("  %-31s custody %s… | names H %s… G %s… M %s… | fp(named) %s == recorded %s: %s | in r3 store %d, r4 store %d"
          % (lab, sha(p)[:8], hh[:8], gg_[:8], mm[:8], f_named, rec, f_named == rec, store_r3.get(f_named, 0), store_r4.get(f_named, 0)))
    print("  %-31s harness bytes filed under this label %s… == named: %s%s" % ("", qb[:8], qb == hh,
          "" if qb == hh else " | fp(filed bytes, named G, M) %s: r3 store %d, r4 store %d" % (f_q, store_r3.get(f_q, 0), store_r4.get(f_q, 0))))
all_named = set()
for _, p in cust:
    t = open(p, encoding="utf-8").read(); all_named |= set(re.findall(r"\b[0-9a-f]{64}\b", t))
for lab, h in (("r3 ATTEMPT5-labelled harness f882b922", "f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5"),
               ("r3 ATTEMPT8-labelled harness 99f895c1", "99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a"),
               ("attempt-8 custody harness 390f42b7", "390f42b72971030033c6964731d699358a1547bf9093b8e949c0e338e6bc0336")):
    as_harness = [l for l, p in cust if gv("harness_sha256", open(p, encoding="utf-8").read()) == h]
    print("  %-40s named as harness_sha256 by custody records: %s | received as bytes: %s | named in: %s"
          % (lab, as_harness or "none", h in got, sorted(k for k, t in notes_text.items() if h in t)))
for gh in ("f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5",):
    for gname, gx, mx in (("e35c2bf0/4544ff75", "e35c2bf06ee4087bac97bd5b6e81d35d079ff1dddf8d2e68555c6c7d18859638", "4544ff7565165f7541c0264b886bc2692374caf2ee875ec65a877c1a2909ec33"),
                          ("cc23c9b5/9c944543", "cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8", "9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a"),
                          ("cc23c9b5/4544ff75", "cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8", "4544ff7565165f7541c0264b886bc2692374caf2ee875ec65a877c1a2909ec33")):
        x = fp(gh, gx, mx); print("  fp(f882b922, %s) = %s | r3 store %d" % (gname, x, store_r3.get(x, 0)))

print("\n== [7] the r3 generator filed as ATTEMPT5: which manifest does it produce (harness writer: csv, LF, ascii)?")
gp = B + "recv7/f3_step2_fixture_generator_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py"
spec = importlib.util.spec_from_file_location("gen_r3_a5", gp); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)
buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(gen.MANIFEST_HEADER); w.writerows(gen.manifest_rows())
print("  generator %s… -> manifest %s | filed ATTEMPT5 manifest %s… | ATTEMPT5 custody names G %s… M %s…"
      % (sha(gp)[:8], hashlib.sha256(buf.getvalue().encode("ascii")).hexdigest(), sha(B + "recv7/f3_step2_fixture_manifest_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.csv")[:8], "e35c2bf0", "4544ff75"))
for lab, p in (("ATTEMPT2-3", B + "recv7/f3_step2_results_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.json"),
               ("ATTEMPT5", B + "recv9/f3_step2_results_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json")):
    r = json.load(open(p)); print("  results %-10s %s… fixture_manifest_sha256 %s… run1 %s… run2 %s…" % (lab, sha(p)[:8], r["fixture_manifest_sha256"][:8], r["run1_canonical_sha256"][:8], r["run2_canonical_sha256"][:8]))
for lab, p in (("ATTEMPT2-3", B + "recv10/f3_step2_test_evidence_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.json"),
               ("ATTEMPT5", B + "recv10/f3_step2_test_evidence_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json")):
    t = open(p, encoding="utf-8").read()
    kinds = collections.Counter(re.findall(r'"kind": "([A-Z_]+)"', t))
    print("  test evidence %-10s %s… capture kinds: %s" % (lab, sha(p)[:8], dict(kinds)))
print("  ATTEMPT5 residual %s… == ATTEMPT2-3 residual: %s == r3 final residual 3ee624f3…: %s" % (
      sha(B + "recv11/f3_step2_residual_series_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json")[:8],
      sha(B + "recv11/f3_step2_residual_series_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json") == sha(B + "recv7/f3_step2_residual_series_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.json"),
      sha(B + "recv11/f3_step2_residual_series_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json") == "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f"))

print("\n== [8] r4 supersession chain: non-comment line changes between consecutive harness revisions")
chain = [("rev1", qh["r4 ATTEMPT1"]), ("rev2", qh["r4 ATTEMPT2"]), ("rev3", qh["r4 ATTEMPT3-4"]), ("rev4", qh["r4 ATTEMPT5-6"]), ("rev5 (delivered)", qh["r4 final"])]
def code_lines(p):
    return [l.rstrip() for l in open(p, encoding="utf-8").read().split("\n") if l.strip() and not l.strip().startswith("#")]
for (a, pa), (b, pb) in zip(chain, chain[1:]):
    d = [l for l in difflib.unified_diff(code_lines(pa), code_lines(pb), lineterm="", n=0) if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    print("  %s %s… -> %s %s…: %d changed non-comment lines" % (a, sha(pa)[:8], b, sha(pb)[:8], len(d)))
    for l in d[:14]: print("     " + l.strip()[:150])
    if len(d) > 14: print("     ... (%d more)" % (len(d) - 14))

print("\n== [9] r4 run logs")
for f in sorted(x for (x, _) in files if x.startswith("f3_step2_r4_attempt") and x.endswith(".log")):
    t = notes_text[f]
    pairs = re.findall(r"(RUN[12][^\n]{0,40}?)([0-9a-f]{64})", t)
    print("  %-44s %8d B | Traceback: %-5s | EXIT_CODE: %s | AssertionError: %s | canonical hashes: %s"
          % (f, os.path.getsize(paths[[h for (x, h) in files if x == f][0]]), "Traceback" in t, re.findall(r"EXIT_CODE=(\d+)", t) or "-",
             [x[:80] for x in re.findall(r"AssertionError[^\n]*", t)][:1] or "-", sorted(set(h[:8] for _, h in pairs)) or "-"))
alog = open(B + "recv/f3_step2_r4_attempt_log_2026-09-24.md", encoding="utf-8").read()
for h8 in ("19454f65", "bfa626a6", "777fca02", "148db2d1"):
    print("  %s in r4 attempt log: %s | in logs: %s" % (h8, h8 in alog, sorted(f for f in notes_text if f.endswith(".log") and h8 in notes_text[f])))

print("\n== [10] two stray items")
c = B + "recv7/f3_step2_r3_auditor_transmittal_note_2026-09-22_CORRUPTED_2026-09-23.md"; o = up("880ad739-")
print("  CORRUPTED transmittal %s… vs the copy A-1 received (%s…): diff" % (sha(c)[:8], sha(o)[:8]))
for l in difflib.unified_diff(open(o, encoding="utf-8").read().split("\n"), open(c, encoding="utf-8").read().split("\n"), lineterm="", n=0):
    if l[:1] in "+-" and not l.startswith(("+++", "---")): print("     %r" % l)
```

Output `r4_04_transmission_checks.out.txt` (verbatim):

```text
== [1] inventory of every received file (all batches), by distinct content
  received file instances: 107 | distinct (name, content): 89 | distinct contents: 88
  same name with different content across batches: none

== [2] transmission list: 72 entries, by group
  A 54274b4e… calibration/f3_step2_adequacy_harness_r4_2026-09-24.py                                           received recv
  A e70cd58d… calibration/f3_step2_adequacy_harness_r4_2026-09-24.py.sha256                                    received recv4
  A 39391730… calibration/f3_step2_fixture_generator_r4_2026-09-24.py                                          received recv
  A cf655df0… calibration/f3_step2_fixture_generator_r4_2026-09-24.py.sha256                                   received recv4
  A c0b38ceb… calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv                                          received recv
  A fec2eadf… calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv.sha256                                   received recv4
  A 0f1724ab… provenance/f3_step2_r4_preexecution_custody_2026-09-24.md                                        received recv
  A 8af35f82… provenance/f3_step2_r4_preexecution_custody_2026-09-24.md.sha256                                 received recv3
  A 11e1e721… calibration/f3_step2_telemetry_r4_2026-09-24.csv                                                 received recv
  A 61cc185d… calibration/f3_step2_telemetry_r4_2026-09-24.csv.sha256                                          received recv4
  A a15b7eff… calibration/f3_step2_results_r4_2026-09-24.json                                                  received recv
  A 6d94e207… calibration/f3_step2_results_r4_2026-09-24.json.sha256                                           received recv4
  A 3ee624f3… calibration/f3_step2_residual_series_r4_2026-09-24.json                                          received recv
  A 2de33321… calibration/f3_step2_residual_series_r4_2026-09-24.json.sha256                                   received recv11
  A 118c3507… calibration/f3_step2_test_evidence_r4_2026-09-24.json                                            received recv
  A 8a86e063… calibration/f3_step2_test_evidence_r4_2026-09-24.json.sha256                                     received recv4
  A 0eed314c… calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md                                       received recv
  A c5593347… calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md.sha256                                received recv9
  A 5c9dea88… provenance/f3_step2_correction_report_r4_2026-09-27.md                                           received recv
  A 572ddd0b… provenance/f3_step2_correction_report_r4_2026-09-27.md.sha256                                    received recv3
  A 84090147… provenance/f3_step2_r4_attempt_log_2026-09-24.md                                                 received recv
  A d82c3fdc… provenance/f3_step2_r4_attempt_log_2026-09-24.md.sha256                                          received recv3
  A d7f689fe… calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv                                  received recv
  A ea9e877f… calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv.sha256                           received recv4
  A f3c923b1… calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv                                    received recv
  A 58458ee9… calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv.sha256                             received recv9
  B 756fcf5b… calibration/f3_step2_adequacy_harness_r3_2026-09-22.py.sha256                                    received recv9
  B 7761a2f4… calibration/f3_step2_fixture_generator_r3_2026-09-22.py.sha256                                   received recv9
  B 955f010c… calibration/f3_step2_fixture_manifest_r3_2026-09-22.csv.sha256                                   received recv9
  B feace2be… provenance/f3_step2_r3_preexecution_custody_2026-09-22.md.sha256                                 received recv9
  B 8a801fde… calibration/f3_step2_telemetry_r3_2026-09-22.csv.sha256                                          received recv9
  B 714b5072… calibration/f3_step2_results_r3_2026-09-22.json.sha256                                           NOT RECEIVED
  B 91dd3b85… calibration/f3_step2_residual_series_r3_2026-09-22.json.sha256                                   received recv11
  B 5e99371a… calibration/f3_step2_test_evidence_r3_2026-09-22.json.sha256                                     received recv10
  B 152db955… provenance/f3_step2_correction_report_r3_2026-09-24.md.sha256                                    received recv9
  B ce2cbe70… provenance/f3_step2_r3_start_state_inventory_2026-09-22.md.sha256                                received recv9
  B ffc90aab… provenance/f3_step2_r3_attempt_log_2026-09-22.md.sha256                                          received recv9
  B 790cf31a… calibration/f3_step2_spline_percall_telemetry_r3_2026-09-22.csv.sha256                           received recv9
  B d5539e00… calibration/f3_step2_r3_restart_store_manifest_2026-09-22.csv.sha256                             received recv9
  C 78e6627d… quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md                                  received recv9
  C 88558b26… quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md                                 received recv7
  C 9db9079f… quarantine/f3_step2_r3_independent_audit_corrections_note_2026-09-23.md                          received recv7
  C 3a1ad5aa… quarantine/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md                          received recv7
  C 683108f3… quarantine/f3_step2_r3_auditor_transmittal_note_corruption_incident_2026-09-23.md                received recv7
  D 6ddcc26d… quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py                        received recv9
  D c8d47629… quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT1_SUPERSEDED.md                    received recv9
  D 891574fc… quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py      received recv7
  D a4c7d65c… quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.md  received recv7
  D f882b922… quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py       received recv7
  D e67bd9d7… quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.md   received recv7
  D 99f895c1… quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py      received recv7
  D 2e55e150… quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md  received recv7
  E 0ebaaaeb… quarantine/f3_step2_r4_attempt1_supersession_note_2026-09-24.md                                  received recv5
  E f137299c… quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py            received recv8
  E 307809c5… quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.md        received recv6
  E 1f1e0e08… quarantine/f3_step2_r4_attempt2_interruption_note_2026-09-26.md                                  received recv5
  E 20d830e0… quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py                       received recv8
  E 856201af… quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT2_INTERRUPTED.md                   received recv8
  E e467d95f… quarantine/f3_step2_r4_attempt34_k05_nondeterminism_note_2026-09-26.md                           received recv5
  E 814e395a… quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py      received recv5
  E 51499dc4… quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.md  received recv5
  E 3ba2075f… quarantine/f3_step2_r4_attempt56_mutation_leak_note_2026-09-27.md                                received recv5
  E 90ea0ff3… quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py                   received recv5
  E cb2204b1… quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.md               received recv5
  E 40b3a53d… quarantine/f3_step2_r4_attempt1_stdout_2026-09-24.log                                            received recv6
  E 71a0bfd2… quarantine/f3_step2_r4_attempt2_stdout_2026-09-26.log                                            received recv8
  E fbbcc5e6… quarantine/f3_step2_r4_attempt3_stdout_2026-09-26.log                                            received recv5
  E 3b871223… quarantine/f3_step2_r4_attempt4_stdout_2026-09-26.log                                            received recv5
  E ca429b22… quarantine/f3_step2_r4_attempt5_stdout_2026-09-26.log                                            received recv5
  E 3130cb5f… quarantine/f3_step2_r4_attempt6_stdout_2026-09-27.log                                            received recv5
  F 7a77da84… quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv                      received recv5
  F 9fe259d5… quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv.sha256               received recv5
  group A: listed 26 | received with equal hash 26
  group B: listed 13 | received with equal hash 12
  group C: listed  5 | received with equal hash  5
  group D: listed  8 | received with equal hash  8
  group E: listed 18 | received with equal hash 18
  group F: listed  2 | received with equal hash  2
  total listed: 72 | received equal: 71 | not received: [('714b5072', 'calibration/f3_step2_results_r3_2026-09-22.json.sha256')]

== [3] the entry not received: reconstruction of its bytes from the audited file it names
  calibration/f3_step2_results_r3_2026-09-22.json.sha256: named file f3_step2_results_r3_2026-09-22.json audited in A-1 as 352791648b7c3dc1151962905ec2270fe3ae4246846f2021c2dcda3e3dfe18fb (in A-1 text: True)
    sha256('<hash>  <name>\n')   = 714b5072589bec65f32f2a76f5b49130f4064b73bfd9ce5e9eb68df95570ed35 == listed: True
    sha256('<hash>  <name>\r\n') = a14fe2d44d4d9647b1d8f61f3412c5a41b01ee0741876207787102f4119a98f1 == listed: False

== [4] received files not on the transmission list (hash, bytes, where the executor names that hash)
  d7068f3dd5436e03        46 STRAY_MALFORMED_root_f3_step2_correction_report_r3_2026-09-24.md.sha256                      named in: -
  cc23c9b5ef658bb2     46877 f3_step2_fixture_generator_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py             named in: ['f3_step2_r3_independent_audit_corrections_note_2026-09-23.md', 'f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md']
  4544ff7565165f75     18878 f3_step2_fixture_manifest_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.csv             named in: ['f3_step2_r3_independent_audit_corrections_note_2026-09-23.md', 'f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT1_SUPERSEDED.md', 'f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.md', 'f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.md']
  bc793a3b25e3e0a1      7201 f3_step2_r3_auditor_transmittal_note_2026-09-22_CORRUPTED_2026-09-23.md                      named in: ['f3_step2_r3_auditor_transmittal_note_corruption_incident_2026-09-23.md']
  ff1c30d9e0d9a777    232316 f3_step2_r4_attempt1_stderr_2026-09-24.log                                                   named in: -
  6c5a4874140b161f    258927 f3_step2_r4_attempt2_stderr_2026-09-26.log                                                   named in: -
  93528feb913f403a     29190 f3_step2_r4_attempt4_stderr_2026-09-26.log                                                   named in: -
  f677655fceb2178f       423 f3_step2_r4_attempt6_stderr_2026-09-27.log                                                   named in: -
  10635daea95656ba      9936 f3_step2_r4_transmission_list_2026-09-27.md                                                  named in: -
  45d2b28ed1c0de76       110 f3_step2_r4_transmission_list_2026-09-27.md.sha256                                           named in: -
  f28bd6a02978154d     46709 f3_step2_residual_series_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.json            named in: ['f3_step2_r3_exc_classification_bug_note_2026-09-22.md', 'f3_step2_r3_independent_audit_corrections_note_2026-09-23.md']
  f28bd6a02978154d     46709 f3_step2_residual_series_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json             named in: ['f3_step2_r3_exc_classification_bug_note_2026-09-22.md', 'f3_step2_r3_independent_audit_corrections_note_2026-09-23.md']
  52e430aaae48be73   1184210 f3_step2_results_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.json                    named in: ['f3_step2_r3_exc_classification_bug_note_2026-09-22.md']
  06210546d4d1053d   1186035 f3_step2_results_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json                     named in: ['f3_step2_r3_independent_audit_corrections_note_2026-09-23.md']
  931a9640cb0feaa8   1608802 f3_step2_telemetry_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.csv                   named in: ['f3_step2_r3_exc_classification_bug_note_2026-09-22.md']
  858eaf3b181d61a8   1608722 f3_step2_telemetry_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.csv                    named in: ['f3_step2_r3_independent_audit_corrections_note_2026-09-23.md']
  14edaaa57eb3fce1     24630 f3_step2_test_evidence_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.json              named in: ['f3_step2_r3_exc_classification_bug_note_2026-09-22.md']
  f74459354d8526ee     24693 f3_step2_test_evidence_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.json               named in: ['f3_step2_r3_independent_audit_corrections_note_2026-09-23.md']

== [5] every received sidecar: format, listed hash, and the hash it states vs the file it names
  STRAY_MALFORMED_root_f3_step2_correction_report_r3_2026-09-24.md.sha256          MALFORMED (46 bytes): '  f3_step2_correction_report_r3_2026-09-24.md\n'
  f3_step2_adequacy_harness_r3_2026-09-22.py.sha256                        listed=True  names ok | stated 5fea165cf593… | A-1 row with this name and hash: True | CR=0
  f3_step2_adequacy_harness_r4_2026-09-24.py.sha256                        listed=True  names ok | stated 54274b4e1edf… | received f3_step2_adequacy_harness_r4_2026-09-24.py: EQUAL | CR=0
  f3_step2_class_c_pin_register_r4_2026-09-27.md.sha256                    listed=True  names ok | stated 0eed314c0420… | received f3_step2_class_c_pin_register_r4_2026-09-27.md: EQUAL | CR=0
  f3_step2_correction_report_r3_2026-09-24.md.sha256                       listed=True  names ok | stated 80df7914940f… | A-1 row with this name and hash: True | CR=0
  f3_step2_correction_report_r4_2026-09-27.md.sha256                       listed=True  names ok | stated 5c9dea88e45d… | received f3_step2_correction_report_r4_2026-09-27.md: EQUAL | CR=0
  f3_step2_fixture_generator_r3_2026-09-22.py.sha256                       listed=True  names ok | stated cc23c9b5ef65… | A-1 row with this name and hash: True | CR=0
  f3_step2_fixture_generator_r4_2026-09-24.py.sha256                       listed=True  names ok | stated 393917300d2c… | received f3_step2_fixture_generator_r4_2026-09-24.py: EQUAL | CR=0
  f3_step2_fixture_manifest_r3_2026-09-22.csv.sha256                       listed=True  names ok | stated 9c944543bb2f… | A-1 row with this name and hash: True | CR=0
  f3_step2_fixture_manifest_r4_2026-09-24.csv.sha256                       listed=True  names ok | stated c0b38cebcddf… | received f3_step2_fixture_manifest_r4_2026-09-24.csv: EQUAL | CR=0
  f3_step2_r3_attempt_log_2026-09-22.md.sha256                             listed=True  names ok | stated 253163891bab… | A-1 row with this name and hash: True | CR=0
  f3_step2_r3_preexecution_custody_2026-09-22.md.sha256                    listed=True  names ok | stated a910e1b65f47… | A-1 row with this name and hash: True | CR=0
  f3_step2_r3_restart_store_manifest_2026-09-22.csv.sha256                 listed=True  names ok | stated 933dcaeeb979… | A-1 row with this name and hash: True | CR=0
  f3_step2_r3_start_state_inventory_2026-09-22.md.sha256                   listed=True  names ok | stated 71a3f5a7cf98… | A-1 row with this name and hash: True | CR=0
  f3_step2_r4_attempt_log_2026-09-24.md.sha256                             listed=True  names ok | stated 840901474867… | received f3_step2_r4_attempt_log_2026-09-24.md: EQUAL | CR=0
  f3_step2_r4_preexecution_custody_2026-09-24.md.sha256                    listed=True  names ok | stated 0f1724ab8b8d… | received f3_step2_r4_preexecution_custody_2026-09-24.md: EQUAL | CR=0
  f3_step2_r4_restart_store_manifest_2026-09-24.csv.sha256                 listed=True  names ok | stated f3c923b11942… | received f3_step2_r4_restart_store_manifest_2026-09-24.csv: EQUAL | CR=0
  f3_step2_r4_transmission_list_2026-09-27.md.sha256                       listed=False names ok | stated 10635daea956… | received f3_step2_r4_transmission_list_2026-09-27.md: EQUAL | CR=0
  f3_step2_residual_series_r3_2026-09-22.json.sha256                       listed=True  names ok | stated 3ee624f3a3e0… | A-1 row with this name and hash: True | CR=0
  f3_step2_residual_series_r4_2026-09-24.json.sha256                       listed=True  names ok | stated 3ee624f3a3e0… | received f3_step2_residual_series_r4_2026-09-24.json: EQUAL | CR=0
  f3_step2_results_r4_2026-09-24.json.sha256                               listed=True  names ok | stated a15b7efffd1b… | received f3_step2_results_r4_2026-09-24.json: EQUAL | CR=0
  f3_step2_spline_percall_telemetry_r3_2026-09-22.csv.sha256               listed=True  names ok | stated 9d0c627ebc59… | A-1 row with this name and hash: True | CR=0
  f3_step2_spline_percall_telemetry_r4_2026-09-24.csv.sha256               listed=True  names ok | stated d7f689fe5e9f… | received f3_step2_spline_percall_telemetry_r4_2026-09-24.csv: EQUAL | CR=0
  f3_step2_telemetry_r3_2026-09-22.csv.sha256                              listed=True  names ok | stated 24f21811886c… | A-1 row with this name and hash: True | CR=0
  f3_step2_telemetry_r4_2026-09-24.csv.sha256                              listed=True  names ok | stated 11e1e721595c… | received f3_step2_telemetry_r4_2026-09-24.csv: EQUAL | CR=0
  f3_step2_test_evidence_r3_2026-09-22.json.sha256                         listed=True  names ok | stated b7d3b861be33… | A-1 row with this name and hash: True | CR=0
  f3_step2_test_evidence_r4_2026-09-24.json.sha256                         listed=True  names ok | stated 118c35076263… | received f3_step2_test_evidence_r4_2026-09-24.json: EQUAL | CR=0
  r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv.sha256  listed=True  names ok | stated 7a77da849785… | received r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv: EQUAL | CR=0

== [6] fingerprints: every custody record received; named triple vs recorded fingerprint vs stores
  r3 final store manifest (A-1 upload, 933dcaee…) prefixes: {'1ba561daefb48b2e': 11723, '548ae790f6ac756a': 11723}
  r4 store manifest prefixes: {'5ef61a412c6bd76c': 11869} | foreign listing rows: 11723 prefixes: {'548ae790f6ac756a': 11723}
  foreign listing == the 548ae790 rows of the r3 store manifest (path, size, sha256): True
  r3 final (A-1 upload 0650b2af)  custody a910e1b6… | names H 5fea165c… G cc23c9b5… M 9c944543… | fp(named) 1ba561daefb48b2e == recorded 1ba561daefb48b2e: True | in r3 store 11723, r4 store 0
                                  harness bytes filed under this label 5fea165c… == named: True
  r3 ATTEMPT1_SUPERSEDED          custody c8d47629… | names H 6ddcc26d… G e35c2bf0… M 4544ff75… | fp(named) 2cf50b2f18cfb34e == recorded 2cf50b2f18cfb34e: True | in r3 store 0, r4 store 0
                                  harness bytes filed under this label 6ddcc26d… == named: True
  r3 ATTEMPT2-3                   custody a4c7d65c… | names H 891574fc… G e35c2bf0… M 4544ff75… | fp(named) d505bf76994abf60 == recorded d505bf76994abf60: True | in r3 store 0, r4 store 0
                                  harness bytes filed under this label 891574fc… == named: True
  r3 ATTEMPT5                     custody e67bd9d7… | names H d67e097d… G e35c2bf0… M 4544ff75… | fp(named) 6f4e29ccc903bce6 == recorded 6f4e29ccc903bce6: True | in r3 store 0, r4 store 0
                                  harness bytes filed under this label f882b922… == named: False | fp(filed bytes, named G, M) 9bb07bae05cdeb5e: r3 store 0, r4 store 0
  r3 ATTEMPT8                     custody 2e55e150… | names H 390f42b7… G cc23c9b5… M 9c944543… | fp(named) 548ae790f6ac756a == recorded 548ae790f6ac756a: True | in r3 store 11723, r4 store 0
                                  harness bytes filed under this label 99f895c1… == named: False | fp(filed bytes, named G, M) 327fcf82f949fc66: r3 store 0, r4 store 0
  r4 ATTEMPT1                     custody 307809c5… | names H f137299c… G 39391730… M c0b38ceb… | fp(named) e9d93b0e7e5a9834 == recorded e9d93b0e7e5a9834: True | in r3 store 0, r4 store 0
                                  harness bytes filed under this label f137299c… == named: True
  r4 ATTEMPT2                     custody 856201af… | names H 20d830e0… G 39391730… M c0b38ceb… | fp(named) f03efb7069fa533e == recorded f03efb7069fa533e: True | in r3 store 0, r4 store 0
                                  harness bytes filed under this label 20d830e0… == named: True
  r4 ATTEMPT3-4                   custody 51499dc4… | names H 814e395a… G 39391730… M c0b38ceb… | fp(named) de4720325eb70003 == recorded de4720325eb70003: True | in r3 store 0, r4 store 0
                                  harness bytes filed under this label 814e395a… == named: True
  r4 ATTEMPT5-6                   custody cb2204b1… | names H 90ea0ff3… G 39391730… M c0b38ceb… | fp(named) 6ec6fc2a42343433 == recorded 6ec6fc2a42343433: True | in r3 store 0, r4 store 0
                                  harness bytes filed under this label 90ea0ff3… == named: True
  r4 final                        custody 0f1724ab… | names H 54274b4e… G 39391730… M c0b38ceb… | fp(named) 5ef61a412c6bd76c == recorded 5ef61a412c6bd76c: True | in r3 store 0, r4 store 11869
                                  harness bytes filed under this label 54274b4e… == named: True
  r3 ATTEMPT5-labelled harness f882b922    named as harness_sha256 by custody records: none | received as bytes: True | named in: ['f3_step2_r3_independent_audit_corrections_note_2026-09-23.md', 'f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md', 'f3_step2_r4_transmission_list_2026-09-27.md', 'r3_attempt_log (A-1 upload e065f255)']
  r3 ATTEMPT8-labelled harness 99f895c1    named as harness_sha256 by custody records: none | received as bytes: True | named in: ['f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md', 'f3_step2_r4_transmission_list_2026-09-27.md', 'r3_attempt_log (A-1 upload e065f255)']
  attempt-8 custody harness 390f42b7       named as harness_sha256 by custody records: ['r3 ATTEMPT8'] | received as bytes: False | named in: ['f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md']
  fp(f882b922, e35c2bf0/4544ff75) = 9bb07bae05cdeb5e | r3 store 0
  fp(f882b922, cc23c9b5/9c944543) = e3ccc7d133c9ff2f | r3 store 0
  fp(f882b922, cc23c9b5/4544ff75) = 2c2e92ca7c7cc780 | r3 store 0

== [7] the r3 generator filed as ATTEMPT5: which manifest does it produce (harness writer: csv, LF, ascii)?
  generator cc23c9b5… -> manifest 9c944543bb2f0eeb660ee86c84cd4199db9576bf3c32e7eb0f28eb92447f086a | filed ATTEMPT5 manifest 4544ff75… | ATTEMPT5 custody names G e35c2bf0… M 4544ff75…
  results ATTEMPT2-3 52e430aa… fixture_manifest_sha256 4544ff75… run1 943d14ab… run2 943d14ab…
  results ATTEMPT5   06210546… fixture_manifest_sha256 4544ff75… run1 943d14ab… run2 943d14ab…
  test evidence ATTEMPT2-3 14edaaa5… capture kinds: {'UNRELATED': 1}
  test evidence ATTEMPT5   f7445935… capture kinds: {'COVERED': 1}
  ATTEMPT5 residual f28bd6a0… == ATTEMPT2-3 residual: True == r3 final residual 3ee624f3…: False

== [8] r4 supersession chain: non-comment line changes between consecutive harness revisions
  rev1 f137299c… -> rev2 20d830e0…: 11 changed non-comment lines
     -SUPERSEDES_HARNESS_SHA256 = None
     -SUPERSEDES_CUSTODY_SHA256 = None
     -SUPERSEDES_NOTE_PATH = None
     -ATTEMPT_NUMBER = 1
     +SUPERSEDES_HARNESS_SHA256 = "f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418"
     +SUPERSEDES_CUSTODY_SHA256 = "307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441"
     +SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4_attempt1_supersession_note_2026-09-24.md"
     +ATTEMPT_NUMBER = 2
     -                if cr.get("kind") == "UNRELATED" and "TEST_ONLY" not in cr.get("message", ""):
     +                if cr.get("kind") == "UNRELATED":
     +                any_mode_unrelated = True   # attempt-1 bug: was never set here
  rev2 20d830e0… -> rev3 814e395a…: 10 changed non-comment lines
     -RESTART_LAYER_ACTIVE = False
     -SUPERSEDES_HARNESS_SHA256 = "f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418"
     -SUPERSEDES_CUSTODY_SHA256 = "307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441"
     -SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4_attempt1_supersession_note_2026-09-24.md"
     -ATTEMPT_NUMBER = 2
     +RESTART_LAYER_ACTIVE = True
     +SUPERSEDES_HARNESS_SHA256 = "20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306"
     +SUPERSEDES_CUSTODY_SHA256 = "856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78"
     +SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4_attempt2_interruption_note_2026-09-26.md"
     +ATTEMPT_NUMBER = 3
  rev3 814e395a… -> rev4 90ea0ff3…: 13 changed non-comment lines
     -SUPERSEDES_HARNESS_SHA256 = "20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306"
     -SUPERSEDES_CUSTODY_SHA256 = "856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78"
     -SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4_attempt2_interruption_note_2026-09-26.md"
     -ATTEMPT_NUMBER = 3
     +SUPERSEDES_HARNESS_SHA256 = "814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f"
     +SUPERSEDES_CUSTODY_SHA256 = "51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f"
     +SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4_attempt34_k05_nondeterminism_note_2026-09-26.md"
     +ATTEMPT_NUMBER = 5
     +    k05_before = K05_CHECK_COUNT[0]
     -    ev["k05_result"] = ("PASS(%d checks, assertion never triggered)"
     -                        % K05_CHECK_COUNT[0])
     +    ev["k05_result"] = ("PASS(%d checks this fixture, assertion never triggered)"
     +                        % (K05_CHECK_COUNT[0] - k05_before))
  rev4 90ea0ff3… -> rev5 (delivered) 54274b4e…: 15 changed non-comment lines
     -SUPERSEDES_HARNESS_SHA256 = "814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f"
     -SUPERSEDES_CUSTODY_SHA256 = "51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f"
     -SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4_attempt34_k05_nondeterminism_note_2026-09-26.md"
     -ATTEMPT_NUMBER = 5
     +SUPERSEDES_HARNESS_SHA256 = "90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805"
     +SUPERSEDES_CUSTODY_SHA256 = "cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273"
     +SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4_attempt56_mutation_leak_note_2026-09-27.md"
     +ATTEMPT_NUMBER = 7
     +        mutations_to_restore = []
     -                    S[sx]["P01"]["d"][field][idx] = float("nan")
     +                    arr = S[sx]["P01"]["d"][field]
     +                    mutations_to_restore.append((arr, idx, arr[idx]))
     +                    arr[idx] = float("nan")
     +        for arr, idx, orig in mutations_to_restore:
     ... (1 more)

== [9] r4 run logs
  f3_step2_r4_attempt1_stderr_2026-09-24.log     232316 B | Traceback: True  | EXIT_CODE: - | AssertionError: ['AssertionError'] | canonical hashes: -
  f3_step2_r4_attempt1_stdout_2026-09-24.log       5872 B | Traceback: False | EXIT_CODE: ['1'] | AssertionError: - | canonical hashes: -
  f3_step2_r4_attempt2_stderr_2026-09-26.log     258927 B | Traceback: False | EXIT_CODE: - | AssertionError: - | canonical hashes: -
  f3_step2_r4_attempt2_stdout_2026-09-26.log       6969 B | Traceback: False | EXIT_CODE: - | AssertionError: - | canonical hashes: -
  f3_step2_r4_attempt3_stdout_2026-09-26.log       7346 B | Traceback: False | EXIT_CODE: - | AssertionError: - | canonical hashes: -
  f3_step2_r4_attempt4_stderr_2026-09-26.log      29190 B | Traceback: True  | EXIT_CODE: - | AssertionError: ['AssertionError: RUN1/RUN2 canonical document mismatch -> STOP'] | canonical hashes: -
  f3_step2_r4_attempt4_stdout_2026-09-26.log      10084 B | Traceback: True  | EXIT_CODE: ['1'] | AssertionError: - | canonical hashes: ['19454f65', 'bfa626a6']
  f3_step2_r4_attempt5_stdout_2026-09-26.log       8483 B | Traceback: False | EXIT_CODE: - | AssertionError: - | canonical hashes: -
  f3_step2_r4_attempt6_stderr_2026-09-27.log        423 B | Traceback: True  | EXIT_CODE: - | AssertionError: ['AssertionError: RUN1/RUN2 canonical document mismatch -> STOP'] | canonical hashes: -
  f3_step2_r4_attempt6_stdout_2026-09-27.log       9410 B | Traceback: True  | EXIT_CODE: ['1'] | AssertionError: - | canonical hashes: ['148db2d1', '777fca02']
  19454f65 in r4 attempt log: True | in logs: ['f3_step2_r4_attempt4_stdout_2026-09-26.log']
  bfa626a6 in r4 attempt log: True | in logs: ['f3_step2_r4_attempt4_stdout_2026-09-26.log']
  777fca02 in r4 attempt log: True | in logs: ['f3_step2_r4_attempt6_stdout_2026-09-27.log']
  148db2d1 in r4 attempt log: True | in logs: ['f3_step2_r4_attempt6_stdout_2026-09-27.log']

== [10] two stray items
  CORRUPTED transmittal bc793a3b… vs the copy A-1 received (bbe898cc…): diff
     '-## 2. Reading order'
     '+## 2. Reading +'
     '+'
     '+order'
```
