import dlib
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, img = camera.read()

    cv2.imshow("Image",img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break