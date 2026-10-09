# Linked follow-up PRs

Treat a PR as linked only when it mentions the original PR on the original PR's thread. A shared author, title, or similar diff is not evidence of linkage.

When a linked follow-up appears:

1. Mark it ready when authorized so reviewer bots can run. Record an authorization failure; treat it as blocking only if it prevents inspection or validation.
2. Use it as a reference proposal. Inspect its diff and reviews, validate every underlying claim, and place valid changes only on the original head.
3. Preserve attribution when directly reusing substantive code or commits.
4. Before closure, prove every valid concern is covered by the original head or defensibly dismissed.
5. Post covering-commit, diff, or dismissal evidence. Close it when authorized and confirm the state; otherwise leave it open and report why.

Keep an open linked follow-up out of the clean state whenever it retains a unique valid change.
