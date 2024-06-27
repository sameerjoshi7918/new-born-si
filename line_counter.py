#counting all the number of line of code written in all python files
import  pyttsx3 as ppt
from threading import Thread
def liner():
    with open(r'C:\Users\samee\Desktop\normal_jarvis\jarvis.pyw','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\alarm_clock.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1

    with open(r'C:\Users\samee\Desktop\normal_jarvis\virtual_mouse.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1

    with open(r'C:\Users\samee\Desktop\normal_jarvis\auto_wt.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\call_receiver.pyw','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\name_check.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\camera_check.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1

    with open(r'C:\Users\samee\Desktop\normal_jarvis\whatsapp_open_check.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1

    with open(r'C:\Users\samee\Desktop\normal_jarvis\spotify_open.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\comparision_of_2_photos.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\folder_check.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\instagram_open.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\mobile.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\mouse_check.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\musics.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\news_watch.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\pygame_volume.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\recycler.pyw','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\return_to_jarvis.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\time_check.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\title_checker.pyw','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\volume_check.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\whatsapp_message_sender.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    
    with open(r'C:\Users\samee\Desktop\normal_jarvis\line_counter.py','r') as fp:
        for count, line in enumerate(fp):
            pass
    total_number=total_number+count+1
    print('Total number of lines is {}'.format(total_number))
    t=Thread(target=ppt.speak, args=[('Total number of lines is {}'.format(total_number))])
    t.start()
    del t

#liner()
