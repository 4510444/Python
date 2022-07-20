# How To Capture webcame in python

# Step-1 Import libraries

import cv2 as cv
import numpy as np
# Step-2 Read the frames from camera

cap = cv.VideoCapture(0)    # Webcame No. 1

# if (cap.isOpened() == False):
#     print("There is an error")

# Read Untill the End
# Display the camera frame by frame
while (cap.isOpened()): 
    ret , frame = cap.read()
    if ret == True:
        cv.imshow("Frame", frame)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
# Release and Close windows easily
cap.release()
cv.destroyAllWindows()