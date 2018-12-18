import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response,'html.parser')
music_table = soup.select("table tr.lst50") #리스트 

for music in music_table:
    number = music.select_one("span.rank").text #랭크에 대한 정보
    title = music.select_one("div.wrap_song_info a").text #제목에 대한 정보 
    title = music.select_one("div.rank01 a").text #제목에 대한 정보 
    print(number +"위 : "+ title)
