import cv2
import numpy as np

img = cv2.imread("../00_images/squares.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
green = (0,255,0)
red = (0, 0, 255)

# the image to detect, max corners, qualityLevel, minDistance = distance btw each corner
corners = cv2.goodFeaturesToTrack(gray_image, 150, 0.80, 40)
#print(corners)

#int0 is alias for intp. Integer used for indexing. Int32 or int64. Removes the dot in [36. 262.] => [36 262]
corners = np.int0(corners)
#print(corners)

for corner in corners:
    # numpy ravel function Return a contiguous flattened array.
    # x and y are destructured from an array into 2 variables
    x,y = corner.ravel()
    # x,y, radius, color, thickness=-1 means we fill the circle
    cv2.circle(img, (x,y), 5, red, -1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()