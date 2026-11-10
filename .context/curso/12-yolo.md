# Detección de objetos y YOLO

> **Fuente:** `material-clase/4_Yolo.md` (22 diapositivas, transcripción del PDF `4_Yolo.pptx`). Felipe Buitrago Carmona, Universidad de Caldas.
> **Posición en el curso:** material recibido **después** de CNN (`11-cnn.md`). Segundo corte. Aún sin trabajo evaluativo asociado.
> **Etiquetas:** `[CURSO]` / `[AMPLIACIÓN]` / `[NOTA]` como en `10-kmeans.md`.

## 1. Qué es YOLO `[CURSO]`

**YOLO (You Only Look Once)**: detector de objetos que identifica y localiza **varios objetos** en una imagen con **una sola pasada** por la red.

- Detección en tiempo real, alta velocidad de inferencia.
- Predice clases y ubicaciones simultáneamente.

Diferencia con la CNN de clasificación (`11-cnn.md`): clasificar da **una etiqueta por imagen**; detectar da **N cajas + clase + confianza**.

## 2. Componentes de un detector `[CURSO]`

| Componente | Qué es | Pregunta que responde |
|---|---|---|
| **Backbone** | CNN que extrae *features* (ej. VGG16) | ¿Qué características tiene la imagen? |
| **Region Proposal** | Propone "aquí podría haber un objeto" | ¿Dónde podría haber un objeto? |
| **ROI Pooling** | Lleva cada región a tamaño fijo | ¿Cómo estandarizo cada región? |
| **Bounding Box Regression** | Genera la caja `(x, y, ancho, alto)` | ¿Dónde está el objeto? |
| **Una / dos etapas** | Paso 1 encontrar candidatos, paso 2 clasificar | ¿Lo hago en uno o dos pasos? |

- **Backbone:** los *feature maps* se ven como imágenes en gris; zonas claras = activación alta; los patrones dependen de lo que aprendió cada filtro. VGG16: conv1…conv5 + max pooling (224×224×64 → 7×7×512) + fc6/fc7/fc8.
- **Region Proposal:** (1) divide en regiones pequeñas, (2) busca similitud de color/textura/intensidad, (3) agrupa progresivamente, (4) genera candidatas de distintos tamaños (*Selective Search*; en Faster R-CNN lo aprende una **RPN**).
- **ROI Pooling:** (1) estandariza regiones a tamaño fijo (ej. 7×7), (2) aplica Max Pooling por subdivisión, (3) deja representaciones uniformes para clasificación y regresión.
- **Bounding Box Regression:** parte de una caja aproximada (ancla); la red predice cuánto **desplazar y escalar** (`σ(tx)`, `σ(ty)`, `e^tw`, `e^th` respecto a la celda `cx, cy`) y produce la caja refinada.

## 3. Cómo clasifican los modelos `[CURSO]`

| | Por región | Compartida | Directa |
|---|---|---|---|
| Cómo | Una CNN por región | CNN una vez; regiones comparten features | Una pasada predice clases y cajas |
| Velocidad | Muy lenta | Más rápida | Muy rápida (tiempo real) |
| Modelos | R-CNN (2014) | Fast / Faster R-CNN (2015) | SSD (2016), YOLO (2015 →) |

**Idea clave:** al evolucionar se eliminan pasos intermedios (propuestas de regiones, ROI Pooling) → más velocidad sin perder tanta precisión.

## 4. Versiones `[CURSO]`

