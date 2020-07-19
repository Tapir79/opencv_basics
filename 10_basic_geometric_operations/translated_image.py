import cv2
import numpy as np

img = cv2.imread("../00_images/red_panda.jpg")
rows, cols, ch = img.shape

print("Height", rows)
print("Width", cols)
print("Channels", ch)

# move the image from 0,0 50 pixels to right, 50 pixels to left
matrix_trans = np.float32([[1, 0, 50], [0, 1, 50]])

translated_img = cv2.warpAffine(img, matrix_trans, (cols,rows))



cv2.imshow("Original image", img)
cv2.imshow("Translated image", translated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()