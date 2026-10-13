# Facial Analysis — Real-Time Multi-View

A single program (`facial_analysis.py`) that opens the webcam and shows a
2x2 grid of views, all built from the same live frame:

1. **Mirror** — plain flipped feed, exactly how you'd normally see yourself
   in a mirror.
2. **Face width** — draws a line across the cheekbones and shows the
   measured width in pixels.
3. **Face length** — draws a line from forehead to chin and shows the
   measured length in pixels.
4. **Face shape** — overlays the full 478-point face mesh and shows an
   estimated face shape plus the length/width ratio.

## How it works

### `face_metrics.py` (shared logic)

- Loads MediaPipe's `FaceLandmarker` (Tasks API) from the bundled model file
  `models/face_landmarker.task`, in `VIDEO` running mode so it can process a
  webcam stream frame by frame with timestamps.
- Each detected face gives 478 3D landmarks (normalized 0-1 coordinates).
  A handful of fixed landmark indices are used as anatomical reference
  points:
  - `10` forehead top, `152` chin bottom → **face length**
  - `234` / `454` left/right cheekbone → **face width**
  - `172` / `397` left/right jaw → **jaw width**, used for shape
- `measure_face()` converts those normalized points to pixel coordinates for
  the current frame size and computes Euclidean distances between them.
- `classify_face_shape()` applies a simple heuristic on the length/width
  ratio and the jaw-to-cheekbone width ratio to label the face as Oval,
  Round, Square, Oblong, or Heart/undefined. **This is a rough geometric
  approximation, not a medical or professional anthropometric measurement.**

### `facial_analysis.py` (main program)

- Captures frames from the default webcam, flips them horizontally (mirror
  effect), and runs `FaceLandmarker.detect_for_video()` on each frame.
- Builds the four tiles described above from the same frame + measurements,
  and stacks them into a 2x2 grid with `cv2.hconcat` / `cv2.vconcat`.
- Press `q` to close the window.

## Measurement units

Measurements are reported in **pixels**, not centimeters — a single camera
without depth or a size reference (e.g. a known-size object) can't recover
real-world scale. Distances are still meaningful for comparing proportions
(e.g. the length/width ratio) frame to frame.

## Run it

```
../../venv/Scripts/python.exe facial_analysis.py
```

or, with the venv activated:

```
python facial_analysis.py
```

## Model file

`models/face_landmarker.task` is Google's official pretrained MediaPipe
Face Landmarker model, downloaded from:
`https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task`

If the file is ever missing, re-download it to that path before running.
