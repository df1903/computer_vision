---
source: "2_CNNs.pdf"
format: "pdf"
converted: "2026-10-13"
title: "Redes Neuronales Convolucionales CNN"
lang: "es"
pages: 60
pdf_title: "Microsoft PowerPoint - 2_0_CNNs.pptx"
pdf_author: "Felipe"
pdf_creationDate: "D:20260530155045-05'00'"
running_text: ["footer on every slide: Felipe Buitrago Carmona – Facultad Inteligencia Artificial e Ingenierías – Universidad de Caldas", "slide number printed bottom-left in green on most slides (the number equals the page number): 2 3 4 5 6 7 10 12 13 14 15 16 17 18 19 20 21 23 24 25 26 27 28 29 31 32 34 35 37 38 39 40 41 42 43 44 46 47 48 49 50 51 52 53 54 55 56 57 58"]
images: 60
notes: ["every page is a slide exported as one picture of the whole slide (leaf and circle decorations in green/grey are decorative and not described); text that is also in the text layer is given in the page body, text that only exists inside pictures is in the image blocks", "slides are pages 1-60; slide numbers 1, 9, 11, 22, 30, 33, 36, 45 are not printed on the slide", "p.10, p.13, p.47, p.49: the grid of small numbers (What the computer sees) is partially covered by overlay lines/arrows and too small to read completely; only legible parts are transcribed", "p.14 and p.24 are embedded videos shown as a still frame; only the still frame is described", "p.31 the derivative printed for the sigmoid has a minus sign in the numerator, kept verbatim and marked [sic]", "p.34, p.32, p.35 average pooling output shows 20 for the window 37,4,25,12 (mean 19.5), kept as printed", "p.50 unpacks three values from cargarDatos, p.51 defines cargarDatos returning two values; kept verbatim", "p.50 and p.60 code strings and p.51 variable names are kept exactly as written (e.g. num_chanels, limiteImagenesEntrenamiento)", "URL in footnotes of several slides is broken across two lines in the slide (image- / classification/...); written here with the hyphen as displayed", "p.39, p.40, p.43 the source credit text overlaps the footer text in the slide; both are given separately", "p.42 slide is titled Estructura- Capas Ocultas but the red box highlights the output layer; kept as shown"]
---

<!-- page:1 -->
# Redes Neuronales Convolucionales CNN

<image id="img-001" kind="slide-image" page="1">
text: "Redes Neuronales Convolucionales" | "CNN" | "Felipe Buitrago Carmona – Facultad Inteligencia Artificial e Ingenierías – Universidad de Caldas" | "Centro de Investigación, Innovación, Desarrollo y Transferencia de Tecnología" | "CIDT2"
visual: cover slide; photo of green terraced fields inside leaf-shaped crops; logo of the research center (tree with circuit-board branches, text CiDT²) at bottom-left.
</image>

<!-- page:2 -->
## Supervisado

Ej: Detección mascotas

Dot CSV. Source https://www.youtube.com/watch?v=oT3arRRB2Cw

<image id="img-002" kind="slide-image" page="2">
text: "X" "14%" "Y" "GATO" | "X" "20%" "Y" "PERRO"
visual: two rows. Row 1: photo of a kitten, arrows to a purple-pink square (axes X and Y, label 14%), then a blue box GATO. Row 2: photo of a beagle puppy on grass, arrows to a purple-pink square (X, 20%, Y), then an orange box PERRO.
</image>

<!-- page:3 -->
## Supervisado

Dot CSV. Source https://www.youtube.com/watch?v=oT3arRRB2Cw

<image id="img-003" kind="slide-image" page="3">
text: "X" "94%" "Y" "GATO"
visual: photo of a tabby cat face, arrow to a purple-pink square (X, 94%, Y), then a blue box GATO.
</image>

<!-- page:4 -->
## Observación

Source: https://www.youtube.com/watch?v=40riCqvRoMs

<image id="img-004" kind="photo" page="4">
description: photo of a smiling dark-haired toddler in an orange T-shirt (printed animals and the word "Sydney" partly visible) sitting in a high chair at a table outdoors, arm raised; a cake and an orange bowl are on the table, green garden in the background. No other text.
</image>

<!-- page:5 -->
## Observación

Source: https://www.youtube.com/watch?v=40riCqvRoMs

