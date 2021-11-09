import cv2
import numpy as np

rectagle = 0
circle = 0
# mouse callback function
def MouseCallback(event, x, y, flags, param):
    ix, iy = 0,0
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
    global rectagle, circle
    if event == cv2.EVENT_LBUTTONUP : #idicates that the left mouse button is released
            ix, iy = x, y
            rectagle+=1
            cv2.rectangle(img, (ix, iy), (x+100, y+100), (255, 0, 0), cv2.FILLED) #COLOUR  BGR in OPENCV
            cv2.putText(img,"Rectangle: "+str(rectagle),(x,y),fontFace,2,(255,255,255))
    if event == cv2.EVENT_RBUTTONUP : #idicates that the right  mouse button is released
            ix, iy= x, y
            circle +=1
            cv2.circle(img,(ix, iy),30,(0,0,255),cv2.FILLED)#COLOR  BGR in OpenCV
            cv2.putText(img, "Circle: "+str(circle), (x, y), fontFace, 2, (255, 255, 255))

img = np.zeros((512, 512, 3), np.uint8) #create a black image, a window bind the function to window
cv2.namedWindow('image')
cv2.setMouseCallback('image', MouseCallback)
while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
       break
def Straightening():
    path="road.jpg"
    img=cv2.imread(path,1)
    cv2.namedWindow('Straightening')
    dsize=(1920,1080)
    img_scaled=cv2.resize(img,dsize,interpolation=cv2.INTER_AREA)
    height=img_scaled.shape[0]
    width=img_scaled.shape[1]
    while True:
        cv2.imshow('Straightening',img_scaled)
        k=cv2.waitKey(1)
        if k==27:
           exit()

if __name__=="__main__":
    Straightening()
    cv2.destroyAllWindows()
