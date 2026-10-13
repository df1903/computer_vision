# Visión Artificial — Curso

Repo del curso de Visión Artificial (Python + OpenCV, Universidad de Caldas). Contiene los trabajos, retos y actividades evaluativas del curso, cada uno en su propia carpeta bajo `trabajos/`.

## Entorno

Un único venv y `requirements.txt` compartidos por todos los trabajos.

```
python -m venv venv
venv\Scripts\pip install -r requirements.txt
```

## Contenido

- `trabajos/01-deteccion-color-amarillo/` — detección de llama amarilla de estufa por color (HSV + contornos).
- `trabajos/02-espacios-color/` — comparación en vivo de espacios de color (RGB, HSV, LAB, LUV, YCrCb, XYZ).
- `trabajos/03-analisis-facial/` — análisis facial en tiempo real con MediaPipe (medidas y forma de rostro).
- `trabajos/04-filtros-morfologicos/` — bordes (Canny) + operaciones morfológicas ajustables en vivo.
- `trabajos/05-lector-pare-siga/` — lector de semáforo PARE/SIGA por color (HSV) + morfología + contornos.
- `material-clase/` — notebooks y diapositivas del profesor (ver su `README.md`).

## Estado del curso

| Corte | Alcance | Estado |
|---|---|---|
| 1 | Fundamentos → K-Means | Cerrado |
| 2 | CNN en adelante | Abierto |

Notas: K-Means y CNN viven como material de clase y contexto (`.context/curso/`), sin trabajo propio en `trabajos/` por ahora.

Cada trabajo tiene su propio `README.md` con detalle de cómo funciona y cómo correrlo.

## Para Claude Code

Ver `AGENTS.md` (fuente portable) y `CLAUDE.md` (import + notas de Claude Code). Contexto en `.context/`: temario del curso en `.context/curso/temario.md`, convenciones en `.context/conventions.md`.
