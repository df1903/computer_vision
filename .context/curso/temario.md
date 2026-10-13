# Fundamentos de Visión Artificial — Documento de contexto (OpenCV + Python)

> **Fuente:** presentación "Fundamentos Visión Artificial" — Felipe Buitrago Carmona, Facultad de Inteligencia Artificial e Ingenierías, Universidad de Caldas.
> **Propósito de este archivo:** servir como insumo/contexto persistente para un Proyecto de Claude y para Claude Code. Contiene (1) todo lo que enseña la presentación, texto e imágenes, transcrito y explicado, y (2) una ampliación en la misma línea para que Claude entienda hacia dónde va el curso, qué técnicas se usan y cómo ayudar mejor.
> **Convención de etiquetas:**
> - `[CURSO]` = contenido que aparece en la presentación.
> - `[AMPLIACIÓN]` = contenido añadido para dar contexto y apoyo (no aparece en las diapositivas).
> - `[NOTA DE PRECISIÓN]` = aclaración técnica sobre una simplificación o detalle de las diapositivas.

---

## 0. Instrucciones para Claude / Claude Code (leer primero)

1. **Contexto del usuario:** es un estudiante de un curso universitario de visión artificial. Trabaja con **Python 3 + OpenCV (`cv2`) + NumPy**, y a veces matplotlib para visualizar.
2. **Idioma:** responder en **español**. Comentarios del código en español. Los nombres de variables del curso están en español (`imagen`, `gris`, `bordes`, `contornos`, `aproximacion`, `umbral`, `resta`); mantenerlos por consistencia.
3. **Estilo didáctico del curso:** el profesor explica con **ejemplos numéricos pequeños** (matrices 3×3, 9×9, un solo píxel) y con **pipelines paso a paso**. Al explicar algo, preferir: definición corta → intuición → ejemplo numérico → código OpenCV → aplicaciones.
4. **Recordar siempre BGR:** OpenCV carga y guarda imágenes en orden **B, G, R**, no RGB. Es la fuente #1 de errores de color (ver sección 2 y 11).
5. **Distinguir origen de la información:** cuando el usuario pregunte "¿qué dijo el profe sobre X?", responder desde las secciones `[CURSO]`. Cuando pida profundizar o ir más allá, usar las `[AMPLIACIÓN]` y decirlo.
6. **Al generar código para el proyecto (Claude Code):**
   - Usar `cv2` y `numpy` (`import cv2`, `import numpy as np`).
   - Verificar siempre que `cv2.imread` no devolvió `None` (ruta incorrecta).
   - Ser explícito con tipos (`np.uint8`, `np.float32`) porque las operaciones dependen del tipo.
   - En scripts con ventanas: `cv2.waitKey(0)` y `cv2.destroyAllWindows()`.
   - `cv2.putText` **no soporta tildes ni ñ** con fuentes Hershey: usar textos sin acentos (`"Triangulo"`) o PIL si se necesitan.
7. **Uso responsable:** las técnicas se usan con fines educativos y constructivos (automatización, control de calidad, robótica, análisis de imágenes, accesibilidad, investigación). En aplicaciones sobre personas (vigilancia, seguimiento) mencionar consideraciones de privacidad y consentimiento.
8. **Si hay ambigüedad** entre la simplificación de una diapositiva y el comportamiento real de OpenCV, explicar ambas (ver sección 11).

---

## 1. Mapa del temario `[CURSO]`

Orden en que aparecen los temas en la presentación:

| # | Tema | Idea central | Funciones OpenCV clave |
|---|------|--------------|------------------------|
| 1 | La imagen como arreglo (cubo alto×ancho×canales) | Una imagen a color es un tensor 3D; cada píxel es un vector BGR | `img.shape`, `cv2.imread`, `cv2.split` |
| 2 | Representación BGR (bandera de Colombia) | Descomposición en canales B, G, R | `cv2.split`, `cv2.merge` |
| 3 | RGB → HSV (fórmulas y ejemplo con la bandera) | H = tipo de color, S = pureza, V = brillo; en OpenCV H ∈ [0,179] | `cv2.cvtColor(..., COLOR_BGR2HSV)` |
| 4 | BGR → HSV en OpenCV (paisaje) | HSV segmenta color y es más robusto a la iluminación | `cv2.cvtColor` |
| 5 | RGB → CIELAB | Espacio perceptualmente uniforme (L\*, a\*, b\*) | `cv2.cvtColor(..., COLOR_BGR2LAB)` |
| 6 | Operación AND entre imágenes | Máscaras: conservar solo una región | `cv2.bitwise_and` |
| 7 | Diferencia entre imágenes | Resta absoluta + umbral = mapa de cambios | `cv2.absdiff`, `cv2.threshold` |
| 8 | Filtros y kernels | Convolución con una matriz pequeña | `cv2.filter2D` |
| 9 | Filtro Gaussiano | Promedio ponderado que suaviza el ruido | `cv2.GaussianBlur` |
| 10 | Algoritmo de Canny (teoría + matemáticas) | Bordes vía gradientes, NMS e histéresis | `cv2.Canny`, `cv2.Sobel` |
| 11 | Operaciones morfológicas: dilatación y erosión | Crecer/encoger objetos binarios con un kernel | `cv2.dilate`, `cv2.erode` |
| 12 | Detección de figuras geométricas | Pipeline: gris → blur → Canny → contornos → polígono → clasificar | `cv2.findContours`, `cv2.approxPolyDP`, `cv2.boundingRect` |

**Hilo conductor `[CURSO]`:** *entender la imagen como números → cambiar de espacio de color → operar entre imágenes → filtrar/suavizar → detectar bordes → limpiar formas binarias → extraer y clasificar figuras.* Cada tema alimenta el siguiente: el suavizado prepara a Canny; Canny prepara a los contornos; la morfología limpia lo binario; los contornos permiten clasificar formas.

> **Continuación del curso (fuera de esta presentación):** K-Means (cierra el primer corte) en `10-kmeans.md`; CNN y arquitecturas reconocidas (segundo corte) en `11-cnn.md`. Estado del corte en `corte-1.md`. Índice en `README.md`.

---

## 2. La imagen como arreglo numérico y la representación BGR `[CURSO]`

### 2.1 Imagen como cubo (diapositiva "Imagen de Colombia como un cubo 3×3")

- Se modela la bandera de Colombia como una imagen de **3 filas × 3 columnas × 3 canales**: `shape = (3, 3, 3)` → `(alto, ancho, canales)`.
- Fila 0 = amarillo, fila 1 = azul, fila 2 = rojo (cada fila repite el mismo color en sus 3 columnas).
- **Cada píxel es un vector BGR** de 3 valores (0–255):

| Color | Valor en OpenCV (B, G, R) |
|-------|---------------------------|
| Amarillo | `[0, 255, 255]` |
| Azul | `[255, 0, 0]` |
| Rojo | `[0, 0, 255]` |

- Ejemplos de la diapositiva: píxel `(0,0)` = `[0,255,255]`; píxel `(1,1)` = `[255,0,0]`; píxel `(2,2)` = `[0,0,255]`.
- "La imagen completa es un cubo (3×3×3)": alto = 3 (filas), ancho = 3 (columnas), canales = 3 (BGR).

### 2.2 Representación BGR en OpenCV (diapositiva "Bandera de Colombia")

- En OpenCV cada píxel se almacena en orden **BGR (Azul, Verde, Rojo)**, cada canal en 0–255.
- **Descomposición en canales** (valores por franja de la bandera):

| Canal | Amarillo | Azul | Rojo |
|-------|----------|------|------|
| **B** (Azul) | 0 | 255 | 0 |
| **G** (Verde) | 255 | 0 | 0 |
| **R** (Rojo) | 255 | 0 | 255 |

- Visualmente: el canal B solo "enciende" la franja azul; el canal G solo la amarilla (verde puro en esa vista); el canal R enciende amarillo y rojo (en la diapositiva se ve rojo en la franja roja; el amarillo también tiene R=255).
- Ejemplo de matriz BGR: filas de píxeles `[0,255,255]` (amarillo), `[255,0,0]` (azul), `[0,0,255]` (rojo).

### 2.3 Código equivalente `[AMPLIACIÓN]`

```python
import cv2
import numpy as np

# Bandera de Colombia simplificada (3x3) en BGR
bandera = np.zeros((3, 3, 3), dtype=np.uint8)
bandera[0, :] = (0, 255, 255)   # amarillo (B, G, R)
bandera[1, :] = (255, 0, 0)     # azul
bandera[2, :] = (0, 0, 255)     # rojo

print(bandera.shape)            # (3, 3, 3) -> (alto, ancho, canales)
print(bandera[1, 1])            # [255   0   0]  (píxel azul)

# Separar canales
b, g, r = cv2.split(bandera)
print(b)  # matriz 3x3 con 0,255,0 por filas
# Unir canales
bandera2 = cv2.merge([b, g, r])

# Ampliar para verla (interpolación por vecino más cercano para no suavizar)
grande = cv2.resize(bandera, (300, 300), interpolation=cv2.INTER_NEAREST)
cv2.imshow("Bandera", grande)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 2.4 Conceptos base `[AMPLIACIÓN]`

- **Indexación:** `img[fila, columna]` = `img[y, x]`. ¡Fila primero! Pero las funciones de dibujo/coordenadas de OpenCV (`cv2.circle`, `cv2.rectangle`, `boundingRect`) usan `(x, y)` = `(columna, fila)`.
- **Tipo de dato:** imágenes típicas `uint8` (0–255). Escala de grises: `shape = (alto, ancho)` (2D, sin eje de canales).
- **Recorte (ROI):** `roi = img[y:y+h, x:x+w]`.
- **BGR ↔ RGB para matplotlib:** `rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` o `img[:, :, ::-1]`.
- **Escala de grises:** `gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`; usa la combinación ponderada `Y = 0.299 R + 0.587 G + 0.114 B` (refleja la sensibilidad del ojo).

---

## 3. Espacios de color `[CURSO]`

### 3.1 RGB → HSV: fórmulas y ejemplo con la bandera

**Idea:** en HSV el color se describe con
- **H (Hue / Tono / Matiz):** el "tipo de color" (rojo, verde, azul…), es un ángulo en el círculo cromático.
- **S (Saturation / Saturación):** intensidad o pureza del color (0 = gris, máximo = color puro).
- **V (Value / Valor):** brillo (0 = negro, máximo = brillo máximo).

**Fórmulas de conversión (con R, G, B normalizados a [0,1], es decir, `R = R_8bit / 255`):**

```
Cmax = max(R, G, B)
Cmin = min(R, G, B)
Δ    = Cmax − Cmin

