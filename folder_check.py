import pyttsx3 as ppt
import pyautogui as pg
import os
import gtts
import playsound
from threading import Thread
jarvis_names=['jarvis','jarbis','jarbie','uncle','jarvia','service','Oo halo','hello','chotu','javis','beta','jarcis','beta jarvis','jarvios','jarvi']

def folder_check():
    file=pg.prompt('1) movies \n2) python \n3) normal_jarvis \n4) speech_jarvis  \n5) certificates \n6) Third Year \n7) Downloads \n8) Sem 5 ')
    file_access=file.lower()
    if file_access=='1' or file_access=='aatala' or file_access=='movie' or file_access=='movies':
        os.startfile(r'D:\aatala')
    elif file_access=='2' or file_access=='python':
        os.startfile(r'C:\Users\samee\Desktop\python')
    elif file_access=='3' or file_access=='normal_jarvis':
        os.startfile(r'C:\Users\samee\Desktop\normal_jarvis')
    elif file_access=='4' or file_access=='speech_jarvis':
        os.startfile(r'C:\Users\samee\Desktop\speech_jarvis')
    elif file_access=='5' or file_access=='certificates' or file_access=='cert':
        os.startfile(r'C:\Users\samee\Desktop\certificates')
    elif file_access=='6' or file_access=='Third Year':
        os.startfile(r'C:\Users\samee\Desktop\Third Year')
    elif file_access=='7' or file_access=='Downloads':
        os.startfile(r'C:\Users\samee\Downloads')
    elif file_access=='8' or file_access=='sem 5':
        os.startfile(r'C:\Users\samee\Desktop\Third Year\CS\SEM 5')
    elif file_access=='jarvis' or file_access=='jarvie' or file_access=='jarbis':
        print('Yes Boss!')
    elif jarvis_names in file_access:
        return None
    else:
        t = Thread(target=playsound.playsound, args=["audios\kya_kar_rahe_ho_sir_ya_to_sahi_number_dalo_ya_sahi_nam.mp3"])
        t.start()
        del t
#folder_check()
#folder_check.folder_check()
