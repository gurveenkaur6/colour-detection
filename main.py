import numpy as np
import cv2

# Initialises video capture from the first available camera
cap = cv2.VideoCapture(0)

# To continously capture frames from the camera
while True:
    # ret returns a boolean value indicating if the frame was captured or not
    # frame is the captured image in the BGR color space
    ret, frame = cap.read() 

    # convert from BGR to HSV color space
    # HSV is prefered over RGB for color detection tasks because it separates color information (hue) from intensity (value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Returns a mask/binary mask ( a binary image that defines which pixels in the given image should be considered (white or 1) and which should be ignored (black or 0).)
    mask = cv2.inRange(hsv, )
    
    cv2.imshow('Frame', frame)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

# release the camera
cap.release()
cv2.destroyAllWindows()