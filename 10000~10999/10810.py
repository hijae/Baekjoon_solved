# https://www.acmicpc.net/problem/10810
# 공 넣기

n,m=map(int,input().split())
arr=[0]*n
for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a-1,b):
        arr[j]=c
for i in arr:
    print(i,end=' ')
print()