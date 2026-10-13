---
source: "18-K-MEANS-Basico.pdf"
format: "pdf"
converted: "2026-10-13"
title: "K-MEANS"
lang: "es"
pages: 28
pdf_author: "Admin"
images: 28
notes: ["every page is a slide exported as a picture (28 of 28); content transcribed from renders, with the text layer used as cross-check", "slides are a manual k-means walkthrough with 17 numbered 'cards' (3 centroids + 14 observations) colored yellow/red/green; the card's own color is part of its identity, the rectangle it sits in is its cluster", "the three centroid cards all have a green background on pages 8-19 regardless of the rectangle they sit above", "pages 9 and 10 share the same calculation and card pool; page 10 additionally circles the result 5 in blue (repeated animation build)", "page 23 shows 8 inside the red rectangle while page 28 groups the card 8 with the yellow cards; kept as in source", "page 19: the sum 114 is divided by 13 giving 8.7 and the resulting card shows 8 (red background); kept verbatim", "page 24: the first URL is split by a layout break in the source text layer ('se gmentation'); written here as the intended URL", "verify exceptions (9 tokens): 'ndimensional' and 'extraclouster' are line-break joins in the text layer (slides show 'n-dimensional' and 'extra-clouster'); the formula tokens (dxi, xj, σk, xik, xjk) are rewritten as LaTeX; 'se' + 'gmentation' are the split URL on page 24", "p.5 'observaciones evaluados' and 'clousters' / 'clouster' are spelling or agreement errors in the source, kept verbatim and marked [sic] where first needed"]
---

<!-- page:1 -->
# K-MEANS

<image id="img-001" kind="slide-image" page="1">
title slide: "K-MEANS", subtitle "FELIPE BUITRAGO CARMONA"
visual: dark title bar with a black square at its right; gray gradient background.
</image>

<!-- page:2 -->
## Descripción

- Agrupación entre elementos que son similares
- Se puede utilizar en datos no etiquetados
- Algoritmo de aprendizaje automático no supervisado

<image id="img-002" kind="chart" page="2">
text: "k-Means Clusters" | "Dim. 1" "Dim. 2" "Dim. 3" | "Cluster 1 +" "Cluster 2 x" "Cluster 3 O"
description: 3D-style scatter plot titled "k-Means Clusters" with axes Dim. 1 (horizontal), Dim. 2 (vertical) and a small Dim. 3 axis at the bottom-left. Cluster 1 = red "+" marks, small group at upper-left with one larger "+" as its centroid. Cluster 2 = blue "x" marks, group below and left of Cluster 1, one larger "x" as its centroid. Cluster 3 = green circles, a large spread-out group on the right and lower-right, one larger circle as its centroid. Legend at bottom-right. Individual point values are not labeled.
</image>

<!-- page:3 -->
## Descripción

- Centroide: Elemento central en el espacio n-dimensional de los n Atributos del Data Set.
- Clúster: Consisten en valores similares. La similitud entre los valores se basa en una medida de distancia entre ellos.
- Observación: Elemento del grupo de datos

<image id="img-003" same_as="img-002" page="3"/>
<image id="overlay-p3-1" kind="diagram" page="3">
description: drawn over the scatter plot: a black ellipse outline encircling the green Cluster 3 cloud, a black upward-pointing arrow pointing at the center of that cloud (its centroid) and a small red arrow pointing at a single green point at the upper right (an observation).
</image>

<!-- page:4 -->
## Consideraciones

- Minimizar variación intra-clouster
- Maximizar variación extra-clouster

<image id="img-004" same_as="img-002" page="4"/>

<!-- page:5 -->
## Distancia

$$d(x_i, x_j) = \sqrt{\sum_{k=1}^{p} (x_{ik}-x_{jk})^2}$$

Fórmula 1

- p= Número de dimensiones
- x= observaciones evaluados [sic]

<image id="img-005" same_as="img-002" page="5"/>

<!-- page:6 -->
## Algoritmo

- Paso 1. k= Número de clousters [sic]
- Paso 2. Elección de centroides
- Paso 3. Medir la distancia de las observaciones a los k centroides. (Fórmula 1)
- Paso 4.Asignar cada observación al centroide mas cercano
- Paso 5. Por cada grupo, actualizar el centroide, calculando el dato medio del conjunto
- Paso 6. Repetir el paso 3,4 y 5 hasta que no cambien los centroides

<image id="img-006" kind="slide-image" page="6">
visual: text-only slide; no figure beyond the slide frame.
</image>

<!-- page:7 -->
## Algoritmo

Paso 1. **k= 3**

