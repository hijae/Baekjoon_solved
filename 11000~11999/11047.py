#https://www.acmicpc.net/problem/11047
#동전 0

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
cnt=0
for i in arr:
    cnt+=m//i
    m%=i
print(cnt)