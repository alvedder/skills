# Agent Skills

Reusable skills for software-engineering agents.

## Available skills

### `drive-github-pr-to-clean`

Drive a feature or bugfix from source evidence through an open, ready, review-clean GitHub pull request. The skill verifies claims, works on an isolated branch, tests and publishes changes, resolves review feedback, handles linked follow-up PRs, and requires two clean polling cycles before stopping.

### `consult-cursor-agent`

Use Cursor Grok 4.5 as a read-only, independent consultant for evidence-backed cross-agent deliberation. It preserves one Cursor chat across follow-up rounds and keeps implementation authority with the calling agent.

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
	└── drive-github-pr-to-clean/
			├── SKILL.md
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
