#volumne up
import pyautogui as pg
import time
from threading import Thread
def final_volume_up():
    volu=int(pg.prompt('kitni aavaz badhau sir? '))
    if volu%2=='0':
        final_vol=volu/2
        for i in range(int(final_vol)):
            pg.hotkey('volumeup')
    else:
        final_volu=(volu+1)/2
        for i in range(int(final_volu)):
            pg.hotkey('volumeup')
        
def final_volume_down():
    volu=int(pg.prompt('kitni aavaz kam karu sir? '))
    if volu%2=='0':
        final_vol=volu/2
        for i in range(int(final_vol)):
            pg.hotkey('volumedown')
            time.sleep(0.5)
    else:
        final_volu=(volu+1)/2
        for i in range(int(final_volu)):
            pg.hotkey('volumedown')
            time.sleep(0.5)

def final_volume_full():
    for i in range(50):
        pg.hotkey('volumeup')

def final_volume_mute():
    for i in range(40):
        pg.hotkey('volumedown')
        time.sleep(0.1)
#volume_check.final_volume_up()





