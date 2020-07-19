import cv2
import numpy as np

early_1800 = cv2.imread("../00_images/early_1800.jpg")
balloons = cv2.imread("../00_images/balloons_noisy.png")
img = cv2.imread("../00_images/carpet.jpg")

# 5 pix and 5 pix height sums all these pixels and uses those average values for all pixels in 5,5
averaging = cv2.blur(img, (5,5))

# kernel 5x5 pixels, keeps more details in the image
gaussian_blur = cv2.GaussianBlur(img, (5,5), 0)

# median blur works for very noisy images
median = cv2.medianBlur(img, 5)

# bilateral
bilateral = cv2.bilateralFilter(img, 9, 250, 250)

cv2.imshow("original image", img)
cv2.imshow("averaged", averaging)
cv2.imshow("Gaussian blur", gaussian_blur)
cv2.imshow("Median", median)
cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

