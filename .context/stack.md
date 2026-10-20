# Stack

- **Lenguaje:** Python 3.13.
- **Entorno:** un único `venv/` en la raíz del repo, compartido por todos los trabajos. Se activa con `venv/Scripts/activate` (Windows) o se llama directo con `venv/Scripts/python.exe`.
- **Dependencias:** un único `requirements.txt` en la raíz. Instalar con `venv\Scripts\pip.exe install -r requirements.txt`. Si un trabajo necesita una librería nueva, se añade aquí, no en un requirements.txt local.

## Librerías actuales (`requirements.txt`)

- `opencv-contrib-python` — visión artificial (núcleo del curso).
- `numpy` — arrays/álgebra.
- `matplotlib` — visualización cuando OpenCV no basta.
- `jupyter`, `ipykernel` — notebooks de `material-clase/`.
- `mediapipe` — detección de landmarks (usado en `trabajos/03-analisis-facial/`).
- `tensorflow` (incluye `keras`) — CNN y transfer learning (usado en `trabajos/06-cnns/`, ver `.context/curso/11-cnn.md`).
- `scikit-learn` — métricas (`classification_report`, matriz de confusión) en `trabajos/06-cnns/`; también `KMeans` en `material-clase/4_Kmeans_Imagenes.ipynb` (alternativa sin dependencia: `cv2.kmeans`).

Si algo no está aquí, no está aprobado: pídele al usuario confirmación antes de agregar una dependencia nueva.

## Documentación y comandos del repo

- Commits: Conventional Commits (`tipo(ámbito): descripción corta en español`). Ver `AGENTS.md`.
