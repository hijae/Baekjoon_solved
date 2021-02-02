#https://www.acmicpc.net/problem/1010
#다리 놓기

def factorial(r):
    if r==1 or r==0:
        return 1
    return r*factorial(r-1)

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(factorial(b)//(factorial(a)*factorial(b-a)))