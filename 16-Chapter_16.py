# Saving HD recording of cam stram

# resolution of camera
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

# resolution HD,fHD,SD (1280x720)
def fhd_resolution():
    cap.set(3,1980)
    cap.set(4, 1080)
def hd_resolution():
    cap.set(3,1280)
    cap.set(4, 720)
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)

# fhd_resolution()
# hd_resolution()
sd_resolution()

# writing format , codec, video writer objct and file output
frame_width= int(cap.get(3))
frame_height= int(cap.get(4))

# out = cv.VideoWriter("camrec.avi", (frame_width, frame_height))
out = cv.VideoWriter("camrec.avi", cv.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))
# out = cv.VideoWriter("resources/camrec_video.avi", cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))


while (True):
    (ret, frame) = cap.read()
    # to show in player
    if ret == True:
        out.write(frame)
        cv.imshow('Video', frame)
        # to quit with q key
        if cv.waitket(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows