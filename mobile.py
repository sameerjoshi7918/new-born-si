import pyautogui as pg
import os
import time
import playsound
from threading import Thread
import pyttsx3 as pt
call_log=['phone','call','krna','karna','lagana','call krna he','call lagana he','phone krna he','phone lagana he','phone karna he','call karna he']
call_names=['aai','baba','manutai','manu tai','kirmada','teena','vp','abbas']

def accessing_phone():
    t = Thread(target=playsound.playsound, args=["audios/What_do_you_want_to_do_with_phone.mp3"])
    t.start()
    del t
    mobile_what=pg.prompt('What do you want to do with phone')
    t = Thread(target=playsound.playsound, args=["audios\Kise_call_lagana_chahte_he_sir.mp3"])
    t.start()
    del t
    call_info=pg.prompt("Kise call lagana chahte he sir " )
    if mobile_what in call_log:
        pt.speak('Bssss, ek min, {} ji ko call laga raha hu'.format(call_info))
        time.sleep(1)
        pg.moveTo(550,1050)
        time.sleep(1)
        pg.click()

        pg.write('phone')
        time.sleep(1)
        pg.press('enter')
        time.sleep(2)
        pg.moveTo(1518, 214, 1)
        pg.click()
        time.sleep(2)
        pg.write('{}'.format(call_infor), interval=0.25)
        time.sleep(1)
        pg.press('enter')
        pg.moveTo(1518, 414, 1)
        pg.click()
        #time.sleep(2)
        pg.hotkey('pagedown')
        time.sleep(1)
        pg.moveTo(1621, 946, 1)
        pg.click() 

    
#accessing_phone()
