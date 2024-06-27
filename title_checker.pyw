#always background checker that check which title is running

import pyautogui as pg
import time
from threading import Thread
import pyttsx3 as pt
import playsound
import random
def sus():
    
    a=pg.getAllTitles()
    print('st')
    time.sleep(10)
    b=pg.getAllTitles()
    if a==b:
        #print('yes')
        sus()
    else:
        #print('not')
        for i in range(len(a)):
            try:
                
                if a[i]==b[i]:
                    del a[i]
                    del b[i]
                    
                else:
                    
                    index_b=str(b[i])
                    print(index_b)
                    if 'Brave' in index_b and 'Coursera' in index_b:
                        playsound.playsound('audios\Good to see you Studying.mp3')
                    elif 'VLC' in index_b:
                        cch=['a','b']
                        nw=random.choice(cch)
                        if nw=='a':
                            playsound.playsound('audios\Kya deekh rahe ho sir.mp3')
                        elif nw=='b':
                            playsound.playsound('audios\Konsi movie daikh rahe ho sar.mp3')
                            
                    break
                    sus()
            except:
                sus()
        sus()

sus()
