import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while(True):
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)

    cv.imshow('Originalcam', frame)
    cv.imshow('graycam', gray_frame)
    cv.imshow('binarycam', binary)

    if cv.waitkey(1) & 0xFF == ord('q'):
        break

    cap.release()
    cv.destroyAllWindows