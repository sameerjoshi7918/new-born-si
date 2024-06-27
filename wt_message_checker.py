import requests
from bs4 import BeautifulSoup
def fands(url, path):
    r=requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup)
url='https://www.instagram.com/'
#r=requests.get(url)
#print(r.text)
fands(url,'scrap\whatsapp_data.html')
