---
source: "YOLO.pdf"
format: "pdf"
converted: "2026-11-10"
title: "Detección de Objetos"
lang: "es"
pages: 22
pdf_title: "Microsoft PowerPoint - 4_Yolo.pptx"
pdf_author: "Felipe"
pdf_creationDate: "D:20261110093826-05'00'"
running_text: ["footer on every slide except pages 1 and 11 (page 11 has it above the figure): Felipe Buitrago Carmona – Facultad Inteligencia Artificial e Ingenierías – Universidad de Caldas"]
images: 12
notes: ["slide deck exported to PDF; pages 3, 11, 12, 18 and 20 are almost entirely a picture and are transcribed inside the image blocks", "p.5 the text 'Ejemplo VGG16' is a large caption overlapping the lower part of the slide and the figure; placed after the figure and kept as a plain line", "p.4 the PDF text layer fused bold markup with words ('extraer características (features)de la imagen'); cleaned to normal spacing", "p.20 the figure reads 'EffidientNet' with a glitched glyph (rendered like 'Effi?entNet'); written as EfficientNet", "p.12 speed and precision cells have small icons (turtle, car, plane, rocket, targets) that only repeat the word printed under them; icons not transcribed", "p.3 YOLOv7 panel (top-left) has tiny blue labels that are illegible; transcribed as [illegible]", "p.11 the picture is cut at the bottom by the footer text; the strip of text behind the footer is not readable", "p.16 the bullet 'Adecuadas para tiempo real.' appears after the figure in the text layer; kept in reading order as a bullet of Ventajas", "p.6 figure credit absent from the slide; the images are feature maps of VGG-like layers (pool-1 ... pool-5) for 3 inputs"]
---

<!-- page:1 -->
# Detección de Objetos

<!-- page:2 -->
### YOLO (You Only Look Once): Detección de Objetos en Tiempo Real

**Definición:**

Modelo de detección de objetos que identifica y localiza múltiples objetos en una imagen mediante una única pasada por la red neuronal.

#### **Características**

- Detección en tiempo real.
- Alta velocidad de inferencia.
- Predicción simultánea de clases y ubicaciones.

<!-- page:3 -->
<image id="img-001" kind="photo" page="3">
text: "YOLOv7" | "YOLOv8" | "YOLOv6" | "YOLOv5" | "car 0.78" "car 0.67" "car 0.45" "car 0.35" | "car 0.37" "airplane 0.40" "truck 0.30" "truck 0.44" "car 0.76" "car 0.64" "car 0.46" "2" "27" "3" | "car 0.2" "car 0.37" "car 0.27" "car 0.45" "car 0.83" "car 0.70" "car 0.65" "0" | [illegible]
description: 2x2 grid of the same still frame of a multi-lane highway seen from a bridge, with a gray pole in the middle and a bridge crossing in the background; each panel has a black rounded label at the top-left naming the YOLO version (top-left YOLOv7, top-right YOLOv8, bottom-left YOLOv6, bottom-right YOLOv5). Each panel draws bounding boxes with class and confidence labels over the cars. YOLOv7 (top-left): small blue boxes with tiny unreadable labels on about 7 cars, a light car in the lower-left of the road, none on the bridge. YOLOv8 (top-right): orange boxes labeled car 0.78, car 0.67, car 0.45 (near the bridge) and car 0.35 (right lane). YOLOv6 (bottom-left): orange boxes car 0.37, car 0.76, car 0.64, car 0.46 plus a green box truck 0.30 on the right, and a large yellow box labeled airplane 0.40 around the bridge with a green truck 0.44 label inside it, plus small stray labels "2" and "27" and "3". YOLOv5 (bottom-right): orange boxes car 0.2 and car 0.37 on the left, car 0.83, car 0.70, car 0.27 and car 0.45 near the bridge, and car 0.65 on the right with a small green label "0". No other text.
</image>