<image id="img-007" kind="diagram" page="7">
description: three empty rectangles (amarillo, rojo, verde) for the 3 clusters; below them 17 numbered oval cards, each on a colored square (amarillo/rojo/verde), not yet placed.
| Fila | Tarjetas (valor: color) |
|---|---|
| Superior | 4: rojo, 8: rojo, 13: amarillo, 10: amarillo, 2: verde, 12: amarillo, 6: rojo, 1: verde |
| Inferior | 10: amarillo, 3: verde, 13: amarillo, 1: verde, 6: rojo, 5: rojo, 13: amarillo, 2: verde, 11: amarillo |
</image>

<!-- page:8 -->
## Algoritmo

### Paso 2. Elección de centroides

<image id="img-008" kind="diagram" page="8">
description: same rectangles; one centroid card sits above each rectangle (all three on green squares). 14 cards remain unplaced below.
| Elemento | Valor(es) |
|---|---|
| Centroide sobre el rectángulo amarillo | 3 |
| Centroide sobre el rectángulo rojo | 2 |
| Centroide sobre el rectángulo verde | 1 |
| Tarjetas sin asignar (fila superior) | 4: rojo, 8: rojo, 13: amarillo, 10: amarillo, 12: amarillo, 6: rojo |
| Tarjetas sin asignar (fila inferior) | 10: amarillo, 13: amarillo, 1: verde, 6: rojo, 5: rojo, 13: amarillo, 2: verde, 11: amarillo |
</image>

<!-- page:9 -->
## Algoritmo

### Paso 3. Medir la distancia de las observaciones a los k centroides. (Fórmula 1)

<image id="img-009" kind="diagram" page="9">
description: black boxes inside each rectangle show the distance from observation 8 (red card) to that rectangle's centroid. Card 8 is not in the unplaced pool.
| Rectángulo | Cálculo mostrado |
|---|---|
| Amarillo (centroide 3) | 8 - 3 = 5 |
| Rojo (centroide 2) | 8 - 2 = 6 |
| Verde (centroide 1) | 8 - 1 = 7 |
Tarjetas sin asignar (fila superior): 4: rojo, 13: amarillo, 10: amarillo, 12: amarillo, 6: rojo
Tarjetas sin asignar (fila inferior): 10: amarillo, 13: amarillo, 1: verde, 6: rojo, 5: rojo, 13: amarillo, 2: rojo, 11: amarillo
</image>

<!-- page:10 -->
## Algoritmo

### Paso 3. Medir la distancia de las observaciones a los k centroides. (Fórmula 1)

<image id="img-010" kind="diagram" page="10">
description: same as page 9, with the result 5 of the yellow rectangle circled in blue (smallest distance).
| Rectángulo | Cálculo mostrado |
|---|---|
| Amarillo (centroide 3) | 8 - 3 = 5 (5 circled in blue) |
| Rojo (centroide 2) | 8 - 2 = 6 |
| Verde (centroide 1) | 8 - 1 = 7 |
Tarjetas sin asignar (fila superior): 4: rojo, 13: amarillo, 10: amarillo, 12: amarillo, 6: rojo
Tarjetas sin asignar (fila inferior): 10: amarillo, 13: amarillo, 1: verde, 6: rojo, 5: rojo, 13: amarillo, 2: rojo, 11: amarillo
</image>

<!-- page:11 -->
## Algoritmo

### Paso 4.Asignar cada observación al centroide mas cercano

<image id="img-011" kind="diagram" page="11">
description: card 8 is now inside the yellow rectangle next to centroid 3.
| Elemento | Valor(es) |
|---|---|
| Rectángulo amarillo | centroide 3; asignado: 8 |
| Rectángulo rojo | centroide 2; sin asignaciones |
| Rectángulo verde | centroide 1; sin asignaciones |
| Tarjetas sin asignar (fila superior) | 4: rojo, 13: amarillo, 10: amarillo, 12: amarillo, 6: rojo |
| Tarjetas sin asignar (fila inferior) | 10: amarillo, 13: amarillo, 1: verde, 6: rojo, 5: rojo, 13: amarillo, 2: rojo, 11: amarillo |
</image>

<!-- page:12 -->
Repetir Proceso Por Cada Elemento

<image id="img-012" kind="slide-image" page="12">
visual: divider slide; only the title text above.
</image>

<!-- page:13 -->
## Algoritmo

### Paso 3. Medir la distancia de las observaciones a los k centroides. (Fórmula 1)

<image id="img-013" kind="diagram" page="13">
description: same layout as page 9 but evaluating observation 4 (red card). The yellow result 4 - 3 = 1 is circled in red (smallest). Yellow rectangle holds centroid 3 and, from before, card 8 (not drawn on this page).
| Rectángulo | Cálculo mostrado |
|---|---|
| Amarillo (centroide 3) | 4 - 3 = 1 (1 circled in red) |
| Rojo (centroide 2) | 4 - 2 = 2 |
| Verde (centroide 1) | 4 - 1 = 3 |
Tarjetas sin asignar (fila superior): 13: amarillo, 10: amarillo, 12: amarillo, 6: rojo
Tarjetas sin asignar (fila inferior): 10: amarillo, 13: amarillo, 1: verde, 6: rojo, 5: rojo, 13: amarillo, 2: rojo, 11: amarillo
</image>

