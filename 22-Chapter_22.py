# face detection in images
import cv2 as cv

face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

img = cv.imread('resources/faces.jpg')
# img = cv.resize(img, (250,374))

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

# draw a rectangle
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)


cv.imshow('image', img)
cv.imwrite('resources/face_detected.png', img)
cv.waitKey(0)
cv.destroyAllWindows


# https://github.com/opencv/opencv/tree/master/data/haarcascades