import cv2
import numpy as np
from time import perf_counter
def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass
def filter2D():
    path="baby_yoda.jpg"
    img=cv2.imread(path,0)
    nameWindow='Standard photo in colour grey'
    nameWindow1='Sobel mask x'
    nameWindow2='Sobel mask y'
    cv2.namedWindow(nameWindow)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)/4
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)/4
    print('Max value of SobelX: ',np.max(sobelx))
    print('Max value of SobelY: ',np.max(sobely))
    np.abs(sobelx).astype(np.uint8)
    module=np.sqrt(sobelx ** 2 + sobely ** 2)
    module=np.sqrt(pow(sobelx,2) + pow(sobely,2))

    print('Max value of module: ',np.max(module))
    while True:
        cv2.imshow(nameWindow,img)
        cv2.imshow(nameWindow1,np.abs(sobelx).astype(np.uint8))
        cv2.imshow(nameWindow2, np.abs(sobely).astype(np.uint8))
        cv2.imshow('Module',module.astype(np.uint8))
        key_code=cv2.waitKey(1)
        if key_code==27:
            break
def Canny():
    path="baby_yoda.jpg"
    img= cv2.imread(path,0)
    cv2.namedWindow('Canny algorithm')
    cv2.createTrackbar('LowRange','Canny algorithm',0,100,empty_callback)
    cv2.createTrackbar('MaxRange', 'Canny algorithm', 0, 100, empty_callback)
    while True:
        low,high=cv2.getTrackbarPos('LowRange','Canny algorithm'),cv2.getTrackbarPos('MaxRange','Canny algorithm')
        canny=cv2.Canny(img,low,high)
        cv2.imshow('Canny algorithm',canny)
        key_code=cv2.waitKey(1)
        if key_code==27:
            exit()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filter2D()
    Canny()