import os
import glob

#작업하고 있는 위치 변경
#r: 날것의 (윈도우 url구조를 원시 구조로 바꿔주는 코드)
os.chdir(r'C:\Users\student\change\SSAFY지원자')

# #지정된 디렉토리 전체 파일 목록 얻기
# for filename in os.listdir("."):
#     print(filename)
#     #(원래이름,바꿀이름)
#     os.rename(filename,"SAMSUNG_"+filename)



for filename in os.listdir("."):
    after_name = filename.replace('SAMSUNG_SSAFY_','SSAFY_')
    os.rename(filename,after_name)
   

   #010.9689.0525