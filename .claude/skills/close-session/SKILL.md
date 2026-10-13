---
name: close-session
description: Cierra una sesión de trabajo: actualiza el estado actual, crea el siguiente handoff numerado y registra decisiones. Úsala cuando el usuario diga "cerrar sesión", "guardar progreso" o "crear handoff".
disable-model-invocation: true
metadata:
  version: "1.0"
---
# Cierre de sesión

1. Lee `.context/state/current.md` y el último `.context/handoffs/NNN.md`.
2. **Sobrescribe** `.context/state/current.md` con la foto actual: fase, tareas activas (quita las cerradas), tabla de avance de trabajos y cortes.
3. Actualiza `.context/state/known-issues.md`: añade los problemas nuevos y quita los resueltos.
4. Crea `.context/handoffs/<NNN+1>.md` (3 dígitos) siguiendo `references/handoff-template.md`. Nunca edites un handoff anterior.
5. Si hubo una decisión que afecta a todo el repo, añade una entrada a `.context/project/decisions.md` (contexto, decisión, alternativas descartadas, fecha). No borres entradas.
6. Muestra un resumen de 5 líneas máximo con lo que cambió. No hagas commit salvo que el usuario lo pida.
