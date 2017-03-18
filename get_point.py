import cv2

def run(im):
    img_disp = im.copy()
    img_draw = im.copy()
    cv2.imshow("track",img_draw)
