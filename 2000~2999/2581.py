#https://www.acmicpc.net/problem/2581
#소수

n=int(input())
m=int(input())
sum=0
min=99999
for i in range(n,m+1):
    flag=0
    if i==1:
        flag=1
    for j in range(2,i//2+1):
        if i%j==0:
            flag=1
    if flag==0:
        if min>i:
            min=i
        sum+=i
if min!=99999:
    print(sum)
    print(min)
else:
    print(-1)