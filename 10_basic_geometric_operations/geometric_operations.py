import cv2
import numpy as np

img = cv2.imread("../00_images/red_panda.jpg")

cv2.imshow("Original image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()