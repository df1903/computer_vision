"""
Lector de semaforo: PARE (rojo) y SIGA (verde).

Pipeline completo, armado unicamente con temas vistos en el curso
(ver .context/curso/temario.md):

  Imagen BGR
    -> Tema 3 (Espacios de color): BGR -> HSV, para segmentar color
       aislado del brillo.
    -> Tema 3.3 / Tema 6 (AND / mascaras): cv2.inRange genera una mascara
       binaria; cv2.bitwise_and se usa para ver el resultado recortado.
    -> Tema 8 (Operaciones morfologicas): apertura (erosion+dilatacion)
       para quitar ruido, cierre (dilatacion+erosion) para rellenar huecos.
    -> Tema 9 (Deteccion de figuras geometricas): findContours +
       contourArea + circularidad (4*pi*area/perimetro^2) para quedarnos
       solo con blobs redondos (el foco del semaforo), no con cualquier
       objeto rojo o verde de la escena.
    -> Decision PARE/SIGA segun cual color tiene el blob redondo mas
       grande.

No se usa ningun modelo entrenado ni deteccion de objetos por IA: todo
el "reconocimiento" es color (HSV) + forma (contornos), que es lo que
cubre el temario.
"""

import cv2
import numpy as np

# --- Tema 3.3: rangos HSV aproximados para rojo y verde -------------------
# En OpenCV H va de 0 a 179. El rojo "da la vuelta" al circulo de matices,
# por eso necesita DOS rangos (0-10 y 170-179) unidos con bitwise_or,
# exactamente como se explica en la seccion 3.3 del temario.
ROJO_BAJO_1 = np.array([0, 120, 70])
ROJO_ALTO_1 = np.array([10, 255, 255])
ROJO_BAJO_2 = np.array([170, 120, 70])
ROJO_ALTO_2 = np.array([179, 255, 255])

# El verde no cruza el limite 0/179, con un solo rango alcanza.
VERDE_BAJO = np.array([35, 80, 70])
VERDE_ALTO = np.array([85, 255, 255])

# Area minima (en pixeles) para descartar puntos de ruido que sobreviven
# a la limpieza morfologica (Tema 8).
AREA_MINIMA = 300

# Que tan "redondo" debe ser un blob para contar como foco de semaforo.
# circularidad = 1 es un circulo perfecto (Tema 9.5, formula 4*pi*A/P^2).
CIRCULARIDAD_MINIMA = 0.55


def _mascara_roja(hsv):
    """Combina los dos rangos de rojo (Tema 3.3) en una sola mascara binaria."""
    mascara_1 = cv2.inRange(hsv, ROJO_BAJO_1, ROJO_ALTO_1)  # rojo cerca de H=0
    mascara_2 = cv2.inRange(hsv, ROJO_BAJO_2, ROJO_ALTO_2)  # rojo cerca de H=179
    return cv2.bitwise_or(mascara_1, mascara_2)  # Tema 6: operacion logica entre mascaras


def _mascara_verde(hsv):
    """Mascara binaria del verde (Tema 3.3): un solo rango de H alcanza."""
    return cv2.inRange(hsv, VERDE_BAJO, VERDE_ALTO)


def _limpiar_mascara(mascara):
    """
    Limpieza morfologica de la mascara binaria (Tema 8).

    - Apertura (erosion -> dilatacion): borra puntos sueltos de ruido
      sin encoger de forma notoria el blob grande del foco.
    - Cierre (dilatacion -> erosion): rellena huequitos internos que
      deja el reflejo del foco, para que quede un blob solido.
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    abierta = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    cerrada = cv2.morphologyEx(abierta, cv2.MORPH_CLOSE, kernel)
    return cerrada


def _mejor_blob_circular(mascara):
    """
    Busca, dentro de una mascara binaria, el contorno mas grande que
    ademas sea razonablemente circular (Tema 9: findContours,
    contourArea, arcLength y circularidad).

    Devuelve (x, y, w, h, area) del mejor blob, o None si no hay ninguno
    que cumpla el area minima y la circularidad minima.
    """
    # Tema 9.5: findContours necesita una imagen binaria (nuestra mascara
    # limpia); RETR_EXTERNAL porque solo nos importa el contorno exterior.
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mejor = None
    mejor_area = 0
    for contorno in contornos:
        area = cv2.contourArea(contorno)          # Tema 9.5: cv2.contourArea
        if area < AREA_MINIMA:
            continue

        perimetro = cv2.arcLength(contorno, True)  # Tema 9.5: cv2.arcLength
        if perimetro == 0:
            continue

        # Formula de circularidad del temario (seccion 9.5): 1.0 = circulo
        # perfecto. Sirve para distinguir el foco redondo de otros objetos
        # rojos/verdes de la escena que no son circulares.
        circularidad = 4 * np.pi * area / (perimetro ** 2)
        if circularidad < CIRCULARIDAD_MINIMA:
            continue

        if area > mejor_area:
            mejor_area = area
            x, y, w, h = cv2.boundingRect(contorno)  # Tema 9.4: boundingRect
            mejor = (x, y, w, h, area)

    return mejor


def leer_semaforo(frame):
    """
    Recibe un frame BGR (una imagen de camara/video) y devuelve:
      - estado: "PARE", "SIGA" o "SIN DETECCION"
      - salida: copia del frame con el recuadro y el texto dibujados
      - mascara_debug: mascara binaria combinada (rojo+verde), util para
        ver que esta detectando el algoritmo mientras se ajustan rangos.
    """
    # Tema 5.4 / Tema 6: suavizar primero (Gaussiano) reduce ruido antes
    # de segmentar por color, igual que en la receta 10.1 del temario.
    suavizado = cv2.GaussianBlur(frame, (5, 5), 0)

    # Tema 3.2: convertir de BGR (formato nativo de OpenCV) a HSV, porque
    # en HSV el color (H) queda separado del brillo (V) y la segmentacion
    # es mas robusta a cambios de iluminacion.
    hsv = cv2.cvtColor(suavizado, cv2.COLOR_BGR2HSV)

    mascara_rojo = _limpiar_mascara(_mascara_roja(hsv))
    mascara_verde = _limpiar_mascara(_mascara_verde(hsv))

    blob_rojo = _mejor_blob_circular(mascara_rojo)
    blob_verde = _mejor_blob_circular(mascara_verde)

    salida = frame.copy()
    # Mascara combinada solo para depurar visualmente (Tema 6: bitwise_or).
    mascara_debug = cv2.bitwise_or(mascara_rojo, mascara_verde)

    if blob_rojo is None and blob_verde is None:
        estado = "SIN DETECCION"
    elif blob_rojo is not None and (blob_verde is None or blob_rojo[4] >= blob_verde[4]):
        # Gana el rojo si es el unico o si su area es mayor o igual que la del verde.
        estado = "PARE"
        x, y, w, h, _ = blob_rojo
        cv2.rectangle(salida, (x, y), (x + w, y + h), (0, 0, 255), 3)  # BGR: rojo puro
    else:
        estado = "SIGA"
        x, y, w, h, _ = blob_verde
        cv2.rectangle(salida, (x, y), (x + w, y + h), (0, 255, 0), 3)  # BGR: verde puro

    # cv2.putText con fuente Hershey no soporta tildes/enye (seccion 0 y
    # 11.1 del temario) -> el texto se escribe sin acentos a proposito.
    cv2.putText(salida, estado, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.1,
                (255, 255, 255), 3, cv2.LINE_AA)

    return estado, salida, mascara_debug
