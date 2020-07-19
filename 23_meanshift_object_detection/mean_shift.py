# problems with meanshift: the window size is always the same
# we need to put the object into the frame for the algorithm to start detecting it

import cv2
import numpy as np

video = cv2.VideoCapture("../00_videos/mouthwash.avi")

# how to get the first frame
_, first_frame = video.read()
x = 300
y = 305
width = 100
height = 115

# region of interest
roi = first_frame[y: y + height, x : x + width]

# transfer roi image to hsv image
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# to calculate the background projection
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

# normalize the histogram values to get rid of anomalies
roi_hist_normalized = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
# cv2.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    _, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist_normalized, [0, 180], 1)
    # get the highest concentration of white points
    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
    x,y, w, h = track_window
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("mask", mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(60)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()