# Tyler Osborne — local CV

Edit `tyler-osborne-cv.tex` to update the one-page CV. The source, original
template, license, and verification files in this directory are tracked in Git.
The compiler, generated PDFs, previews, and logs here are ignored. This directory
is excluded from Jekyll. The published PDF is tracked at
`files/tyler-osborne-cv.pdf` and linked from the CV webpage.

The layout adapts Jake Gutierrez's MIT-licensed Jake's Resume:
https://github.com/jakegut/resume. The original template and its license are
included as `template-original.tex` and `LICENSE-template`.

The CV uses the website's education, work experience, and teaching content,
with teaching counts expressed as terms (for example, “Compilers (2 terms)”).
It includes the two clinical AI papers, the Murzaku paper, and the undergraduate
thesis. Talks and the HPV paper are omitted. Contact details are plain text;
the two advisors' names link to their webpages using the original website URLs.
All hyperlinks display a small black external-link icon next to their text,
without colored text, underlining, or borders. The shared `\href` definition
applies this style to future hyperlinks as well.

Publications use a consistent author–date format: surnames and initials, up to
three authors followed by “et al.” for longer lists, boldface for Tyler's name,
sentence-case titles without quotation marks, italic venues, and uniform
punctuation. The `\publication` command controls the shared formatting.

## Rebuild

From the repository root:

```sh
local/cv/bin/tectonic --keep-logs --outdir local/cv local/cv/tyler-osborne-cv.tex
.personal-website/bin/python local/cv/verify.py
```

The local compiler is standalone Tectonic 0.17.0 for macOS ARM64. On a fresh
checkout, download the appropriate executable from
https://github.com/tectonic-typesetting/tectonic/releases/tag/tectonic%400.17.0
and place it at `local/cv/bin/tectonic` (create the directory and make the binary
executable with `chmod +x local/cv/bin/tectonic`). Alternatively, install
Tectonic with your package manager and use `tectonic` in the rebuild command.
Its first run downloads LaTeX support files; subsequent runs reuse its cache.
No system-wide LaTeX installation is needed.

Verification uses the existing Python 3.12.9 environment. To reinstall its PDF
inspection dependency:

```sh
uv pip install --python .personal-website/bin/python pymupdf
```

If the environment is missing, first recreate it with:

```sh
uv venv --python 3.12 .personal-website
```

`verify.py` checks page size, page count, preserved text, and both advisor links.
It saves `preview.png` for visual inspection and `verification.txt` with its
results. `expected-text.txt` records the current intended PDF wording; update
it alongside intentional wording changes.

After rebuilding and verifying, update the published copy and commit it with
the source changes:

```sh
cp local/cv/tyler-osborne-cv.pdf files/tyler-osborne-cv.pdf
```

