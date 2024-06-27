import pyautogui as pg
import time
import webbrowser
import os

#whatsapp checking that whether it is open
def call_this():
    titles=pg.getAllTitles()
    for i in range(len(titles)):
        if 'Brave' in titles[i]:
                #print(titles[i])
                #print('brave found')
                openit=titles[i]
                break
    try:
        #print('entered try')
        pg.getWindowsWithTitle(openit)[0].minimize()
        pg.getWindowsWithTitle(openit)[0].maximize()
        time.sleep(1)
    except:
        os.startfile(r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe')
        time.sleep(2)

    def okay():
        a1=pg.getActiveWindowTitle()
        #print('active window : ',a1)
        
        def cc():
            pg.hotkey('ctrl','tab')
            next_til=pg.getActiveWindowTitle()
            
            if a1==next_til:
                #print('whatsapp not opened, opening whatsapp')
                webbrowser.open('https://web.whatsapp.com/')
            elif 'WhatsApp' in next_til:
                print('')
            else:
                #print('else statement at last')
                cc()
        if 'WhatsApp' in a1:
            print('')
        else:
            cc()
        
    okay()
#call_this()
