import cv2
import numpy as np
from matplotlib import pyplot as plt

original_image = cv2.imread("../00_images/goalkeeper.jpg")
hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# roi = region of interest
roi = cv2.imread("../00_images/pitch_ground.jpg")
# hue, saturation, value
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# more detailed
hue, saturation, value = cv2.split(hsv_roi)


# 1st take the roi histogram
# images, channels, mask, histSize (hue=0-179, saturation 0-255), range (180 is not counted)
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
mask = cv2.calcBackProject([hsv_original], [0,1], roi_hist, [0, 180, 0, 256], 1)

# filter the noise from
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask = cv2.filter2D(mask, -1, kernel)
# apply threshold to remove even more noise
_, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)

# bitwise operation on 3 channel image
mask = cv2.merge((mask, mask, mask))
result = cv2.bitwise_and(original_image, mask)

cv2.imshow("Original", original_image)
cv2.imshow("Roi",roi)
cv2.imshow("mask", mask)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(roi_hist)
# plt.show()