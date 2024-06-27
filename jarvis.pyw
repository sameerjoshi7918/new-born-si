import datetime
import webbrowser
import os
import win32api
import random
import time
import pyautogui as pg
import speech_recognition as s
import pyttsx3 as pt
import gtts
import playsound
from threading import Thread
import cv2
import keyboard as kd

#import photo_check
import musics
import instagram_open
import news_watch
import return_to_jarvis
import whatsapp_message_sender
import mobile
import alarm_clock
import camera_check
import volume_check
import mouse_check
import time_check
import folder_check
import line_counter
import whatsapp_open_check
import spotify_open
import email_web
import name_check
#whatsapp
#instagram
#music
#amazon
#python course
#movies
#news
#youtube
#email / sender
#cmd
#edx
#time
#alarm
#call
#google

jarvis_names=['jarvis','jarbis','jarbie','uncle','jarvia','service','Oo halo','hello','chotu','javis','beta','jarcis','beta jarvis','jarvios','jarvi']
ha_list=['ha','yup','yes',',ya','okay','ok','alright','ohk','hmm']
call_names=['aai','baba','manutai','kirmada','teena','vp','abbas','ishika','samar','lav','anuj','arpit', 'shubhi']
news_channels=['abp','ndtv','aajtak','aaj tak','abvp']
good=['sabas','saabas','shabash','good','nice','very nice','badhiya','gg']
##########

def jack_openerr():
    kd.wait('`')
    pg.press('backspace')
    titles=pg.getAllTitles()
    for i in range(len(titles)):
        if titles[i]=='Jack':
            openit=titles[i]
            pg.getWindowsWithTitle(openit)[0].minimize()
            pg.getWindowsWithTitle(openit)[0].maximize()
            pg.getWindowsWithTitle(openit)[0].restore()
            break

##########
now=datetime.datetime.now()
#playsound.playsound('audios\hello_sir.mp3')
print('Hello Sir! ')
#time_check.time_check1()
print(now)
##########
def time_bata():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:
        list_mm=['Sir, Mujhe lagta he apko so jana chahiye','sir kuch zyda hi rat ho gayi he, apko shayad so jana chahiye','sir ji mazak ki bat nahi he, lekin aap so jaiye']
        jarvis_speak1=random.choice(list_mm)
        if jarvis_speak1=='Sir, Mujhe lagta he apko so jana chahiye':
            t=Thread(target=playsound.playsound, args=(['audios\Sir_Mujhe_lagta_he_apko_so_jana_chahiye.mp3']))
            t.start()
            del t
        elif jarvis_speak1=='sir kuch zyda hi rat ho gayi he, apko shayad so jana chahiye':
            t=Thread(target=playsound.playsound, args=['audios\sir_kuch_zyd_hi_rat_ho_gayi_he_apko_shayad_so_jana_chahiye.mp3'])
            t.start()
            del t
        elif jarvis_speak1=='sir ji mazak ki bat nahi he, lekin aap so jaiye':
            t=Thread(target=playsound.playsound, args=['audios\sir ji mazak ki bat nahi he, lekin aap so jaiye.mp3'])
            t.start()
            del t
    elif hour>6 and hour<12:
        list_gm=['Good Morning Sir','Early morning sir, huh','Itni subah laptop khole he, kuch to bat he','sir ye bhi koi time he laptop chalane ka']
        jarvis_speak2=random.choice(list_gm)
        if jarvis_speak2=='Good Morning Sir':
            t = Thread(target=playsound.playsound, args=["audios\Good_Morning_Sir.mp3"])
            t.start()
            del t
        elif jarvis_speak2=='Early morning sir, huh':
            t = Thread(target=playsound.playsound, args=["audios\Early morning sir, huh.mp3"])
            t.start()
            del t
        elif jarvis_speak2=='Itni subah laptop khole he, kuch to bat he':
            t = Thread(target=playsound.playsound, args=["audios\Itni subah laptop khole he, kuch to bat he.mp3"])
            t.start()
            del t
    elif hour>=12 and hour<18:        
        t = Thread(target=playsound.playsound, args=["audios\Itni bhari dopahar me apko kyu kam krna he.mp3"])
        t.start()
        del t
    elif hour>=18 and hour<22:
        t = Thread(target=playsound.playsound, args=["audios\Good_Evening_Sir!_Kesa_raha_apka_din.mp3"])
        t.start()
        del t
        print("Good Evening Sir!, Kesa raha apka din? ")
        print('Sham ka bhoola jab ghar lot kar aaye to use bhoola nahi kehte, Good Evening sir')
    elif hour>=22 and hour<23:
        t = Thread(target=playsound.playsound, args=["audios\Sir_apke_parents_kabhi_bhi_aa_sakte_he.mp3"])
        t.start()
        del t
        print("Sir, apke parents kabhi bhi aa sakte he ;( ")
        print('Sir, sleeping beauty banne ki jagah aap dat khane ki harkat kr rahe he, SO jaiye na sir')
    elif hour>=23:
        t = Thread(target=playsound.playsound, args=["audios\Sir_Mujhe_lagta_he_apko_so_jana_chahiye.mp3"])
        t.start()
        del t
    del hour
#########time end




