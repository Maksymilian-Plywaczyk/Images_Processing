import cv2
import numpy as np


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass


# yolo
# create and read path images
path = "krysiak.jpg"
img = cv2.imread(path, 1)

path1 = "qr.jpg"  # way relative, qr.jpg sitting in the same place like main.py
img1 = cv2.imread(path1, 1)

path2 = "logo_put.png"
img2 = cv2.imread(path2, 1)

# scaled images
img_scaled = cv2.resize(img1, None, fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR)
krysiak_scaled = cv2.resize(img, dsize=(313, 313), interpolation=cv2.INTER_LINEAR)

cv2.namedWindow('Blending')
cv2.namedWindow('image')
cv2.namedWindow('resize window')
# create trackbars for color change

cv2.createTrackbar('Thresholding_Binary', 'image', 0, 255, empty_callback)
cv2.createTrackbar('Thresholding_BinaryINV', 'image', 0, 255, empty_callback)
cv2.createTrackbar('Thresholding_Trunc', 'image', 0, 255, empty_callback)
cv2.createTrackbar('Thresholding_Tozero', 'image', 0, 255, empty_callback)
# create switch for ON/OFF functionality
switch_trackbar_name = 'Choose Thresholding'
cv2.createTrackbar(switch_trackbar_name, 'image', 0, 4, empty_callback)

blending_range = 'Range_of_Alfa_and_Beta'

alpha_slider_max = 100


def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = (1.0 - alpha)
    dst = cv2.addWeighted(krysiak_scaled, alpha, img2, beta, 0.0)
    cv2.imshow('Blending', dst)
    pass


while True:
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout

    # get current positions of four trackbars
    thresholding = cv2.getTrackbarPos('Thresholding_Binary', 'image')
    thresholding1 = cv2.getTrackbarPos('Thresholding_BinaryINV', 'image')
    thresholding2 = cv2.getTrackbarPos('Thresholding_Trunc', 'image')
    thresholding3 = cv2.getTrackbarPos('Thresholding_Tozero', 'image')

    ret, thresh = cv2.threshold(img, 127, thresholding, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, thresholding1, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, thresholding2, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, thresholding3, cv2.THRESH_TOZERO)

    s = cv2.getTrackbarPos(switch_trackbar_name, 'image')

    cv2.createTrackbar(blending_range, 'Blending', 0, alpha_slider_max, on_trackbar)
    on_trackbar(0)
    if s == 1:
        cv2.imshow('image', thresh)
    if s == 2:
        cv2.imshow('image', thresh2)
    if s == 3:
        cv2.imshow('image', thresh3)
    if s == 4:
        cv2.imshow('image', thresh4)

    cv2.imshow('resize window', img_scaled)
    # cv2.imshow('Blending', blending_img)

    key_code = cv2.waitKey(0)
    if key_code == ord('k'):
        # escape key pressed
        break

# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()