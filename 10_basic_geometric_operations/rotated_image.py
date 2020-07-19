import cv2
import numpy as np

img = cv2.imread("../00_images/red_panda.jpg")
rows, cols, ch = img.shape

# centerpoint of the image , degree, scale (1=original size)
matrix_rot = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_img = cv2.warpAffine(img, matrix_rot, (cols,rows))

cv2.imshow("Original image", img)
cv2.imshow("Rotated image", rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()