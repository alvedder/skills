# Repository instructions

- Treat `skills/` as the source of truth.
- Store each skill in `skills/<skill-name>/`.
- Keep the folder name and `SKILL.md` frontmatter `name` identical.
- Require valid YAML frontmatter with `name` and `description`.
- Keep skill instructions portable; isolate agent-specific metadata under `agents/`.
- Keep the root README catalog synchronized with the skills present.
- Run `npx skills add . --list` before publishing.
- Never commit credentials, private repository data, or task-specific artifacts.
- Do not push unless the user explicitly requests it.
