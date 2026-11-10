import os
import queue
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import cv2
import keras
import numpy as np

from cnn_trainer import MODELOS, CNNTrainer

# Rutas relativas a este archivo, no al directorio desde donde se ejecute
CARPETA = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(CARPETA, "dataset")
RESULTADOS = os.path.join(CARPETA, "resultados")

LADO_VISTA = 280  # Lado (px) del recuadro donde se muestra la imagen


def listar_modelos():
    """Busca resultados/<experimento>/<modelo>/<modelo>.keras y devuelve {etiqueta: ruta}."""
    encontrados = {}
    if not os.path.isdir(RESULTADOS):
        return encontrados
    for exp in sorted(os.listdir(RESULTADOS)):
        for nombre in MODELOS:
            ruta = os.path.join(RESULTADOS, exp, nombre, f"{nombre}.keras")
            if os.path.isfile(ruta):
                encontrados[f"{exp} / {nombre}"] = ruta
    return encontrados


class _Redirector:
    """Manda lo que se imprima (print y logs de Keras) a una cola para mostrarlo en la GUI."""

    def __init__(self, cola):
        self.cola = cola

    def write(self, texto):
        if texto:
            self.cola.put(texto)

    def flush(self):
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CNN - Cargar modelo y predecir")
        self.geometry("760x820")

        self.modelo = None
        self.preprocess = None
        self.img_size = (224, 224)
        # Las clases son las carpetas del dataset ordenadas, igual que en CNNTrainer
        self.clases = sorted(d for d in os.listdir(DATASET)
                             if os.path.isdir(os.path.join(DATASET, d)))
        self.cola_log = queue.Queue()
        self.entrenando = False
        self.rutas_modelos = {}
        self._foto = None  # referencia para que Tk no libere la imagen

        self._armar_panel_modelo()
        self._armar_panel_prediccion()
        self.refrescar_modelos()
        self.after(100, self._vaciar_log)

    # ------------------------------------------------------------------ UI
    def _armar_panel_modelo(self):
        marco = ttk.LabelFrame(self, text="1. Modelo")
        marco.pack(fill="x", padx=10, pady=8)

        fila = ttk.Frame(marco)
        fila.pack(fill="x", padx=8, pady=6)
        ttk.Label(fila, text="Modelo guardado:").pack(side="left")
        self.combo_modelo = ttk.Combobox(fila, state="readonly", width=34)
        self.combo_modelo.pack(side="left", padx=6)
        ttk.Button(fila, text="Cargar", command=self.cargar_modelo).pack(side="left")
        self.etq_estado = ttk.Label(fila, text="Ningun modelo cargado", foreground="gray")
        self.etq_estado.pack(side="left", padx=10)

        fila = ttk.Frame(marco)
        fila.pack(fill="x", padx=8, pady=6)
        ttk.Label(fila, text="Generar nuevo:").pack(side="left")
        self.combo_arq = ttk.Combobox(fila, state="readonly", width=12, values=list(MODELOS))
        self.combo_arq.current(0)
        self.combo_arq.pack(side="left", padx=6)
        ttk.Label(fila, text="Experimento:").pack(side="left")
        self.var_exp = tk.StringVar(value="experimento_gui")
        ttk.Entry(fila, textvariable=self.var_exp, width=16).pack(side="left", padx=6)
        ttk.Label(fila, text="Epocas:").pack(side="left")
        self.var_epocas = tk.IntVar(value=10)
        ttk.Spinbox(fila, from_=1, to=200, textvariable=self.var_epocas, width=5).pack(side="left", padx=6)
        self.btn_entrenar = ttk.Button(fila, text="Generar modelo", command=self.generar_modelo)
        self.btn_entrenar.pack(side="left", padx=6)

        self.txt_log = tk.Text(marco, height=9, state="disabled", bg="#111", fg="#ddd",
                               font=("Consolas", 9))
        self.txt_log.pack(fill="x", padx=8, pady=(0, 8))

    def _armar_panel_prediccion(self):
        marco = ttk.LabelFrame(self, text="2. Prediccion")
        marco.pack(fill="both", expand=True, padx=10, pady=8)

        fila = ttk.Frame(marco)
        fila.pack(fill="x", padx=8, pady=6)
        ttk.Button(fila, text="Elegir imagen y predecir", command=self.elegir_imagen).pack(side="left")
        self.etq_ruta = ttk.Label(fila, text="", foreground="gray")
        self.etq_ruta.pack(side="left", padx=10)

        # Imagen vacia para que el Label mida LADO_VISTA px (sin imagen, width son caracteres)
        self._foto = tk.PhotoImage(width=LADO_VISTA, height=LADO_VISTA)
        self.lienzo = tk.Label(marco, image=self._foto, bg="#222")
        self.lienzo.pack(pady=6)

        self.etq_resultado = ttk.Label(marco, text="", font=("Segoe UI", 16, "bold"))
        self.etq_resultado.pack(pady=4)
        self.txt_top = tk.Text(marco, height=5, state="disabled", font=("Consolas", 10))
        self.txt_top.pack(fill="x", padx=8, pady=(0, 8))

    # ------------------------------------------------------------ modelos
    def refrescar_modelos(self, seleccionar=None):
        self.rutas_modelos = listar_modelos()
        etiquetas = list(self.rutas_modelos)
        self.combo_modelo["values"] = etiquetas
        if seleccionar in self.rutas_modelos:
            self.combo_modelo.set(seleccionar)
        elif etiquetas and not self.combo_modelo.get():
            self.combo_modelo.current(0)

    def cargar_modelo(self):
        etiqueta = self.combo_modelo.get()
        if not etiqueta:
            messagebox.showwarning("Sin modelo", "No hay modelo seleccionado. Genera uno primero.")
            return
        ruta = self.rutas_modelos[etiqueta]
        nombre = etiqueta.split(" / ")[1]
        self.etq_estado.config(text="Cargando...", foreground="orange")
        self.update_idletasks()
        self.modelo = keras.models.load_model(ruta)
        self.preprocess = MODELOS[nombre][1]
        self.img_size = tuple(self.modelo.input_shape[1:3])
        self.etq_estado.config(text=f"Cargado: {etiqueta}", foreground="green")

    def generar_modelo(self):
        if self.entrenando:
            return
        exp = self.var_exp.get().strip()
        if not exp:
            messagebox.showwarning("Experimento", "Escribe un nombre de experimento.")
            return
        nombre = self.combo_arq.get()
        epocas = self.var_epocas.get()
        self.entrenando = True
        self.btn_entrenar.config(state="disabled")
        threading.Thread(target=self._entrenar, args=(nombre, exp, epocas), daemon=True).start()

    def _entrenar(self, nombre, exp, epocas):
        # El entrenamiento corre en otro hilo para no congelar la ventana
        original = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = _Redirector(self.cola_log)
        try:
            trainer = CNNTrainer(dataset_dir=DATASET, output_dir=RESULTADOS,
                                 experimento=exp, max_epochs=epocas)
            trainer.entrenar_todos([nombre])
            self.cola_log.put(("FIN", f"{exp} / {nombre}"))
        except Exception as e:
            self.cola_log.put(f"\nERROR: {e}\n")
            self.cola_log.put(("FIN", None))
        finally:
            sys.stdout, sys.stderr = original

    def _vaciar_log(self):
        """Pasa los mensajes del hilo de entrenamiento al cuadro de texto (hilo de la GUI)."""
        try:
            while True:
                msg = self.cola_log.get_nowait()
                if isinstance(msg, tuple):  # ("FIN", etiqueta del modelo nuevo)
                    self.entrenando = False
                    self.btn_entrenar.config(state="normal")
                    self.refrescar_modelos(seleccionar=msg[1])
                    continue
                self.txt_log.config(state="normal")
                self.txt_log.insert("end", msg)
                self.txt_log.see("end")
                self.txt_log.config(state="disabled")
        except queue.Empty:
            pass
        self.after(100, self._vaciar_log)

    # --------------------------------------------------------- prediccion
    def elegir_imagen(self):
        if self.modelo is None:
            messagebox.showwarning("Sin modelo", "Carga un modelo primero.")
            return
        ruta = filedialog.askopenfilename(
            initialdir=DATASET,
            filetypes=[("Imagenes", "*.jpg *.jpeg *.png *.bmp *.webp"), ("Todos", "*.*")])
        if not ruta:
            return
        # np.fromfile + imdecode: cv2.imread falla con rutas con tildes en Windows
        imagen = cv2.imdecode(np.fromfile(ruta, dtype=np.uint8), cv2.IMREAD_COLOR)
        if imagen is None:
            messagebox.showerror("Imagen", "No se pudo leer la imagen.")
            return
        self.etq_ruta.config(text=os.path.basename(ruta))
        self._mostrar(imagen)
        self._predecir(imagen)

    def _mostrar(self, imagen_bgr):
        escala = LADO_VISTA / max(imagen_bgr.shape[:2])
        # INTER_NEAREST: los digitos son de 28x28 y se ven nitidos al ampliar
        vista = cv2.resize(imagen_bgr, None, fx=escala, fy=escala, interpolation=cv2.INTER_NEAREST)
        ok, png = cv2.imencode(".png", vista)
        self._foto = tk.PhotoImage(data=png.tobytes())
        self.lienzo.config(image=self._foto)

    def _predecir(self, imagen_bgr):
        # Mismo pipeline que el entrenamiento: RGB, resize, float32, preprocess_input del modelo
        rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)
        rgb = cv2.resize(rgb, self.img_size[::-1])  # cv2 recibe (ancho, alto)
        x = self.preprocess(rgb.astype(np.float32))[np.newaxis]
        probs = self.modelo.predict(x, verbose=0)[0]

        orden = np.argsort(probs)[::-1][:3]
        self.etq_resultado.config(
            text=f"Prediccion: {self.clases[orden[0]]}  ({probs[orden[0]] * 100:.1f}%)")
        self.txt_top.config(state="normal")
        self.txt_top.delete("1.0", "end")
        for i in orden:
            barra = "#" * int(probs[i] * 30)
            self.txt_top.insert("end", f"Clase {self.clases[i]:>2}  {probs[i] * 100:5.1f}%  {barra}\n")
        self.txt_top.config(state="disabled")


if __name__ == "__main__":
    App().mainloop()
