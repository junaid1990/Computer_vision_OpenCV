# Chapter_1

## Import Libraries
import cv2 as cv

#load data
img = cv.imread('resources/image.jpg')

# Display
cv.imshow('1st pic', img)

# Delay Code
cv.waitKey(0)
