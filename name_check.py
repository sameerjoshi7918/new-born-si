#new string creation
import pyautogui as pg
import pyttsx3 as pt
import gtts
import playsound
from threading import Thread
import os
def name():
    t=Thread(target=playsound.playsound, args=[('sEnter your full name.mp3')])
    t.start()
    del t
    name1=pg.prompt("Enter your full name : ")
    name_surname=name1.split()

    name=name_surname[0]
    surname_ladka=name_surname[1]
    if name=='sameer' or name=='samer':
        var='sameer'
    if name[-1]=='a' or name[-1]=='e' or name[-1]=='i' or name[-1]=='o' or name[-1]=='u':
        t=Thread(target=playsound.playsound, args=[('sEnter your partner name.mp3')])
        t.start()
        del t
        ladka_name=pg.prompt("Enter your partner name : ")
        ladka_name_surname=ladka_name.split()
        name2_new=ladka_name_surname[0]
        if name2_new[-1]=='a' or name2_new[-1]=='e' or name2_new[-1]=='i' or name2_new[-1]=='o' or name2_new[-1]=='u':
            if os.path.exists("sIt means you are lesbian.mp3"):
                t=Thread(target=playsound.playsound, args=[('sIt means you are lesbian.mp3')])
                t.start()
                del t
            else:
                text='It means you are lesbian'
                sound=gtts.gTTS(text, lang='hi')
                sound.save('sIt means you are lesbian.mp3')
                #playsound.playsound('sIt means you are lesbian.mp3')
                t=Thread(target=playsound.playsound, args=[('sIt means you are lesbian.mp3')])
                t.start()
                del t
        else:
            ladka_surname=ladka_name_surname[1]
            if os.path.exists('sHey girl, your new name after marriage will be.mp3'):
                os.remove('sHey girl, your new name after marriage will be.mp3')

                
                text='Hey girl, your new name after marriage will be {} {}'.format(name,ladka_surname)
                sound=gtts.gTTS(text, lang='hi')
                sound.save('sHey girl, your new name after marriage will be.mp3')
                
                t=Thread(target=playsound.playsound, args=[('sHey girl, your new name after marriage will be.mp3')])
                t.start()
                del t
            else:
                text='Hey girl, your new name after marriage will be {}'.format(name,ladka_surname)
                sound=gtts.gTTS(text, lang='hi')
                sound.save('sHey girl, your new name after marriage will be.mp3')
                
                t=Thread(target=playsound.playsound, args=[('sHey girl, your new name after marriage will be.mp3')])
                t.start()
                del t
        del ladka_name
        del ladka_name_surname
        del name2_new
    else:
        t=Thread(target=playsound.playsound, args=[('sEnter your partner name.mp3')])
        t.start()
        del t
        name2=pg.prompt("Enter your lovers name : ")
        ladki=name2.split()
        ladki_name=ladki[0]
        ladki_surname=ladki[1]
        if ladki_name[-1]=='a' or ladki_name[-1]=='e' or ladki_name[-1]=='i' or ladki_name[-1]=='o' or ladki_name[-1]=='u':
            if os.path.exists('syo boye name.mp3'):
                os.remove('syo boye name.mp3')
                if var=='sameer':
                    if os.path.exists('sameer_sir_cal.mp3'):
                        os.remove('sameer_sir_cal.mp3')
                        text='Wow sir, Your Bride name after marriage will be {} {}'.format(ladki_name,surname_ladka)
                        sound=gtts.gTTS(text, lang='hi')
                        sound.save('sameer_sir_cal.mp3')
                        
                        t=Thread(target=playsound.playsound, args=[('sameer_sir_cal.mp3')])
                        t.start()
                        del t
                    else:
                        text='Wow sir, Your Bride name after marriage will be {} {}'.format(ladki_name,surname_ladka)
                        sound=gtts.gTTS(text, lang='hi')
                        sound.save('sameer_sir_cal.mp3')
                        
                        t=Thread(target=playsound.playsound, args=[('sameer_sir_cal.mp3')])
                        t.start()
                        del t
                    
                else:
                    text='Yo Boy, your girls name, after marriage will be : {} {}'.format(ladki_name,surname_ladka)
                    sound=gtts.gTTS(text, lang='hi')
                    sound.save('syo boye name.mp3')
                    
                    t=Thread(target=playsound.playsound, args=[('syo boye name.mp3')])
                    t.start()
                    del t
            else:
                text='Yo Boy, your girls name, after marriage will be : {} {}'.format(ladki_name,surname_ladka)
                sound=gtts.gTTS(text, lang='hi')
                sound.save('syo boye name.mp3')
                
                t=Thread(target=playsound.playsound, args=[('syo boye name.mp3')])
                t.start()
                del t
        else:                
            t=Thread(target=playsound.playsound, args=[('sBro you are gay.mp3')])
            t.start()
            del t
        del name2
        del ladki
        del ladki_name
        del ladki_surname
        try:
            del var
            del name1
            del name_surname
            del name
            del surname_ladka
        except:
            return None
#name()
