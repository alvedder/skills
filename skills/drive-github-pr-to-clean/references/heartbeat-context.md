# Heartbeat context

Cache invariant instructions and processed-feedback provenance; refresh remote evidence every poll.

## Validate context

Record authoritative instruction paths and content hashes only after full loads. Reuse while the same loaded content remains in usable context and hashes still match. Context loss/reset, changed documents or unverifiable receipts require full reloads. Choose a fresh context identity after loss; never restore it from a saved prompt or cache alone.

Retain per-artifact fingerprints, original/linked PR heads and claim-validation evidence. Attest unchanged feedback by validated receipts, without printing it in full again. Completely read new/changed artifacts and validate their claims against current code. Changed heads require renewed claim validation; missing/damaged provenance requires rereading. A receipt establishes processed context, not a passing review or a clean PR.

## Refresh and evaluate

Every wake completely refreshes current original/linked PR identities, heads, readiness, applicable required checks and reviewer jobs, reviews, unresolved threads/comments and explicit linked activity. Reuse neither skips remote reads nor hides incomplete retrieval. Refresh workflow policy from this current evidence. Preserve all publication/artifact/readiness/check/activity/incomplete resets and two full-interval polls. Disclose unavailable hosted review accurately; missing required review remains a gate.

When a repository provides a validated-context helper, use it with its collector and policy evaluator. In Atlas, follow `docs/agents/pr-heartbeat.md`: `tools/pr_heartbeat.py prepare` produces a private read plan; `attest` records actual instruction loads and content-bound claim notes; `evaluate` restricts unprocessed context before calling the existing evaluator. Without such a helper, keep equivalent private receipts and validation decisions; do not pretend a hash was previously loaded content.

## Save a short prompt

Store original checkout, stable task, authoritative paths and private cache/policy/poll-state paths. Keep the prompt cohesive and refer to validated instructions rather than inlining them or demanding unconditional rereads. In Atlas, generate it with `tools/pr_heartbeat.py prompt`. Exclude the current usable-context identity from saved prompts.

Use the evaluator's `nextEligibleAt` when available. Stay quiet while unchanged; notify on material change, completion, failure or required user action. Stop the wake after two qualifying polls, confirmed merge/closure, user stop or terminal scheduler failure. Report scheduler failure without inventing cleanliness. Preserve the existing blocker audit and explicit merge authority; merge/closure never substitutes for two clean polls.
