#https://www.acmicpc.net/problem/13420
#사칙연산

n=int(input())

for i in range(n):
    t=list(input().split())
    if int(t[4])==eval(t[0]+t[1]+t[2]):
        print("correct")
    else:
        print("wrong answer")