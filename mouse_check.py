import win32api
import time
import return_to_jarvis
def mouce():
    savedpos = win32api.GetCursorPos()
    time.sleep(6)
    curpos = win32api.GetCursorPos()
    if savedpos == curpos:
        return_to_jarvis.back_to_jarvis()

#mouse_check.mouce()
