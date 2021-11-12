import cv2 as cv
import numpy as np

drawing = False  # true if mouse is pressed
mode =  True    # if True, draw rectangle.
ix, iy = -1, -1

fontFace = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
rectagle =0
circle =0
<<<<<<< Updated upstream
square=0
=======
>>>>>>> Stashed changes
# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode,rectagle,circle
    if event == cv.EVENT_LBUTTONDBLCLK:
        drawing = False
        ix, iy = x, y
        if mode == True:
            rectagle+=1
            cv.rectangle(img, (ix, iy), (x+100, y+100), (0, 255, 0), -1)
            cv.putText(img,str(rectagle),(x,y),fontFace,2,(255,255,255))
    if event == cv.EVENT_RBUTTONDBLCLK:
            drawing = False
            ix, iy= x, y
            circle +=1
            if mode == True:
                cv.circle(img,(ix, iy),30,(0,0,255),None)
                cv.putText(img, str(circle), (x, y), fontFace, 2, (255, 255, 255))

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)


while True:
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()