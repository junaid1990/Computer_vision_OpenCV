# how change the prespective of an image

import cv2 as cv
import numpy as np

img = cv.imread('resources/warp.jpg')
# print(img.shape) , to findout width and height of image

# defining points
point1 = np.float32([[233,196],[82,471],[522,169],[715,482]])
width = 800
height = 900
point2 = np.float32([[0,0],[800,0],[0,height],[width,height]])

# width, height = 800,900

matrix = cv.getPerspectiveTransform(point1,point2)
out_img = cv.warpPerspective(img, matrix, (width,height))
# out_img = cv.resize()

cv.imshow('Original', img)
cv.imshow('Transformed', out_img)
cv.imwrite('resources/warp_prespective.png', out_img) # to write or save image
cv.waitKey(0)
cv.destroyAllWindows()