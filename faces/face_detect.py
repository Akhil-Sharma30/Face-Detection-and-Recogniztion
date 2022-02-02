import cv2 as cv

img = cv.imread('photos/wallpaper.png')
cv.imshow('person',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray-Person',gray)

# reading the haarcascade file and storing the data into the variable
haar_casacade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_casacade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print(f'Number of faces = {len(face_rect)}')

for(x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
cv.imshow('detected faces',img)

cv.waitKey(0)