import cv2
import numpy as np

img = cv2.imread("../00_images/simpsons.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
""" template = cv2.imread("../00_images/barts_face.jpg")
gray_template = cv2.cvtColor(template, cv2.COLOR2GRAY) """
template = cv2.imread("../00_images/barts_face.jpg", cv2.IMREAD_GRAYSCALE)
# usually rows, cols
# [::-1] inverts order so cols, rows
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# result gives a new blac and white image where there is 1 white point that matches
# the template rectangle upleft corner point
# value 1 is completely white, find the highest value location
# find just 1 point
loc = np.where(result >= 0.9)
print('loc:',loc)
# loc: (array([44], dtype=int64), array([478], dtype=int64))
# unzip the array and invert the axis order
for pt in zip(*loc[::-1]):
    # pt = (44, 478)
    # draw on image where the template match is found
    # pt[0] = 44
    # pt[1] = 478
    cv2.rectangle(img, pt, (pt[0]+ w, pt[1]+h), (0, 255, 0), 3)

cv2.imshow("img", img)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
