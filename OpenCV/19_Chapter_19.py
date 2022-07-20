# Coordinates of audio or video

# Step-1 (import Libraries)
import cv2 as cv
import numpy as np

# Step-2 (Defining a Function)

def find_cordinates(event,x,y,flags,paramns):
    if event == cv.EVENT_FLAG_LBUTTON:   
        # left mouse click         
        print(x,'',y)
        # How to print on the same image 
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x)+ ','+ str(y),(x,y),font,1, (255,0,0),2)
        # Show the text on the image
        cv.imshow("Image",img)
    if event == cv.EVENT_RBUTTONDOWN:
        print(x,'',y)
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        cv.putText(img, str(b)+','str(g)+','str(r), (x,y), font, 1, (255,167,243), 2)
        cv.imshow("Image",img)



# Final Function to read and display
if __name__ == "__main__":
    # Reading an image
    img = cv.imread("resources/Picture.jpg",1)
    # Displaying an image
    cv.imshow("Image",img)
    # Setting callback function
    cv.setMouseCallback("Image",find_cordinates)
    cv.waitKey(0)
    cv.destroyAllWindows()