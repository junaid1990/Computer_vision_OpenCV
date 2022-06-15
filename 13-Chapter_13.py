# basic function and manipulation in open cv

import cv2 as cv
from cv2 import dilate
import numpy as np

img = cv.imread('resources/image.jpg')

#resize
resized_img= cv.resize(img, (350,250))

# gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blurred image
blurr_img = cv.GaussianBlur(img, (7,7))

# edge dedection
edge_img = cv.Canny(img, 48, 48)

# thickness of lines
mat_kernal = np.ones((7,7), np.unit8)
dilated_img = cv.dilate(edge_img, (23,23), iterations=1)

# make thinner outlines
ero_img = cv.erode(dilated_img , mat_kernal, iterations=1)





cv.imshow('Original', img)
cv.imshow('resized', resized_img)
cv.imshow("Gray", gray_img)
cv.imshow("Blurr", blurr_img)
cv.imshow('Edge', edge_img)
cv.imshow('Dilated', dilated_img)
cv.imshow('Erosion', ero_img)
# make white and black image

cv.waitkey(0)
cv.destroyAllWindows