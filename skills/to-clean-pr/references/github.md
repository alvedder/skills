# GitHub pull requests

Use `gh`; `gh api graphql` reaches what `gh pr view --json` omits.

- **Identity**: head is `headRefOid`; ready is `isDraft` false (`gh pr ready`).
- **Mergeable**: `mergeStateStatus`. `CLEAN` passes. `UNSTABLE` means a non-required check fails; it passes only when every failure is green by the usage-limit exception. `UNKNOWN` is still computing: retry. Other values name the blocker; `mergeable` alone reports only conflicts.
- **Checks**: `gh pr checks` lists every check (`--required` filters). `bucket` `pass` and `skipping` (neutral or skipped) are green; `fail`, `cancel` and `pending` are not. A failure's reason, the evidence for the usage-limit exception, is in the check run's `output` (`gh api repos/{owner}/{repo}/check-runs/<id>`) or the status `description`.
- **Superseded**: a check's details URL names its run and job. A cancelled run is superseded when each of its jobs never executed (`actions/runs/<id>/jobs`: `runner_id` 0 or null, empty `runner_name` and `steps`) and a run with a greater `run_number` passed with the same `workflow_id`, `path`, `event`, `head_branch`, `head_sha`, `head_repository` and `referenced_workflows`, including a passing job of each cancelled job's name. Only `pull_request`, `pull_request_target` and `push` runs qualify; run records omit dispatch inputs. `gh run view --log` fails for a run with a never-executed job; read its other jobs' logs via `actions/jobs/<id>/logs`.
- **Reviews**: a review counts for the head only when its `commit.oid` equals `headRefOid`; `reviewDecision` summarizes required reviews.
- **Threads**: GraphQL only: `reviewThreads` (`isResolved`, `isOutdated`); resolve with `resolveReviewThread`. An outdated thread stays unresolved until resolved.
- **Comments**: read three channels in full: PR comments, review bodies and inline review comments (`gh api repos/{owner}/{repo}/pulls/<n>/comments`).
- **Activity and links**: `gh api repos/{owner}/{repo}/issues/<n>/timeline` records pushes, readiness changes and `cross-referenced` events, which reveal linked PRs.
