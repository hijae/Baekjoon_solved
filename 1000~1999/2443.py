#https://www.acmicpc.net/problem/2443
#별 찍기 - 6

n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print(" ",end='')
    for j in range(0,(n-i)*2-1):
        print("*",end='')
    print()
