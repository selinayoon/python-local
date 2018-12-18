import requests
from bs4 import BeautifulSoup

print("Hello")

url = "https://www.daum.net/"

res = requests.get(url).text


soup = BeautifulSoup(res,'html.parser')

#앞의 li~ 는 li만 남겨두고 지운다 : 모든 li를 다 가져오기
#코드 안에 child는 bs4가 인식을 못해 type으로 고친다

pick = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')
#코드 분석 : 아이디가 Article + 클래스가 cmain_tmp  인거 ~ +  li 목록 가져오기 
print(pick)

 #a 태그에 있는 텍스트만 뽑아오기 
 for  p in 