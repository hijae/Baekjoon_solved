#https://www.acmicpc.net/problem/2440
#별 찍기 - 3

n=int(input())
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print("*",end='')
    print()