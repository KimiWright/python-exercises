import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.tulsaworld.com/weather/?mode=week&weather_zip=74103')
soup=BeautifulSoup(r.text, 'lxml')
xingqi=[]
lowtemp=[]
for link in soup.find_all(class_='high-temp'): #class_ is built into BeautifulSoup
        lowtemp.append(link.text.replace('\n','').strip())
for day in soup.find_all(class_='weather-index-time col-sm-1 col-xs-2 opacity-change'):
        xingqi.append(day.text.replace('\n','').strip())
print('5 day forecast:')
for x in range(len(xingqi)):
    print(xingqi[x],' ', lowtemp[x], sep='')
