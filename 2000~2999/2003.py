#https://www.acmicpc.net/problem/2003
#수들의 합 2

n,m=map(int,input().split())
arr=list(map(int,input().split()))

sum=[0]*(len(arr)+1)
for i in range(len(arr)):
    sum[i+1]=sum[i]+arr[i]

s=0
e=1
cnt=0
while s<len(sum):
        if sum[e]-sum[s]==m:
            cnt+=1
            s+=1
        elif sum[e]-sum[s]>m:
            s+=1
        else:
            if e<len(sum)-1:
                e+=1
            else:
                s+=1
print(cnt)