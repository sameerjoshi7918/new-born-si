import win32api
import pyautogui as pg
import webbrowser
import random
import time

print('start')

                
def back():
        time.sleep(1)
        titles=pg.getAllTitles()
        for i in range(len(titles)):
            if 'Coursera' not in titles[i] or 'AllAnime' not in titles[i] or 'YouTube' not in titles[i] or 'VLC' not in titles[i]:
                print(titles[i])
                del titles
                d1=pg.position()
                time.sleep(100)#100
                titles=pg.getAllTitles()
                d2=pg.position()
                if d1==d2:
                        pg.moveRel(30,10)
                        p1=win32api.GetCursorPos()
                        print('back entered')
                        time.sleep(50)#30
                        p2=win32api.GetCursorPos()
                        print('checked')
                        if p1==p2:
                            print('opening')
                            time.sleep(4)
                            pg.hotkey('win','d')
                            time.sleep(1)
                            pg.moveTo(56,60)
                            time.sleep(1)
                            pg.click()
                            pg.press('enter')
                            pg.moveTo(437,283)
                            time.sleep(0.4)
                            pg.click()
                            time.sleep(0.3)
                            pg.hotkey('ctrl','a')
                            time.sleep(1)
                            pg.hotkey('delete')
                            time.sleep(1)
                            pg.press('enter')
                            pg.moveTo(1878,17)
                            time.sleep(0.3)
                            pg.click()
                            time.sleep(0.3)
                            pg.moveTo(1300,1050,2)
                            time.sleep(2)
                            pg.click()
                            pg.moveTo(1400,950, 1)
                            pg.click()
                            time.sleep(1)
                            scroll_list=['-1862','-1260','-1600','-9320','-2600']
                            select=random.choice(scroll_list)
                            webbrowser.open('https://open.spotify.com/')
                            time.sleep(9)
                            
                            pg.moveTo(162,685)
                            time.sleep(1)
                            pg.click()
                            time.sleep(1)
                            pg.moveTo(1697, 1040, 1)
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(1866, 849, 1)
                            pg.click()
                            time.sleep(1)
                            ll=pg.locateCenterOnScreen('images\head_connected.png')
                            call=str(ll)
                            if call=='None':
                                print('headphones not found ')
                                time.sleep(1)
                                titles=pg.getAllTitles()
                                print(titles)
                                for i in range(len(titles)):
                                        if 'Spotify' in titles[i]:
                                                
                                                #print(titles[i])
                                                print('Spotify found')
                                                openit=titles[i]
                                                time.sleep(1)
                                                
                                                time.sleep(1)
                                                pg.getWindowsWithTitle(openit)[0].maximize()
                                                time.sleep(3)
                                                pg.moveTo(162,685)
                                                time.sleep(1)
                                                pg.click()
                                                time.sleep(1)
                                                pg.moveTo(523,553, 1)
                                                time.sleep(0.9)
                                                pg.scroll(int(select))#yaha random dalne he -9320
                                                time.sleep(5)
                                                pg.click()#jarico
                                                time.sleep(1)
                                                back()
                            else:
                                    print('headphones are connected')
                                    pg.moveTo(1598, 491, 1)
                                    time.sleep(0.4)
                                    pg.click()
                                    titles=pg.getAllTitles()
                                    print(titles)
                                    for i in range(len(titles)):
                                        if 'Spotify' in titles[i]:
                                            #print(titles[i])
                                            print('Spotify found')
                                            openit=titles[i]
                                    try:
                                            time.sleep(1)
                                            
                                            time.sleep(1)
                                            pg.getWindowsWithTitle(openit)[0].maximize()
                                            time.sleep(3)
                                            pg.moveTo(162,685)
                                            time.sleep(1)
                                            pg.click()
                                            time.sleep(1)
                                            pg.moveTo(523,553, 1)
                                            time.sleep(0.9)
                                            pg.scroll(int(select))#yaha random dalne he -9320
                                            time.sleep(5)
                                            pg.click()#jarico
                                            time.sleep(1)
                                            back()
                                    except:
                                            print('Spotify is not opened')
                                            webbrowser.open('https://open.spotify.com/')
                                            time.sleep(9)
                                            pg.moveTo(162,685)
                                            time.sleep(1)
                                            pg.click()
                                            time.sleep(1)
                                            pg.moveTo(523,553, 1)
                                            time.sleep(0.9)
                                            pg.scroll(int(select))#yaha random dalne he -9320
                                            time.sleep(5)
                                            pg.click()#jarico
                                            time.sleep(1)
                                            back()
                        else:
                            back()
                else:
                        pg.moveRel(20,20)
                        back()
            
        print('back')
        back()
try:
        back()
except:
        back()
