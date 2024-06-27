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
            name=str(pg.getActiveWindowTitle())
            if 'Brave' in name:
                print('brave is already active window')
                openit=titles[i]
            else:
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
    asa=[]
    taa=[]#to check the number of parsing for okay()
    
    def okay():
        time.sleep(0.3)
        title=pg.getActiveWindowTitle()
        if '•' in title or 'Spotify' in title:
            print('spotify found')
        else:
            asa.append(title)
            if (len(asa)==1):
                print('do nothing')
            else:
                if asa[0]==asa[-1] and len(asa)>1:
                    print('spotify not found, open new spotify')
                    webbrowser.open('https://www.spotify.com/')
                else:
                    pg.hotkey('ctrl','tab')
            okay()
        
    okay()
#call_this()
