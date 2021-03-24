#https://www.acmicpc.net/problem/10807
#개수 세기

n=int(input())
arr=map(int,input().split())
v=int(input())
cnt=0
for i in arr:
    if v==i:
        cnt+=1
print(cnt)