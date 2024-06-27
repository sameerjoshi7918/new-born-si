import pyautogui as pg
import time
from threading import Thread
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def start_check():
    time.sleep(1)
    titles=pg.getActiveWindowTitle()
    if 'OlaMovies' in titles:
        print('ola tab')
        if os.path.exists(r'images\olamoviename.png'):
            os.remove(r'images\olamoviename.png')
            im = pg.screenshot('images\olamoviename.png',region=(429, 69, 200, 40))
        else:
            im = pg.screenshot('images\olamoviename.png',region=(429, 69, 200, 40))
            
        site_url=pytesseract.image_to_string(Image.open('images\olamoviename.png'))
        site_url=str(site_url)
        site_url=site_url.strip()
        f=open(r'txt_files\ola.txt','a+')
        f.seek(0)
        a=f.readlines()
        c=a[-1]
        b=str(c.replace('\n',''))
        b=b.strip()
        if b==site_url:
            print('')
        elif b!=site_url:
            print(b,site_url)
            print('else vali condition')
            f.write('{}'.format(site_url))
            f.close()
            start_check()

        f.close()
        
        
    else:
        print('not found')
        start_check()

start_check()
