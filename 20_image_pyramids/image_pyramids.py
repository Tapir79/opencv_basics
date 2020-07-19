import cv2
import numpy as np

img = cv2.imread("../00_images/hand.jpg")

# create Gaussian pyramid
# We can find Gaussian pyramids using cv.pyrDown() and cv.pyrUp() functions.
layer = img.copy()
gaussian_pyramid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

# create laplacian (laplaacian) pyramid
layer = gaussian_pyramid[5]
cv2.imshow("6", layer)
laplacian_pyramid = [layer]
# start =5, stop = 0, -1 = reverse order
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize = size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)
    cv2.imshow(str(i), laplacian)


cv2.imshow("Gaussian 0", gaussian_pyramid[0])

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()