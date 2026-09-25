# Interpreting lint

The linter finds configured text patterns and characters. Its output establishes what
matched, not authorship, factual accuracy or writing quality. Run it on the deliverable;
linting this skill's fenced examples does not test their rewrites.

## Choose the scope

Run commands from the skill directory and pass absolute paths to drafts stored elsewhere.
Use `python3 scripts/humanize_lint.py --help` for supported inputs, codes and thresholds.

When comparing a rewrite's length with the original, add `--source` with the original file
path. The ratio is a review cue: terse notes may need expansion, while a long source may
still need shortening. The reader's needs and any requested length limit decide the budget.

## Resolve findings

Read each match in context and correct applicable findings. Keep a justified match when
changing it would damage fidelity, the language or the requested format:

- **Wording and structure:** a lexical match may be a precise term; a high list ratio may
  be an appropriate checklist. Judge the passage's purpose.
- **Punctuation and scripts:** quoted text, mathematical notation, multilingual words and
  writing-system controls may be intentional. Preserve them when they carry meaning;
  remove accidental artifacts only after checking their role.
- **Placeholders:** fill a missing value from supplied evidence, or state that it remains
  unknown. Preserve intentional template slots when a template is the requested output.

Use `--ignore` only for categories that do not apply to the document's requirements, after
reviewing their matches. For individual exceptions, retain the finding and its reason in
working notes; a category-wide ignore can hide other matches. Keep the notes separate from
the rewritten text unless the user requests a review report.

Exit 0 means no findings under the selected checks; exit 1 means findings or no input files.
Other execution errors require checking the diagnostic. Apply the completion criterion
in SKILL.md; the exit code alone does not decide whether the text is ready.

## Coverage limits

The script masks fenced code, simple inline code, URLs, Markdown link targets and HTML
comments. It uses regular expressions rather than a full Markdown parser: indented code,
complex markup and quotations may still be scanned. Preserve their contents during review.

Word counts are whitespace-based and exclude masked spans. Phrase checks target English;
character checks can also flag valid text in other languages. Review unsupported formats
directly. A clean exit cannot establish that claims, tone or reasoning survived the rewrite.
