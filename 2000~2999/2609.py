#https://www.acmicpc.net/problem/2609
#최대공약수와 최소공배수

def ucl(a,b):
    if b==0:
        return a
    else:
        return ucl(b, a%b)

a,b=map(int,input().split())
res=ucl(a,b)
print(res)
print(a*b//res)