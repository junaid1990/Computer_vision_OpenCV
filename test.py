import cv2 as cv
import numpy as np
img = cv.imread('resources/junaid.jpg')
img = cv.resize(img, (500,700))
print(img.shape)
print("The size of our image is: ", img.shape)

cropped_img = img[0:500 , 150:400]

cv.imshow("Original", img)
cv.imshow("Cropped", cropped_img)
cv.waitKey(0)
cv.destroyAllWindows