#############
def movies_shower():
    t = Thread(target=playsound.playsound, args=["audios\sir_konsi_movie_dekhna_pasand_karenge_folder_vali_ya_server_vali.mp3"])
    t.start()
    del t
    access_per=pg.prompt(text='Sir konsi movie dekhna chahenge, folder vali ya server vali?', title='Movies')
    if access_per=='olamovies' or access_per=='latest' or access_per=='site' or access_per=='server' or access_per=='olamovies vali' or access_per=='picture' or access_per=='movies' or access_per=='jitna kaha utna karo' or access_per=='internet' or access_per=='ola':
        t = Thread(target=playsound.playsound, args=["audios\sari_ya.mp3"])
        t.start()
        del t
        movies_check=pg.prompt("sari ya.........")
        if movies_check=='sari':
            webbrowser.open("https://olamovies.rest/")
            mouse_check.mouce()
            main1()
        else:
            webbrowser.open("https://olamovies.rest/{}".format(movies_check))
            time.sleep(8)
            return_to_jarvis.back_to_jarvis()
            main1()
        del access_per
    elif access_per=='jarvis' or access_per=='chotu' or access_per=='jarbis':
        del access_per
        main1()
    elif access_per=='123' or access_per=='123mkv' or access_per=='mkv':
        webbrowser.open("https://123mkv.press/")
        del access_per
        mouse_check.mouce()
        main1()
    else:
        os.startfile(r'D:\aatala')#aatala folder khola he
        t = Thread(target=playsound.playsound, args=["audios\Sir_folder_khol_diya_he.mp3"])
        t.start()
        del t
        del access_per
        mouse_check.mouce()
        main1()

def call_check():
    ok=pg.locateCenterOnScreen('images\phone_link_not_connected.png')
    okay=str(ok)
    if okay=='None':
        return None
    else:
        pt.speak('sir, first you have to connect to the mobile bluetooth, hope you understand')


