import cv2 as cv

#reading images 
# img = cv.imread('photos/wallpaper.png')

# cv.imshow('tanjiro',img)

# Reading Videos

capture = cv.VideoCapture('photos/model-working.mp4')

while True:
    isTrue , frame = capture.read()
    
    cv.imshow('video',frame)
    
  #used when we want to break the loop of the on going video and 
  #we are doing it by pressing 'd' key on keyboard
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