<image id="img-005" kind="photo" page="5">
text: "Leo" | "Standing On" | "Ecstatic" | "High Chair" | "Cake"
description: same photo as page 4 darkened, with yellow bounding boxes: one on the child's face labeled "Leo", one on the chair, one on the cake; arrows from the "Leo" box to the chair box (label "Standing On") and to the cake box (label "Ecstatic").
</image>

<!-- page:6 -->
## Procesamiento de imágenes en el cerebro

The Visual Pathway. Source: https://commons.wikimedia.org/wiki/File:Human_visual_pathway.svg

<image id="img-006" kind="diagram" page="6">
text: "Left visual field" | "Right visual field" | "Nasal retina" | "Temporal retina" | "Optical lens" | "Temporal retina" | "Eye" | "Optic nerve" | "Optic chiasm" | "Lateral geniculate nucleus (LGN)" | "Primary visual cortex"
description: top view of a brain with both eyes; the left and right visual fields (red and cyan bars) project through the lenses onto the retinas; red and cyan fibers go along the optic nerves, cross at the optic chiasm, reach the lateral geniculate nucleus on each side and continue to the primary visual cortex at the back of the brain. "Primary visual cortex" is underlined in dark red.
</image>

<!-- page:7 -->
## Ejemplo Predicción

<image id="img-007" kind="photo" page="7">
description: close-up photo of a tiger's face, frontal view. No text.
</image>

<!-- page:8 -->
## Entrenamiento

El cerebro ha tardado 500 millones de años para desarrollar esta habilidad

<image id="img-008" kind="photo" page="8">
description: 3 rows by 5 columns collage of felines, face photos: row 1 puma, lion, tiger, jaguar, clouded leopard; row 2 leopard, lynx, cheetah, white tiger, snow leopard (dark grey); row 3 black panther, ocelot, white lion yawning, jaguar, white tiger. No text.
</image>

<!-- page:9 -->
## Definición

Una red neuronal convolucional (Convolutional Neural Network CNN) es una clase de redes neuronales artificiales que utiliza capas convolucionales para filtrar entradas y obtener información útil.

Tiene diversas aplicaciones tales como:

- Reconocimiento y clasificación de imágenes,
- Análisis de texto y video
- Reconocimiento de voz
- Clasificación de texto entre otros.

(NVIDIA DEVELOPER,2018)

<image id="img-009" kind="slide-image" page="9">
visual: all text of the slide is the body above; decorative leaves only.
</image>

<!-- page:10 -->
## Representación de Imágenes

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks

<image id="img-010" kind="photo" page="10">
text: "What the computer sees"
description: photo of a grey British shorthair cat sitting among bare branches; a small square on its face is connected by two black lines to a large grid of two-digit numbers (0–99) captioned "What the computer sees". The first row of the grid begins "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91"; the rest of the grid is too small to transcribe reliably.
</image>

<!-- page:11 -->
## Ejercicio de clase

<image id="img-011" kind="slide-image" page="11">
text: "Ejercicio de clase"
visual: section divider with leaf graphics.
</image>

<!-- page:12 -->
<image id="img-012" kind="illustration" page="12">
text: "1 2 3 4 5" | "6 7 8 9 0" | "22"
description: ten hand-drawn black brush-stroke digits on white, two rows: 1 2 3 4 5 and 6 7 8 9 0; a small green "22" at the bottom-left of the embedded image.
</image>

<!-- page:13 -->
<image id="img-013" kind="photo" page="13">
description: grid of handwritten digits (MNIST-style samples), 10 rows by 15 columns; row r contains 15 different handwriting samples of the digit r−1, from 0 in the first row to 9 in the last row. No text.
</image>

<!-- page:14 -->
<image id="img-014" kind="screenshot" page="14">
text: "www.cybercontrols.org"
description: black video frame (embedded video not played); only the faint watermark www.cybercontrols.org at the bottom-right.
</image>

<!-- page:15 -->
## Estructura

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks

<image id="img-015" kind="diagram" page="15">
text: "input layer" | "hidden layer 1" | "hidden layer 2" | "output layer"
description: fully connected neural network diagram: input layer (red background) with 3 neurons, hidden layer 1 (blue) with 4 neurons, hidden layer 2 (blue) with 4 neurons, output layer (green) with 1 neuron; every neuron connected to all neurons of the next layer.
</image>

<!-- page:16 -->
## Estructura

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks

<image id="img-016" kind="diagram" page="16">
text: "input layer" | "hidden layer 1" | "hidden layer 2" | "output layer"
description: same network as page 15 with a red rectangle highlighting the input layer.
</image>

