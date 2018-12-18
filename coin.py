import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"


res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')

# #coinlist 중에서 tbody요소만 찾아올래
# coin = soup.select('tbody.coin_list')

#coinlist 중에서 tbody요소만 찾아올래 + tr만 가져올래
coins = soup.select('#fxprint > table > tbody > tr ')

print(coins)
#반복문 돌려 출력 : 한줄이 하나씩 출력 
#텍스트 형식으로 첫번째 항목(이름) 텍스트 형식으로 출력 : td:nth-of-type(1) a strong
#두번째 항목 (가격): td:nth-of-type(2)  strong
#for coin in coins:
    # print(coin.select_one ("td:nth-of-type(1) a strong").text) #a태그 안에 strong
    # print(coin.select_one ("td:nth-of-type(2)  strong").text) 
    # print("-------")
#fxprint > table > tbody > tr > td:nth-child(2)