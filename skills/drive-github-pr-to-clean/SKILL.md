---
name: drive-github-pr-to-clean
description: 'Drive a GitHub PR to evidence-backed review clean: verify the requested feature or defect, use one isolated PR head, implement, test, publish, resolve valid feedback, and confirm two clean polls. Use for end-to-end feature or bugfix PR work, review feedback, CI failures, safe PR rebases, or recurring PR-cleanliness checks.'
---

# Drive GitHub PR to Clean

Run a **tight PR loop**: evidence → original head → review → two clean polls.

## 1. Orient

1. Read the exact issue or PR, acceptance criteria or reproduction, linked artifacts, and repository instructions.
2. Inspect the worktree, remotes, default/base/head branches, divergence, mergeability, existing PR, checks, reviews, unresolved threads, comments, and follow-up activity.
3. Attach to the original PR head when one exists; otherwise create one dedicated task branch from the intended base.
4. Record an activity watermark from the newest PR, review, thread, comment, check, or linked-follow-up event; use it to detect later activity, not to skip existing feedback.

Keep branch integrity: work only on the original head, preserve unrelated changes, and use a separate worktree when needed. Rebase that head only when required; when policy blocks a rebase, stop rather than merge the base into the head. Use `--force-with-lease` only for an agent-owned original head. Merge a PR only on explicit user request.

## 2. Prove the change

For a defect, establish a reproduction, failing regression, or conclusive current-code path. If none exists, report what was tested and stop as unverified. For a feature, make acceptance criteria observable. Change the root-cause variants and touched regression seams; report adjacent work separately.

## 3. Change and publish

1. Write a red regression where practical, then implement the smallest coherent change.
2. Run the regression, affected suites, and repository-required checks; broaden by risk. Classify pre-existing, flaky, and inconclusive failures precisely.
3. Inspect the final diff for scope, generated or migration drift, conflict artifacts, and formatting. Stage only task files, commit coherently, and push the verified original head.
4. Fetch the base before synchronization. Rebase and reverify when required, then push normally or with the permitted lease.
5. Locate or create the original PR, make it ready when repository policy permits, and confirm readiness before polling.

## 4. Turn feedback into evidence

Treat every review, comment, bot patch, and follow-up proposal as a claim.

1. Trace the cited code and reproduce the claim or establish equivalent evidence.
2. Put each valid fix and its regression coverage on the original head, verify it, then push it.
3. Post concise evidence for every dismissal. Resolve a thread only after its remote fix or dismissal evidence exists, and reply clearly to non-thread feedback.

When a PR may be a follow-up, read [linked-follow-ups.md](references/linked-follow-ups.md) before acting on it.

## 5. Prove clean

Use the user-specified interval, or 15 minutes. Use an available wait, monitor, or automation rather than ending between polls. Before starting or restarting a clean-poll cycle, read [clean-polls.md](references/clean-polls.md).

Stop only after two consecutive clean polls separated by the full interval. Remove any monitor when stopping.

## Stop

Report a blocker only for missing authority, product decisions, permissions, unavailable infrastructure, or repeated non-actionable failure after bounded retries. Unless the user separately asks to merge, leave the original PR open and ready.

Report the PR and final head, implemented and dismissed findings, validation evidence, review and follow-up state, two-poll evidence, and residual risk, skipped validation, or blockers.
