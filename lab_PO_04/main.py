import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rectagle = 0
circle = 0
selected_points = []
selected_points2=[]
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
        selected_points.append([x,y])#POLISH wczytuje wspolrzedne punktow na ktore nacisne
        selected_points2.append([x,y])
        print(selected_points2)
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

img4 = cv2.imread('pug.png', 1)
img5 = cv2.imread('gallery.png', 1)
height_pug, width_pug = img4.shape[0], img4.shape[1]
print('Height of pug: ',height_pug)
cv2.namedWindow('Gallery')
cv2.setMouseCallback('Gallery',MouseCallback)
while True:
    cv2.imshow('image',img)
    cv2.imshow('Straightening',img2)
    cv2.imshow('Histogram',equalization_img)
    cv2.imshow('Gallery',img5)
    key_code = cv2.waitKey(100)
    if key_code == 27:
        break
    if len(selected_points) == 4:
        pts1 = np.float32(selected_points)
        pts2 = np.float32([[0,0],[900,0],[0,900],[900,900]])
        perspective = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(img2,perspective,(900,900))
        cv2.imshow('Result of Straightening',dst)
    if len(selected_points2)==4:
        pts11 = np.float32([[0,0],[width_pug,0],[0,height_pug],[width_pug,height_pug]])
        pts22 = np.float32(selected_points2)
        M = cv2.getPerspectiveTransform(pts11,pts22)
        dst = cv2.warpPerspective(img4,M,(img5.shape[1],img5.shape[0]))
        ret,mask=cv2.threshold(dst,0,255,cv2.THRESH_BINARY)
        img5[mask!=0]=0
        img6 = dst+img5
        cv2.imshow('Mops in gallery',img6)


cv2.destroyAllWindows()