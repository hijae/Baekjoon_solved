#https://www.acmicpc.net/problem/16170
#오늘의 날짜는?

from datetime import datetime
print(datetime.today().strftime("%Y")) #직접 출력해도 되고 이와 같이 실기간으로 시간을 받아 출력도 가능하다.
print(datetime.today().strftime("%m"))
print(datetime.today().strftime("%d"))