<!-- page:17 -->
## Estructura- Capa Entrada

<image id="img-017" kind="diagram" page="17">
text: "7" | "What the computer sees" | "08" | "…" | "input layer"
description: a 28x28-style image of a handwritten 7 is connected by two black lines to a grid of two-digit numbers (What the computer sees). A red circle marks the first cell (value 08, top-left) and a red arrow goes to the first neuron of the input layer, labeled 08. The input layer shows three circles with "…" between the second and third; the first holds 08.
</image>

<!-- page:18 -->
## Estructura- Capa Entrada

<image id="img-018" kind="diagram" page="18">
text: "7" | "What the computer sees" | "08" | "02" | "…" | "input layer"
description: same as page 17; the red circle is now on the second cell of the first row (02) and a red arrow goes to the second input neuron, labeled 02; the first neuron still shows 08.
</image>

<!-- page:19 -->
## Estructura- Capa Entrada

<image id="img-019" kind="diagram" page="19">
text: "7" | "What the computer sees" | "08" | "02" | "…" | "48" | "input layer"
description: same as page 17; the red circle is now on the last cell (bottom-right, value 48) and a red arrow goes to the last input neuron, labeled 48; the first two neurons show 08 and 02.
</image>

<!-- page:20 -->
## Estructura- Capas Ocultas

Extracción de características

Operaciones:

1. Convoluciones
2. Funciones de activación
3. Pooling
4. Aplanamientos

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neu

<image id="img-020" kind="diagram" page="20">
text: "input layer" | "hidden layer 1" | "hidden layer 2" | "output layer"
description: same network as page 15 with a red rectangle around the two hidden layers.
</image>

<!-- page:21 -->
<image id="img-021" kind="diagram" page="21">
text: "Input Image (28x28 pixels)" | "Convolutional Layer 1" | "Filter-Weights (5x5 pixels)" | "(14x14 pixels)" | "(16 channels)" | "Convolutional Layer 2" | "Filter-Weights (5x5 pixels)" | "16 of these ..." | "(7x7 pixels)" | "(36 channels)" | "Fully-Connected Layer" | "(128 features)" | "Output Layer" | "(10 features)" | "Class" | "0 1 2 3 4 5 6 7 8 9" | output values "0.0" "0.0" "0.1" "0.0" "0.0" "0.1" "0.0" "0.8" "0.0" "0.0" | circled class "7"
description: CNN architecture for digit recognition. Input: image of a handwritten 7 (28x28). Convolutional layer 1: a 4x4 grid of 16 red/blue 5x5 filter weights, producing 16 channels of 14x14 images (4x4 grid of 7s). Convolutional layer 2: 16 groups of 6 filter-weight tiles (5x5), producing 36 channels of 7x7 images (6x6 grid). Fully-connected layer: a vertical column of 128 features. Output layer: 10 values, one per class 0–9; the value 0.8 is for class 7, which is circled; 0.1 for classes 2 and 5; the rest 0.0. Two orange vertical bars mark the input boundary and the output layer.
</image>

<!-- page:22 -->
## 1.Convolución

<image id="img-022" kind="slide-image" page="22">
text: "1.Convolución"
visual: section divider with leaf graphics.
</image>

<!-- page:23 -->
## Estructura- Capas Ocultas Convolución

Desliza filtros sobre la imagen original para realzar características

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks

<image id="img-023" kind="diagram" page="23">
text: "Input Feature Map" | "Convolutional Filter"
data:
Input Feature Map (5x5):
| | | | | |
|---|---|---|---|---|
| 3 | 5 | 2 | 8 | 1 |
| 9 | 7 | 5 | 4 | 3 |
| 2 | 0 | 6 | 1 | 6 |
| 6 | 3 | 7 | 9 | 2 |
| 1 | 4 | 9 | 5 | 1 |
Convolutional Filter (3x3, red):
| | | |
|---|---|---|
| 1 | 0 | 0 |
| 1 | 1 | 0 |
| 0 | 0 | 1 |
</image>

<!-- page:24 -->
<image id="img-024" kind="screenshot" page="24">
text: "A" | "C D E"
description: dark video frame (embedded video of a CNN visualization): a pixel grid of the white letter A on blue, drawn in perspective over a dark panel, with small letters "C D E" and small colored bars at its right, and a mouse pointer below it. Mostly black background.
</image>