H' =  0                              si Δ = 0
      60° × ( ((G − B) / Δ) mod 6 )  si Cmax = R
      60° × ( ((B − R) / Δ) + 2 )    si Cmax = G
      60° × ( ((R − G) / Δ) + 4 )    si Cmax = B

S  =  0          si Cmax = 0
      Δ / Cmax   si Cmax ≠ 0

V  =  Cmax
```

**Rangos en OpenCV (8 bits):** `H ∈ [0, 179]`, `S ∈ [0, 255]`, `V ∈ [0, 255]`. Como H en grados va de 0° a 360° y no cabe en 8 bits, OpenCV usa **la mitad**: `H_opencv = H' / 2`.

**Ejemplo de cálculo con los colores de la bandera (RGB de entrada):**

| Color | RGB (0–255) | Cmax | Cmin | Δ | H' (grados) | S | V | HSV en OpenCV |
|-------|-------------|------|------|---|-------------|---|---|---------------|
| Amarillo | (255, 255, 0) | 1 | 0 | 1 | 60° | 1 | 1 | **(30, 255, 255)** |
| Azul | (0, 0, 255) | 1 | 0 | 1 | 240° | 1 | 1 | **(120, 255, 255)** |
| Rojo | (255, 0, 0) | 1 | 0 | 1 | 0° | 1 | 1 | **(0, 255, 255)** |

Detalle de los cálculos que muestra la diapositiva:
- **Amarillo:** `Cmax = R = G`; `H' = 60° × ((G−B)/Δ mod 6) = 60° × 1 = 60°`; `S = Δ/Cmax = 1`; `V = 1` → HSV (grados) `(60°, 1, 1)` → OpenCV `(30, 255, 255)`.
- **Azul:** `Cmax = B`; `H' = 60° × ((R−G)/Δ + 4) = 60° × (0 + 4) = 240°`; `S = 1`; `V = 1` → OpenCV `(120, 255, 255)`.
- **Rojo:** `Cmax = R`; `H' = 0°`; `S = 1`; `V = 1` → OpenCV `(0, 255, 255)`.

> **[NOTA DE PRECISIÓN]** La diapositiva enseña las tablas con RGB (R,G,B). En OpenCV, esos mismos colores se almacenan como BGR: amarillo `(0,255,255)`, azul `(255,0,0)`, rojo `(0,0,255)`. El resultado HSV es el mismo. La "imagen HSV" que se muestra en las diapositivas (colores verdosos/limón) es solo ilustrativa: al mostrar un arreglo HSV con `imshow` como si fuera BGR se ven colores "falsos"; eso no significa que la conversión esté mal.

Resumen visual de la diapositiva: *En HSV, H = tipo de color, S = intensidad del color, V = brillo del color.*

### 3.2 BGR → HSV en OpenCV (diapositiva del paisaje)

- OpenCV **lee imágenes en BGR**. Para trabajar con color de forma más intuitiva se convierte a HSV.
- Código de la diapositiva:

```python
import cv2
imagen_bgr = cv2.imread('paisaje.jpg')                       # OpenCV carga en BGR
imagen_hsv = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2HSV)     # Conversión a HSV
```

- **Canales por separado:**
  - **H:** tipo de color (rojos, verdes, azules…). Rango 0–179.
  - **S:** qué tan "puro" es el color. Blanco = color puro, negro = gris.
  - **V:** brillo. Blanco = muy brillante, negro = oscuro.
- **¿Por qué usar HSV?** (lista de la diapositiva)
  - Permite **segmentar colores de forma más robusta**.
  - Es **menos sensible a cambios de iluminación** (el brillo queda aislado en V).
  - Ideal para **detección de objetos por color, seguimiento, visión robótica**, etc.
- **Rangos OpenCV (8 bits/canal):** H 0–179 (equivale a 0°–360°), S 0–255 (0 = gris, 255 = color puro), V 0–255 (0 = negro, 255 = muy brillante).
- Representación geométrica: **cono HSV** (H = ángulo alrededor, S = distancia al eje, V = altura).

### 3.3 Segmentación por color con HSV `[AMPLIACIÓN]`

Es la aplicación estrella de HSV y se combina directamente con el tema de máscaras (AND):

```python
import cv2
import numpy as np

img = cv2.imread("objetos.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Rangos aproximados de H en OpenCV (0-179):
#  rojo ≈ 0-10 y 170-179 | naranja ≈ 10-20 | amarillo ≈ 20-35
#  verde ≈ 35-85 | cian ≈ 85-100 | azul ≈ 100-130 | violeta/magenta ≈ 130-170
inferior = np.array([100, 120, 70])    # azul
superior = np.array([130, 255, 255])
mascara = cv2.inRange(hsv, inferior, superior)     # 255 donde está en rango
resultado = cv2.bitwise_and(img, img, mask=mascara)

# El ROJO "da la vuelta" al círculo: hacen falta DOS rangos
m1 = cv2.inRange(hsv, np.array([0, 120, 70]),   np.array([10, 255, 255]))
m2 = cv2.inRange(hsv, np.array([170, 120, 70]), np.array([179, 255, 255]))
mascara_roja = cv2.bitwise_or(m1, m2)
```

Consejos: subir el mínimo de S y V descarta grises y zonas oscuras; limpiar la máscara con morfología (apertura/cierre, sección 7) antes de buscar contornos.

Para calcular el rango HSV de un color concreto: convertir un píxel BGR:

```python
pix = np.uint8([[[0, 255, 255]]])            # amarillo en BGR
print(cv2.cvtColor(pix, cv2.COLOR_BGR2HSV))  # [[[ 30 255 255]]]
```

### 3.4 RGB → CIELAB `[CURSO]`

- El espacio **CIELAB (L\*a\*b\*)** está diseñado para que **la distancia entre colores sea perceptualmente uniforme para el ojo humano** (dos colores a distancia numérica similar "se ven" igual de distintos).
- **Componentes:**
  - **L\*** (Luminosidad): 0 = negro, 100 = blanco.
  - **a\***: eje verde ↔ rojo (negativo = verde, positivo = rojo).
  - **b\***: eje azul ↔ amarillo (negativo = azul, positivo = amarillo).
- **Rangos típicos:** `L* ∈ [0, 100]`, `a* ∈ [−128, 127]`, `b* ∈ [−128, 127]`.
- **Flujo:** `RGB → (Normalización + Gamma) → XYZ → (Normalización por blanco de referencia) → CIELAB`.

**Paso 1 – RGB a XYZ:**
1. Normalizar a [0,1]: `r = R/255, g = G/255, b = B/255`.
2. **Corrección gamma** (linealización sRGB), para `C ∈ {r, g, b}`:
   ```
   C_lin = C / 12.92                    si C ≤ 0.04045
   C_lin = ((C + 0.055) / 1.055)^2.4    si C > 0.04045
   ```
3. Conversión a XYZ (iluminante **D65**):
   ```
   [X]   [0.4124  0.3576  0.1805]   [r_lin]
   [Y] = [0.2126  0.7152  0.0722] · [g_lin]
   [Z]   [0.0193  0.1192  0.9505]   [b_lin]
   ```
   X, Y, Z son los **tristímulos** del color.

**Paso 2 – XYZ a CIELAB:**
1. Normalizar por el blanco de referencia D65: `x = X/Xn, y = Y/Yn, z = Z/Zn` con `Xn = 95.047, Yn = 100.000, Zn = 108.883`.
2. Función `f(t)`:
   ```
   f(t) = t^(1/3)                          si t > (6/29)^3
   f(t) = (1/3)·(29/6)^2·t + 4/29          si t ≤ (6/29)^3
   ```
3. Cálculo final:
   ```
   L* = 116 · f(y) − 16
   a* = 500 · [ f(x) − f(y) ]
   b* = 200 · [ f(y) − f(z) ]
   ```

> **[NOTA DE PRECISIÓN]** La escala de XYZ debe coincidir con la del blanco de referencia. Si `Xn, Yn, Zn = 95.047, 100, 108.883`, entonces hay que multiplicar el XYZ obtenido de la matriz por 100 (la matriz devuelve valores en 0–1). Alternativa equivalente: usar `Xn, Yn, Zn = 0.95047, 1.0, 1.08883`.

### 3.5 CIELAB en OpenCV y por qué importa `[AMPLIACIÓN]`

