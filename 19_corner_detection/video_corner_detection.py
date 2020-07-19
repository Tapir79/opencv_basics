import cv2
import numpy as np

def nothing(x):
    pass

cap  = cv2.VideoCapture(0)
green = (0,255,0)
red = (0, 0, 255)

# Trackbars
cv2.namedWindow("Frame")
cv2.createTrackbar("quality", "Frame", 1, 100, nothing)


while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    quality = cv2.getTrackbarPos("quality", "Frame")
    quality = quality / 100 if quality > 0 else 0.01
    corners = cv2.goodFeaturesToTrack(gray_frame, 100, quality, 10)

    if corners is not None:
        corners = np.int0(corners)
        for corner in corners:
            # numpy ravel function Return a contiguous flattened array.
            # x and y are destructured from an array into 2 variables
            x,y = corner.ravel()
            # x,y, radius, color, thickness=-1 means we fill the circle
            cv2.circle(frame, (x,y), 3, red, -1)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()