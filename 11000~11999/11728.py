#https://www.acmicpc.net/problem/11728
#배열 합치기

n,m=map(int,input().split())
aarr=list(map(int,input().split()))
barr=list(map(int,input().split()))

for i in sorted(aarr+barr):
    print(i,end=' ')
print()