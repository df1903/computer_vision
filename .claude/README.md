# .claude/

**Native** Claude Code configuration for this project. Everything here is read directly by the harness (agents, skills, commands, permissions) — no one needs to point to it manually.

- `agents/` — this project's own specialized subagents (`.md` with frontmatter: name, description, tools).
- `skills/` — this project's own skills invokable with `/name`.
- `commands/` — simple slash commands (a fixed, reusable prompt).
- `settings.json` — project permissions and configuration. Versioned in git.
- `settings.local.json` (not included, created only if needed) — local/machine overrides, goes in `.gitignore`, never versioned.

Difference from `.context/`: this is "how the harness operates"; `.context/` is "what it knows about the project." The bridge between the two is the root `CLAUDE.md`.

## Contenido actual (2026-10-13)

| Ruta | Qué hay |
|---|---|
| `agents/vision-artificial-cv.md` | Implementa y depura scripts de visión artificial del curso (temas 1-9 + K-Means). |
| `commands/nuevo-trabajo.md` | `/nuevo-trabajo <nombre>`: crea `trabajos/NN-nombre/` con README. |
| `commands/cerrar-sesion.md` | `/cerrar-sesion`: actualiza `state/`, crea el siguiente handoff y registra decisiones. |
| `settings.json` | Permite lecturas de git y el Python del venv raíz; deniega `git push`, `reset --hard`, `rm -rf`. |
