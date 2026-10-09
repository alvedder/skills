---
name: consult-hermes-agent
description: 'User-invoked, read-only Hermes consultation for an independent second opinion. Explicitly use when Codex, Claude Code, Cursor, or another non-Hermes agent needs to resolve a controversial design, debugging, architecture, security, or trade-off question through evidence and rebuttal; do not use it to delegate implementation.'
---

# Consult Hermes Agent

Get an independent, evidence-backed Hermes view. The calling agent owns the decision, changes, and verification.

## Consult

This invocation authorizes Hermes to inspect in-scope workspace code and architecture. Hermes has no enforced read-only mode, so run every round inside a fence: `-t file` leaves only file tools, and `HERMES_WRITE_SAFE_ROOT` set to an empty temp dir makes them refuse every workspace write and patch.

```bash
HERMES_WRITE_SAFE_ROOT="$(mktemp -d)" hermes chat -Q -t file --run-budget 300 \
  --query-file - <<'EOF'
<consultation prompt>
EOF
```

Give the call a timeout above the run budget. Hermes prints its answer, then `session_id: <id>` on stderr; add `--resume <id>` from the latest round to continue the same session.

Give Hermes a precise question and the relevant evidence:

```text
Act as an independent, read-only engineering consultant. Inspect relevant workspace
code with read_file and search_files. Do not modify files or read/expose secrets.

Question: <decision to make>
Evidence: <paths, tests, logs, constraints, competing positions>

Return: recommendation; evidence and uncertainty; strongest counterargument;
confidence; smallest validating check.
```

Verify material claims yourself. For a real disagreement, send only the new evidence and rebuttal through the same session; ask Hermes to revise or defend its conclusion. Stop when evidence decides the issue or the remainder is a user product/policy choice.

Never widen `-t file`, drop the write root, add `--yolo`, or ask Hermes to implement. Do not intentionally provide credentials, keys, tokens, or `.env` content.
