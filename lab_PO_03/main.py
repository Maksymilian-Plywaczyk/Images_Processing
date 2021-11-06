import cv2
import numpy as np
from time import perf_counter


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass


def Filtering():
    nameWindow = 'Filtering'
    nameWindow2 = 'Filtering salt and pepper'
    path = "lenna_noise.bmp"
    path2 = "lenna_salt_and_pepper.bmp"
    trackbar_name = 'Wybieranie: \n Averaging \n Gaussian Blurring \n Median Blurring \n Bilateral Filtering'
    trackbar_name2 = 'Range'
    img = cv2.imread(path, 0)
    img2 = cv2.imread(path2, 0)
    cv2.namedWindow(nameWindow)
    cv2.namedWindow(nameWindow2)
    cv2.createTrackbar(trackbar_name, nameWindow, 0, 2, empty_callback)
    cv2.createTrackbar(trackbar_name2, nameWindow, 0, 20, empty_callback)

    cv2.createTrackbar(trackbar_name, nameWindow2, 0, 2, empty_callback)
    cv2.createTrackbar(trackbar_name2, nameWindow2, 0, 20, empty_callback)

    while True:
        s = cv2.getTrackbarPos(trackbar_name, nameWindow)
        s2 = cv2.getTrackbarPos(trackbar_name2, nameWindow)
        s3 = cv2.getTrackbarPos(trackbar_name2, nameWindow2)
        s4 = cv2.getTrackbarPos(trackbar_name, nameWindow2)
        if s2 % 2 == 0:
            s2 += 1
        if s3 % 2 == 0:
            s3 += 1

        blur = cv2.blur(img, (s2, s2))
        blur2p = cv2.GaussianBlur(img, (s2, s2), 0)
        median = cv2.medianBlur(img, s2)

        blur2 = cv2.blur(img2, (s3, s3))
        blur2p2 = cv2.GaussianBlur(img2, (s3, s3), 0)
        median2 = cv2.medianBlur(img2, s3)
        if s == 0:
            cv2.imshow(nameWindow, blur)

        if s == 1:
            cv2.imshow(nameWindow, blur2p)

        if s == 2:
            cv2.imshow(nameWindow, median)

        if s4 == 0:
            cv2.imshow(nameWindow2, blur2)

        if s4 == 1:
            cv2.imshow(nameWindow2, blur2p2)

        if s4 == 2:
            cv2.imshow(nameWindow2, median2)

        key_code = cv2.waitKey(10)
        if key_code == 27:
            # escape key pressed
            break


def OperationMorphologic():
    path = "j.png"
    img = cv2.imread(path, 0)
    nameWindow = 'OperationMorphologic'
    nameWindow2 = 'Erosion'
    cv2.namedWindow(nameWindow)
    cv2.namedWindow(nameWindow2)
    cv2.createTrackbar('Erosioning', nameWindow2, 0, 7, empty_callback)

    while True:
        erosioning = cv2.getTrackbarPos('Erosioning', nameWindow2)
        ret, thresh = cv2.threshold(img, 55, 255, cv2.THRESH_BINARY)
        cv2.imshow(nameWindow, thresh)
        kernel = np.ones((erosioning, erosioning), np.uint8)
        erosion = cv2.erode(thresh, kernel, iterations=1)
        cv2.imshow(nameWindow2, erosion)
        key_code = cv2.waitKey(1)
        if key_code == 27:
            # escape key pressed
            break


def SmoothingImage():
    path = "krysiak.jpg"
    img=cv2.imread(path, 0)
    cv2.namedWindow('SmoothingImage')
    dim=(3,3)
    img_resize=cv2.resize(img,dim, interpolation=cv2.INTER_AREA)
    height = img_resize.shape[0]
    width = img_resize.shape[1]
    number_channels=img_resize[2]

    #Start the stopwatch / counter
    time_start = perf_counter()

    for height in range(1, height-1):
        for width in range(1, width-1):
            new_values_pixels = img_resize[height, width] * 0.4 + img_resize[height, width + 1] * -0.1 + img_resize[height, width - 1] * 0.1\
                                + img_resize[height + 1, width] * 0.1 + img_resize[height + 1, width + 1] * -0.05 + img_resize[
                                    height + 1, width - 1] * 0.05 \
                                + img_resize[height - 1, width] * 0.1 + img_resize[height - 1, width + 1] * -0.05 + img_resize[
                                    height - 1, width - 1] * 0.05
            new_values_pixels_sum = (img_resize[height, width] + img_resize[height, width + 1] + img_resize[height, width - 1] \
                                     + img_resize[height + 1, width] + img_resize[height + 1, width + 1] + img_resize[height + 1, width - 1] \
                                     + img_resize[height - 1, width] + img_resize[height - 1, width + 1] + img_resize[
                                         height - 1, width - 1]) / 9
            img_resize[height, width] = new_values_pixels_sum

    #Stop the stopwatch / counter
    time_stop = perf_counter()
    print('Elapsed time: ', time_start - time_stop)
    kernel = np.ones((3, 3), np.uint8)
    time_start2D=perf_counter()
    cv2.filter2D(img_resize,ddepth=-1,kernel=kernel)
    time_stop2D=perf_counter()
    print('Elapsed time: ',time_start2D-time_stop2D)
    #Comparing our function with filter2D
    if time_start-time_stop<time_start2D-time_stop2D:
        print('Linear function is faster')
    else:
        print('Filter2D is faster')

    cv2.imshow('SmoothingImage', img_resize)
    cv2.waitKey(0)


def ScalingImage():
    path = "krysiak.jpg"
    img = cv2.imread(path, 0)
    cv2.namedWindow('ScalingImage')
    cv2.namedWindow('BlurScaling')
    height, width = img.shape
    time_start = perf_counter()
    for h in range(0, height):
        for w in range(0, width):
            if h % 3 and w % 3 == 0:
                img[h, w] = 255
    time_stop = perf_counter()
    print("Elapsed time: ", time_start, time_stop)
    period_pixel = time_stop - time_start

    time_startBlur = perf_counter()
    blur = cv2.blur(img, (3, 3))
    time_stopBlur = perf_counter()
    print("Elapsed time of blur: ", time_startBlur, time_stopBlur)
    period_blur = time_startBlur - time_stopBlur
    if period_pixel <= period_blur:
        print('Period of pixel is faster than blur')
    else:
        print('Period of blur function is faster than pixel')

    cv2.imshow('BlurScaling', blur)
    cv2.imshow('ScalingImage', img)
    cv2.waitKey(0)


if __name__ == "__main__":  # makeshift main
    Filtering()
    OperationMorphologic()
    ScalingImage()
    SmoothingImage()
cv2.destroyAllWindows()
