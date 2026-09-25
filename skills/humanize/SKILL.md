---
name: humanize
description: Humanize drafts when compressed prose or formulaic phrasing obscures the point. Also use when checking reader-facing text for style or character-level issues.
---

# Humanize

Make the point easier to read with the smallest useful edit. The user's audience, voice,
length and format govern the rewrite, including requests for terse or technical prose.

## Workflow

1. **Frame.** Establish the reader, purpose and destination from the request and source.
   Ask only when a missing detail would materially change the rewrite; otherwise use the
   source's language and register. Proceed once all three are specified or inferred.
2. **Edit.** Apply Fidelity and Readability below. For a passage that still feels
   formulaic, consult [PATTERNS.md](PATTERNS.md). When choosing how much to change in an
   alert, dense notes or uncertain findings, consult [EXAMPLES.md](EXAMPLES.md).
   Finish when every passage has been checked against Readability and the needed edits
   are made; already effective text can stay unchanged.
3. **Verify.** Compare the entire draft with the source against Fidelity, then read it in
   the destination's format. Run the bundled linter on the exact final text, using a
   temporary file for chat output. From this skill's directory:

   ```bash
   python3 scripts/humanize_lint.py /absolute/path/to/draft.md
   ```

   For source-length comparison, format exceptions or findings, read [LINT.md](LINT.md).
   Finish when the source comparison passes and every finding is corrected or justified
   by the content or requested style. Recheck changed text. If execution is unavailable,
   disclose that verification gap rather than claiming a lint pass.

For a rewrite, return the text alone unless the user requests explanation. For a review,
return actionable findings and any requested revision. Keep validation notes out of the
deliverable except when a verification gap must be disclosed.

## Fidelity

- Preserve numbers and their units, dates, named entities, identifiers, quotations and
  links. Keep their exact form unless the user requests a conversion or correction.
- Preserve each claim's scope, attribution, uncertainty and causal strength. Keep
  recommendations with their original force, owners, counts and deadlines.
- Connect facts only through relationships supported by the source. Add calculations,
  explanations of significance or new inferences only when the requested task includes
  them; distinguish additions from source claims.
- Keep unknowns visible. Retain an undefined label or ambiguous value, or flag the missing
  context when it prevents a faithful rewrite. Supply specifics only from available evidence.

## Readability

- **Lede:** start with the action or finding the reader needs, then its explanation.
- **Context:** explain unfamiliar terms at first use when their meaning is established
  and the reader needs it. Expert shorthand can remain compact.
- **Structure:** use paragraphs for reasoning, lists for parallel items or steps, and
  tables for comparisons or lookups. Preserve a requested structure.
- **Diction:** replace empty abstractions with supported concrete wording. Use active
  voice when the actor is known; retain passive voice when ownership is unknown.
- **Economy:** remove repetition and ceremonial framing. Add only context needed to
  understand the point; a short alert stays short. End on the last substantive point.
- **Presentation:** match the destination's renderer. Use plain keyboard punctuation in
  new prose unless the language, requested style or notation calls for another form.
  Make identifiers clickable when a verified target is available.
