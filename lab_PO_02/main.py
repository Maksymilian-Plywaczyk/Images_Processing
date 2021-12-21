import cv2
import numpy as np
from time import perf_counter

def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass


path = "krysiak.jpg"
img = cv2.imread(path, 1)

path2 = "logo_put.png"
img2 = cv2.imread(path2, 1)

path3 = "kampus.png"
img3 = cv2.imread(path3,cv2.IMREAD_GRAYSCALE)


# scaled images
krysiak_scaled = cv2.resize(img, dsize=(313, 313), interpolation=cv2.INTER_LINEAR)

cv2.namedWindow('Blending')
cv2.namedWindow('images')
cv2.namedWindow('resize window')
# create trackbars for color change

cv2.createTrackbar('Thresholding_Binary', 'images', 0, 255, empty_callback)
cv2.createTrackbar('Thresholding_BinaryINV', 'images', 0, 255, empty_callback)
cv2.createTrackbar('Thresholding_Trunc', 'images', 0, 255, empty_callback)
cv2.createTrackbar('Thresholding_Tozero', 'images', 0, 255, empty_callback)
# create switch for ON/OFF functionality
switch_trackbar_name = 'Choose Thresholding'
cv2.createTrackbar(switch_trackbar_name, 'images', 0, 4, empty_callback)

blending_range = 'Range_of_Alfa_and_Beta'

alpha_slider_max = 100


def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = (1.0 - alpha)
    dst = cv2.addWeighted(krysiak_scaled, alpha, img2, beta, 0.0)
    cv2.imshow('Blending', dst)
    pass

def scaled_photo():
    time_start=perf_counter()
    path1 = "qr.jpg"  # way relative, qr.jpg sitting in the same place like detect_fruits.py
    img1 = cv2.imread(path1, 1)
    img_scaled = cv2.resize(img1, None, fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('resize window', img_scaled)
    time_stop=perf_counter()
    print("Elapsed time: ",time_start,time_stop)
    print("Elapsed time during the whole program in seconds: ", time_stop-time_start)
    pass

def negative_function():
    read="logo_put.png"
    image=cv2.imread(read,0)
    cv2.namedWindow('Negative')
    ret, mask = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)
    image_neg=cv2.bitwise_not(mask)
    cv2.imshow('Negative',image_neg)

while True:

    # sleep for 10 ms waiting for user to press some key, return -1 on timeout

    # get current positions of four trackbars
    thresholding = cv2.getTrackbarPos('Thresholding_Binary', 'images')
    thresholding1 = cv2.getTrackbarPos('Thresholding_BinaryINV', 'images')
    thresholding2 = cv2.getTrackbarPos('Thresholding_Trunc', 'images')
    thresholding3 = cv2.getTrackbarPos('Thresholding_Tozero', 'images')

    ret, thresh = cv2.threshold(img3, 55, thresholding, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img3, 55, thresholding1, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img3, 55, thresholding2, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img3, 55, thresholding3, cv2.THRESH_TOZERO)

    s = cv2.getTrackbarPos(switch_trackbar_name, 'images')

    cv2.createTrackbar(blending_range, 'Blending', 0, alpha_slider_max, on_trackbar)

    if s == 1:
        cv2.imshow('images', thresh)
    if s == 2:
        cv2.imshow('images', thresh2)
    if s == 3:
        cv2.imshow('images', thresh3)
    if s == 4:
        cv2.imshow('images', thresh4)


    scaled_photo()
    on_trackbar(0)
    negative_function()
    key_code = cv2.waitKey(0)
    if key_code == 27:
        # escape key pressed
        exit()

# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()