#https://www.acmicpc.net/problem/2444
#별 찍기 - 7

n=int(input())
for i in range(1,n):
    for j in range(0,n-i):
        print(" ",end='')
    for j in range(0,i*2-1):
        print("*",end='')
    print()
for i in range(0,n):
    for j in range(0,i):
        print(" ",end='')
    for j in range(0,(n-i)*2-1):
        print("*",end='')
    print()
