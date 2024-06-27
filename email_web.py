import pyautogui as pg
import time
import webbrowser

#whatsapp checking that whether it is open
def call_this():
    
    titles=pg.getAllTitles()
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
    a=openit
    print(a)

    def okay():
        b=str(pg.locateCenterOnScreen('images\compose_email.png'))
        if b!='None':
            print('Email found from b')
        else:
            pg.hotkey('ctrl','tab')
            title=pg.getAllTitles()
            for i in range(len(title)):
                if 'Brave' in title[i]:
                    openq=title[i]
                    break
            try:
                if openq==a:
                    print('Gmail not opened yet')
                    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
                    time.sleep(6)
                else:
                    okay()
            except:
                return None
    okay()
