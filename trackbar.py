import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros([300,300,3],dtype='uint8')

cv2.namedWindow('Color Variation')
cv2.createTrackbar('red','Color Variation',0,255,nothing)
cv2.createTrackbar('blue','Color Variation',0,255,nothing)
cv2.createTrackbar('green','Color Variation',0,255,nothing)

while True:
    cv2.imshow('Original',img)
    if cv2.waitKey(1) == 13:
        break
    r = cv2.getTrackbarPos('red','Color Variation')
    g = cv2.getTrackbarPos('green','Color Variation')
    b = cv2.getTrackbarPos('blue','Color Variation')
    img[0:100,0:300]=[0,0,r]
    img[100:200,0:300]=[0,g,0]
    img[200:300,0:300]=[b,0,0]

cv2.destroyAllWindows()
