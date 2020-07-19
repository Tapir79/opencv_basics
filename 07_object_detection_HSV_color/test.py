# it's hard to use RGB so we convert the frame to HSV format
# in RGB there are 3 channels with colors to mix
# in HSV we have
# H = hue/the color 0 is red, max is violet
# S = saturation of the color 0 is white, max is full color
# V = lightness/value 0 is darkest, max lightest
# min = (0,0,0)
# max = (179, 255, 255)

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

### 6 trackbars to change HSV values in real time
cv2.namedWindow("tracks")

cv2.createTrackbar("LH", "tracks", 0, 179, nothing)
cv2.createTrackbar("LS", "tracks", 0, 255, nothing)
cv2.createTrackbar("LV", "tracks", 0, 255, nothing)
cv2.createTrackbar("UH", "tracks", 179, 179, nothing)
cv2.createTrackbar("US", "tracks", 255, 255, nothing)
cv2.createTrackbar("UV", "tracks", 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "tracks")
    l_s = cv2.getTrackbarPos("LS", "tracks")
    l_v = cv2.getTrackbarPos("LV", "tracks")
    u_h = cv2.getTrackbarPos("UH", "tracks")
    u_s = cv2.getTrackbarPos("US", "tracks")
    u_v = cv2.getTrackbarPos("UV", "tracks")

    lower_blue = np.array([l_h,l_s,l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()