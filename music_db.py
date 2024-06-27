import time
import pyautogui as pg
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root")
c=mydb.cursor()

def music_check():
    name=pg.getAllTitles()
    for i in range(len(name)):
        if 'Brave' in name[i]:
            print('found at',i)
            if '•' in name[i]:#only works when spotify is active title
                music_name=name[i]
                music_name=music_name[:music_name.index('•')]
                print(music_name)
            break
    
music_check()


