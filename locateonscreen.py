

import pyautogui as pg
import time
import webbrowser
time.sleep(4)
#webbrowser.open('https://open.spotify.com/')
#time.sleep(4)
#im = pg.screenshot('save.png')
x=pg.locateCenterOnScreen('images\sameer_playlist_opened.png')
print(x)
strx=str(x)
xi=pg.locateCenterOnScreen('images\spotify_opened.png')
print(xi)
webbrowser.open('https://www.google.com')
if strx=='None' and xi=='None':
    webbrowser.open('https://open.spotify.com/')
    time.sleep(0.3)
    pg.moveTo(xi)
    pg.moveRel(106,0)
    time.sleep(0.3)
    pg.click()
    time.sleep(1)
    webbrowser.open('https://open.spotify.com/')
else:
    time.sleep(0.3)
    pg.moveTo(xi)
    pg.moveRel(106,0)
    time.sleep(0.3)
    pg.click()
    time.sleep(1)
    webbrowser.open('https://open.spotify.com/')
    
pg.moveTo(xi)

