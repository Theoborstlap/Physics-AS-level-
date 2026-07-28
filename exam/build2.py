"""Build PACK 2: render the Pack 2 question/answer HTML to PDF with headless Chromium.
Imports ONLY the Pack 2 question modules so engine.theory / engine.mcq contain
just the Pack 2 questions."""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import engine
engine.PACK_LABEL = "Pack 2"

import reference            # noqa: F401  (defines REFERENCE_HTML)

# Importing these modules appends the Pack 2 questions to engine.theory / engine.mcq
import theory_pack2_1   # noqa
import theory_pack2_2   # noqa
import theory_pack2_3   # noqa
import mcq_pack2_1      # noqa
import mcq_pack2_2      # noqa

CHROME = "/opt/playwright/chromium-1232/chrome-linux64/chrome"


def write(path, html):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def to_pdf(html_path, pdf_path):
    subprocess.run([
        CHROME, "--headless", "--no-sandbox", "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}", html_path,
    ], check=True, cwd=HERE,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    print(f"[Pack 2] Theory questions: {len(engine.theory)}")
    print(f"[Pack 2] MCQ questions   : {len(engine.mcq)}")
    print(f"[Pack 2] TOTAL           : {len(engine.theory) + len(engine.mcq)}")

    q_html = os.path.join(HERE, "questions_pack2.html")
    a_html = os.path.join(HERE, "answers_pack2.html")
    write(q_html, engine.render_questions())
    write(a_html, engine.render_answers())

    out_dir = os.path.dirname(HERE)  # repo root
    to_pdf(q_html, os.path.join(out_dir, "AS_Physics_9702_Pack2_Questions.pdf"))
    to_pdf(a_html, os.path.join(out_dir, "AS_Physics_9702_Pack2_Answers.pdf"))
    print("Pack 2 PDFs written to repo root.")


if __name__ == "__main__":
    main()
