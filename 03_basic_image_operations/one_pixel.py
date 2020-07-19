import cv2
import numpy as np

# color images have 3 channels, red, green and blue
image = cv2.imread("../00_images/flag.png")
# height, width
#print(image.shape)
# print 1 pixel color at coords 175,300
#print(image[175,300])

# image[y,x]
image[175,300] = (255, 0, 0)
image[175,301] = (255, 0, 0)
image[175,302] = (255, 0, 0)

# black and white have just 1 channel from black to white 0 - 255
image_grey_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image_grey_scale)

image_grey_scale[175,300] = 255
image_grey_scale[175,301] = 255
image_grey_scale[175,302] = 255
image_grey_scale[175,303] = 0
image_grey_scale[175,304] = 0
image_grey_scale[175,305] = 0

cv2.imshow("Grey Flag", image_grey_scale)
cv2.imshow("Flag", image)
cv2.waitKey(0)
cv2.destroyAllWindows()