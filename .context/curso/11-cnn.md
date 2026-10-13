# Redes Neuronales Convolucionales (CNN) y arquitecturas reconocidas

> **Fuentes:** `material-clase/2_CNNs.md` (60 diapositivas) y `material-clase/2_CNNs_Reconocidas.md` (VGG, MobileNet, ResNet, DenseNet, ConvNeXt). Felipe Buitrago Carmona, Universidad de Caldas.
> **Posición en el curso:** material recibido **después** de K-Means. Inicio del segundo corte; **no** está dentro del primer corte cerrado (ver `corte-1.md`). Aún sin trabajo evaluativo asociado.
> **Etiquetas:** `[CURSO]` / `[AMPLIACIÓN]` / `[NOTA]` como en `10-kmeans.md`.

## 1. Contexto y definición `[CURSO]`

- Aprendizaje **supervisado**: entrada X (imagen) → salida Y (etiqueta con probabilidad). Ej.: gato 94 %, perro 20 %.
- Motivación biológica: la corteza visual primaria; "el cerebro tardó 500 millones de años en desarrollar esta habilidad".
- **CNN**: clase de red neuronal artificial que usa capas convolucionales para filtrar entradas y obtener información útil (NVIDIA, 2018). Aplicaciones: clasificación de imágenes, texto, video, voz.
- Lo que la máquina "ve": una matriz de números (0–255 por píxel) → conecta con el tema 1 del temario (imagen como arreglo).

## 2. Estructura `[CURSO]`

```
Entrada → [Convolución → Activación → Pooling] ×N → Aplanamiento → Densa(s) → Salida (softmax)
          └──────── extracción de características ────────┘   └──── clasificación ────┘
```

| Capa | Qué hace |
|---|---|
| **Entrada** | Cada píxel es una neurona (imagen 28×28 → 784 entradas, o `Reshape` a `(28, 28, canales)`). |
| **Convolución** | Desliza filtros (kernels) sobre la imagen para realzar características. Puede reducir la imagen. Es el mismo concepto de kernel del tema 5 del temario, pero los valores se **aprenden**. |
| **Activación** (ReLU, sigmoide, tanh, escalón) | Introduce **no linealidad**. |
| **Pooling** (max / average) | Reduce la imagen conservando lo más relevante. |
| **Aplanamiento (Flatten)** | Matriz → vector (fila tras fila) para pasar a capas densas. |
| **Densa (fully connected)** | Clasifica con las características extraídas (`Dense(128, 'relu')`). |
| **Salida** | Una neurona por clase, `softmax` → valor 0–1 por clase; la **mayor** es la clasificación final. |

## 3. Convolución: cuenta paso a paso `[CURSO]`

Entrada 5×5 y filtro 3×3:

```
Entrada            Filtro
3 5 2 8 1          1 0 0
9 7 5 4 3          1 1 0
2 0 6 1 6          0 0 1
6 3 7 9 2
1 4 9 5 1
```

Ventana superior izquierda: `3·1 + 9·1 + 7·1 + 6·1 = 25` (los demás productos valen 0). Mapa de salida 3×3:

```
25 18 17
18 22 14
20 15 23
```

**Tamaño de salida** (sin padding): `w_f = (w_i − f)/s + 1`, `h_f = (h_i − f)/s + 1` (`f` = lado del filtro, `s` = stride). 5×5 con f=3, s=1 → 3×3.
`[AMPLIACIÓN]` Con padding `p`: `(w_i − f + 2p)/s + 1`. `padding='same'` en Keras conserva el tamaño.

Kernels de ejemplo de la clase (los mismos del temario): Original `[[0,0,0],[0,1,0],[0,0,0]]`, Gaussian blur `1/16·[[1,2,1],[2,4,2],[1,2,1]]`, Sharpen `[[0,-1,0],[-1,5,-1],[0,-1,0]]`, Edge detection `[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]`.

## 4. Activación `[CURSO]`

| Función | Fórmula | Rango |
|---|---|---|
| Escalón | 0 si x<0; 1 si x≥0 | 0–1 |
| Escalón simétrico | −1 si x<0; 1 si x≥0 | −1–1 |
| Sigmoide | `1/(1+e^−x)`; `f'(x) = y(1−y)` | 0–1 |
| Tangente hiperbólica | `(e^x−e^−x)/(e^x+e^−x)` | −1–1 |

`[NOTA]` La diapositiva se titula "ReLU" pero no grafica ReLU. `[AMPLIACIÓN]` ReLU = `max(0, x)`, la usada en el código de la clase. La diapositiva imprime la derivada de la sigmoide con signo menos en el numerador (error tipográfico en la fuente).

## 5. Pooling `[CURSO]`

Entrada 4×4, ventanas 2×2, stride 2:

```
12  20 | 30  0         max pooling:   20  30      average pooling:  13   8
 8  12 |  2  0                        112  37                        79  20
-------+-------
34  70 | 37  4
112 100| 25 12
```

`[NOTA]` Ventana `37,4,25,12` → media 19.5; la diapositiva imprime 20 (redondeo).

## 6. Código de la clase (Keras) `[CURSO]`

