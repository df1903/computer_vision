# Trabajo 05 — Lector de semaforo: PARE y SIGA

Programa que mira un semaforo (por camara o por video) y decide si dice
**PARE** (foco rojo encendido) o **SIGA** (foco verde encendido). Solo usa
tecnicas vistas en el curso — sin modelos entrenados ni deteccion de
objetos por IA: color (HSV) + forma (contornos) + limpieza morfologica.

## Como funciona (`semaforo_detector.py`)

Pipeline, con la sección del temario (`.context/curso/temario.md`) que
corresponde a cada paso:

1. **Suavizado Gaussiano** (tema 5/6) — reduce ruido antes de segmentar
   por color.
2. **BGR → HSV** (tema 3.2) — separa el color (H) del brillo (V), así la
   detección es más robusta a cambios de iluminación.
3. **Segmentación por color con `inRange`** (tema 3.3) — dos rangos de
   rojo (el rojo "da la vuelta" al círculo de matices en H=0/179, por eso
   son dos rangos unidos con `bitwise_or`, ver tema 6) y un rango de
   verde.
4. **Limpieza morfológica** (tema 8) — apertura para quitar puntos de
   ruido, cierre para rellenar huecos dentro del foco (el reflejo del
   vidrio del semáforo suele dejar agujeritos en la máscara).
5. **Contornos + circularidad** (tema 9) — `findContours`, `contourArea`,
   `arcLength` y la fórmula de circularidad `4·π·área / perímetro²` para
   quedarnos solo con blobs redondos (el foco), descartando otros objetos
   rojos/verdes de la escena que no son circulares.
6. **Decisión** — si el blob rojo circular es más grande (o es el único),
   el estado es `PARE`; si gana el verde, `SIGA`; si no hay ningún blob
   válido, `SIN DETECCION`.
7. Se dibuja un recuadro sobre el foco detectado y el estado como texto
   (sin tildes, porque `cv2.putText` con fuentes Hershey no las soporta).

## `leer_semaforo_camara.py`

Corre el pipeline en vivo con la webcam.

```
python leer_semaforo_camara.py
```

Tecla `q` para cerrar.

## `leer_semaforo_video.py`

Mismo pipeline sobre un archivo de video.

```
python leer_semaforo_video.py ruta/al/video.mp4
```

Tecla `q` para cerrar.

## Notas / ajuste

- Los rangos HSV de rojo y verde en `semaforo_detector.py` (`ROJO_*`,
  `VERDE_*`) son un punto de partida; ajustarlos según la iluminación y
  el semáforo real que se use.
- `AREA_MINIMA` descarta blobs muy pequeños (ruido). `CIRCULARIDAD_MINIMA`
  descarta blobs que no sean razonablemente redondos (para no confundir
  el foco con otro objeto rojo/verde del fondo, como un carro).
- Se abren dos ventanas: el resultado final y la máscara binaria
  rojo+verde, para poder ver qué está detectando el algoritmo mientras se
  ajustan los rangos.
- Si el semáforo real tiene poca resolución o está muy lejos, el foco
  puede no salir suficientemente redondo para pasar el filtro de
  circularidad; en ese caso bajar `CIRCULARIDAD_MINIMA`.