<!-- page:4 -->
|**Componente**|**Definición**|**Pregunta que responde**|
|---|---|---|
|Backbone|Es la red neuronal encargada de **extraer características (features)** de la imagen.<br>Ej: VGG16|¿Qué características tiene la imagen?|
|Region Proposal|Es el mecanismo que propone: "Aquí podría haber un objeto."|¿Dónde podría haber un objeto?|
|ROI Pooling|(Región de interés)<br>Una vez encontrada una posible región con un objeto, necesitamos convertirla a un tamaño fijo.|¿Cómo estandarizo cada región?|
|Bounding Box Regression|Genera las coordenadas de la caja.<br>Ejemplo: (x, y, ancho, alto)|¿Dónde está el objeto?|
|Una/Dos etapas *|Paso 1:<br>Encontrar posibles objetos<br>Paso 2:<br>Clasificarlos|¿Lo hago en uno o dos pasos?|

<!-- page:5 -->
### Backbone

<image id="img-002" kind="diagram" page="5">
text: "conv1" "conv2" "conv3" "conv4" "conv5" | "fc6" "fc7" "fc8" | "224 × 224 × 64" "112 × 112 × 128" "56 × 56 × 256" "28 × 28 × 512" "14 × 14 × 512" "7 × 7 × 512" "1 × 1 × 4096" "1 × 1 × 1000" | "convolution+ReLU" "max pooling" "fully connected+ReLU"
description: 3D block diagram of VGG16 from left to right: a grayscale input image slab, then stacks of blue convolution+ReLU slabs that shrink in spatial size and grow in depth, separated by red max pooling slabs, ending with thin green fully connected bars. Legend at lower right: blue = convolution+ReLU, red = max pooling, green = fully connected+ReLU. An arrow points up to the last red pooling slab from the label 7 × 7 × 512.
data:
| group | slabs | output size label |
|---|---|---|
| input | grayscale image | |
| conv1 | 2 blue | 224 × 224 × 64 |
| max pooling | 1 red | |
| conv2 | 2 blue | 112 × 112 × 128 |
| max pooling | 1 red | |
| conv3 | 3 blue | 56 × 56 × 256 |
| max pooling | 1 red | |
| conv4 | 3 blue | 28 × 28 × 512 |
| max pooling | 1 red | |
| conv5 | 3 blue | 14 × 14 × 512 |
| max pooling | 1 red | 7 × 7 × 512 |
| fc6 | 1 green | 1 × 1 × 4096 |
| fc7 | 1 green | 1 × 1 × 4096 |
| fc8 | 1 green | 1 × 1 × 1000 |
</image>

Ejemplo VGG16

<!-- page:6 -->
### Backbone

- Como puedes observar, los Feature Maps suelen visualizarse como imágenes en escala de grises o con colores artificiales.
- Las zonas más claras representan valores de activación mayores.
- Las zonas oscuras representan valores de activación menores.
- Los patrones que aparecen dependen de las características que ha aprendido cada filtro.

<image id="img-003" kind="illustration" page="6">
text: "Original Image" | "layer pool-1" "layer pool-2" "layer conv-3-3" "layer pool-3" "layer conv-4-3" "layer pool-4" "layer conv-5-3" "layer pool-5" | "bird" "flower" "cat" | "last config. p = 1" "last config. p = 2" "next config. p = 1" "next config. p = 2"
description: grid of grayscale feature-map images. Left column: three original photos with captions bird (a duck-like bird on a log by a pond with pink blossoms), flower (yellow daffodils) and cat (a brown Abyssinian-type cat held by a person). To the right, for each photo, 4 rows by 8 columns of feature maps for the layers pool-1, pool-2, conv-3-3, pool-3, conv-4-3, pool-4, conv-5-3 and pool-5 (column headers at the top). Rows are labeled at the right: "last" (red italic) config. p = 1, "last" config. p = 2, "next" (green italic) config. p = 1, "next" config. p = 2. In the "last" rows the maps are dark with bright spots; in the "next" rows they are lighter with visible edges and shapes. In the layers pool-5 column the maps are a blurred bright oval in the center. Dashed horizontal lines separate the three photo groups.
</image>