<!-- page:25 -->
## Estructura- Capas Ocultas Convolución

Desliza filtros sobre la imagen original para realzar características

<image id="img-025" kind="diagram" page="25">
text: "Original" | "Gaussian Blur" | "Sharpen" | "Edge Detection"
data:
| filtro | kernel |
|---|---|
| Original | [[0,0,0],[0,1,0],[0,0,0]] |
| Gaussian Blur | 1/16 · [[1,2,1],[2,4,2],[1,2,1]] |
| Sharpen | [[0,−1,0],[−1,5,−1],[0,−1,0]] |
| Edge Detection | [[−1,−1,−1],[−1,8,−1],[−1,−1,−1]] |
description: table with 4 columns, each with the kernel matrix and below it the result applied to the same photo of a small brown animal head (a chevrotain-like animal): original, blurred, sharpened (more contrast), and edge detection (black image with white outlines).
</image>

<!-- page:26 -->
## Estructura- Capas Ocultas Convolución

Desliza filtros sobre la imagen original para realzar características

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks

<image id="img-026" kind="diagram" page="26">
text: "Input Feature Map" | "3×1" "5×0" "2×0" "9×1" "7×1" "5×0" "2×0" "0×0" "6×1" | "3+0+0+9+7+0+0+0+6" | "Output Feature Map"
data:
Input Feature Map, top-left 3x3 window highlighted in red with the filter value as multiplier:
| | | | | |
|---|---|---|---|---|
| 3×1 | 5×0 | 2×0 | 8 | 1 |
| 9×1 | 7×1 | 5×0 | 4 | 3 |
| 2×0 | 0×0 | 6×1 | 1 | 6 |
| 6 | 3 | 7 | 9 | 2 |
| 1 | 4 | 9 | 5 | 1 |
Output Feature Map (3x3, yellow; first cell 25 outlined in red):
| | | |
|---|---|---|
| 25 | 18 | 17 |
| 18 | 22 | 14 |
| 20 | 15 | 23 |
description: arrow from the highlighted window to the output cell 25 labeled with the sum 3+0+0+9+7+0+0+0+6.
</image>

<!-- page:27 -->
## Estructura- Capas Ocultas Convolución

Desliza filtros sobre la imagen original para realzar características

Apsl, https://www.apsl.net/blog/2018/02/02/tensor-flow-para-principiantes-vi-uso-de-la-api-keras/

<image id="img-027" kind="diagram" page="27">
text: "Convolutional Layer 1" | "Filter-Weights (5x5 pixels)" | "(14x14 pixels)" | "(16 channels)"
description: zoom of layer 1 of page 21: a 4x4 grid of 16 red/blue filter-weight tiles on the left, and to the right a 4x4 grid of 16 small images of the digit 7 (the 16 channels, 14x14 pixels).
</image>

<!-- page:28 -->
## Estructura- Capas Ocultas Convolución

Desliza filtros sobre la imagen original para realzar características

Apsl, https://www.apsl.net/blog/2018/02/02/tensor-flow-para-principiantes-vi-uso-de-la-api-keras/

<image id="img-028" kind="diagram" page="28">
text: "Convolutional Layer 2" | "Filter-Weights (5x5 pixels)" | "16 of these ..." | "(7x7 pixels)" | "(36 channels)"
description: zoom of layer 2 of page 21: two blocks of 6x6 red/blue filter-weight tiles labeled "16 of these ...", and to the right a 6x6 grid of 36 small images (36 channels, 7x7 pixels); an arrow enters from the left and leaves to the right.
</image>

<!-- page:29 -->
<image id="img-029" kind="formula" page="29">
text: "Wf=Ancho final" | "Hf=Altura final" | "f= Ancho o Altura del filtro" | "s= stride"
data:
$$w_f = \frac{w_i - f}{s} + 1$$
$$h_f = \frac{h_i - f}{s} + 1$$
</image>

<!-- page:30 -->
## 2.Funciones de Activación

<image id="img-030" kind="slide-image" page="30">
text: "2.Funciones de Activación"
visual: section divider with leaf graphics.
</image>

<!-- page:31 -->
## Estructura- Capas Ocultas ReLu-Funcion de Activación

Tiene como fin introducir la no linealidad en el modelo

