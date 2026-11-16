"""Check the local CV and render a preview using PyMuPDF."""

from pathlib import Path
import re
import unicodedata

import pymupdf


HERE = Path(__file__).resolve().parent


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u00ad", "")
    text = text.translate(str.maketrans({"“": '"', "”": '"', "’": "'", "–": "-", "—": "-"}))
    text = re.sub(r"-{2,}", "-", text)
    return re.sub(r"\s+", "", text).casefold()


with pymupdf.open(HERE / "tyler-osborne-cv.pdf") as document:
    assert len(document) == 1, f"Expected one page, got {len(document)}"
    page = document[0]
    assert abs(page.rect.width - 612) < 0.1 and abs(page.rect.height - 792) < 0.1, page.rect
    links = page.get_links()
    expected_links = {
        "https://www3.cs.stonybrook.edu/~fuswang/": "Prof. Fusheng Wang",
        "http://www.amittai.com": "Prof. Amittai Aviram",
    }
    assert len(links) == 2 and {link.get("uri") for link in links} == set(expected_links), "Unexpected advisor hyperlinks"
    for link in links:
        name_rects = page.search_for(expected_links[link["uri"]])
        assert any(link["from"].intersects(rect) for rect in name_rects), "Advisor link is misplaced"
    actual = normalize(page.get_text())
    expected = (HERE / "expected-text.txt").read_text().splitlines()
    missing = [line for line in expected if normalize(line) not in actual]
    assert not missing, "Missing or changed content:\n" + "\n".join(missing)
    assert "vaccination" not in actual.lower(), "Excluded HPV paper found"
    assert "Talks" not in page.get_text(), "Excluded talks found"
    citations = [line for line in expected if re.search(r"\(20\d{2}\)", line)]
    assert len(citations) == 4, f"Expected four citations, got {len(citations)}"
    assert all(actual.count(normalize(citation)) == 1 for citation in citations), "Repeated publication citation"
    spans = [span for block in page.get_text("dict")["blocks"] if "lines" in block
             for line in block["lines"] for span in line["spans"]]
    for span in spans:
        rect = pymupdf.Rect(span["bbox"])
        assert page.rect.contains(rect), f"Text extends off page: {span['text']}"
    page.get_pixmap(matrix=pymupdf.Matrix(2, 2)).save(HERE / "preview.png")
    report = (
        "PASS: 1 page, US Letter (612 × 792 pt)\n"
        f"PASS: all {len(expected)} source text entries preserved\n"
        "PASS: exactly 4 selected publication citations\n"
        "PASS: both advisor names link to their original webpages\n"
        "PASS: no additional hyperlinks, talks, or HPV paper\n"
        "PASS: selectable text contained within page bounds\n"
        f"Smallest text: {min(span['size'] for span in spans):.2f} pt\n"
    )
    (HERE / "verification.txt").write_text(report)
    print(report, end="")
