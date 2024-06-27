import cv2
from deepface import DeepFace
import time
import os
import pyautogui as pg
name=[]
def check():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    ret,frame = cap.read() # return a single frame in variable `frame`

    if os.path.exists("new_check.png"):
      os.remove("new_check.png")
      cv2.imwrite("new_check.png", frame)
    else:
      cv2.imwrite("new_check.png", frame)
    cap=cv2.VideoCapture(0)
    reference_img1=cv2.imread('images\sameer_bed.jpg')
    reference_img2=cv2.imread('new_check.png')
    rf1=cv2.imread('images\sameer_bed.jpg')
    try:
        
        if DeepFace.verify(reference_img1, reference_img2.copy())['verified']:
            face_match=True
            print('find from bed')
            check()
        else:
            if DeepFace.verify(reference_img2, rf1.copy())['verified']:
                face_match=True
                print('find on chair')
                check()
        name.clear()
    except ValueError:
            
        print('Not found')
        if len(name)>20:
            #me nahi hu, to baki ke functions.
            print('')
        else:
            name.append('sameer')
            print(name)
        check()
        
    check()
check()
