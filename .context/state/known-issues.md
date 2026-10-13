# Known Issues

Known bugs or limitations not yet fixed, so Claude doesn't "rediscover" them or try to fix them without being asked. Remove the entry once resolved.

- **`material-clase/4_Kmeans_Imagenes.ipynb` no corre en local tal cual**: usa `google.colab.files.upload()` (solo Colab) y `sklearn.cluster.KMeans` (`scikit-learn` no está en `requirements.txt`). Decisión pendiente del usuario: agregar `scikit-learn` o usar `cv2.kmeans` (alternativa sin dependencia nueva, ver `curso/10-kmeans.md` §5). No se modifica el notebook: es material del profesor.
- **Código de CNN (`curso/11-cnn.md` §6) requiere TensorFlow/Keras**, no aprobado en `requirements.txt`. Pedir confirmación antes de agregarlo cuando haya un trabajo de CNN.
- **`material-clase/3_OperacionesMatemáticas.ipynb` descarga una imagen por URL (Unsplash)** con `urllib`: necesita internet.
- **`trabajos/03-analisis-facial/models/face_landmarker.task` (~3.7 MB)** está versionado en git (decisión: junto al trabajo, ver `constraints.md`).
