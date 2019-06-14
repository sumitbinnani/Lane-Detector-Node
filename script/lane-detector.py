#!/usr/bin/env python

import argparse
import os
import sys

# Set Python Path and Current Working Directory for Python
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR)
os.chdir(DIR)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lane Detection")
    parser.add_argument("--detector", dest="detector", help="lanenet", default="lanenet", type=str)
    parser.add_argument("--subscriber", dest="subscriber", help="video/node", default='node', type=str)
    parser.add_argument("--name", dest="name", help="path to video or the node to be subscribed")
    parsed_args = parser.parse_args()

    assert parsed_args.detector.lower() in ["lanenet"]
    assert parsed_args.subscriber.lower() in ["node", "video"]

    if parsed_args.detector.lower() == "lanenet":
        from detectors.lanenet_detector import LanenetLaneDetector
        detector = LanenetLaneDetector(y_range=[151, 256])

    if parsed_args.subscriber.lower() == "video":
        import cv2
        cap = cv2.VideoCapture(parsed_args.name)
        while cap.isOpened():
            ret, image = cap.read()
            lanes, shape = detector.get_lanes(image)
            mask_image = detector.draw_lanes(lanes, shape)
            cv2.imshow('frame', mask_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit()
        cap.release()

    else:
        import rospy
        from node import LaneDetectionNode
        lane_detector_node = LaneDetectionNode(parsed_args.name, detector)
        rospy.init_node('Lane_Detector', anonymous=True)
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down ROS Lane Detector Module")
