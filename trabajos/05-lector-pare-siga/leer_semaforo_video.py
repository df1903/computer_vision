"""
Runner: lee el semaforo (PARE/SIGA) sobre un archivo de video.

Misma logica de deteccion que leer_semaforo_camara.py (semaforo_detector.py);
aqui la fuente de frames es un archivo de video en vez de la webcam.
"""

import os
import sys

import cv2

from semaforo_detector import leer_semaforo


def main():
    if len(sys.argv) < 2:
        print("Uso: python leer_semaforo_video.py ruta/al/video.mp4")
        return

    # Seccion 2.3 del temario / coding-standards.md: resolver rutas con
    # os.path para que el script funcione igual sin importar desde donde
    # se invoque; aqui el argumento ya viene dado por el usuario, solo
    # normalizamos separadores de ruta.
    ruta_video = os.path.normpath(sys.argv[1])

    captura = cv2.VideoCapture(ruta_video)

    # Verificar apertura antes de seguir (seccion 11.1 del temario).
    if not captura.isOpened():
        print(f"No se pudo abrir el video: {ruta_video}")
        return

    while True:
        ok, frame = captura.read()
        if not ok:
            break  # se acabo el video

        estado, salida, mascara_debug = leer_semaforo(frame)

        cv2.imshow("Lector PARE / SIGA", salida)
        cv2.imshow("Mascara (rojo+verde)", mascara_debug)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
