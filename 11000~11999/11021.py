#https://www.acmicpc.net/problem/11021
#A+B - 7

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print("Case #"+str(i+1)+":",a+b)