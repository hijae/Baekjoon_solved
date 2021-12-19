#https://www.acmicpc.net/problem/2845
#파티가 끝나고 난 뒤

l,p=map(int,input().split())
arr=list(map(int,input().split()))

for i in arr:
    print(i-l*p,end=' ')
print()