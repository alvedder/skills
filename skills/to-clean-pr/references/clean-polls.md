# Clean polls

Clean means two consecutive qualifying polls separated by the full interval: the user's, else 15 minutes.

## Each poll

Refresh the original and linked PRs: identity, head, base, readiness, mergeability, every check on the latest push, reviews, threads, comments and linked activity, read as the platform reference defines them.

Reset the count to zero on any push, PR/comment/thread/review change, readiness or check-state change, linked activity or incomplete retrieval. Process changed feedback and retry failed reads before advancing the watermark, then restart the interval. A read failing identically on three consecutive polls spanning the interval is a stall. When the base moves and mergeability needs it, rebase the original head, verify, push and reset.

## Qualify

A poll qualifies only when:

- The original PR is open, ready and mergeable.
- Every check on the exact published head, required or not, is terminal and **green**: passing, neutral, or a reviewer stopped by its usage limit as its own output states. Anything else is **red**, except a **superseded** check (its run never executed, and a newer run of the same workflow, event, ref and head passed, as the platform reference proves): disclosed, never counted as passing.
- Every review that repository instructions or workflow policy require is completed on the exact published head; an unobservable required review blocks.
- The original and linked PRs have no actionable comment or unresolved thread.
- Every valid follow-up proposal is covered or defensibly dismissed on the original head; follow-ups eligible to close are closed, and any left open are reported.
- No verified fix is uncommitted or unpushed.

For an optional reviewer stopped by its usage limit or with unobservable completion, report "no new feedback observed", not "review completed".

## Report

Report **health** (current checks, reviews and feedback, from the records retrieved) apart from **qualification** (poll count and evidence completeness). Incomplete evidence never qualifies and is no health failure:

```text
Health (retrieved records): checks green; 0 unresolved threads; no actionable feedback.
Qualification: 0/2; the run log read for cancelled job 115 fails identically on 3 polls. Stall: repair the collector's log read.
```
