import cv2
import numpy as np
import time
import dlib

def selectROI(event,x,y,flags,param):
    global aa,bb
    if event == cv2.EVENT_LBUTTONDOWN:
        a,b=x,y
        aa=(a,b)
    if event == cv2.EVENT_LBUTTONUP:
        c,d=x,y
        bb=(c,d)


camera = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cv2.moveWindow('frame', 100, 100)


while True:
    ret, frame = camera.read()
    cv2.imshow('frame',frame)

    cv2.setMouseCallback('frame', selectROI)
    if aa is not None:
        cv2.rectangle(frame,aa,bb,(0,255,0),2,2)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r') :
        a = 1
        img = frame


    if key == ord('q'):
        break



camera.release()
cv2.destroyAllWindows()