<!-- page:7 -->
### Region Proposal

- Las propuestas de regiones (Region Proposals) son áreas o fragmentos de una imagen que un algoritmo considera candidatos a contener un objeto.

<!-- page:8 -->
### Region Proposal

1. Divide la imagen en regiones pequeñas.
2. Busca regiones con características visuales similares (color, textura, intensidad).
3. Agrupa regiones similares progresivamente.
4. Genera diferentes regiones candidatas de distintos tamaños.

<image id="img-004" kind="photo" page="8">
description: photo of two golden retrievers lying on grass, one on the left and one on the right, with several rectangles drawn over it: two large green rectangles (one around each dog) and several blue rectangles of different sizes (some around the dogs' bodies or heads, some on empty grass at the corners and edges), illustrating candidate regions of different sizes. No text.
</image>

<!-- page:9 -->
### ROI Pooling

1. Estandarización: convierte regiones de diferentes dimensiones en representaciones de tamaño fijo (por ejemplo, 7 × 7).
2. Reducción dimensional: aplica Max Pooling en cada subdivisión, conservando las características más relevantes y reduciendo la cantidad de información.
3. Preparación para la clasificación: genera representaciones uniformes que pueden pasar a las capas de clasificación y regresión para identificar y localizar objetos.

<image id="img-005" kind="diagram" page="9">
text: "Project proposal onto features" | "CNN" | "Max-pool within each subregion" | "Region features (here 512 x 2 x 2; In practice e.g 512 x 7 x 7)" | "Pull up for precise seeking"
description: from left to right: photo of a kitten walking on grass with a green rectangle around it; a gray trapezoid labeled CNN; a 3D grid (feature map) with a blue rectangle covering a block of cells divided in 4 colored quadrants (blue top-left, orange top-right, green bottom-left, yellow bottom-right). A curved arrow from the green rectangle over the photo to the grid is labeled "Project proposal onto features". An arrow from the grid points to a small cube with 4 matching colored quadrants, labeled "Max-pool within each subregion" above and "Region features (here 512 x 2 x 2; In practice e.g 512 x 7 x 7)" below. The text "Pull up for precise seeking" is a video overlay fragment at the bottom of the photo.
</image>

<!-- page:10 -->
### Bounding Box Regression

1. Predicción inicial: recibe una caja aproximada alrededor del objeto.
2. Cálculo de ajustes: la red neuronal predice cuánto debe desplazarse y cambiar de tamaño la caja.
3. Refinamiento: genera una nueva caja que delimita mejor el objeto.

<image id="img-006" kind="diagram" page="10">
text: "c_x" | "c_y" | "Anchor" | "e^{tw}" | "e^{th}" | "σ(t_x)" | "σ(t_y)" | "Ground truth box to predict" | "Image"
description: light-blue rectangle labeled "Image" at the bottom-left with a dotted grid. Arrows on the top and left edges are labeled c_x (horizontal) and c_y (vertical), measuring the offset of one grid cell. A thin square labeled "Anchor" sits near the center. A larger thick black rectangle, labeled "Ground truth box to predict" at its bottom-left, extends to the lower right of the anchor. A small white circle marks the center of the predicted box. Dashed lines from that center: a vertical dashed line and a horizontal dashed line crossing the thick rectangle. A short horizontal arrow labeled σ(t_x) shows the horizontal offset from the anchor's center line to the box center, and a short vertical arrow labeled σ(t_y) shows the vertical offset. A curved arrow over the top labeled e^{tw} indicates the width scale and another curved arrow at the left labeled e^{th} indicates the height scale.
</image>

<!-- page:11 -->
<image id="img-007" kind="slide-image" page="11">
## ¿CÓMO CLASIFICAN LOS MODELOS?

Evolución de la clasificación en la detección de objetos

### 1. CLASIFICACIÓN POR REGIÓN (R-CNN)

Cada región candidata se clasifica con una CNN de manera independiente.

Flow: "Imagen" → "Selective Search (~2000 regiones)" → "CNN por región" → "Clasificación". Three CNN boxes, each with a result: Perro 95%, Árbol 90%, Auto 98%, followed by "...".

Se ejecuta la CNN para cada región. **Muy lento.**

Ejemplo: image → CNN → bar chart.

| clase | probabilidad |
|---|---|
| Perro | 95% |
| Gato | 3% |
| Auto | 1% |
| ... | |

### 2. CLASIFICACIÓN COMPARTIDA (Fast R-CNN / Faster R-CNN)

La CNN se ejecuta una sola vez y las regiones comparten las características extraídas.

Flow: "Imagen" → "CNN (una sola vez)" → "Mapa de características" → "ROI Pooling (regiones)" → "Clasificación": Perro 95%, Árbol 90%, Auto 98%, "...".

La CNN se ejecuta una sola vez. **Mucho más rápido y eficiente.**

Ejemplo: image → "Feature Map" → "ROI Pooling" → bar chart.

| clase | probabilidad |
|---|---|
| Perro | 95% |
| Gato | 3% |
| Auto | 1% |
| ... | |

### 3. CLASIFICACIÓN DIRECTA (SSD / YOLO)

La red predice directamente las clases y las cajas sin regiones propuestas.

Flow: "Imagen" → "Red (una sola pasada)" → "Predicciones" (photo with boxes Perro 95% and Auto 98%).

Predice clases y cajas simultáneamente. **Muy rápido. Tiempo real.**

Ejemplo (YOLO): image with grid → "Red (YOLO)" → grid of predictions → "Celda (2,2): Perro 95%", "Celda (3,3): Auto 98%", "...".

### RESUMEN COMPARATIVO

| Tipo de clasificación | CNN POR REGIÓN | COMPARTIDA | DIRECTA |
|---|---|---|---|
| ¿Cómo funciona? | Cada región se clasifica con una CNN independiente. | La CNN se ejecuta una vez y las regiones comparten las características. | La red predice clases y cajas directamente en una sola pasada. |
| Velocidad | Muy lenta | Más rápida | Muy rápida (tiempo real) |
| Modelos | R-CNN (2014) | Fast R-CNN (2015) / Faster R-CNN (2015) | SSD (2016) / YOLO (2015 en adelante) |

**IDEA CLAVE:** A medida que evoluciona la arquitectura, se eliminan pasos intermedios (propuestas de regiones y ROI Pooling), logrando mayor velocidad sin sacrificar tanta precisión.

visual: infographic with three colored column headers (red, blue, green); in the first column a golden retriever photo cut into about 2000 small regions each fed to a CNN; in the second a photo through one CNN producing a feature-map grid and ROI-pooled crops (dog, tree, car); in the third a photo through one green box producing a photo with dashed boxes Perro 95% and Auto 98%. Small icons (speedometer, stopwatch, rocket, snail, network, lightning) decorate the summary table. The bottom of the image is cut by the slide footer text.
</image>

<!-- page:12 -->
### Versiones

<image id="img-008" kind="table-image" page="12">
| Característica | R-CNN (2014) | Fast R-CNN (2015) | Faster R-CNN (2015) | SSD (2016) | YOLOv1 (2015) | YOLOv2 (2016) | YOLOv3 (2018) | YOLOv4 (2020) | YOLOv5 (2020) | YOLOv6 (2022) | YOLOv7 (2022) | YOLOv8 (2023) | YOLOv10 (2024) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Backbone (extractor de características) | AlexNet | VGG16 | VGG16 / ResNet | VGG16 | CNN propia (24 conv + 2 FC) | Darknet-19 | Darknet-53 | CSPDarknet53 | CSPDarknet53 | Efficient RepBackbone | E-ELAN | C2f / CSP | C2f / OBB optimizado |
| Region Proposal (propuesta de regiones) | Selective Search | Selective Search | RPN (aprendido) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| ROI Pooling (Region of Interest Pooling) | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Clasificación | CNN por región | Compartida | Compartida | Directa | Directa | Directa | Directa | Directa | Directa | Directa | Directa | Directa | Directa |
| Regresión de Bounding Box | ✓ (por región) | Compartida | Compartida | Directa | Directa | Directa | Directa | Directa | Directa | Directa | Directa | Directa | Directa |
| Detección multiescala | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Una etapa / Dos etapas | Dos etapas | Dos etapas | Dos etapas | Una etapa | Una etapa | Una etapa | Una etapa | Una etapa | Una etapa | Una etapa | Una etapa | Una etapa | Una etapa |
| Velocidad (relativa) | Muy lenta | Lenta | Media | Rápida | Rápida | Muy rápida | Muy rápida | Muy rápida | Muy rápida | Muy rápida | Muy rápida | Muy rápida | Ultra rápida |
| Precisión (relativa) | Media | Media | Alta | Alta | Baja | Media | Alta | Muy alta | Muy alta | Muy alta | Muy alta | Muy alta | Muy alta |

Legend: ✓: Sí aplica / presente. ✗: No aplica / no presente. Velocidad: Muy lenta, Lenta, Media, Rápida, Muy rápida, Ultra rápida. Precisión: Baja, Media, Alta, Muy alta.

visual: dark-blue header row with an icon above each model name; speed cells carry a small icon (turtle for Muy lenta, orange turtle for Lenta, taxi for Media, plane for Rápida and Muy rápida, rocket for Ultra rápida) and precision cells carry a target icon whose color encodes the level (red Baja, yellow Media, green Alta and Muy alta). Green check marks and red crosses in the cells.
</image>

<!-- page:13 -->
# Arquitecturas de dos etapas

<!-- page:14 -->
### Arquitecturas de dos etapas

Las arquitecturas de dos etapas primero generan regiones candidatas y luego clasifican cada región.

###### **Faster R-CNN**

- Utiliza Region Proposal Network (RPN).
- Alta precisión.

###### **Mask R-CNN**

- Extiende Faster R-CNN.
- Añade segmentación de instancias.

###### **Ventajas**

- Excelente precisión.

###### **Desventajas**

- Mayor tiempo de procesamiento.

<image id="img-009" kind="diagram" page="14">
text: "1. ENTRADA" "Imagen completa" | "2. GENERACIÓN DE REGIONES CANDIDATAS" "La red propone posibles regiones con objetos." "RPN / Selective Search (propuestas de regiones)" | "3. EXTRACCIÓN DE CARACTERÍSTICAS" "Se extraen características de cada región propuesta." "CNN (compartida)" | "4. CLASIFICACIÓN" "Cada región se clasifica de forma independiente." | "5. SALIDA" "Cajas delimitadoras y clases detectadas." | "Bus 0.90" "Auto 0.08" "Peatón 0.02" "..." | "Auto 0.95" "Bus 0.03" "Peatón 0.02" "..." | "Auto 0.92" "Bus 0.05" "Peatón 0.03" "..." | "Auto 0.95" "Auto 0.92" "Bus 0.90" | "PROCESO EN DOS PASOS:" "1. Proponer regiones (dónde podría haber objetos)" "2. Clasificar cada región (qué objeto es y dónde está)" | "VENTAJAS:" "Mayor precisión" "Mejor detección de objetos pequeños" | "DESVENTAJA PRINCIPAL:" "Más lento que las arquitecturas de una etapa (hay pasos intermedios)." | "EJEMPLOS DE ARQUITECTURAS DE DOS ETAPAS:" "R-CNN (2014), Fast R-CNN (2015), Faster R-CNN (2015), entre otras."
description: infographic of five steps in a row joined by gray arrows. 1: photo of a city street with a black car on the left, a silver car in the center and a blue bus on the right. 2: the same photo with many yellow rectangles of different sizes over cars and the bus. 3: three small crops (bus, silver car, silver car) with green arrows into a green box labeled CNN (compartida). 4: a white card with three crops, each with a ranked list of class scores (first value in red, second in green, third in gray): crop of the bus Bus 0.90 / Auto 0.08 / Peatón 0.02; crop of the silver car Auto 0.95 / Bus 0.03 / Peatón 0.02; another crop of the silver car Auto 0.92 / Bus 0.05 / Peatón 0.03. 5: the photo with boxes: blue Auto 0.95 (black car), green Auto 0.92 (silver car), red Bus 0.90 (bus). Below: an orange-bordered strip "PROCESO EN DOS PASOS" with a green box 1 and a blue box 2 joined by an arrow, plus a trophy icon next to "VENTAJAS"; a dashed blue strip with a clock icon "DESVENTAJA PRINCIPAL" and a network icon "EJEMPLOS DE ARQUITECTURAS DE DOS ETAPAS".
</image>

<!-- page:15 -->
# Arquitecturas de una etapa

<!-- page:16 -->
### Arquitecturas de una etapa

Las arquitecturas de una etapa realizan la localización y clasificación en un único proceso.

##### **SSD**

- Single Shot MultiBox Detector.
- Predicción en diferentes escalas.

##### **YOLO**

- Divide la imagen en una cuadrícula.
- Predice cajas y clases simultáneamente.

##### **Ventajas**

- Alta velocidad.
- Adecuadas para tiempo real.

<image id="img-010" kind="diagram" page="16">
text: "1. ENTRADA" "Imagen completa" | "2. RED NEURONAL" "La imagen pasa una sola vez por la red." "Extracción de características" | "3. PREDICCIÓN" "La red predice clases y cajas simultáneamente para todas las regiones de la imagen." "Mapa de predicciones (en toda la imagen)" | "CLASIFICACIÓN" "Auto 0.95" "Bus 0.90" "Auto 0.88" "..." | "LOCALIZACIÓN" "(x, y, w, h)" "Confianza 0.95" "..." | "4. SALIDA" "Cajas delimitadoras y clases detectadas." | "Auto 0.95" "Auto 0.88" "Bus 0.90" | "VENTAJA PRINCIPAL:" "Al hacer todo en una sola pasada, son mucho más rápidas y adecuadas para aplicaciones en tiempo real." | "EJEMPLOS DE ARQUITECTURAS DE UNA ETAPA:" "SSD, YOLO (v1, v2, v3, v4, v5, v6, v7, v8, v10), entre otras."
description: infographic in four steps with gray arrows. 1: photo of the same city street (black car, silver car, blue bus). 2: a stack of four shrinking blue blocks (a backbone) with the label "Extracción de características". 3: a 5x4 grid ("Mapa de predicciones (en toda la imagen)") with small colored boxes and dots in some cells (blue, red, green); a brace on its right leads to two cards: CLASIFICACIÓN (Auto 0.95 in blue, Bus 0.90 in red, Auto 0.88 in green, "...") and LOCALIZACIÓN ((x, y, w, h), Confianza 0.95, "..."). 4: the photo with boxes: blue Auto 0.95 (black car), green Auto 0.88 (silver car), red Bus 0.90 (bus). Below: a green strip with a check icon and a speedometer icon, and a dashed blue strip with a lightbulb icon.
</image>

<!-- page:17 -->
# ¿Cómo funciona YOLO?

<!-- page:18 -->
<image id="img-011" kind="slide-image" page="18">
## PROCESO DE DETECCIÓN

1. **ENTRADA DE IMAGEN** — Se ingresa la imagen completa al modelo.
2. **DIVISIÓN EN CUADRÍCULA** — La imagen se divide en una cuadrícula S x S. Cada celda será responsable de predecir objetos.
3. **PREDICCIÓN DE BOUNDING BOXES** — Cada celda predice B cajas delimitadoras (Bounding Boxes) con: (x, y, w, h) y un *confidence score*.
4. **PREDICCIÓN DE CLASES** — Para cada caja, el modelo predice la probabilidad de pertenecer a cada clase.

| caja | clase 1 | clase 2 | clase 3 |
|---|---|---|---|
| perro (amarilla) | Perro: 0.92 | Gato: 0.05 | Auto: 0.01 |
| auto (azul) | Auto: 0.90 | Camión: 0.07 | Moto: 0.02 |
| bicicleta (verde) | Bicicleta: 0.95 | Moto: 0.03 | Auto: 0.01 |
| ... (rosada) | ... | | |

5. **SELECCIÓN DE DETECCIONES FINALES** — Se eliminan predicciones duplicadas y de baja confianza (NMS) y se obtienen las detecciones finales.

### CONCEPTOS CLAVE

**BOUNDING BOX:** Rectángulo que delimita un objeto.

**CONFIDENCE SCORE:** Probabilidad de que exista un objeto en la caja predicha. Escala de 0.0 ("Sin objeto") a 1.0 ("Objeto seguro"), con marcas en 0.0, 0.5 y 1.0 y un marcador en 0.92.

**RESUMEN:** El modelo observa la imagen, divide en una cuadrícula, predice cajas y clases, y selecciona las mejores detecciones.

visual: five numbered colored headers (blue, green, purple, orange, teal) joined by arrows. Step 1: photo of a street with a golden retriever sitting in the center, a red car on the right and a yellow bicycle on the left. Step 2: the same photo covered by a white grid. Step 3: the same photo with many thin colored rectangles (yellow around the dog, blue, pink, green near the bicycle and the car). Step 4: a white card with a yellow dashed crop of the dog, a blue dashed crop of the red car and a green dashed crop of the bicycle, plus a pink dashed empty slot, each with its class list (first value colored). Step 5: the photo with final boxes: yellow Perro 0.92, blue Auto 0.90, green Bicicleta 0.95. Key concepts: a dashed blue square beside a small photo of the dog with a blue box; a horizontal red-to-yellow-to-green bar for the confidence score with a black marker near 0.92 and the green number 0.92 below it; a lightbulb icon next to RESUMEN.
</image>

<!-- page:19 -->
# Arquitectura de YOLO

<!-- page:20 -->
<image id="img-012" kind="slide-image" page="20">
## ARQUITECTURA DE YOLO

- **BACKBONE** — Extrae características visuales.
- **NECK** — Combina información de diferentes escalas.
- **HEAD** — Genera las predicciones finales.

### FLUJO

Imagen → Backbone → Neck → Head → Detecciones.

- Backbone: "Ejemplo: CSPDarknet, EfficientNet".
- Neck: "Ejemplo: FPN, PAN-FPN".
- Head: "Predice: clases, cajas (x, y, w, h) y confianza para cada celda/ancla."
- Detecciones: boxes "auto 0.93", "bus 0.91", "bici 0.88".

**QUÉ DECIR:** "Las versiones modernas utilizan estructuras especializadas para detectar tanto objetos grandes como pequeños."

**EN RESUMEN:** YOLO procesa la imagen una sola vez y, mediante su arquitectura (Backbone → Neck → Head), genera predicciones eficientes en diferentes escalas.

visual: three headline boxes at the top (blue with stacked-layers icon, green with four inward arrows, purple with a cube). Flow row: a street photo (dark car in front-left, blue bus at the center-right with a cyclist at the far right, crosswalk below) → a blue dashed box with a descending stack of blue blocks (backbone) → a green dashed box with three rows of green plates linked by vertical double arrows, ending in three green grids of different density (neck, feature pyramid) → a purple dashed box with three purple 3D grids each linked to a small grid of dots (head) → the street photo with boxes: red auto 0.93, blue bus 0.91, green bici 0.88. Under "QUÉ DECIR": a grid with four framed pictures of different sizes: an elephant (red frame), a silver car (blue frame), a motorcycle (green frame) and a small dog (purple frame). A lightbulb and a target with a speedometer icon decorate the boxes.
</image>

<!-- page:21 -->
# Desafíos en detección de objetos

<!-- page:22 -->
### Desafíos en detección de objetos

- Objetos pequeños
- Oclusiones.
- Variaciones de iluminación
- Diferentes escalas
- Fondos complejos
- Tiempo real.
