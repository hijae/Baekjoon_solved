#https://www.acmicpc.net/problem/10093
#숫자

a,b=map(int,input().split())
if a==b:
    print(0)
elif a>b:
    print(a-b-1)
    for i in range(b+1,a):
        print(i)
else:
    print(b-a-1)
    for i in range(a+1,b):
        print(i)