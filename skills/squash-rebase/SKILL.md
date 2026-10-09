---
name: squash-rebase
description: "User-invoked: squash a branch's unique commits into one on its open GitLab MR's target branch, then force-with-lease push. Run only when the user explicitly asks to squash-rebase. Auto-detects commits a stacked lower MR already re-pushed."
compatibility: "Requires git 2.26+, an authenticated glab CLI, and the MR's GitLab project as the origin remote."
---

# Squash rebase onto the MR target

## Inputs

- **repo**: absolute path of the main worktree.
- **source**: the feature branch to rewrite.
- **commits**: optional unique commit SHAs, oldest first. Present: Named replay. Absent: Auto-detect replay.
- **mr**: optional MR number.

The destination always comes from the open MR (step 2).

## Guardrails

- The **main worktree** stays as found. From **repo**, run only `git fetch`, `git worktree add`, and `git worktree remove`; every rebase, cherry-pick, reset, and commit runs in the **temp worktree**.
- `<source>` is a feature branch. When it is `master` or `main`, stop.
- The one push is `--force-with-lease=<source>:<recorded-tip>` to `<source>` (step 8).
- Hooks run on every commit; step 6 holds the one retry.
- Use glab. The MR's one edit is its stack line (step 9).

**Stop** means: run Clean up (step 10), then report the evidence the stop names plus Report items 10–11. A stop leaves `<source>` and the MR as they were.

## 1. Record the main worktree

From **repo**:

```bash
git branch --show-current
git status --porcelain
git rev-parse HEAD
```

Clean up confirms all three still match.

## 2. Find the destination

The open MR's target branch is the destination and the **stack parent**. Call it `<target>`.

- **mr** set: `glab mr view <mr>`. Its source branch must be `<source>`; otherwise stop.
- **mr** unset: `glab mr list --source-branch <source>`. One open MR: use it. None: stop, destination unknown. Several: stop with the list.

When the user names a destination, it must equal `<target>`. A different one is a stop with the mismatch.

## 3. Fetch

```bash
git fetch origin <target> <source>
```

Record three SHAs. Every later command uses them, so the whole run sees one snapshot:

- `<target-base>`: `git rev-parse origin/<target>`
- `<recorded-tip>`: `git rev-parse origin/<source>`
- `<fork-point>`: `git merge-base <target-base> <recorded-tip>`

## 4. Add the temp worktree

Put it in the system temp directory, so the run depends on no agent's home folder:

```bash
mktemp -d "${TMPDIR:-/tmp}/squash-rebase.XXXXXX"
```

Call the printed path `<temp>`; steps 5–8 run there. From **repo**:

```bash
git worktree add --detach <temp> <recorded-tip>
```

## 5. Replay

Replay the unique commits onto `<target-base>`: Named when **commits** is present, Auto-detect otherwise. Then account for every commit.

### Named

The named SHAs are the unique set.

1. Each SHA exists (`git cat-file -e <sha>^{commit}`), is in `<source>` (`git merge-base --is-ancestor <sha> <recorded-tip>`), and the last equals `<recorded-tip>`. Otherwise stop with `<recorded-tip>` and `git log --oneline <target-base>..<recorded-tip>`.
2. Replay exactly those commits, in order:
  ```bash
   git checkout --detach <target-base>
   git cherry-pick <oldest> ... <newest>
  ```
   A named commit that cherry-picks empty is already on `<target>`: stop and name it.

### Auto-detect

Because `<target>` is the stack parent, a commit is **unique** when its change is missing from `<target>`'s tree and **re-pushed** when the change is already there. Only a replay can tell the two apart: when the lower MR squashed or force-pushed, its old commits keep their SHAs and patch-ids on `<source>` while `<target>` carries the same change under new SHAs, so ancestry and `git cherry` count them as unique.

```bash
git rebase --onto <target-base> <fork-point> --empty=drop
```

Re-pushed commits apply empty and drop; unique commits keep a diff and stay. Re-pushed commits from a squashed lower branch often conflict, because later lower commits rewrote the same lines; resolve them under Conflicts.

### Conflicts

In both replays, `ours` is `<target>` and `theirs` is the source commit being applied. Resolve hunk by hunk:

- Keep `<target>`'s version of every change already on `<target>`, with the source commit's unique behavior on top. Then `git add` and `--continue`.
- Auto-detect: a resolution that leaves the commit with no diff means it was re-pushed: `git rebase --skip`. Named: the same outcome is a stop naming that commit.
- Stop with the conflicted files when the source-only behavior is unclear, or when the commit needs code that is missing from `<target>`.

### Account for every commit

```bash
git range-diff <fork-point>..<recorded-tip> <target-base>..HEAD
```

Each old commit appears exactly once: `<` is **dropped**, `=` or `!` is **kept**. Any `>` line (a new commit with no old counterpart) is a stop. Named: the kept set is exactly the named SHAs, else stop. Auto-detect: an empty kept set is a stop.

Print dropped and kept, with SHAs and subjects, then record `<replay-tree>`: `git rev-parse HEAD^{tree}`.

## 6. Squash

Read the full message of every kept commit. Write one subject and body covering their combined change: reuse their conventional-commit type, scope, and ticket id, and name each kept commit's behavior. Dropped commits are already on `<target>` and stay out of the message.

```bash
git reset --soft <target-base>
git commit
```

When the hook fails only because `node_modules` is missing in `<temp>` and **repo** has one, link it and retry the same commit:

```bash
ln -s <repo>/node_modules <temp>/node_modules
```

Any other hook failure is a stop with the hook output.

## 7. Verify

All three hold, or stop:

- `git rev-parse HEAD^` is `<target-base>`.
- `git rev-list --count <target-base>..HEAD` is `1`.
- `git rev-parse HEAD^{tree}` is `<replay-tree>`: the squash carries exactly the kept commits' combined change. A hook that rewrote files breaks this; stop with `git diff <replay-tree> HEAD`.

## 8. Push

```bash
git push --force-with-lease=<source>:<recorded-tip> origin HEAD:<source>
```

The lease compares the remote tip at push time. When it rejects, `git fetch origin <source>` and stop with both SHAs and `git log --oneline -n 20 origin/<source>`.

## 9. Update the MR

`glab mr view` the MR from step 2 and confirm source `<source>` and target `<target>`. When the description has a stack or previous-branch line naming a branch other than `<target>`, rewrite that line to name `<target>`. The target branch, state, and the rest of the description stay as they are.

## 10. Clean up

Runs on every exit, stops included.

1. In `<temp>`: abort any in-progress rebase or cherry-pick, and `unlink <temp>/node_modules` if step 6 linked it (`node_modules/` in `.gitignore` matches directories only, so the symlink counts as untracked and `git worktree remove` refuses).
2. From **repo**: `git worktree remove <temp>`, and confirm the path is gone. Remove only `<temp>`.
3. Confirm the main worktree's branch, `HEAD`, and `git status --porcelain` match step 1.

## 11. Report

In order:

1. Exact git commands used, in order.
2. Old remote tip (`<recorded-tip>`).
3. New tip.
4. Target base (`<target-base>`).
5. Dropped versus kept commits, and old SHAs to the new SHA.
6. Final commit subject.
7. Conflicts and how each was resolved, or clean.
8. Push result.
9. MR URL, source, target, and state.
10. Main worktree unchanged.
11. Temp worktree removed.

