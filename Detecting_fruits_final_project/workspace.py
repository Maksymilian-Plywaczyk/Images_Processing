## sprawdzanie różnych rozwiązań
import cv2
import numpy as np

##TODO poprawić implementacje problemu, aby optymalizacja byla sprawniejsza
#TODO sprawdzić tracbara
def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass
def HSV_without_trackbar():
    orange = 0
    apple =  0
    banana = 0
    path = "data/09.jpg"
    jpg = cv2.imread(path,1)
    resize_jpg = cv2.resize(jpg, dsize=(1000, 800), interpolation=cv2.INTER_AREA)
    jpg = cv2.GaussianBlur(resize_jpg,(19,19),0)
    hsv_jpg = cv2.cvtColor(jpg, cv2.COLOR_BGR2HSV)

    #Banana
    lower_banana = np.array([20, 100, 160])
    upper_banana = np.array([30, 255, 255])
    mask_banana = cv2.inRange(hsv_jpg, lower_banana, upper_banana)
    banana_contours = cv2.findContours(mask_banana, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    banana_contours = banana_contours[0]
    for c in banana_contours:
        x,y,w,h = cv2.boundingRect(c)
        contour = cv2.contourArea(c)
        if contour > 7500:
            print('contour area of banana', contour)
            cv2.rectangle(jpg, (x, y),(x + w, y + h), (0,0,255), 2) ##BGR
            banana += 1


    #Orange
    lower_orange = np.array([0, 217, 0]) # 10 200 200
    upper_orange = np.array([19, 255, 255]) # 25 255 255
    mask_orange = cv2.inRange(hsv_jpg,lower_orange,upper_orange)
    orange_contours = cv2.findContours(mask_orange,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    orange_contours = orange_contours[0]
    for o in orange_contours:
        x,y,w,h = cv2.boundingRect(o)
        contour = cv2.contourArea(o)
        if contour > 8000:
            print('contour area of orange', contour)
            cv2.rectangle(jpg, (x, y),(x + w, y + h), (255,0,0), 2) ##BGR
            orange += 1


    lower2 = np.array([0, 36, 0]) #0 128 24    0 125 0
    upper2 = np.array([13, 220, 255]) #10 255 255 31 255 148

    upper_mask = cv2.inRange(hsv_jpg, lower2, upper2)

    apple_mask = upper_mask
    apple_contours = cv2.findContours(apple_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    apple_contours = apple_contours[0]
    for a in apple_contours:
        x,y,w,h = cv2.boundingRect(a)
        contour = cv2.contourArea(a)
        if contour> 8000: #contours area function need to check
            print('contour area of apple', contour)
            cv2.rectangle(jpg, (x, y),(x + w, y + h), (0,255,0), 2) ##BGR
            apple += 1


    print('Number of orange: '+str(orange))
    print('Number of banana: '+str(banana))
    print('Number of apple: '+str(apple))
    while True:
        cv2.imshow('Result',jpg)
        cv2.imshow('Mask',apple_mask)
        key_code = cv2.waitKey(1)
        if key_code == 27:
            exit()

def HSV_with_trackbar():
    path = "data/02.jpg"
    nameWindow = "Trackbar HSV"
    img = cv2.imread(path, 1)
    resize_img = cv2.resize(img, dsize=(1000, 800), interpolation=cv2.INTER_AREA)
    gaus= cv2.GaussianBlur(resize_img, (19, 19), 0)
    hsv_img = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)
    cv2.namedWindow(nameWindow)
    #lower range
    cv2.createTrackbar("LH",nameWindow,  0, 255, empty_callback)
    cv2.createTrackbar("LS", nameWindow, 0, 255, empty_callback)
    cv2.createTrackbar("LV", nameWindow, 0, 255, empty_callback)

    #upper range
    cv2.createTrackbar("UH", nameWindow, 0, 255, empty_callback)
    cv2.createTrackbar("US", nameWindow, 0, 255, empty_callback)
    cv2.createTrackbar("UV", nameWindow, 0, 255, empty_callback)

    while True:
        #lower range HSV
        LH = cv2.getTrackbarPos("LH",nameWindow)
        LS = cv2.getTrackbarPos("LS", nameWindow)
        LV = cv2.getTrackbarPos("LV", nameWindow)

        #upper range HSV
        UH = cv2.getTrackbarPos("UH", nameWindow)
        US = cv2.getTrackbarPos("US", nameWindow)
        UV = cv2.getTrackbarPos("UV", nameWindow)

        lower_HSV = np.array([LH, LS, LV])
        upper_HSV = np.array([UH, US, UV])
        mask = cv2.inRange(hsv_img,lower_HSV,upper_HSV)
        result_img = cv2.bitwise_and(resize_img,resize_img,mask= mask)


        cv2.imshow('Trackbar_HSV', result_img)
        cv2.imshow('Mask',mask)
        cv2.imshow('HSV',hsv_img)
        key_code = cv2.waitKey(1)
        if key_code == 27:
            exit()
    cv2.destroyAllWindows()

#HSV_with_trackbar()
HSV_without_trackbar()