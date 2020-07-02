import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('sudoku.jpg',0)
cv2.namedWindow('Cannyt')
cv2.createTrackbar('Thresh 1','Cannyt',0,255,nothing)
cv2.createTrackbar('Thresh 2','Cannyt',0,255,nothing)
while True:
    thresh_1 = cv2.getTrackbarPos('Thresh 1','Cannyt')
    thresh_2 = cv2.getTrackbarPos('Thresh 2','Cannyt')
    canny = cv2.Canny(img,thresh_1,thresh_2)
    cv2.imshow('Original IMage',img)
    cv2.imshow('Canny Image',canny)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
