---
name: delegate-to
description: 'Delegate a task to an external agent CLI (Cursor, Hermes) and collect its verified result. Use when a user or automation prompt names one of those agents for a task ("have hermes fix…", "ask cursor to review…", "/delegate-to cursor") or explicitly asks to hand work off to another agent.'
---

# Delegate To

Hand one task to an external agent and bring back a result you have checked. The delegate does the work; you own the brief, the verification, and the report.

## 1. Pick the backend

Each backend is a file in [backends/](backends/): `/delegate-to <name>` reads `backends/<name>.md`. With no name, use the only backend whose CLI is installed, or ask the user which one. For an unknown name, list the backend files and stop.

## 2. Pick the mode and workspace

- **Read-only** for questions, reviews, research, and plans: the backend's read-only command, in place. When the backend file says its read-only mode is not enforced, point it at a disposable snapshot instead; re-run the copy into the same directory before each follow-up round, and delete it when the session ends:

  ```bash
  snap="$(mktemp -d)"
  git -C "$repo" ls-files -coz --exclude-standard | tar -C "$repo" --null -T - -cf - | tar -C "$snap" -xf -
  ```

  Outside git, copy the directory without its `.env*` files.
- **Write** for anything that edits files:
  - In a git repo: the backend's worktree flag. If it has none, `git worktree add -b delegate/<slug> <path>` and run the backend there.
  - Outside git: in place. Leave the delegate's paths alone until it exits.

A worktree starts from committed state; the backend file names its base. When the task depends on uncommitted changes, ask the user whether to commit first or run in place.

## 3. Write the brief

Write it to `brief.md` in a fresh `mktemp -d` run directory:

```text
Task: <the user's request, verbatim where possible>
Context: <paths, constraints, evidence, decisions already made>
Authorized outward actions: <exactly what the user approved: push, PR, messages; or "none">
Workspace: <read-only: do not modify files> | <isolated worktree: commit your work on its branch before finishing>
Return: outcome; changes (files, branch, commits, PRs, outward actions); checks run and results; open risks.
```

Give paths relative to the repo root, so the delegate resolves them inside its own worktree or snapshot. The brief carries only what the user authorized. Keep credentials, keys, tokens, and `.env` content out of it.

## 4. Launch

Run the backend command in the background with your harness's own mechanism, output redirected into the run directory, and keep working; collect the run when it exits. Several delegates can run at once, each in its own worktree.

- Pass a model only when the user named one; otherwise the backend's configured default runs.
- Add the backend's force flag only with the user's written approval in the current request; an automation prompt counts. Otherwise the backend's own approvals and sandbox apply.

## 5. Collect and report

Read the result and the session ID. Verify material claims yourself: inspect the worktree diff, rerun the key check. Report the outcome, what you verified, where the changes live (worktree path, branch, commits, PRs), outward actions taken, and the session ID. Integrate changes into the user's tree only when asked.

For follow-ups or corrections, resume the same session with only the new information.
