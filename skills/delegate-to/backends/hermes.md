# Hermes backend

CLI: `hermes` (Nous Research Hermes Agent). Runs the configured default model, provider, and toolsets; the provider decides whose quota pays.

## Commands

Write, in a Hermes worktree:

```bash
hermes chat --quiet --worktree --in "$repo" --query-file "$run/brief.md" \
  >"$run/out" 2>"$run/err"
```

- **Read-only:** drop `--worktree`, add `--toolsets file`, and prefix `HERMES_WRITE_SAFE_ROOT="$(mktemp -d)"`. Hermes has no read-only mode; together these leave only file tools and make them refuse every workspace write.
- **In place:** drop `--worktree`.
- **Model:** `--model <id>`, plus `--provider <name>` when the model needs one.
- **Force:** `--yolo`.
- **Resume:** `hermes chat --quiet --resume <session_id> --in <worktree path> --query-file <new message file>`, without `--worktree`; read-only rounds keep the fence.

`out` holds the final answer, framed by the worktree path, branch, and base above it and a keep-or-remove notice below it. `err` ends with `session_id: <id>`; use the latest, since it changes after context compression. Exit 0 means completed, 130 interrupted, 1 failed.

## Gotchas

- On exit, `--worktree` force-removes the worktree and deletes its branch unless it holds unpushed commits, so uncommitted work is lost: keep the brief's commit instruction, and keep `terminal` in the configured toolsets so the delegate can commit.
- `--worktree` creates `<repo>/.worktrees/hermes-<hex>` on branch `hermes/hermes-<hex>`, based on the freshly fetched remote tip (local HEAD when the remote is unreachable or `worktree_sync: false`), and appends `.worktrees/` to the repo's tracked `.gitignore`.
- It also tells the delegate to commit, push, and open a PR; when those are not authorized, the brief must say so.
- Quiet single-query runs auto-deny commands that need approval (`approvals.single_query_mode`) and block `execute_code`; other terminal commands, `git commit` and `git push` included, run freely. Top-level `hermes -z` bypasses every approval; use `hermes chat --quiet`.
