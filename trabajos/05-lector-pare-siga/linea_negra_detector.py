"""
Detector de linea negra.

Mismo esquema que semaforo_detector.py, pero segmentando NEGRO:

  Imagen BGR
    -> Tema 5/6: suavizado Gaussiano para reducir ruido.
    -> Tema 3.2: BGR -> HSV.
    -> Tema 3.3: cv2.inRange. El negro no tiene un matiz propio: se
       caracteriza por V (brillo) bajo, sin importar H ni S.
    -> Tema 8: apertura + cierre para limpiar la mascara.
    -> Tema 9: findContours + contourArea, nos quedamos con el contorno
       mas grande (la linea). Momentos (cv2.moments) para el centroide.
    -> Error horizontal = centroide_x - centro de la imagen (util para
       saber hacia que lado esta la linea).
"""

import cv2
import numpy as np

# Negro en HSV: H y S libres, V bajo. Subir V_MAX si la linea sale gris por
# iluminacion; bajarlo si se cuelan sombras u objetos oscuros.
NEGRO_BAJO = np.array([0, 0, 0])
# La cinta real se ve gris oscuro (V~80), no negro puro; el fondo claro tiene V>200.
NEGRO_ALTO = np.array([179, 90, 120])

# Se ignoran bordes negros del video y la parte baja (donde sale el robot).
MARGEN_LATERAL = 0.06
MARGEN_INFERIOR = 0.14

# Area minima (en pixeles) para descartar ruido.
AREA_MINIMA = 500


def _mascara_negra(hsv):
    """Mascara binaria del negro (Tema 3.3): solo se limita el brillo V."""
    return cv2.inRange(hsv, NEGRO_BAJO, NEGRO_ALTO)


def _limpiar_mascara(mascara):
    """Apertura (quita ruido) y cierre (rellena huecos), Tema 8."""
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    abierta = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    return cv2.morphologyEx(abierta, cv2.MORPH_CLOSE, kernel)


def _contorno_mas_grande(mascara):
    """Devuelve el contorno de mayor area (>= AREA_MINIMA) o None (Tema 9)."""
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = [c for c in contornos if cv2.contourArea(c) >= AREA_MINIMA]
    if not contornos:
        return None
    return max(contornos, key=cv2.contourArea)


def detectar_linea_negra(frame):
    """
    Recibe un frame BGR y devuelve:
      - encontrada: True si se detecto la linea negra
      - error: pixeles entre el centroide de la linea y el centro de la
        imagen (negativo = izquierda, positivo = derecha), o None
      - salida: copia del frame con contorno, recuadro y centroide
      - mascara: mascara binaria del negro (para depurar rangos)
    """
    suavizado = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(suavizado, cv2.COLOR_BGR2HSV)
    mascara = _limpiar_mascara(_mascara_negra(hsv))

    salida = frame.copy()
    alto, ancho = frame.shape[:2]
    m_x = int(ancho * MARGEN_LATERAL)
    mascara[:, :m_x] = 0
    mascara[:, ancho - m_x:] = 0
    mascara[int(alto * (1 - MARGEN_INFERIOR)):, :] = 0
    cv2.line(salida, (ancho // 2, 0), (ancho // 2, alto), (255, 0, 0), 1)  # BGR: azul, centro

    contorno = _contorno_mas_grande(mascara)
    if contorno is None:
        cv2.putText(salida, "SIN LINEA", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.1,
                    (255, 255, 255), 3, cv2.LINE_AA)
        return False, None, salida, mascara

    x, y, w, h = cv2.boundingRect(contorno)
    m = cv2.moments(contorno)
    cx = int(m["m10"] / m["m00"])  # centroide = momento de orden 1 / area
    cy = int(m["m01"] / m["m00"])
    error = cx - ancho // 2

    cv2.drawContours(salida, [contorno], -1, (0, 255, 0), 2)
    cv2.rectangle(salida, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.circle(salida, (cx, cy), 8, (0, 0, 255), -1)
    cv2.putText(salida, f"LINEA error={error}px", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                (255, 255, 255), 3, cv2.LINE_AA)

    return True, error, salida, mascara
