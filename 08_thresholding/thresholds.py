# threshold
#
#

import cv2
import numpy as np

def nothing(x):
    pass

img_bw = cv2.imread("../00_images/black_to_white.jpeg", cv2.IMREAD_GRAYSCALE)

# print(img.shape)
# print(img[0,0])
# print(img[0,250])
cv2.namedWindow("image")
cv2.createTrackbar("lower", "image", 0, 255, nothing)
img = cv2.imread("../00_images/red_panda.jpg", cv2.IMREAD_GRAYSCALE)

while True:
    lower = cv2.getTrackbarPos("lower", "image")
    # image, min_value, max_value, type
    # set everything from 0- 128 to zero value
    # everything else is 255
    _, threshold_binary = cv2.threshold(img, lower, 255, cv2.THRESH_BINARY)
    _, threshold_binary_inv = cv2.threshold(img, lower, 255, cv2.THRESH_BINARY_INV)
    # all is kept btw 0-128 and above 128 is 128
    _, threshold_binary_trunc = cv2.threshold(img, lower, 255, cv2. THRESH_TRUNC)
    # from 100-255, everything below 100 is 0
    _, threshold_to_zero = cv2.threshold(img, lower, 255, cv2.THRESH_TOZERO)
    _, threshold_to_zero_inv = cv2.threshold(img, lower, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow("image", img)
    cv2.imshow("binary", threshold_binary)
    cv2.imshow("binary_inv", threshold_binary_inv)
    cv2.imshow("binary_trunc", threshold_binary_trunc)
    cv2.imshow("th to zero", threshold_to_zero)
    cv2.imshow("th to zero inv", threshold_to_zero_inv)

    key = cv2.waitKey(100)
    if key == 27:
        break

cv2.destroyAllWindows()