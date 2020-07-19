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
laplacian_pyramid = [layer]
# start =5, stop = 0, -1 = reverse order
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize = size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)

reconstructed_image = laplacian_pyramid[0]
for i in range(1,6):
    # first check the laplacian pyramid image size. Then give the same size to the image that we are expanding
    # shape[1] = width of the image
    # shape[0] = height of the image
    size = (laplacian_pyramid[i].shape[1], laplacian_pyramid[i].shape[0])
    reconstructed_image = cv2.pyrUp(reconstructed_image, dstsize = size)
    reconstructed_image = cv2.add(reconstructed_image, laplacian_pyramid[i])
    cv2.imshow(str(i), reconstructed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()