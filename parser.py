import requests
from bs4 import BeautifulSoup

headers={
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
url="https://cbr.ru/currency_base/daily/"
req=requests.get(url,headers=headers)
src=req.text
soup=BeautifulSoup(src,'lxml')
tbl=soup.find('table',class_='data').find_all('tr')
euro=tbl[15].find_all('td')
euro=euro[-1].text
dollar=tbl[14].find_all('td')
dollar=dollar[-1].text
yuan=tbl[23].find_all('td')
yuan=yuan[-1].text
print('Курс евро: '+euro+' рублей\nКурс доллара: '+dollar+' рублей\nКурс юаня: '+yuan+' рублей')