Dataset de dígitos manuscritos 28×28 en escala de grises, 10 clases. Estructura: `dataset/train/N/N_i.jpg` y `dataset/test/N/N_i.jpg` (60 imágenes por dígito en train, 20 en test).

```python
width = 28; height = 28
img_size_flat = width * height
num_chanels = 1            # RGB, HSV -> 3
img_shape = (width, height, num_chanels)
num_clases = 10

def cargarDatos(fase, numeroCategorias, limite, width, height):
    imagenesCargadas, valorEsperado = [], []
    for categoria in range(numeroCategorias):
        for idImagen in range(limite[categoria]):
            ruta = fase + str(categoria) + "/" + str(categoria) + "_" + str(idImagen) + ".jpg"
            imagen = cv2.imread(ruta)
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (width, height))
            imagen = imagen.flatten() / 255          # normalizar 0-1
            imagenesCargadas.append(imagen)
            probabilidades = np.zeros(numeroCategorias)
            probabilidades[categoria] = 1            # one-hot
            valorEsperado.append(probabilidades)
    return np.array(imagenesCargadas), np.array(valorEsperado)

model = Sequential()
model.add(InputLayer(input_shape=(img_size_flat,)))
model.add(Reshape(img_shape))
model.add(Conv2D(kernel_size=5, strides=1, filters=16, padding='same', activation='relu', name='capa_convolucion_1'))
model.add(MaxPooling2D(pool_size=2, strides=2))
model.add(Conv2D(kernel_size=5, strides=1, filters=36, padding='same', activation='relu', name='capa_convolucion_2'))
model.add(MaxPooling2D(pool_size=2, strides=2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_clases, activation='softmax'))

model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x=imagenes, y=probabilidades, epochs=10, batch_size=100)
resultados = model.evaluate(x=imagenesPrueba, y=probabilidadesPrueba)
model.save('models/modeloA.keras')
```

Flujo de tamaños: 28×28×1 → conv1 (16 filtros) 28×28×16 → pool 14×14×16 → conv2 (36) 14×14×36 → pool 7×7×36 → flatten 1764 → densa 128 → salida 10.
`[NOTA]` Las diapositivas muestran el bloque de código de forma fragmentada (el `MaxPooling2D` y el `Flatten` aparecen en slides distintas); el modelo completo es el de arriba. `cargarDatos` en la diapositiva desempaca 3 valores al llamarla pero devuelve 2 (inconsistencia de la fuente).
`[AMPLIACIÓN]` Requiere TensorFlow/Keras, que **no** está en `requirements.txt` (ver `state/known-issues.md`).

## 7. Arquitecturas reconocidas `[CURSO]` (`2_CNNs_Reconocidas.md`)

Todas toman entrada 224×224×3 y terminan en 1000 clases (ImageNet).

| Arquitectura | Idea clave | Detalles de la clase |
|---|---|---|
| **VGG16 / VGG19** | Pilas de convoluciones **3×3** + max pooling, simple y profunda. | 16 / 19 capas con pesos; bloques de 64→128→256→512→512 filtros; `FC 4096, FC 4096, FC 1000`, softmax. |
| **MobileNet** | Modelo ligero para móvil/embebido. | `[NOTA]` La figura bajo ese título en las diapositivas es en realidad una pila estilo VGG (conv1–conv5, fc6–fc8: 224×224×64 … 7×7×512 → 1×1×4096 → 1×1×1000). |
| **ResNet-50** | **Bloques residuales**: salida = `F(x) + x` (conexión skip/identidad). | conv1 7×7 s2 → pool → conv2_x(3) conv3_x(4) conv4_x(6) conv5_x(3) → global avg pool → fc. La suma ayuda al flujo del gradiente; bloques con stride 2 usan proyección 1×1 en el skip. |
| **DenseNet-121** | **Conexiones densas**: cada capa recibe la **concatenación** de todas las anteriores del bloque. | Dense blocks de 6, 12, 24, 16 capas, crecimiento `k = 32`; capas de transición (1×1 conv + avg pool 2×2) comprimen canales y resolución. |
| **ConvNeXt-Base** | CNN moderna inspirada en Transformers. | Stem 4×4 s4; 4 stages (3, 3, 9, 3 bloques; dim 96/192/384/768); patch merging 2×2 s2; depthwise conv 7×7, LayerNorm, expansión 1×1 (4C), GELU, Layer Scale γ. |

Resumen de progresión: **VGG** (apilar) → **ResNet** (sumar atajos) → **DenseNet** (concatenar todo) → **ConvNeXt** (CNN con ideas de Transformers). **MobileNet** = eficiencia.

## 8. Conexión con el temario `[AMPLIACIÓN]`

- Kernel y convolución del tema 5 son exactamente la operación de la capa convolucional; la diferencia es que en CNN el entrenamiento **aprende** los valores del kernel.
- Las primeras capas de una CNN aprenden filtros parecidos a Gauss/Sobel; las siguientes combinan bordes en formas (conecta con temas 7–9).
- Normalizar `/255` y pasar a gris/`resize` es preprocesamiento clásico del curso.
- K-Means (`10-kmeans.md`) = no supervisado; CNN = supervisado (necesita dataset etiquetado).
