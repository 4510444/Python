# Basic functions or manipulations in OpenCV
import cv2 as cv

img = cv.imread("resources/Picture.jpg")

# Resize
#resized_img = cv.resize(img,(450,250))    # 1st one is the width and 2nd one is the height

# Gray image
# gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Blurr Image
# blur_img = cv.GaussianBlur(img,(7,7),0)

# Black/White Image
# thresh, binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# Edge Detection
# edge_img = cv.Canny(img,48,48)q

# Thickness of lines
# dilated_img = cv.dilate(edge_img,(7,7),iterations=1)

# Make Thinner Outline
# erod_img = cv.erode(dilated_img,(7,7),iterations=1)

# Cropping (We will use numpy no open cv )
print("The shape of our image is:", img.shape)
crop_img = img[0:200, 200:300]


cv.imshow("Orignal",img)
# cv.imshow("Resised",resized_img)
# cv.imshow("Gray Image",gray_img)
# cv.imshow("B/W Image",binary)
# cv.imshow("Blur Image",blur_img)
# cv.imshow("edge Image", edge_img)
# cv.imshow("dilated Image", dilated_img)
# cv.imshow("Erode Image", erod_img)
cv.imshow("Crop Image",crop_img)
cv.waitKey(0) & 0xFF == ord("q")
cv.destroyAllWindows()