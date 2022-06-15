# Chapter_2

## Import Libraries
import cv2 as cv

#load data
img = cv.imread('resources/image.jpg')
img1 = cv.resize(img, (800,600))

# Display
cv.imshow('1st pic', img)
cv.imshow('2nd pic', img1)

# Delay Code
cv.waitKey(0)
cv.destroyaAllWindows()

