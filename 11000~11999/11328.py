#https://www.acmicpc.net/problem/11328
#Strfry

n=int(input())
for i in range(n):
    a,b=input().split()
    if sorted(a)==sorted(b):
        print("Possible")
    else:
        print("Impossible")