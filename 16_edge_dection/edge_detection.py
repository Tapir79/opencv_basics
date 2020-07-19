""" CV_8U is unsigned 8bit/pixel - ie a pixel can have values 0-255,
this is the normal range for most image and video formats.

CV_32F is float - the pixel can have any value between 0-1.0,
this is useful for some sets of calculations on data -
but it has to be converted into 8bits to save or display by multiplying each pixel by 255.

CV_32S is a signed 32bit integer value for each pixel -
again useful of you are doing integer maths on the pixels,
but again needs converting into 8bits to save or display.
This is trickier since you need to decide how to convert the much larger range
of possible values (+/- 2billion!) into 0-255 """

import cv2
import numpy as np


img = cv2.imread('../00_images/white_panda.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (11,11), 0)
# You can try more different parameters
dstx = cv2.Sobel(img, cv2.CV_8U, 1, 0)
dsty = cv2.Sobel(img, cv2.CV_8U, 0, 1)

laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize=5)
canny = cv2.Canny(img, 100,150)


cv2.imshow('canvasOutputx', dstx)
cv2.imshow('canvasOutputy', dsty)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny)


cv2.waitKey(0)
cv2.destroyAllWindows()