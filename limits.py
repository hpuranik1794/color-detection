import cv2
import numpy as np

def get_limits(colour):
    c = np.uint8([[colour]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower = hsvC[0][0][0] - 10, 100, 100
    upper = hsvC[0][0][0] - 10, 255, 255

    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)

    return lower, upper