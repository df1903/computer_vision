# Primer corte — CERRADO

Estado: **cerrado** (2026-10-13). Alcance: desde *Fundamentos* hasta **K-Means** inclusive. Lo que llegue después (CNN en adelante) pertenece al segundo corte.

## Contenido cubierto

| Bloque | Material de clase (`material-clase/`) | Contexto (`.context/curso/`) |
|---|---|---|
| Imagen como arreglo, BGR | `1_Fundamentación.ipynb`, `FundamentosVisionArtificial.md` | `temario.md` §2 |
| Espacios de color (HSV, CIELAB) | `2_Espacios_de_Color.ipynb` | `temario.md` §3 |
| Operaciones entre imágenes (resta, AND) | `3_OperacionesMatemáticas.ipynb` | `temario.md` §4 |
| Filtros, Gaussiano, Canny | `FundamentosVisionArtificial.md` | `temario.md` §5–7 |
| Morfología, figuras geométricas | `FundamentosVisionArtificial.md` | `temario.md` §8–9 |
| K-Means (clustering / segmentación por color) | `18-K-MEANS-Basico.pdf.md`, `4_Kmeans_Imagenes.ipynb` | `10-kmeans.md` |

## Trabajos entregados en el corte

| # | Trabajo | Técnicas |
|---|---|---|
| 01 | `trabajos/01-deteccion-color-amarillo/` | HSV + `inRange` + contornos |
| 02 | `trabajos/02-espacios-color/` | `cvtColor` entre 9 espacios en vivo |
| 03 | `trabajos/03-analisis-facial/` | MediaPipe FaceLandmarker (fuera del temario clásico) |
| 04 | `trabajos/04-filtros-morfologicos/` | Canny + erosión/dilatación/apertura/cierre en vivo |
| 05 | `trabajos/05-lector-pare-siga/` | HSV + morfología + contornos/circularidad |

## Notas de cierre

- K-Means **no** tiene trabajo propio en `trabajos/`: se vio con diapositivas y notebook (Colab). Si el profesor pide una actividad evaluativa, va como `trabajos/06-*/`.
- Material posterior a K-Means ya recibido: CNN y arquitecturas reconocidas (`11-cnn.md`). Se trata como **inicio del segundo corte**, no como parte de este.
- Pendiente fuera del repo: ninguna entrega abierta conocida del corte 1.
