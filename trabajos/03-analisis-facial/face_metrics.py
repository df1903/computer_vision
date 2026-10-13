"""Shared face landmark detection and measurement logic.

Uses MediaPipe's FaceLandmarker (Tasks API) to get 478 3D face landmarks per
frame, then derives simple geometric measurements (face width, face length,
approximate face shape) from a handful of reference points.
"""

import math
import os

import mediapipe as mp
from mediapipe.tasks.python import vision as mp_vision

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "face_landmarker.task")

# Landmark indices from MediaPipe's 468-point face mesh topology.
FOREHEAD_TOP = 10       # top of the forehead / hairline
CHIN_BOTTOM = 152       # bottom of the chin
LEFT_CHEEK = 234        # left face contour, cheekbone height
RIGHT_CHEEK = 454       # right face contour, cheekbone height
LEFT_JAW = 172          # left jaw line
RIGHT_JAW = 397         # right jaw line


def create_landmarker(running_mode=mp_vision.RunningMode.VIDEO):
    base_options = mp.tasks.BaseOptions(model_asset_path=MODEL_PATH)
    options = mp_vision.FaceLandmarkerOptions(
        base_options=base_options,
        running_mode=running_mode,
        num_faces=1,
    )
    return mp_vision.FaceLandmarker.create_from_options(options)


def _point(landmarks, index, width, height):
    lm = landmarks[index]
    return lm.x * width, lm.y * height


def _distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def classify_face_shape(length, width, jaw_width):
    """Rough heuristic classification, not a medical/anthropometric measure."""
    ratio = length / width if width else 0
    jaw_to_cheek = jaw_width / width if width else 0

    if ratio >= 1.55:
        return "Oblong"
    if jaw_to_cheek >= 0.95 and ratio < 1.25:
        return "Square"
    if ratio < 1.15 and jaw_to_cheek < 0.9:
        return "Round"
    if ratio >= 1.25:
        return "Oval"
    return "Heart / undefined"


def measure_face(face_landmarks, width, height):
    """Return a dict with pixel measurements and shape classification."""
    forehead = _point(face_landmarks, FOREHEAD_TOP, width, height)
    chin = _point(face_landmarks, CHIN_BOTTOM, width, height)
    left_cheek = _point(face_landmarks, LEFT_CHEEK, width, height)
    right_cheek = _point(face_landmarks, RIGHT_CHEEK, width, height)
    left_jaw = _point(face_landmarks, LEFT_JAW, width, height)
    right_jaw = _point(face_landmarks, RIGHT_JAW, width, height)

    face_length = _distance(forehead, chin)
    face_width = _distance(left_cheek, right_cheek)
    jaw_width = _distance(left_jaw, right_jaw)
    shape = classify_face_shape(face_length, face_width, jaw_width)

    return {
        "length_px": face_length,
        "width_px": face_width,
        "jaw_width_px": jaw_width,
        "ratio": face_length / face_width if face_width else 0,
        "shape": shape,
        "points": {
            "forehead": forehead,
            "chin": chin,
            "left_cheek": left_cheek,
            "right_cheek": right_cheek,
            "left_jaw": left_jaw,
            "right_jaw": right_jaw,
        },
    }
