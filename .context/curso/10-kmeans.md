# K-Means — clustering y segmentación de imágenes por color

> **Fuentes:** `material-clase/18-K-MEANS-Basico.pdf.md` (diapositivas, Felipe Buitrago Carmona) y `material-clase/4_Kmeans_Imagenes.ipynb` (notebook de Colab).
> **Etiquetas:** `[CURSO]` = aparece en clase · `[AMPLIACIÓN]` = añadido para dar contexto · `[NOTA]` = precisión sobre las diapositivas.
> **Posición en el curso:** último tema del **primer corte** (cerrado). Sigue a morfología y detección de figuras; ver `corte-1.md`.

## 1. Idea `[CURSO]`

- Agrupa elementos **similares**; sirve con datos **no etiquetados**.
- Algoritmo de aprendizaje automático **no supervisado**.
- Vocabulario:
  - **Observación**: un elemento del conjunto de datos (en imágenes: un píxel).
  - **Centroide**: elemento central en el espacio n-dimensional de los n atributos.
  - **Clúster**: conjunto de observaciones parecidas; la similitud se mide con una distancia.
- Objetivo: **minimizar la variación intra-clúster** y **maximizar la variación extra-clúster**.

## 2. Distancia (Fórmula 1) `[CURSO]`

Distancia euclidiana entre observaciones `x_i` y `x_j` en `p` dimensiones:

```
d(x_i, x_j) = sqrt( sum_{k=1..p} (x_ik - x_jk)^2 )
```

En una imagen a color, `p = 3` (los tres canales del píxel).

## 3. Algoritmo (6 pasos) `[CURSO]`

1. Elegir `k` = número de clústeres.
2. Elegir los `k` centroides iniciales.
3. Medir la distancia de cada observación a los `k` centroides (Fórmula 1).
4. Asignar cada observación al centroide **más cercano**.
5. Por cada grupo, **actualizar el centroide** = dato medio del grupo.
6. Repetir 3, 4 y 5 hasta que **no cambien los centroides** (o se alcance un máximo de iteraciones).

### Ejemplo manual de la diapositiva (1-D, k = 3)

17 tarjetas numéricas, centroides iniciales **3, 2, 1**. Distancia de la observación 8: `|8-3|=5`, `|8-2|=6`, `|8-1|=7` → va al centroide 3. Repetir por cada observación. Tras asignar todo:

| Clúster | Centroide | Miembros |
|---|---|---|
| Amarillo | 3 | 8, 11, 13, 10, 13, 5, 4, 12, 6, 6, 13, 10 |
| Rojo | 2 | 2 |
| Verde | 1 | 1 |

Actualización del centroide amarillo: `(8+11+13+10+13+5+4+12+6+6+13+10+3) / 13 = 114/13 ≈ 8.77`. Iteraciones siguientes (centroides amarillo/rojo/verde): `8/2/1` → `10/3/1` → `11/4/1` → `11/6/2`.

`[NOTA]` En la diapositiva el centroide nuevo se "ajusta" a una tarjeta existente (8.7 → tarjeta 8). K-Means real **no** hace eso: el centroide es el promedio exacto (8.77) y no tiene por qué coincidir con ninguna observación.
`[NOTA]` Colores de las tarjetas ≠ clúster: el color de la tarjeta es solo su identidad visual; el clúster lo define el rectángulo donde está.

## 4. K-Means sobre imágenes `[CURSO]` (notebook `4_Kmeans_Imagenes.ipynb`)

Cada **píxel** es una observación con 3 atributos (R, G, B). Se agrupan los colores y cada píxel se reemplaza por el color de su centroide → imagen **cuantizada a K colores** (segmentación por color).

Pasos del notebook:

1. Cargar la imagen (`cv2.imread`, verificar `None`).
2. `BGR → RGB` para mostrar con matplotlib.
3. Dimensiones `alto, ancho, canales = imagen.shape`.
4. **Tabla de píxeles**: `pixeles = imagen_rgb.reshape((-1, 3)).astype(np.float32)` → forma `(alto·ancho, 3)`.
5. `K = 3`; `modelo = KMeans(n_clusters=K, random_state=42, n_init=10)`; `etiquetas = modelo.fit_predict(pixeles)`.
6. `centroides = modelo.cluster_centers_` → `colores = np.uint8(centroides)`.
7. `pixeles_segmentados = colores[etiquetas]` (indexación avanzada: cada etiqueta elige su color).
8. `imagen_segmentada = pixeles_segmentados.reshape(imagen_rgb.shape)`.
9. Mostrar original vs segmentada con `plt.subplots(1, 2)`.

```python
import cv2
import numpy as np
from sklearn.cluster import KMeans

imagen = cv2.imread("foto.jpg")
if imagen is None:
    raise ValueError("No fue posible leer la imagen")

pixeles = imagen.reshape((-1, 3)).astype(np.float32)   # (N, 3)
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
etiquetas = modelo.fit_predict(pixeles)
colores = np.uint8(modelo.cluster_centers_)
segmentada = colores[etiquetas].reshape(imagen.shape)  # sigue en BGR si se leyó con imread
```

`[NOTA]` El notebook original corre en **Google Colab** (`from google.colab import files`, `files.upload()`) y usa **scikit-learn**. En local hay que cambiar la carga por `cv2.imread(ruta)` y tener `scikit-learn` instalado (hoy **no** está en `requirements.txt`; ver `state/known-issues.md`).

## 5. Alternativa solo con OpenCV `[AMPLIACIÓN]`

```python
criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
_, etiquetas, centros = cv2.kmeans(pixeles, 3, None, criterio, 10, cv2.KMEANS_PP_CENTERS)
segmentada = np.uint8(centros)[etiquetas.flatten()].reshape(imagen.shape)
```

No requiere scikit-learn; entrada `float32` de forma `(N, 3)`.

## 6. Cosas que conviene saber `[AMPLIACIÓN]`

- **Elegir K**: método del codo (inercia vs K) o silueta; no hay K "correcto" universal.
- **Inicialización**: el resultado depende de los centroides iniciales → `n_init`, `random_state`, `k-means++` (`KMEANS_PP_CENTERS`).
- **Espacio de color**: en BGR la distancia no es perceptual; agrupar en **CIELAB** (tema 3.4–3.5 del temario) suele dar clústeres más fieles a lo que ve el ojo. Para segmentar por color también se puede hacer en HSV.
- **Costo**: cada píxel es una observación; en fotos grandes reducir con `cv2.resize` antes.
- **Sensible a outliers y a la escala** de los atributos; asume clústeres compactos/convexos.
- **Usos en visión**: cuantización/paleta de colores, segmentación simple, separar fondo/objeto, preprocesar antes de contornos (tema 9).

## 7. Conexión con el resto del curso

K-Means usa lo visto antes (imagen como arreglo → `reshape`, BGR/RGB, espacios de color) y sirve de puente al segundo corte: pasa de reglas fijas escritas a mano (umbrales, `inRange`) a **aprender estructura de los datos**. El siguiente paso lógico es aprendizaje supervisado con CNN (`11-cnn.md`).
