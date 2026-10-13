"""Real-time facial analysis with multiple synchronized camera views.

Shows four tiles side by side, all fed from the same webcam frame:
  1. Mirror       - plain flipped view, how you normally see yourself
  2. Face width   - horizontal measurement across the cheekbones
  3. Face length  - vertical measurement from forehead to chin
  4. Face shape   - full landmark mesh + estimated face shape

Press 'q' to quit.
"""

import time

import cv2

from face_metrics import create_landmarker, measure_face
import mediapipe as mp

TILE_W, TILE_H = 480, 360


def label(img_bgr, text):
    cv2.putText(img_bgr, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 255, 0), 2, cv2.LINE_AA)
    return img_bgr


def draw_mirror_tile(frame):
    tile = cv2.resize(frame, (TILE_W, TILE_H))
    return label(tile, "Mirror (normal view)")


def draw_width_tile(frame, measurements):
    tile = cv2.resize(frame, (TILE_W, TILE_H))
    if measurements:
        lc = _scale_point(measurements["points"]["left_cheek"], frame, tile)
        rc = _scale_point(measurements["points"]["right_cheek"], frame, tile)
        cv2.line(tile, lc, rc, (255, 0, 255), 2)
        cv2.circle(tile, lc, 4, (255, 0, 255), -1)
        cv2.circle(tile, rc, 4, (255, 0, 255), -1)
        label(tile, f"Width: {measurements['width_px']:.0f}px")
    else:
        label(tile, "Width: no face")
    return tile


def draw_length_tile(frame, measurements):
    tile = cv2.resize(frame, (TILE_W, TILE_H))
    if measurements:
        fh = _scale_point(measurements["points"]["forehead"], frame, tile)
        ch = _scale_point(measurements["points"]["chin"], frame, tile)
        cv2.line(tile, fh, ch, (255, 255, 0), 2)
        cv2.circle(tile, fh, 4, (255, 255, 0), -1)
        cv2.circle(tile, ch, 4, (255, 255, 0), -1)
        label(tile, f"Length: {measurements['length_px']:.0f}px")
    else:
        label(tile, "Length: no face")
    return tile


def draw_shape_tile(frame, face_landmarks, measurements):
    tile = cv2.resize(frame, (TILE_W, TILE_H))
    if face_landmarks:
        for lm in face_landmarks[::3]:
            x = int(lm.x * TILE_W)
            y = int(lm.y * TILE_H)
            cv2.circle(tile, (x, y), 1, (0, 200, 255), -1)
    if measurements:
        label(tile, f"Shape: {measurements['shape']} (ratio {measurements['ratio']:.2f})")
    else:
        label(tile, "Shape: no face")
    return tile


def _scale_point(point_px, source_frame, target_tile):
    sh, sw = source_frame.shape[:2]
    th, tw = target_tile.shape[:2]
    x, y = point_px
    return int(x * tw / sw), int(y * th / sh)


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open the camera")

    landmarker = create_landmarker()
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # mirror, so it feels natural

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        timestamp_ms = int((time.time() - start_time) * 1000)
        result = landmarker.detect_for_video(mp_image, timestamp_ms)

        measurements = None
        face_landmarks = None
        if result.face_landmarks:
            face_landmarks = result.face_landmarks[0]
            h, w = frame.shape[:2]
            measurements = measure_face(face_landmarks, w, h)

        tile_mirror = draw_mirror_tile(frame)
        tile_width = draw_width_tile(frame, measurements)
        tile_length = draw_length_tile(frame, measurements)
        tile_shape = draw_shape_tile(frame, face_landmarks, measurements)

        top = cv2.hconcat([tile_mirror, tile_width])
        bottom = cv2.hconcat([tile_length, tile_shape])
        grid = cv2.vconcat([top, bottom])

        cv2.imshow("Facial analysis - multi view", grid)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    landmarker.close()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