```python
import cv2
import numpy as np

# --- Con OpenCV ---
img = cv2.imread("foto.jpg")
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# En uint8 OpenCV re-escala: L* → 0..255 (L*·255/100), a* y b* → +128 (0..255)
# Para obtener rangos "reales" usar float32 en [0,1]:
lab_real = cv2.cvtColor(img.astype(np.float32) / 255.0, cv2.COLOR_BGR2LAB)
# → L en [0,100], a y b aprox en [-127,127]

# --- Implementación manual (para entender las fórmulas del curso) ---
def rgb_a_lab(r, g, b):
    c = np.array([r, g, b], dtype=np.float64) / 255.0
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124, 0.3576, 0.1805],
                  [0.2126, 0.7152, 0.0722],
                  [0.0193, 0.1192, 0.9505]])
    X, Y, Z = (M @ lin) * 100.0                 # escalar a 0-100 como el blanco de referencia
    Xn, Yn, Zn = 95.047, 100.0, 108.883
    d = 6 / 29
    f = lambda t: np.where(t > d**3, np.cbrt(t), t / (3 * d**2) + 4 / 29)
    fx, fy, fz = f(X / Xn), f(Y / Yn), f(Z / Zn)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)

print(rgb_a_lab(255, 0, 0))      # ≈ (53.2, 80.1, 67.2)  rojo puro
print(rgb_a_lab(255, 255, 255))  # ≈ (100, 0, 0)         blanco
```

**Usos típicos:**
- **Diferencia perceptual de color (ΔE):** `ΔE76 = sqrt((L1−L2)² + (a1−a2)² + (b1−b2)²)`. Útil para comparar colores como los ve una persona (control de calidad, color matching).
- **Mejora de contraste sin distorsionar color:** aplicar CLAHE solo al canal L:
  ```python
  l, a, b = cv2.split(lab)
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
  lab2 = cv2.merge((clahe.apply(l), a, b))
  mejorada = cv2.cvtColor(lab2, cv2.COLOR_LAB2BGR)
  ```
- **Segmentación** cuando HSV falla (colores con poca saturación, piel, texturas).

### 3.6 Comparativa rápida de espacios de color `[AMPLIACIÓN]`

| Espacio | Canales | Fortaleza | Cuándo usarlo |
|---------|---------|-----------|---------------|
| BGR/RGB | Azul, Verde, Rojo | Formato nativo de captura/pantalla | Lectura, escritura, visualización |
| Gris | Intensidad | Menos datos, base de bordes/umbrales | Filtros, Canny, contornos |
| HSV | Tono, Saturación, Valor | Separa color de brillo | Segmentación/seguimiento por color |
| CIELAB | L\*, a\*, b\* | Distancias perceptualmente uniformes | Comparar colores, mejorar contraste |
| YCrCb | Luma + crominancias | Separa luminancia | Compresión, detección de piel |

---

## 4. Operaciones entre imágenes: AND y diferencia `[CURSO]`

### 4.1 Operación AND entre dos imágenes (máscaras)

- La operación **AND se aplica píxel por píxel**: `I_resultado(x, y) = I1(x, y) AND I2(x, y)`, **aplicada a cada canal (R, G, B)**.
- Ejemplo de la diapositiva: **Imagen 1** (paisaje) AND **Imagen 2** (máscara de círculos blancos sobre fondo negro) = **resultado**: solo se ven las partes del paisaje dentro de los círculos.
- **Lógica:** `1 AND 1 = 1` (se conserva), `0 AND 1 = 0` (se elimina), `1 AND 0 = 0` (se elimina), `0 AND 0 = 0` (se elimina).
- **En imágenes:** blanco (255) actúa como 1 (conserva el píxel); negro (0) actúa como 0 (elimina el píxel).
- **Ejemplo numérico de un píxel:** paisaje `(R,G,B) = (120, 200, 150)`.
  - Dentro del círculo (máscara 255,255,255): resultado `(120, 200, 150)` → **se conserva**.
  - Fuera del círculo (máscara 0,0,0): resultado `(0, 0, 0)` → **se elimina**.
- **Aplicaciones:** aplicar máscaras, extraer regiones de interés (ROI), segmentación, visión por computadora.

```python
import cv2
import numpy as np

img = cv2.imread("paisaje.jpg")
mascara = np.zeros(img.shape[:2], dtype=np.uint8)          # 1 canal, negro
cv2.circle(mascara, (150, 120), 80, 255, -1)               # círculo blanco relleno (x, y)
cv2.circle(mascara, (400, 200), 50, 255, -1)

resultado = cv2.bitwise_and(img, img, mask=mascara)        # forma recomendada
# Alternativa con máscara de 3 canales:
# mascara3 = cv2.cvtColor(mascara, cv2.COLOR_GRAY2BGR)
# resultado = cv2.bitwise_and(img, mascara3)
```

> **[NOTA DE PRECISIÓN]** `bitwise_and` opera **bit a bit** sobre los 8 bits. Con una máscara de 255 (`11111111`) el valor original se conserva (`120 & 255 = 120`) y con 0 se anula. Con una máscara que no sea 0/255 el resultado no es una "conservación" limpia, por eso las máscaras deben ser binarias.

**Familia de operaciones lógicas `[AMPLIACIÓN]`:** `cv2.bitwise_or` (unión de regiones), `cv2.bitwise_xor` (diferencia simétrica), `cv2.bitwise_not` (invertir máscara: fondo ↔ objeto). Combinadas con `cv2.inRange` forman el flujo "segmentar por color → aislar objeto".

### 4.2 Diferencia entre imágenes: `absdiff` + umbral

- **Idea:** para hallar diferencias entre dos imágenes se usa la **resta absoluta** (`absdiff`) y luego un **umbral** (`threshold`) para resaltar los cambios.
- **Pasos** (según la diapositiva "¿Cómo funciona en OpenCV?"):
  1. Cargar imagen 1 (original).
  2. Cargar imagen 2 (con cambios).
  3. Calcular la diferencia absoluta por píxel: `|I1(x,y) − I2(x,y)|`.
  4. Convertir a escala de grises.
  5. Aplicar umbral: solo quedan las diferencias (blanco = cambio).
  6. Mostrar resultados.
- **Interpretación:** valores cercanos a 0 (negro) = zonas iguales; valores altos (blanco) = zonas diferentes; el umbral convierte esas diferencias en blanco puro para verlas fácil.

**Código de la diapositiva:**

```python
import cv2
import numpy as np

# 1. Cargar imágenes
img1 = cv2.imread('imagen1.png')   # Imagen original
img2 = cv2.imread('imagen2.png')   # Imagen con diferencias

# 2. Asegurar mismo tamaño
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))   # (ancho, alto)

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

**Tabla de ejemplo de un píxel (umbral > 30):**

| Imagen 1 (I1) | Imagen 2 (I2) | Resta abs \|I1−I2\| | Umbral (>30) |
|---------------|---------------|---------------------|--------------|
| 120 | 120 | 0 | 0 (negro) |
| 200 | 50 | 150 | 255 (blanco) |
| 80 | 90 | 10 | 0 (negro) |

- **Leyenda:** `0 = sin diferencia (negro)`, `255 = diferencia (blanco)`.
- **Conclusión del curso:** OpenCV detecta diferencias usando resta absoluta + umbralización; es la base de juegos "Encuentra las diferencias" y de aplicaciones de visión.
- **Aplicaciones:** juegos infantiles, detección de cambios, seguridad y vigilancia, seguimiento de objetos.

### 4.3 Mejoras y advertencias `[AMPLIACIÓN]`

- **No restar con `-` de NumPy en `uint8`:** `img1 - img2` **da la vuelta** (wrap-around: `50 − 200 = 106`). Usar `cv2.absdiff` o `cv2.subtract` (que satura en 0).
- **Ruido y luz:** cambios de iluminación o ruido de cámara generan falsos positivos. Suavizar antes (`GaussianBlur`) y limpiar después con morfología (apertura para quitar puntos, cierre para rellenar).
- **Ubicar las diferencias:** tras el umbral, `cv2.findContours` + `cv2.boundingRect` (sección 8) permiten encerrar cada diferencia en un recuadro (así se ve el resultado final con círculos rojos en la diapositiva).
- **Umbral automático:** `cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)` elige el umbral solo (funciona bien con histogramas bimodales).
- Requiere imágenes **alineadas** (misma cámara/posición). Si no, primero registrar/alinear.
- Extensión natural al video: **sustracción de fondo** (`cv2.createBackgroundSubtractorMOG2()`), que es una diferencia contra un modelo de fondo adaptativo.

---

## 5. Filtros y convolución `[CURSO]`

### 5.1 ¿Qué es un filtro?

- Un **filtro** es una operación aplicada a una imagen para **modificar sus píxeles** con el objetivo de **resaltar información importante o reducir ruido**.
- Se usan para: mejorar la calidad de la imagen, extraer bordes, detectar patrones, suavizar, realzar detalles.
- La mayoría de los filtros funcionan por **convolución**: se **mueve una pequeña matriz (kernel) sobre cada píxel** de la imagen y se calcula un nuevo valor a partir de los píxeles vecinos.

### 5.2 ¿Qué es el kernel?

- El **kernel** (o máscara) es una **pequeña matriz de números** que define cómo se combinan los píxeles vecinos.
  - Se desplaza por toda la imagen.
  - En cada posición se **multiplica elemento a elemento** con la vecindad de la imagen.
  - Luego se **suman** los resultados para obtener el nuevo valor del píxel central.
- Un kernel de 3×3 tiene 9 valores que determinan el comportamiento del filtro.

**Ejemplo numérico de la diapositiva:**

```
Vecindad (3×3)        Kernel (3×3)        Resultado
105 110 108           1 1 1
100 102  98     *     1 1 1         =        900
 95  90  92           1 1 1
