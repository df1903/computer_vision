# `.context/curso/` — contexto de la materia

Orden de lectura sugerido al escribir o explicar código de visión artificial:

| Archivo | Qué contiene | Corte |
|---|---|---|
| `temario.md` | Base del curso: imagen/BGR, HSV, CIELAB, AND/absdiff, filtros, Canny, morfología, figuras geométricas, errores comunes, glosario. **Leer primero.** | 1 |
| `10-kmeans.md` | K-Means: algoritmo, ejemplo manual, segmentación de imágenes por color. | 1 |
| `corte-1.md` | Qué cubre el primer corte (cerrado) y qué trabajos lo componen. | 1 |
| `11-cnn.md` | CNN: capas, convolución/pooling, código Keras, arquitecturas (VGG, ResNet, DenseNet, ConvNeXt). | 2 (inicio) |
| `12-yolo.md` | Detección de objetos: componentes (backbone, region proposal, ROI pooling), una vs dos etapas, versiones YOLO, proceso (cuadrícula, NMS), arquitectura backbone/neck/head. | 2 |

## Convenciones

- Archivos nuevos: `NN-tema.md`, numeración continua tras `10`. `temario.md` no se parte.
- Cada archivo marca el origen: `[CURSO]` (dado en clase), `[AMPLIACIÓN]` (añadido), `[NOTA]` (precisión sobre una diapositiva).
- Las fuentes crudas (transcripciones, notebooks) viven en `material-clase/`; aquí va la versión **curada** para trabajar.
