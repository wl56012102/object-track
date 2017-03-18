import dlib
import cv2
import get_point

camera = cv2.VideoCapture(0)
cv2.namedWindow("Image")
cv2.moveWindow("Image",100,100)

while True:
    ret, img = camera.read()
    cv2.imshow("Image",img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('i'):
        cv2.destroyWindow("Image")
        break

area = get_point.run(img)
print area

while True:
    ret,img2= camera.read()
    cv2.imshow("Image",img2)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyWindow("Image")
        break

