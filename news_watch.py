import datetime
import webbrowser
import os
import random
import pywhatkit as pt
import time
import pyautogui as pg
import return_to_jarvis
import playsound
import speech_recognition as s
from threading import Thread
def news_watching():
    t=Thread(target=playsound.playsound, args=(['audios\Sir_aap_news_live_dekhna_chahte_he_ya_padhna_chahte_he.mp3']))
    t.start()
    del t
    watch_in_what=pg.prompt('Sir aap news live dekhna chahte he ya padhna chahte he?')
    if watch_in_what=='padhna' or watch_in_what=='read':
        t=Thread(target=playsound.playsound, args=(['audios\Konsi_site_se_padhna_chahenge_sir.mp3']))
        t.start()
        del t
        site=pg.prompt("Konsi site se padhna chahenge sir ")
        if site=='abp' or site=='abvp':
            webbrowser.open("https://www.abplive.com/")
        elif site=='ndtv':
            webbrowser.open("https://www.ndtv.com/")
        elif site=='jarvis' or site=='chotu' or site=='jarbis' :
            main1()
        else:
            webbrowser.open("https://www.aajtak.in/")
    elif watch_in_what=='dekhna' or watch_in_what=='live':
        t=Thread(target=playsound.playsound, args=(['audios\Konsi_site_se_dekhna_chahenge_sir.mp3']))
        t.start()
        del t
        wsite=pg.prompt("Konsi site pe dekhna chahenge sir ")        
        if wsite=='abp' or wsite=='abvp':
            webbrowser.open("https://www.abplive.com/live-tv")
        elif wsite=='ndtv':
            webbrowser.open("https://www.ndtv.com/video/live/channel/ndtv24x7#pfrom=home-ndtv_mainnavgation")
        else:
            webbrowser.open("https://www.aajtak.in/livetv")
        time.sleep(3)
        return_to_jarvis.back_to_jarvis()
    elif watch_in_what=='jarvis' or watch_in_what=='chotu' or watch_in_what=='jarbis':
        print('Yes Sir!')
    elif watch_in_what=='jitna kaha utna karo' or watch_in_what=='kuch bhi laga de' or watch_in_what=='kuch bhi laga do':
        print("Theek he sir, me apni marzi se news play krta hu! ")
        ch1="https://www.abplive.com/live-tv"
        ch2="https://www.aajtak.in/livetv"
        ch3="https://www.ndtv.com/video/live/channel/ndtv24x7#pfrom=home-ndtv_mainnavgation"
        p1="https://www.abplive.com/"
        p2="https://www.aajtak.in/"
        p3="https://www.ndtv.com/"
        list_of_channels=[ch1,ch2,ch3,p1,p2,p3]
        aa=random.choice(list_of_channels)
        webbrowser.open(aa)
    elif watch_in_what=='jarvis' or watch_in_what=='jarbis' or watch_in_what=='uncle' or watch_in_what=='service' or watch_in_what=='Oo halo' or watch_in_what=='hello' or watch_in_what=='chotu'or watch_in_what=='javis'  or watch_in_what=='beta' or watch_in_what=='jarcis' or watch_in_what=='beta jarvis' or watch_in_what=='jarvios' or watch_in_what=='jarvi':
        print('Yes Sir!')
    else:     
        def new_channel():
            t=Thread(target=playsound.playsound, args=(['audios/Sir_aap_konse_new_channel_se_news_dekhna_chahte_he.mp3']))
            t.start()
            del t
            news_channel=pg.prompt("Sir, aap konse new channel se news dekhna chahte he : ")
            if news_channel=='ndtv':
                webbrowser.open("https://www.ndtv.com/video/live/channel/ndtv24x7#pfrom=home-ndtv_mainnavgation")
                
            elif news_channel=='aajtak' or news_channel=='aaj tak':
                webbrowser.open("https://www.aajtak.in/livetv")
                
            elif news_channel=='abp' or news_channel=='abvp':
                webbrowser.open("https://www.abplive.com/live-tv")
                
            elif news_channel=='jarvis' or news_channel=='jarbis' or news_channel=='uncle' or news_channel=='service' or news_channel=='Oo halo' or news_channel=='hello' or news_channel=='chotu'or news_channel=='javis'  or news_channel=='beta' or news_channel=='jarcis' or news_channel=='beta jarvis' or news_channel=='jarvios' or news_channel=='jarvi':
                print('Yes Sir!')
            else:
                print("Itne hi channel pata he sir! ")
                print("Please try again! :( ")
                del news_channel
                new_channel()
        new_channel()
