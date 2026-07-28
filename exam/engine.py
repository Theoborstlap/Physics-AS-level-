"""
Generator engine for the Cambridge AS Physics 9702 exam pack.
Builds questions.html and answers.html from the theory[] and mcq[] lists,
then those are rendered to PDF with headless Chromium (see build.py).

Question data formats
---------------------
Theory question (dict):
    topic  : str  -> section label, e.g. "1  Physical quantities and units"
    q      : str  -> HTML question text (may contain sub-parts <ol type='a'>)
    svg    : str  -> optional inline SVG diagram (or "" for none)
    marks  : int  -> total marks
    ans    : str  -> HTML detailed worked answer

MCQ question (dict):
    topic   : str
    q       : str -> HTML stem
    svg     : str -> optional inline SVG (or "")
    options : list[str] of length 4 (A,B,C,D content, HTML allowed)
    correct : int -> index 0..3 of the correct option
    ans     : str -> HTML detailed explanation
"""

theory = []   # populated by theory_*.py
mcq = []      # populated by mcq_*.py
PACK_LABEL = ""  # optional badge text, e.g. "Pack 2"; set by a build script

# ---------------------------------------------------------------------------
# Shared CSS
# ---------------------------------------------------------------------------
CSS = """
@page { size: A4; margin: 16mm 15mm 18mm 15mm; }
* { box-sizing: border-box; }
body { font-family: 'Noto Sans', Arial, Helvetica, sans-serif; font-size: 10.5pt;
       color: #1a1a1a; line-height: 1.45; margin: 0; }
h1.title { font-size: 22pt; margin: 0 0 2mm 0; color: #0b3d5c; }
.subtitle { font-size: 11pt; color: #444; margin: 0 0 1mm 0; }
.cover { text-align: center; padding-top: 55mm; page-break-after: always; }
.cover .rule { width: 60%; margin: 6mm auto; border: none; border-top: 2px solid #0b3d5c; }
.cover .meta { font-size: 11pt; color: #333; margin-top: 4mm; }
.cover .badge { display:inline-block; background:#0b3d5c; color:#fff; padding:3px 12px;
       border-radius:14px; font-size:10pt; margin:2mm 2px; }
.topic-head { background: #0b3d5c; color: #fff; padding: 5px 10px; margin: 8mm 0 4mm 0;
       font-size: 13pt; font-weight: bold; border-radius: 3px; page-break-after: avoid;
       page-break-before: always; }
.topic-head.first { page-break-before: avoid; }
.section-banner { border-left: 6px solid #c0392b; background:#faf0ef; padding:8px 12px;
       margin: 4mm 0; font-size: 12pt; font-weight:bold; color:#7b241c; }
.q { page-break-inside: avoid; margin: 0 0 5mm 0; padding: 3mm 0 3mm 0;
     border-bottom: 1px solid #e3e3e3; }
.qnum { font-weight: bold; color: #0b3d5c; }
.marks { float: right; color: #c0392b; font-weight: bold; font-size: 9.5pt; }
.qtext { margin: 1mm 0 2mm 0; }
ol.parts { margin: 1mm 0 1mm 5mm; padding-left: 4mm; }
ol.parts > li { margin: 1.5mm 0; }
ol.romn { list-style-type: lower-roman; margin: 1mm 0 1mm 5mm; }
.opts { margin: 1mm 0 0 4mm; }
.opts .opt { margin: 0.6mm 0; }
.opts .lab { display:inline-block; width: 6mm; font-weight: bold; color:#0b3d5c; }
.ans { background: #f4f9f4; border-left: 4px solid #27794b; padding: 4px 10px;
       margin: 1mm 0; border-radius: 2px; }
.ans .lead { font-weight: bold; color:#1e5c39; }
.correct { font-weight: bold; color:#1e5c39; }
.eq { font-style: italic; }
.eqn { display:block; margin: 1mm 0 1mm 4mm; font-style: italic; }
.note { font-size: 9.5pt; color:#555; }
table.ref { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 2mm 0; }
table.ref th, table.ref td { border: 1px solid #bbb; padding: 3px 6px; text-align: left;
       vertical-align: top; }
table.ref th { background: #eaf1f6; }
table.data { border-collapse: collapse; margin: 2mm 0; font-size: 10pt; }
table.data th, table.data td { border:1px solid #999; padding: 2px 8px; text-align:center; }
table.data th { background:#eef; }
svg { display: block; margin: 2mm auto; }
.figcap { text-align:center; font-size: 9pt; color:#555; margin-top:-1mm; }
.small { font-size: 9pt; }
sub, sup { line-height: 0; }
"""

