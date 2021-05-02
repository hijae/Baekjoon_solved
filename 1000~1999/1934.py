#https://www.acmicpc.net/problem/1934
#최소공배수

def ucl(a,b):
    if b==0:
        return a
    else:
        return ucl(b, a%b)

i=int(input())
for i in range(i):
    a,b=map(int,input().split())
    res=ucl(a,b)
    print(a*b//res)