# How to draw lines, shapes in python
import cv2 as cv
import numpy as np

# Darw a Canvas
img = np.zeros((600,600)) # 0 for Black  
# img1 = np.ones((600,600)) # 1 for white


# Print Size
print("The size of our canvas is:",img.shape)
print(img)

# Adding Colors to the canvas
colored_img = np.zeros((600,600,3), np.uint8)
colored_img[:] = 255,0,255                       # Colour on Complete image
colored_img[150:200, 100:200] = 255,168,155      # Part of image to be coloured


# cv.line(colored_img,(0,0),(600,600),(255,0,0),3)                                    # Adding Line
cv.line(colored_img,(0,0), (colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)   # Adding Line


# Adding Rectangle
# cv.rectangle(colored_img,(200,300),(400,500),(255,165,376), 3)           # 3 is line thickness of rectangle
cv.rectangle(colored_img,(200,300),(400,500),(255,165,376), cv.FILLED)   # Filling inside a Rectangle

# Adding Circle
# cv.circle(colored_img,(300,300),100,(135,0,243),5)
cv.circle(colored_img,(300,300),100,(135,0,243),cv.FILLED)

# Adding Text
cv.putText(colored_img,"Python ka Chilla with Ammar",(100,200),cv.FONT_HERSHEY_DUPLEX,1,(255,324,123),2)


# cv.imshow("Black", img)
cv.imshow("Colored Image", colored_img)
cv.waitKey(0) & 0xFF == ord("q")
cv.destroyAllWindows()