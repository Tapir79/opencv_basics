import cv2
import numpy as np

# 0 first webcam on computer
cap = cv2.VideoCapture(0)

# start getting frame by frame
while True:
    ret, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("gray scale", gray_scale)
    cv2.imshow("frame", frame)
    # wait 1 millisecond
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()