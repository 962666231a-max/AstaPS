#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit quest coverage: which condition/exec types used by the quest table can never fire.

A type is reachable only if BOTH:
  * an enum constant with that name exists (enums/QuestContent.java, enums/QuestExec.java), and
  * a handler annotated with @QuestValue*(<type>) exists under game/quest/content|exec.

Covered = reachable. Everything else is a step that can never complete.

Usage:
    python tools/quest-coverage-audit.py <resources dir> [--src <repo root>] [--json out.json]

Reads   <resources>/ExcelBinOutput/QuestExcelConfigData.json
Writes  JSON: totals + per-type rows/subquests/examples for the uncovered types.
"""
import collections
import json
import os
import re
import sys


def enum_names(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return set(re.findall(r"\b(QUEST_(?:CONTENT|EXEC)_[A-Z0-9_]+)\b", f.read()))


def handler_names(quest_dir):
    content, exe = set(), set()
    for root, _dirs, files in os.walk(quest_dir):
        for name in files:
            if not name.endswith(".java"):
                continue
            with open(os.path.join(root, name), encoding="utf-8", errors="ignore") as f:
                text = f.read()
            content |= set(
                re.findall(r"@QuestValue(?:Content|Cond)\([^)]*?(QUEST_CONTENT_[A-Z0-9_]+)", text)
            )
            exe |= set(re.findall(r"@QuestValueExec\([^)]*?(QUEST_EXEC_[A-Z0-9_]+)", text))
    return content, exe


def collect(rows, fields):
    count = collections.Counter()
    subs = collections.defaultdict(set)
    examples = collections.defaultdict(list)
    for quest in rows:
        for field in fields:
            for item in quest.get(field) or []:
                t = item.get("type")
                if not t:
                    continue
                count[t] += 1
                subs[t].add(quest.get("subId"))
                if len(examples[t]) < 2:
                    examples[t].append(
                        {
                            "subId": quest.get("subId"),
                            "mainId": quest.get("mainId"),
                            "field": field,
                            "param": item.get("param"),
                        }
                    )
    return count, subs, examples


def gaps(count, subs, examples, enums, handlers, kind):
    out = []
    for t, n in count.most_common():
        if t in enums and t in handlers:
            continue
        out.append(
            {
                "type": t,
                "kind": kind,
                "rows": n,
                "subquests": len(subs[t]),
                "missing": ("enum" if t not in enums else "")
                + ("+handler" if t not in handlers else ""),
                "examples": examples[t],
            }
        )
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    res = sys.argv[1]
    src = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    if "--src" in sys.argv:
        src = sys.argv[sys.argv.index("--src") + 1]
    out_path = None
    if "--json" in sys.argv:
        out_path = sys.argv[sys.argv.index("--json") + 1]

    table = os.path.join(res, "ExcelBinOutput", "QuestExcelConfigData.json")
    if not os.path.exists(table):
        print("not found:", table)
        return 2
    with open(table, encoding="utf-8", errors="ignore") as f:
        rows = json.load(f)

    quest_dir = os.path.join(src, "src", "main", "java", "emu", "grasscutter", "game", "quest")
    enum_c = enum_names(os.path.join(quest_dir, "enums", "QuestContent.java"))
    enum_e = enum_names(os.path.join(quest_dir, "enums", "QuestExec.java"))
    handler_c, handler_e = handler_names(quest_dir)

    c_count, c_subs, c_ex = collect(rows, ("finishCond", "failCond"))
    e_count, e_subs, e_ex = collect(rows, ("beginExec", "finishExec", "failExec"))

    report = {
        "sample": {"quest_table": table, "quest_rows": len(rows)},
        "conditions": {
            "total_rows": sum(c_count.values()),
            "total_types": len(c_count),
            "uncovered": gaps(c_count, c_subs, c_ex, enum_c, handler_c, "condition"),
        },
        "execs": {
            "total_rows": sum(e_count.values()),
            "total_types": len(e_count),
            "uncovered": gaps(e_count, e_subs, e_ex, enum_e, handler_e, "exec"),
        },
    }
    for key in ("conditions", "execs"):
        block = report[key]
        block["uncovered_rows"] = sum(r["rows"] for r in block["uncovered"])
        block["uncovered_types"] = len(block["uncovered"])
        block["covered_pct"] = round(
            100.0 * (block["total_rows"] - block["uncovered_rows"]) / block["total_rows"], 1
        )

    text = json.dumps(report, ensure_ascii=False, indent=2)
    if out_path:
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
        print("written", out_path)
    else:
        print(text)

    print(
        "conditions: %d/%d rows reachable (%.1f%%), %d types missing"
        % (
            report["conditions"]["total_rows"] - report["conditions"]["uncovered_rows"],
            report["conditions"]["total_rows"],
            report["conditions"]["covered_pct"],
            report["conditions"]["uncovered_types"],
        )
    )
    print(
        "execs:      %d/%d rows reachable (%.1f%%), %d types missing"
        % (
            report["execs"]["total_rows"] - report["execs"]["uncovered_rows"],
            report["execs"]["total_rows"],
            report["execs"]["covered_pct"],
            report["execs"]["uncovered_types"],
        )
    )
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
