#alarm
import datetime
import playsound
import pyautogui as pg
import time
from threading import Thread

def alarm_set():
    last=pg.position()
    pmam='am'
    now=datetime.datetime.now()
    print(datetime.datetime.now().hour)
    cur_hour=int(datetime.datetime.now().hour)
    
    print(datetime.datetime.now().minute)
    cur_min=int(datetime.datetime.now().minute)
    #playsound.playsound('audios\Kitni_baje_ka_lagau_sir.mp3')
    
    alarm_time=pg.prompt("Kitni baje ka lagau sir? (hour minute)")
    if alarm_time=='jarvis':
        print('Yes Boss!')
        playsound.playsound('audios\yesboss.mp3')
        return_to_jarvis.back_to_jarvis()
    alarm_time_hm=alarm_time.split()
    alarm_hour=int(alarm_time_hm[0])
    alarm_min=int(alarm_time_hm[1])
    if cur_hour>12:
        alarm_hour=alarm_hour+12
    if alarm_hour>=cur_hour and cur_hour<12:
        if alarm_hour>cur_hour and alarm_hour<12:
            ampm='am'
            print(ampm)
        elif alarm_hour==cur_hour:
            if alarm_min>cur_min:
                ampm='am'
                print(ampm)
            else:
                ampm='pm'
                print(ampm)
        elif alarm_hour>cur_hour and alarm_hour>12:
            ampm='pm'
            print('pm')
    elif alarm_hour>=cur_hour and cur_hour>12:
        cur_hour=cur_hour-12
        if alarm_hour>cur_hour:
            ampm='pm'
            print(ampm)
        elif alarm_hour==cur_hour:
            if alarm_min>cur_min:
                ampm='pm'
                print(ampm)
            else:
                ampm='am'
                print(ampm)
    elif alarm_hour<=cur_hour:
        if alarm_hour<cur_hour and cur_hour>12:
            ampm='am'
            print(ampm)
        elif alarm_hour<cur_hour and cur_hour<12:
            ampm='pm'
            print(ampm)
        elif alarm_hour==cur_hour:
            if alarm_min>cur_min:
                ampm='am'
                print(ampm)
            else:
                ampm='pm'
                print(ampm)


    pg.moveTo(562,1050, 0.8)
    time.sleep(0.7)
    pg.click()
    time.sleep(0.3)
    pg.write('alarm', 0.1)
    pg.press('enter')
    time.sleep(2)
    pg.moveTo(313, 215, 1)
    time.sleep(1)
    pg.click()
    pg.moveTo(1850, 940, 1)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.moveTo(968, 203)
    for i in range(alarm_min):
        pg.click()
        time.sleep(0.1)
    time.sleep(0.5)
    def ss():
        
        if alarm_hour>7:
            pg.moveTo(804, 190, 1)
            print('more than 7')
            for j in range(alarm_hour-7):
                pg.click()
                time.sleep(0.1)
        else:
            pg.moveTo(819, 378, 1)
            for k in range(7-alarm_hour):
                pg.click()
                time.sleep(0.1)
    ss()

    if pmam==ampm:
        pg.moveTo(848, 891, 1)
        time.sleep(0.6)
        pg.click()
        pg.moveTo(1884, 12, 1)
        pg.click()
        time.sleep(0.6)
    else:
        pg.moveTo(1113, 189, 1)
        time.sleep(0.6)
        pg.click()
        pg.moveTo(848, 891, 1)
        time.sleep(0.5)
        pg.click()
        pg.moveTo(1884, 12, 1)
        pg.click()
        time.sleep(0.5)
    pg.moveTo(last)
        

#alarm_clock.alarm_set()
#alarm_set()
