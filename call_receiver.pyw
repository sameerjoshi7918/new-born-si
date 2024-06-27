import pyautogui as pg
import time
import os
from threading import Thread
import playsound
import pyttsx3 as pt

def check():
    ll=pg.locateCenterOnScreen('images\incoming_call.png')
    call=str(ll)
    if call=='None':
        print('not found')
        time.sleep(7.5)
        check()
    else:
        a=pg.position()
        time.sleep(5)
        b=pg.position()
        if a==b:
            t=Thread(target=pt.speak, args=["call received"])
            t.start()
            del t
            pt.speak('call received')
            pg.moveTo(1449, 910)
            pg.click()
            time.sleep(3)
            t=Thread(target=playsound.playsound, args=["audios\caller.mp3"])
            t.start()
            del t
            check()
        else:
            check()
        
        
check()


