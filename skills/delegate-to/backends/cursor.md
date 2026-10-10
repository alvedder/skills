# Cursor backend

CLI: `cursor-agent`, billed to the Cursor subscription.

## Commands

Write, in a Cursor worktree branched from local HEAD (`--worktree-base <ref>` to change it):

```bash
cursor-agent --print --trust --output-format json --workspace "$repo" \
  --worktree "<name>" "$(cat "$run/brief.md")" >"$run/out" 2>"$run/err"
```

- **Read-only (not enforced):** replace `--worktree "<name>"` with `--mode ask` and point `--workspace` at a snapshot. Ask mode only steers the prompt; headless edits still succeed in it, so the snapshot is what keeps the repo untouched.
- **In place:** drop `--worktree "<name>"`.
- **Model:** `--model <id>`; `cursor-agent --list-models` lists them.
- **Force:** `--force`.
- **Resume:** the same command plus `--resume <session_id>`, with the same worktree name and the new message in place of the brief.

The last line of `out` is the JSON result with `result` and `session_id`; with a worktree, the line above it is `Using worktree: <path>`. A failed run exits non-zero with the reason in `err`.

## Gotchas

- Headless runs edit workspace files freely but auto-deny shell commands outside `permissions.allow` in `~/.cursor/cli-config.json`, so the delegate cannot run tests or `git commit`; its deliverable is uncommitted edits in the worktree. Allowlist the commands, or enable Cursor's sandbox (`--sandbox enabled`) where available.
- Headless runs reject writes outside the workspace, except under `/tmp`. `--force` lifts that check and the protected-path check, `.git/hooks` included.
- Neither the hidden `--exclude-tools` flag nor a `Write(**)` deny in the workspace's `.cursor/cli.json` blocks edits (tested with `cursor-agent` 2026.10.01).
- `--trust` records a persistent trust marker under `~/.cursor/projects/<slug>` for every workspace path, snapshots included; it approves no commands.
- Worktrees live at `~/.cursor/worktrees/<repo>/<name>` on branch `<name>` and are never removed; `.cursor/worktrees.json` setup scripts run when one is created.
