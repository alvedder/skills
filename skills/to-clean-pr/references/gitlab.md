# GitLab merge requests

Use `glab`; `glab api` reaches what its subcommands omit.

- **Identity**: `glab mr view <iid> -F json`; head is `sha`, base `target_branch`; ready is `draft` false (`glab mr update <iid> --ready`).
- **Mergeable**: `detailed_merge_status`. `mergeable` passes; `checking`, `unchecked` and `preparing` are still computing: retry. Other values name the blocker.
- **CI**: only `head_pipeline` jobs count (`glab api projects/:id/pipelines/<id>/jobs`). `success` and `skipped` are green; `failed` and `canceled` are red, even when `allow_failure` lets `detailed_merge_status` pass. A failure's reason is in the job trace (`projects/:id/jobs/<id>/trace`).
- **Reviews**: approvals (`.../merge_requests/<iid>/approvals`; `.../approval_state` per rule on Premium). With `reset_approvals_on_push`, re-read after every push.
- **Threads**: `.../discussions`; unresolved means `resolvable` and not `resolved`. Resolve with `PUT .../discussions/<id>` and `resolved=true`.
- **Comments**: every note of every discussion; `system` notes are activity, not feedback.
- **Activity and links**: system notes, `updated_at`, the head pipeline and approvals; a linking MR appears as a `mentioned in merge request !<iid>` system note.
