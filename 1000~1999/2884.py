#https://www.acmicpc.net/problem/2884
#알람 시계

h,m=input().split()
h=int(h)+24
m=int(m)+60
m=m-45
if m<60:
    h-=1
print(h%24,m%60)