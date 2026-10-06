# Heartbeat context

Retain validated instructions and processed-feedback receipts between wakes.

## Validate context

A usable-context ID is an opaque identifier for the instruction content currently loaded in the agent's context. Keep private receipts under the original checkout/task's uncommitted working directory so they survive wakes. Record authoritative paths, including the skill entry point, both clean-poll and heartbeat-context references, and governing repository guidance.

Record instruction paths and content hashes after actual full loads. Reuse while that loaded content remains usable and its hashes match. Context loss/reset, changed documents or unverifiable receipts require full reloads. After loss, reset or uncertainty choose a fresh usable-context ID; establish usability by loading source content again.

A processed-feedback receipt binds the artifact fingerprint, original/linked heads and concrete claim-validation evidence. Reuse unchanged feedback only through validated receipts. Completely read new/changed artifacts and validate their claims against current code. Changed heads require renewed claim validation; missing/damaged provenance requires rereading. Feedback receipts can survive context loss; instruction-load usability cannot.

## Refresh and evaluate

Read [clean-polls.md](clean-polls.md) for the authoritative remote-refresh, gate, reset and completion rules. Reuse decisions do not replace that evidence flow. Refresh repository workflow policy from current evidence and validated claims before evaluation.

When the repository provides a validated-context helper, use its documented collector, read-plan, attestation and policy-evaluation flow. Otherwise retain equivalent private receipts and validation decisions. A processed receipt establishes an actual read and claim validation; the workflow policy determines whether review and cleanliness gates pass.

## Save a short prompt

Store the original checkout, stable task, authoritative instruction paths and private cache/policy/poll-state paths. Keep the prompt cohesive and point to those instructions. Its bootstrap must load authoritative content unless already validated in the current usable context. Exclude the current usable-context ID. Use a repository prompt generator when one is available; otherwise save these same paths and bootstrap decisions directly.

## Schedule and stop

Use the policy evaluator's nextEligibleAt when available; otherwise use the interval in [clean-polls.md](clean-polls.md). Arm each wake as a scheduled task, then end the turn. Wait in-session only when the environment has no scheduler. Stay quiet while unchanged; notify on material change, completion, failure or required user action.

Cancel the wake on clean-poll completion, confirmed original merge/closure, user stop or terminal scheduler failure (another wake cannot be scheduled after bounded recovery). Merge/closure and scheduler failure do not establish cleanliness. Report scheduler failure; preserve the blocker handling in the skill's Stop section and explicit user merge authority.
