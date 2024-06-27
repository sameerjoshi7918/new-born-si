#creating an table in mysql using python inputs

import mysql.connector
import time
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root")
c=mydb.cursor()
def calling():
        
    t_name=input('Enter the name of table: ')
    a=['create','table',t_name,'(']
    attribute=[]
    att_ins=['insert','into',t_name,'values','(']
    nn=int(input('how many attributes would you like to add: '))
    for i in range(nn):
        aa=input('Enter attribute {}:'.format(i+1))
        bb=input('Enter type of attribute: ')
        attribute.append(aa)
        a.append(aa)
        a.append(bb)
        a.append(',')

    if a[-1]==',':
        a.pop(-1)
    a.append(')')
    str1=''
    for i in a:
        str1+=i
        str1+=' '
    c.execute('use sameer_joshi')
    c.execute('{}'.format(str1))
    print('table ban gayi sir','  ',str1)
    for i in range(len(attribute)):
        entry1=input('Enter the data for attribute {} : '.format(i+1))
        att_ins.append("'")
        att_ins.append(entry1)
        att_ins.append("'")
        att_ins.append(',')
    if att_ins[-1]==',':
        att_ins.pop(-1)
    att_ins.append(')')
    str2=''
    for i in att_ins:
        str2+=i
        str2+=' '
    print(str2)
    time.sleep(1)
    c.execute('{}'.format(str2))
calling()
          
result = c.fetchall();
print(result)
