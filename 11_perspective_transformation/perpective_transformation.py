import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.circle(frame, (215,260), 5, (0,0,255), -1)
    cv2.circle(frame, (430,260), 5, (0,0,255), -1)
    cv2.circle(frame, (185,385), 5, (0,0,255), -1)
    cv2.circle(frame, (470,385), 5, (0,0,255), -1)

    pts1 = np.float32([[215,260],[430,260],[185,385],[470,385]])
    pts2 = np.float32([[0,0],[400, 0],[0,600],[400,600]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)

    result = cv2.warpPerspective(frame, matrix,(400,600))

    cv2.imshow("Frame", frame)
    cv2.imshow("Perpective tranform", result)

    key = cv2.waitKey(1)
    if key == 27:
        break