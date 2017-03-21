import cv2
import dlib
from skimage import io
import glob
import numpy as np

camera = cv2.VideoCapture(0)
pt1=[]
pt2=[]
global CATCH_FLAGS
CATCH_FLAGS=False
tracker = dlib.correlation_tracker()


def selectroi(event,x,y,flags,param):
    global CATCH_FLAGS
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1.append((x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        pt2.append((x,y))
        CATCH_FLAGS =True



print "Press key i to select "
while True:
    ret, frame = camera.read()
    cv2.imshow("frame",frame)
    cv2.setMouseCallback("frame", selectroi)
    if cv2.waitKey(1) & 0xff == ord("i"):
        break

cv2.setMouseCallback("frame",selectroi)
while CATCH_FLAGS is not True:
    cv2.imshow("frame",frame)
    cv2.waitKey(1) & 0xff
cv2.destroyWindow("frame")

img_select = frame[pt1[-1][1]:pt2[-1][1], pt1[-1][0]:pt2[-1][0]]
img_select1 =np.array(img_select,dtype=np.uint8)
x=pt1[-1][0]
y=pt1[-1][1]
w = pt2[-1][0]-pt1[-1][0]
h = pt2[-1][1]- pt1[-1][1]
tracker.start_track(frame,dlib.rectangle(pt1[-1][0],pt1[-1][1],pt2[-1][0],pt2[-1][1]))
win = dlib.image_window()
while True:

    cv2.imshow("img",img_select1)
    tracker.update(frame)
    print tracker.get_position().center()
    win.clear_overlay()
    win.set_image(frame)
    win.add_overlay(tracker.get_position())
    ret, frame = camera.read()
    cv2.imshow("frame",frame)
    #tracker.start_track(frame,img_select)


    if cv2.waitKey(1) & 0xff ==ord("q"):
        break
cv2.destroyAllWindows()
camera.release()

