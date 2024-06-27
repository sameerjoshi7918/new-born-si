#talking function

import time
import random
import pyautogui as pg
from threading import Thread
import playsound

def talk():
    ques=['what','how','why','who','whom','when','where']
    message=pg.prompt('Type:')
    messag=message.lower()
    mes=messag.split()
    if 'hi' in mes or 'hi,' in mes or 'hello' in mes or 'hey' in mes:
        if len(mes)<4:
            str1=''
            for ele in mes:
                str1+=ele
                str1+=' '
            if ',' in str1:
                print('lagta he aap commas ka bahut use karte he')
                print('Aap, bataiye, kese he aap?')
        elif len(mes)>4:
            if 'sameer' in mes or 'joshi' in mes:
                print('I know you name sir')
            elif 'what' in mes:
                qq=mes.index('what')
                if mes[qq+1]=='is':
                    print('you types what is.........') #here aswell
            elif 'where' in mes:
                ww=mes.index('where')
                if mes[ww+1]=='are':
                    print('question')#we are gonna add new things over here
            elif 'how' in mes:
                ee=mes.index('how')
                if mes[ee+1]=='are':
                    print('You typed how are')
    else:
        print('Other then that')
    t=Thread(target=playsound.playsound, args=[('audios\sHey there sir how do you do.mp3')])
    t.start()
    del t
    message=pg.prompt('Hey there sir!, how do you do?')
    mes=message.split()
    print(mes)
    if 'name' in mes:
        qw=mes.index('name')
        if mes[qw+1]=='is':
            #a,e,i,o,u
            name=mes[qw+2]
            name1=name[0].upper()
            name=name.removeprefix('s')
            final_name=name1+name
            if name[-1]=='a' or name[-1]=='e' or name[-1]=='i' or name[-1]=='o' or name[-1]=='u':
                print('I will remember you name Miss. {}'.format(final_name),'good to talking to you')
            else:
                print('Hi dude! {}'.format(final_name),'nice Name')
            message=pg.prompt('Kuch bhi likh sakti he.')
    else:
        t=Thread(playsound.playsound, args=[('audios\sLets me start talking I will start.mp3')])
        t.start()
        del t
        print('Lets me start talking, I will start')


talk()
















