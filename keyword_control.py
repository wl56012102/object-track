import serial
import time
import cv2
arduino =serial.Serial("/dev/ttyUSB0",38400)
send_str ="t"
camera =cv2.VideoCapture(0)
ret ,frame = camera.read()

while True:

    cv2.imshow("frame",frame)
    k = cv2.waitKey(2) & 0xff
    if k==ord("a"):
        send_str="a"
    elif k==ord("d"):
        send_str="d"
    elif k==ord("w"):
        send_str="w"
    elif k==ord("s"):
        send_str="s"
    elif k==ord("t"):
        send_str="t"
    elif k==ord("q"):
        send_str="t"
        break
    else:
        send_str="t"
    arduino.write(send_str)
    time.sleep(0.02)

cv2.destroyAllWindows()
camera.release()