# https://www.acmicpc.net/problem/25305
# 커트라인

n,k=map(int,input().split())
x=list(map(int,input().split()))

x.sort()
print(x[n-k])