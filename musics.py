import time
import webbrowser
import pyautogui as pg
import return_to_jarvis
import os
import speech_recognition as s
import playsound
import random
from threading import Thread
import mouse_check
jarvis_names=['jarvis','jarbis','uncle','service','Oo halo','hello','chotu','javis','beta','jarcis','beta jarvis','jarvios','jarvi']
def cc():
    time.sleep(1)
    a=pg.locateCenterOnScreen('images\music_library.png')
    na=str(a)
    if na=='None':
        del na
        del a
        cc()
    else:
        del a
        del na
        
def closing():
    time.sleep(1)
    titles=pg.getAllTitles()
    for i in range(len(titles)):
        if 'Spotify' in titles[i]:
            openit=titles[i]
            break
    try:
        if 'Spotify' in openit:
            pg.moveTo(1377, 230)
            time.sleep(0.4)
            pg.click()
            time.sleep(0.3)
            pg.hotkey('space')
        else:
            print('baj to raha he sir')
        
    except:
        t=Thread(target=playsound.playsound, args=['audios\sGaana baj to raha hey sar.mp3'])
        t.start()
        del t


    
def player_online():
    titles=pg.getAllTitles()
    
    for i in range(len(titles)):
        if 'Brave' in titles[i]:
            openit=titles[i]
            break
    try:
        pg.getWindowsWithTitle(openit)[0].minimize()
        pg.getWindowsWithTitle(openit)[0].maximize()
    except:
        return None
    time.sleep(1)
    pg.click(1634, 71, duration=0.4)
    time.sleep(1)
    pg.moveRel(-345,143)
    pg.click()
    time.sleep(1)


    
def okay():
    scroll_list=['-1539','-939','-1279','-8999','-2500','-12000']
    #############sombari,#jai jai#sooraj d#jarico#hookha##naan
    select=random.choice(scroll_list)
    time.sleep(0.5)
    pg.click()
    print('clicked')
    
    time.sleep(1)
    pg.moveTo(505,730)
    time.sleep(0.3)
    pg.scroll(-20)
                
    pg.scroll(int(random.choice(scroll_list)))#yaha random dalne he -9320
    time.sleep(3)
    pg.click()#jarico
    time.sleep(1)
    def again():
        titles=pg.getAllTitles()
        for i in range(len(titles)):
            if 'sameer' in titles[i]:
                openit=titles[i]
                pg.moveRel(0,5)
                pg.click()
                del titles
                again()
            else:
                return None
    again()

    
