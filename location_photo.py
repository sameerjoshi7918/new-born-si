import pyautogui as pg
import time
time.sleep(3)
x, y = pg.locateOnScreen('box.png')
pg.click(x, y)
