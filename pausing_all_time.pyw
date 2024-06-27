import pyautogui as pg
import time
import keyboard as kd
from threading import Thread
import os

aa=[1]
def pause():
    length=int(len(aa))
    time.sleep(0.5)
    titles=pg.getActiveWindowTitle()
    title=titles.lower()
    if 'whatsapp' in title or 'idle' in title or 'untitled' in title or 'txt' in title or 'instagram' in title or 'libre' in title or 'google' in title or 'ola' in title or 'mkv' in title or 'jack' in title or 'youtube' in title or 'coursera' in title or '•' in title or 'normal_jarvis' in title:
        pause()
    else:
        kd.wait(hotkey='space')
        titlt=pg.getActiveWindowTitle()
        titu=titlt.lower()
        if 'whatsapp' in titu or 'idle' in titu or 'untitled' in titu or 'txt' in titu or 'instagram' in titu or 'libre' in titu or 'google' in titu or 'ola' in titu or 'mkv' in titu or 'jack' in titu or 'youtube' in titu or 'coursera' in titu or '•' in titu or 'normal_jarvis' in titu:
            pause()
        else:
            if length%2==1:
                if 'vlc' in titu:
                    pg.hotkey('ctrl','win','right')
                    time.sleep(0.5)
                    titles22=pg.getActiveWindowTitle()
                    title22=titles22.lower()
                    if 'vlc' in title22:
                        pg.hotkey('ctrl','win','d')
                    aa.append(length)
                    os.startfile(r'C:\Users\samee\Desktop\Third Year\CS\SEM 5')
                    pause()
                else:
                    pg.hotkey('ctrl','win','right')
                    aa.append(length)
                    pause()
            else:
                pg.hotkey('ctrl','win','left')
                aa.append(length)
                pause()
        print(title)
pause()
