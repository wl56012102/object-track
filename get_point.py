import cv2

def run(im):
    global img_track
    img_disp = im.copy()
    img_draw = im.copy()
    pot1=[]
    pot2=[]
    run.mouse_down =False
    run.track_flag = False

    cv2.imshow("track", img_draw)
    cv2.moveWindow("track", 100, 100)

    def select_roi(event, x, y, flags, param):
        global img_track
        if event == cv2.EVENT_LBUTTONDOWN:
            pot1.append((x,y))
            run.mouse_down =True
        elif event == cv2.EVENT_LBUTTONUP and run.mouse_down ==True:
            pot2.append((x,y))
            img_track = img_draw[pot1[-1][0]:x,pot1[-1][1]:y]
            return img_track
            run.track_flag =True
            cv2.destroyWindow("track")


    cv2.setMouseCallback("track", select_roi)
    if run.track_flag == True:
        while True:
            cv2.imshow("track", img_track)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                cv2.destroyWindow("Image")
                break

