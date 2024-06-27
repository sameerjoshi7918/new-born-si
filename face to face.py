import os
import pyautogui as pg
import time

os.startfile('c1.png')
time.sleep(5)
aa=pg.locateOnScreen('sameer_side.png')
a=str(aa)
if a=='None':
    print('not found')
else:
    print('found')
'''
if os.path.exists("c1.png"):
    os.remove("c1.png")
    cv2.imshow('c1',frame) #display the captured image
    cv2.imwrite('c1.png',frame)
    if pg

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
'''
