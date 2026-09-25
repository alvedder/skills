#!/usr/bin/env python3
"""humanize-lint - deterministic style and character checks for prose.

Reports pattern matches for contextual review. See ../LINT.md for interpretation
and coverage limits; these checks cannot establish authorship or fidelity.

Usage:
    python3 humanize_lint.py DRAFT.md
    python3 humanize_lint.py DRAFT.md --source NOTES.md
    python3 humanize_lint.py docs/
    python3 humanize_lint.py DRAFT.md --ignore CLICHE,BULLETS

Exit 0 = no findings under selected checks. Exit 1 = findings or no input files.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

CODES = [
    "DASH", "QUOTE", "SHORTHAND", "INVISIBLE", "HOMOGLYPH",
    "PLACEHOLDER", "CLICHE", "META", "PARALLEL", "BULLETS", "BLOAT",
]

# --------------------------------------------------------------- character sets

DASHES = {
    "\u2010": "HYPHEN",
    "\u2011": "NON-BREAKING HYPHEN",
    "\u2012": "FIGURE DASH",
    "\u2013": "EN DASH",
    "\u2014": "EM DASH",
    "\u2015": "HORIZONTAL BAR",
    "\u2212": "MINUS SIGN",
    "\u2e3a": "TWO-EM DASH",
    "\u2e3b": "THREE-EM DASH",
    "\ufe58": "SMALL EM DASH",
    "\ufe63": "SMALL HYPHEN-MINUS",
    "\uff0d": "FULLWIDTH HYPHEN-MINUS",
}

QUOTES = {
    "\u2018": "LEFT SINGLE QUOTE",
    "\u2019": "RIGHT SINGLE QUOTE",
    "\u201a": "LOW-9 SINGLE QUOTE",
    "\u201b": "REVERSED-9 SINGLE QUOTE",
    "\u201c": "LEFT DOUBLE QUOTE",
    "\u201d": "RIGHT DOUBLE QUOTE",
    "\u201e": "LOW-9 DOUBLE QUOTE",
    "\u201f": "REVERSED-9 DOUBLE QUOTE",
    "\u2032": "PRIME",
    "\u2033": "DOUBLE PRIME",
    "\u00ab": "LEFT GUILLEMET",
    "\u00bb": "RIGHT GUILLEMET",
    "\u2039": "LEFT SINGLE GUILLEMET",
    "\u203a": "RIGHT SINGLE GUILLEMET",
}

# Shorthand characters that may need expansion for the intended reader.
SHORTHAND = {
    "\u2026": "ELLIPSIS (write three periods, or end the sentence)",
    "\u00b7": "MIDDLE DOT (fragment glue)",
    "\u2022": "BULLET CHARACTER (use a hyphen list)",
    "\u2043": "HYPHEN BULLET",
    "\u2192": "RIGHT ARROW (name the relation in words)",
    "\u21d2": "DOUBLE RIGHT ARROW",
    "\u27f6": "LONG RIGHT ARROW",
}

# Invisible characters, including controls needed by some writing systems.
INVISIBLE = {
    "\u00ad": "SOFT HYPHEN",
    "\u061c": "ARABIC LETTER MARK",
    "\u180e": "MONGOLIAN VOWEL SEPARATOR",
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\u200e": "LEFT-TO-RIGHT MARK",
    "\u200f": "RIGHT-TO-LEFT MARK",
    "\u2060": "WORD JOINER",
    "\ufeff": "ZERO WIDTH NO-BREAK SPACE",
}
INVISIBLE.update({chr(c): "INVISIBLE OPERATOR" for c in range(0x2061, 0x2065)})
INVISIBLE.update({chr(c): "BIDI CONTROL" for c in range(0x202A, 0x202F)})
INVISIBLE.update({chr(c): "BIDI ISOLATE" for c in range(0x2066, 0x206A)})
INVISIBLE.update({chr(c): "TAG CHARACTER" for c in range(0xE0000, 0xE0080)})
INVISIBLE.update({chr(c): "EXOTIC SPACE" for c in
                  list(range(0x2000, 0x200B)) + [0x00A0, 0x202F, 0x205F, 0x3000]})

# --------------------------------------------------------------------- patterns

_CYR_GRK = "\u0400-\u04FF\u0370-\u03FF"
HOMOGLYPH = re.compile(f"[A-Za-z][{_CYR_GRK}]|[{_CYR_GRK}][A-Za-z]")
WORD = re.compile(r"[^\W\d_]+(?:[-'][^\W\d_]+)*", re.UNICODE)

PLACEHOLDER_CS = re.compile(r"\bTODO\b|\bFIXME\b|\bTBD\b|\bXXX\b|\$[A-Z]\b|<[A-Z][a-zA-Z ]{1,28}>")
PLACEHOLDER_CI = re.compile(
    r"\blorem ipsum\b"
    r"|\[(?:insert|your|placeholder|todo|name here|company)[^\]]{0,40}\]"
    r"|\b(?:insert|add)\s+(?:your\s+)?(?:name|text|details)\s+here\b",
    re.I,
)

# Lexical review cues; matches can have legitimate meanings in context.
CLICHES = [
    r"\bdelv(?:e|es|ing|ed)\s+into\b",
    r"\bit(?:'s|\s+is)\s+worth\s+noting\b",
    r"\bit\s+is\s+important\s+to\s+note\b",
    r"\bimportant\s+to\s+note\s+that\b",
    r"\bin\s+today'?s\s+(?:fast[- ]paced|digital|modern|competitive)\b",
    r"\bever[- ](?:evolving|changing|growing)\b",
    r"\btapestry\b",
    r"\ba\s+testament\s+to\b",
    r"\bunderscor(?:e|es|ing|ed)\s+the\s+(?:importance|need|significance)\b",
    r"\bplays?\s+a\s+(?:crucial|vital|key|pivotal|significant)\s+role\b",
    r"\bat\s+the\s+end\s+of\s+the\s+day\b",
    r"\bunlock(?:ing)?\s+the\s+(?:full\s+)?potential\b",
    r"\bharness(?:ing)?\s+the\s+power\b",
    r"\bseamless(?:ly)?\b",
    r"\bgame[- ]chang(?:er|ing)\b",
    r"\bcutting[- ]edge\b",
    r"\bstate[- ]of[- ]the[- ]art\b",
    r"\bin\s+conclusion\b",
    r"\bdeep\s+dive\b",
    r"\bdiv(?:e|ing)\s+deep(?:er)?\s+into\b",
    r"\belevat(?:e|es|ing)\s+your\b",
    r"\bembark(?:ing|s)?\s+on\b",
    r"\bthe\s+realm\s+of\b",
    r"\bmyriad\s+of\b",
    r"\bplethora\s+of\b",
    r"\bmeticulous(?:ly)?\b",
    r"\bparamount\b",
    r"\bnavigat(?:e|es|ing)\s+the\s+(?:complex|complexities|landscape|world)\b",
    r"\blandscape\s+of\s+(?:modern|today)",
    r"\bleverag(?:e|es|ing|ed)\b",
    r"\butiliz(?:e|es|ing|ed)\b",
    r"\bfacilitat(?:e|es|ing|ed)\b",
    r"\brobust\s+(?:solution|framework|approach|system|platform)\b",
    r"\bcomprehensive\s+(?:guide|overview|solution|approach|understanding)\b",
    r"\bwhen\s+it\s+comes\s+to\b",
    r"\b(?:furthermore|moreover)\b",
    r"\bcrucial\b",
    r"\bvital\b",
    r"\bpivotal\b",
]
CLICHE_RE = re.compile("|".join(CLICHES), re.I)

# Framing that may be removable when it adds no content.
META = [
    r"^\s*(?:great|excellent|good)\s+question\b",
    r"^\s*(?:certainly|absolutely|sure)\s*[!,.]",
    r"\bI\s+hope\s+this\s+helps\b",
    r"\blet\s+me\s+know\s+if\s+you\s+(?:have|need|want|'d)\b",
    r"\bfeel\s+free\s+to\s+(?:ask|reach)\b",
    r"^\s*here(?:'s|\s+is)\s+(?:a|an|the)\s+(?:summary|overview|breakdown|rundown)\b",
    r"\bas\s+an\s+AI\b",
    r"\b(?:in\s+summary|to\s+summarize|to\s+sum\s+up)\b",
    r"^\s*overall\s*,",
    r"\bI\s+(?:will|'ll)\s+now\s+(?:explain|describe|walk)\b",
]
META_RE = re.compile("|".join(META), re.I | re.M)

# "not just X but Y" and "it's not X, it's Y". One is rhetoric, several is a tic.
PARALLEL_RE = re.compile(
    r"\bnot\s+(?:just|only|merely|simply)\b[^.!?\n]{0,80}?\bbut\b"
    r"|\bit(?:'s|\s+is)\s+not\s+(?:about\s+)?\w+[^.!?\n]{0,60}?,\s*it(?:'s|\s+is)\b",
    re.I,
)

BULLET_LINE = re.compile(r"^\s{0,8}(?:[-*+]\s|\d+[.)]\s)")

# ------------------------------------------------------------------- extraction

FENCE_RE = re.compile(r"^[ \t]*(?:```|~~~).*?(?:^[ \t]*(?:```|~~~)|\Z)", re.S | re.M)
INDENT_CODE_RE = re.compile(r"^(?: {4}|\t).*$", re.M)
INLINE_RE = re.compile(r"`[^`\n]*`")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
URL_RE = re.compile(r"<?https?://\S+|\]\([^)\n]*\)")


def _blank(match: re.Match) -> str:
    """Replace a match with spaces, keeping newlines so offsets stay truthful."""
    return re.sub(r"[^\n]", " ", match.group(0))


def mask(text: str) -> str:
    """Mask recognized non-prose spans, preserving every character offset."""
    for pattern in (COMMENT_RE, FENCE_RE, INLINE_RE, URL_RE):
        text = pattern.sub(_blank, text)
    return text


def line_col(text: str, idx: int) -> tuple[int, int]:
    return text.count("\n", 0, idx) + 1, idx - text.rfind("\n", 0, idx)


# ----------------------------------------------------------------------- checks

def _chars(prose, table, code, out):
    for idx, ch in enumerate(prose):
        name = table.get(ch)
        if name:
            out.append((idx, code, f"{name} (U+{ord(ch):04X})"))


def check(text: str, args) -> tuple[list, int]:
    """Return (findings, word_count). Findings are (index, code, message)."""
    prose = mask(text)
    words = len(re.findall(r"\S+", prose))
    out: list[tuple[int, str, str]] = []

    _chars(prose, DASHES, "DASH", out)
    _chars(prose, QUOTES, "QUOTE", out)
    _chars(prose, SHORTHAND, "SHORTHAND", out)
    _chars(prose, INVISIBLE, "INVISIBLE", out)

    for m in WORD.finditer(prose):
        token = m.group(0)
        if "-" not in token and HOMOGLYPH.search(token):
            out.append((m.start(), "HOMOGLYPH", f"mixed scripts in one word: {token!r}"))

    for rx in (PLACEHOLDER_CS, PLACEHOLDER_CI):
        for m in rx.finditer(prose):
            out.append((m.start(), "PLACEHOLDER", f"possible placeholder: {m.group(0)!r}"))

    for m in CLICHE_RE.finditer(prose):
        out.append((m.start(), "CLICHE", f"phrase to review in context: {m.group(0).strip()!r}"))

    for m in META_RE.finditer(prose):
        out.append((m.start(), "META", f"possible framing to review: {m.group(0).strip()!r}"))

    hits = list(PARALLEL_RE.finditer(prose))
    if len(hits) > args.max_parallel:
        for m in hits[args.max_parallel:]:
            out.append((m.start(), "PARALLEL",
                        f"'not just X but Y' used {len(hits)} times, "
                        f"limit {args.max_parallel}: {m.group(0).strip()!r}"))

    content = bullets = 0
    for line in prose.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "|", ">")):
            continue
        content += 1
        if BULLET_LINE.match(line):
            bullets += 1
    if content >= args.min_lines and bullets / content > args.max_bullet_ratio:
        out.append((0, "BULLETS",
                    f"{bullets} of {content} prose lines are list items "
                    f"({bullets / content:.0%}, limit {args.max_bullet_ratio:.0%}). "
                    "Review whether the list structure suits the content."))

    out.sort(key=lambda f: (f[0], f[1]))
    return out, words


def source_words(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        return len(re.findall(r"\S+", mask(fh.read())))


# ------------------------------------------------------------------------- main

def targets(path: str) -> list[str]:
    if os.path.isfile(path):
        return [path]
    found = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        found += [os.path.join(root, f) for f in sorted(files)
                  if f.endswith((".md", ".txt"))]
    return found


def run(path: str, args, ignore: set[str]) -> int:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    findings, words = check(text, args)

    if args.source:
        allowed = source_words(args.source) * args.max_inflation
        if words > allowed:
            findings.append((0, "BLOAT",
                             f"{words} words against a {allowed:.0f} word threshold "
                             f"({args.max_inflation}x the source). Review whether the expansion is needed."))

    findings = [f for f in findings if f[1] not in ignore]
    if not findings:
        print(f"clean  {path}  ({words} words)")
        return 0

    print(f"FAIL   {path}  ({len(findings)} findings, {words} words)")
    for idx, code, message in findings[:args.max_report]:
        line, col = line_col(text, idx)
        print(f"  {line}:{col}  [{code}] {message}")
    if len(findings) > args.max_report:
        print(f"  ... {len(findings) - args.max_report} more")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", help="file or directory of .md and .txt")
    ap.add_argument("--source", help="original draft, to check inflation against")
    ap.add_argument("--max-inflation", type=float, default=1.4)
    ap.add_argument("--max-parallel", type=int, default=1)
    ap.add_argument("--max-bullet-ratio", type=float, default=0.5)
    ap.add_argument("--min-lines", type=int, default=12,
                    help="skip the bullet check on documents shorter than this")
    ap.add_argument("--max-report", type=int, default=40)
    ap.add_argument("--ignore", default="",
                    help="comma-separated codes to skip: " + ", ".join(CODES))
    args = ap.parse_args()

    ignore = {c.strip().upper() for c in args.ignore.split(",") if c.strip()}
    unknown = ignore - set(CODES)
    if unknown:
        ap.error(f"unknown code(s): {', '.join(sorted(unknown))}")

    files = targets(args.path)
    if not files:
        print(f"nothing to check at {args.path}", file=sys.stderr)
        return 1
    return max(run(f, args, ignore) for f in files)


if __name__ == "__main__":
    sys.exit(main())
