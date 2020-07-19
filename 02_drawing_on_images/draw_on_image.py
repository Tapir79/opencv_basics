import cv2
import numpy as np

image = cv2.imread("../00_images/red_panda.jpg")

shape = image.shape
print(shape)

blue = (255, 0 , 0)
red = (0, 0, 255)
green = (0, 255, 0)
violet = (180,0, 180)
yellow = (0, 180, 180)
white = (255, 255, 255)

cv2.line(image, (0, 200), (450,350), blue, thickness = 5)
cv2.circle(image, (20,20), 20, red, thickness =10)
cv2.rectangle(image, (50,60),(450,95), green, thickness = 4)

# image, coordinates, ellipse size, rotation degree, circle, color, thickness
cv2.ellipse(image, (80,100), (100,50), 0, 0, 90, violet, -1)
cv2.ellipse(image, (230,150), (80,20), 20, 0, 180, violet, -1)
cv2.ellipse(image, (370,150), (80,20), 90, 0, 360, violet, -1)

points = np.array([[129,130],[400,230], [320, 250], [280, 250]], np.int32)
cv2.polylines(image, [points], True, yellow, thickness = 4)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, "Panda", (20, 100), font, 4, white)

cv2.imshow("red panda", image)
cv2.waitKey(0)
cv2.destroyAllWindows()