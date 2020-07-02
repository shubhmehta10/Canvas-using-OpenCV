import cv2 #importing cv library 
import numpy as np #importing numpy library for creating arrays

img = np.ones([600,600],dtype='uint8')*255 #creating a variable named img to get white picture of 600*600 pixels

img[100:500,100:500] = 0 #defining my window name

wname = 'Canvas' #defining my window name
cv2.namedWindow(wname)

abc = False #flag by default value to be considered as false

def draw_eraser(event,x,y,flags,param): #defining my function for mouse call back
    global abc #variable is considered to be global so that it can used in the function
    if event == cv2.EVENT_LBUTTONDOWN: #checking the first condition for left button down event
        abc = True #set flag value to TRue indicating that left button is clicked 
        cv2.circle(img,(x,y),5,(255,255,255),-1) #circle shape is drawn
    elif event == cv2.EVENT_MOUSEMOVE: #checking the second condition for scrolling the mouse 
        if (abc == True): #nested if to check another condition with flag being true 
            cv2.circle(img,(x,y),10,(255,255,255),-1) #circle shape is drawn
    else: #if none of the above conditions are met
        abc = False #flag is set to default  

cv2.setMouseCallback(wname,draw_eraser) #call back method 

while True: #forever loop
    cv2.imshow(wname,img)
    key = cv2.waitKey(1)#declaring a variable key and initializing it ot a waitkey (1)
    if key == 13: #1st condition 13: quit
        break
    elif key == ord('c'):#2nd conditioon c: Clear
        img[100:500,100:500] = 0
    elif key == ord('w'):#3rd condition w: writing/saving
        out = img[100:500,100:500]
        cv2.imwrite('Output Image.jpg',out)
        
cv2.destroyAllWindows()
