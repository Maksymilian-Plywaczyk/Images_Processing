import cv2
import sys
import numpy as np
def main():
    path= r'/home/lab/Desktop/krajobraz1.jpg'
    img=cv2.imread(path,1)
    img2=cv2.imread(path,0)
    if img is None:
        sys.exit("Could not read the image")
    cv2.imshow('color image', img)
    cv2.imshow('grey image', img2)
    k=cv2.waitKey(0)
    key=ord('a')
    if key==ord('a'):
        cv2.imwrite("/home/lab/Desktop/krajobraz_po_edycji.jpg",img)
    print(np.shape(img))
    print("Wartosc jasnosci pixela w kolorze:")
    print(f'Pixel value at [220, 270]: {img[220,270]}')
    print("Wartosc jasnosci pixela w szarosci:")
    print(f'Pixel value at [220, 270]: {img2[220,270]}')
    ball = img[300:320, 150:170]
    img[150:170, 300:320] = ball
    cv2.imshow('wyciety', img)
    k1 = cv2.waitKey(0)
    path1=r'/home/lab/Desktop/rgb.png'
    img3=cv2.imread(path1,1)
    if img3 is None:
        sys.exit("Could not read the image")
    cv2.imshow('rgb',img3)
    k5=cv2.waitKey(0)
    green = img[..., 1]
    blue = img[..., 0]
    red = img[..., 2]
    cv2.imshow('green', green)
    k2 = cv2.waitKey(0)
    cv2.imshow('blue', blue)
    k3 = cv2.waitKey(0)
    cv2.imshow('red', red)
    k4 = cv2.waitKey(0)
if __name__ == '__main__':
    main()