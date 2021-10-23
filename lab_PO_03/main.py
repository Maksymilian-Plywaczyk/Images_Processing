import cv2
import numpy as np


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass


def filtering_exercise_1():
    path = "lenna_noise.bmp"
    img = cv2.imread(path, 1)
    nameWindow = 'Filtering'
    cv2.namedWindow(nameWindow)
    trackbar_name = 'Wybieranie: \n Averaging \n Gaussian Blurring \n Median Blurring \n Bilateral Filtering'
    cv2.createTrackbar(trackbar_name, nameWindow, 0, 2, empty_callback)
    s = cv2.getTrackbarPos(trackbar_name, nameWindow)
    blur = cv2.blur(img, (5, 5))
    blur2p = cv2.GaussianBlur(img, (5, 5))
    medianp = cv2.medianBlur(img, (5))
    if (s == 0):
        cv2.imshow(nameWindow, blur)

    if (s == 1):
        cv2.imshow(nameWindow, blur2p)

    if (s == 2):
        cv2.imshow(nameWindow, medianp)


while True:
    key_code = cv2.waitKey(0)
    if key_code == ord('a'):
        # escape key pressed
        break