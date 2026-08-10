# Clean polls

## Refresh every poll

Refresh the original PR's head, base, ready state, mergeability, required checks, and observable reviewer jobs after the latest push. Refresh reviews, unresolved threads, comments, linked follow-ups, and activity newer than the watermark.

## Reset on activity

Reset the clean-poll count to zero for any new review artifact, push, readiness or check-state change, or linked-follow-up activity. Address it, advance the watermark to the newest processed event, and restart the interval. If the base moves and mergeability requires synchronization, rebase the original head, verify and push it, then reset.

## Count a clean poll

Count a poll as clean only when all of these hold:

- The original PR is open, ready, mergeable, and every required check is terminal and passing.
- Observable reviewer jobs after the latest push are terminal.
- The original and linked PRs have no actionable comment or unresolved review thread.
- Every valid follow-up proposal is covered or defensibly dismissed on the original head; no unique valid follow-up change remains uncovered.
- Every follow-up eligible to close is closed. Any open follow-up is covered or dismissed, ineligible to close, and identified in the report.
- No verified fix remains uncommitted or unpushed.

If reviewer completion is not observable, report “no new feedback observed,” not “review completed”; still require both clean polls.