########################
time_bata()
a=(' whatsapp\n instagram\n music\n amazon\n dance\n python course\n movies\n news \n youtube\n email\n cmd\n time\n alarm\n call\n folder open\n Google\n Name Check')
print(a)
yut=[]
#################3
def main1():
    def main2():
            jarvis=pg.prompt(text='Jack', title='Jack')
            
            call_infor=jarvis.split()
            def call_number():
                time.sleep(0.5)
                pg.moveTo(550,1050)
                time.sleep(0.5)
                pg.click()
                time.sleep(1)
                pg.write('phone')
                time.sleep(1)
                pg.press('enter')
                time.sleep(1)
                call_check()
                a=pg.confirm('Continue?', buttons=['Yes','No'])
                if a=='Yes':
                    pg.moveTo(1518, 214, 1)
                    pg.click()
                    time.sleep(1)
                    pg.write('{}'.format(call_infor[-1]), interval=0.3)
                    time.sleep(1)
                    pg.press('enter')
                    pg.moveTo(1518, 414, 1)
                    pg.click()
                    pg.hotkey('pagedown')
                    time.sleep(0.5)
                    pg.moveTo(1621, 946, 1)
                    pg.click()
                else:
                    return None

            def call_name():
                if call_infor[1]=='arpit':
                    call_infor[1]='arpit drama'
                elif call_infor[1]=='shubhi':
                    call_infor[1]=='shubhi drama'
                time.sleep(1)
                pg.moveTo(550,1050)
                time.sleep(1)
                pg.click()
                time.sleep(1)
                pg.write('phone', interval=0.1)
                time.sleep(1)
                pg.press('enter')
                time.sleep(2)
                call_check()
                a=pg.confirm('Continue?', buttons=['Yes','No'])
                if a=='Yes':
                    pg.moveTo(1518, 214, 1)
                    pg.click()
                    time.sleep(1)
                    pg.write('{}'.format(call_infor[1]), interval=0.1)
                    time.sleep(0.5)
                    pg.press('enter')
                    pg.moveTo(1518, 414, 1)
                    pg.click()
                    pg.hotkey('pagedown')
                    time.sleep(0.5)
                    pg.moveTo(1621, 946, 1)
                    pg.click()
                else:
                    return None

        
            if jarvis in jarvis_names:
                print("Yes Boss!")
                t = Thread(target=playsound.playsound, args=["audios\options.mp3"])
                t.start()
                del t
                choice=pg.prompt(title='Jack', text='Options')
                call_infor1=choice.split()
                #movies
                if choice=='movies' or choice=='movies dikhao' or choice=='nayi movies dikhao' or choice=='movie':
                    movies_shower()
                    del choice
                #news
                elif choice=='news' or choice=='news dikhao' or choice=='latest news' or choice=='khabre' or choice=='taza khabre':
                    news_watch.news_watching()
                    del choice
                    main1()
                elif call_infor1[0]=='news' and call_infor1[1] in news_channels:
                    asking_news=pg.prompt(title='Jack', text='Dekhna ya Padhna')
                    if asking_news.lower()=='d' or asking_news.lower()=='dekhna':
                        if call_infor1[1]=='abp' or call_infor1[1]=='abvp':
                            webbrowser.open("https://www.abplive.com/live-tv")
                        if call_infor1[1]=='ndtv':
                            webbrowser.open("https://www.ndtv.com/video/live/channel/ndtv24x7#pfrom=home-ndtv_mainnavgation")
                        if call_infor1[1]=='aajtak' or call_infor[1]=='aaj tak':
                            webbrowser.open("https://www.aajtak.in/livetv")
                    elif asking_news.lower()=='p' or asking_news.lower()=='padhna':
                        if call_infor[1]=='abp' or call_infor[1]=='abvp':
                            webbrowser.open("https://www.abplive.com/")
                            mouse_check.mouce()
                            main2()
                        if call_infor[1]=='ndtv':
                            webbrowser.open("https://www.ndtv.com/")
                            mouse_check.mouce()
                            main2()
                        if call_infor[1]=='aajtak' or call_infor[1]=='aaj tak':
                            webbrowser.open("https://www.aajtak.in/")
                            mouse_check.mouce()
                            main2()
                        
                elif choice=='music' or choice=='musc' or choice=='music suna de yr' or choice=='music baja' or choice=='music laga' or choice=='gane laga' or choice=='gana baja' or choice=='gana':
                    musics.music_player()
                    del choice
                    main2()
                    
                elif choice=='email' or choice=='mail' or choice=='gmail':
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                    del choice
                    mouse_check.mouce()
                    main2()
                    
                elif choice=='whatsapp' or choice=='wp' or choice=='wa' or choice=='ws'or choice=='wt':
                    whatsapp_message_sender.wt_particular()
                    del choice
                    main2()
                    
                elif choice=='insta' or choice=='instagram' or choice=='insta gram':
                    instagram_open.insta_open()
                    mouse_check.mouce
                    main2()

                    
                elif choice=='alarm' or choice=='anaram' or choice=='set alarm' :
                    alarm_clock.alarm_set()
                    del choice
                    main2()
                    
                
                    ###########  misuc
                elif (choice in jarvis_names):
                    main2()
                    del choice
                    
                    #cmd commands executing
                elif choice=='cmd' or choice=='cm':
                    cmd_command=pg.prompt(title='Jack', text="Enter your command : ")
                    os.system('cmd /k "{}" '.format(cmd_command))
                    del choice
                    main2()
                    
                elif choice=='dance':
                    os.system('cmd /k "curl ascii.live/parrot" ')
                    del choice
                    main1()
                    
                elif choice=='phone' or choice=='mobile' or choice=='call':
                    mobile.accessing_phone()
                    main2()
                    del choice
                    mouse_check.mouce()
                elif call_infor[0]=='call' and call_infor[1] in call_names: 
                    call_name()
                    del choice
                    mouse_check.mouce()
                    main2()
                elif call_infor[0]=='call' and call_infor[-1].isnumeric():
                    call_number()
                    del choice
                    mouse_check.mouce()

                elif ('camera' in choice) or ('photo' in choice) or ('selfie' in choice):
                    camera_check.camera_start()
                    del choice
                    main2()
                elif call_infor1[0]=='yt' or call_infor1[0]=='youtube':
                    yt_list=call_infor1[1:]
                    if choice=='youtube' or choice=='yt':
                        webbrowser.open('https://www.youtube.com/')
                        mouse_check.mouce()
                        main2()

                    elif call_infor1[0]=='yt' or call_infor1[0]=='youtube':
                        if int(len(yt_list))>2:
                            str1 = ""
                            for ele in yt_list:
                                str1 += ele
                                str1 +=' '
                            webbrowser.open('https://www.youtube.com/results?search_query={}'.format(str1))
                            mouse_check.mouce()
                            main2()

                elif choice=='samay' or choice=='time' or choice=='time bata do' or choice=='time kya hua he' or choice=='time batana zara' or choice=='time bata to':
                    time_check.time_check1()
                    del choice
                    main2()
                    

                    #music column
                elif choice=='pause' or choice=='stop' or choice==' ':
                    pg.hotkey('playpause')
                    time.sleep(0.5)
                    del choice
                    main2()
                    
                elif choice=='play':
                    pg.hotkey('playpause')
                    time.sleep(0.5)
                    del choice
                    main2()
                    
                elif choice=='prev' or choice=='previouse' or choice=='previous' or choice=='pichla' or choice=='prev song':
                    pg.hotkey('prevtrack')
                    time.sleep(0.5)
                    pg.hotkey('prevtrack')
                    time.sleep(0.2)
                    del choice
                    main2()
                    
                elif choice=='next song' or choice=='next' or choice=='agla gana' or choice=='next song' or choice=='aage vala gana':
                    pg.hotkey('nexttrack')
                    time.sleep(0.2)
                    del choice
                    main2()
                    
                elif choice=='vol' or choice=='volume':
                    t = Thread(target=playsound.playsound, args=["audios/up_or_dowm.mp3"])
                    t.start()
                    del t
                    volume_kitna=pg.prompt(title='Jack', text='up or down')
                    if volume_kitna=='up' or volume_kitna=='zyda' or volume_kitna=='badha' or volume_kitna=='increase' or volume_kitna=='inc':
                        volume_check.final_volume_up()
                        del choice
                        main2()
                        
                    elif volume_kitna=='full' or volume_kitna=='max':
                        volume_check.final_volume_full()
                        del choice
                        main2()
                        
                    elif volume_kitna=='mute' or volume_kitna=='min':
                        volume_check.final_volume_mute()
                        del choice
                        main2()
                        
                    else:
                        volume_check.final_volume_down()
                        main2()
                        del choice
                elif choice=='vol full':
                    t=Thread(target=volume_check.final_volume_full, args=[()])
                    t.start()
                    del t
                    del choice
                    main2()
                elif choice=='mute':
                    t=Thread(target=volume_check.final_volume_mute, args=[])
                    t.start()
                    del t
                    del choice
                    main2()
                        
                elif choice=='starting' or choice=='start':
                    pg.hotkey('prevtrack')
                    del choice
                    main2()
                    
                elif choice=='vol up' or choice=='volume up':
                    t=Thread(target=volume_check.final_volume_up, args=[()])
                    t.start()
                    del t
                    del choice
                    main2()
                    
                elif choice=='vol down' or choice=='volume down':
                    t=Thread(target=volume_check.final_volume_down, args=[()])
                    t.start()
                    del t
                    del choice
                    main2()
                    
                elif choice=='course' or choice=='cource':
                    webbrowser.open('https://www.coursera.org/learn/python/lecture/GoNcs/video-welcome-to-class-dr-chuck')
                    del choice
                    time.sleep(4)
                    mouse_check.mouce()
                    main2()
                    
               
                elif (('open' and 'file' in choice) or 'folder' in choice) :
                    folder_check.folder_check()
                    del choice
                    mouse_check.mouce()
                    main2()

                    
                elif call_infor1[0]=='g' or call_infor1=='google':
                    ss=call_infor1[1:]
                    la=call_infor1[-1]
                    if la[-4:]=='.com':
                        webbrowser.open('https://www.{}'.format(call_infor1[-1]))
                        mouse_check.mouce()
                        main2()
                    elif int(len(ss))>2:
                        str1 = ""
                        for ele in ss:
                            str1 += ele
                            str1 +=' '
                        webbrowser.open('https://www.google.com/search?q={}'.format(str1))
                        mouse_check.mouce()
                        del str1
                        del call_infor1
                        main2()
                    else:
                        
                        kya_google=pg.prompt(title='Jack', text='Search..... ')
                        webbrowser.open('https://www.google.com/search?q={}'.format(kya_google))
                        time.sleep(2)
                        mouse_check.mouce()
                        main2()
                    
                    
                elif choice=='edx':
                    os.startfile(r"C:\Users\samee\Desktop\eDEX-UI.lnk")
                    del choice
                    main2()
                    
                elif choice=='dance' or choice=='nach':
                    os.system('cmd /k "curl ascii.live/parrot" ')
                    del choice
                    return_to_jarvis.back_to_jarvis()
                elif choice=='amazon':
                    webbrowser.open('https://www.amazon.in')
                    mouse_check.mouce()
                    main2()
                elif choice=='name check' or choice=='namecheck' or choice=='name':
                    name_check.name()
                    main2()
                elif choice=='brave' or choice=='b':
                    titles=pg.getAllTitles()
                    print(titles)
                    for i in range(len(titles)):
                        if 'Brave' in titles[i]:
                            #print(titles[i])
                            print('brave found')
                            openit=titles[i]
                            break
                    try:
                        pg.getWindowsWithTitle(openit)[0].minimize()
                        pg.getWindowsWithTitle(openit)[0].maximize()
                    except:
                        print('Brave is not opened')
                        webbrowser.open('https://www.google.com/')
                    t=Thread(target=main2(), args=[])
                    t.start()
                    del t
                    del titles
                    del choice
                    main2()
                elif choice=='lines' or choice=='line' or choice=='number of lines':
                    line_counter.liner()
                    del choice
                    main2()
                elif choice=='vlc':
                    titles=pg.getAllTitles()
                    print(titles)
                    for i in range(len(titles)):
                        if 'VLC' in titles[i]:
                            #print(titles[i])
                            print('VLC found found')
                            openit=titles[i]
                            break
                    try:
                        
                        pg.getWindowsWithTitle(openit)[0].minimize()
                        pg.getWindowsWithTitle(openit)[0].maximize()
                    except:
                        print('VLC is not opened')
                        pg.click(558, 1038, duration=1)
                        pg.write('VLC', 0.1)
                        time.sleep(0.8)
                        loc=pg.locateCenterOnScreen('images\recent.png')
                        pg.moveTo(loc)
                        pg.moveRel(10, 50)
                        time.sleep(1)
                        pg.click()
                    del titles
                    del choice
                    time.sleep(2)
                    mouse_check.mouce()
                    main2()
                else:
                    del choice
                    main1()
                    
                main1()


                