<image id="img-031" kind="diagram" page="31">
text: "Escalón" | "Escalón simétrico" | "Sigmoidal" | "Tang. Hiperbólica"
data:
| función | fórmula | rango del eje y |
|---|---|---|
| Escalón | f(x)=0 si x<0; f(x)=1 si x≥0 | 0 a 1 |
| Escalón simétrico | f(x)=−1 si x<0; f(x)= 1 si x≥0 | −1 a 1 |
| Sigmoidal | f(x) = 1/(1+e^−x); f'(x) = −e^−x/(1+e^−x)^2 [sic] = y(1−y) (boxed) | 0 a 1 |
| Tang. Hiperbólica | f(x) = (e^x−e^−x)/(e^x+e^−x) | −1 a 1 |
description: four small plots with axes x and y: a step from 0 to 1 at x=0; a step from −1 to 1 at x=0; a smooth S-shaped curve between 0 and 1; a smooth S-shaped curve between −1 and 1. The slide title mentions ReLu but no ReLU function is plotted.
</image>

<!-- page:32 -->
<image id="img-032" kind="slide-image" page="32">
text: "Convolución" | "Pasar filtros sobre la imagen y realzar detalles (Puede reducir la imagen)" | "Pooling" | "Reducción de las imágenes obteniendo características mas relevantes" | "max pooling" | "average pooling" | "model.add(Conv2D(kernel_size=5, strides=1, filters=16, padding='same',activation='relu', name='layer_conv1'))"
data:
Convolución: same kernel table as page 25 (Original, Gaussian Blur, Sharpen, Edge Detection).
Pooling, input 4x4 (2x2 windows colored red, yellow, blue, green):
| | | | |
|---|---|---|---|
| 12 | 20 | 30 | 0 |
| 8 | 12 | 2 | 0 |
| 34 | 70 | 37 | 4 |
| 112 | 100 | 25 | 12 |
max pooling output: | 20 | 30 | / | 112 | 37 |
average pooling output: | 13 | 8 | / | 79 | 20 |
visual: the last code line is highlighted with a red rectangle. The first line of the code block above it is partly cut: "# Primera capa convolucional con ReLU-activation y max-pooling."
</image>

<!-- page:33 -->
## 3.Pooling

<image id="img-033" kind="slide-image" page="33">
text: "3.Pooling"
visual: section divider with leaf graphics.
</image>

<!-- page:34 -->
## Estructura- Capas Ocultas Pooling

Reduce la matriz convolucionada para la siguiente capa

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks

<image id="img-034" kind="diagram" page="34">
text: "max pooling" | "average pooling"
data:
Input 4x4 with 2x2 windows in red, yellow, blue, green:
| | | | |
|---|---|---|---|
| 12 | 20 | 30 | 0 |
| 8 | 12 | 2 | 0 |
| 34 | 70 | 37 | 4 |
| 112 | 100 | 25 | 12 |
max pooling output (2x2): 20, 30 / 112, 37
average pooling output (2x2): 13, 8 / 79, 20
</image>

<!-- page:35 -->
<image id="img-035" kind="slide-image" page="35">
text: "Convolución" | "Pasar filtros sobre la imagen y realzar detalles (Puede reducir la imagen)" | "Pooling" | "Reducción de las imágenes obteniendo características mas relevantes" | "max pooling" | "average pooling"
data:
Same kernel table (Original, Gaussian Blur, Sharpen, Edge Detection) and same pooling example as page 32 (max pooling 20 30 / 112 37; average pooling 13 8 / 79 20).
code:
```python
# Primera capa convolucional con ReLU-activation y max-pooling.
model.add(Conv2D(kernel_size=5, strides=1, filters=16, padding='same',activation='relu', name='layer_conv1'))
model.add(MaxPooling2D(pool_size=2, strides=2))
# Segunda capa convolucional con ReLU-activation y max-pooling.
#padding = same --> imagen de salida mismo tamaño de la entrada
model.add(Conv2D(kernel_size=5, strides=1, filters=36, padding='same',activation='relu', name='layer_conv2'))
model.add(MaxPooling2D(pool_size=2, strides=2))
```
visual: the two MaxPooling2D lines are highlighted with red rectangles.
</image>

<!-- page:36 -->
## Aplanamiento

<image id="img-036" kind="slide-image" page="36">
text: "Aplanamiento"
visual: section divider with leaf graphics.
</image>

<!-- page:37 -->
## Aplanamiento

