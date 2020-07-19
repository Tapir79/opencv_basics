import cv2
import numpy as np

singapore_video_name = "Standard_SCU5ZI_2019-09-18_0630.001"
road_car_video_name = "road_car_view"

vname = singapore_video_name

video  = cv2.VideoCapture("../00_videos/"+vname+".mp4")

while True:
    # ret = true/false , if true still a frame, false no more video
    ret, original_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("../00_videos/"+vname+".mp4")
        continue

    frame = cv2.GaussianBlur(original_frame, (5,5), 0)
    # convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_yellow = np.array([18, 94, 140])
    up_yellow = np.array([48, 255, 255])

    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    edges = cv2.Canny(mask, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    green = (0, 255, 0)

    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(frame, (x1,y1), (x2,y2), green, thickness = 3)

    # get the edges of the frame image
    # gray = cv2.cvtColor("")

    cv2.imshow("Image", frame)
    cv2.imshow("Edges", edges)
    key = cv2.waitKey(25)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()


