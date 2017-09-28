import serial
import time
import cv2
arduino =serial.Serial("/dev/ttyUSB0",38400)
send_str ="t\n"
camera =cv2.VideoCapture(0)
ret ,frame = camera.read()

while True:

    cv2.imshow("frame",frame)
    k = cv2.waitKey(1) & 0xff
    if k==ord("a"):
        send_str="a\n"
    if k==ord("d"):
        send_str="d\n"
    if k==ord("w"):
        send_str="w\n"
    if k==ord("s"):
        send_str="s\n"
    if k==ord("t"):
        send_str="t\n"
    if k==ord("q"):
        break
    arduino.write(send_str)
    time.sleep(0.01)

cv2.destroyAllWindows()
camera.release()