| Modelo | Año | Backbone | Etapas | Velocidad | Precisión |
|---|---|---|---|---|---|
| R-CNN | 2014 | AlexNet | 2 | Muy lenta | Media |
| Fast R-CNN | 2015 | VGG16 | 2 | Lenta | Media |
| Faster R-CNN | 2015 | VGG16 / ResNet | 2 | Media | Alta |
| SSD | 2016 | VGG16 | 1 | Rápida | Alta |
| YOLOv1 | 2015 | CNN propia (24 conv + 2 FC) | 1 | Rápida | Baja |
| YOLOv2 | 2016 | Darknet-19 | 1 | Muy rápida | Media |
| YOLOv3 | 2018 | Darknet-53 | 1 | Muy rápida | Alta |
| YOLOv4 | 2020 | CSPDarknet53 | 1 | Muy rápida | Muy alta |
| YOLOv5 | 2020 | CSPDarknet53 | 1 | Muy rápida | Muy alta |
| YOLOv6 | 2022 | Efficient RepBackbone | 1 | Muy rápida | Muy alta |
| YOLOv7 | 2022 | E-ELAN | 1 | Muy rápida | Muy alta |
| YOLOv8 | 2023 | C2f / CSP | 1 | Muy rápida | Muy alta |
| YOLOv10 | 2024 | C2f / OBB optimizado | 1 | Ultra rápida | Muy alta |

- Region Proposal: Selective Search (R-CNN, Fast), RPN (Faster); ninguno en SSD/YOLO. ROI Pooling: solo Fast y Faster R-CNN.
- Detección multiescala: no en R-CNN/Fast/Faster ni YOLOv1; sí en SSD y YOLOv2 en adelante.

## 5. Dos etapas vs una etapa `[CURSO]`

- **Dos etapas** (R-CNN, Fast/Faster R-CNN, **Mask R-CNN** = Faster R-CNN + segmentación de instancias): 1) proponer regiones, 2) clasificar cada una. Pro: excelente precisión, mejor con objetos pequeños. Contra: más lento.
- **Una etapa** (SSD, YOLO): localiza y clasifica en un solo proceso. SSD = *Single Shot MultiBox Detector*, predice a varias escalas. YOLO divide en cuadrícula y predice cajas y clases a la vez. Pro: alta velocidad, tiempo real.

## 6. Proceso de detección de YOLO `[CURSO]`

1. **Entrada:** imagen completa.
2. **Cuadrícula S×S:** cada celda es responsable de predecir objetos.
3. **Bounding boxes:** cada celda predice **B** cajas `(x, y, w, h)` + *confidence score*.
4. **Clases:** por caja, probabilidad de cada clase (ej. Perro 0.92, Gato 0.05, Auto 0.01).
5. **Selección final:** se eliminan duplicados y baja confianza con **NMS** (*Non-Maximum Suppression*).

- **Bounding box:** rectángulo que delimita un objeto.
- **Confidence score:** probabilidad de que haya objeto en la caja, de 0.0 (sin objeto) a 1.0 (seguro).

`[AMPLIACIÓN]` NMS: ordena cajas por confianza, conserva la mayor y descarta las que se solapan con ella por encima de un umbral de **IoU** (intersección sobre unión). `cv2.dnn.NMSBoxes` lo implementa en OpenCV.

## 7. Arquitectura de YOLO `[CURSO]`

Flujo: `Imagen → Backbone → Neck → Head → Detecciones`

| Parte | Función | Ejemplos |
|---|---|---|
| **Backbone** | Extrae características visuales | CSPDarknet, EfficientNet |
| **Neck** | Combina información de distintas escalas | FPN, PAN-FPN |
| **Head** | Predice clases, cajas `(x, y, w, h)` y confianza por celda/ancla | — |

Las versiones modernas usan estructuras especializadas para detectar objetos grandes y pequeños.

## 8. Desafíos `[CURSO]`

Objetos pequeños · oclusiones · variaciones de iluminación · diferentes escalas · fondos complejos · tiempo real.

## 9. Conexión con el resto del curso `[AMPLIACIÓN]`

- El backbone de YOLO es una CNN como las de `11-cnn.md` (VGG, ResNet, etc.) usada para extraer *features*.
- Las cajas se dibujan con `cv2.rectangle` y `cv2.putText` (`temario.md`); `boundingRect` (contornos clásicos) también da `(x, y, w, h)`, pero sin clase ni aprendizaje.
- Ejecutar un modelo ya entrenado en OpenCV: `cv2.dnn` (ONNX). Usar YOLO moderno con la librería `ultralytics` **no está aprobado** en `stack.md`: preguntar antes de añadirla.
