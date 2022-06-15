# how to draw lines and shape in python

import cv2 as cv
import numpy as np

# draw a canvas , zeroes = black, ones = white
img = np.zeros((600,600))
img1 = np.ones((600,600))



cv.imshow('black', img)
cv.imshow('white', img1)


print ( "The size of our canvas is: ", img.shape)
# print(img)

# adding colos to the canvas
colored_img = np.zeroes((600,600,3), np.uint8)

colored_img[:] = 255,0,255 # color complete image

colored_img[150:230, 100:500] # part of image to be colored

# adding lines
cv.line(colored_img, (0,0), (colored_img.shape[0], colored_img.shape[1]) , (255,0,0) ,3)
cv.line(colored_img, (100,100), (300,300), (255,255,50) ,3) # part line

# adding rectangles
cv.rectangle(colored_img, (50,100), (300,400), (255,255,255), 3) # draw
cv.rectangle(colored_img, (50,100), (300,400), (255,255,255), cv.filled) # fill

# adding circle
cv.circle(colored_img, (400,300), 50, (255,100,0), 5)
cv.circle(colored_img, (400,300), 50, (255,100,0), cv.filled)

# adding text
cv.putText(colored_img, "Python ka Chilla", (200,500), cv.FONT_HERSHEY_DUPLEX, 1, (255,255,0), 1)

cv.waitKey(0)
cv.destroyAllWindows()