#https://www.acmicpc.net/problem/10707
#수도요금

a=int(input())
b=int(input())
c=int(input())
d=int(input())
p=int(input())

if c>=p:
    if a*p>b:
        print(b)
    else:
        print(a*p)
else:
    if a*p>b+(p-c)*d:
        print(b+(p-c)*d)
    else:
        print(a*p)