```
Suma total = 105+110+108+100+102+98+95+90+92 = **900** → nuevo valor del píxel central.

> **[NOTA DE PRECISIÓN]** Con un kernel de puros 1 esto es una **suma**, no un promedio. Un filtro de media (box filter) real normaliza dividiendo entre 9 → 100. Los kernels de suavizado se **normalizan** (suman 1) para no cambiar el brillo global; por eso el Gaussiano lleva el factor `1/16`.

### 5.3 Tres filtros importantes (diapositiva "Tres filtros importantes")

**1) Filtro Gaussiano (suavizado)** — Reduce el ruido y suaviza cambios bruscos de intensidad.
```
        1  2  1
1/16 ×  2  4  2
        1  2  1
```

**2) Filtro de Sobel (detección de bordes)** — Detecta bordes resaltando los cambios de intensidad en horizontal y vertical.
```
Sobel X (Gx)        Sobel Y (Gy)
-1  0  1            -1 -2 -1
-2  0  2             0  0  0
-1  0  1             1  2  1
```
El ejemplo de la diapositiva muestra "bordes en X + Y" (se combinan ambos gradientes).

**3) Filtro Laplaciano (realce de bordes)** — Resalta bordes y detalles finos; útil para identificar contornos.
```
0  1  0
1 -4  1
0  1  0
```

### 5.4 Código y variantes `[AMPLIACIÓN]`

```python
import cv2
import numpy as np

gris = cv2.imread("casa.jpg", cv2.IMREAD_GRAYSCALE)

# Kernel manual con filter2D (aplica correlación con el kernel dado)
k_gauss = np.array([[1, 2, 1],
                    [2, 4, 2],
                    [1, 2, 1]], dtype=np.float32) / 16
suave_manual = cv2.filter2D(gris, -1, k_gauss)

# Funciones dedicadas (equivalentes/optimizadas)
suave = cv2.GaussianBlur(gris, (3, 3), 0)     # sigma=0 → OpenCV lo calcula del tamaño

# Sobel: usar float (CV_64F) para conservar valores negativos
sx = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3)   # derivada en x → bordes verticales
sy = cv2.Sobel(gris, cv2.CV_64F, 0, 1, ksize=3)   # derivada en y → bordes horizontales
magnitud = cv2.magnitude(sx, sy)                  # sqrt(sx² + sy²)
sobel_xy = cv2.convertScaleAbs(magnitud)          # a uint8 para mostrar

# Laplaciano (ksize=1 usa exactamente el kernel [[0,1,0],[1,-4,1],[0,1,0]])
lap = cv2.convertScaleAbs(cv2.Laplacian(gris, cv2.CV_64F, ksize=1))
```

**Otros filtros de suavizado que conviene conocer:**

| Filtro | Función | Cuándo |
|--------|---------|--------|
| Media (box) | `cv2.blur(img, (5,5))` | Suavizado simple y rápido |
| Gaussiano | `cv2.GaussianBlur(img, (5,5), 0)` | Ruido gaussiano; paso previo a bordes |
| Mediana | `cv2.medianBlur(img, 5)` | Ruido "sal y pimienta" (puntos blancos/negros) |
| Bilateral | `cv2.bilateralFilter(img, 9, 75, 75)` | Suaviza **preservando bordes** (más lento) |

**Detalles técnicos:**
- **Convolución vs. correlación:** la convolución matemática voltea el kernel; `cv2.filter2D` hace correlación (sin voltear). Para kernels simétricos (Gaussiano, Laplaciano) es igual; para Sobel cambia solo el signo.
- **Tamaño del kernel:** siempre **impar** (3, 5, 7…). Más grande = más suavizado/desenfoque.
- **Bordes de la imagen:** OpenCV rellena con reflejo por defecto (`BORDER_REFLECT_101`).
- **Sigma (σ):** controla el ancho de la campana Gaussiana; a mayor σ, más desenfoque.
- **Separabilidad:** el Gaussiano 2D se puede aplicar como dos pasadas 1D (más rápido).
- **Sobel** aproxima la derivada (gradiente); **Laplaciano** aproxima la segunda derivada y es **muy sensible al ruido** → suavizar antes (esto es el filtro **LoG**, Laplaciano de Gaussiano).

---

## 6. Filtro Gaussiano en detalle `[CURSO]`

### 6.1 Idea (diapositiva "Filtro gaussiano")

Título de la diapositiva: *"De imágenes ruidosas a información útil"* — Visión artificial: imágenes claras para mejores decisiones. Estructura en 3 partes:

**1. Una imagen puede contener ruido.**
- El ruido produce pequeñas variaciones de intensidad que pueden dificultar el análisis.
- Ejemplo con una vecindad 3×3 donde el centro vale **200** y los vecinos **10**: el 200 es una variación muy fuerte respecto a sus vecinos.

**2. El filtro combina cada píxel con sus vecinos.**
- **Máscara gaussiana:** centro = mayor peso (4), vecinos (arriba/abajo/izq/der) = peso intermedio (2), esquinas = menor peso (1). **Todo dividido entre 16.**
- **Cálculo del nuevo valor:**
  ```
  Nuevo valor = (1·10 + 2·10 + 1·10 +
                 2·10 + 4·200 + 2·10 +
                 1·10 + 2·10 + 1·10) / 16
              = 920 / 16
              = 57.5
  ```
- El valor extremo se reduce al mezclarse con la información de los píxeles vecinos (200 → 57.5).

**3. La imagen queda más suave y estable.**
- Imagen original → filtro gaussiano → imagen suavizada.
- **El suavizado facilita tareas posteriores:** detección de bordes, reconocimiento de objetos, segmentación, análisis de formas.
- *"El filtro no busca detectar objetos directamente; prepara la imagen para que otros algoritmos trabajen mejor."*

**Conclusión del curso:** el filtro gaussiano reduce variaciones pequeñas de intensidad **reemplazando cada píxel por un promedio ponderado de sus vecinos**. Flujo: **Ruido → Promedio ponderado → Imagen suavizada.**

(La diapositiva anterior muestra un ejemplo "Before/After" de una ciudad de noche con ruido fuerte a la izquierda y la imagen limpia a la derecha.)

### 6.2 Verificación en código `[AMPLIACIÓN]`

```python
import numpy as np
import cv2

vecindad = np.array([[10, 10, 10],
                     [10, 200, 10],
                     [10, 10, 10]], dtype=np.float32)
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], dtype=np.float32) / 16

print((vecindad * kernel).sum())   # 57.5

# Sobre una imagen real
ruidosa = cv2.imread("ruidosa.jpg")
limpia = cv2.GaussianBlur(ruidosa, (5, 5), 0)
```

**Práctica recomendada:** el suavizado gaussiano es el **primer paso** de casi todos los pipelines de bordes/contornos (Canny lo incluye como etapa 1; la detección de polígonos lo aplica antes de Canny).

---

## 7. Algoritmo de Canny `[CURSO]`

### 7.1 Qué es y relación con las derivadas

- **Canny** es un método de **detección de bordes** que identifica **cambios bruscos en la intensidad** de los píxeles, usando **derivadas** para encontrar dónde la intensidad cambia significativamente: eso corresponde a los bordes de los objetos.
- Se considera la intensidad `I(x, y)` como una **función**; las derivadas miden cuánto cambia esa intensidad.
- **Derivadas parciales:** `Gx = ∂I/∂x` (cambios en horizontal) y `Gy = ∂I/∂y` (cambios en vertical).
- **Magnitud del gradiente:** `G = √(Gx² + Gy²)` → indica **la fuerza del borde** en cada píxel.
- **Dirección del gradiente:** `θ = tan⁻¹(Gy / Gx)`.
- **Aproximación de derivadas — operador Sobel:** las derivadas se aproximan con **convoluciones**. Sobel horizontal (Gx) `[[-1,0,1],[-2,0,2],[-1,0,1]]`; Sobel vertical (Gy) es su **transpuesta** `[[-1,-2,-1],[0,0,0],[1,2,1]]`.

### 7.2 Etapas del algoritmo de Canny (5 etapas)

| Etapa | Nombre | Qué hace |
|-------|--------|----------|
| 1 | **Suavizado Gaussiano** | Reduce el ruido de la imagen |
| 2 | **Cálculo de derivadas** | Obtiene Gx y Gy usando filtros como Sobel |
| 3 | **Magnitud y dirección** | Calcula la magnitud G y la dirección θ del gradiente |
| 4 | **Supresión de no máximos** | Conserva solo los máximos locales en la dirección del gradiente (afina los bordes a 1 píxel) |
| 5 | **Umbralización por histéresis** | Usa **dos umbrales (alto y bajo)** para eliminar bordes débiles y ruido |

Regla de la histéresis (leyenda de la diapositiva):
- **Bordes fuertes:** se conservan.
- **Bordes débiles:** se conservan **si están conectados a bordes fuertes**.
- **Ruido:** se elimina.

**Objetivo de Canny:** detectar bordes verdaderos con **buena localización, buena detección y mínima respuesta a ruido**.
- **Buena detección:** encuentra la mayoría de los bordes reales.
- **Buena localización:** los bordes detectados están cerca de la posición real.
- **Mínima respuesta a ruido:** reduce falsas detecciones causadas por ruido.

**Resumen del curso:** Canny usa derivadas (gradientes) para encontrar cambios importantes de intensidad y así detectar bordes de manera precisa y robusta.

### 7.3 Matemáticas paso a paso (ejemplo 3×3)

Imagen 3×3 con un salto brusco: columnas izquierdas **10, 10** (oscuro) y columna derecha **200** (claro) en las tres filas → sugiere un **borde vertical**.

```
10  10  200
10  10  200
10  10  200
```

**Cálculo del gradiente con Sobel:**
- `Gx = (−1·10) + (0·10) + (1·200) + (−2·10) + (0·10) + (2·200) + (−1·10) + (0·10) + (1·200)`
  `= −10 + 0 + 200 − 20 + 0 + 400 − 10 + 0 + 200 = 760`
- `Gy = (−1·10) + (−2·10) + (−1·200) + (0·10) + (0·10) + (0·200) + (1·10) + (2·10) + (1·200) = 0`
- **Magnitud:** `G = √(Gx² + Gy²) = √(760² + 0²) = 760`
- **Dirección:** `θ = arctan(Gy / Gx) = arctan(0 / 760) = 0°` → como Gx es grande y Gy es 0, el algoritmo detecta un **borde vertical**.

**Decisión: ¿es borde o no?** (regla didáctica de la diapositiva)

| Valor de G | Resultado |
|------------|-----------|
| G > 300 | borde fuerte |
| 100 < G ≤ 300 | borde débil |
| G ≤ 100 | no es borde |

Como `G = 760`, este punto se clasifica como **borde fuerte**. Salida binaria de ejemplo: `[[0,255,0],[0,255,0],[0,255,0]]` (columna central blanca = borde).

**Flujo del algoritmo (diapositiva):** Matriz de entrada → Sobel en x e y → Magnitud y dirección → Umbral → Borde detectado.

**Conclusión del curso:** Canny identifica bordes midiendo matemáticamente los cambios de intensidad entre píxeles; el salto de 10 a 200 produce un gradiente alto, por lo que se detecta un borde vertical.

### 7.4 Verificación en código y uso real `[AMPLIACIÓN]`

```python
import numpy as np
import cv2

