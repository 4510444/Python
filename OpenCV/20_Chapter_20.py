# Split your videos into frames
import cv2 as cv

cap = cv.VideoCapture("resources/saeed.mp4")

frameNo = 0

while (True):
    ret,frame = cap.read()
    if ret:
        cv.imwrite(f"resources/frames/frame_{frameNo}.jpg",frame)
    else:
        break
    frameNo = frameNo+1

cap.release()