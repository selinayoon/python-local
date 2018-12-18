import webbrowser

#검색하고 싶은 키워드
q_list = ["이대훈","블랙핑크","정보처리기사","아이유"]

url = "https://www.google.com/search?q="

#https://www.google.com/search?hl=ko&source=hp&ei=VEkYXJ3tF4mC8gXrpKD4CA&q=ssafy&btnK=Google+%EA%B2%80%EC%83%89&oq=ssafy&gs_l=psy-ab.3..35i39j0i20i263j0j0i10j0l3j0i67j0i10l2.3532.4554..4909...1.0..0.109.626.1j5......0....1..gws-wiz.....6..0i131.W-fZZNTmglY

#브라우저 열어주기

for q in q_list:
    webbrowser.open(url+q) 