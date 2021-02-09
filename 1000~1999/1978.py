#https://www.acmicpc.net/problem/1978
#소수 찾기

n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    flag=0
    if i==1:
        flag=1
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag==0:
        sum+=1
print(sum)