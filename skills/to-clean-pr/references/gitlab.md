# GitLab merge requests

Use `glab`; `glab api` reaches what its subcommands omit (`:id` expands to the current project; add `--paginate` for lists). Flags: `--help`. `<iid>` is the MR number shown as `!<iid>`.

## Signals

- **Identity**: `glab mr view <iid> -F json`. Head is `sha` (equals `diff_refs.head_sha`); base is `target_branch`. Ready means `draft` false (`glab mr update <iid> --ready`).
- **Mergeable**: `detailed_merge_status` is the verdict. `mergeable` passes; other values name the blocker (`ci_must_pass`, `ci_still_running`, `not_approved`, `requested_changes`, `discussions_not_resolved`, `need_rebase`, `draft_status`, ...). `checking`, `unchecked` and `preparing` mean still computing: incomplete retrieval, retry.
- **CI**: `head_pipeline` is the pipeline on the head commit; read its jobs with `glab api projects/:id/pipelines/<pipeline_id>/jobs`. Pipelines of older commits and branch pipelines do not count for the head. `detailed_merge_status` already applies the project's pipeline policy; use job states to diagnose.
- **Reviews**: approvals, not review objects. `GET projects/:id/merge_requests/<iid>/approvals` gives `approved`, `approvals_left`, `approved_by`; Premium/Ultimate adds `.../approval_state` per rule. A project with `reset_approvals_on_push` drops approvals on every push, so re-read after each push.
- **Threads**: `GET projects/:id/merge_requests/<iid>/discussions`; a thread is unresolved when its notes are `resolvable` and not `resolved`. Resolve with `PUT .../discussions/<discussion_id>` and `resolved=true`. `blocking_discussions_resolved` is the rolled-up verdict.
- **Comments**: every note of every discussion, including individual (non-resolvable) notes. `system` true marks activity records (pushes, label changes, mentions), not feedback.
- **Activity**: system notes plus `updated_at`, the head pipeline and approvals.
- **Linked MRs**: a mention of the original MR surfaces as a system note on it (`mentioned in merge request !<iid>`).
