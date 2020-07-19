import cv2
import numpy as np

img1 = cv2.imread("../00_images/road.jpg")
img2 = cv2.imread("../00_images/car.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# take all the values from 0-252 will be black, all the values btw 252-255 are white
# inverted threshold
#ret, maskinv = cv2.threshold(img2_gray, 252, 255, cv2.THRESH_BINARY_INV)
ret, mask = cv2.threshold(img2_gray, 252, 255, cv2.THRESH_BINARY)
maskinv = cv2.bitwise_not(mask)

road = cv2.bitwise_and(img1, img1, mask=mask)
car = cv2.bitwise_and(img2,img2, mask=maskinv)
sum = cv2.add(road,car)

#cv2.imshow("road",img1)
#cv2.imshow("car", img2)
""" cv2.imshow("img1 bitwise mask", road)
cv2.imshow("thrshold road", mask)
cv2.imshow("threshold car", car) """
cv2.imshow("sum",sum)

cv2.waitKey(0)
cv2.destroyAllWindows()
