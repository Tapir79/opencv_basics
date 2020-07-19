import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../../00_images/sea_beach.jpg")
b, g, r = cv2.split(img)

black = 0
white = 255

cv2.imshow("img", img)
cv2.imshow("b img", b)
cv2.imshow("g img", g)
cv2.imshow("r img", r)


# img, size, histogram value range
plt.hist(b.ravel(), 256, (0,256))
plt.hist(g.ravel(), 256, (0,256))
plt.hist(r.ravel(), 256, (0,256))
# histogram will show 4000 pixels of 0 value and 4000 pixels of 255 value
# and 2000 pixels of 127 value
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
