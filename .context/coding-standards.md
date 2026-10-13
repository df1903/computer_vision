# Coding Standards

- Scripts sueltos por trabajo (no paquetes complejos), estilo ya usado en `trabajos/01-deteccion-color-amarillo/` y `trabajos/03-analisis-facial/`: un módulo con la lógica compartida (ej. `yellow_detector.py`, `face_metrics.py`) y uno o más scripts "runner" que la usan.
- Rutas a archivos propios de un trabajo (modelos, assets) se resuelven con `os.path.join(os.path.dirname(__file__), ...)`, nunca rutas relativas al cwd — así cada trabajo corre igual sin importar desde dónde se invoque.
- Nombres de variables: en español cuando el curso los usa así (`imagen`, `gris`, `bordes`, `umbral`), en inglés si el trabajo es autocontenido y no sigue terminología del curso. Mantener consistencia dentro de cada trabajo, no mezclar en el mismo archivo.
- `cv2.putText` no soporta tildes/ñ con fuentes Hershey: usar texto sin acentos.
- Siempre verificar que `cv2.imread` / `cv2.VideoCapture` no hayan fallado antes de seguir.
- README por trabajo: qué hace, cómo correrlo, notas de ajuste/tuning si aplica (ver los README existentes como plantilla).
