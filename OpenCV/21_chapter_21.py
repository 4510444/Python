# How to detect specifics colours inside python

import cv2 as cv
import numpy as np

img = cv.imread("resources/Picture.jpg")

# Convert in hsu (hue,saturation,values)

hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

#Sliders
def slider():
    pass

path = "resources/Picture.jpg"

cv.namedWindow("Bars")
cv.resizeWindow("Bars",900,300)

cv.createTrackbar("Hue Min","Bars",0,179,slider)
cv.createTrackbar("Hue Max","Bars",179,179,slider)
cv.createTrackbar("Sat Min","Bars",0,255,slider)
cv.createTrackbar("Sat Max","Bars",255,255,slider)
cv.createTrackbar("Val Min","Bars",0,255,slider)
cv.createTrackbar("Val Max","Bars",255,255,slider)

img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min","Bars")
    hue_max = cv.getTrackbarPos("Hue Max","Bars")
    sat_min = cv.getTrackbarPos("Sat Min","Bars")
    sat_max = cv.getTrackbarPos("Sat Max","Bars")
    val_min = cv.getTrackbarPos("Val Min","Bars")
    val_max = cv.getTrackbarPos("Val Max","Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

    #To see these changes inside images
    lower = np.array(([hue_min,sat_min,val_min])) 
    Upper = np.array(([hue_max,sat_max,val_max]))
    mask_img = cv.inRange(hsv_img,lower,Upper)
    out_img = cv.bitwise_and(img,img,mask=mask_img) 

    cv.imshow("Orignal",img)
    cv.imshow("HSV Image",hsv_img)
    cv.imshow("Mask Image",mask_img)
    cv.imshow("Out Image",out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()