##########################################----------J-A-R-V-I-S---------------###############################################


                
            elif jarvis=='kyu' or jarvis=='kya' or jarvis=='kaiko' or jarvis=='kaiku' or jarvis=='jyu':
                playsound.playsound('audios\Kyuki_is_time_pr_apke_parents_aa_sakte_he_aur_apko_acha_nahi_lagega.mp3')

                
                playsound.playsound('audios/Kya_aap_fir_bhi_suffer_karna_chahte_he.mp3')
                power=pg.prompt(title='Jack', text='Kya aap fir bhi suffer karna chahte he')
                if power in ha_list:
                    print("Jesi apki marzi BOSS! ")
                    del jarvis
                    main2()
                    
                else:
                    print("okay sir, have a GOOD NIGHT SIR ;) ")
                    
            elif jarvis=='nahi' or jarvis=='no' or jarvis=='nop':
                print("Theek he sir, jesi apki marzi ")
                kya_me=pg.prompt("Kya me main run karu? ")
                if kya_me=='yes' or kya_me=='yup' or kya_me=='ya' or kya_me=='ha':
                    main2()
                    
            elif jarvis=='sameer' or jarvis=='sameeer':
                print("Sir, mene kaha tha soo jaiye, aa gaye na apke parents ")
                #moods
                
            elif ("theek" in jarvis) or ('chod' in jarvis):
                print("Lagta he kisi ne kuch kaha he aapse. ")
                print("Agar me sahi hu, to kon he vo? ")
                theek=pg.prompt(title='Jack', text="")
                if ("nahi" in theek) or ("chod" in theek):
                    print("theek he sir me force nahi karunga ")
                    main_ac=pg.prompt(title='Jack', text="Main RUN karu? :")
                    if main_ac in ha_list:
                        main2()
                        
            elif jarvis=='pause' or jarvis=='stop':
                pg.hotkey('playpause')
                del jarvis
                main2()
                
            elif jarvis=='play' or jarvis=='p' or jarvis==' ':
                pg.hotkey('playpause')
                del jarvis
                main2()
            elif jarvis=='prev' or jarvis=='previouse' or jarvis=='previous' or jarvis=='pichla':
                pg.hotkey('prevtrack')
                time.sleep(0.5)
                pg.hotkey('prevtrack')
                del jarvis
                main1()
                
            elif jarvis=='next song' or jarvis=='next' or jarvis=='agla gana' or jarvis=='next song' or jarvis=='aage vala gana':
                pg.hotkey('nexttrack')
                del jarvis
                main1()
                
            elif  jarvis=='starting' or jarvis=='start':
                pg.hotkey('prevtrack')
                del jarvis
                main1()
                
            elif jarvis=='vol' or jarvis=='volume':
                playsound.playsound('audios/up_or_down.mp3')
                volume_kitna=pg.prompt(title='Jack', text='up or down')
                if volume_kitna=='up' or volume_kitna=='zyda' or volume_kitna=='badha' or volume_kitna=='increase' or volume_kitna=='inc':
                    volume_check.final_volume_up()
                    del jarvis
                    main2()
                    
                elif volume_kitna=='full' or volume_kitna=='max':
                    volume_check.final_volume_full()
                    del jarvis
                    main2()
                    
                elif volume_kitna=='mute' or volume_kitna=='min':
                    volume_check.final_volume_mute()
                    del jarvis
                    main2()
                    
                else:
                    volume_check.final_volume_down()
                    del jarvis
                    main2()
                    
            elif jarvis=='vol up' or jarvis=='volume up':
                volume_check.final_volume_up()
                del jarvis
                main2()
                    
            elif jarvis=='vol down' or jarvis=='volume down':
                volume_check.final_volume_down()
                del jarvis
                main2()
                
            elif jarvis=='vol full':
                volume_check.final_volume_full()
                del jarvis
                main2()
                
            elif jarvis=='mute':
                volume_check.final_volume_mute()
                del jarvis
                main2()
                    

                    


            ##########################################
                #rewriting all functions
    




    
            elif jarvis=='movies' or jarvis=='movies dikhao' or jarvis=='nayi movies dikhao' or jarvis=='movie':
                movies_shower()
                del jarvis
            elif jarvis=='cmd' or jarvis=='cm' or jarvis=='command prompt'or jarvis=='comand'  :
                cmd_command=pg.prompt(title='Jack', text="Enter your command : ")
                os.system('cmd /k "{}" '.format(cmd_command))
                del jarvis
                main2()
                
            elif jarvis=='email' or jarvis=='mail' or jarvis=='gmail':
                t=Thread(target=playsound.playsound, args=[('audios\sDo you want to send a MAIL.mp3')])
                t.start()
                del t
                lethim=pg.prompt(title='Jack', text='Do you want to send a MAIL?')
                if lethim in ha_list:
                    t=Thread(target=playsound.playsound, args=[('audios\sEnter the Email.mp3')])
                    t.start()
                    del t
                    email_email=pg.prompt(title='Jack', text='Enter the Email')
                    t=Thread(target=playsound.playsound, args=[('audios\sEnter the inside content.mp3')])
                    t.start()
                    del t
                    content=pg.prompt(title='Jack', text='Enter the inside content')
                    t=Thread(target=playsound.playsound, args=[('audios\sDo you want to add subject.mp3')])
                    t.start()
                    del t
                    yn=pg.confirm(text='Do you want to\n add subject?', title='OPTIONAL', buttons=('YES','NO'))
                    subject=pg.prompt(title='Jack', text='Enter the subject')
                    t=Thread(target=playsound.playsound, args=[('audios\scomposing the mail for you.mp3')])
                    t.start()
                    del t
                    time.sleep(1)
                    email_web.call_this()
                    def cc():
                        time.sleep(1)
                        a=pg.locateCenterOnScreen('images\compose_email.png')
                        na=str(a)
                        if na=='None':
                            del na
                            del a
                            cc()
                        else:
                            del a
                            del na
                    img=pg.locateCenterOnScreen('images\compose_email.png')
                    pg.moveTo(img)
                    pg.click()
                    pg.moveTo(1162, 395, 1)
                    pg.click()
                    if email_email=='manutai' or email_email=='manu tai':
                        email_email='njnandinijoshi@gmail.com'
                    elif email_email=='hum':
                        email_email='humhegamers@gmail.com'
                    pg.write('{}'.format(email_email))
                    pg.press('enter')
                    time.sleep(1)
                    if len(subject)>1:
                        pg.moveRel(0, 75, 1)
                        pg.click()
                        pg.write('{}'.format(subject))
                    pg.moveTo(1120, 531)
                    pg.click()
                    pg.write('{}'.format(content))
                    time.sleep(1)
                    know=pg.locateCenterOnScreen('images\email_send.png')
                    pg.moveTo(know)
                    pg.click()
                    time.sleep(2)
                    pg.hotkey('ctrl','w')
                        
                else:
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                    del jarvis
                mouse_check.mouce()
                t=Thread(target=main2(), args=[])
                t.start()
                del t
                
            elif jarvis=='insta' or jarvis=='instagram' or jarvis=='insta gram':
                instagram_open.insta_open()
                mouse_check.mouce
                main2()
                
            elif call_infor[0]=='yt' or call_infor[0]=='youtube':
                yt_list=call_infor[1:]
                if jarvis=='youtube' or jarvis=='yt':
                    webbrowser.open('https://www.youtube.com/')
                    mouse_check.mouce()
                    t=Thread(target=main2(), args=[])
                    t.start()
                    del t

                elif call_infor[0]=='yt' or call_infor[0]=='youtube':
                    if int(len(yt_list))>=1:
                        str1 = ""
                        for ele in yt_list:
                            str1 += ele
                            str1 +=' '
                        webbrowser.open('https://www.youtube.com/results?search_query={}'.format(str1))
                        mouse_check.mouce()
                        t=Thread(target=main2(), args=[])
                        t.start()
                        del t
                    
                
            elif jarvis=='dance':
                os.system('cmd /k "curl ascii.live/parrot" ')
                main2()
                
            elif jarvis=='amazon':
                webbrowser.open('https://www.amazon.in')
                mouse_check.mouce()
                t=Thread(target=main2(), args=[])
                t.start()
                del t
                
            elif jarvis=='news' or jarvis=='news dikhao' or jarvis=='latest news' or jarvis=='khabre' or jarvis=='taza khabre':
                news_watch.news_watching()
                t=Thread(target=main2(), args=[])
                t.start()
                del t
            elif jarvis=='samay' or jarvis=='time' or jarvis=='time bata do' or jarvis=='time kya hua he' or jarvis=='time batana zara' or jarvis=='time bata to':
                time_check.time_check1()
                main2()
                
            
            elif jarvis=='s' or jarvis=='spotify':
                spotify_open.call_this()
                jack_openerr()
                main2()
            elif jarvis=='i':
                new=pg.getAllTitles()
                for i in range(len(new)):
                    if len(new[i])==0:
                        pass
                    elif new[i][0]=='*':
                        ss=new[i][0]
                        print(ss)
                        
                        if new[i][-1]=='*':
                            print('editing idle confirmed')
                            pg.getWindowsWithTitle(new[i])[0].minimize()
                            pg.getWindowsWithTitle(new[i])[0].maximize()
                            break
                kd.wait('`')
                jack_openerr()
                main2()
            elif jarvis=='phone' or jarvis=='mobile' or jarvis=='call':
                mobile.accessing_phone()
                del jarvis
                kd.wait('`')
                jack_openerr()
                main2()
                
            elif call_infor[0]=='call' and call_infor[1] in call_names: 
                call_name()
                del jarvis
                kd.wait('`')
                jack_openerr()
                main2()
            elif call_infor[0]=='call' and call_infor[-1].isnumeric():
                call_number()
                del jarvis
                kd.wait('`')
                main2()
                
            elif jarvis=='music' or jarvis=='musc' or jarvis=='music suna de yr' or jarvis=='music baja' or jarvis=='music laga' or jarvis=='gane laga' or jarvis=='gana baja' or jarvis=='gana':
                try:
                    musics.music_player()
                except:
                    main2()
                del jarvis
                jack_openerr()
                kd.wait('`')
                main2()
                
            elif jarvis=='alarm' or jarvis=='anaram' or jarvis=='set alarm' :
                alarm_clock.alarm_set()
                del jarvis
                jack_openerr()
                kd.wait('`')
                main2()
                
            elif jarvis=='file' or jarvis=='folder':
                folder_check.folder_check()
                mouse_check.mouce()
                t=Thread(target=main2(), args=[])
                t.start()
                del t
                
            elif call_infor[0]=='g' or call_infor=='google':
                ss=call_infor[1:]
                la=call_infor[-1]
                if la[-4:]=='.com':
                    webbrowser.open('https://www.{}'.format(call_infor[-1]))
                    kd.wait('`')
                    main2()
                elif int(len(ss))>1:
                    str1 = ""
                    for ele in ss:
                        str1 += ele
                        str1 +=' '
                    webbrowser.open('https://www.google.com/search?q={}'.format(str1))
                    mouse_check.mouce()
                    del str1
                    del call_infor
                    kd.wait('`')
                    main2()
                    
                else:
                    kya_google=pg.prompt(title='Jack', text='Search..... ')
                    webbrowser.open('https://www.google.com/search?q={}'.format(kya_google))
                    kd.wait('`')
                    main2()
                    
            elif jarvis=='course' or jarvis=='cource':
                webbrowser.open('https://www.coursera.org/learn/python/lecture/GoNcs/video-welcome-to-class-dr-chuck')
                kd.wait('`')
                main2()
                
            elif jarvis=='brave' or jarvis=='b':
                titles=pg.getAllTitles()
                print(titles)
                for i in range(len(titles)):
                    if 'Brave' in titles[i]:
                        #print(titles[i])
                        print('brave found')
                        openit=titles[i]
                        break
                try:
                    pg.getWindowsWithTitle(openit)[0].minimize()
                    pg.getWindowsWithTitle(openit)[0].maximize()
                    time.sleep(1)
                except:
                    print('Brave is not opened')
                    webbrowser.open('https://www.google.com/')
                    time.sleep(1)
                del titles
                del jarvis
                jack_openerr()
                main2()

            elif jarvis=='i' or jarvis=='idle':
                titles=pg.getAllTitles()
                for ele in range(len(titles)-1):
                    name=titles[ele]
                    if '.pyw' in name or '.py' in name or 'samee' in name:
                        print('found idle', name)
                        time.sleep(0.3)
                        pg.getWindowsWithTitle(name)[0].minimize()
                        pg.getWindowsWithTitle(name)[0].maximize()
                        break
                jack_openerr()
                main2()
            elif jarvis=='w':
                whatsapp_open_check.call_this()
                jack_openerr()
                main2()
                
            elif jarvis=='vlc':
                titles=pg.getAllTitles()
                print(titles)
                for i in range(len(titles)):
                    if 'VLC' in titles[i]:
                        #print(titles[i])
                        print('VLC found found')
                        openit=titles[i]
                        break
                try:
                    pg.getWindowsWithTitle(openit)[0].minimize()
                    pg.getWindowsWithTitle(openit)[0].maximize()
                except:
                    print('VLC is not opened')
                    pg.click(558, 1038, duration=1)
                    time.sleep(0.3)
                    pg.write('VLC', 0.1)
                    time.sleep(0.8)
                    loc=pg.locateCenterOnScreen(r'C:\Users\samee\Desktop\normal_jarvis\images\recent.png')
                    pg.moveTo(loc)
                    pg.moveRel(10, 50)
                    time.sleep(1)
                    pg.click()
                del titles
                t=Thread(target=main2(), args=[])
                t.start()
                del t
                
            elif jarvis=='camera' or jarvis=='cam' or jarvis=='selfie':
                camera_check.camera_start()
                del choice
                main2()
                
            elif jarvis=='sabas' or jarvis=='saabas' or jarvis=='shabash' or jarvis=='good' or jarvis=='badhiya':
                t=Thread(target=playsound.playsound, args=[('audios\sthankyou sir.mp3')])
                t.start()
                del t
                main2()

            elif jarvis=='nice' or jarvis=='very good' or jarvis=='ver nice':
                t=Thread(target=playsound.playsound, args=[('audios\Thankyou very much sir.mp3')])
                t.start()
                del t
            elif jarvis=='shutdown':
                os.system('cmd /k  shutdown /s')
                del jarvis
            elif jarvis=='lines' or jarvis=='line' or jarvis=='number of lines':
                t=Thread(target=line_counter.liner(), args=[])
                t.start()
                del t
                del jarvis
                main2()
            elif jarvis=='name check' or jarvis=='namecheck' or jarvis=='name':
                name_check.name()
                main2()
                
            elif jarvis=='music name' or jarvis=='musicname':
                def cc():
                    a=pg.getAllTitles()
                    ll=len(a)
                    for i in range(ll):
                        if 'Brave' in a[i]:
                            print('Brave found')
                            f=str(a[i])
                            print(f)
                            if '•' in f:
                                aa=f.split()
                                num=int(aa.index('•'))
                                sstt=aa[0:num]
                                str1=''
                                for ele in sstt:
                                    str1+=ele
                                    str1+=' '
                                text=str(str1)
                                sound=gtts.gTTS(text, lang='hi')
                                sound.save('str1.mp3')
                                pg.hotkey('playpause')
                                time.sleep(0.3)
                                t=Thread(target=playsound.playsound, args=[('str1.mp3')])
                                t.start()
                                t.join()
                                pg.hotkey('playpause')
                                del t
                                print('Song name is: ',str1)
                                os.remove('str1.mp3')
                                break
                cc()
                main2()
                
            elif call_infor[0]=='news' and call_infor[1] in news_channels:
                    asking_news=pg.prompt(title='Jack', text='Dekhna ya Padhna')
                    if asking_news.lower()=='d' or asking_news.lower()=='dekhna':
                        if call_infor[1]=='abp' or call_infor[1]=='abvp':
                            webbrowser.open("https://www.abplive.com/live-tv")
                        if call_infor[1]=='ndtv':
                            webbrowser.open("https://www.ndtv.com/video/live/channel/ndtv24x7#pfrom=home-ndtv_mainnavgation")
                        if call_infor[1]=='aajtak' or call_infor[1]=='aaj tak':
                            webbrowser.open("https://www.aajtak.in/livetv")
                            
                    elif asking_news.lower()=='p' or asking_news.lower()=='padhna':
                        if call_infor[1]=='abp' or call_infor[1]=='abvp':
                            webbrowser.open("https://www.abplive.com/")
                            mouse_check.mouce()
                            
                        if call_infor[1]=='ndtv':
                            webbrowser.open("https://www.ndtv.com/")
                            mouse_check.mouce()

                        if call_infor[1]=='aajtak' or call_infor[1]=='aaj tak':
                            webbrowser.open("https://www.aajtak.in/")
                            mouse_check.mouce()
                    main2()
            elif call_infor[0]=='whatsapp' or call_infor[0]=='wt':
                try:  
                    if call_infor[0]=='whatsapp' or call_infor[0]=='wt':
                        if call_infor[1]=='manutai':
                            call_infor[1]='kirmada'
                        t = Thread(target=playsound.playsound, args=["audios\Enter_message.mp3"])
                        t.start()
                        del t
                        message=pg.prompt(title='Jack', text='Enter message : ')
                        tim=pg.prompt(title='Jack', text='Enter time')
                        def back():
                            time1=tim.split()
                            if tim=='now' or tim=='Now':
                                print('Now')
                            elif time1[0].isnumeric():
                                def ok():
                                    hour=datetime.datetime.now().hour
                                    min1=datetime.datetime.now().minute
                                    if hour>12:
                                        hour=hour-12
                                        if int(time1[0])==hour and int(time1[1])==min1:
                                            return None
                                        else:
                                            time.sleep(1)
                                            ok()
                                    elif hour<12:
                                        if int(time1[0])==hour and int(time1[0])==min1:
                                            return None
                                        else:
                                            time.sleep(1)
                                            ok()
                                ok()
                            whatsapp_open_check.call_this()
                            def cc():
                                time.sleep(1)
                                a=pg.locateCenterOnScreen('images\search_wt.png')
                                na=str(a)
                                if na=='None':
                                    del na
                                    del a
                                    cc()
                                else:
                                    del a
                                    del na
                            cc()
                            a=pg.locateCenterOnScreen('images\search_wt.png')
                            pg.moveTo(a)
                            pg.click()
                            time.sleep(1)
                            pg.write('{}'.format(call_infor[1]), interval=0.1)
                            time.sleep(1)
                            pg.press('enter')
                            time.sleep(2)
                            pg.moveTo(1169, 965, 1)
                            time.sleep(1)
                            pg.click()
                            pg.write('{}'.format(message), interval=0.1)
                            pg.press('enter')
                        r=Thread(target=back(), args=[])
                        r.start()
                    else:
                        whatsapp_message_sender.wt_particular()
                    t=Thread(target=main2(), args=[])
                    t.start()
                    del t
                except:
                    whatsapp_message_sender.wt_particular()
                    t=Thread(target=main2(), args=[])
                    t.start()
                    del t
            elif 'what can you do' in jarvis or 'kya kar sakte' in jarvis:
                ya=(' \n\n\n\n\n whatsapp\n instagram\n music\n amazon\n dance\n python course\n movies\n news \n youtube\n email\n cmd\n time\n alarm\n call\n folder open')
                print(ya)
                del jarvis
                main2()
                    
            elif jarvis=='chatting':
                def chatting():
                    t=Thread(target=playsound.playsound, args=[('audios\sar aapne kuch galat likh diya ya mujhse baat karna chahte ho.mp3')])
                    t.start()
                    del t
                    bate=pg.prompt(title='Jack', text='Sir aapne kuch galat likh diya ya mujhse baat karna chahte ho?')
                    if 'bate' in bate or 'bat' in bate:
                        hour = int(datetime.datetime.now().hour)
                        if hour>=0 and hour<3:
                            a=Thread(target=playsound.playsound, args=[('audios\sir yeah koi baat karne ka time hey kya.mp3')])
                            b=Thread(target=playsound.playsound, args=[('audios\sar ji itna free time hey to kuch naya kar lijiye, mujhse baat karne key kya zarurat.mp3')])
                            a.start() or b.start()
                            del a
                            del b
                        elif hour>=3 and hour<4:
                            def aa():
                                a=Thread(target=playsound.playsound, args=[('audios\sir ji.mp3')])
                                a.start()
                                time.sleep(2)
                                c=Thread(target=playsound.playsound, args=[('audios\ab aap mujhe bahut gussa dila rahey hain, itni der tak kam karenge, to mera to kuch nahi jayega, aap alag daat khayenge vo alag.mp3')])
                                c.start()
                            b=Thread(target=playsound.playsound, args=[('audios\sar ji itna free time hey to kuch naya kar lijiye, mujhse baat karne key kya zarurat.mp3')])
                            sa=['xz','zx']
                            stara=random.choice(sa)
                            if sa=='zx':
                                b.start()
                            else:
                                aa()
                            del a
                            del b
                            del sa

                        elif hour>=4 and hour<6:
                            a=Thread(target=playsound.playsound, args=[('audios\sar ji itni unusual time pr laptop khola he, ya fir aap abhi tak kaam kar rahey hain.mp3')])
                            a.start()
                        elif hour>=6 and hour<12:
                            a=Thread(target=playsound.playsound, args=[('audios\mere to bhagya he khul gaye sar, itni subah subah aap mujhse baat karne aaye.mp3')])
                            b=Thread(target=playsound.playsound, args=[('audios\lagta hey kal raat apne zyda padhai nahi key, jaldi ooth gaye aap.mp3')])
                            sa=['xz','zx']
                            stara=random.choice(sa)
                            if stara=='zx':
                                b.start()
                            else:
                                a.start()
                            del a
                            del b
                            del sa
                        elif hour>=12 and hour<16:
                            a=Thread(target=playsound.playsound, args=[('audios\Haan ji sar, bataiye, pooja karli aapne, ya fir bachi he.mp3')])
                            b=Thread(target=playsound.playsound, args=[('audios\sar ji, itni bhri dopahar me kya ookhadne aaye hey.mp3')])
                            sa=['xz','zx']
                            stara=random.choice(sa)
                            if stara=='zx':
                                b.start()
                            else:
                                a.start()
                            del a
                            del b
                            del sa
                        elif hour>=16 and hour<20:
                            a=Thread(target=playsound.playsound, args=[('audios\aek zamana vo huva karta th, jab aap is time par khelne jate they.mp3')])
                            b=Thread(target=playsound.playsound, args=[('audios\shyam ka time hai sar, kyu na aap apni mummy ki help karva dain.mp3')])
                            sa=['xz','zx']
                            stara=random.choice(sa)
                            if sa=='zx':
                                b.start()
                            else:
                                a.start()
                            del a
                            del b
                            del sa
                        elif hour>=20 and hour<22:
                            print('')

                        elif hour>=22 and hour<=23:
                            a=Thread(target=playsound.playsound, args=[('audios\saek zamana vo huva karta th, jab aap is time par khelne jate they.mp3')])
                            b=Thread(target=playsound.playsound, args=[('audios\shyam ka time hai sar, kyu na aap apni mummy ki help karva dain.mp3')])
                            sa=['xz','zx']
                            stara=random.choice(sa)
                            if sa=='zx':
                                b.start()
                            else:
                                a.start()
                            del a#process
                            del b#process
                            del sa#list of process
                            print('')
                        #call talking function
                    else:
                        main2()

