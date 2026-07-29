# -*- coding: utf-8 -*-
"""Inject questions.json into tutor_template.html to produce a single,
self-contained tutor.html that runs offline from file:// in any browser."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "questions.json"), encoding="utf-8") as f:
    data = f.read()

# Validate it is JSON.
parsed = json.loads(data)
n = len(parsed["questions"])

# Escape sequences that would prematurely close the <script> tag.
safe = data.replace("</", "<\\/")

with open(os.path.join(HERE, "tutor_template.html"), encoding="utf-8") as f:
    tmpl = f.read()

out = tmpl.replace("__DATA__", safe)

out_path = os.path.join(HERE, "tutor.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(out)

kb = os.path.getsize(out_path) / 1024
print(f"Embedded {n} questions -> {out_path} ({kb:.0f} KB)")
