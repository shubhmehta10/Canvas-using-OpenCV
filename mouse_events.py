import cv2
import numpy as np

img = np.ones([400,400,3],dtype='uint8')*255
wname = 'Drawing'
cv2.namedWindow(wname)

def draw_shape(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(55,55,55),-1)
        print(x,y)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+100,y+50),(55,0,55),-1)
        print(x,y)

    
cv2.setMouseCallback(wname,draw_shape)#Callback Method

while True:
    cv2.imshow(wname,img)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()

