import numpy as np
import cv2

w = np.zeros([400,400],dtype = 'uint8')
# two variables: i - Rows and j - Columns

for i in range (0,401,100):
    for j in range(0,401,100):
        w[i:i+50,j:j+50] = 255
for i in range (50,401,100):
    for j in range(50,401,100):
        w[i:i+50,j:j+50] = 255        
cv2.imshow('white',w)
cv2.waitKey(0)
cv2.destroyAllWindows()
