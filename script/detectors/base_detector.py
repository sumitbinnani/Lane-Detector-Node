try:
  from abc import ABC
except:
  from abc import ABCMeta as ABC
from abc import abstractmethod

import numpy as np

class LaneDetector(ABC):
    COLOR_MAP = [np.array([255, 0, 0]),
                 np.array([0, 255, 0]),
                 np.array([0, 0, 255]),
                 np.array([125, 125, 0]),
                 np.array([0, 125, 125]),
                 np.array([125, 0, 125]),
                 np.array([50, 100, 50]),
                 np.array([100, 50, 100])]

    @abstractmethod
    def get_lanes(self, img):
        pass
        
    @staticmethod
    def draw_lanes(lane_coords, shape):
        pass