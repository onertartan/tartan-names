# Cross-version diff application

The patches compare UTF-8 source lines with LF line endings. The executor targets are LF; a Windows checkout of the historical parent can be CRLF. The original files and approved source bytes were never changed.

For each patch, create a disposable copy of the baseline under the target relative path named in diff_custody.json. Convert CRLF to LF only in that disposable copy, then run:

```text
git -c core.autocrlf=false apply --unidiff-zero --whitespace=nowarn -p0 <patch>
```

The recorded actual application checks require the resulting byte SHA256 to equal the approved target hash. All recorded checks passed. Context-zero patches require --unidiff-zero. Initial checks with historical bytes placed only under the baseline filename failed because git apply chooses the target filename; a later check with Windows autocrlf produced CRLF output. Those checks changed disposable copies only. The explicit LF procedure above produced the exact approved bytes. The label tables partition each mixed hunk into non-overlapping old/new line intervals, each with one originating-package label.
