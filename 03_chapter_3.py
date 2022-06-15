# Chapter_3

## Import Libraries
import cv2 as cv
from cv2 import cvtColor

#load data
img = cv.imread('resources/image.jpg')
img = cv.resize(img, (800,600))

# Conversion
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)

# Display
cv.imshow('1st pic', img)
cv.imshow('2nd pic', gray_img)

# Delay Code
cv.waitKey(0)
# cv.destroyaAllWindows()
