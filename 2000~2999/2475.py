#https://www.acmicpc.net/problem/2475
#검증수

arr=map(int,input().split())
sum=0
for i in arr:
    sum+=i*i
print(sum%10)