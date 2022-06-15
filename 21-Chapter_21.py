# how to detect specific colors inside python

import cv2 as cv
import numpy as np

# img  = cv.imread('resources/imgs.jpg')

# convert in hsv *(Hue, Saturatio, value)
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# slider
def slider():
    pass

path = 'resources/imgs.jpg'

cv.namedWindow('Bars')
cv.resizeWindow('Bars', 900, 300) # can change Values


cv.createTrackbar('Hue Min', 'Bars', 0,179, slider) # huw value in max 1-180 here we use python thats why 0-179
cv.createTrackbar('Hue Max', 'Bars', 179,179, slider) 
cv.createTrackbar('Sat Min', 'Bars', 0,255, slider) # saturation
cv.createTrackbar('Sat Max', 'Bars', 255,255, slider) 
cv.createTrackbar('Val Min', 'Bars', 0,255, slider) # value
cv.createTrackbar('Val Max', 'Bars', 255,255, slider) 

img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# hue_min = cv.getTrackbarPos("Hue min", "Bars")
# print(hue_min)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue min", "Bars")
    hue_max = cv.getTrackbarPos("Hue max", "Bars")
    sat_min = cv.getTrackbarPos("Sat min", "Bars")
    sat_max = cv.getTrackbarPos("Sat max", "Bars")
    val_min = cv.getTrackbarPos("Val min", "Bars")
    val_max = cv.getTrackbarPos("Val max", "Bars")
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)
    
    # to see these changes inside an image
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img, mask=mask_img)


    cv.imshow('original', img)
    cv.imshow('hsv_img', hsv_img)
    cv.imshow('Mask', mask_img)
    cv.imshow('Final output', out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()

