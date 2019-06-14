#!/usr/bin/env python

import os
import sys

# Set Python Path and Current Working Directory for Python
DIR = os.path.dirname(__file__)
sys.path.append(DIR)
os.chdir(DIR)


from detectors.base_detector import LaneDetector

