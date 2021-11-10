import cv2
import numpy as np

rectagle = 0
circle = 0
selected_points = []
# mouse callback function
def MouseCallback(event, x, y, flags, param):
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
    global rectagle, circle
    if event == cv2.EVENT_LBUTTONUP : #idicates that the left mouse button is released
            rectagle+=1
            cv2.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), cv2.FILLED) #COLOUR  BGR in OPENCV
            cv2.putText(img,"Rectangle: "+str(rectagle),(x,y),fontFace,2,(255,255,255))
    if event == cv2.EVENT_RBUTTONUP : #idicates that the right  mouse button is released
            circle +=1
            cv2.circle(img,(x, y),30,(0,0,255),cv2.FILLED)#COLOR  BGR in OpenCV
            cv2.putText(img, "Circle: "+str(circle), (x, y), fontFace, 2, (255, 255, 255))
    if event==cv2.EVENT_LBUTTONDBLCLK:
        selected_points.append([x,y]) #POLISH wczytuje wspolrzedne punktow na ktore nacisne
        print(selected_points)


img = np.zeros((512, 512, 3), np.uint8) #create a black image, a window bind the function to window
#cv2.namedWindow('image')
#cv2.setMouseCallback('image', MouseCallback)

path = "road.jpg"
img2 = cv2.imread(path)
cv2.namedWindow('Straightening')
img2 = cv2.resize(img2, None,fx=0.5,fy=0.5)
cv2.setMouseCallback('Straightening', MouseCallback)

while True:
    #cv2.imshow('image',img)
    cv2.imshow('Straightening',img2)
    key_code = cv2.waitKey(100)
    if key_code == 27:
        break
    if len(selected_points) == 4:
        pts1 = np.float32(selected_points)
        pts2 = np.float32([[0,0],[900,0],[0,900],[900,900]])
        perspective = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(img2,perspective,(900,900))
        cv2.imshow('Result of Straightening',dst)

cv2.destroyAllWindows()
