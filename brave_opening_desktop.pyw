import os
import pyautogui as pg
import keyboard as kd
import time
def keyboard_jarvis():
    print('started')
    kd.wait('j')
    kd.wait('a')
    kd.wait('r')
    kd.wait('v')
    kd.wait('i')
    kd.wait('s')
    titles=pg.getActiveWindowTitle()
    title=titles.lower()
    if '' in title:
        pg.moveTo(507, 852, 1)
        time.sleep(0.3)
        pg.click()
        time.sleep(0.3)
        pg.press('enter')
        time.sleep(2)
        pg.moveTo(1191, 379, 1)
        pg.click()
        time.sleep(0.3)
        def cc():
            pg.scroll(-100)
            cm=pg.locateOnScreen(r'C:\Users\samee\Pictures\Screenshots\jarvis_found.png')
            cn=str(cm)
            if cn=='None':
                time.sleep(1)
                cc()
            else:
                pg.moveTo(cm)
                time.sleep(0.3)
                pg.click()
                time.sleep(0.3)
                pg.press('enter')
        cc()
        time.sleep(1)
        openit='normal_jarvis'
        pg.getWindowsWithTitle(openit)[0].close()
    else:
        keyboard_jarvis()
keyboard_jarvis()
