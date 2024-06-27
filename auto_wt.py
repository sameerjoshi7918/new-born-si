from PIL import Image
import pytesseract
import pyautogui as pg
import os
import time
import cv2
import numpy as np
from PIL import Image
import datetime

import whatsapp_open_check

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
hourhe=datetime.datetime.now().hour
y_axis=['817']
fav_names=['Baba','Aai','Kuch bhi','Kirmada']
def poi():
    time.sleep(4)
    final1=pytesseract.image_to_string(Image.open('images\myfirst.png'))
    print(final1)
    a=final1.split()
    print(a)
    sifi=''
    try:
        for i in range(len(a)):
            if a[i]=='pm':
                ww=int(a.index('pm'))
                a.pop(ww)
                a.insert(ww, ' ')
                print(a, '\nPM FOUND')
                print('\n Your message at last')
                sifi='sifi'
                break
    except:
        pg.click(1623,300)
        pg.scroll(100)
        cc()
        poi()
    if sifi=='sifi':
        #lst message vala code
        unread1=pg.locateCenterOnScreen(r'images\unread1.png')
        unread=str(unread1)
        if unread=='None':
            print('no unread messages')
        else:
            print('please read the messages')
    else:
        unread1=pg.locateCenterOnScreen(r'images\unread.png')
        unread=str(unread1)
        if unread=='None':
            print('no unread messages')
        else:
            print('please read the messages')

def cc():
    if os.path.exists('images\mymessage.png'):
        os.remove('images\mymessage.png')
        im = pg.screenshot('images\myfirst.png',region=(1623,817, 235, 81))
    else:
        im = pg.screenshot('images\myfirst.png',region=(1623,817, 235, 81))
    time.sleep(1)

    
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
            im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 200, 32))
        else:
            im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 200, 32))
        try:
            wt_name1=pytesseract.image_to_string(Image.open('images\wt_chat_name.png'))
            wt_name=wt_name1.split()
            print(wt_name)
            name=str(wt_name[0])
            print(name,'line 89')
        except:
            if os.path.exists('images\wt_chat_name.png'):
                os.remove('images\wt_chat_name.png')
                im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 100, 32))
            else:
                im = pg.screenshot('images\wt_chat_name.png',region=(x1, y1, 100, 32))
            try:
                wt_name1=pytesseract.image_to_string(Image.open('images\wt_chat_name.png'))
                wt_name=wt_name1.split()
                print(wt_name1)
                name=str(wt_name1[0])
                print(name,'line 101')
            except:
                print('kahatarnak error')
                #name list is empty
        if (name[-1]=='a' or name[-1]=='e' or name[-1]=='i' or name[-1]=='o' or name[-1]=='u') and name!='Kirmada' and name!='Aai' and name!='Baba' and name!='Kuch bhi':
            gender='Girl'
            message='I appreciate your patience, please wait, Sameer will reach you soon'
            print(name,'line 108')
        elif name=='Baba':
            message='Hi, baba, sameer abhi kahi gaya he, thodi der me message karega.'
        elif name=='Aai':
            message='Hi aai, sameer abhi kahi gaya he, thodi der me message karega.'
        elif name=='Kirmada':
            message='Hola, amigo manutai, me thodi der se message krta hu'
        elif name=='Kuch bhi':
            message='Hola amigo, me abhi thoda busy hu, agar bura na mane to thodi der me bat krta hu'
        elif name=='Sunfeast':
            message='Hi sunfeast, added now'
        else:
            gender='Boy'
            message='wait for sameer for reaching'
        #pg.write('{}'.format(message))
        #time.sleep(1)
        #pg.press('enter')
        abc=[]
        def message_uppar():            
            if os.path.exists('images\message_got.png'):
                os.remove('images\message_got.png')
                if len(abc)<1:
                    print(y_axis)#################
                    newnum=int(y_axis[0])
                    y_axis.insert(0,newnum-81)
                    im = pg.screenshot('images\message_got.png',region=(1623, int(y_axis[0]), 235, 81))
                else:
                    newnum=int(y_axis[0])
                    if newnum<0:
                        pg.moveTo(1623, 300)
                        pg.click()
                        pg.scroll(-100)
                    else:
                        y_axis.insert(0,newnum-81)
                        im = pg.screenshot('images\message_got.png',region=(1623, int(y_axis[0]), 235, 81))
            else:
                if len(abc)<1:
                    print(y_axis)
                    im = pg.screenshot('images\message_got.png',region=(1623, int(y_axis[0]), 235, 81))
            time.sleep(1)
            final_mes=pytesseract.image_to_string(Image.open('images\message_got.png'))
            abq=final_mes.split()
            for i in range(len(abq)):
                if abq[i]=='pm' or 'am' in abq[i] or abq[i].isnumeric():
                    if hourhe>12:
                        a='PM'
                        ww=int(abq.index('pm'))
                    else:
                        a='AM'
                        try:
                            ww=int(abq.index('am'))
                        except:
                            try:
                                ww=int(abq.index('pm'))
                            except:
                                #write something
                                pg.moveTo(1623, 300)
                                pg.click()
                                pg.scroll(-100)
                    abq.pop(ww)
                    abq.insert(ww, ' ')
                    print(abq[i], '{} FOUND'.format(a))
                    print('Your message at last from message_uppar')
                    sifir='sifir'
                    break
            try:
                if 'sifir' in sifir:
                    pg.write('You send me {} messages, i think'.format(len(y_axis)-2))
                    pg.press('enter')
                    pg.write(message)
                    pg.press('enter')
                    print('Pg.move to only me function pr hu me')
                    pg.moveTo(359, 479)#only me location on whatsapp
                    pg.click()
                else:
                    abc.append('sameer')
                    time.sleep(0.3)
                    message_uppar()
            except:
                message_uppar()
        message_uppar()
    time.sleep(0.3)
    cc()
    poi()
    
    ok()
ok()
