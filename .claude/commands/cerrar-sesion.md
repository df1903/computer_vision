---
description: Cierra la sesión: actualiza state/, crea el siguiente handoff y registra decisiones
---

Cierra la sesión de trabajo actual.

1. Actualiza `.context/state/active-tasks.md`, `progress.md` y `known-issues.md` si cambió algo.
2. Crea el siguiente `.context/handoffs/NNN.md` (qué se hizo, qué falta, qué decidir). Nunca edites un handoff anterior.
3. Si hubo una decisión que afecta a todo el repo, añade una entrada a `.context/project/decisions.md`.
4. Resume en pocas líneas lo que quedó. No hagas commit salvo que el usuario lo pida.
