import numpy as np
import cv2
from matplotlib import pyplot as plt

img0 = np.zeros((100, 100), np.uint8)
img = cv2.imread("../00_images/sea.jpg", cv2.IMREAD_GRAYSCALE)

black = 0
white = 255

cv2.imshow("img", img)

# img, size, histogram value range
plt.hist(img.ravel(), 256, (0,256))
# histogram will show 4000 pixels of 0 value and 4000 pixels of 255 value
# and 2000 pixels of 127 value
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
