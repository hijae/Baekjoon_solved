#https://www.acmicpc.net/problem/10162
#전자레인지

n=int(input())
if n%10!=0:
    print(-1)
else:
    print(n//300)
    n%=300
    print(n//60)
    n%=60
    print(n//10)
