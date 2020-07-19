# template must be quite exactly the same size and lightning/colors to match
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

template = cv2.imread("../00_images/smash.jpg", cv2.IMREAD_GRAYSCALE)
# usually rows, cols
# [::-1] inverts order so cols, rows
w, h = template.shape[::-1]
print(w)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.65)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+ w, pt[1]+h), (0, 255, 0), 3)

    cv2.imshow("gray template", template)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
