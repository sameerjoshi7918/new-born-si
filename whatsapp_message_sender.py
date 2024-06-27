import webbrowser
import time
import pyautogui as pg
import return_to_jarvis
import playsound
from threading import Thread
import whatsapp_open_check
import datetime
                            

def wt_particular():
    hour=datetime.datetime.now().hour
    min1=datetime.datetime.now().minute
    name_of_wt_person=pg.prompt('Name')
    if name_of_wt_person=='manutai':
        name_of_wt_person='kirmada'
    if name_of_wt_person=='jarvis':
        print('Yes Boss!')
        playsound.playsound('audios\yesboss.mp3')
        return_to_jarvis.back_to_jarvis()
    t = Thread(target=playsound.playsound, args=["audios\Enter_message.mp3"])
    t.start()
    del t
    message=pg.prompt('Enter message : ')
    tim=pg.prompt('Enter time')
    time1=tim.split()
    if tim=='now' or tim=='Now':
        return None

        
    elif time1[0].isnumeric():
        def ok():
            hour=datetime.datetime.now().hour
            min1=datetime.datetime.now().minute
            if hour>12:
                hour=hour-12
                print(hour)
                if int(time1[0])==hour and int(time1[1])==min1:
                    return None
                else:
                    time.sleep(1)
                    ok()
            elif hour<12:
                if int(time1[0])==hour and int(time1[0])==min1:
                    return None
                else:
                    time.sleep(1)
                    ok()
        ok()
        
    whatsapp_open_check.call_this()
    def cc():
        time.sleep(1)
        a=pg.locateCenterOnScreen('images\wt_search.png')
        na=str(a)
        if na=='None':
            del na
            del a
            cc()
        else:
            pg.click(a)
            del a
            del na
    cc()
    #moving location of search name in whatsapp
    time.sleep(1)
    pg.write('{}'.format(name_of_wt_person), interval=0.1)
    time.sleep(1)
    pg.press('enter')
    time.sleep(0.3)
    pg.moveTo(1169, 965, 1)
    time.sleep(0.5)
    pg.click()
    pg.write('{}'.format(message), interval=0.1)
    pg.press('enter')
#wt_particular()
