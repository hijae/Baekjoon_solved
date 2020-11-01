#https://www.acmicpc.net/problem/2577
#숫자의 개수

a=int(input())
b=int(input())
c=int(input())
n=a*b*c
num=[0,0,0,0,0,0,0,0,0,0]
while n!=0:
    num[n%10]+=1
    n//=10
for i in num:
    print(i)