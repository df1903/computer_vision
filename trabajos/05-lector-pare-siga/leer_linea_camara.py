"""
Runner: detecta la linea negra en vivo desde la webcam.

Toda la logica vive en linea_negra_detector.py; este script solo abre la
camara y muestra los resultados frame a frame.
"""

import cv2

from linea_negra_detector import detectar_linea_negra


def main():
    captura = cv2.VideoCapture(0)

    if not captura.isOpened():
        print("No se pudo abrir la camara.")
        return

    while True:
        ok, frame = captura.read()
        if not ok:
            print("No se pudo leer un frame de la camara.")
            break

        _, _, salida, mascara = detectar_linea_negra(frame)

        cv2.imshow("Linea negra", salida)
        cv2.imshow("Mascara (negro)", mascara)  # ventana de depuracion

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
