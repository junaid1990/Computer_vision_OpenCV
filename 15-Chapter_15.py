# resolution of camera
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)
# resolution HD (1280x720)


# def fhd_resolution():
#     cap.set(3,1980)
#     cap.set(4, 1080)


# def hd_resolution():
#     cap.set(3,1280)
#     cap.set(4, 720)

def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)

# fhd_resolution()
# hd_resolution()

sd_resolution()

# how to change and fix the frame rate to 30fps

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Camera', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()