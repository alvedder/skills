---
name: consult
description: 'Read-only, evidence-backed second opinion from another agent (`/consult <backend>`), with rebuttal rounds in one session.'
disable-model-invocation: true
---

# Consult

Get an independent, evidence-backed view on a contested design, debugging, architecture, security, or trade-off question. You own the decision, changes, and verification.

Use the `delegate-to` skill in read-only mode with the backend the user named, and this brief in place of its template:

```text
Act as an independent, read-only engineering consultant. Inspect relevant workspace
code. Do not modify files, run mutating commands, or read/expose secrets.

Question: <decision to make>
Evidence: <paths, tests, logs, constraints, competing positions>

Return: recommendation; evidence and uncertainty; strongest counterargument;
confidence; smallest validating check.
```

Wait for each answer before deciding. Verify material claims yourself. For a real disagreement, resume the same session with only the new evidence and rebuttal; ask the consultant to revise or defend its conclusion. Stop when evidence decides the issue or the remainder is a user product/policy choice.
