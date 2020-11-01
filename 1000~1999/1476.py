#https://www.acmicpc.net/problem/1476
#날짜 계산

n=1
a,b,c=map(int, input().split())
while True:
    if (n-a)%15==0 and (n-b)%28==0 and (n-c)%19==0:
        print(n)
        break
    n+=1

