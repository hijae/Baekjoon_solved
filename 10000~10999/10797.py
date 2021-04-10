#https://www.acmicpc.net/problem/10797
#10부제

n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in arr:
    if i==n:
        cnt+=1
print(cnt)