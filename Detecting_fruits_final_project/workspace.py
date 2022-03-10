## sprawdzanie różnych rozwiązań
import cv2
import numpy as np


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass

def HSV_without_trackbar():
    orange = 0
    apple = 0
    banana = 0

    path = "data/04.jpg"
    jpg = cv2.imread(path,1)
    resize_jpg = cv2.resize(jpg, dsize=None,fx=0.25,fy=0.25, interpolation=cv2.INTER_AREA)
    jpg = cv2.GaussianBlur(resize_jpg,(19,19),0)
    hsv_jpg = cv2.cvtColor(jpg, cv2.COLOR_BGR2HSV)
    kernel = np.ones((7, 7), np.uint8)



   #Banana
    lower_banana = np.array([20, 100, 160])
    upper_banana = np.array([30, 255, 255])
    mask_banana = cv2.inRange(hsv_jpg, lower_banana, upper_banana)

    lower_banana1 = np.array([19, 78, 87])
    upper_banana1 = np.array([45, 255, 255])
    mask_banana1 = cv2.inRange(hsv_jpg, lower_banana1, upper_banana1)

    mask_banana_full = mask_banana+mask_banana1

    closing_banana = cv2.morphologyEx(mask_banana_full, cv2.MORPH_CLOSE, kernel)
    banana_contours = cv2.findContours(closing_banana, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    banana_contours = banana_contours[0]
    for c in banana_contours:
        x,y,w,h = cv2.boundingRect(c)
        contour = cv2.contourArea(c)
        if contour > 10000:
            print('contour area of banana', contour)
            cv2.rectangle(resize_jpg, (x, y),(x + w, y + h), (0,0,255), 2) ##BGR
            cv2.putText(resize_jpg,"Banana",(x,y), cv2.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,0,255),thickness=None)
            banana += 1

    #Orange
    lower_orange = np.array([0, 206, 0]) # 10 200 200
    upper_orange = np.array([19, 255, 255]) # 25 255 255
    mask_orange = cv2.inRange(hsv_jpg, lower_orange, upper_orange)

    lower_orange1 = np.array([9,102, 227])  # 10 200 200
    upper_orange1 = np.array([52, 252, 255])  # 25 255 255
    mask_orange1 = cv2.inRange(hsv_jpg, lower_orange1, upper_orange1)

    mask_orange_full = mask_orange1+mask_orange

    closing_orange = cv2.morphologyEx(mask_orange_full, cv2.MORPH_CLOSE, kernel)
    orange_contours = cv2.findContours(closing_orange,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    orange_contours = orange_contours[0]
    for o in orange_contours:
        x,y,w,h = cv2.boundingRect(o)
        contour = cv2.contourArea(o)
        if contour > 10000:
            print('contour area of orange', contour)
            cv2.rectangle(resize_jpg, (x, y),(x + w, y + h), (255,0,0), 2) ##BGR
            cv2.putText(resize_jpg, "Orange", (x, y), cv2.FONT_HERSHEY_DUPLEX,fontScale=1,color=(255,0,0),thickness=None)
            orange += 1


    lower = np.array([0, 36, 0]) #0 128 24    0 125 0
    upper = np.array([14, 220, 255]) #10 255 255 31 255 148
    upper_mask = cv2.inRange(hsv_jpg, lower, upper)

    lower1 = np.array([52, 45, 0])  # 0 128 24    0 125 0
    upper1 = np.array([189, 255, 255])  # 10 255 255 31 255 148
    upper_mask1 = cv2.inRange(hsv_jpg, lower1, upper1)

    apple_mask = upper_mask+upper_mask1

    closing_apple = cv2.morphologyEx(apple_mask, cv2.MORPH_CLOSE, kernel)
    apple_contours = cv2.findContours(closing_apple,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    apple_contours = apple_contours[0]
    for a in apple_contours:
        x,y,w,h = cv2.boundingRect(a)
        contour = cv2.contourArea(a)
        if contour> 10000: #contours area function need to check
            print('contour area of apple', contour)
            cv2.rectangle(resize_jpg, (x, y),(x + w, y + h), (0,255,0), 2) ##BGR
            cv2.putText(resize_jpg, "Apple", (x, y), cv2.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,255,0),thickness=None)
            apple += 1


    print('Number of orange: '+str(orange))
    print('Number of banana: '+str(banana))
    print('Number of apple: '+str(apple))
    while True:
        cv2.imshow('Result',resize_jpg)
        cv2.imshow('Mask',closing_banana)
        key_code = cv2.waitKey(1)
        if key_code == 27:
            exit()

def HSV_with_trackbar():
    path = "data/08.jpg"
    nameWindow = "Trackbar HSV"
    nameWindow1 = "Trackbar HSV1"
    img = cv2.imread(path, 1)
    resize_img = cv2.resize(img, dsize=(1000, 800), interpolation=cv2.INTER_AREA)
    gaus= cv2.GaussianBlur(resize_img, (19, 19), 0)
    hsv_img = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)
    cv2.namedWindow(nameWindow)
    cv2.namedWindow(nameWindow1)
    kernel = np.ones((7, 7), np.uint8)
    #lower range
    cv2.createTrackbar("LH",nameWindow,  0, 255, empty_callback)
    cv2.createTrackbar("LS", nameWindow, 0, 255, empty_callback)
    cv2.createTrackbar("LV", nameWindow, 0, 255, empty_callback)

    #upper range
    cv2.createTrackbar("UH", nameWindow, 0, 255, empty_callback)
    cv2.createTrackbar("US", nameWindow, 0, 255, empty_callback)
    cv2.createTrackbar("UV", nameWindow, 0, 255, empty_callback)

    cv2.createTrackbar("LH1", nameWindow1, 0, 255, empty_callback)
    cv2.createTrackbar("LS1", nameWindow1, 0, 255, empty_callback)
    cv2.createTrackbar("LV1", nameWindow1, 0, 255, empty_callback)

    # upper range
    cv2.createTrackbar("UH1", nameWindow1, 0, 255, empty_callback)
    cv2.createTrackbar("US1", nameWindow1, 0, 255, empty_callback)
    cv2.createTrackbar("UV1", nameWindow1, 0, 255, empty_callback)

    while True:
        #lower range HSV
        LH = cv2.getTrackbarPos("LH",nameWindow)
        LS = cv2.getTrackbarPos("LS", nameWindow)
        LV = cv2.getTrackbarPos("LV", nameWindow)

        #upper range HSV
        UH = cv2.getTrackbarPos("UH", nameWindow)
        US = cv2.getTrackbarPos("US", nameWindow)
        UV = cv2.getTrackbarPos("UV", nameWindow)

        LH1 = cv2.getTrackbarPos("LH1", nameWindow1)
        LS1 = cv2.getTrackbarPos("LS1", nameWindow1)
        LV1 = cv2.getTrackbarPos("LV1", nameWindow1)

        # upper range HSV
        UH1 = cv2.getTrackbarPos("UH1", nameWindow1)
        US1 = cv2.getTrackbarPos("US1", nameWindow1)
        UV1 = cv2.getTrackbarPos("UV1", nameWindow1)

        lower_HSV = np.array([LH, LS, LV])
        upper_HSV = np.array([UH, US, UV])

        lower_HSV1 = np.array([LH1, LS1, LV1])
        upper_HSV1= np.array([UH1, US1, UV1])
        mask = cv2.inRange(hsv_img,lower_HSV,upper_HSV)
        mask1 = cv2.inRange(hsv_img, lower_HSV1, upper_HSV1)
        full = mask + mask1
        closing = cv2.morphologyEx(full, cv2.MORPH_CLOSE, kernel)
        cv2.imshow('Trackbar_HSV',closing)

        key_code = cv2.waitKey(1)
        if key_code == 27:
            exit()
    cv2.destroyAllWindows()

#HSV_with_trackbar()
HSV_without_trackbar()