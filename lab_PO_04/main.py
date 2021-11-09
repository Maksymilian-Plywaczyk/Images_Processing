import cv2 as cv
import numpy as np

rectagle = 0
circle = 0
# mouse callback function
def MouseCallback(event, x, y, flags, param):
    ix, iy = 0,0
    fontFace = cv.FONT_HERSHEY_COMPLEX_SMALL
    global rectagle, circle
    if event == cv.EVENT_LBUTTONUP : #idicates that the left mouse button is released
            ix, iy = x, y
            rectagle+=1
            cv.rectangle(img, (ix, iy), (x+100, y+100), (255, 0, 0), cv.FILLED) #COLOUR  BGR in OPENCV
            cv.putText(img,"Rectangle: "+str(rectagle),(x,y),fontFace,2,(255,255,255))
    if event == cv.EVENT_RBUTTONUP : #idicates that the right  mouse button is released
            ix, iy= x, y
            circle +=1
            cv.circle(img,(ix, iy),30,(0,0,255),cv.FILLED)#COLOR  BGR in OpenCV
            cv.putText(img, "Circle: "+str(circle), (x, y), fontFace, 2, (255, 255, 255))

img = np.zeros((512, 512, 3), np.uint8) #create a black image, a window bind the function to window
cv.namedWindow('image')
cv.setMouseCallback('image', MouseCallback)
while True:
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        exit()
cv.destroyAllWindows()
