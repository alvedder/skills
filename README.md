# Agent Skills

Reusable skills for software-engineering agents.

## Available skills

### `drive-github-pr-to-clean`

Drive a feature, bugfix, or existing PR through an evidence-backed loop: one isolated PR head, verified changes, valid review fixes, and two clean polls.

### `consult-cursor-agent`

User-invoked, read-only Cursor consultation for evidence-backed cross-agent deliberation. It preserves one Cursor chat across follow-up rounds and keeps implementation authority with the calling agent.

### `humanize`

Improve readability while preserving facts, uncertainty and the requested voice. Includes calibration examples and a linter for style and character-level review.

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
	├── drive-github-pr-to-clean/
	│		├── SKILL.md
	│		└── agents/
	│				└── openai.yaml
	└── humanize/
			├── SKILL.md
			├── PATTERNS.md
			├── EXAMPLES.md
			├── LINT.md
			└── scripts/
```

Each skill is self-contained. `SKILL.md` is the portable skill definition; `agents/openai.yaml` adds Codex-facing display metadata.

## Development

Keep the skill folder name and frontmatter `name` aligned. Before publishing changes, validate local discovery:

```bash
npx skills add . --list
```

## License

MIT
