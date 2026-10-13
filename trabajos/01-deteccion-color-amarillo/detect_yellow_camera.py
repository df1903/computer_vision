"""Detect a gas stove's yellow flame live from the PC webcam.

Press 'q' to quit.
"""

import cv2

from yellow_detector import annotate_frame, build_mask, mask_to_bgr

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Could not open the camera")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    mask = build_mask(frame)
    annotated, _ = annotate_frame(frame, mask)

    view = cv2.hconcat([annotated, mask_to_bgr(mask)])
    cv2.imshow("Stove flame detection (camera)", view)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
