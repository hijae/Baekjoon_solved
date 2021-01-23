#https://www.acmicpc.net/problem/11720
#숫자의 합

n=int(input())
arr=list(input())
sum=0
for i in arr:
    sum+=int(i)
print(sum)