import cv2

img = cv2.imread('sudoku.jpg',0)

sobel_x = cv2.Sobel(img,cv2.CV_8U,dx=1,dy=0,ksize=-1)
sobel_y = cv2.Sobel(img,cv2.CV_8U,dx=0,dy=1,ksize=-1)
sobel_f = cv2.bitwise_or(sobel_x,sobel_y)#convolution
canny = cv2.Canny(img,127,255)

cv2.imshow('Original IMage',img)
cv2.imshow('Sobel X Image',sobel_x)
cv2.imshow('Sobel Y Image',sobel_y)
cv2.imshow('Sobel Total Image',sobel_f)
cv2.imshow('Canny Image',canny)

cv2.waitKey()
cv2.destroyAllWindows()
