import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"

res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

kbos = soup.select('#asiaBody tr.link')

for kbo in kbos:
    print((kbo.select_one("td.name a").text)+(kbo.select_one("td.idx").text))
    print("----")

print("bye")    
