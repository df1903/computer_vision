# Constraints

- **Un solo venv, una sola `requirements.txt`, en la raíz.** Ningún trabajo bajo `trabajos/` tiene su propio entorno o su propio archivo de dependencias. Motivo: evitar reinstalar librerías pesadas (opencv, mediapipe) por cada tarea.
- `venv/`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/` van en `.gitignore` (ya configurado) — nunca versionar el venv.
- Los trabajos son independientes entre sí: no crear imports cruzados entre carpetas de `trabajos/` salvo decisión explícita del usuario.
- Archivos de modelos pesados (ej. `face_landmarker.task` en `trabajos/03-analisis-facial/models/`) se versionan junto al trabajo que los usa, no se centralizan, salvo que el usuario decida lo contrario.
