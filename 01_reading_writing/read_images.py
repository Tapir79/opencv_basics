import numpy
import cv2

image = cv2.imread("../00_images/red_panda.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Red panda", image)
cv2.imshow("Grey panda", gray_image)

# waits for a key before window is closed
cv2.waitKey(0)
cv2.destroyAllWindows()
