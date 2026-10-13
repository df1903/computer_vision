# `.context/` y estructura del repo

Mapa de carpetas y convención de nombres. Leer antes de crear un archivo nuevo.

## Modelo de este repo: curso, no producto

No hay "fases" de un proyecto único ni features con ciclo planning→implementación→testing. Hay **trabajos independientes** (tareas, retos, actividades evaluativas) del mismo curso. Algunos se anuncian con anticipación, otros son improvisados en clase. La estructura está pensada para eso.

## Convención de nombres

- Trabajos: `trabajos/NN-nombre-corto-en-espanol/`, numeración secuencial de 2 dígitos por orden de creación (no por tema). Ej: `trabajos/01-deteccion-color-amarillo/`.
- Archivos de contenido: `descriptive-kebab-case.md`.
- Series (handoffs): prefijo numérico de 3 dígitos: `000`, `001`... Nunca mezclar convenciones dentro de una misma serie.

## Carpetas de nivel raíz

| Carpeta | Contenido |
|---|---|
| `trabajos/` | Un subdirectorio por trabajo/reto/actividad. Cada uno con su propio código y `README.md` (enunciado + cómo correrlo + notas). Trabajos aislados entre sí; no se importan código unos a otros salvo que se decida explícitamente. |
| `material-clase/` | Notebooks y material que reparte el profesor. No evaluativo, no se reorganiza por trabajo. |
| `requirements.txt`, `venv/` (raíz) | Entorno **único y compartido** para todo el repo. Ver `.context/constraints.md`. |
| `.context/` | Contexto para Claude (ver abajo). |
| `.claude/` | Configuración nativa del harness (agentes, skills, permisos). |

## Carpetas de `.context/`

| Carpeta | Qué va aquí | Cuándo se actualiza |
|---|---|---|
| `curso/` | Temario y contexto de la materia: `temario.md` es la base: pega ahí nuevos `.md` de temas que te vaya pasando el usuario, o añade archivos nuevos `curso/NN-tema.md` si el archivo crece demasiado. | Cuando el usuario pasa nuevo material o se cubre un tema nuevo en clase. |
| `.context/*.md` (raíz) | Conocimiento estable: stack, estilo de código, restricciones, instrucciones de trabajo. Cambia poco. | Al tomar una decisión técnica estructural. |
| `project/decisions.md` | Decisiones que afectan a todo el repo (convención de carpetas, cambio de venv, etc.). Una entrada por decisión, orden cronológico, no se borran entradas viejas. | Al tomar una decisión de ese tipo. |
| `state/` | Foto del momento actual: tareas activas, issues conocidos. Se sobreescribe, no se acumula historial. | Cada sesión de trabajo. |
| `handoffs/` | Log secuencial de qué se hizo/qué falta entre sesiones. | Al cerrar una sesión significativa. |

## Regla para decidir dónde va algo

- ¿Es contenido/temario del curso? → `.context/curso/`.
- ¿Es una decisión que afecta a todo el repo (estructura, entorno)? → `project/decisions.md`.
- ¿Es el estado actual (no una decisión, una foto)? → `state/`.
- ¿Es código o enunciado de un trabajo concreto? → `trabajos/NN-nombre/`, con su propio `README.md`.
- No cabe en nada de esto: usa el archivo más cercano, no crear carpetas nuevas sin necesidad.

## Cuándo crear un `trabajos/NN-nombre/` nuevo

Cada vez que empiece un trabajo, reto o actividad evaluativa nueva y claramente delimitada, aunque sea pequeña. Si es solo un experimento rápido sin entregar, puede vivir suelto hasta que se decida si se formaliza.
