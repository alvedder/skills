---
name: to-clean-pr
description: 'Drive a GitHub PR or GitLab MR to evidence-backed clean: one original head, verified changes, valid feedback resolved, two clean polls. Use for feature or bugfix PR/MR work, review feedback, CI failures, rebases, or recurring PR cleanliness checks.'
---

# Drive PR to Clean

Run a **tight PR loop**: evidence → original head → review → two clean polls. Before acting, read [github.md](references/github.md) or [gitlab.md](references/gitlab.md) for the PR's platform signals.

## 1. Orient

Read the task, repository instructions and the PR's current state. Attach to the original PR head, or create one task branch from the intended base. Record an activity watermark from the newest event to detect later activity; existing feedback still gets processed.

Branch integrity:

- Work only on the original head; preserve unrelated changes, using a separate worktree when needed.
- Rebase only when required, then reverify; when policy blocks a rebase, stop rather than merge the base in. Use `--force-with-lease` only on an agent-owned head.
- Merge, auto-merge included, only on explicit user request.

## 2. Prove the change

Defect: establish a reproduction, failing regression or conclusive code path; without one, report what was tested and stop as unverified. Feature: make the acceptance criteria observable. Fix every variant of the root cause; report adjacent work separately.

## 3. Change and publish

1. Write a red regression where practical, make the smallest coherent change, run affected suites and repository-required checks, and push the verified original head with only task files committed.
2. Decide readiness for the original PR and each authorized task-owned companion. Ready is the default; draft needs an explicit user or repository-policy requirement, and unrun qualification is one only where that policy says so. Record the source and reason; a human keep-draft preference persists across wakes.
3. Promote with the platform's ready command, then re-read the PR, head and ready state. Done when they match the intended PR and head; a changed head needs revalidation. Remove stale keep-draft wording from the PR body. Ready means reviewable, not qualified, clean or mergeable.

## 4. Turn feedback into evidence

Every review, comment, bot patch and follow-up proposal is a **claim**: trace and reproduce it before acting. Put valid fixes with regression coverage on the original head and push them. Post evidence for each dismissal; resolve a thread only once its pushed fix or dismissal evidence exists. For a possible follow-up PR, read [linked-follow-ups.md](references/linked-follow-ups.md).

## 5. Prove clean

Read [clean-polls.md](references/clean-polls.md) before starting a clean-poll cycle, and [heartbeat-context.md](references/heartbeat-context.md) before scheduling or resuming wakes.

## Stop

Report a blocker only for missing authority, product decisions, permissions, unavailable infrastructure, or a **stall**: the same blocker unchanged after bounded retries, such as a draft with no authorized transition or a read failing identically. Name its next action (promote or cite the draft gate, retry a transient read, repair a broken collector), notify once, pause that portion with its resume condition, and continue independent ones. Running CI, pending review and the poll interval are progress. A stall proves nothing about whether evidence is absent or superseded.

Leave the original PR open and ready. Report the PR and final head, implemented and dismissed findings, validation, follow-up state, [health and qualification](references/clean-polls.md#report), and residual risk or skipped validation.
