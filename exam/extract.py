# -*- coding: utf-8 -*-
"""Extract all questions (Pack 1 + Pack 2, theory + MCQ) into a single JSON file
that the browser tutor (tutor.html) embeds. Preserves pack, topic, type, marks,
options, correct answer, worked solution and any inline SVG diagram."""
import os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import engine


def snapshot(theory_items, mcq_items, pack):
    out = []
    for i, it in enumerate(theory_items, 1):
        out.append({
            "id": f"{pack}-T{i}",
            "pack": pack,
            "type": "theory",
            "num": i,
            "topic": it["topic"],
            "q": it["q"],
            "svg": it.get("svg", ""),
            "marks": it.get("marks"),
            "ans": it["ans"],
        })
    for i, it in enumerate(mcq_items, 1):
        out.append({
            "id": f"{pack}-M{i}",
            "pack": pack,
            "type": "mcq",
            "num": i,
            "topic": it["topic"],
            "q": it["q"],
            "svg": it.get("svg", ""),
            "options": it["options"],
            "correct": it["correct"],
            "ans": it["ans"],
        })
    return out


all_questions = []

# ---- Pack 1 -------------------------------------------------------------
import reference          # noqa
import theory_01_10       # noqa
import theory_extra       # noqa
import mcq_all            # noqa
import mcq_extra          # noqa

all_questions += snapshot(list(engine.theory), list(engine.mcq), "Pack 1")
p1_t, p1_m = len(engine.theory), len(engine.mcq)

# ---- reset shared lists, then Pack 2 -----------------------------------
engine.theory.clear()
engine.mcq.clear()

import theory_pack2_1     # noqa
import theory_pack2_2     # noqa
import theory_pack2_3     # noqa
import mcq_pack2_1        # noqa
import mcq_pack2_2        # noqa

all_questions += snapshot(list(engine.theory), list(engine.mcq), "Pack 2")
p2_t, p2_m = len(engine.theory), len(engine.mcq)

from reference import REFERENCE_HTML

payload = {"reference": REFERENCE_HTML, "questions": all_questions}

out_path = os.path.join(HERE, "questions.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=1)

print(f"Pack 1: {p1_t} theory + {p1_m} MCQ")
print(f"Pack 2: {p2_t} theory + {p2_m} MCQ")
print(f"TOTAL : {len(all_questions)} questions -> {out_path}")
