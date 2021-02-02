#https://www.acmicpc.net/problem/10872
#팩토리얼

def factorial(r):
    if r==1 or r==0:
        return 1
    return r*factorial(r-1)

n=int(input())
print(factorial(n))