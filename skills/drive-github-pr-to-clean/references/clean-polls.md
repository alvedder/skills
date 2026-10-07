# Clean polls

Use the user-specified interval, or 15 minutes. Completion requires two consecutive qualifying polls separated by the full interval.

For instruction loads and processed-feedback receipts, read [heartbeat-context.md](heartbeat-context.md) at the context-validation step.

## Refresh every poll

Refresh the original and explicitly linked PR identities, heads, bases, ready states and mergeability. Refresh required/applicable CI checks, workflows and jobs, observable reviewer jobs after the latest push, all reviews, unresolved threads, comments and explicit linked activity.

## Reset on activity

Reset the clean-poll count to zero for any push, published PR/comment/thread change, new/changed review artifact, readiness or check-state change, linked activity or incomplete retrieval. Fully process changed feedback and retry incomplete retrieval before advancing the processed-event watermark; then restart the interval. If the base moves and mergeability requires synchronization, rebase the original head, verify and push it, then reset.

## Count a clean poll

Repository instructions and explicit workflow policy define required checks and reviews. Count a poll as clean only when all of these hold:

- The original PR is open, ready and mergeable; every required and applicable CI check, workflow and job is terminal and passing.
- Every required review is completed on the exact published head. Unavailable or unobservable required review prevents qualification.
- Observable advisory reviewer jobs after the latest push are terminal. Failed or unavailable advisory review is a disclosed limitation, never completed review.
- The original and linked PRs have no actionable comment or unresolved review thread.
- Every valid follow-up proposal is covered or defensibly dismissed on the original head; no unique valid follow-up change remains uncovered.
- Every follow-up eligible to close is closed. Any open follow-up is covered or dismissed, ineligible to close, and identified in the report.
- No verified fix remains uncommitted or unpushed.

If optional reviewer completion is not observable, report "no new feedback observed", not "review completed". Both qualifying polls are still required.
