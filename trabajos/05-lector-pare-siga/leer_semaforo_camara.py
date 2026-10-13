"""
Runner: lee el semaforo (PARE/SIGA) en vivo desde la webcam.

Toda la logica de deteccion vive en semaforo_detector.py; este script
solo se encarga de abrir la camara y mostrar los resultados frame a frame.
"""

import cv2

from semaforo_detector import leer_semaforo


def main():
    # cv2.VideoCapture(0) abre la camara por defecto del equipo.
    captura = cv2.VideoCapture(0)

    # Seccion 11.1 del temario: siempre verificar que la camara abrio bien
    # antes de seguir, para no reventar mas adelante con errores raros.
    if not captura.isOpened():
        print("No se pudo abrir la camara.")
        return

    while True:
        ok, frame = captura.read()  # ok=False si ya no hay mas frames o fallo la lectura
        if not ok:
            print("No se pudo leer un frame de la camara.")
            break

        estado, salida, mascara_debug = leer_semaforo(frame)

        cv2.imshow("Lector PARE / SIGA", salida)
        cv2.imshow("Mascara (rojo+verde)", mascara_debug)  # ventana de depuracion

        # cv2.waitKey(1) espera 1 ms por una tecla; & 0xFF aisla el byte
        # bajo del codigo de tecla para comparar con ord('q') de forma segura.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
