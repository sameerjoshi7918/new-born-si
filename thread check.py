import cv2
import time
import os
import pyautogui as pg
from threading import Thread

def calling():
    titles=pg.getAllTitles()
    print(titles)
    for i in range(len(titles)):
        if 'c1' in titles[i]:
            #print(titles[i])
            print('c1')
            openit=titles[i]
            pg.getWindowsWithTitle(openit)[0].minimize()
                
    


cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

def hota():
    if os.path.exists("c1.png"):
        os.remove("c1.png")
        cv2.imshow('c1',frame) #display the captured image
        cv2.imwrite('c1.png',frame)
        #pg.getWindowsWithTitle('c1')[0].minimize()
        
        
    else:
        print("The file does not exist")

        cv2.imshow('c1',frame) #display the captured image
        cv2.imwrite('c1.png',frame)
        #Win32Window(hWnd=10815782)
        #pg.getWindowsWithTitle('c1')[0].minimize()

title=pg.getAllTitles()
titles=list(title)
print(titles)
for i in range(len(titles)):
    if 'c1' in titles[i]:
        print(titles[i])
        print('photo found')
        openit=titles[i]
        print(i)

#cap.release()
hota()




