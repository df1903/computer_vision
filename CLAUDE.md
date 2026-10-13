# CLAUDE.md

Repo de curso universitario de Visión Artificial (Python + OpenCV). No es un producto único: es una colección de trabajos/retos/actividades independientes que comparten stack y entorno.

## Al iniciar sesión, leer en este orden

1. `.context/curso/temario.md` — contexto del curso: temario, convenciones del profesor (BGR, nombres en español, etc.), instrucciones específicas de estilo. **Lee esto siempre que vayas a escribir o explicar código de visión artificial.** Índice del resto del curso (K-Means, CNN, estado de cortes) en `.context/curso/README.md`.
2. `.context/state/active-tasks.md` — qué trabajo está en curso ahora mismo.
3. `.context/handoffs/` — el `NNN.md` más reciente, para saber qué se hizo en la última sesión.
4. Si vas a tocar un trabajo existente: su propio `trabajos/NN-nombre/README.md`.

## Estado del curso

- **Primer corte: cerrado** (Fundamentos → K-Means). Ver `.context/curso/corte-1.md`.
- **Segundo corte: abierto** (CNN en adelante). Trabajos entregados: 01–05, todos del primer corte.

## Estructura física del repo

- `trabajos/NN-nombre-corto/` — un trabajo/reto/actividad evaluativa por carpeta, numerado secuencialmente sin importar el tema. Cada uno tiene su propio `README.md` con enunciado y notas. Ver `.context/directory-structure.md` para la convención completa.
- `material-clase/` — notebooks y material entregado en clase (no evaluativo, fuente cruda; índice en su `README.md`).
- `requirements.txt` y `venv/` en la raíz — **compartidos por todos los trabajos**. Nunca crear un venv o requirements.txt dentro de una carpeta de `trabajos/`; si un trabajo necesita una librería nueva, se agrega aquí. Ver `.context/constraints.md`.

## Conocimiento estable (consultar según se necesite)

- `.context/curso/` — temario y contexto del curso: `temario.md` (base), `10-kmeans.md`, `11-cnn.md`, `corte-1.md`; crece con nuevos `NN-tema.md` por tema.
- `.context/stack.md` — stack aprobado y cómo se instala/ejecuta.
- `.context/coding-standards.md` — estilo de código.
- `.context/constraints.md` — restricciones no negociables (venv único, etc.).
- `.context/instructions.md` — cómo prefiero que trabajes en este repo.
- `.context/directory-structure.md` — convención de nombres y qué va en cada carpeta.
- `.context/project/decisions.md` — decisiones globales del repo.

## Al terminar una sesión de trabajo significativa

- Actualiza `.context/state/active-tasks.md` y `known-issues.md` si cambió el estado.
- Crea el siguiente `.context/handoffs/NNN.md` con qué se hizo, qué falta, qué decidir.
- Si tomaste una decisión que afecta a todo el repo (ej. cambio de convención), regístrala en `.context/project/decisions.md`.

## `.claude/`

Agentes, skills, comandos y permisos propios del repo — ver `.claude/README.md`. Comandos: `/nuevo-trabajo`, `/cerrar-sesion`.

## Commits

Conventional Commits en español, cortos, un tema por commit. Claude nunca figura como autor ni coautor. Detalle en `.context/instructions.md`.