# Reproducir el ejemplo del curso
parche = np.array([[10, 10, 200]] * 3, dtype=np.float32)
Gx_k = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
Gy_k = Gx_k.T                                   # [[-1,-2,-1],[0,0,0],[1,2,1]]
gx = (parche * Gx_k).sum()                      # 760
gy = (parche * Gy_k).sum()                      # 0
G = np.hypot(gx, gy)                            # 760
theta = np.degrees(np.arctan2(gy, gx))          # 0°
print(gx, gy, G, theta)

# Canny real en OpenCV (hace TODAS las etapas: derivadas, NMS e histéresis)
img = cv2.imread("casa.jpg", cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(img, (5, 5), 0)         # etapa 1 (recomendado aunque Canny no la incluye)
bordes = cv2.Canny(blur, 100, 200)              # umbral_bajo=100, umbral_alto=200

# Umbrales automáticos basados en la mediana
def canny_auto(gris, sigma=0.33):
    v = np.median(gris)
    bajo = int(max(0, (1.0 - sigma) * v))
    alto = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(gris, bajo, alto)
```

> **[NOTA DE PRECISIÓN]**
> - **`cv2.Canny(img, umbral_bajo, umbral_alto)`** aplica internamente Sobel + NMS + histéresis. Los umbrales 100/300 de la diapositiva son didácticos; en la práctica se usan pares como `(50,150)`, `(100,200)`, con relación alto:bajo ≈ **2:1 o 3:1**.
> - Por defecto OpenCV mide la magnitud con `|Gx|+|Gy|` (norma L1); con `L2gradient=True` usa `√(Gx²+Gy²)` (la fórmula del curso).
> - Con Sobel 3×3 sobre imágenes de 8 bits la magnitud puede superar 255 (máx. teórico ≈ 1020 por eje), por eso los umbrales de la diapositiva (300) tienen sentido en ese contexto.
> - La **dirección** del gradiente es perpendicular al borde: un borde vertical tiene gradiente horizontal (θ = 0°).
> - **NMS** cuantiza θ en 4 direcciones (0°, 45°, 90°, 135°) y compara cada píxel con sus dos vecinos en esa dirección.

**Parámetros que se ajustan en la práctica:** tamaño y σ del blur, umbral bajo/alto, `apertureSize` (3, 5, 7) y `L2gradient`. Poco blur → muchos bordes de ruido; demasiado blur → se pierden bordes finos.

---

## 8. Operaciones morfológicas `[CURSO]`

Las operaciones morfológicas trabajan sobre **imágenes binarias** (fondo = 0, objeto = 1/255) usando un **elemento estructurante (kernel)**.

### 8.1 Diapositiva de introducción (tres imágenes binarias)

Muestra tres imágenes en blanco y negro: (1) un campo con **muchos cuadrados blancos de distintos tamaños y puntitos de ruido**; (2) una imagen casi negra con solo **tres puntos diminutos**; (3) una imagen con **solo los tres cuadrados grandes**.

> **[AMPLIACIÓN – interpretación]** La diapositiva no trae leyenda; lo más coherente es que ilustra la secuencia **erosión → dilatación** (= **apertura**): la erosión elimina el ruido y encoge los objetos (los grandes quedan como puntos), y la dilatación siguiente devuelve el tamaño a lo que sobrevivió, quedando solo los objetos grandes. Es el ejemplo clásico de "filtrar objetos por tamaño".

### 8.2 Dilatación morfológica

- **¿Qué es?** La dilatación **agrega píxeles a los bordes de los objetos (valor 1)** utilizando un kernel.
- **Kernel utilizado (3×3):** todo unos `[[1,1,1],[1,1,1],[1,1,1]]`; el kernel define la **forma y dirección de la expansión**.
- Ejemplo paso a paso con una **imagen de 9×9**:
  - **Caso 1 – todo es 0:** el kernel se posiciona arriba a la izquierda, se mueve a la derecha, luego hacia abajo y recorre toda la imagen; como todos los píxeles son 0 **no se agregan píxeles y la imagen permanece igual**.
  - **Caso 2 – el kernel encuentra un 1:** se recorre la imagen; cuando el kernel se coloca sobre el 1 (el 1 queda en el centro) **se agregan píxeles (dilatación)**. Resultado: **un solo píxel 1 se convierte en un bloque de 3×3 de unos** — el objeto se expande en todas las direcciones según el kernel.
- Leyenda de colores: negro/0 = fondo; verde/1 = objeto; recuadro azul = posición del kernel (3×3); recuadro rojo = píxel central del kernel; verde claro = píxeles agregados por la dilatación.

### 8.3 Erosión morfológica

- **¿Qué es?** La erosión **elimina píxeles en los bordes de los objetos (valor 1)** utilizando un kernel. **Solo el píxel central se mantiene en 1 si TODOS los píxeles bajo el kernel son 1.**
- Mismo kernel 3×3 de unos; ejemplo con imagen 9×9:
  - **Caso 1 – todo es 0:** no se cumple la condición; no se elimina nada porque no hay píxeles con valor 1.
  - **Caso 2 – el kernel encuentra un 1:** mientras el píxel central es 0, o no todos los píxeles bajo el kernel son 1, **no se cambia nada**. Cuando el kernel se coloca sobre el centro del objeto (todos los valores son 1) **se mantiene el 1 y se eliminan los demás**. Resultado: **solo el píxel central del objeto se mantiene en 1; los bordes se eliminan.**

### 8.4 Código y operaciones derivadas `[AMPLIACIÓN]`

```python
import cv2
import numpy as np

# --- Reproducir los ejemplos 9x9 de la presentación ---
img = np.zeros((9, 9), dtype=np.uint8)
img[4, 4] = 1                                           # un solo 1
k = np.ones((3, 3), dtype=np.uint8)
dil = cv2.dilate(img, k)
print(dil)                                              # bloque de 3x3 unos alrededor de (4,4)

obj = np.zeros((9, 9), dtype=np.uint8)
obj[3:6, 3:6] = 1                                       # objeto de 3x3
ero = cv2.erode(obj, k)
print(ero)                                              # queda solo el píxel (4,4)

# --- Con imágenes reales (0/255) ---
binaria = cv2.imread("binaria.png", cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))   # también MORPH_ELLIPSE, MORPH_CROSS

