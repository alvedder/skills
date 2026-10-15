# GitHub pull requests

Use `gh`; `gh api graphql` reaches what `gh pr view --json` omits. Flags: `--help`.

## Signals

- **Identity**: `gh pr view --json number,state,isDraft,headRefOid,baseRefName,baseRefOid,isCrossRepository`. Head is `headRefOid`. Ready means `isDraft` false (`gh pr ready`).
- **Mergeable**: `mergeStateStatus` is the verdict. `CLEAN` passes; `UNSTABLE` means a non-required check fails, so it passes only when every failure is green by the usage-limit exception; other values name the blocker. `mergeable` alone reports conflicts only. `UNKNOWN` means still computing: incomplete retrieval, retry.
- **CI**: plain `gh pr checks` lists every check (`--required` filters); `bucket` gives the terminal state. `pass` and `skipping` (neutral or skipped) are green; `fail`, `cancel` and `pending` are not. `gh run view` for workflow jobs. A failure's reason is in the check run `output` (`gh api repos/{owner}/{repo}/check-runs/<id>`) or the status `description`: the evidence for the usage-limit exception.
- **Reviews**: `reviews` and `latestReviews`; each review's `commit.oid` must equal `headRefOid` to count for the exact head. `reviewDecision` summarizes required reviews.
- **Threads**: GraphQL only: `pullRequest.reviewThreads` with `isResolved`, `isOutdated` and comments. Resolve with the `resolveReviewThread` mutation. An outdated thread stays unresolved until resolved.
- **Comments**: three channels, each read in full: PR comments (`comments`), review bodies (`reviews`), inline review comments (`gh api repos/{owner}/{repo}/pulls/<n>/comments`).
- **Activity**: `gh api repos/{owner}/{repo}/issues/<n>/timeline` records pushes (`committed`, `head_ref_force_pushed`), readiness changes and cross-references.
- **Linked PRs**: a mention of the original PR surfaces as a `cross-referenced` timeline event on it.
