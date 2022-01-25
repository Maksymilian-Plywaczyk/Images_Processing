## sprawdzanie różnych rozwiązań
import cv2
import numpy as np

##TODO poprawić implementacje problemu, aby optymalizacja byla sprawniejsza
def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass
def HSV_without_trackbar():
    orange = 0
    apple =  0
    banana = 0
    path = "data/01.jpg"
    jpg = cv2.imread(path,1)
    jpg = cv2.resize(jpg, dsize=(1000, 800), interpolation=cv2.INTER_AREA)
    hsv_jpg = cv2.cvtColor(jpg, cv2.COLOR_BGR2HSV)

    #Banana
    lower_banana = np.array([20, 100, 160])
    upper_banana = np.array([30, 255, 255])
    mask_banana = cv2.inRange(hsv_jpg, lower_banana, upper_banana)
    banana_contours = cv2.findContours(mask_banana, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    banana_contours = banana_contours[0]
    for c in banana_contours:
        x,y,w,h = cv2.boundingRect(c)
        print('Banana width', w)
        if w > 120:
            cv2.rectangle(jpg, (x, y),(x + w, y + h), (0,0,255), 2) ##BGR
            banana += 1


    #Orange
    lower_orange = np.array([10, 200, 200])
    upper_orange = np.array([25, 255, 255])
    mask_orange = cv2.inRange(hsv_jpg,lower_orange,upper_orange)
    orange_contours = cv2.findContours(mask_orange,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    orange_contours = orange_contours[0]
    for o in orange_contours:
        x,y,w,h = cv2.boundingRect(o)
        print('Orange width',w)
        if w > 64:
            cv2.rectangle(jpg, (x, y),(x + w, y + h), (255,0,0), 2) ##BGR
            orange += 1


    lower1 = np.array([0, 38, 24])
    upper1 = np.array([9, 255, 255])

    lower2 = np.array([12, 128, 0])
    upper2 = np.array([12,255, 255])

    upper_mask = cv2.inRange(hsv_jpg, lower1, upper1)
    upper_mask1 = cv2.inRange(hsv_jpg, lower2, upper2)

    apple_mask1 = upper_mask1
    apple_mask = upper_mask

    apple_contours = cv2.findContours(apple_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    apple_contours = apple_contours[0]
    apple_contours1 = cv2.findContours(apple_mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    apple_contours1 = apple_contours1[0]
    for o in apple_contours:
        x,y,w,h = cv2.boundingRect(o)
        #print('Apple width: ',w)
        #print('Apple height: ',h)
        if w > 120:
            cv2.rectangle(jpg, (x, y),(x + w, y + h), (0,255,0), 2) ##BGR
            apple += 1
            cv2.putText(jpg, 'Width of rectangle' + str(w), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    for o in apple_contours1:
        x,y,w,h = cv2.boundingRect(o)
        print('Apple width: ',w)
        if h > 155:
            cv2.rectangle(jpg, (x, y),(x + w, y + h), (0,255,0), 2) ##BGR
            apple += 1
            cv2.putText(jpg, 'Height of rectangle' + str(h), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (255, 0, 0), 2)
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
    path = "data/05.jpg"
    nameWindow = "Trackbar HSV"
    img = cv2.imread(path, 1)
    resize_img = cv2.resize(img, dsize=(1000, 800), interpolation=cv2.INTER_AREA)
    hsv_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)
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
        key_code = cv2.waitKey(1)
        if key_code == 27:
            exit()
    cv2.destroyAllWindows()

#HSV_with_trackbar()
HSV_without_trackbar()
