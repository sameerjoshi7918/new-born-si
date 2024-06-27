#camera unlock
import pyautogui as pg
import time
import win32api
import mouse_check
import playsound
def camera_start():
    playsound.playsound('audios\kitni_photos_kheechna_chahte_he_sir.mp3')
    count=pg.prompt('kitni photos kheechne chahte he sir? ')
    #kuch speech recognition for input
    playsound.playsound('Time_interval_in_2_photos_in sec.mp3')
    interval_in_photos=int(pg.prompt('Time interval in 2 photos in sec :'))
    sr=s.Recognizer()
    print('eNTER something : ')
    with s.Microphone() as m:
        audio=sr.listen(m)
        interval_in_photos_see=sr.recognize_google(audio, language='eng-in')
        interval_in_photos=str(interval_in_photos_see)
    if count.isnumeric():
        
        pg.moveTo(550,1050, 2)
        time.sleep(1)
        pg.click()
        time.sleep(1)
        pg.write('camera', interval=0.3)
        time.sleep(1)
        pg.press('enter')
        for i in range(int(count)):
            pg.moveTo(1853, 527, 1)
            time.sleep(1)
            pg.click()
            time.sleep(interval_in_photos)
        pg.moveTo(1853, 938, 1)
        time.sleep(1)
        pg.click()
        savedpos = win32api.GetCursorPos()
        time.sleep(5)
        curpos = win32api.GetCursorPos()
        if savedpos == curpos:
            pg.moveTo(1880, 40, 3)
            time.sleep(1)
            pg.click()
