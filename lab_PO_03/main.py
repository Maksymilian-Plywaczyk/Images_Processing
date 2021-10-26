import cv2


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass

#checking its work from different PC
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


def Filtering():
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


while True:

    Filtering()
    key_code = cv2.waitKey(1)
    if key_code == 27:
        # escape key pressed
        break

cv2.destroyAllWindows()
