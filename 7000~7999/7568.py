# https://www.acmicpc.net/problem/7568
# 덩치

n=int(input())
weight=[]
height=[]

for i in range(n):
    a,b=map(int,input().split())
    weight.append(a)
    height.append(b)

for i in range(n):
    rank=1
    for j in range(n):
        if weight[i]<weight[j] and height[i]<height[j]:
            rank+=1
    print(rank,end=' ')
print()