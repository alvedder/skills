# GitHub pull requests

Use `gh`; `gh api graphql` reaches what `gh pr view --json` omits. Flags: `--help`.

## Signals

- **Identity**: `gh pr view --json number,state,isDraft,headRefOid,baseRefName,baseRefOid,isCrossRepository`. Head is `headRefOid`. Ready means `isDraft` false (`gh pr ready`).
- **Mergeable**: `mergeStateStatus` is the verdict. `CLEAN` passes; `UNSTABLE` means non-required checks fail, so judge their applicability; other values name the blocker. `mergeable` alone reports conflicts only. `UNKNOWN` means still computing: incomplete retrieval, retry.
- **CI**: `gh pr checks --required` for required checks, plain `gh pr checks` for the rest; `bucket` gives the terminal state (`pass`, `fail`, `pending`, `skipping`, `cancel`). `gh run view` for workflow jobs.
- **Reviews**: `reviews` and `latestReviews`; each review's `commit.oid` must equal `headRefOid` to count for the exact head. `reviewDecision` summarizes required reviews.
- **Threads**: GraphQL only: `pullRequest.reviewThreads` with `isResolved`, `isOutdated` and comments. Resolve with the `resolveReviewThread` mutation. An outdated thread stays unresolved until resolved.
- **Comments**: three channels, each read in full: PR comments (`comments`), review bodies (`reviews`), inline review comments (`gh api repos/{owner}/{repo}/pulls/<n>/comments`).
- **Activity**: `gh api repos/{owner}/{repo}/issues/<n>/timeline` records pushes (`committed`, `head_ref_force_pushed`), readiness changes and cross-references.
- **Linked PRs**: a mention of the original PR surfaces as a `cross-referenced` timeline event on it.
