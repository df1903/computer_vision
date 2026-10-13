# Filtros Morfológicos — Bordes en Vivo

`filtros.py` abre la cámara y muestra un mosaico 2x2 en vivo: original, escala de grises, blur gaussiano, y bordes (Canny) con una operación morfológica ajustable encima.

## Cómo funciona

1. Convierte cada frame a escala de grises.
2. Aplica `cv2.GaussianBlur` con un kernel ajustable (trackbar "Kernel Gauss", forzado a impar).
3. Detecta bordes con `cv2.Canny`, usando umbrales bajo/alto ajustables por trackbar.
4. Aplica dilatación/erosión sobre los bordes, en el orden elegido con el mouse (panel superior izquierdo de la ventana): "Dilatación → Erosión" o "Erosión → Dilatación".

## Controles

- Trackbars: `Umbral Bajo`, `Umbral Alto` (Canny), `Kernel Gauss`, `Dilatar`, `Erosionar` (iteraciones).
- Click en el panel superior izquierdo para cambiar el orden dilatación/erosión.
- `q` o `Esc` cierra la ventana.

## Correr

```
../../venv/Scripts/python.exe filtros.py
```

o con el venv activado:

```
python filtros.py
```
