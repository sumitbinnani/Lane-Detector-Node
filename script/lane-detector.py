#!/usr/bin/env python

import argparse
import os
import sys

import cv2

# Set Python Path and Current Working Directory for Python
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR)
os.chdir(DIR)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lane Detection")
    parser.add_argument("--detector", dest="detector", help="lanenet", default="lanenet", type=str)
    parser.add_argument("--video", dest="video", help="input video file", default=None)
    parsed_args = parser.parse_args()
    assert parsed_args.detector.lower() in ["lanenet"]

    if parsed_args.detector.lower() == "lanenet":
        from detectors.lanenet_detector import LanenetLaneDetector
        detector = LanenetLaneDetector(y_range=[151, 256])

    if parsed_args.video:
        cap = cv2.VideoCapture(parsed_args.video)
        while cap.isOpened():
            ret, image = cap.read()
            lanes, shape = detector.get_lanes(image)
            detector.draw_lanes(lanes, shape)
        cap.release()