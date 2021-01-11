#https://www.acmicpc.net/problem/10250
#ACM 호텔

c=int(input())
for i in range(c):
    h,w,n=map(int,input().split())
    print(100*((n-1)%h+1)+(n-1)//h+1)