import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rectagle = 0
circle = 0
selected_points = []
def MouseCallback(event, x, y, flags, param):
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
    global rectagle, circle
    if event == cv2.EVENT_LBUTTONUP:
            rectagle+=1
            cv2.rectangle(img, (x, y), (x+50, y+50), (255, 0, 0), cv2.FILLED) #COLOUR  BGR in OPENCV
            cv2.putText(img,"Rectangle: "+str(rectagle),(x,y),fontFace,2,(255,255,255))
    if event == cv2.EVENT_RBUTTONUP : #idicates that the right  mouse button is released
            circle +=1
            cv2.circle(img,(x, y),30,(0,0,255),cv2.FILLED)#COLOR  BGR in OpenCV
            cv2.putText(img, "Circle: "+str(circle), (x, y), fontFace, 2, (255, 255, 255))
    if event==cv2.EVENT_LBUTTONDBLCLK:
        selected_points.append([x,y]) #POLISH wczytuje wspolrzedne punktow na ktore nacisne
        print(selected_points)
img = np.zeros((512, 512, 3), np.uint8) #create a black image, a window bind the function to window
cv2.namedWindow('image')
cv2.setMouseCallback('image', MouseCallback)
path = "road.jpg"
img2 = cv2.imread(path)
cv2.namedWindow('Straightening')
Size=(1920,1080)
img2 = cv2.resize(img2,Size,interpolation=cv2.INTER_AREA)
cv2.setMouseCallback('Straightening', MouseCallback)

img3 = cv2.imread('baby_yoda.jpg',0)
equalization_img = cv2.equalizeHist(img3)
histogram_img = cv2.calcHist([equalization_img],[0],None,[256],[0,256])
histogram_img2 = cv2.calcHist([img3],[0],None,[256],[0,256])
plt.plot(histogram_img2); plt.show()
while True:
    cv2.imshow('image',img)
    cv2.imshow('Straightening',img2)
    cv2.imshow('Histogram',equalization_img)
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