########################## NOT IN COMMAND FUNCTION ##########################

            else:
                def new_command():
                    f=open(r'memory/new_command.txt','r')
                    f.seek(0)
                    aall=f.readlines(-1)#this will create an array aall in which all the questions are availabe in the form of an array.
                    last=aall[-1]
                    f.close()#############################
                    if '\n' in last:
                        last.replace('\n','')

                    question_number=int(last[0:last.find(')')])
                    
                    
                    file_command=[]
                    for name in aall:
                        name=name.replace('\n','')
                        s=name[3:]
                        file_command.append(s)
                    
                    command_question=jarvis
                    print('command question : ',command_question)
                    print('file command : ',file_command)
                    if command_question.lower() in file_command:
                        for i in range(len(file_command)):
                            if command_question in file_command[i]:
                                num=i+1########
                                break
                        print('found the question in the file, and can extract the answer')###########
                        f1=open(r'memory/new_command_answer.txt','r')
                        f1.seek(0)
                        answer=f1.readlines(-1)
                        answers=[]
                        for name in answer:
                            a=name.replace('\n','')
                            answers.append(a)
                        for j in range(len(answer)):
                            if int(answer[j][0])==num:
                                ##########
                                gg=answer[j].find(')')
                                final_get=answer[j][gg+1:]
                                sound=gtts.gTTS(final_get, lang='hi')
                                if os.path.exists('audios/sanswer_audios.mp3'):
                                    os.remove('audios/sanswer_audios.mp3')
                                    sound.save('audios/sanswer_audios.mp3')#kis naam se save krna he
                                    t=Thread(target=playsound.playsound, args=(['audios/sanswer_audios.mp3']))
                                    t.start()
                                    
                                    del t
                                else:
                                    sound.save('audios/sanswer_audios.mp3')#kis naam se save krna he
                                    t=Thread(target=playsound.playsound, args=(['audios/sanswer_audios.mp3']))
                                    t.start()
                                    
                                    del t
                                

                                ##########
                                print(answer[j])
                                break
                            
                        f1.close()

                    else:
                        print('new command, will add soon')
                        f=open(r'memory/new_command.txt','a')
                        f.write('\n{}) {}'.format(question_number+1,jarvis))
                        f.close()
                        
                        
                        
                        command=pg.prompt('Sir this is new command, what should be the answer?')
                        f1=open(r'memory/new_command_answer.txt','a')
                        f1.write('\n{}) {}'.format(question_number+1, command))
                        f1.close()
                        
                    
                new_command()
                    
                
                        
                #chatting()
                main2()
            try:
                del choice
                del jarvis
            except:
                try:
                    del jarvis
                except:
                    return None
    main2()
main1()
