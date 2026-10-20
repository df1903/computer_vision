# Known Issues

Known bugs or limitations not yet fixed, so Claude doesn't "rediscover" them or try to fix them without being asked. Remove the entry once resolved.

- **`material-clase/4_Kmeans_Imagenes.ipynb` no corre en local tal cual**: usa `google.colab.files.upload()` (solo Colab); hay que cambiarla por `cv2.imread`. `scikit-learn` ya está en `requirements.txt` (aprobado con el trabajo 06). No se modifica el notebook: es material del profesor.
- **`trabajos/06-cnns/` no se ha ejecutado en este venv**: `tensorflow` y `scikit-learn` se añadieron a `requirements.txt` (el resolvedor de pip los acepta en Python 3.13, TensorFlow 2.21) pero aún no se instalaron ni se corrió `main.py`. `main.py` trae `max_epochs: 3` (prueba rápida) y entrena solo `ResNet50`.
- **`material-clase/3_OperacionesMatemáticas.ipynb` descarga una imagen por URL (Unsplash)** con `urllib`: necesita internet.
- **`trabajos/03-analisis-facial/models/face_landmarker.task` (~3.7 MB)** está versionado en git (decisión: junto al trabajo, ver `constraints.md`).
