import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("No se pudo abrir la camara")

TILE_W, TILE_H = 320, 240


def label(img_bgr, text):
    img = cv2.resize(img_bgr, (TILE_W, TILE_H))
    cv2.putText(img, text, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (0, 255, 0), 2, cv2.LINE_AA)
    return img


def to_bgr_3ch(single_channel_or_bgr):
    if len(single_channel_or_bgr.shape) == 2:
        return cv2.cvtColor(single_channel_or_bgr, cv2.COLOR_GRAY2BGR)
    return single_channel_or_bgr


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (TILE_W, TILE_H))

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    luv = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
    ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    xyz = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    tiles = [
        label(frame, "BGR (original)"),
        label(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), "RGB"),
        label(to_bgr_3ch(gray), "Grayscale"),
        label(hsv, "HSV"),
        label(hls, "HLS"),
        label(lab, "CIELAB"),
        label(luv, "CIELUV"),
        label(ycrcb, "YCrCb"),
        label(xyz, "XYZ"),
    ]

    row1 = np.hstack(tiles[0:3])
    row2 = np.hstack(tiles[3:6])
    row3 = np.hstack(tiles[6:9])
    grid = np.vstack([row1, row2, row3])

    cv2.imshow("Espacios de color - camara en vivo", grid)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