erosion  = cv2.erode(binaria, kernel, iterations=1)
dilatac  = cv2.dilate(binaria, kernel, iterations=1)
apertura = cv2.morphologyEx(binaria, cv2.MORPH_OPEN,  kernel)   # erosión → dilatación
cierre   = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, kernel)   # dilatación → erosión
gradiente = cv2.morphologyEx(binaria, cv2.MORPH_GRADIENT, kernel)  # dilatación − erosión = contorno
```

| Operación | Definición | Efecto | Uso típico |
|-----------|------------|--------|------------|
| **Erosión** | mínimo bajo el kernel | Encoge objetos, elimina ruido pequeño | Quitar puntos/ruido, separar objetos que se tocan |
| **Dilatación** | máximo bajo el kernel | Agranda objetos, rellena huecos pequeños | Unir fragmentos, conectar bordes rotos |
| **Apertura** | erosión → dilatación | Quita ruido/objetos pequeños sin encoger mucho los grandes | Limpiar máscaras |
| **Cierre** | dilatación → erosión | Rellena agujeros pequeños dentro de objetos | Completar objetos con huecos |
| **Gradiente** | dilatación − erosión | Deja el contorno del objeto | Extraer bordes |
| **Top-hat / Black-hat** | imagen − apertura / cierre − imagen | Resalta detalles claros / oscuros pequeños | Iluminación desigual, defectos |

> **[NOTA DE PRECISIÓN]** Las diapositivas explican el proceso desde la perspectiva del **píxel central del kernel** ("el píxel central es 0, no se agrega nada" hasta que el kernel se centra sobre el 1). La definición formal es: **dilatación → el píxel de salida es 1 si AL MENOS UN píxel bajo el kernel es 1 (máximo)**; **erosión → es 1 solo si TODOS los píxeles bajo el kernel son 1 (mínimo)**. El resultado final es idéntico al de las diapositivas (un 1 aislado se vuelve un bloque 3×3; un objeto 3×3 se reduce a un píxel). También: el tamaño y forma del kernel controlan cuánto y hacia dónde crece o se encoge el objeto (`iterations` repite el proceso).

---

## 9. Detección de figuras geométricas `[CURSO]`

### 9.1 Pipeline general de detección de polígonos (visión general, 7 pasos)

| Paso | Nombre | Descripción | Código de la diapositiva |
|------|--------|-------------|--------------------------|
| 1 | Imagen original | Se captura el frame desde la cámara | `frame` |
| 2 | Conversión a gris | Se convierte la imagen a escala de grises | `gris` |
| 3 | Gaussian Blur | Suavizado para reducir el ruido | `gauss = GaussianBlur(gris)` |
| 4 | Detección de bordes | Se aplica Canny para detectar bordes | `bordes = Canny(gauss)` |
| 5 | Encontrar contornos | Se buscan los contornos en la imagen de bordes | `contornos = findContours(bordes)` |
| 6 | Aproximación y clasificación | Cada contorno se aproxima a un polígono y se cuenta el número de lados | `aproximacion = approxPolyDP(contorno)`, `lados = len(aproximacion)` |
| 7 | Dibujar y resultado final | Se dibujan los polígonos, sus vértices y el nombre según los lados | `salida = dibujar_poligonos(frame, contornos, ...)` |

**Clasificación por número de lados:** 3 → Triángulo · 4 → Cuadrado/Rectángulo · 5 → Pentágono · 6 → Hexágono · 7+ → Polígono (n lados).

**Resumen del proceso:** `Frame → Gris → Gaussian Blur → Canny (bordes) → Contornos → Aproximación → Clasificación → Dibujo del resultado`.

Escena de ejemplo: figuras de colores sobre una mesa de madera (triángulo azul, cuadrado verde, pentágono rojo, hexágono amarillo, rectángulo morado), que se detectan y etiquetan ("Triángulo (3)", "Cuadrado (4)", "Pentágono (5)", "Hexágono (6)", "Rectángulo (4)").

### 9.2 Aproximación de contornos — proceso general (8 pasos)

Objetivo: **convertir los contornos detectados en polígonos con menos vértices para poder clasificar formas.**

1. **Imagen binaria (bordes):** partir de una imagen donde los bordes están definidos (ej. con Canny).
2. **Encontrar contornos:** `findContours()` detecta contornos conectados; cada contorno es una **lista de puntos**.
3. **Contorno como conjunto de puntos:** muchos puntos que siguen el borde del objeto.
4. **Simplificación del contorno:** se aplica el **algoritmo de Douglas–Peucker** (implementado en `approxPolyDP()`), que **elimina puntos innecesarios manteniendo la forma general**.
5. **Contorno aproximado:** polígono con menos vértices que representa al objeto.
6. **Contar vértices:** número de lados del polígono aproximado (ej. "5 lados").
7. **Clasificar la forma:** 3 triángulo, 4 cuadrado/rectángulo, 5 pentágono, 6 hexágono, 7 heptágono, 8 octágono, n polígono de n lados.
8. **Uso en la detección:** se dibuja el polígono aproximado sobre la imagen original.

**Resumen:** `Bordes (Canny) → findContours() → Contornos (puntos) → approxPolyDP() → Polígono aproximado → Contar lados → Clasificar forma`.

### 9.3 ¿Cómo funciona `approxPolyDP()`? (Douglas–Peucker)

- **Sintaxis:** `approxPolyDP(contorno, epsilon, cerrado)`
  - `contorno`: puntos del contorno (lista de puntos).
  - `epsilon`: **tolerancia** (double).
  - `cerrado`: `True` si el contorno está cerrado, `False` si está abierto.
- **¿Qué es?** El algoritmo de Douglas–Peucker adaptado a polígonos: elimina puntos intermedios que están "cerca" de la línea que une dos vértices importantes.
- **Parámetro clave `epsilon`:** es la **distancia máxima permitida** entre un punto del contorno original y el segmento que lo reemplaza.
  - **Mayor epsilon → más simplificación (menos vértices).**
  - **Menor epsilon → menos simplificación (más vértices).**
- **Idea principal:** conservar los puntos "importantes" (esquinas) y eliminar los que no cambian la forma del contorno más allá de la tolerancia.
- **Paso a paso del algoritmo:**
  1. **Contorno original:** muchos puntos.
  2. **Unir extremos:** se toma el primer y último punto y se traza una línea recta.
  3. **Distancia máxima:** se busca el punto más alejado de esa línea y se mide su **distancia perpendicular `d`**.
  4. **Comparar con epsilon:** si `d > epsilon`, ese punto se considera importante y **divide el contorno en dos partes**.
  5. **Repetir recursivamente** en cada parte hasta que todos los puntos estén a una distancia ≤ epsilon.
- **Efecto del valor de epsilon:** con epsilon muy pequeño el resultado es muy detallado (casi todos los puntos); con epsilon grande, muy simplificado (pocos vértices, forma casi poligonal).

### 9.4 ¿Qué hace `cv2.boundingRect(aproximacion)?`

- Devuelve el **rectángulo alineado con los ejes (horizontal y vertical) más pequeño que contiene completamente al contorno o polígono**.
- **Sintaxis:** `x, y, w, h = cv2.boundingRect(aproximacion)`
  - `x`: coordenada X de la esquina superior izquierda.
  - `y`: coordenada Y de la esquina superior izquierda.
  - `w`: ancho del rectángulo.
  - `h`: alto del rectángulo.
- **Cómo funciona:** (1) contorno aproximado → (2) buscar extremos (`minX, maxX, minY, maxY`) → (3) definir rectángulo → (4) devolver `x = minX, y = minY, w = maxX − minX, h = maxY − minY`.
- **Ejemplos de la diapositiva:** si devuelve `(50, 30, 120, 80)` → esquina (50,30), ancho 120, alto 80. Ejemplo real con un pentágono: `(x, y, w, h) = (84, 63, 198, 146)`.
- **¿Para qué sirve?**
  - Obtener la **posición y tamaño** de un objeto detectado.
  - Dibujar **cuadros (bounding boxes)** alrededor de formas.
  - **Recortar (ROI)** la región que contiene el objeto.
  - Calcular **relaciones de aspecto**, centrar objetos, etc.

### 9.5 Implementación completa del pipeline `[AMPLIACIÓN]`

```python
import cv2
import numpy as np

