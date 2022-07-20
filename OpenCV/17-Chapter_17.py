# Joining two images

import cv2 as cv
import numpy as np

img = cv.imread("resources/Picture.jpg")

# Stacking the same image

# 1- Horizontal stack
hor_img = np.hstack((img,img))

# 2- Vertical stack
ver_img = np.vstack((img,img))


# cv.imshow("Horizontal",hor_img)
cv.imshow("Vertical",ver_img)
cv.waitKey(0)
cv.destroyAllWindows()




# you have to define a function to stack multiple images of different sizes and tunes
# To use np function the no. of channels should be same