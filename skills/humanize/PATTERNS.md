# Editing patterns

Use these repairs when a passage feels formulaic. Choose the repair that addresses the
reading problem; a matched word or sentence shape is only a cue to inspect its context.

## Concrete wording

Replace an inflated verb with the action it names. Retain a technical term when it carries
the intended meaning, such as leverage in a financial discussion.

```text
Before: We should leverage the existing pipeline to facilitate delivery.
After: We should use the existing pipeline to help deliver the work.
```

For an empty adjective, use its supporting detail if supplied. If the adjective is itself
a substantive claim, preserve it or flag the missing support rather than quietly deleting
the claim or inventing a measurement.

```text
Before: Retry support is a crucial feature: it lets failed uploads resume.
After: Retry support is essential because it lets failed uploads resume.
```

## Real connections

Replace a transition with the relationship already present in the source. When that
relationship is unknown, let the observations remain separate.

```text
Before: During the test, latency rose. Furthermore, the cache was cold throughout. The cause is unknown.
After: During the test, latency rose while the cache was cold. The cause is unknown.
```

Keep uncertainty attached to the claim it qualifies. Compress redundant hedges without
changing a possibility into a prediction.

```text
Before: This may potentially be able to improve throughput.
After: This may improve throughput.
```

## Useful structure

Repeated contrasts or uniform sentence shapes can obscure the point. State it directly
where the emphasis survives the edit; preserve parallel structure that helps comparison.

```text
Before: It is not just slow, but unreliable. Delivery is not only late, but over budget.
After: It is slow and unreliable. Delivery is late and over budget.
```

Turn fragments into prose when the reader needs to follow an argument. Keep separate
facts scannable when comparison is the task; a list or table may already be the right form.

```text
Before: **Speed:** improved. **Cost:** unchanged. **Risk:** moderate.
After: Speed improved and cost stayed the same. Risk is moderate.
```

Name headings for their content. An ending earns its place by adding an action,
qualification or unresolved issue; a restatement can usually be cut. For a section
explaining a supplied rollback recommendation:

```text
Before: ## Key Takeaways
After: ## Why rollback is recommended
```

## Appropriate register

In a rewrite, remove framing that merely announces the requested text. Preserve greetings,
thanks or conversational warmth when they belong to the author's message and audience.

```text
Before: Here is a summary of the test result: the auth test failed.
After: The auth test failed.
```

For punctuation, invisible characters or suspicious script mixing, use
[LINT.md](LINT.md) to interpret the diagnostic before changing the text.
