"""Shared yellow-flame detection logic used by the camera and video scripts."""

import cv2
import numpy as np

# HSV range tuned for the yellow/orange flame of a gas stove burner.
# OpenCV hue goes 0-179, so this covers the yellow band.
LOWER_YELLOW = np.array([15, 90, 120])
UPPER_YELLOW = np.array([35, 255, 255])

MIN_CONTOUR_AREA = 200


def build_mask(frame_bgr):
    hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((5, 5), np.uint8))
    return mask


def find_yellow_regions(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return [c for c in contours if cv2.contourArea(c) >= MIN_CONTOUR_AREA]


def annotate_frame(frame_bgr, mask):
    output = frame_bgr.copy()
    regions = find_yellow_regions(mask)

    detected = len(regions) > 0
    for contour in regions:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 255), 2)

    status = "STOVE FLAME DETECTED" if detected else "no yellow flame"
    color = (0, 0, 255) if detected else (200, 200, 200)
    cv2.putText(output, status, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                color, 2, cv2.LINE_AA)

    return output, detected


def mask_to_bgr(mask):
    return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
