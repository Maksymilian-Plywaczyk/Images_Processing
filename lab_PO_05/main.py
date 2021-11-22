import cv2
import imageio
import numpy as np
from time import perf_counter
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter
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
            break
def DetectingLinesCircle():
    path='shapes.jpg'
    img=cv2.imread(path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur_gray=cv2.GaussianBlur(gray,(5,5),0) #0=sigmaY
    canny=cv2.Canny(blur_gray,50,150)
    blurred=cv2.medianBlur(gray,25)
    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 1 # minimum number of pixels making up a line
    max_line_gap = 12  # maximum gap in pixels between connectable line segments
    lines = cv2.HoughLinesP(canny, rho,theta, threshold, np.array([]),
        min_line_length, max_line_gap)
    circles=cv2.HoughCircles(blurred,cv2.HOUGH_GRADIENT,dp=1,minDist=30,param1=10,param2=50,
        minRadius=0,maxRadius=100)
    #minRadius=0,maxRadius=0 algorytm sam okresla maksymalny i minimalny promien okregu.
    circles = np.uint16(np.around(circles))
    count =0
    for line in lines:
      for x1,y1,x2,y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        print('Start line: ',(x1,y1),'End line: ',(x2,y2))
    for circle in circles[0,:]:
        cv2.circle(img,(circle[0],circle[1]),circle[2],(255,0,0),2)
        print('X coordinate:  ',circle[0],'Y coorditate: ',circle[1],'Radians: ',circle[2])
        count +=1
        print(count)
        cv2.putText(img,'Circle: '+str(count),(circle[0],circle[1]),cv2.FONT_HERSHEY_SIMPLEX
        ,0.7,(255,0,0),2)
    while True:
        cv2.imshow('Result',img)
        key_code=cv2.waitKey(1)
        if key_code==27:
            break
def PlatformDronLines():
   path='drone_ship.jpg'
   img=cv2.imread(path)
   img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   gaussian_blur=cv2.GaussianBlur(img_gray,(13,13),0)
   median_blur=cv2.medianBlur(img_gray,5)
   canny_gaussian=cv2.Canny(gaussian_blur,100,200)#mozna pozmieniac progi wykrywania krawedzi
   canny2_median=cv2.Canny(median_blur,50,150)
   rho = 1  # distance resolution in pixels of the Hough grid
   theta = np.pi / 180  # angular resolution in radians of the Hough grid
   threshold = 10  # minimum number of votes (intersections in Hough grid cell)
   min_line_length = 1  # minimum number of pixels making up a line
   max_line_gap = 12  # maximum gap in pixels between connectable line segments
   lines = cv2.HoughLinesP(canny_gaussian, rho, theta, threshold, np.array([]),
     min_line_length, max_line_gap)
   for line in lines:
       for x1, y1, x2, y2 in line:
           cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
           print('Start line: ', (x1, y1), 'End line: ', (x2, y2))
   while True:
       cv2.imshow('Result', canny_gaussian)
       cv2.imshow('Result2',canny2_median)
       cv2.imshow('Patform',img)
       key_code = cv2.waitKey(1)
       if key_code == 27:
           break

def CoinDetected():
    path='coins.jpg'
    img=cv2.imread(path)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussianblur=cv2.GaussianBlur(img_gray,(13,13),0)
    circles=cv2.HoughCircles(gaussianblur,cv2.HOUGH_GRADIENT,dp=1,minDist=50,param1=10,param2=50,
        minRadius=50,maxRadius=107)
    circles=np.uint16(np.around(circles))
    radius = []
    for circle in circles[0,:]:
        cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)
        print('X coordinate:  ', circle[0], 'Y coorditate: ', circle[1]
        , 'Radians: ', circle[2])
        radius.append([circle[2]])
        print(radius)
    largest=max(radius)
    print(largest)
    count =0
    count2=0
    value = []
    for coin in circles[0,:]:
        if coin[2]<=53:
            count+=1
            cv2.putText(img, '10 groszy: ' + str(count), (coin[0],coin[1]), cv2.FONT_HERSHEY_SIMPLEX
                        , 0.7, (255, 0, 0), 2)
            value.append(0.1)
        if coin[2]==largest:
            count2+=1
            cv2.putText(img, '1 zlotowka: ' + str(count2), (coin[0], coin[1]), cv2.FONT_HERSHEY_SIMPLEX
                        , 0.7, (0, 255, 0), 2)
            value.append(1)
    money=sum(value)
    sum_of_money=np.around(money,1)
    print('Suma zebranych pieniedzy: ',sum_of_money,'zl')
    cv2.putText(img,'Suma zebranych pieniedzy: '+str(sum_of_money)+'zl',(20,20),cv2.FONT_HERSHEY_SIMPLEX
                        , 0.7, (255, 0, 0), 2)
    while True:
        cv2.imshow('Result',img)
        key_code=cv2.waitKey(1)
        if key_code==27:
            break
def FruitDetection():
    path='fruit.jpg'
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianblur = cv2.GaussianBlur(img_gray, (13, 13), 0)
    circles = cv2.HoughCircles(gaussianblur, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=10, param2=50,
                               minRadius=100, maxRadius=200)
    circles = np.uint16(np.around(circles))
    radius=[]
    for circle in circles[0, :]:
        cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)
        print('X coordinate:  ', circle[0], 'Y coorditate: ', circle[1]
              , 'Radians: ', circle[2])
        radius.append([circle[2]])
        print(radius)
    while True:
        cv2.imshow('GaussianBlur',gaussianblur)
        cv2.imshow('Result', img)
        key_code = cv2.waitKey(1)
        if key_code == 27:
            exit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # filter2D()
    # Canny()
    # DetectingLinesCircle()
    # PlatformDronLines()
    #CoinDetected()
    FruitDetection()