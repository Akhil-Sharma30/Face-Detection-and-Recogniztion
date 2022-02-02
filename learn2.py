#writing a text or drawing objects in a image
import cv2 as cv
import numpy as np 

#creating a blank image 
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
# 1. Paint the image a certain colour
# for whole image to be filed
#blank[:]=0,0,255
#for specific part
blank[200:300, 300:400] = 0,0,255
cv.imshow('tanjiro',blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0),(250,250),(0,255,0),thickness=cv.FILLED)
# cv.imshow("rectangle",blank)


# 5. Write a text on a image
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)
cv.waitKey(0)