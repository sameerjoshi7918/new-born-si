#control from other device using whatsapp

import time
import pyautogui as pg
from datetime import datetime
import os
from PIL import Image
import pytesseract
import keyboard as kd
#################   MY PACKAGE FOR WhatsApp  #####################
import whatsapp_open_check

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
num_arr=[]
last_input=[]
qwerty_len=[]
folder_explore=[]

def get_self_name():#1
    f=open('memory\whatsapp_self_name.txt', 'r')
    a=f.read()
    f.close()
    if len(a)>0:
        print('name already located')
    else:
        name=pg.prompt('Enter the name(as per WhatsApp)  : ')
        f=open('memory\whatsapp_self_name.txt','w')
        f.write(name)
        f.close()
    





def only_me_chat_open():#2
    time.sleep(1)
    a=pg.locateOnScreen(r'images\wt_search.png')
    aa=str(a)
    if aa=='None':
        print(a)
        only_me_chat_open()
    else:
        pg.click(a)
        f=open('memory\whatsapp_self_name.txt','r')
        name=f.read()
        f.close()
        pg.write(name)
        pg.press('enter')
        check()

                




def check():#3
    print('entered check')
    time.sleep(1)
    if os.path.exists('images\online_access.png'):
        os.remove('images\online_access.png')
        im = pg.screenshot('images\online_access.png',region=(1307,838,516,65))
    else:
        im = pg.screenshot('images\online_access.png',region=(1307,838,516,65))#1107,838,716,65

    try:
        print('try strarted')
        query1=pytesseract.image_to_string(Image.open('images\online_access.png'))
        
        first_input=query1.split()#first input from message
        st1=pg.position()
        
        print('Query : ',first_input)
        if 'Python' in first_input:
            num=first_input.index('Python')
            if first_input[num+1]=='start':
                #print('Python start begins here')
                #minimize and maximize the window
                def gogototo():
                    loc=pg.locateCenterOnScreen(r'C:\Users\samee\Desktop\normal_jarvis\images\type_a_message.png')
                    if loc=='None':
                        gogototo()
                    else:
                        pg.click(loc)
                gogototo()
                #pg.click(1100,956)
                pg.write('PROGRAM IS STARTED')
                pg.press('enter')
                print('program finished here, code after')


                def fetch_it():
                    print('entered fetch_it')
                    os.remove('images\online_access.png')
                    time.sleep(1)
                    im = pg.screenshot('images\online_access.png',region=(1307,838,516,65))
                    query1=pytesseract.image_to_string(Image.open('images\online_access.png'))#string
                    user=query1.split()
                    print(user)
                    if 'end' in user:
                        for i in range(len(user)):
                            if user[-1]=='end':
                                user.pop(-1)
                                #print(user)
                                break
                            else:
                                user.pop(-1)
                                #print('For loop again : ',user)
                        a=''
                        for com in user:
                            a+=com
                            a+=' '
                        a=a.rstrip()
                        a=a.lower()
                        print('final command of user is : ',a)
                        write_online='your command is : {}'.format(a)
                        pg.write(write_online)
                        pg.press('enter')
                        print('adding in list')
                        last_input.append(a)

                    else:
                        fetch_it()
                fetch_it()


                
                def drive_function(user_ans):
                    folder=user_ans.upper()
                    pg.write('Do you want to go inside a folder or want to choose from the files of this folder?')
                    pg.press('enter')
                    def qwerty():
                        qwerty_len.append(1)
                        os.remove('images\online_access.png')
                        time.sleep(1)
                        im = pg.screenshot('images\online_access.png',region=(1307,838,516,65))
                        query1=pytesseract.image_to_string(Image.open('images\online_access.png'))#string
                        user=query1.split()
                        print(user)
                        if 'end' in user:
                            for i in range(len(user)):
                                if user[-1]=='end':
                                    user.pop(-1)
                                    #print(user)
                                    break
                                else:
                                    user.pop(-1)
                                    #print('For loop again : ',user)
                            a=''
                            for com in user:
                                a+=str(com)
                                a+=' '
                            a=a.rstrip()
                            #a=a.lower()
                            last_input.append(a)
                            if last_input[-1]==last_input[-2]:
                                if len(qwerty_len)%2!=0:
                                    time.sleep(1)
                                    qwerty()
                        else:
                            qwerty()
                        
                    qwerty()
                    
                    def file_extraction():
                        #last_input[-1]=last_input[-1].lower()
                        pg.write('Write the name of the file.')
                        pg.press('enter')
                        
                        qwerty()
                        print('after qwerty in line 171')
                            
                        file_name=last_input[-1]
                        file_name=file_name.lstrip()
                        file_name=file_name.rstrip()
                        print('before cur dic')
                        print('folerr : ',folder)
                        folder_explore.append(file_name)
                        print('FILE NAME INCLUDES : ',folder_explore)
                        ##
                        if '.' in folder_explore[-1]:
                            t='fyu'
                            directory=str('{}'.format(folder))
                        else:
                            cur_di=folder+'/'
                            print('behind cur_directory  ', cur_di)
                            list_of_files_in_drive=os.listdir(cur_di)
                            print('paasses 182')
                            for i in list_of_files_in_drive:
                                print('in loop')
                                if i==file_name:
                                    directory=str('{}:\{}'.format(folder,file_name))
                                    print(directory)
                                    break
                        print('yaha')
                        pg.click(974,958)
                        time.sleep(0.3)
                        pg.click(1069,575)
                        time.sleep(0.3)
                        pg.moveTo(668,82)
                        time.sleep(0.3)
                        pg.moveRel(-160,0)
                        pg.click()
                        pg.write(directory)
                        time.sleep(0.3)
                        pg.press('enter')
                        
                        pg.click(337,626)
                        time.sleep(0.3)
                        pg.write(file_name)
                        time.sleep(0.3)
                        pg.press('enter')
                        time.sleep(1)
                        pg.press('enter')
                            
                    if 'file' in last_input[-1] or 'files' in last_input[-1] or 'Files' in last_input[-1] or 'File' in last_input[-1]:
                        
                        file_extraction()
                        
                                                    
                                            
                    elif 'folder' in last_input[-1] or 'Folder' in last_input[-1]:
                        def folder_extract():
                            pg.write('Enter the name of the folder')
                            pg.press('enter')
                            qwerty()
                            cur_fol=last_input[-1]
                            print(cur_fol)
                            folder_explore.append('/{}'.format(cur_fol))
                            
                            print(folder_explore)
                            a=''
                            for name in folder_explore:
                                a+=str(name)
                            print(a)
                            dirr=os.listdir(a)##imp
                            for i in range(len(dirr)):
                                on_it=[i+1,') ' ,dirr[i]]
                                final_oop=''
                                for j in on_it:
                                    final_oop+=str(j)
                                    final_oop+=' '
                                    
                                pg.write(final_oop)
                                pg.press('enter')
                                time.sleep(0.3)
                            drive_function(a)
                        folder_extract()
                    else:
                        pg.write('Wronge command, please try again later')
                        pg.press('enter')
                        


                
                #input extractiong function begins
                print(last_input)
                if 'file' in last_input[-1] or 'files' in last_input[-1]:
                    #Educational files
                    #video files
                    #images
                    #documents
                    pg.write('Which Drive should I find the file?')
                    pg.press('enter')
                    fetch_it()
                    time.sleep(0.3)
                    print('Printing last input before entering directory')
                    print(last_input)
                    user_ans=last_input[-1]
                    user_ans=user_ans.lstrip()
                    user_ans=user_ans.rstrip()
                    
                    print('user_ans : ', user_ans)
                    if user_ans=='c':
                        data=user_ans.upper()+':'
                        
                        folder_explore.append(data)
                        list_of_files_in_c_drive=os.listdir(r'C:')
                        for i in range(len(list_of_files_in_c_drive)):
                            on_it=[i+1,') ' ,list_of_files_in_c_drive[i]]
                            final_oop=''
                            for j in on_it:
                                final_oop+=str(j)
                                final_oop+=' '
                            
                            pg.write(final_oop)
                            pg.press('enter')
                            time.sleep(0.3)
                        drive_function(user_ans)
                                                                
                    elif user_ans=='d':
                        print('check1')
                        data=user_ans.upper()+':'
                        print('check2')
                        folder_explore.append(data)
                        print('check3')
                        list_of_files_in_d_drive=os.listdir(r'D:')
                        for i in range(len(list_of_files_in_d_drive)):
                            on_it=[i+1,') ' ,list_of_files_in_d_drive[i]]
                            final_oop=''
                            for j in on_it:
                                final_oop+=str(j)
                                final_oop+=' '
                                
                            pg.write(final_oop)
                            pg.press('enter')
                            time.sleep(0.3)
                        drive_function(user_ans)
                            
            
        else:
            check()
            
    except:
        print('check started from except')
        
whatsapp_open_check.call_this()
get_self_name()
only_me_chat_open()   
#check()

