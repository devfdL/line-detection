import cv2
import numpy as np

# input video from camera
video = cv2.VideoCapture(0)

while True:
    # Input frame from video
    ret, orig_frame = video.read()
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

    # Detecting white color
    lower = np.uint8([0, 200, 0])
    upper = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(hsv, lower, upper)
    edges = cv2.Canny(white_mask, 75, 150)

    # Line detection
    lines = cv2.HoughLinesP(edges, 5, np.pi/180, 100, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    cv2.imshow("frame", frame)
    #cv2.imshow("edges", edges)
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()