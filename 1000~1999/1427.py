#https://www.acmicpc.net/problem/1427
#소트인사이드

n=list(input())
for i in range(len(n)):
    n[i]=int(n[i])
n.sort(reverse=True)
for i in n:
    print(i,end='')
print()