#checking if one photo is availabe on another photo or not
import cv2
from deepface import DeepFace
import os
import time
import pyautogui as pg

def start():
    time.sleep(3)
    if os.path.exists('images\screen_photo.png'):
        os.remove('images\screen_photo.png')
        pg.screenshot('images\screen_photo.png',region=(482,365,795,400))
    else:
        pg.screenshot('images\screen_photo.png',region=(482,365,795,400))
    reference_img1=cv2.imread('images\screen_photo.png')
    reference_img2=cv2.imread('images\play_button_spotify.png')
    if DeepFace.verify(reference_img1, reference_img2.copy())['verified']:
        face_match=True
        print('find from bed')
    else:
        print('nothing')
    
    #if os.path.exist('image\play_button_spotify.jpg')
#start()
