# Instructions

Cómo prefiero que trabajes en este repo (curso de Visión Artificial).

- Cada trabajo nuevo va en `trabajos/NN-nombre-corto/` (ver `.context/directory-structure.md`). No mezclar código de trabajos distintos.
- Nunca instales dependencias dentro de una carpeta de trabajo ni crees un venv local ahí. Todo pasa por el `venv/` y `requirements.txt` de la raíz. Si falta una librería, agrégala a `requirements.txt` e instálala en el venv raíz.
- Antes de generar código de visión artificial, ten en cuenta las convenciones del curso en `.context/curso/temario.md` (BGR no RGB, `cv2.putText` sin tildes, nombres de variable en español cuando el curso los usa así, verificar `cv2.imread` no devuelva `None`, etc.).
- Cuando el usuario pase un `.md` nuevo de un tema, intégralo en `.context/curso/` (añádelo a `temario.md` o créalo como `curso/NN-tema.md` si es grande) en vez de dejarlo suelto en la raíz.
- Cada trabajo debe tener su propio `README.md`: qué es, cómo correrlo, notas de ajuste. Sigue el estilo ya usado en los trabajos existentes (ver ejemplos en `trabajos/`).
- Al cerrar una sesión de trabajo relevante, actualiza `.context/state/active-tasks.md` y crea el siguiente `.context/handoffs/NNN.md`.
- No asumas que un trabajo es "el proyecto"; son entregas aisladas. No refactorices entre trabajos ni crees abstracciones compartidas salvo que el usuario lo pida explícitamente.
- **Commits**: Conventional Commits (`feat`, `fix`, `docs`, `refactor`, `chore`), ámbito opcional (`trabajo-05`, `context`, `material-clase`), descripción corta en español en imperativo, sin punto final, una sola idea por commit. Claude **nunca** aparece como autor, coautor ni en el mensaje (sin `Co-Authored-By`). Solo se commitea cuando el usuario lo pide.
- Antes de dar un corte por cerrado o abrir otro, actualiza `.context/curso/corte-1.md` (o el archivo del corte) y `state/progress.md`.
- Material nuevo del profesor: la fuente cruda va a `material-clase/` (y se lista en su `README.md`); la versión curada va a `.context/curso/NN-tema.md`.
