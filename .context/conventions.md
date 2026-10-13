# Conventions

> Estilo no obvio, ubicación de archivos y nombres. Se lee **antes de crear un archivo nuevo**. Se actualiza al cambiar una convención.

## Modelo del repo: curso, no producto
No hay fases de un proyecto único ni features con ciclo planning→implementación→testing. Hay **trabajos independientes** (tareas, retos, actividades evaluativas); algunos anunciados, otros improvisados en clase. Por eso no se usan `sdd-NNN-<slug>/`.

## Estilo de código
- Scripts sueltos por trabajo (no paquetes complejos), estilo de `trabajos/01-deteccion-color-amarillo/` y `trabajos/03-analisis-facial/`: un módulo con la lógica compartida (ej. `yellow_detector.py`, `face_metrics.py`) y uno o más scripts "runner" que la usan.
- Rutas a archivos propios de un trabajo (modelos, assets) con `os.path.join(os.path.dirname(__file__), ...)`, nunca relativas al cwd.
- Variables en español cuando el curso las usa así (`imagen`, `gris`, `bordes`, `umbral`); en inglés si el trabajo es autocontenido y no sigue terminología del curso. No mezclar en el mismo archivo.
- `cv2.putText` no soporta tildes/ñ con fuentes Hershey: texto sin acentos.
- Verificar que `cv2.imread` / `cv2.VideoCapture` no hayan fallado antes de seguir.
- Convenciones de visión artificial (BGR, etc.): `.context/curso/temario.md`.

## Dónde va cada archivo (código)
| Carpeta | Contenido |
|---|---|
| `trabajos/NN-nombre-corto/` | Un trabajo/reto/actividad: código + `README.md` (qué es, cómo correrlo, notas de ajuste). Aislado de los demás. |
| `material-clase/` | Notebooks y material del profesor. No evaluativo; fuente cruda, no se edita. |
| `requirements.txt`, `venv/` (raíz) | Entorno único compartido (ver `constraints.md`). |

## Nombres
- Trabajos: `trabajos/NN-nombre-corto-en-espanol/`, 2 dígitos secuenciales por orden de creación (no por tema).
- Archivos de contenido: `kebab-case-descriptivo.md`.
- Series (`handoffs/`): prefijo de 3 dígitos (`000`, `001`...). Nunca mezclar formatos en una serie.
- Contexto del curso: `curso/NN-tema.md`, numeración continua tras `10`; `temario.md` no se parte.
- No existe carpeta "otros": elige la categoría más cercana.

## Dónde va la información en `.context/`
1. ¿Contenido/temario del curso? → `curso/`.
2. ¿Afecta a todo el repo y persiste? → `project/decisions.md`.
3. ¿Es el estado actual (foto del momento)? → `state/current.md` (bugs/limitaciones: `state/known-issues.md`).
4. ¿Es historia de qué pasó en una sesión? → `handoffs/`.
5. ¿Código o enunciado de un trabajo? → `trabajos/NN-nombre/README.md`.

Estado se sobrescribe; historia se acumula (`handoffs/`, `decisions.md`).

## Cuándo crear `trabajos/NN-nombre/`
Cada vez que empiece un trabajo, reto o actividad evaluativa claramente delimitada, aunque sea pequeña. Un experimento rápido sin entregar puede vivir suelto hasta formalizarse.

## Commits
Ver `AGENTS.md` → "Cómo trabajar".