<image id="img-037" kind="diagram" page="37">
text: "input" "conv1" "pool1" "conv2" "pool2" "hidden4" "output" | "Convolution" | "Subsample" | "Convolution" | "Subsample" | "Full connection" | "Convolution"
description: CNN diagram: a large square input image, then a stack of 6 feature maps (conv1) obtained by "Convolution", a stack of smaller maps (pool1) by "Subsample", a stack of 12 maps (conv2) by "Convolution", smaller maps (pool2) by "Subsample", then a column of long thin bars (hidden4) and a final bar (output) joined by "Full connection". A red rotated rectangle highlights the flattened layers between pool2 and output.
</image>

<!-- page:38 -->
## Aplanamiento

<image id="img-038" kind="diagram" page="38">
text: "M"
data:
Matrix M (4x4), cell label M_{column,row}:
| | | | |
|---|---|---|---|
| M0,0 | M1,0 | M2,0 | M3,0 |
| M0,1 | M1,1 | M2,1 | M3,1 |
| M0,2 | M1,2 | M2,2 | M3,2 |
| M0,3 | M1,3 | M2,3 | M3,3 |
Flattened vector M (16 cells, row after row): M0,0 M1,0 M2,0 M3,0 M0,1 M1,1 M2,1 M3,1 M0,2 M1,2 M2,2 M3,2 M0,3 M1,3 M2,3 M3,3
description: a down arrow from the matrix to the long horizontal vector; each matrix row has its own gray shade, kept in the vector.
</image>

<!-- page:39 -->
## Estructura- Capas Ocultas Directamente conectadas

Apsl, https://www.apsl.net/blog/2018/02/02/tensor-flow-para-principiantes-vi-uso-de-la-api-keras/

<image id="img-039" kind="diagram" page="39">
text: same diagram text as page 21
description: same CNN architecture as page 21 with a red rectangle around the Fully-Connected Layer (128 features).
</image>

<!-- page:40 -->
## Estructura- Capas Ocultas Directamente conectadas

Realiza la clasificación basado en las características obtenidas de las convoluciones. Estas por lo general tienen una función de **activación softmax** la cual brinda un valor de probabilidad de 0 a 1 por cada una de las salidas.

Apsl, https://www.apsl.net/blog/2018/02/02/tensor-flow-para-principiantes-vi-uso-de-la-api-keras/

<image id="img-040" kind="diagram" page="40">
text: same diagram text as page 21
description: same as page 39: CNN architecture with a red rectangle around the Fully-Connected Layer.
</image>

<!-- page:41 -->
<image id="img-041" kind="screenshot" page="41">
code:
```python
#Aplanar imagen
model.add(Flatten())
#Capa densa
model.add(Dense(128,activation='relu'))
```
description: screenshot of code in an editor; the first line is highlighted in light yellow with a text cursor after "imagen".
</image>

<!-- page:42 -->
## Estructura- Capas Ocultas

Extracción de características

Operaciones:

1. Convoluciones
2. Pooling
3. Funciones de activación

Google Developers, https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks

<image id="img-042" kind="diagram" page="42">
text: "input layer" | "hidden layer 1" | "hidden layer 2" | "output layer"
description: same network as page 15 with a red rectangle around the output layer.
</image>

<!-- page:43 -->
## Estructura- Capa de Salida

Según el número de etiquetas de salida, proporciona un valor entre 0 y 1. Aquella que posea el valor mas alto, será la clasificación final

Apsl, https://www.apsl.net/blog/2018/02/02/tensor-flow-para-principiantes-vi-uso-de-la-api-keras/

<image id="img-043" kind="diagram" page="43">
text: same diagram text as page 21
description: same CNN architecture as page 21 with a red rectangle around the Output Layer and the Class column (values 0.0 0.0 0.1 0.0 0.0 0.1 0.0 0.8 0.0 0.0, class 7 circled).
</image>

<!-- page:44 -->
<image id="img-044" kind="screenshot" page="44">
code:
```python
#Capa salida
model.add(Dense(num_clases,activation='softmax'))
```
</image>

<!-- page:45 -->
## Práctica

<image id="img-045" kind="slide-image" page="45">
text: "Práctica"
visual: section divider with leaf graphics.
</image>

<!-- page:46 -->
<image id="img-046" kind="illustration" page="46">
text: "1 2 3 4 5" | "6 7 8 9 0"
description: enlarged version of the hand-drawn brush-stroke digits of page 12 (1 2 3 4 5 in the first row, 6 7 8 9 0 in the second).
</image>

