#!/usr/bin/python
# -*- coding: utf-8 -*-

import dlib
import cv2
from skimage import io


camera = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()

cv2.namedWindow('frame')
cv2.moveWindow('frame', 100, 100)

while True:
    ret, frame = camera.read()

    dets = detector(frame,1)
    print len(dets)
    for i,d in enumerate(dets):
        print (format(d))
    print format(len(dets))

    win.set_image(frame)
    win.add_overlay(dets)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break



camera.release()
cv2.destroyAllWindows()
