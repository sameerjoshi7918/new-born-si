import pyautogui as pg
import time
from datetime import datetime
import os


c=datetime.now()
cur_time=c.strftime('%H:%M')
cur_date=c.strftime('%d-%m-%y')
print(cur_date)
cur_time=str(cur_time)


f=open(r'txt_files\text_data_for_ai.arff','a+')
def write_in_file():
    
    time.sleep(3)
    title=pg.getActiveWindowTitle()
    f.seek(0)
    a=f.readlines()
    last_line=a[-1]
    last_line=last_line.split()
    print(last_line)

    
    #if title==last_line:
#        print('do nothing')
 #   else:
  #      f.write("""'{}', {}, {}\n""".format(title, cur_date, cur_time))
   # write_in_file()

write_in_file()

f.close()
f=open(r'txt_files\text_data_for_ai.arff','r')
def read_function():
    #f.seek(2)
    p=f.readlines()#[-1]
    print(type(p))
    print(p)
#read_function()
#os.startfile(r'txt_files\text_data_for_ai.arff')