def detectar_figuras(frame, area_minima=500):
    """Detecta y clasifica polígonos siguiendo el pipeline del curso."""
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)             # 2. gris
    gauss = cv2.GaussianBlur(gris, (5, 5), 0)                  # 3. suavizado
    bordes = cv2.Canny(gauss, 50, 150)                         # 4. bordes
    # Cerrar pequeños huecos en los bordes para que los contornos queden cerrados
    bordes = cv2.dilate(bordes, np.ones((3, 3), np.uint8), iterations=1)

    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)   # 5. contornos
    salida = frame.copy()

    for contorno in contornos:
        if cv2.contourArea(contorno) < area_minima:            # descartar ruido
            continue

        perimetro = cv2.arcLength(contorno, True)
        epsilon = 0.02 * perimetro                             # 1%-5% del perímetro
        aproximacion = cv2.approxPolyDP(contorno, epsilon, True)   # 6. aproximar
        lados = len(aproximacion)
        x, y, w, h = cv2.boundingRect(aproximacion)

        if lados == 3:
            nombre = "Triangulo"
        elif lados == 4:
            relacion = w / float(h)
            nombre = "Cuadrado" if 0.95 <= relacion <= 1.05 else "Rectangulo"
        elif lados == 5:
            nombre = "Pentagono"
        elif lados == 6:
            nombre = "Hexagono"
        else:
            area = cv2.contourArea(contorno)
            circularidad = 4 * np.pi * area / (perimetro ** 2)
            nombre = "Circulo" if circularidad > 0.8 else f"Poligono ({lados})"

        cv2.drawContours(salida, [aproximacion], -1, (0, 255, 0), 2)     # 7. dibujar
        for p in aproximacion:
            cv2.circle(salida, tuple(p[0]), 4, (0, 0, 255), -1)          # vértices
        cv2.putText(salida, f"{nombre} ({lados})", (x, y - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return salida

# Uso con cámara
cap = cv2.VideoCapture(0)
while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow("Figuras", detectar_figuras(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

**Detalles importantes de `findContours` / contornos:**
- En **OpenCV 4.x** `cv2.findContours` devuelve **2 valores** `(contornos, jerarquia)`; en OpenCV 3.x devolvía 3. Si sale error de "unpack", revisar la versión (`cv2.__version__`).
- **Modos de recuperación:** `RETR_EXTERNAL` (solo contornos exteriores), `RETR_LIST` (todos sin jerarquía), `RETR_TREE` (jerarquía completa: útil con objetos con huecos).
- **Métodos de aproximación:** `CHAIN_APPROX_NONE` (todos los puntos), `CHAIN_APPROX_SIMPLE` (comprime segmentos rectos, ahorra memoria).
- `findContours` espera una imagen **binaria** (sirve la salida de Canny o de `threshold`). Alternativa habitual y más robusta para figuras rellenas: `threshold`/`inRange` + morfología en vez de Canny.
- **Epsilon típico:** `0.01–0.05 × perímetro` (`cv2.arcLength(contorno, True)`). Muy bajo → contar demasiados lados (ruido); muy alto → se pierden esquinas.
- **Propiedades útiles:** `cv2.contourArea`, `cv2.arcLength`, `cv2.isContourConvex`, `cv2.minAreaRect` (rectángulo rotado), `cv2.minEnclosingCircle`, `cv2.convexHull`, `cv2.moments` (centroide: `cx = M["m10"]/M["m00"]`, `cy = M["m01"]/M["m00"]`).
- **Cuadrado vs. rectángulo:** ambos tienen 4 lados; se distinguen con la **relación de aspecto** `w/h` (≈ 1 → cuadrado). Para figuras rotadas usar `minAreaRect`.
- **Círculo:** un círculo aproximado produce muchos lados; distinguirlo con la **circularidad** `4πA/P²` (≈ 1 para un círculo) o con `cv2.HoughCircles`.
- **Limitaciones:** figuras superpuestas/tocándose, sombras, fondos con textura, perspectiva fuerte y bajo contraste degradan el resultado.

---

## 10. Pipeline integrado del curso `[CURSO + AMPLIACIÓN]`

```
                ┌───────────────┐
 Imagen (BGR) → │ Espacio color │ → HSV / LAB / Gris
                └──────┬────────┘
                       │
          ┌────────────┴───────────┐
          │ Suavizado (Gaussiano)  │ ← reduce ruido
          └────────────┬───────────┘
                       │
        ┌──────────────┴───────────────┐
        │ Bordes (Sobel/Laplaciano/    │
        │ Canny)  o  Segmentación      │
        │ (inRange / threshold / AND)  │
        └──────────────┬───────────────┘
                       │
        ┌──────────────┴───────────────┐
        │ Morfología (abrir/cerrar)    │ ← limpia la binaria
        └──────────────┬───────────────┘
                       │
        ┌──────────────┴───────────────┐
        │ findContours → approxPolyDP  │
        │ → boundingRect / lados       │
        └──────────────┬───────────────┘
                       │
                Resultado (clasificación, ROI, conteo, dibujo)
```

**Cómo se conectan los temas del curso:**
- **HSV/LAB** → separar color y brillo → `inRange` produce máscara.
- **AND** → aplicar esa máscara a la imagen original.
- **Gaussiano** → pre-limpieza para bordes y umbrales.
- **Canny/Sobel** → bordes; **morfología** → cerrar/limpiar.
- **Contornos + approxPolyDP + boundingRect** → geometría y clasificación.
- **absdiff + threshold** → detección de cambios (variante que usa dos imágenes).

### 10.1 Receta: contar y localizar objetos de un color `[AMPLIACIÓN]`

```python
import cv2
import numpy as np

img = cv2.imread("figuras.jpg")
blur = cv2.GaussianBlur(img, (5, 5), 0)
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

mascara = cv2.inRange(hsv, np.array([100, 120, 70]), np.array([130, 255, 255]))  # azul
k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, k)     # quita ruido
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, k)    # rellena huecos

contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
validos = [c for c in contornos if cv2.contourArea(c) > 300]
print("Objetos azules:", len(validos))

for c in validos:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Resultado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 10.2 Receta: resaltar cambios entre dos imágenes con recuadros `[AMPLIACIÓN]`

```python
import cv2
import numpy as np

a = cv2.imread("imagen1.png")
b = cv2.imread("imagen2.png")
b = cv2.resize(b, (a.shape[1], a.shape[0]))

dif = cv2.absdiff(cv2.GaussianBlur(a, (5, 5), 0), cv2.GaussianBlur(b, (5, 5), 0))
gris = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
_, umbral = cv2.threshold(gris, 30, 255, cv2.THRESH_BINARY)
umbral = cv2.dilate(umbral, np.ones((5, 5), np.uint8), iterations=2)   # une fragmentos

contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in contornos:
    if cv2.contourArea(c) > 100:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(b, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.imshow("Diferencias", b)
cv2.waitKey(0)
```

---

## 11. Errores comunes y notas de precisión sobre las diapositivas `[AMPLIACIÓN]`

### 11.1 Errores frecuentes al programar con OpenCV

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Colores "raros" (rojo ↔ azul) al mostrar con matplotlib | OpenCV usa BGR, matplotlib espera RGB | `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` |
| `AttributeError: 'NoneType' ... shape` | `imread` no encontró el archivo | Revisar ruta; `if img is None: ...` |
| `cv2.error` en `absdiff`/`bitwise_and` | Tamaños o tipos distintos | `cv2.resize` al mismo tamaño; mismo `dtype` y canales |
| Resta de imágenes con "ruido raro" | `img1 - img2` en `uint8` da la vuelta | `cv2.absdiff` / `cv2.subtract` |
| Coordenadas invertidas | `img[y, x]` vs `(x, y)` de las funciones de dibujo | Fila primero al indexar; `(x, y)` al dibujar |
| `ValueError: too many values to unpack` en `findContours` | Diferencia de versiones (OpenCV 3 vs 4) | Usar `contornos, _ = cv2.findContours(...)` en OpenCV 4 |
| Contornos de figuras "abiertas"/fragmentadas | Canny deja huecos | Dilatar bordes o usar umbral + morfología |
| Muchos polígonos con demasiados lados | epsilon muy bajo o sin blur | Subir epsilon (0.02–0.04·perímetro); suavizar |
| Máscara roja incompleta en HSV | El rojo cruza H=0/179 | Dos rangos (0–10 y 170–179) y unir con `bitwise_or` |
| Texto con tildes sale como `???` | Las fuentes Hershey no soportan Unicode | Escribir sin tildes o usar PIL |
| Ventana que no se cierra | Falta `waitKey` | `cv2.waitKey(0)` + `destroyAllWindows()` |

### 11.2 Simplificaciones/detalles de las diapositivas (para responder con precisión)

1. **Diapositiva 2 (matriz BGR):** el título dice "3×3 píxeles", pero el arreglo dibujado muestra 4 filas; es una figura ilustrativa. En el modelo de la diapositiva 1 la imagen es realmente 3×3×3. La bandera oficial de Colombia además tiene proporciones 2:1:1 (amarillo ocupa la mitad).
2. **Diapositiva HSV (bandera):** la imagen "HSV" mostrada es una visualización ilustrativa; no es cómo se ve un arreglo HSV real al graficarlo como BGR.
3. **Fórmula de H con empates (`Cmax = R = G`):** se usa la primera rama aplicable (R). Algunas implementaciones ajustan `H' < 0` sumando 360°; la fórmula con `mod 6` ya evita el caso negativo.
4. **CIELAB:** ver la nota de escala de XYZ (sección 3.4). En OpenCV `uint8`, L\* se reescala a 0–255 y a\*/b\* se desplazan +128.
5. **Kernel de unos = 900:** es suma, no promedio (sección 5.2).
6. **Canny:** los umbrales 100/300 de la diapositiva son didácticos; `cv2.Canny` usa histéresis con umbral bajo/alto (sección 7.4).
7. **Morfología:** las diapositivas explican desde el píxel central; la definición formal es máximo/mínimo bajo el kernel (sección 8.4).
8. **Detección de polígonos:** la diapositiva 7 usa `dibujar_poligonos(...)` como función genérica (no existe en OpenCV; es una función que el estudiante debe escribir).
9. **AND:** requiere máscaras estrictamente binarias (0/255).

---

## 12. Glosario `[CURSO + AMPLIACIÓN]`

| Término | Significado |
|---------|-------------|
| **Píxel** | Unidad mínima de una imagen; en color es un vector (B, G, R). |
| **Canal** | Cada "capa" de una imagen (B, G y R; o H, S y V). |
| **BGR** | Orden de canales que usa OpenCV (Azul, Verde, Rojo). |
| **Escala de grises** | Imagen de 1 canal con intensidades 0–255. |
| **HSV** | Espacio de color Tono–Saturación–Valor. |
| **CIELAB** | Espacio perceptualmente uniforme (L\*, a\*, b\*). |
| **Iluminante D65** | Luz de día estándar usada como blanco de referencia. |
| **Máscara** | Imagen binaria que indica qué píxeles conservar (255) o descartar (0). |
| **Umbral (threshold)** | Valor que separa píxeles en dos clases (0 o 255). |
| **Kernel / núcleo / máscara de convolución** | Matriz pequeña que define cómo se combinan los vecinos. |
| **Convolución** | Deslizar el kernel por la imagen y sumar productos con la vecindad. |
| **Ruido** | Variaciones aleatorias e indeseadas de intensidad. |
| **Gradiente** | Vector de cambio de intensidad (Gx, Gy); magnitud = fuerza del borde. |
| **Sobel** | Kernel que aproxima la derivada de la imagen. |
| **Laplaciano** | Operador de segunda derivada que resalta cambios rápidos. |
| **Borde** | Cambio brusco de intensidad entre regiones. |
| **NMS (supresión de no máximos)** | Adelgaza los bordes conservando el máximo local. |
| **Histéresis** | Uso de dos umbrales (alto/bajo) con conectividad para decidir bordes. |
| **Erosión / Dilatación** | Encoger / agrandar objetos binarios con un kernel. |
| **Apertura / Cierre** | Erosión→dilatación / dilatación→erosión. |
| **Contorno** | Curva (lista de puntos) que delimita un objeto. |
| **Douglas–Peucker** | Algoritmo que simplifica una curva con tolerancia ε. |
| **Epsilon (ε)** | Distancia máxima permitida entre el contorno original y su aproximación. |
| **Bounding box** | Rectángulo alineado a los ejes que encierra un objeto. |
| **ROI** | Región de interés (recorte de la imagen). |
| **Frame** | Un cuadro de video. |
| **Segmentación** | Separar la imagen en regiones/objetos. |

---

## 13. Ampliación: temas relacionados y siguiente paso natural `[AMPLIACIÓN]`

Estos temas continúan la línea del curso y son los que probablemente vendrán o resultan útiles como refuerzo.

### 13.1 Binarización y umbralización
- **Umbral global:** `cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)` (y variantes `_INV`, `TRUNC`, `TOZERO`).
- **Otsu:** calcula el umbral óptimo automáticamente: `cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)`.
- **Adaptativo:** umbral por región, ideal con iluminación desigual: `cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)`.

### 13.2 Histogramas y contraste
- `cv2.calcHist`, `cv2.equalizeHist` (ecualización global), **CLAHE** (ecualización adaptativa con límite de contraste).
- Corrección **gamma** y ajustes de brillo/contraste: `cv2.convertScaleAbs(img, alpha=1.2, beta=20)`.

### 13.3 Transformaciones geométricas
- `cv2.resize`, `cv2.flip`, `cv2.rotate`, `cv2.warpAffine` (rotación/traslación/escala), `cv2.warpPerspective` (corrección de perspectiva, base del **escáner de documentos**), recorte con slicing.

### 13.4 Detección de formas y bordes avanzada
- **Transformada de Hough:** líneas `cv2.HoughLines/HoughLinesP` y círculos `cv2.HoughCircles`.
- **Momentos y descriptores:** `cv2.moments`, `cv2.HuMoments`, `cv2.matchShapes` (comparar formas).
- **Componentes conectados:** `cv2.connectedComponentsWithStats` (contar y medir objetos en una binaria).
- **Watershed** para separar objetos que se tocan.

### 13.5 Características y emparejamiento
- **Template matching:** `cv2.matchTemplate` (buscar una plantilla en la imagen).
- **Detectores de esquinas:** Harris, Shi-Tomasi (`cv2.goodFeaturesToTrack`).
- **Descriptores:** ORB, SIFT, AKAZE + matching (`BFMatcher`, FLANN) para reconocimiento y panoramas.

### 13.6 Video y movimiento
- Captura con `cv2.VideoCapture`; sustracción de fondo (`MOG2`, `KNN`); **flujo óptico** (`calcOpticalFlowPyrLK`, Farneback); seguimiento con `cv2.Tracker*`.

### 13.7 Cámara y geometría
- Calibración de cámara (`cv2.calibrateCamera`), distorsión, marcadores ArUco (`cv2.aruco`), estimación de pose.

### 13.8 Visión con aprendizaje profundo
- Clasificación (CNN), detección de objetos (YOLO, SSD), segmentación (U-Net, Mask R-CNN), y el módulo `cv2.dnn` para ejecutar modelos ya entrenados. Las técnicas clásicas del curso (filtros, bordes, morfología, contornos) siguen siendo el **preprocesamiento** y la base para entender qué aprende una CNN (sus primeras capas aprenden filtros parecidos a Sobel/Gauss).

### 13.9 Proyectos de práctica sugeridos (constructivos)
1. **Clasificador de figuras geométricas** en tiempo real con cámara (pipeline de la sección 9).
2. **Juego "Encuentra las diferencias"** automático (sección 4.2 + recuadros).
3. **Contador de objetos por color** (monedas, fichas, frutas) con HSV + morfología + contornos.
4. **Escáner de documentos:** bordes → contorno de 4 vértices → `warpPerspective`.
5. **Detector de cambios** para monitoreo de un espacio (ej. detectar si un objeto fue movido), cuidando privacidad.
6. **Control de calidad simple:** comparar una pieza contra una referencia con `absdiff` y umbral.
7. **Seguimiento de un objeto de color** para robótica (centroide con momentos).
8. **Visualizador educativo** de convolución: aplicar kernels personalizados y ver el efecto.
9. **Segmentación de la bandera de Colombia** en una foto real (HSV para amarillo/azul/rojo).

### 13.10 Ejercicios de comprensión (con respuestas breves)
1. *¿Cuál es el `shape` de una imagen BGR de 480 filas y 640 columnas?* → `(480, 640, 3)`.
2. *¿Cuál es el valor BGR del amarillo puro?* → `(0, 255, 255)`.
3. *¿Cuál es el H en OpenCV del azul puro?* → 120 (240° / 2).
4. *¿Por qué HSV es mejor que BGR para segmentar por color?* → separa el brillo (V) del tono (H).
5. *Calcula el filtro gaussiano 3×3 con centro 200 y vecinos 10.* → 57.5.
6. *Si Gx = 760 y Gy = 0, ¿cuál es G y θ?* → G = 760, θ = 0° (borde vertical).
7. *¿Qué hace una erosión con un kernel 3×3 sobre un objeto de 3×3 unos?* → deja un solo píxel.
8. *¿Qué pasa al aumentar epsilon en `approxPolyDP`?* → menos vértices, más simplificación.
9. *¿Cómo distingues cuadrado de rectángulo si ambos tienen 4 lados?* → relación de aspecto `w/h`.
10. *¿Qué secuencia morfológica quita ruido pequeño y conserva objetos grandes?* → apertura (erosión → dilatación).

---

## 14. Referencia rápida de funciones (cheat sheet) `[AMPLIACIÓN]`

```python
# Lectura / escritura / ventanas
img = cv2.imread(ruta)                       # BGR uint8 (None si falla)
img_g = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("salida.png", img)
cv2.imshow("titulo", img); cv2.waitKey(0); cv2.destroyAllWindows()

# Canales y color
b, g, r = cv2.split(img);  img = cv2.merge([b, g, r])
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)      # H 0-179, S/V 0-255
lab  = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mask = cv2.inRange(hsv, inferior, superior)

# Operaciones entre imágenes
cv2.bitwise_and(a, b, mask=m); cv2.bitwise_or(a, b); cv2.bitwise_xor(a, b); cv2.bitwise_not(a)
cv2.absdiff(a, b); cv2.add(a, b); cv2.subtract(a, b); cv2.addWeighted(a, .5, b, .5, 0)
_, bin_ = cv2.threshold(gris, 30, 255, cv2.THRESH_BINARY)

# Filtros
cv2.filter2D(img, -1, kernel)
cv2.blur(img, (5,5)); cv2.GaussianBlur(img, (5,5), 0)
cv2.medianBlur(img, 5); cv2.bilateralFilter(img, 9, 75, 75)
cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3); cv2.Laplacian(gris, cv2.CV_64F)
cv2.Canny(gris, 100, 200)

# Morfología
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
cv2.erode(bin_, k); cv2.dilate(bin_, k)
cv2.morphologyEx(bin_, cv2.MORPH_OPEN / MORPH_CLOSE / MORPH_GRADIENT, k)

# Contornos y formas
contornos, jer = cv2.findContours(bin_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.contourArea(c); cv2.arcLength(c, True)
aprox = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
x, y, w, h = cv2.boundingRect(aprox)
cv2.drawContours(img, [aprox], -1, (0,255,0), 2)
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
cv2.putText(img, "texto", (x,y-8), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,0,0), 2)
```

**Valores de referencia del curso:**

| Concepto | Valor |
|----------|-------|
| Amarillo / Azul / Rojo en BGR | `(0,255,255)` / `(255,0,0)` / `(0,0,255)` |
| Amarillo / Azul / Rojo en HSV OpenCV | `(30,255,255)` / `(120,255,255)` / `(0,255,255)` |
| Rangos HSV en OpenCV | H 0–179 · S 0–255 · V 0–255 |
| Rangos CIELAB teóricos | L\* 0–100 · a\*, b\* ≈ −128…127 |
| Blanco D65 | Xn = 95.047, Yn = 100.000, Zn = 108.883 |
| Kernel Gaussiano 3×3 | `1/16 · [[1,2,1],[2,4,2],[1,2,1]]` |
| Sobel Gx / Gy | `[[-1,0,1],[-2,0,2],[-1,0,1]]` / `[[-1,-2,-1],[0,0,0],[1,2,1]]` |
| Laplaciano | `[[0,1,0],[1,-4,1],[0,1,0]]` |
| Ejemplo Gauss | (10s alrededor de 200) → 920/16 = **57.5** |
| Ejemplo Canny 3×3 | Gx = 760, Gy = 0, G = 760, θ = 0° |
| Lados → figura | 3 triángulo · 4 cuadrado/rectángulo · 5 pentágono · 6 hexágono · 7 heptágono · 8 octágono |

---

## 15. Guía de respuesta para Claude según el tipo de pregunta

| Si el usuario pregunta… | Responder con… |
|--------------------------|----------------|
| "Explícame X del curso" | Secciones `[CURSO]` correspondientes: definición → ejemplo numérico del profesor → código. |
| "¿Cómo lo hago en OpenCV?" | Código de este documento adaptado (español, `cv2`, `numpy`), con comentarios y verificaciones (`imread is None`). |
| "¿Por qué me sale este error/resultado?" | Sección 11 (errores comunes) y revisar BGR/RGB, tipos (`uint8`), tamaños, versión de OpenCV. |
| "Quiero mejorar/ampliar este proyecto" | Secciones 10 y 13 (pipelines integrados, proyectos, temas relacionados). |
| "Ayúdame a estudiar / quiz" | Ejercicios de 13.10 y ejemplos numéricos (Gauss 57.5, Canny 760, dilatación/erosión 9×9). |
| "¿Esto de la diapositiva está bien?" | Sección 11.2 (simplificaciones didácticas) y explicar la diferencia con el comportamiento real de OpenCV. |
| "Hazme un script/agent/skill sobre esto" | Mantener el pipeline y convenciones del curso (nombres en español, comentarios en español, BGR), modular: una función por etapa (`suavizar`, `detectar_bordes`, `limpiar_mascara`, `clasificar_contorno`). |

**Reglas finales:**
- Priorizar la **consistencia con el material del curso** y luego aportar profundidad.
- Explicar el **porqué** de cada parámetro (tamaño de kernel, umbrales, epsilon, sigma).
- Sugerir siempre **visualizar resultados intermedios** (gris, blur, bordes, máscara, contornos) para depurar.
- Mantener las aplicaciones en un marco **educativo, técnico y responsable**.

---
*Fin del documento.*
