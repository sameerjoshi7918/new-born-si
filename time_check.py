import pyttsx3 as ppt
import datetime
import time
from threading import Thread
def time_check1():
    if int(datetime.datetime.now().hour) >= 12:
        a=datetime.datetime.now().hour
        aa=int(a)
        #ppt.speak(datetime.datetime.now().minute)
        #ppt.speak('P M')
        t=Thread(target=ppt.speak, args=[('its',aa-12,datetime.datetime.now().minute,'P M')])
        t.start()
        del t
    elif int(datetime.datetime.now().hour) < 12:
        t=Thread(target=ppt.speak, args=[('its',datetime.datetime.now().hour,datetime.datetime.now().minute,'A M')])
        t.start()
        del t
