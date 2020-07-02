import cv2
import numpy as np

img = np.zeros([400,400,3],dtype='uint8')*255
wname = 'Drawing'
cv2.namedWindow(wname)

abc = False

def draw_eraser(event,x,y,flags,param):
    global abc
    if event == cv2.EVENT_LBUTTONDOWN:
        abc = True
        cv2.circle(img,(x,y),10,(255,255,255),-1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if (abc == True):
            cv2.circle(img,(x,y),10,(255,255,255),-1)
    else:
        abc = False 

cv2.setMouseCallback(wname,draw_eraser)

#def draw_shape(event,x,y,flags,param):
    #if event == cv2.EVENT_RBUTTONDOWN:
     #   cv2.circle(img,(x,y),10,(250,55,67),10)
    #if event == cv2.EVENT_MBUTTONDOWN:
     #   cv2.rectangle(img,(x,y),(x+100,y+50),(55,0,55),5)

#cv2.setMouseCallback(wname,draw_shape)       
#Callback Method


while True:
    cv2.imshow(wname,img)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
