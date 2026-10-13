"""Detect a gas stove's yellow flame in a video file.

Usage:
    python detect_yellow_video.py <path_to_video>

Press 'q' to quit.
"""

import argparse

import cv2

from yellow_detector import annotate_frame, build_mask, mask_to_bgr


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video_path", help="Path to the input video file")
    return parser.parse_args()


def main():
    args = parse_args()

    cap = cv2.VideoCapture(args.video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {args.video_path}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        mask = build_mask(frame)
        annotated, _ = annotate_frame(frame, mask)

        view = cv2.hconcat([annotated, mask_to_bgr(mask)])
        cv2.imshow("Stove flame detection (video)", view)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
