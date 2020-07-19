# if you have cv2 import error, deactivate venv
import cv2
import numpy as numpy

cap = cv2.VideoCapture("red_panda_snow.mp4")

# XVID codex is avi format
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# name, codek, frames per second, size of video
out = cv2.VideoWriter("flipped_red_panda.avi", fourcc, 25, (640, 360))

# start getting frame by frame
while True:
    ret, frame = cap.read()
    # how to get video size
    print(frame.shape)
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 0 = vertical
    flip_frame_vertical = cv2.flip(frame, 0)
    flip_frame_horizontal = cv2.flip(frame, 1)

    # show videos
    cv2.imshow("gray scale", gray_scale)
    cv2.imshow("original", frame)
    cv2.imshow("vertical flip", flip_frame_vertical)
    cv2.imshow("horizontal flip", flip_frame_horizontal)

    # save video
    out.write(flip_frame_vertical)

    # wait 1 millisecond
    key = cv2.waitKey(25)
    if key == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()