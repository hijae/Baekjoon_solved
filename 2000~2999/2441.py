#https://www.acmicpc.net/problem/2441
#별 찍기 - 4

n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end='')
    for j in range(0,n-i+1):
        print("*",end='')
    print()