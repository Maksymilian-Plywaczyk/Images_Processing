import cv2 as cv
import numpy as np

drawing = False  # true if mouse is pressed
mode =  True    # if True, draw rectangle.
ix, iy = -1, -1

fontFace = "FONT_HERSHEY_SCRIPT_SIMPLEX"


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDBLCLK:
        drawing = False
        ix, iy = x, y
        if mode == True:
            cv.rectangle(img, (ix, iy), (x+100, y+100), (0, 255, 0), -1)
    if event == cv.EVENT_RBUTTONDBLCLK:
            drawing = False
            ix, iy= x, y
            if mode == True:
                cv.circle(img,(ix, iy),30,(0,0,255),None)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while True:
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()