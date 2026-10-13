# Espacios de Color — Cámara en Vivo

`camera_color_spaces.py` abre la cámara y muestra en una sola ventana un mosaico 3x3 con el mismo frame convertido a distintos espacios de color: BGR (original), RGB, escala de grises, HSV, HLS, CIELAB, CIELUV, YCrCb y XYZ.

## Cómo funciona

Cada frame se redimensiona a 320x240 y se convierte con `cv2.cvtColor` a cada espacio de color usando las constantes `COLOR_BGR2*`. Todas las conversiones parten del mismo frame BGR capturado por la cámara, para poder comparar el mismo instante en distintos espacios.

## Correr

```
../../venv/Scripts/python.exe camera_color_spaces.py
```

o con el venv activado:

```
python camera_color_spaces.py
```

Presiona `q` para cerrar.
