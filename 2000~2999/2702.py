#https://www.acmicpc.net/problem/2702
#초6 수학

def ucl(a,b):
    if b==0:
        return a
    else:
        return ucl(b, a%b)

i=int(input())
for i in range(i):
    a,b=map(int,input().split())
    res=ucl(a,b)
    print(a*b//res,res)