from PIL import Image
import pytesseract
import pyautogui as pg
import os
import time
import cv2
import numpy as np
import datetime

import whatsapp_open_check
hourhe=datetime.datetime.now().hour
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def ok():
    whatsapp_open_check.call_this()
    if hourhe>12:#am pm photo check for screen shot
        we=pg.locateCenterOnScreen(r'images\unread_pm.png')
    else:
        we=pg.locateCenterOnScreen(r'images\unread_am.png')
    
    wed=str(we)
    if wed=='None':
        print('no unreaded message from ok vala func')
    else:
        pg.moveTo(we)
        pg.moveRel(-623, -16)
        x1,y1=pg.position()
        pg.moveRel(0,35)
        pg.click()#click on unraed chat
        if os.path.exists('images\wt_chat_name.png'):
            os.remove('images\wt_chat_name.png')
            im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 1107, 838))
        else:
            im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 1108, 838))
        try:
            wt_name1=pytesseract.image_to_string(Image.open('images\wt_chat_name.png'))
            wt_name=wt_name1.split()
            print(wt_name1)
            name=str(wt_name[0])
        except:
            if os.path.exists('images\wt_chat_name.png'):
                os.remove('images\wt_chat_name.png')
                im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 300, 32))
            else:
                im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 300, 32))
            try:
                wt_name1=pytesseract.image_to_string(Image.open('images\wt_chat_name.png'))
                wt_name=wt_name1.split()
                print(wt_name1)
                name=str(wt_name[0])
            except:
                name=pytesseract.image_to_string(Image.open('images\wt_chat_name.png'))
                print('kahatarnak error')
                print(name)
        del x1,y1
    a=pg.locateCenterOnScreen(r'images\unread1.png')
    aa=str(a)
    if aa=='None':
        a=pg.locateCenterOnScreen(r'images\unread2.png')
        aa=str(a)
        if aa=='None':
            a=pg.locateCenterOnScreen(r'images\unread3.png')
            aa=str(a)
            pg.moveTo(a)
            time.sleep(1)
            pg.moveRel(-532,0)
        pg.moveTo(a)
        time.sleep(1)
        pg.moveRel(-532,0)
    else:
        pg.moveTo(a)
        time.sleep(1)
        pg.moveRel(-532,0)
        ###############################################################
    x1,y1=pg.position()
    x1=56
    if x1 in range(1200,1400):
        print('theek he')
    else:
        pg.moveTo(774, 904)
        if os.path.exists(r'images\chek_for_last.png'):
            os.remove(r'images\chek_for_last.png')
            im = pg.screenshot(r'images\chek_for_last.png',region=(774, 904, 300,250))
        else:
            im = pg.screenshot(r'images\chek_for_last.png',region=(774, 904, 300,250))
    def call():
        if os.path.exists(r'images\all_messages.png'):
            os.remove(r'images\all_messages.png')
            im = pg.screenshot(r'images\all_messages.png',region=(x1, y1, 600,600))
        else:
            im = pg.screenshot(r'images\all_messages.png',region=(x1, y1, 600,600))
    call()
ok()
