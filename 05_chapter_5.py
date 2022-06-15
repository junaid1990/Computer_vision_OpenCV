# Image into black to white image
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite

img = cv.imread('resources/image1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127,255,cv.THRESH_BINARY)

binary = cv.resize(binary, (400,500))

imwrite('resources/image1_gray.jpg', gray)
imwrite('resources/image1_bw.jpg', binary)

cv.waitKey(0)
cv.destroyAllWindows()