#https://www.acmicpc.net/problem/2018
#수들의 합 5

n=int(input())

s=0
e=0
sum=0
cnt=0
while s<=n:
    if sum==n:
        cnt+=1
        s+=1
        sum-=s
    elif sum>n:
        s+=1
        sum-=s
    else:
        if e<n:
            e+=1
            sum+=e
        else:
            s+=1
            sum-=s
print(cnt)