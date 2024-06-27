from threading import Thread
import webbrowser
import pyautogui as pg


t = Thread(target=pg.moveTo, args=[45,35])
t.start()
t2=Thread(target=pg.click())
t2.start()
