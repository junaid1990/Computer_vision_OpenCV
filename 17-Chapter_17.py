# joining two iages
import cv2 as cv
import numpy as np

img = cv.imread('resources/imgs.jpg')
img1 = cv.imread('resources/imgs1.jpg')


# stacking same image

# 1- Horizontal stack
hor_img = np.hstack((img, img))

# 1- Vertical stack
ver_img = np.vstack((img1, img1))


cv.imshow('Horizontol', hor_img)
cv.imshow('Vertical', ver_img)

cv.waitKey(0)
cv.destroyAllWindows

