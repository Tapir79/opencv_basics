import numpy as np
import cv2
from matplotlib import pyplot as plt

img = np.zeros((100, 100), np.uint8)

black = 0
white = 255

# draw a white rectagle on image, -1 = fill it with color
cv2.rectangle(img, (0,50),(100,100), (255), -1)
cv2.circle(img, (50,50), 25, 127, thickness=-1)

cv2.imshow("img", img)

# img, size, histogram value range
plt.hist(img.ravel(), 256, (0,256))
# histogram will show 4000 pixels of 0 value and 4000 pixels of 255 value
# and 2000 pixels of 127 value
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
