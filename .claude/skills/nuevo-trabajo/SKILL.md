---
name: nuevo-trabajo
description: Crea la carpeta de un trabajo nuevo en trabajos/NN-nombre/ con su README. Úsala cuando el usuario anuncie un trabajo, reto o actividad evaluativa nueva.
disable-model-invocation: true
argument-hint: <nombre-corto> [enunciado]
metadata:
  version: "1.0"
---
# Nuevo trabajo

Crea un trabajo nuevo del curso con el nombre `$ARGUMENTS`.

1. Lee `.context/conventions.md`.
2. Calcula el siguiente `NN` mirando `trabajos/` (secuencial, 2 dígitos).
3. Crea `trabajos/NN-nombre-corto/` con un `README.md` (qué es, cómo correrlo, notas de ajuste) siguiendo el estilo de `trabajos/05-lector-pare-siga/README.md`.
4. No crees venv ni `requirements.txt` locales. Si falta una librería, pide confirmación antes de agregarla al `requirements.txt` raíz y consulta `.context/stack.md`.
5. Actualiza `.context/state/current.md` (tareas activas y tabla de avance) y la lista de trabajos del `README.md` raíz.
