#https://www.acmicpc.net/problem/16396
#선 그리기

n=int(input())
arr=[0 for _ in range(10000)]
for i in range(n):
    x,y=input().split()
    for _ in range(int(x),int(y)):
        arr[_-1]=1
cnt=0
for i in range(10000):
    cnt+=arr[i]
print(cnt)