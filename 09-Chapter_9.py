# 1-Import libraries
import cv2 as cv
import numpy as np

# 2- Read the frames from camera
cap = cv.VideoCapture(1, cv.CAP_DSHOW)
# cap = cv.VideoCapture(1) # 0 = webcam no.1, 1= webcam no.2, etc

# read untill the end
# 3- Display frame by frame
while (cap.isOpened()):
    # capture frame ny frame
    ret, frame = cap.read()
    if ret == True:
        # to display frame
        cv.imshow('Frame', frame)
        # to quit with q key
        if cv.waitkey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
# release or cclose windows easily
cap.release()
cv.destroyAllWindows()
