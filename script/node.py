#!/usr/bin/env python

import cv2
import numpy as np
import rospy
from sensor_msgs.msg import CompressedImage

VERBOSE = True


class LaneDetectionNode:
    def __init__(self, sub, detector):
        self.image_pub = rospy.Publisher("/output/lane_detection/compressed", CompressedImage)
        self.subscriber = rospy.Subscriber(sub, CompressedImage, self.callback, queue_size=1)
        self.detector = detector

    def callback(self, ros_data):
        # direct conversion to CV2
        np_arr = np.fromstring(ros_data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        lanes, shape = self.detector.get_lanes(image_np)
        mask_image = self.detector.draw_lanes(lanes, shape)

        # Create CompressedIamge
        msg = CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv2.imencode('.jpg', mask_image)[1]).tostring()
        # Publish new image
        self.image_pub.publish(msg)
