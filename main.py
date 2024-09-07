import numpy as np
import cv2

# Initialises video capture from the first available camera
cap = cv2.VideoCapture(0)

# To continously capture frames from the camera
while True:
    # ret returns a boolean value indicating if the frame was captured or not
    # frame is the captured image in the BGR color space
    ret, frame = cap.read() 

    cv2.imshow('Frame', frame)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

# release the camera
cap.release()
cv2.destroyAllWindows()