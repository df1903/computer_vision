# Decisions (project-global)

## 2026-09-21 — Reorganización del repo a modelo "curso" en vez de "proyecto"

Contexto: el scaffold `.context/`/`.claude/` inicial (plantilla `sdd-NNN`, fases, requirements) está pensado para un producto único con ciclo de desarrollo. Este repo es en realidad una colección de trabajos aislados de un curso universitario, algunos planeados y otros improvisados en clase.

Decisión:
- Trabajos de código pasan a vivir en `trabajos/NN-nombre-corto/` (antes sueltos en la raíz: `task_1`, `camara_color`, `facial_analysis`, `filtros.py`).
- Material del profesor pasa a `material-clase/` (antes `class_material/`).
- El contexto del curso (`fundamentos_vision_artificial_contexto.md`) pasa a `.context/curso/temario.md`, pensado para crecer con nuevos temas.
- Se elimina el concepto de `sdd-NNN` (feature con ciclo propio) y de fases de proyecto; se reemplaza por `trabajos/` + `state/active-tasks.md`.
- Se mantiene un único `venv/` y `requirements.txt` en la raíz para todos los trabajos (ya era así, se formaliza como restricción en `constraints.md`).

Alternativas descartadas: mantener cada trabajo en la raíz sin carpeta contenedora (rechazado: no escala con más entregas ni se distingue de material de clase o config).

## 2026-10-13 — Primer corte cerrado hasta K-Means; contexto por corte

Contexto: se cerró el primer corte del curso. Llegó material nuevo (K-Means, CNN) y el contexto debía reflejar qué pertenece a cada corte.

Decisión:
- El primer corte abarca desde Fundamentos hasta **K-Means** inclusive. CNN y arquitecturas reconocidas se tratan como **inicio del segundo corte**.
- El contexto curado vive en `.context/curso/` con archivos `NN-tema.md` (continuando desde `10`); `temario.md` no se parte. `curso/corte-1.md` fija el alcance del corte y `curso/README.md` indexa.
- Las fuentes crudas (transcripciones, notebooks) permanecen en `material-clase/` con un `README.md` índice; no se editan.
- Dependencias que exigen el material nuevo (`scikit-learn`, TensorFlow/Keras) **no** se agregan sin confirmación del usuario; quedan registradas en `state/known-issues.md`.
- Commits: Conventional Commits en español, cortos, un tema por commit, **sin** coautoría ni mención de IA como autor.

Alternativas descartadas: partir `temario.md` por tema (rompe su rol de documento base enriquecido); agregar `scikit-learn`/TensorFlow de entrada (viola la regla de dependencias aprobadas).
