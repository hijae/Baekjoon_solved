#https://www.acmicpc.net/problem/2438
#별 찍기 - 1

n=int(input())
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end="")
    print()
