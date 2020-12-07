#https://www.acmicpc.net/problem/2776
#암기왕

t=int(input())
for i in range(t):
    n=int(input())
    num=set(map(int,input().split()))
    m=int(input())
    arr=list(map(int,input().split()))
    for j in arr:
        if j in num:
            print(1)
        else:
            print(0)