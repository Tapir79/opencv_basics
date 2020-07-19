import cv2
import numpy as np

orange = cv2.imread("../00_images/orange.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("../00_images/balls.jpg", cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# fill the holes
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(mask, kernel)

# separate balls close to each other, mask, kernel, iterations
erosion = cv2.erode(mask, kernel, iterations=4)

cv2.imshow("gray img", img)
cv2.imshow("mask", mask)
cv2.imshow("Dilation", dilation)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

