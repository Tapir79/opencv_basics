import cv2
import numpy as numpy

cap = cv2.VideoCapture("flipped_red_panda.avi")

# start getting frame by frame
while True:
    ret, frame = cap.read()
    # gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 0 = vertical
    flip_frame_vertical = cv2.flip(frame, 0)
    flip_frame_horizontal = cv2.flip(frame, 1)

    cv2.imshow("vertical flip", flip_frame_vertical)
    cv2.imshow("horizontal flip", flip_frame_horizontal)
    # wait 1 millisecond
    key = cv2.waitKey(25)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()