<!-- page:14 -->
## Algoritmo

### Paso 4.Asignar cada observación al centroide mas cercano

<image id="img-014" kind="diagram" page="14">
description: yellow rectangle now holds centroid 3 and cards 8 and 4.
| Elemento | Valor(es) |
|---|---|
| Rectángulo amarillo | centroide 3; asignados: 8, 4 |
| Rectángulo rojo | centroide 2; sin asignaciones |
| Rectángulo verde | centroide 1; sin asignaciones |
| Tarjetas sin asignar (fila superior) | 13: amarillo, 10: amarillo, 12: amarillo, 6: rojo |
| Tarjetas sin asignar (fila inferior) | 10: amarillo, 13: amarillo, 1: verde, 6: rojo, 5: rojo, 13: amarillo, 2: rojo, 11: amarillo |
</image>

<!-- page:15 -->
Finalmente

<image id="img-015" kind="slide-image" page="15">
visual: divider slide; only the title text above.
</image>

<!-- page:16 -->
## Algoritmo

### Paso 4.Asignar cada observación al centroide mas cercano

<image id="img-016" kind="diagram" page="16">
description: fully assigned state of Paso 4. Yellow rectangle holds its centroid plus 12 cards in a 3x4 grid; red and green rectangles hold only one card each besides their centroid.
| Rectángulo | Centroide | Miembros |
|---|---|---|
| Amarillo | 3 | 8: rojo, 11: amarillo, 13: amarillo, 10: amarillo, 13: amarillo, 5: rojo, 4: rojo, 12: amarillo, 6: rojo, 6: rojo, 13: amarillo, 10: amarillo |
| Rojo | 2 | 2: verde |
| Verde | 1 | 1: verde |
</image>

<!-- page:17 -->
Paso 5

<image id="img-017" kind="slide-image" page="17">
visual: divider slide; only the title text above.
</image>

<!-- page:18 -->
## Algoritmo

### Paso 5. Por cada grupo, actualizar el centroide, calculando el dato medio del conjunto

<image id="img-018" kind="diagram" page="18">
description: same state as page 16 (yellow: centroid 3 plus the 12 members; red: centroid 2 and card 2; green: centroid 1 and card 1), shown before the mean calculation.
| Rectángulo | Centroide | Miembros |
|---|---|---|
| Amarillo | 3 | 8, 11, 13, 10, 13, 5, 4, 12, 6, 6, 13, 10 |
| Rojo | 2 | 2 |
| Verde | 1 | 1 |
</image>

<!-- page:19 -->
## Algoritmo

### Paso 5. Por cada grupo, actualizar el centroide, calculando el dato medio del conjunto

8+11+13+10+13+5+4+12+6+6+13+10+3=114

114/13=8.7

<image id="img-019" kind="diagram" page="19">
description: the yellow rectangle (centroid 3 with the 12 members) is shown at the left, the sum and the division at the right. Below the calculation a red card with 8 appears: the new yellow centroid.
| Rectángulo | Centroide | Miembros |
|---|---|---|
| Amarillo | 3 | 8, 11, 13, 10, 13, 5, 4, 12, 6, 6, 13, 10 |
</image>

<!-- page:20 -->
## Algoritmo

### Paso 6. Repetir el paso 3,4 y 5 hasta que no cambien los centroides

<image id="img-020" kind="diagram" page="20">
description: first iteration of Paso 6. Yellow centroid is now 8 (red card).
| Rectángulo | Centroide | Miembros |
|---|---|---|
| Amarillo | 8 | 13, 11, 13, 10, 13, 12, 10, 6, 6 |
| Rojo | 2 | 2, 3, 4, 5 |
| Verde | 1 | 1 |
</image>

<!-- page:21 -->
## Algoritmo

### Paso 6. Repetir el paso 3,4 y 5 hasta que no cambien los centroides

<image id="img-021" kind="diagram" page="21">
description: yellow centroid is 10 (yellow card); red centroid is 3 (green card); green centroid is 1.
| Rectángulo | Centroide | Miembros |
|---|---|---|
| Amarillo | 10 | 13, 11, 13, 8, 13, 12, 10 |
| Rojo | 3 | 2, 2, 4, 5, 6, 6 |
| Verde | 1 | 1 |
</image>

<!-- page:22 -->
## Algoritmo

### Paso 6. Repetir el paso 3,4 y 5 hasta que no cambien los centroides