def frac(a, b):
    return f"<span style='display:inline-block;text-align:center;vertical-align:middle'>" \
           f"<span style='display:block;border-bottom:1px solid #000;padding:0 3px'>{a}</span>" \
           f"<span style='display:block;padding:0 3px'>{b}</span></span>"

# ---------------------------------------------------------------------------
# Math glyphs.  The installed fonts LACK: sqrt, approx, >=, <=, !=, ->, =>,
# proportional, therefore, infinity.  We render each as a tiny inline SVG that
# inherits the current text colour (works inside coloured boxes/headers), or as
# safe CSS.  Author all content using these helpers -- never the raw entities.
# ---------------------------------------------------------------------------
def _sym(inner, vb="0 0 24 24", w="0.80em"):
    return (f"<svg viewBox='{vb}' style='height:{w};width:auto;vertical-align:-0.12em;"
            f"display:inline-block' fill='none' stroke='currentColor' stroke-width='2' "
            f"stroke-linecap='round' stroke-linejoin='round'>{inner}</svg>")

RARR  = _sym("<path d='M3 12 H19'/><path d='M14 7 L20 12 L14 17'/>")
IMPL  = _sym("<path d='M3 9 H16'/><path d='M3 15 H16'/><path d='M13 5 L21 12 L13 19'/>")
APPROX= _sym("<path d='M3 9 q3 -3.2 6 0 t6 0'/><path d='M3 15 q3 -3.2 6 0 t6 0'/>")
GE    = _sym("<path d='M6 4 L18 11 L6 18'/><path d='M6 21 H18'/>", vb="0 0 24 26")
LE    = _sym("<path d='M18 4 L6 11 L18 18'/><path d='M6 21 H18'/>", vb="0 0 24 26")
NE    = _sym("<path d='M4 9 H20'/><path d='M4 15 H20'/><path d='M17 4 L7 20'/>")
PROP  = _sym("<path d='M21 7 C13 4 7 9 11 12 C7 15 13 20 21 17'/><path d='M11 12 H21'/>")

def rt(x):
    """Square root with a proper radical sign + vinculum over the radicand."""
    return ("<span style='white-space:nowrap;'>"
            "<svg viewBox='0 0 12 20' style='height:1em;width:auto;vertical-align:-0.18em;"
            "display:inline-block' fill='none' stroke='currentColor' stroke-width='1.4' "
            "stroke-linecap='round' stroke-linejoin='round'>"
            "<path d='M0 12 L3 12 L6 19 L11 2'/></svg>"
            f"<span style='border-top:1.4px solid currentColor;padding:0 3px;'>{x}</span></span>")

import re
def sanitize(html):
    """Replace entities the installed fonts cannot render with safe SVG glyphs."""
    # square roots (parenthesised radicand, then bare number)
    html = re.sub(r"&radic;\(([^()]+)\)", lambda m: rt(m.group(1)), html)
    html = re.sub(r"&radic;([0-9][0-9.eE]*)", lambda m: rt(m.group(1)), html)
    html = re.sub(r"&radic;([A-Za-z])", lambda m: rt(m.group(1)), html)
    repl = {"&rarr;": RARR, "&rArr;": IMPL, "&asymp;": APPROX, "&ge;": GE,
            "&le;": LE, "&ne;": NE, "&prop;": PROP, "&there4;": IMPL}
    for k, v in repl.items():
        html = html.replace(k, v)
    return html

# ---------------------------------------------------------------------------
# Cover page
# ---------------------------------------------------------------------------
def cover(kind):
    n_theory = len(theory)
    n_mcq = len(mcq)
    total = n_theory + n_mcq
    sub = "Question Paper" if kind == "Q" else "Detailed Answers &amp; Worked Solutions"
    extra = (f"Diagrams included &middot; {n_theory} structured (theory) + {n_mcq} multiple-choice"
             if kind == "Q" else
             "Full method, working and mark-by-mark reasoning for every question")
    return f"""
    <div class="cover">
      <h1 class="title">Cambridge International AS Level</h1>
      <h1 class="title">Physics (9702)</h1>
      <hr class="rule">
      <div class="subtitle"><b>{total} Extreme-Difficulty Practice Questions</b></div>
      <div class="subtitle">{sub}</div>
      <div class="meta">
        {('<span class="badge">' + PACK_LABEL + '</span>') if PACK_LABEL else ''}
        <span class="badge">AS syllabus 2025-2027</span>
        <span class="badge">Target series: Oct / Nov 2026</span>
        <span class="badge">Topics 1&ndash;11</span>
      </div>
      <p class="meta">{extra}</p>
      <p class="meta small">Take <span class="eq">g</span> = 9.81 m s<sup>&minus;2</sup> and
      <span class="eq">c</span> = 3.00 &times; 10<sup>8</sup> m s<sup>&minus;1</sup> unless stated otherwise.</p>
    </div>
    """

# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def _group_by_topic(items):
    order = []
    groups = {}
    for it in items:
        t = it["topic"]
        if t not in groups:
            groups[t] = []
            order.append(t)
        groups[t].append(it)
    return [(t, groups[t]) for t in order]


def render_questions():
    parts = [f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"]
    parts.append(cover("Q"))
    # Reference sheet
    from reference import REFERENCE_HTML
    parts.append(REFERENCE_HTML)

    # Section A: theory
    parts.append(f"<div class='section-banner'>SECTION A &mdash; Structured (theory) questions "
                 f"&nbsp;[Q1&ndash;Q{len(theory)}]</div>")
    n = 0
    first = True
    for topic, items in _group_by_topic(theory):
        cls = "topic-head first" if first else "topic-head"
        first = False
        parts.append(f"<div class='{cls}'>{topic}</div>")
        for it in items:
            n += 1
            parts.append("<div class='q'>")
            parts.append(f"<span class='marks'>[{it['marks']}]</span>")
            parts.append(f"<span class='qnum'>Q{n}.</span> ")
            parts.append(f"<span class='qtext'>{it['q']}</span>")
            if it.get("svg"):
                parts.append(it["svg"])
            parts.append("</div>")
    parts.append(f"<p class='note'>End of Section A &mdash; {n} structured questions.</p>")

    # Section B: MCQ
    parts.append(f"<div class='section-banner'>SECTION B &mdash; Multiple choice "
                 f"&nbsp;[Q1&ndash;Q{len(mcq)}] &nbsp;<span class='small'>(choose one: A, B, C or D)</span></div>")
    m = 0
    first = True
    for topic, items in _group_by_topic(mcq):
        cls = "topic-head first" if first else "topic-head"
        first = False
        parts.append(f"<div class='{cls}'>{topic}</div>")
        for it in items:
            m += 1
            parts.append("<div class='q'>")
            parts.append(f"<span class='qnum'>{m}.</span> ")
            parts.append(f"<span class='qtext'>{it['q']}</span>")
            if it.get("svg"):
                parts.append(it["svg"])
            parts.append("<div class='opts'>")
            for i, opt in enumerate(it["options"]):
                lab = "ABCD"[i]
                parts.append(f"<div class='opt'><span class='lab'>{lab}</span>{opt}</div>")
            parts.append("</div></div>")
    parts.append(f"<p class='note'>End of Section B &mdash; {m} multiple-choice questions.</p>")
    parts.append("</body></html>")
    return sanitize("\n".join(parts))


def render_answers():
    parts = [f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"]
    parts.append(cover("A"))

    parts.append(f"<div class='section-banner'>SECTION A &mdash; Structured (theory) answers "
                 f"&nbsp;[Q1&ndash;Q{len(theory)}]</div>")
    n = 0
    first = True
    for topic, items in _group_by_topic(theory):
        cls = "topic-head first" if first else "topic-head"
        first = False
        parts.append(f"<div class='{cls}'>{topic}</div>")
        for it in items:
            n += 1
            parts.append("<div class='q'>")
            parts.append(f"<span class='marks'>[{it['marks']}]</span>")
            parts.append(f"<span class='qnum'>Q{n}.</span> ")
            parts.append(f"<span class='qtext'>{it['q']}</span>")
            if it.get("svg"):
                parts.append(it["svg"])
            parts.append(f"<div class='ans'><span class='lead'>Answer.</span> {it['ans']}</div>")
            parts.append("</div>")

    parts.append(f"<div class='section-banner'>SECTION B &mdash; Multiple choice answers "
                 f"&nbsp;[Q1&ndash;Q{len(mcq)}]</div>")
    m = 0
    first = True
    for topic, items in _group_by_topic(mcq):
        cls = "topic-head first" if first else "topic-head"
        first = False
        parts.append(f"<div class='{cls}'>{topic}</div>")
        for it in items:
            m += 1
            lab = "ABCD"[it["correct"]]
            parts.append("<div class='q'>")
            parts.append(f"<span class='qnum'>{m}.</span> ")
            parts.append(f"<span class='qtext'>{it['q']}</span>")
            if it.get("svg"):
                parts.append(it["svg"])
            parts.append("<div class='opts'>")
            for i, opt in enumerate(it["options"]):
                l = "ABCD"[i]
                cls2 = " class='correct'" if i == it["correct"] else ""
                parts.append(f"<div class='opt'><span class='lab'>{l}</span><span{cls2}>{opt}</span></div>")
            parts.append("</div>")
            parts.append(f"<div class='ans'><span class='lead'>Correct: {lab}.</span> {it['ans']}</div>")
            parts.append("</div>")
    parts.append("</body></html>")
    return sanitize("\n".join(parts))