def music_player():
    t = Thread(target=playsound.playsound, args=["audios\Do_you_want_to_hear_my_playlist.mp3"])
    t.start()
    del t
    playlist_option=pg.prompt('Do you want to hear my playlist')
    if playlist_option=='ha' or playlist_option=='yes' or playlist_option=='ya' or playlist_option=='yup' or playlist_option=='ok':
        print("ok then let me play randomly")
        t = Thread(target=playsound.playsound, args=["audios\ok then let me play randomly.mp3"])
        t.start()
        del t
        song_by=['sameer','wei','suspence']
        song_choice=random.choice(song_by)
        
        song_choice='sameer'####################################333
        player_online()
        time.sleep(2)
        if song_choice=='sameer':
            print('sameer chosen')
            music_willq=pg.locateCenterOnScreen('images\music_library.png')
            music_will=str(music_willq)
            if music_will=='None':
                webbrowser.open('https://open.spotify.com/')
                cc()
                time.sleep(1)
                print('opening white sameer')
                x=pg.locateCenterOnScreen('images\sameer_playlist.png')
                play=str(x)
                if play=='None':
                    x1=pg.locateCenterOnScreen('images\sameer_not_green.png')
                    time.sleep(1)
                    pg.moveTo(x1)
                    time.sleep(1)
                    okay()
                else:
                    time.sleep(0.5)
                    pg.moveTo(x)
                    time.sleep(0.3)
                    okay()
            else:
                closing()



        elif song_choice=='wei':
            print('wei chosen')
            music_will=str(pg.locateCenterOnScreen('images\music_library.png'))

            if music_will=='None':
                webbrowser.open('https://open.spotify.com/')
                cc()
                time.sleep(1)
                x=pg.locateCenterOnScreen('images\wei_at_green.png')
                play1=str(x)
                if play1=='None':
                    x1=pg.locateCenterOnScreen('images\white_not_at_wei.png')
                    time.sleep(0.5)
                    pg.moveTo(x1)
                    time.sleep(0.5)
                    pg.click()
                    time.sleep(1)
                    pg.moveTo(520,553,1)
                    time.sleep(1)
                    pg.scroll(-380)
                    time.sleep(1)
                    pg.click()
                    
                else:
                    time.sleep(0.5)
                    pg.moveTo(x)
                    time.sleep(0.3)
                    pg.click()
                    time.sleep(0.3)
                    pg.moveTo(520,553,1)
                    time.sleep(0.3)
                    pg.scroll(-380)
                    time.sleep(1)
                    pg.click()
            else:
                closing()

        elif song_choice=='suspence':
            print('suspence chosen')
            music_will=str(pg.locateCenterOnScreen('images\music_library.png'))

            if music_will=='None':
                webbrowser.open('https://open.spotify.com/')
                cc()
                time.sleep(1)
                x=pg.locateCenterOnScreen('images\suspence_green.png')
                play1=str(x)
                if play1=='None':
                    x1=pg.locateCenterOnScreen('images\white_at_suspence.png')
                    time.sleep(0.5)
                    pg.moveTo(x1)
                    time.sleep(0.3)
                    pg.click()
                    time.sleep(0.3)
                    print('if line 204')
                    pg.moveTo(520,553,1)
                    time.sleep(0.3)
                    pg.scroll(-320)
                    time.sleep(1)
                    pg.click()
                    
                else:
                    time.sleep(0.5)
                    pg.moveTo(x)
                    time.sleep(0.3)
                    pg.click()
                    time.sleep(0.3)
                    pg.moveTo(520,553,1)
                    time.sleep(0.3)
                    pg.scroll(-320)
                    time.sleep(1)
                    pg.click()
            else:
                closing()
                
            

        
    elif (playlist_option in jarvis_names):
        print('Yes Boss!')
        t=Thread(target=playsound.playsound, args=['audios\yesboss.mp3'])
        t.start()
        del t
        
        
    else:
        t = Thread(target=playsound.playsound, args=["audios\Enter_the_name_of_the_music_you_want_to_listen_to.mp3"])
        t.start()
        del t
        music_name=pg.prompt('Enter the name of the song you want to listen to')
        if (music_name in jarvis_names):
            print('Yes Boss!')
            t = Thread(target=playsound.playsound, args=["audios\yesboss.mp3"])
            t.start()
            del t
            return_to_jarvis.back_to_jarvis()
        else:
            if music_name=='Jericho':
                music_name='jarico'
            print('Playing.....',music_name,'Now')
            time.sleep(1)
            player_online()
            music_will=str(pg.locateCenterOnScreen('images\music_library.png'))
            if music_will=='None':
                webbrowser.open('https://open.spotify.com/')
                cc()
            def cop():
                time.sleep(1)
                music_wil=str(pg.locateCenterOnScreen('images\music_library.png'))
                naq=str(music_wil)
                if naq=='None':
                    del naq
                    del music_wil
                    cop()
                else:
                    del music_wil
                    del naq
            cop()
            time.sleep(1)
            #move to search baar of spotify
            sese=pg.locateCenterOnScreen('images\spotify_search.png')
            pg.moveTo(sese)
            time.sleep(1)
            pg.click()
            time.sleep(3)
            pg.write(music_name, interval=0.2)
            pg.press('enter')
            def cola():
                time.sleep(1)
                amy=pg.locateOnScreen(r'images\top_result.png')
                na=str(amy)
                if na=='None':
                    cola()
                else:
                    time.sleep(1)
                    pg.moveTo(1100, 641, 1)#751
                    pg.click()
                    del amy
                    del na
            cola()
            
        del music_name
    try:
        del song_choice
        del song_by
    except:
        del song_by
#music_player()
