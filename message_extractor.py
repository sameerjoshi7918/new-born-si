from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
wt=pytesseract.image_to_string(Image.open(r'images\all_messages.png'))
print(wt)
a=wt.split()


message_all=[]
for i in range(len(a)):
    if a[i]=='pm':
        ww=int(a.index('pm'))
        a.pop(ww)
        a.insert(ww, ' ')
    elif '.' in a[i]:
        a.pop(a.index(a[i]))
        a.insert(a.index(a[i]), ' ')
    elif 'pm' in a[i]:
        a.pop(int(a.index(a[i])))
        a.insert(a.index(a[i]), ' ')
    elif '-' in a[i]:
        a.pop(int(a.index(a[i])))
        a.insert(a.index(a[i]), ' ')
del i
message=a
for j in range(len(message)):
    try:  
        if ' ' in message[j]:
            if message[j+1]==' ':
                message.pop(j+1)
        else:
            if len(message)==j+1:
                message.pop(j)
    except:
        acha=''
            
del j
pop_list=[]
for i in range(len(message)):
    if message[i]==' ':
        if len(message_all)==0:   
            new=(message[0:i])
            num=i
            str1=''
            for j in new:
                str1+=j
                str1+=' '
            message_all.append(str1)
            pop_list.append(i)
        else:
            new=(message[num:i])
            str1=''
            for j in new:
                str1+=j
                str1+=' '
            message_all.append(str1)
            num=i
for i in range(len(message_all)):
    check=message_all[i]
    if check[0]==' ':
        check=check.removeprefix(' ')
        check=check.removesuffix(' ')
        check=check.removeprefix(' ')
        check=check.removesuffix(' ')
        check=check.removeprefix(' ')
        check=check.removesuffix(' ')
        message_all.pop(i)
        message_all.insert(i, check)

final_messages=message_all
print(a)
print(final_messages)
