#https://www.acmicpc.net/problem/1110
#더하기 사이클

cnt=0
m=n=int(input())
a=0
b=0

while 1:
    cnt=cnt+1
    b=m//10+m%10
    a=m%10
    m=a*10+b%10
    if n==m :
        break
print(cnt)