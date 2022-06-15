# converting video into gray or black and white and saving
import cv2 as cv

cap = cv.VideoCapture('resources/video.mp4')

# writing format, codec, video writer object and file output

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/Out_video.avi", cv.VideoWriter_fourcc("M", "j", "P", "G"), 10, (frame_width, frame_height))

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # to show in player
    if ret == True:

        cv.imshow('Video', grayframe)
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
