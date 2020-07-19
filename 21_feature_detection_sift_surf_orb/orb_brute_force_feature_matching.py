# Do not use this with video, uses a lot of CPU power

import cv2
import numpy as np

img1 = cv2.imread("../00_images/the_book_thief.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../00_images/me_holding_book.jpg", cv2.IMREAD_GRAYSCALE)
# scale_percent = 30 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# img = cv2.resize(img, dim)

orb = cv2.ORB_create()
# you can also use sift or suft detectors

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# for d in des1:
#     print(d)

# compare des1 with des2 and the most similar one is a match
# Brute force matching
# with orb we use norm hamming, crossCheck True will take only the best result
# create brute force object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#match the descriptors
matches = bf.match(des1, des2)
# sort matches by distance
matches = sorted(matches, key = lambda x:x.distance)

# take only 20 best, flags=2 don't show all detected features
matching_result_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

cv2.imshow("image1", img1)
cv2.imshow("image2", img2)
cv2.imshow("matching_result_img", matching_result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()