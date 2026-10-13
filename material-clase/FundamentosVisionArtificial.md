---
source: "FundamentosVisionArtificial.pdf"
format: "pdf"
converted: "2026-10-13"
title: "Fundamentos Visión Artificial"
lang: "es"
pages: 25
pdf_title: "Microsoft PowerPoint - 1_Fundamentos.pptx"
pdf_author: "Felipe"
pdf_creationDate: "D:20260915094857-05'00'"
running_text: ["Felipe Buitrago Carmona – Facultad Inteligencia Artificial e Ingenierías – Universidad de Caldas"]
images: 19
notes: ["Slide deck exported to PDF: every content page except the section dividers (pages 1, 9, 11, 14, 17, 21) is a full-page picture, so each was transcribed inside an <image> block", "p.3 the example matrix is labeled '(3x3 píxeles)' but is drawn as 4 rows of 5 pixels (2 yellow, 2 blue, 1 red per row) [sic]; kept verbatim", "p.19 case 1 step 3 has a few smeared glyphs in the third grid row (render artifact); transcribed as 0", "p.20 case 2 steps 1-2 grids have several blurred cells (render artifact); only cells readable with confidence are transcribed, others marked [?]", "p.5 and p.13 and p.16 contain example photos/illustrations; described in English, their on-image Spanish text is kept verbatim", "OCR cross-check ran without Spanish tesseract data (language pack not installable), so it is noisier than usual"]
---

<!-- page:1 -->
# Fundamentos Visión Artificial
felipe.buitrago@ucaldas.edu.co

<!-- page:2 -->
<image id="img-001" kind="slide-image" page="2">
## Imagen de Colombia como un cubo 3x3
(alto=3, ancho=3, canales=3 BGR)

Columna: 0, 1, 2. Fila: 0, 1, 2.

Colores en OpenCV (BGR)

| Color | Valor BGR |
|---|---|
| Amarillo | [0, 255, 255] |
| Azul | [255, 0, 0] |
| Rojo | [0, 0, 255] |

Cada píxel es un vector BGR

| Posición | Vector |
|---|---|
| (0,0) | [0, 255, 255] |
| (1,1) | [255, 0, 0] |
| (2,2) | [0, 0, 255] |

La imagen completa es un cubo (3x3x3)

Forma del cubo (imagen): (3, 3, 3) → alto, ancho, canales (BGR)

Cube labels: alto (3), ancho (3), canales (3).

visual: left, a 3x3 grid of colored cells: row 0 all yellow, row 1 all blue, row 2 all red (Colombian flag), with column indices 0-2 on top and row indices 0-2 on the left. Bottom right, a 3D cube drawn from the same grid with the depth axis labeled "canales (3)", height axis "alto (3)" and width axis "ancho (3)". Arrows below "(3, 3, 3)" point from each number to alto (blue), ancho (green) and canales (red).
</image>

<!-- page:3 -->
<image id="img-002" kind="slide-image" page="3">
## Representación BGR en OpenCV – Bandera de Colombia

Bandera de Colombia (vista normal)

En OpenCV, cada píxel se almacena en orden BGR (Azul, Verde, Rojo)

Estructura de un píxel en OpenCV

| B | G | R |
|---|---|---|
| 0 – 255 | 0 – 255 | 0 – 255 |

Valores BGR por cada color de la bandera

| Color (real) | Apariencia | Valor en OpenCV (B, G, R) |
|---|---|---|
| Amarillo | yellow swatch | ( 0, 255, 255 ) |
| Azul | blue swatch | ( 255, 0, 0 ) |
| Rojo | red swatch | ( 0, 0, 255 ) |

Descomposición de canales en OpenCV (BGR)

| Canal | Valores por fila |
|---|---|
| Canal B (Azul) | Amarillo → 0 \| Azul → 255 \| Rojo → 0 |
| Canal G (Verde) | Amarillo → 255 \| Azul → 0 \| Rojo → 0 |
| Canal R (Rojo) | Amarillo → 255 \| Azul → 0 \| Rojo → 255 |

Ejemplo de matriz BGR en OpenCV (3x3 píxeles) [sic]

```
[ 0, 255, 255 ] [ 0, 255, 255 ] [ 255, 0, 0 ] [ 255, 0, 0 ] [ 0, 0, 255 ]
[ 0, 255, 255 ] [ 0, 255, 255 ] [ 255, 0, 0 ] [ 255, 0, 0 ] [ 0, 0, 255 ]
[ 0, 255, 255 ] [ 0, 255, 255 ] [ 255, 0, 0 ] [ 255, 0, 0 ] [ 0, 0, 255 ]
[ 0, 255, 255 ] [ 0, 255, 255 ] [ 255, 0, 0 ] [ 255, 0, 0 ] [ 0, 0, 255 ]
```

Claves: B = Azul, G = Verde, R = Rojo

visual: the flag (yellow top band, blue middle, red bottom) at top-left; below it three black-background images, one per channel: channel B shows only a blue middle band, channel G shows a bright green top band, channel R shows a bright red bottom band (the yellow top band is not red in the R image, it is black). The matrix rows are shaded yellow, blue and red in three column groups.
</image>

<!-- page:4 -->
<image id="img-003" kind="slide-image" page="4">
## CONVERSIÓN DE LA BANDERA DE COLOMBIA: DE RGB A HSV

### 1. BANDERA DE COLOMBIA EN RGB
(Representación visual)
RGB: cada píxel tiene 3 canales (R, G, B)

### 2. BANDERA DE COLOMBIA EN HSV
(Representación visual)
Conversión RGB → HSV
HSV: cada píxel tiene 3 canales (H, S, V)

### 3. VALORES HSV APROXIMADOS DE CADA COLOR

| Color (Real) | RGB (0-255) | H (0-179) | S (0-255) | V (0-255) |
|---|---|---|---|---|
| Amarillo | (255, 255, 0) | 30 | 255 | 255 |
| Azul | (0, 0, 255) | 120 | 255 | 255 |
| Rojo | (255, 0, 0) | 0 | 255 | 255 |

