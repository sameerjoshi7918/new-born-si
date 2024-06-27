from bs4 import BeautifulSoup as bs
import requests

url='https://web.whatsapp.com/'
page= requests.get(url)
soup=bs(page.text, features="html.parser")
#soup=soup.prettify()
#print(soup)

print(soup.find_all('div'))

