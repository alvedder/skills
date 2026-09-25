#!/usr/bin/env python3
"""Tests for humanize_lint. Runs standalone, no test framework required.

    python3 test_humanize_lint.py

Also collectable by pytest if it happens to be installed.
"""
import argparse
import sys

import humanize_lint as lint

DEFAULTS = dict(max_parallel=1, max_bullet_ratio=0.5, min_lines=12)


def codes(text, **over):
    args = argparse.Namespace(**{**DEFAULTS, **over})
    return [c for _, c, _ in lint.check(text, args)[0]]


def test_clean_prose_passes():
    text = ("The deploy failed on the auth test. Nothing else in the suite is red, "
            "so the change is contained to that one path.")
    assert codes(text) == []


def test_em_dash_is_caught():
    assert "DASH" in codes("The number moved \u2014 and that matters.")


def test_curly_quotes_are_caught():
    assert "QUOTE" in codes("He called it \u201cfinished\u201d yesterday.")
    assert "QUOTE" in codes("That is the team\u2019s call.")


def test_plain_punctuation_passes():
    assert codes("He called it \"finished\" - the team's call, not ours.") == []


def test_invisible_characters_are_caught():
    assert "INVISIBLE" in codes("Revenue\u200b held flat this month.")
    assert "INVISIBLE" in codes("Revenue\u00a0held flat this month.")


def test_shorthand_is_caught():
    assert "SHORTHAND" in codes("Signups went 4 \u2192 3 \u2192 0 over three weeks.")
    assert "SHORTHAND" in codes("Fast \u00b7 cheap \u00b7 correct.")


def test_homoglyph_is_caught():
    assert "HOMOGLYPH" in codes("The \u0441ustomer never replied.")


def test_hyphen_compound_is_not_a_homoglyph():
    assert "HOMOGLYPH" not in codes("The trust-\u043c\u043e\u0434\u0435\u043b\u044c held.")


def test_placeholders_are_caught():
    assert "PLACEHOLDER" in codes("Ship by TODO once review clears.")
    assert "PLACEHOLDER" in codes("Send it to <Name> before Friday.")
    assert "PLACEHOLDER" in codes("Budget is $X for the quarter.")


def test_cliches_are_caught():
    assert "CLICHE" in codes("Let us delve into the numbers.")
    assert "CLICHE" in codes("This is a crucial step for the team.")
    assert "CLICHE" in codes("We should leverage the existing pipeline.")


def test_meta_framing_is_caught():
    assert "META" in codes("Great question! The answer is yes.")
    assert "META" in codes("The answer is yes. I hope this helps.")
    assert "META" in codes("In summary, the migration held.")


def test_one_parallel_is_allowed_two_is_not():
    one = "This is not just slow, but wrong."
    assert "PARALLEL" not in codes(one)
    assert "PARALLEL" in codes(one + " It is not only late, but unreviewed.")


def test_bullet_heavy_document_is_caught():
    text = "Findings follow.\n\n" + "\n".join(f"- item number {i}" for i in range(14))
    assert "BULLETS" in codes(text)


def test_short_document_skips_bullet_check():
    text = "Findings follow.\n\n" + "\n".join(f"- item number {i}" for i in range(4))
    assert "BULLETS" not in codes(text)


def test_code_blocks_are_exempt():
    text = "Banned characters look like this:\n\n```\nem dash \u2014 curly \u201cquote\u201d\n```\n"
    assert codes(text) == []


def test_inline_code_is_exempt():
    assert codes("The em-dash character is `\u2014` and it is banned.") == []


def test_urls_are_exempt():
    assert codes("See https://example.com/a\u2014b for the raw table.") == []


def test_offsets_survive_masking():
    text = "line one\n`\u2014`\nthe \u2014 is on line three\n"
    findings, _ = lint.check(text, argparse.Namespace(**DEFAULTS))
    assert len(findings) == 1
    assert lint.line_col(text, findings[0][0])[0] == 3


def main():
    tests = [(n, f) for n, f in sorted(globals().items())
             if n.startswith("test_") and callable(f)]
    failed = []
    for name, fn in tests:
        try:
            fn()
        except AssertionError:
            failed.append(name)
            print(f"FAIL  {name}")
    print(f"\n{len(tests) - len(failed)}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
