import cv2
import numpy as np

img1 = cv2.imread("../00_images/drawing_1.png")
img2 = cv2.imread("../00_images/drawing_2.png")
bit_and = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
bit_xor = cv2.bitwise_xor(img1,img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

# bit_and
# black and black = black
# black and white = black
# white and white = white
#cv2.imshow("bit_and", bit_and)

# bit_or
# black and black = black
# black and white = white
# white and white = white
#cv2.imshow("bit_or", bit_or)

# bit_xor
# black and black = black
# black and white = white
# white and white = black
#cv2.imshow("bit_xor", bit_xor)

# bit_not
cv2.imshow("bit_not", bit_not)

# bit_not2
cv2.imshow("bit_not2", bit_not2)

cv2.waitKey(0)
cv2.destroyAllWindows()