(HSV (OpenCV) groups the H, S, V columns.)

### 4. FÓRMULAS DE CONVERSIÓN DE RGB A HSV

Sea $R, G, B \in [0, 1]$ (valores normalizados)

Donde: $R = \frac{R_{8bit}}{255},\ G = \frac{G_{8bit}}{255},\ B = \frac{B_{8bit}}{255}$

$$C_{max} = \max(R, G, B),\quad C_{min} = \min(R, G, B),\quad \Delta = C_{max} - C_{min}$$

$$H' = \begin{cases} 0, & \text{si } \Delta = 0 \\ 60° \times \frac{(G-B)}{\Delta} \bmod 6, & \text{si } C_{max} = R \\ 60° \times \left(\frac{(B-R)}{\Delta} + 2\right), & \text{si } C_{max} = G \\ 60° \times \left(\frac{(R-G)}{\Delta} + 4\right), & \text{si } C_{max} = B \end{cases}$$

$$S = \begin{cases} 0, & \text{si } C_{max} = 0 \\ \frac{\Delta}{C_{max}}, & \text{si } C_{max} \neq 0 \end{cases} \qquad V = C_{max}$$

Rangos en OpenCV: $H \in [0, 179]$, $S \in [0, 255]$, $V \in [0, 255]$
(El matiz H en OpenCV es la mitad del valor en grados: $H_{opencv} = \frac{H'}{2}$)

### 5. EJEMPLO DE CÁLCULO PARA LOS COLORES DE LA BANDERA

AMARILLO RGB = (255, 255, 0)
- R = 1, G = 1, B = 0
- $C_{max} = 1,\ C_{min} = 0,\ \Delta = 1$
- $C_{max} = R = G$
- $H' = 60° \times \frac{(G-B)}{\Delta} \bmod 6 = 60° \times 1 = 60°$
- $S = \frac{\Delta}{C_{max}} = \frac{1}{1} = 1$
- $V = C_{max} = 1$
- HSV (grados) = (60°, 1, 1)
- HSV en OpenCV = (30, 255, 255)

AZUL RGB = (0, 0, 255)
- R = 0, G = 0, B = 1
- $C_{max} = 1,\ C_{min} = 0,\ \Delta = 1$
- $C_{max} = B$
- $H' = 60° \times \left(\frac{(R-G)}{\Delta} + 4\right) = 60° \times (0 + 4) = 240°$
- $S = \frac{\Delta}{C_{max}} = \frac{1}{1} = 1$
- $V = C_{max} = 1$
- HSV (grados) = (240°, 1, 1)
- HSV en OpenCV = (120, 255, 255)

ROJO RGB = (255, 0, 0)
- R = 1, G = 0, B = 0
- $C_{max} = 1,\ C_{min} = 0,\ \Delta = 1$
- $C_{max} = R$
- $H' = 0°$
- $S = \frac{\Delta}{C_{max}} = \frac{1}{1} = 1$
- $V = C_{max} = 1$
- HSV (grados) = (0°, 1, 1)
- HSV en OpenCV = (0, 255, 255)

### 6. RESUMEN VISUAL

RGB (Como se ve) | HSV (Representación HSV)

En HSV, el color se representa por:
- H = tipo de color (matiz)
- S = intensidad del color
- V = brillo del color

visual: the RGB flag (yellow, blue, red) next to its HSV-as-RGB rendering (yellow-green top band, blue middle, red bottom), repeated in sections 1-2 and 6; an arrow labeled "Conversión RGB → HSV" between the first two.
</image>

<!-- page:5 -->
<image id="img-004" kind="slide-image" page="5">
## Transformación de BGR a HSV en OpenCV

OpenCV lee las imágenes en formato BGR. Para trabajar con color de forma más intuitiva, podemos convertirlas al espacio HSV (Tono, Saturación, Valor).

### 1. Imagen Original (BGR)
### 2. Imagen en HSV (compuesta)

cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

### ¿Qué representa HSV?
- H (Hue / Tono): color puro (0° a 179° en OpenCV)
- S (Saturation / Saturación): intensidad del color (0 = gris, 255 = color puro)
- V (Value / Valor): brillo (0 = negro, 255 = máximo brillo)

### 3. Canales HSV por separado

| Canal | Descripción |
|---|---|
| H - Tono (Hue) (scale 0° to 179°) | Representa el tipo de color (rojos, verdes, azules, etc.) |
| S - Saturación (Saturation) (scale 0 to 255) | Indica qué tan "puro" es el color. Blanco = color puro, Negro = gris |
| V - Valor (Value) (scale 0 to 255) | Indica el brillo de la imagen. Blanco = muy brillante, Negro = oscuro |

### ¿Por qué usar HSV?
- Permite segmentar colores de forma más robusta.
- Es menos sensible a cambios de iluminación (valor).
- Ideal para aplicaciones como detección de objetos por color, seguimiento, visión robótica, etc.

Código en OpenCV (Python)
```python
import cv2
imagen_bgr = cv2.imread('paisaje.jpg')  # OpenCV carga en BGR
imagen_hsv = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2HSV)  # Conversión a HSV
```

Rangos en OpenCV (8 bits por canal)
- H: 0 - 179 (equivale a 0° - 360°)
- S: 0 - 255 (0 = gris, 255 = color puro)
- V: 0 - 255 (0 = negro, 255 = muy brillante)

visual: a mountain-lake landscape photo (original), the same image rendered with HSV values shown as RGB (magenta/red mountains, green-cyan sky), the H channel as a false-color image with a vertical color bar 0° (bottom) to 179° (top), the S channel as grayscale, the V channel as grayscale, and a small HSV cone diagram with axes H (around), S (radius), V (height).
</image>

<!-- page:6 -->
<image id="img-005" kind="slide-image" page="6">
## CONVERSIÓN DE RGB A CIELAB

El espacio CIELAB ($L^*a^*b^*$) está diseñado para que la distancia entre colores sea perceptualmente uniforme para el ojo humano.

### 1. RGB (Entrada)
Valores: $R, G, B \in [0, 255]$ (RGB cube with axes R, G, B)

### 2. De RGB a XYZ
1. Normalizar RGB a [0,1]: $r = \frac{R}{255},\ g = \frac{G}{255},\ b = \frac{B}{255}$
2. Corrección gamma:

$$C_{lin} = \begin{cases} \frac{C}{12.92} & \text{si } C \le 0.04045 \\ \left(\frac{C + 0.055}{1.055}\right)^{2.4} & \text{si } C > 0.04045 \end{cases}$$

donde $C \in \{r, g, b\}$

3. Conversión a XYZ (Iluminante D65):

$$\begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} 0.4124 & 0.3576 & 0.1805 \\ 0.2126 & 0.7152 & 0.0722 \\ 0.0193 & 0.1192 & 0.9505 \end{bmatrix} \begin{bmatrix} r_{lin} \\ g_{lin} \\ b_{lin} \end{bmatrix}$$

Resultado: $X, Y, Z$ (Tristímulos del color)

### 3. De XYZ a CIELAB
1. Normalizar por el blanco de referencia (D65): $x = \frac{X}{X_n},\ y = \frac{Y}{Y_n},\ z = \frac{Z}{Z_n}$ ($X_n = 95.047$, $Y_n = 100.000$, $Z_n = 108.883$)
2. Función $f(t)$:

$$f(t) = \begin{cases} t^{1/3} & \text{si } t > \left(\frac{6}{29}\right)^3 \\ \frac{1}{3}\left(\frac{29}{6}\right)^2 t + \frac{4}{29} & \text{si } t \le \left(\frac{6}{29}\right)^3 \end{cases}$$

3. Cálculo de $L^*a^*b^*$:

$$L^* = 116\, f(y) - 16$$
$$a^* = 500\,[f(x) - f(y)]$$
$$b^* = 200\,[f(y) - f(z)]$$

Rangos típicos: $L^* \in [0, 100]$, $a^* \in [-128, 127]$, $b^* \in [-128, 127]$

### Ejemplo de Imagen en RGB → Ejemplo de Imagen en CIELAB (Puro)

### ¿Qué representa cada componente en CIELAB?
- $L^*$ (Luminosidad): 0 = negro, 100 = blanco
- $a^*$ (Componente verde ↔ rojo): negativo: verde | positivo: rojo
- $b^*$ (Componente azul ↔ amarillo): negativo: azul | positivo: amarillo

Diagram axes: $L^*$ vertical (0 to 100); $a^*$ horizontal with $-a^*$ (verde) on the left and $+a^*$ (rojo) on the right; $b^*$ diagonal with $+b^*$ (amarillo) up-right and $-b^*$ (azul) down-left.

Resumen del flujo: RGB → (Normalización + Gamma) → XYZ → (Normalización) → CIELAB ($L^*a^*b^*$)

visual: a mountain-lake photo (RGB) and the same photo rendered with raw L*a*b* values shown as RGB (yellow-orange sky, purple-magenta lake).
</image>

<!-- page:7 -->
<image id="img-006" kind="slide-image" page="7">
## OPERACIÓN AND ENTRE DOS IMÁGENES

La operación AND se aplica píxel por píxel.

Imagen 1 (Paisaje) AND Imagen 2 (Máscara de círculos) = Resultado (AND)

IMAGEN 1 (Paisaje) · IMAGEN 2 (Máscara de círculos) · RESULTADO (AND)

Ejemplo de píxeles

| R | G | B |
|---|---|---|
| 120 | 200 | 150 |

Valores reales del paisaje (0 - 255)

Ejemplo de píxeles (máscara)

| Región | R | G | B |
|---|---|---|---|
| Dentro del círculo (blanco = 255) | 255 | 255 | 255 |
| Fuera del círculo (negro = 0) | 0 | 0 | 0 |

Ejemplo de resultado

| Región | R | G | B |
|---|---|---|---|
| Dentro del círculo: Se conserva el píxel | 120 | 200 | 150 |
| Fuera del círculo: Se elimina el píxel | 0 | 0 | 0 |

¿Cómo funciona?

AND es una operación lógica:
- 1 AND 1 = 1 (se conserva)
- 0 AND 1 = 0 (se elimina)
- 1 AND 0 = 0 (se elimina)
- 0 AND 0 = 0 (se elimina)

En imágenes:
- Blanco (255) actúa como 1 (conserva el píxel)
- Negro (0) actúa como 0 (elimina el píxel)

Fórmula: $I_{resultado}(x, y) = I_1(x, y)\ AND\ I_2(x, y)$

Aplicada a cada canal (R, G y B)

Aplicaciones:
- Aplicar máscaras
- Extraer regiones de interés
- Segmentación
- Visión por computadora

visual: left, a mountain-lake landscape photo; center, a black image with three white filled circles (large upper-left, small upper-right, medium lower-center); right, a black image where the landscape is visible only inside those three circles.
</image>

<!-- page:8 -->
<image id="img-007" kind="slide-image" page="8">
## ¿CÓMO FUNCIONA EN OPENCV?

Para encontrar las diferencias entre dos imágenes, se usa la RESTA ABSOLUTA (absdiff) y luego se aplica un umbral para resaltar los cambios.

Pasos: 1 Imagen 1 (Original) → 2 Imagen 2 (Con diferencias) → 3 Resta absoluta (absdiff) → 4 Umbral (threshold) → 5 Diferencias (final)

Código en OpenCV (Python)
```python
import cv2
import numpy as np

# 1. Cargar imágenes
img1 = cv2.imread('imagen1.png')  # Imagen original
img2 = cv2.imread('imagen2.png')  # Imagen con diferencias

# 2. Asegurar mismo tamaño
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# 3. Resta absoluta
resta = cv2.absdiff(img1, img2)

# 4. Convertir a escala de grises
gris = cv2.cvtColor(resta, cv2.COLOR_BGR2GRAY)

# 5. Aplicar umbral para resaltar diferencias
_, umbral = cv2.threshold(gris, 30, 255, cv2.THRESH_BINARY)

# 6. Mostrar resultados
cv2.imshow('Imagen 1', img1)
cv2.imshow('Imagen 2', img2)
cv2.imshow('Diferencias', umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

¿Qué hace cada paso?
1. Carga la imagen original.
2. Carga la segunda imagen con cambios.
3. Calcula la diferencia absoluta por píxel: $|I_1(x,y) - I_2(x,y)|$
4. Convierte la imagen a escala de grises.
5. Aplica un umbral para obtener solo las diferencias (blanco = cambio).
6. Muestra los resultados.

Explicación
- La función cv2.absdiff() calcula la diferencia absoluta entre dos imágenes.
- Los valores cercanos a 0 (negro) son zonas iguales.
- Los valores altos (blanco) son zonas diferentes.
- El umbral convierte esas diferencias en blanco puro para que sean fáciles de ver.

Tabla de ejemplo (un píxel)

| Imagen 1 (I1) | Imagen 2 (I2) | Resta abs \|I1 - I2\| | Umbral (>30) |
|---|---|---|---|
| 120 | 120 | 0 | 0 (negro) |
| 200 | 50 | 150 | 255 (blanco) |
| 80 | 90 | 10 | 0 (negro) |

Leyenda: 0 = sin diferencia (negro); 255 = diferencia (blanco)

Conclusión: OpenCV permite detectar diferencias entre dos imágenes usando resta absoluta y umbralización. Es la base de muchos juegos "Encuentra las diferencias" y aplicaciones de visión por computadora.

Aplicaciones
- Juegos infantiles
- Detección de cambios
- Seguridad y vigilancia
- Seguimiento de objetos

visual: five cartoon thumbnails of a house scene (sun, tree, pond with duck, dog, flowers). Image 2 differs from image 1 (added bird, apples, blue roof, duck); the absdiff image shows white outlines on black; the threshold image shows only white blobs where changes occur; the final image circles the differences in red on the original.
</image>

<!-- page:9 -->
# Filtros

<!-- page:10 -->
<image id="img-008" kind="slide-image" page="10">
## 1. ¿Qué es un filtro en visión artificial?

Un **filtro** es una operación que se aplica a una imagen para modificar sus píxeles con el objetivo de resaltar información importante o reducir ruido. En visión artificial, los filtros se usan para mejorar la calidad de la imagen, extraer bordes, detectar patrones, suavizar, realzar detalles, entre otros.

La mayoría de los filtros trabajan mediante **convolución**, es decir, moviendo una pequeña matriz (**kernel**) sobre cada píxel de la imagen y calculando un nuevo valor a partir de los píxeles vecinos.

## 2. ¿Qué es el kernel?

El **kernel** (o máscara) es una pequeña matriz de números que define cómo se combinarán los píxeles vecinos.
- Se desplaza por toda la imagen.
- En cada posición, se multiplica elemento a elemento con la vecindad de la imagen.
- Luego se suman los resultados para obtener el nuevo valor del píxel central.

Ejemplo: Un kernel de 3×3 tiene 9 valores que determinan el comportamiento del filtro.

Vecindad de la imagen (3×3) * Kernel (3×3) = Resultado

| 105 | 110 | 108 |
|---|---|---|
| 100 | 102 | 98 |
| 95 | 90 | 92 |

\*

| 1 | 1 | 1 |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 1 | 1 |

= 900

Suma total = 900 → nuevo valor del píxel central

## 3. Tres filtros importantes en visión artificial

### 1) Filtro Gaussiano (Suavizado)
Reduce el ruido de la imagen y suaviza los cambios bruscos de intensidad.

Kernel 3×3: $\frac{1}{16} \times$

| 1 | 2 | 1 |
|---|---|---|
| 2 | 4 | 2 |
| 1 | 2 | 1 |

Ejemplo: Imagen original / Con filtro Gaussiano (noisy mountain-lake photo and its smoothed, blurred version)

### 2) Filtro de Sobel (Detección de bordes)
Detecta bordes resaltando los cambios de intensidad en horizontal y vertical.

Kernels 3×3:

Sobel en X ($G_x$):

| -1 | 0 | 1 |
|---|---|---|
| -2 | 0 | 2 |
| -1 | 0 | 1 |

Sobel en Y ($G_y$):

| -1 | -2 | -1 |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 2 | 1 |

Ejemplo (bordes en X + Y): Imagen original / Con filtro Sobel (grayscale house photo and white edge lines on black)

### 3) Filtro Laplaciano (Realce de bordes)
Resalta los bordes y detalles finos. Muy útil para identificar contornos.

Kernel 3×3:

| 0 | 1 | 0 |
|---|---|---|
| 1 | -4 | 1 |
| 0 | 1 | 0 |

Ejemplo: Imagen original / Con filtro Laplaciano (grayscale house photo and a gray image with faint edge lines)
</image>

<!-- page:11 -->
# Filtro Gaussiano

<!-- page:12 -->
<image id="img-009" kind="photo" page="12">
text: "Before" | "After"
description: Side-by-side night photo of a city skyline (a TV tower on the left, a large white-framed building in the center, a bridge and river at the bottom with warm lights). Left half ("Before") is covered in heavy teal/white speckle noise; right half ("After") is the same scene clean and smooth. Split by a thin white vertical line, with rounded dark labels at the top corners.
</image>

<!-- page:13 -->
<image id="img-010" kind="slide-image" page="13">
## Filtro gaussiano

De imágenes ruidosas a información útil · Visión artificial: Imágenes más claras para mejores decisiones

### 1. Una imagen puede contener ruido
Ampliación de una región (ruido)

| 10 | 10 | 10 |
|---|---|---|
| 10 | 200 | 10 |
| 10 | 10 | 10 |

El ruido produce pequeñas variaciones de intensidad que pueden dificultar el análisis de la imagen.
El valor 200 representa una variación muy fuerte respecto a sus vecinos.

### 2. El filtro combina cada píxel con sus vecinos
Máscara gaussiana

| 1 | 2 | 1 |
|---|---|---|
| 2 | 4 | 2 |
| 1 | 2 | 1 |

Centro: mayor peso · Vecinos: peso intermedio · Esquinas: menor peso · Todo dividido entre 16

Cálculo del nuevo valor
- Nuevo valor = (1·10 + 2·10 + 1·10 + 2·10 + 4·200 + 2·10 + 1·10 + 2·10 + 1·10) / 16
- Nuevo valor = 920 / 16
- Nuevo valor = 57.5

El valor extremo se reduce al mezclarse con la información de los píxeles vecinos.

### 3. La imagen queda más suave y estable
Imagen original → Filtro gaussiano → Imagen suavizada

El suavizado facilita tareas posteriores: Persona mejor definida, Automóvil más claro, Señal de tránsito más nítida.

Facilita:
- Detección de bordes
- Reconocimiento de objetos
- Segmentación
- Análisis de formas

El filtro no busca detectar objetos directamente; prepara la imagen para que otros algoritmos trabajen mejor.

Ruido → Promedio ponderado → Imagen suavizada

Conclusión: El filtro gaussiano reduce variaciones pequeñas de intensidad al reemplazar cada píxel por un promedio ponderado de sus vecinos. Esto produce una imagen más suave y adecuada para etapas posteriores de visión artificial.

visual: a cartoon street scene (pedestrian with a red backpack, blue car, red car, a "30" speed-limit sign, buildings and trees) shown noisy with a red-boxed zoomed 3x3 region of gray pixels; later shown blurred (pixelated gray block in the middle) and finally clean.
</image>

<!-- page:14 -->
# Algoritmo Canny

<!-- page:15 -->
<image id="img-011" kind="slide-image" page="15">
## ALGORITMO DE CANNY
Detección óptima de bordes basada en derivadas

### ¿QUÉ ES?
El algoritmo de Canny es un método de detección de bordes que identifica cambios bruscos en la intensidad de los píxeles. Utiliza derivadas para encontrar dónde la intensidad cambia significativamente, correspondiendo a los bordes de los objetos.

(mountain-lake photo → "Canny" → white edge lines on black)

### RELACIÓN CON LAS DERIVADAS
La intensidad de la imagen $I(x, y)$ se considera una función. Las derivadas miden cuánto cambia esa intensidad.

Se calculan las derivadas parciales:
- $G_x = \frac{\partial I}{\partial x}$: Cambios en horizontal
- $G_y = \frac{\partial I}{\partial y}$: Cambios en vertical

Luego se calcula la magnitud del gradiente:

$$G = \sqrt{G_x^2 + G_y^2}$$

Indica la fuerza del borde en cada píxel

La dirección del gradiente es:

$$\theta = \tan^{-1}\left(\frac{G_y}{G_x}\right)$$

### APROXIMACIÓN DE DERIVADAS: OPERADOR SOBEL
Las derivadas se aproximan con convoluciones. Ejemplo: filtro Sobel horizontal ($G_x$):

| -1 | 0 | 1 |
|---|---|---|
| -2 | 0 | 2 |
| -1 | 0 | 1 |

El filtro Sobel vertical ($G_y$) es la transpuesta del anterior:

| -1 | -2 | -1 |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 2 | 1 |

### ETAPAS DEL ALGORITMO DE CANNY
1. Suavizado Gaussiano: Reduce el ruido de la imagen.
2. Cálculo de derivadas: Se obtienen $G_x$ y $G_y$ usando filtros como Sobel.
3. Magnitud y dirección: Se calcula la magnitud $G$ y la dirección $\theta$ del gradiente. (Magnitud (G); Dirección (θ) with a color bar from -π through 0 to π)
4. Supresión de no máximos: Se conservan solo los máximos locales en la dirección del gradiente.
5. Umbralización por histéresis: Se usan dos umbrales (alto y bajo) para eliminar bordes débiles y ruido.
   - Bordes fuertes (se conservan)
   - Bordes débiles (se conservan si están conectados a bordes fuertes)
   - Ruido (se elimina)

### OBJETIVO DE CANNY
Detectar bordes verdaderos con buena localización, buena detección y mínima respuesta a ruido.

### ¿POR QUÉ ES EFECTIVO?
- Buena detección: Encuentra la mayoría de los bordes reales.
- Buena localización: Los bordes detectados están cerca de la posición real.
- Mínima respuesta a ruido: Reduce falsas detecciones causadas por ruido.

### RESUMEN
Canny utiliza derivadas (gradientes) para encontrar cambios importantes de intensidad y así detectar bordes de manera precisa y robusta.

visual: pipeline of grayscale house images: blurred (with a Gaussian bell curve under it), Gx and Gy edge images, magnitude image and a rainbow-colored direction image, thin one-pixel edges after non-maximum suppression, and the final edge map after hysteresis (red, orange and black arrows labeling strong, weak and noise edges). A gradient diagram shows vector G with components Gx (horizontal) and Gy (vertical).
</image>

<!-- page:16 -->
<image id="img-012" kind="slide-image" page="16">
## Algoritmo de Canny: matemáticas paso a paso
Ejemplo con una imagen 3x3 para entender cómo se detecta un borde

Detección de bordes

### 1. La imagen y el cambio de intensidad

| 10 | 10 | 200 |
|---|---|---|
| 10 | 10 | 200 |
| 10 | 10 | 200 |

A la izquierda hay valores oscuros y a la derecha valores claros. El cambio fuerte entre 10 y 200 sugiere la presencia de un borde vertical.

Un borde aparece donde la intensidad cambia bruscamente

### 2. Cálculo del gradiente con Sobel

$G_x$ =

| -1 | 0 | 1 |
|---|---|---|
| -2 | 0 | 2 |
| -1 | 0 | 1 |

$G_y$ =

| -1 | -2 | -1 |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 2 | 1 |

Cálculo de Gx:
- Gx = (-1·10) + (0·10) + (1·200) + (-2·10) + (0·10) + (2·200) + (-1·10) + (0·10) + (1·200)
- Gx = -10 + 0 + 200 - 20 + 0 + 400 - 10 + 0 + 200
- Gx = 760

Cálculo de Gy:
- Gy = (-1·10) + (-2·10) + (-1·200) + (0·10) + (0·10) + (0·200) + (1·10) + (2·10) + (1·200)
- Gy = -10 - 20 - 200 + 0 + 0 + 0 + 10 + 20 + 200
- Gy = 0

Gx mide el cambio horizontal de intensidad. Gy mide el cambio vertical. Aquí el cambio horizontal es muy grande y el vertical es nulo.

Magnitud del gradiente:
- G = √(Gx² + Gy²)
- G = √(760² + 0²)
- G = 760

Dirección del gradiente:
- θ = arctan(Gy / Gx)
- θ = arctan(0 / 760)
- θ = 0°

Como Gx es grande y Gy es 0, el algoritmo detecta un borde vertical

### 3. Decisión: ¿es borde o no?

| Valor de G | Resultado |
|---|---|
| Si G > 300 | borde fuerte |
| Si 100 < G ≤ 300 | borde débil |
| Si G ≤ 100 | no es borde |

Como G = 760, este punto se clasifica como borde fuerte

Salida binaria (valores):

| 0 | 255 | 0 |
|---|---|---|
| 0 | 255 | 0 |
| 0 | 255 | 0 |

Representación visual: black-white-black vertical stripes (white center column).

El algoritmo conserva la ubicación donde el cambio de intensidad es más fuerte y marca ese lugar como borde.

Flujo del algoritmo de Canny: Matriz de entrada → Sobel en x e y → Magnitud y dirección → Umbral → Borde detectado

Conclusión: El algoritmo de Canny identifica bordes al medir matemáticamente los cambios de intensidad entre píxeles. En este ejemplo, el salto de 10 a 200 produce un gradiente alto, por lo que se detecta un borde vertical.

visual: a small robot mascot at top-left pointing at the title; the 3x3 grid has a red dashed vertical line between the second and third columns; the 3x3 darker cells on the left (10) and a light column on the right (200); a monitor icon at top-right.
</image>

<!-- page:17 -->
# Operaciones Morfológicas

<!-- page:18 -->
<image id="img-013" kind="photo" page="18">
description: Three square binary (black and white) images side by side, no text. Left: black background with many white filled squares of varying sizes (about 60 squares plus many tiny white dots, from single pixels to larger squares). Middle: almost entirely black with only three tiny white dots (left-upper, right-middle, bottom-left). Right: black background with three larger white filled squares at roughly the same three positions as the dots (upper-left, right-middle, bottom-center-left).
</image>

<!-- page:19 -->
<image id="img-014" kind="slide-image" page="19">
## DILATACIÓN MORFOLÓGICA
Ejemplo paso a paso con una imagen de 9x9

¿QUÉ ES? La dilatación agrega píxeles a los bordes de los objetos (valor 1) utilizando un kernel.

KERNEL UTILIZADO (3x3): El kernel define la forma y dirección de la expansión.

| 1 | 1 | 1 |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 1 | 1 |

### CASO 1: CUANDO TODO ES 0
1. Posición inicial del kernel (arriba a la izquierda): grid 9x9 of all 0; the 3x3 kernel (blue) over rows 1-3, columns 1-3 with its center (red) at row 2, column 2. "Como todos los píxeles son 0, el píxel central es 0."
2. El kernel se mueve a la derecha: kernel (blue) over rows 1-3, columns 4-6, center at row 2, column 5. "Como todos los píxeles son 0, el píxel central es 0."
3. El kernel se mueve hacia abajo y continúa recorriendo la imagen: kernel over rows 4-6, columns 4-6, center at row 5, column 5. "Como todos los píxeles son 0, el píxel central es 0." (row 3 of this grid has smeared glyphs; all cells are 0)
4. Resultado final: el kernel recorrió toda la imagen y no encontró 1: grid 9x9 of all 0. "No se agregan píxeles. La imagen permanece igual."

### CASO 2: CUANDO EL KERNEL ENCUENTRA UN 1
All grids are 9x9 of 0 except a single 1 at row 5, column 5.
1. Posición inicial del kernel (arriba a la izquierda): kernel over rows 1-3, columns 1-3, center (red) at row 2, column 2 = 0. "El píxel central es 0. No se agrega ningún píxel."
2. El kernel se mueve y se acerca al 1: kernel over rows 2-4, columns 2-4, center at row 3, column 3 = 0, with the 1 just outside at row 5, column 5. "El píxel central es 0. No se agrega ningún píxel."
3. El kernel se coloca sobre el 1 (el 1 queda en el centro): kernel over rows 4-6, columns 4-6, center at row 5, column 5 = 1. "El píxel central es 1. Se agregan píxeles (dilatación)."
4. Resultado después de la dilatación: the 3x3 block of rows 4-6, columns 4-6 is all 1 (green). All other cells 0. "El objeto se expande en todas las direcciones según el kernel."

Leyenda: Píxel con valor 0 (fondo) · Píxel con valor 1 (objeto) · Posición del kernel (3x3) · Píxel central del kernel · Píxeles agregados por la dilatación
</image>

<!-- page:20 -->
<image id="img-015" kind="slide-image" page="20">
## EROSIÓN MORFOLÓGICA
Ejemplo paso a paso con una imagen de 9x9

¿QUÉ ES? La erosión elimina píxeles en los bordes de los objetos (valor 1) utilizando un kernel. Solo el píxel central se mantiene en 1 si TODOS los píxeles bajo el kernel son 1.

KERNEL UTILIZADO (3x3): El kernel define la forma y dirección de la erosión.

| 1 | 1 | 1 |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 1 | 1 |

### CASO 1: CUANDO TODO ES 0
1. Posición inicial del kernel (arriba a la izquierda): 9x9 grid of all 0, kernel over rows 1-3, columns 1-3. "Como todos los píxeles son 0, NO se cumple la condición."
2. El kernel se mueve a la derecha: kernel over rows 1-3, columns 4-6. "Como todos los píxeles son 0, NO se cumple la condición."
3. El kernel se mueve hacia abajo y continúa recorriendo la imagen: kernel over rows 4-6, columns 3-5. "Como todos los píxeles son 0, NO se cumple la condición."
4. Resultado final: el kernel recorrió toda la imagen y no encontró 1: 9x9 grid of all 0. "No se elimina ningún píxel porque no hay píxeles con valor 1."

### CASO 2: CUANDO EL KERNEL ENCUENTRA UN 1
The 9x9 grid contains an object of 1s (a blob roughly 3 to 5 pixels wide in rows 4-8, columns 3-7; several cells are blurred in the render and are marked [?]):

```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 1 1 1 1 1 0 0
0 0 [?] 1 1 1 [?] 0 0
0 0 0 1 1 [?] 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0
```
(approximate shape as drawn in steps 1-2)

1. Posición inicial del kernel (arriba a la izquierda): kernel over rows 1-3, columns 1-3. "El píxel central es 0. No se cumple la condición. No se cambia nada."
2. El kernel se mueve y se acerca al objeto: kernel over rows 3-5, columns 2-4, center at row 4, column 3 = 0. "El píxel central es 0 porque no todos los píxeles bajo el kernel son 1. No se cambia nada."
3. El kernel se coloca sobre el centro del objeto (todos los valores son 1): grid where rows 3-6 (1-indexed rows 3,4,5,6), columns 4-6 are all 1 and the kernel (blue) covers a 3x3 block of 1s with its center (red) at the middle 1.

```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```
"Todos los píxeles bajo el kernel son 1. El píxel central es 1. Se mantiene el 1 y se eliminan los demás."
4. Resultado después de la erosión: all cells 0 except a single 1 (green) at row 5, column 5. "Solo el píxel central del objeto se mantiene en 1. Los bordes se eliminan."

Leyenda: Píxel con valor 0 (fondo) · Píxel con valor 1 (objeto) · Posición del kernel (3x3) · Píxel central del kernel · Píxeles eliminados por la erosión
</image>

<!-- page:21 -->
# Detección Figuras Geométricas

<!-- page:22 -->
<image id="img-016" kind="slide-image" page="22">
## DETECCIÓN DE POLÍGONOS - PASO A PASO (VISIÓN GENERAL)

| Paso | Título | Descripción | Código |
|---|---|---|---|
| 1 | IMAGEN ORIGINAL | Se captura el frame desde la cámara. | `frame` |
| 2 | CONVERSIÓN A GRIS | Se convierte la imagen a escala de grises. | `gris` |
| 3 | GAUSSIAN BLUR | Se aplica un suavizado para reducir el ruido. | `gauss = GaussianBlur(gris)` |
| 4 | DETECCIÓN DE BORDES | Se aplica Canny para detectar los bordes. | `bordes = Canny(gauss)` |
| 5 | ENCONTRAR CONTORNOS | Se buscan los contornos en la imagen de bordes. | `contornos = findContours(bordes)` |

### 6 APROXIMACIÓN Y CLASIFICACIÓN DE POLÍGONOS
Cada contorno se aproxima a un polígono y se cuenta la cantidad de lados para clasificar (triángulo, cuadrado, pentágono, etc.).

```python
aproximacion = approxPolyDP(contorno)
lados = len(aproximacion)
```

CLASIFICACIÓN POR NÚMERO DE LADOS

| Lados | Figura |
|---|---|
| 3 | Triángulo |
| 4 | Cuadrado / Rectángulo |
| 5 | Pentágono |
| 6 | Hexágono |
| 7+ | Polígono (n lados) |

### 7 DIBUJAR POLÍGONOS Y RESULTADO FINAL
Se dibujan los polígonos detectados, sus vértices y se muestra el nombre según la cantidad de lados.

```python
salida = dibujar_poligonos(frame, contornos, ...)
```

Etiquetas del resultado: Triángulo (3), Cuadrado (4), Pentágono (5), Hexágono (6), Rectángulo (4)

RESUMEN DEL PROCESO: Frame → Gris → Gaussian Blur → Canny (bordes) → Contornos → Aproximación → Clasificación → Dibujo del resultado

visual: a wooden-table photo with five colored flat shapes (blue triangle, green square, red pentagon, yellow hexagon, purple rectangle); then its grayscale version, blurred version, white outlines on black (Canny), green contours on black, colored polygons with red vertex dots on black, and finally the labeled polygons drawn over the original photo.
</image>

<!-- page:23 -->
<image id="img-017" kind="slide-image" page="23">
## APROXIMACIÓN DE CONTORNOS – PROCESO GENERAL
Convierte los contornos detectados en polígonos con menos vértices para poder clasificar formas.

1. IMAGEN BINARIA (BORDES): Se parte de una imagen binaria donde los bordes de los objetos están definidos (por ejemplo con Canny).
2. ENCONTRAR CONTORNOS: Se detectan los contornos conectados en la imagen usando findContours(). Cada contorno es una lista de puntos.
3. CONTORNO COMO CONJUNTO DE PUNTOS: Cada contorno está formado por muchos puntos que siguen el borde del objeto.
4. SIMPLIFICACIÓN DEL CONTORNO: Se aplica el algoritmo de Douglas–Peucker (implementado en approxPolyDP()), que elimina puntos innecesarios manteniendo la forma general.
5. CONTORNO APROXIMADO: El resultado es un polígono con menos vértices que representa al objeto original.
6. CONTAR VÉRTICES: Se cuenta la cantidad de vértices del polígono aproximado (número de lados). (pentagon with "5 lados")
7. CLASIFICAR LA FORMA: Según la cantidad de lados, se clasifica el objeto (triángulo, cuadrado, pentágono, hexágono, etc.).

| Lados | Figura |
|---|---|
| 3 | Triángulo |
| 4 | Cuadrado / Rectángulo |
| 5 | Pentágono |
| 6 | Hexágono |
| 7 | Heptágono |
| 8 | Octágono |
| n | Polígono de n lados |

8. USO EN LA DETECCIÓN: Se dibuja el polígono aproximado sobre la imagen original para mostrar el resultado.

RESUMEN DEL PROCESO: Bordes (Canny) → findContours() → Contornos (puntos) → approxPolyDP() → Polígono aproximado → Contar lados → Clasificar forma

visual: step 1 shows white outlines of triangle, square, pentagon, hexagon and rectangle on black; step 2 the same in green; step 3 a pentagon contour with many black points on a grid; step 4 the same contour with red points kept and gray points discarded; step 5 and 6 the simplified red pentagon on a grid; step 8 the colored shapes on a wooden table with green polygon outlines and green vertex dots.
</image>

<!-- page:24 -->
<image id="img-018" kind="slide-image" page="24">
## ¿CÓMO FUNCIONA approxPolyDP()?
approxPolyDP(contorno, epsilon, cerrado) simplifica un contorno reduciendo la cantidad de vértices mientras mantiene la forma general del objeto.

### ¿QUÉ ES?
Es el algoritmo de Douglas-Peucker adaptado para polígonos. Elimina puntos intermedios que están "cerca" de la línea que une dos vértices importantes.

### PARÁMETRO CLAVE: epsilon
Es la distancia máxima permitida entre un punto del contorno original y el segmento que lo reemplaza. A mayor epsilon → más simplificación (menos vértices). A menor epsilon → menos simplificación (más vértices).

### IDEA PRINCIPAL
Conservar los puntos "importantes" (esquinas) y eliminar los puntos que no cambian la forma del contorno más allá de una tolerancia (epsilon).

### PASO A PASO DEL ALGORITMO (Douglas-Peucker)
1. CONTORNO ORIGINAL: Tenemos un contorno con muchos puntos.
2. UNIR EXTREMOS: Se toma el primer y último punto del contorno y se traza una línea recta entre ellos.
3. DISTANCIA MÁXIMA: Se busca el punto más alejado de esa línea y se mide su distancia perpendicular (d).
4. COMPARAR CON EPSILON: Si d > epsilon, ese punto se considera importante y se divide el contorno en dos partes.
5. REPETIR RECURSIVAMENTE: Se repite el proceso en cada parte hasta que todos los puntos estén a una distancia ≤ epsilon.

### RESULTADO: APROXIMACIÓN DEL CONTORNO
El resultado es un polígono con menos vértices que representa la forma original.

### EFECTO DEL VALOR DE epsilon
A mayor epsilon, más vértices se eliminan.

| Epsilon | Resultado |
|---|---|
| epsilon muy pequeño (muy detallado) | many vertices kept |
| epsilon pequeño | many vertices kept, slightly fewer |
| epsilon medio | fewer vertices |
| epsilon grande (muy simplificado) | few vertices, near polygon |

### EN RESUMEN
approxPolyDP() reduce la cantidad de puntos de un contorno manteniendo su forma general, conservando las esquinas y eliminando los puntos innecesarios según la tolerancia epsilon.

Sintaxis:
```
approxPolyDP(contorno, epsilon, cerrado)
```
- contorno: puntos del contorno (lista de puntos)
- epsilon: tolerancia (double)
- cerrado: True si el contorno está cerrado, False si está abierto

visual: a closed irregular contour of black points on a grid; a blue dashed line joining the first and last points (blue dots); a red point farthest from that line with a dashed red perpendicular segment labeled "d" and the text "d > epsilon" in green; the final simplified polygon with green vertex dots; a row of four polygons showing the epsilon effect.
</image>

<!-- page:25 -->
<image id="img-019" kind="slide-image" page="25">
## ¿QUÉ HACE cv2.boundingRect(aproximacion)?
Devuelve el rectángulo alineado con los ejes (horizontal y vertical) más pequeño que contiene completamente al contorno o polígono dado.

### SINTAXIS
```python
x, y, w, h = cv2.boundingRect(aproximacion)
```
Donde devuelve:
- x: coordenada X de la esquina superior izquierda
- y: coordenada Y de la esquina superior izquierda
- w: ancho del rectángulo
- h: alto del rectángulo

### ¿QUÉ RETORNA?
Un rectángulo definido por (x, y, w, h) que encierra completamente al contorno.

### EJEMPLO
Si boundingRect devuelve (50, 30, 120, 80): esquina (50, 30), ancho 120, alto 80.

### ¿CÓMO FUNCIONA? PASO A PASO
1. CONTORNO APROXIMADO: Tenemos un contorno aproximado (polígono) obtenido con approxPolyDP.
2. BUSCAR EXTREMOS: Se encuentran los valores mínimo y máximo de X e Y entre todos los puntos del contorno. (labels minX, maxX, minY, maxY)
3. DEFINIR RECTÁNGULO: Con esos extremos se forma el rectángulo alineado a los ejes que los contiene. ((minX, minY), w, h)
4. DEVOLVER (x, y, w, h): x = minX, y = minY, w = maxX - minX, h = maxY - minY.

### EJEMPLO REAL
Contorno aproximado → cv2.boundingRect(aproximacion)

La función devuelve: (x, y, w, h) = (84, 63, 198, 146)
- x = 84 → esquina superior izquierda en X
- y = 63 → esquina superior izquierda en Y
- w = 198 → ancho del rectángulo
- h = 146 → alto del rectángulo

### ¿PARA QUÉ SIRVE?
- Para obtener la posición y tamaño de un objeto detectado.
- Para dibujar cuadros (bounding boxes) alrededor de formas.
- Para recortar (ROI) la región que contiene el objeto.
- Para calcular relaciones de aspecto, centrar objetos, etc.

### EN RESUMEN
cv2.boundingRect(aproximacion) calcula el rectángulo alineado a los ejes más pequeño que contiene completamente el contorno o polígono dado y devuelve sus coordenadas (x, y) y dimensiones (w, h).

```python
x, y, w, h = cv2.boundingRect(aproximacion)
```

visual: a pentagon with a green dashed bounding box; arrows mark width w (blue, bottom) and height h (orange, right); a second example shows the pentagon with box labeled (84, 63) at its top-left corner, w = 198 and h = 146; a final small panel shows several shapes (triangle, square, pentagon, hexagon, rectangle) each with a green dashed bounding box.
</image>
