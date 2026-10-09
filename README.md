# Agent Skills

Reusable skills for software-engineering agents.

## Available skills

### `to-clean-pr`

Drive a feature, bugfix, or existing GitHub PR or GitLab MR through an evidence-backed loop: one isolated head, verified changes, valid review fixes, and two clean polls.

### `consult-cursor-agent`

User-invoked, read-only Cursor consultation for evidence-backed cross-agent deliberation. It preserves one Cursor chat across follow-up rounds and keeps implementation authority with the calling agent.

### `consult-hermes-agent`

User-invoked, read-only Hermes consultation for evidence-backed cross-agent deliberation. It fences Hermes to file tools with workspace writes blocked, resumes one session across follow-up rounds, and keeps implementation authority with the calling agent.

### `humanize`

Improve readability while preserving facts, uncertainty and the requested voice. Includes calibration examples and a linter for style and character-level review.

### `squash-rebase`

User-invoked squash of a branch's unique commits into one on its open GitLab MR's target branch, pushed with force-with-lease. Auto-detects commits a stacked lower MR already re-pushed, and rewrites only in a temporary worktree.

## Install

This repository has not been published yet. After its first push, list the available skills:

```bash
npx skills add alvedder/skills --list
```

Install a named skill:

```bash
npx skills add alvedder/skills --skill <skill-name>
```

## Repository structure

```text
skills/
	├── consult-cursor-agent/
	│		├── SKILL.md
	│		└── agents/
	│				└── openai.yaml
	├── consult-hermes-agent/
	│		├── SKILL.md
	│		└── agents/
	│				└── openai.yaml
	├── humanize/
	│		├── SKILL.md
	│		├── PATTERNS.md
	│		├── EXAMPLES.md
	│		├── LINT.md
	│		└── scripts/
	├── squash-rebase/
	│		├── SKILL.md
	│		└── agents/
	│				└── openai.yaml
	└── to-clean-pr/
			├── SKILL.md
			├── references/
			└── agents/
					└── openai.yaml
```

Each skill is self-contained. `SKILL.md` is the portable skill definition; `agents/openai.yaml` adds Codex-facing display metadata.

## Development

Keep the skill folder name and frontmatter `name` aligned. Before publishing changes, validate local discovery:

```bash
npx skills add . --list
```

## License

MIT
