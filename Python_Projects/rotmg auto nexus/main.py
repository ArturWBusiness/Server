from PIL import ImageGrab
import numpy as np
import cv2
import win32gui
import time
print("Scanning in 5s!")
time.sleep(5)
print("Scanning!")
flags, hcursor, (x,y) = win32gui.GetCursorInfo()
print("Scanned!")
print(x,y)
time.sleep(5)
print("Scanned!")
flags, hcursor, (x2,y2) = win32gui.GetCursorInfo()
print(x2,y2)
exit()
while True:
    img = ImageGrab.grab(bbox=(x, y, 400, 780))  # x,y,width,height
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("test", frame)
    cv2.waitKey(0)
cv2.destroyAllWindows()