<!-- page:47 -->
<image id="img-047" kind="photo" page="47">
description: same MNIST-style grid of handwritten digits as page 13 (10 rows by 15 columns, row r holds samples of the digit r−1, 0 to 9). No text.
</image>

<!-- page:48 -->
<image id="img-048" kind="diagram" page="48">
text: same diagram text as page 21
description: same CNN architecture as page 21, without highlights (input image 28x28 of a 7, two convolutional layers, fully-connected layer, output layer with 0.8 for class 7).
</image>

<!-- page:49 -->
<image id="img-049" kind="photo" page="49">
text: "What the computer sees"
description: handwritten 7 connected by two black lines to the grid of two-digit numbers captioned "What the computer sees" (same as page 17, without red marks); the numbers are too small to transcribe completely.
</image>

<!-- page:50 -->
```python
width=28
height=28
#Numero de neuronas de la cnn
img_size_flat=width*height
#Parametrizar la forma de imagenes
num_chanels=1
#RGB, HSV -> num_chanels=3
img_shape=(width,height,num_chanels)
num_clases=10
limiteImagenesEntrenamiento=[60,60,60,60,60,60,60,60,60,60]
imagenes,etiquetas,probabilidades=cargarDatos("dataset/train/",num_clases,limiteImagenesEntrenamiento,width,height)
```

<image id="img-050" kind="screenshot" page="50">
visual: code slide; the text is the code block above. In the original, comments are in gray italics, numbers in blue and the string "dataset/train/" in bold teal.
</image>

<!-- page:51 -->
```python
def cargarDatos(fase,numeroCategorias,limite,width,height):
    imagenesCargadas=[]
    etiquetas=[]
    valorEsperado=[]
    for categoria in range(0,numeroCategorias):
        for idImagen in range(0,limite[categoria]):
            ruta=fase+str(categoria)+"/"+str(categoria)+"_"+str(idImagen)+".jpg"
            print(ruta)
            imagen=cv2.imread(ruta)
            imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (width,height))
            imagen=imagen.flatten()
            imagen=imagen/255
            imagenesCargadas.append(imagen)
            probabilidades=np.zeros(numeroCategorias)
            probabilidades[categoria]=1
            valorEsperado.append(probabilidades)
    imagenesEntrenamiento=np.array(imagenesCargadas)
    valoresEsperados=np.array(valorEsperado)
    return imagenesEntrenamiento,valoresEsperados
```

<image id="img-051" kind="screenshot" page="51">
visual: code slide; the text is the code block above. Indentation reconstructed from the slide: the two for loops are nested and the three lines from imagenesEntrenamiento to return are at function level.
</image>

<!-- page:52 -->
<image id="img-052" kind="screenshot" page="52">
text: "Este equipo" | "Disco local (C:)" | "Usuarios" | "FBC" | "Dropbox" | "Vision Artificial" | "cnnSemillero" | "reconocimientoDigitos" | "dataset" | "Nombre" | "Fecha de modifica..." | "Tipo" | "Tamaño" | "Carpeta de archivos"
data:
Windows Explorer, path: Este equipo > Disco local (C:) > Usuarios > FBC > Dropbox > Vision Artificial > cnnSemillero > reconocimientoDigitos > dataset
| Nombre | Fecha de modifica... | Tipo |
|---|---|---|
| 0 | 26/03/2019 9:52 a.... | Carpeta de archivos |
| 1 | 26/03/2019 9:53 a.... | Carpeta de archivos |
| 2 | 26/03/2019 9:53 a.... | Carpeta de archivos |
| 3 | 26/03/2019 9:54 a.... | Carpeta de archivos |
| 4 | 26/03/2019 9:54 a.... | Carpeta de archivos |
| 5 | 26/03/2019 9:55 a.... | Carpeta de archivos |
| 6 | 26/03/2019 9:55 a.... | Carpeta de archivos |
| 7 | 26/03/2019 9:55 a.... | Carpeta de archivos |
| 8 | 26/03/2019 9:56 a.... | Carpeta de archivos |
| 9 | 26/03/2019 9:56 a.... | Carpeta de archivos |
description: the folder "0" is outlined as selected; the left navigation pane is cut off and shows partial entries "es", "eca", "analisis", "nteligentes", "jos", "ificial", "ficial".
</image>

