# Heartbeat context

A scheduled wake may start without memory of earlier turns.

## Receipts

Keep private receipts in the original checkout's uncommitted task directory:

- **Instructions**: paths and content hashes of this skill, its references and governing repository guidance, recorded after a full load. Reload after context loss or reset, a changed hash or an unverifiable receipt.
- **Feedback**: artifact fingerprint, original and linked heads, and claim-validation evidence. Reuse it only for unchanged artifacts on unchanged heads; fully read and validate anything new or changed.
- **Readiness**: the PR, governing source and reason, command outcome, re-read head and ready state, and next action, including a human keep-draft preference.

Receipts preserve decisions; every wake still refreshes remote state per [clean-polls.md](clean-polls.md). When the repository provides an evidence or policy-evaluation helper, use its documented flow.

## Wake prompt

Save a short prompt of pointers in plain words: the original checkout, stable task, instruction paths and receipt/state paths. Its bootstrap reloads instructions unless they are verifiably loaded in the current context. Rewrite it whole each time. Heads, counts, run IDs, timestamps and task guardrails live in receipts or the task handoff, so each wake reads current state rather than a stale copy. Use a repository prompt generator when one exists.

## Schedule and stop

Schedule the next wake at the evaluator's `nextEligibleAt`, else the poll interval, then end the turn; wait in-session only without a scheduler. Stay quiet while unchanged; notify on material change, completion, failure or required action. Handle a stall per the skill's Stop section, and keep waking for portions still progressing.

Cancel the wake on clean-poll completion, confirmed merge or closure, user stop, or a scheduler that cannot re-arm after bounded recovery. Report that merge, closure and scheduler failure establish no cleanliness.
