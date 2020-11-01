#https://www.acmicpc.net/problem/2446
#별 찍기 - 9

n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print(" ",end='')
    for j in range(0,(n-i)*2-1):
        print("*",end='')
    print()
for i in range(2,n+1):
    for j in range(0,n-i):
        print(" ",end='')
    for j in range(0,i*2-1):
        print("*",end='')
    print()