<!-- page:53 -->
<image id="img-053" kind="screenshot" page="53">
text: "Este equipo" | "Disco local (C:)" | "Usuarios" | "FBC" | "Dropbox" | "Vision Artificial" | "cnnSemillero" | "reconocimientoDigitos" | "dataset" | "0" | "Buscar en 0" | "0_0" "0_1" "0_2" … "0_59"
description: Windows Explorer inside the folder dataset > 0, showing 60 thumbnails named 0_0 to 0_59 (white handwritten zeros on black, 28x28 style) in rows of 11 (0_0–0_10, 0_11–0_21, 0_22–0_32, 0_33–0_43, 0_44–0_54, 0_55–0_59); left pane partially visible ("alisis", "eligentes", "s", "cial", "cial").
</image>

<!-- page:54 -->
<image id="img-054" kind="screenshot" page="54">
text: "Este equipo" | "Disco local (C:)" | "Usuarios" | "FBC" | "Dropbox" | "Vision Artificial" | "cnnSemillero" | "reconocimientoDigitos" | "dataset" | "5" | "Buscar en 5" | "5_0" "5_1" … "5_39"
description: Windows Explorer inside the folder dataset > 5, showing 40 thumbnails named 5_0 to 5_39 (white handwritten fives on black) in 4 rows of 10 (5_0–5_9, 5_10–5_19, 5_20–5_29, 5_30–5_39); left pane partially visible ("is", "entes").
</image>

<!-- page:55 -->
<image id="img-055" kind="diagram" page="55">
text: "imagenesEntrenamiento" | "valoresEsperados" | "..."
data:
| variable | primer elemento | siguiente | elemento de dígito 5 | siguiente |
|---|---|---|---|---|
| imagenesEntrenamiento | white handwritten 0 on black | ... | white handwritten 5 on black | ... |
| valoresEsperados | 1 0 0 0 0 0 0 0 0 0 | ... | 0 0 0 0 0 1 0 0 0 0 | ... |
description: two long boxes divided into cells; the top box holds images, the bottom box holds one-hot vectors of 10 values (a 1 at the position of the digit class).
</image>

<!-- page:56 -->
<image id="img-056" kind="diagram" page="56">
text: "imagenesEntrenamiento" | "valoresEsperados" | "..."
description: same diagram as page 55: images 0 ... 5 ... and one-hot vectors 1 0 0 0 0 0 0 0 0 0 ... 0 0 0 0 0 1 0 0 0 0 ...
</image>

<!-- page:57 -->
<image id="img-057" kind="screenshot" page="57">
code:
```python
model=Sequential()
#Capa entrada
model.add(InputLayer(input_shape=(img_size_flat,)))
```
</image>

<!-- page:58 -->
```python
model = Sequential()
# Capa entrada
model.add(InputLayer(input_shape=(img_size_flat,)))
# Reformar imagen
model.add(Reshape(img_shape))
# Capas convolucionales
model.add(Conv2D(kernel_size=5, strides=1, filters=16, padding='same', activation='relu', name='capa_convolucion_1'))
model.add(MaxPooling2D(pool_size=2, strides=2))
model.add(Conv2D(kernel_size=5, strides=1, filters=36, padding='same', activation='relu', name='capa_convolucion_2'))
model.add(MaxPooling2D(pool_size=2, strides=2))
# Aplanar imagen
model.add(Flatten())
# Capa densa
model.add(Dense(128, activation='relu'))
# Capa salida
model.add(Dense(num_clases, activation='softmax'))
```

<image id="img-058" kind="screenshot" page="58">
visual: code slide; the text is the code block above.
</image>

<!-- page:59 -->
```python
model.compile(optimizer="adam",
              loss='categorical_crossentropy',
              metrics=['accuracy']
)
#Entrenamiento del modelo
model.fit(x=imagenes,y=probabilidades,epochs=10,batch_size=100)
```

<image id="img-059" kind="screenshot" page="59">
visual: code slide; the text is the code block above.
</image>

<!-- page:60 -->
```python
limiteImagenesPrueba=[20,20,20,20,20,20,20,20,20,20]
imagenesPrueba,probabilidadesPrueba=cargarDatos("dataset/test/",num_clases,limiteImagenesPrueba,width,height)
resultados=model.evaluate(x=imagenesPrueba,y=probabilidadesPrueba)
print("{0}: {1:.2%}".format(model.metrics_names[1], resultados[1]))
#Carpeta y nombre del archivo como se almacenará el modelo
nombreArchivo='models/modeloA.keras'
model.save(nombreArchivo)
model.summary()
```

<image id="img-060" kind="screenshot" page="60">
visual: code slide; the text is the code block above.
</image>
