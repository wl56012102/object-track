import dlib
import cv2

camera = cv2.VideoCapture(0)
pt1=[]
pt2=[]
img_copy=0
def drawcircle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        pt1.append((x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        pt2.append((x,y))
        cv2.rectangle(frame,pt1[-1],pt2[-1],(0,255,255),3)
        img_copy = frame[pt1[-1][1]:pt2[-1][1],pt1[-1][0]:pt2[-1][0]]
        cv2.imshow("frame",img_copy)


while True:
    ret ,frame = camera.read()
    
    cv2.setMouseCallback("img",drawcircle)
    if img_copy !=0:
        cv2.imshow("img",img_copy)
    print pt1,pt2
    cv2.imshow("frame",frame)
    k = cv2.waitKey(5) & 0xff

    if k ==ord("q"):
        break

cv2.destroyAllWindows()
camera.release()