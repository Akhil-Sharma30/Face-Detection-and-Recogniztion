import cv2 as cv

img = cv.imread('photos/wallpaper.png')

# Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Blur a image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edge Casacade
canny = cv.Canny(img,125,175)
cv.imshow('Canny casacade',canny)

# Dilating the image
dilate = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilate',dilate)

# Eroding 
eroded = cv.erode(dilate,(3,3),iterations=1)
cv.imshow('eroded',eroded)

# resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resize',resize)

# Cropped 
cropped = img[50:200 , 200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)