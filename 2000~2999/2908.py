#https://www.acmicpc.net/problem/2908
#상수

t1,t2=map(int,input().split())
a=t1//100
t1=t1%100
a=a+(t1//10)*10
t1=t1%10
a=a+t1*100

b=t2//100
t2=t2%100
b=b+(t2//10)*10
t2=t2%10
b=b+t2*100

if a>b:
    print(a)
else:
    print(b)