<image id="img-022" kind="diagram" page="22">
description: yellow centroid is 11 (yellow card); red centroid is 4 (red card); green centroid is 1.
| Rectángulo | Centroide | Miembros |
|---|---|---|
| Amarillo | 11 | 13, 13, 8, 13, 12, 10, 10 |
| Rojo | 4 | 2, 2, 3, 5, 6, 6 |
| Verde | 1 | 1 |
</image>

<!-- page:23 -->
## Algoritmo

### Paso 6. Repetir el paso 3,4 y 5 hasta que no cambien los centroides

<image id="img-023" kind="diagram" page="23">
description: last iteration shown. Yellow centroid 11 (unchanged); red centroid 6 (red card); green centroid 2 (green card).
| Rectángulo | Centroide | Miembros |
|---|---|---|
| Amarillo | 11 | 13, 13, 10, 13, 12, 10 |
| Rojo | 6 | 6, 4, 5, 8 |
| Verde | 2 | 1, 1, 2, 3 |
</image>

<!-- page:24 -->
## Referencias

[https://docs.rapidminer.com/latest/studio/operators/modeling/segmentation/k_means.html](https://docs.rapidminer.com/latest/studio/operators/modeling/segmentation/k_means.html)

[https://www.youtube.com/watch?v=zHbxbb2ye3E](https://www.youtube.com/watch?v=zHbxbb2ye3E)

<image id="img-024" kind="slide-image" page="24">
visual: links in light green on the gray gradient background.
</image>

<!-- page:25 -->
## Descripción (P)

- Centroide
- Clúster
- Calcular los centroides de los clústeres promediando todos los valores de un clúster. Los pasos anteriores se repiten para los nuevos centroides hasta que los centroides ya no se muevan o se alcancen los *pasos de optimización máximos*
- Ejemplo K=3

<image id="img-025" kind="diagram" page="25">
description: a black arrow points from the word "Centroide" to a brace under it labeled by the word "Clúster" (one cell). Under "Ejemplo K=3", three black arrows point at three adjacent squares, each with a brace underneath.
| Cuadro | Color | Valor |
|---|---|---|
| 1 | verde oscuro | 2 |
| 2 | verde claro | 4 |
| 3 | verde brillante | 6 |
</image>

<!-- page:26 -->
## Descripción (P)

- Centroide
- Clúster
- Calcular los centroides de los clústeres promediando todos los valores de un clúster. Los pasos anteriores se repiten para los nuevos centroides hasta que los centroides ya no se muevan o se alcancen los *pasos de optimización máximos*
- Ejemplo K=3

<image id="img-026" kind="diagram" page="26">
description: six squares in 3 groups of two, each group under its own brace; arrows over the groups carry the group centroid.
| Cuadro | Color | Valor |
|---|---|---|
| 1 | verde oscuro | 2 |
| 2 | verde claro | 4 |
| 3 | verde brillante | 6 |
| 4 | azul oscuro | 8 |
| 5 | azul medio | 10 |
| 6 | azul claro | 12 |
| Grupo (llave inferior) | Cuadros | Centroide (flecha) |
|---|---|---|
| 1 | 2, 4 | 3 |
| 2 | 6, 8 | 7 |
| 3 | 10, 12 | 11 |
</image>

<!-- page:27 -->
## Descripción (P)

- Centroide
- Clúster
- Calcular los centroides de los clústeres promediando todos los valores de un clúster. Los pasos anteriores se repiten para los nuevos centroides hasta que los centroides ya no se muevan o se alcancen los *pasos de optimización máximos*
- Ejemplo K=3

<image id="img-027" kind="diagram" page="27">
description: nine squares in 3 groups of three, each group under its own brace; arrows over each group's middle square carry the centroid.
| Cuadro | Color | Valor |
|---|---|---|
| 1 | verde oscuro | 2 |
| 2 | verde claro | 4 |
| 3 | verde brillante | 6 |
| 4 | azul oscuro | 8 |
| 5 | azul medio | 10 |
| 6 | azul claro | 12 |
| 7 | rojo oscuro | 14 |
| 8 | rojo | 16 |
| 9 | magenta | 18 |
| Grupo (llave inferior) | Cuadros | Centroide (flecha) |
|---|---|---|
| 1 | 2, 4, 6 | 4 |
| 2 | 8, 10, 12 | 10 |
| 3 | 14, 16, 18 | 16 |
</image>

<!-- page:28 -->
## Algoritmo

## Paso 1. **k= 3**

<image id="img-028" kind="diagram" page="28">
description: the empty yellow/red/green rectangles from page 7, with the 17 cards below now sorted by card color into three groups (not placed inside the rectangles).
| Grupo (color de tarjeta) | Valores |
|---|---|
| Amarillo | 10, 11, 8, 13, 10, 13, 13, 12 |
| Rojo | 6, 3, 2, 6, 4, 5, 2 |
| Verde | 1, 1 |
</image>
