---
name: consult-cursor-agent
description: 'User-invoked, read-only Cursor consultation for an independent second opinion. Explicitly use when Codex, Claude Code, Hermes, or another non-Cursor agent needs to resolve a controversial design, debugging, architecture, security, or trade-off question through evidence and rebuttal; do not use it to delegate implementation.'
---

# Consult Cursor Agent

Get an independent, evidence-backed Cursor view. The calling agent owns the decision, changes, and verification.

## Consult

This invocation authorizes Cursor to inspect in-scope workspace code and architecture. Start one read-only chat:

```bash
chat_id="$(cursor-agent create-chat)"
cursor-agent --trust --resume "$chat_id" --mode ask --print \
  --output-format text --workspace "$PWD" "<consultation prompt>"
```

Give Cursor a precise question and the relevant evidence:

```text
Act as an independent, read-only engineering consultant. Inspect relevant workspace code.
Do not modify files, run mutating commands, or read/expose secrets.

Question: <decision to make>
Evidence: <paths, tests, logs, constraints, competing positions>

Return: recommendation; evidence and uncertainty; strongest counterargument;
confidence; smallest validating check.
```

Verify material claims yourself. For a real disagreement, send only the new evidence and rebuttal through the same `chat_id`; ask Cursor to revise or defend its conclusion. Stop when evidence decides the issue or the remainder is a user product/policy choice.

Never leave Ask mode, add `--force`/`--yolo`, or ask Cursor to implement. Do not intentionally provide credentials, keys, tokens, or `.env` content.
