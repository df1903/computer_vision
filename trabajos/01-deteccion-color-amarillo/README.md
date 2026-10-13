# Task 1 — Stove Yellow Flame Detection

Two small OpenCV programs that detect the yellow flame a gas stove produces
when it's turned on. Both share the same detection logic (`yellow_detector.py`)
and only differ in where the video frames come from.

## How the detection works (`yellow_detector.py`)

1. Convert each BGR frame to HSV. Color-based detection is far more robust
   in HSV than in RGB/BGR because Hue isolates the color itself from
   brightness and lighting changes.
2. `cv2.inRange` thresholds the HSV frame against `LOWER_YELLOW` /
   `UPPER_YELLOW` (hue ~15-35, with minimum saturation/value) to build a
   binary mask of yellow pixels — this is the flame's color band.
3. Morphological opening removes small noise specks, then dilation fills
   small gaps in the flame blob.
4. `cv2.findContours` finds the connected yellow regions on the mask, and
   any region smaller than `MIN_CONTOUR_AREA` is discarded as noise.
5. `annotate_frame` draws a bounding box around each remaining region and
   overlays a "STOVE FLAME DETECTED" label when at least one region survives.

Both scripts show the annotated frame side by side with the raw mask, so you
can see exactly what pixels are being classified as "yellow".

## `detect_yellow_camera.py`

Opens the PC's default webcam (`cv2.VideoCapture(0)`) and runs the detection
loop live, frame by frame.

Run it with:

```
python detect_yellow_camera.py
```

Press `q` to close the window.

## `detect_yellow_video.py`

Same detection pipeline, but the frame source is a video file passed as a
command-line argument instead of the webcam.

Run it with:

```
python detect_yellow_video.py path/to/video.mp4
```

Press `q` to stop playback early.

## Notes / tuning

- The HSV range in `yellow_detector.py` is a starting point tuned for a
  typical yellow/orange flame. If detection is too strict or too loose for
  your footage (different lighting, camera, or stove), adjust
  `LOWER_YELLOW` / `UPPER_YELLOW`.
- `MIN_CONTOUR_AREA` filters out small yellow specks (reflections, etc.).
  Raise it if you get false positives, lower it if small flames are missed.
