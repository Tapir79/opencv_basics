import cv2
import numpy as np

# color images have 3 channels, red, green and blue
image = cv2.imread("../00_images/red_panda.jpg")
rows, cols, ch = image.shape

# the whole image
roi = image[0: rows, 0: cols]
# the cut image
roi2 = image[150:rows, 150:cols]

cv2.imshow("Red panda", image)
cv2.imshow("Roi", roi2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#######################################
#
# a[start:end] # items start through the end (but the end is not included!)
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through the end (but the end is not included!)
#
#######################################