import numpy as np
import cv2

img = cv2.imread("../00_images/red_panda.jpg")

# half
scaled_img = cv2.resize(img, None, fx=1/2, fy = 1/2)
# 1*2
scaled_img2 = cv2.resize(img, None, fx=1*2, fy = 1*2)

# random
scaled_img3 = cv2.resize(img, None, fx=3, fy=4)

cv2.imshow("Original image", img)
cv2.imshow("scaled image", scaled_img)
cv2.imshow("scaled image2", scaled_img2)
cv2.imshow("random scale", scaled_img3)

cv2.waitKey(0)
cv2.destroyAllWindows()