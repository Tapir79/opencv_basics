import cv2
import numpy as np

img1 = cv2.imread("../00_images/road.jpg")
img2 = cv2.imread("../00_images/car.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)



# weighted
weighted = cv2.addWeighted(img1, 1, img2, 0.5, 0)
# take all the values from 0-252 will be black, all the values btw 252-255 are white
# inverted threshold
ret, mask = cv2.threshold(img2_gray, 252, 255, cv2.THRESH_BINARY_INV)

# sum pixels of the 2 images, after 255 everything is always white
sum = cv2.add(img2, img2, mask=mask)


#cv2.imshow("road",img1)
#cv2.imshow("car", img2)
cv2.imshow("graycar", img2_gray)
cv2.imshow("thrshold", mask)
cv2.imshow("sum", sum)
#cv2.imshow("weighted", weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
