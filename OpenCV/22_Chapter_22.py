# Face detection in images
import cv2 as cv


face_cascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

img = cv.imread("resources/Picture.jpg")

gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,1.1,4)

# Draw rectangle
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow("Orignal",img)
cv.waitKey(0)
cv.destroyAllWindows()