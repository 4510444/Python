#How to change the prespective of the images
import cv2 as cv
import numpy as np

img = cv.imread("resources/wrap.png")
print(img.shape)  # (900,800,3)

# Defining Points

point1 = np.float32([[233,196],[82,471],[522,169],[715,482]])
width =  800
height = 900
point2 = np.float32([[0,0],[800,0],[0,900],[800,900]])


matrix = cv.getPerspectiveTransform(point1,point2)
out_img = cv.warpPerspective(img,matrix,(width,height))

cv.imshow("Orignal",img)
cv.imshow("Transformed",out_img)
cv.waitKey(0)
cv.destroyAllWindows()