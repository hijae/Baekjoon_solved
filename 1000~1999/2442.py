#https://www.acmicpc.net/problem/2442
#별 찍기 - 5

n=int(input())
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end='')
    for j in range(0,i*2-1):
        print("*",end='')
    print()
