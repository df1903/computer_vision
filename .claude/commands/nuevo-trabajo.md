---
description: Crea la carpeta de un trabajo nuevo en trabajos/NN-nombre/ con su README
argument-hint: <nombre-corto> [enunciado]
---

Crea un trabajo nuevo del curso con el nombre `$ARGUMENTS`.

1. Lee `.context/directory-structure.md` y `.context/coding-standards.md`.
2. Calcula el siguiente número `NN` mirando `trabajos/` (secuencial, 2 dígitos).
3. Crea `trabajos/NN-nombre-corto/` con un `README.md` (qué es, cómo correrlo, notas de ajuste) siguiendo el estilo de `trabajos/05-lector-pare-siga/README.md`.
4. No crees venv ni `requirements.txt` locales. Si falta una librería, pide confirmación antes de agregarla al `requirements.txt` raíz.
5. Actualiza `.context/state/active-tasks.md` y `.context/state/progress.md`, y la lista de trabajos del `README.md` raíz.
