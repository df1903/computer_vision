# AGENTS.md

> Fuente portable de instrucciones para agentes de IA. Mantén este archivo corto: solo hechos y reglas.
> El detalle vive en `.context/` y se lee **bajo demanda** (no lo cargues todo de entrada).

## Proyecto
Repo de curso universitario de Visión Artificial (Python + OpenCV, Universidad de Caldas). No es un producto único: es una colección de trabajos/retos/actividades independientes en `trabajos/NN-nombre/` que comparten stack y entorno.
Estado: primer corte cerrado (Fundamentos → K-Means); segundo corte abierto (CNN en adelante).

## Comandos
- Instalar: `venv\Scripts\pip.exe install -r requirements.txt`
- Ejecutar un trabajo: `venv/Scripts/python.exe trabajos/NN-nombre/<script>.py`
- Tests / lint: no hay.

## Inicio de sesión (leer en este orden)
1. `.context/state/current.md`
2. El último `.context/handoffs/NNN.md`
3. Si vas a escribir o explicar código de visión artificial: `.context/curso/temario.md` (convenciones del profesor: BGR, nombres en español, etc.)
4. Si tocas un trabajo existente: su `trabajos/NN-nombre/README.md`

## Conocimiento del proyecto (leer solo si hace falta)
| Cuándo | Archivo |
|---|---|
| Antes de añadir una dependencia o tecnología | `.context/stack.md` (si no está aquí, no está aprobado: pregunta) |
| Antes de proponer algo estructural | `.context/constraints.md` (prevalece sobre tus propuestas) |
| Antes de crear un archivo, nombrar algo o escribir código | `.context/conventions.md` |
| Al explicar o escribir código del curso / llega material nuevo | `.context/curso/README.md` (índice: `temario.md`, `10-kmeans.md`, `11-cnn.md`, `corte-1.md`) |
| Al tomar o consultar decisiones previas | `.context/project/decisions.md` |
| Problemas ya conocidos (no los redescubras ni arregles sin que se pida) | `.context/state/known-issues.md` |

## Cómo trabajar
- Cambios pequeños y verificables; ejecuta el script para comprobar que corre antes de darlo por terminado.
- Si hay ambigüedad en el alcance, pregunta antes de implementar.
- No añadas dependencias, carpetas de primer nivel ni abstracciones que no se hayan pedido.
- Trabajos aislados: no mezcles código entre `trabajos/` ni refactorices entre ellos salvo petición explícita.
- Material nuevo del profesor: fuente cruda en `material-clase/` (listada en su `README.md`); versión curada en `.context/curso/NN-tema.md`.
- Antes de cerrar o abrir un corte, actualiza `.context/curso/corte-N.md` y `.context/state/current.md`.
- Una decisión que persiste → regístrala en `.context/project/decisions.md`.
- **Commits**: Conventional Commits (`feat`, `fix`, `docs`, `refactor`, `chore`), ámbito opcional (`trabajo-05`, `context`, `material-clase`), descripción corta en español, imperativo, sin punto final, un tema por commit. Claude nunca figura como autor ni coautor (sin `Co-Authored-By`). Solo se commitea cuando el usuario lo pide.

## Reglas duras
- Un solo `venv/` y un solo `requirements.txt`, en la raíz. Nunca crear venv ni requirements dentro de `trabajos/`.
- Nunca leas ni escribas `.env*`, claves ni credenciales (también lo bloquea un hook).
- Nunca hagas `push --force` ni borres historial de git.
- No agregues `scikit-learn` ni TensorFlow/Keras sin confirmación (ver `known-issues.md`).

## Cierre de sesión
Al terminar un bloque de trabajo relevante, ejecuta la skill `close-session`
(actualiza `state/`, crea el siguiente handoff y registra decisiones).
Para un trabajo nuevo: skill `nuevo-trabajo`.
