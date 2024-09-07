import numpy as np
import cv2

def get_limits(color):
    "Returns the lower and upper HSV color limits for a given BGR color"

    c = np.uint8([color])
    # convert BGR to HSV 
    hsvc = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # extract the hue value from the hsvc. Hue represents color, saturation -> intensity and value -> brightness
    hue = hsvc[0][0][0]

    # red hue wrap around issue
    # hue is represented as a circle and it is at both the ends(0 and 360 degree) of the circle.
    # in OpenCV, hue ranges from 0 - 180 degree, so red appears at both ends of this range.

    if hue >= 165:  # If the hue is ≥ 165, it's treating it as the upper part of the red range.
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)

    elif hue <= 15:  #If the hue is ≤ 15, it's treating it as the lower part of the red range.
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit