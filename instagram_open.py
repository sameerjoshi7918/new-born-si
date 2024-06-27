import pyautogui as pg
import webbrowser
import time
import return_to_jarvis
import win32api
import playsound
import mouse_check
from threading import Thread

def insta_open():
    t = Thread(target=playsound.playsound, args=["audios\Do_you_want_to_send_a_message_to_perticular_person.mp3"])
    t.start()
    del t
    def kuch():
        playsound.playsound('audios\Enter_meassage.mp3')
        message=pg.prompt('Message')
        webbrowser.open("{}".format(web_insta_id))
        time.sleep(8)
        pg.moveTo(1200,950)
        pg.click()
        pg.write(message)
        pg.press("enter")
        time.sleep(1)
        mouse_check.mouce()
    need=pg.prompt("Do you want to send a message to perticular person? ")
    if need=='yes' or need=='ya' or need=='ha' or need=='yup':
        #playsound.playsound('audios\ame.mp3')
        name=pg.prompt('Name')
        if name=='abbas':
            web_insta_id='https://www.instagram.com/direct/t/103049507930529/'
        elif name=='ishika':
            web_insta_id="https://www.instagram.com/direct/t/17843044829844986/"
        elif name=='vp':
            web_insta_id='https://www.instagram.com/direct/t/101036831299119/'
        elif name=='right' or name=='right benchers' or name=='right banchers' or name=='right bencher' or name=='right bancher':
            web_insta_id='https://www.instagram.com/direct/t/5745433222145120/'
        elif name=='teena' or name=='tina':
            web_insta_id='https://www.instagram.com/direct/t/17843435996072331/'
        elif name=='daksh':
            web_insta_id='https://www.instagram.com/direct/t/100955991401691/'
        elif name=='mini':
            web_insta_id='https://www.instagram.com/direct/t/17851764740664423/'
        else:
            message=pg.prompt('Message')
            time.sleep(1)
            webbrowser.open('https://www.instagram.com/')
            time.sleep(8)
            pg.moveTo(128, 418,1)
            time.sleep(0.3)
            pg.click()
            time.sleep(1)
            pg.write(name, interval=0.3)
            time.sleep(1)
            pg.press('enter')
            time.sleep(4)
            x1=pg.locateOnScreen('images\ssfollowing.png')
            aa=str(x1)
            if aa=='None':
                print('Sir pehle follow to kar lijiye')
            else:
                if name[-1]=='a' or name[-1]=='e' or name[-1]=='i' or name[-1]=='o' or name[-1]=='u':
                    print('Kya Boss, kuch kam se bat krni he ya fir.....')
                    pg.moveTo(x1)
                    time.sleep(0.3)
                    pg.moveRel(178,1, 1)
                    time.sleep(1)
                    pg.click()
                else:
                    pg.moveTo(x1)
                    time.sleep(0.3)
                    pg.moveRel(178,1, 1)
                    time.sleep(1)
                    pg.click()
        message=pg.prompt('Message')
        webbrowser.open(web_insta_id)
        time.sleep(10)
        pg.click(1344, 949)
        time.sleep(0.3)
        pg.write(message, interval=0.2)
        time.sleep(0.4)
        pg.press('enter')
        mouse_check.mouce()
        
        
                
    else:
        webbrowser.open('https://www.instagram.com')
        savedpos = win32api.GetCursorPos()
        time.sleep(10)
        curpos = win32api.GetCursorPos()
        if savedpos == curpos:
            return_to_jarvis.back_to_jarvis()
    
#insta_open()
