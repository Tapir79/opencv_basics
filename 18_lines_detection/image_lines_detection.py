import cv2
import numpy as np

img = cv2.imread("../00_images/lines.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

# takes too much CPU
# cv2.HoughLines()

# less CPU
# The resulting rho and theta are indeed one step away from the line(s) you are looking for
# in the image. They represent a line passing through the origin that is perpendicular to
# the line you want to find.
# edges, rho, theta, threshold, lines, minLengthLine
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap = 250)

green = (0, 255, 0)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), green, thickness = 3)

cv2.imshow("Image", img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()