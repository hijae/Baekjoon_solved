#https://www.acmicpc.net/problem/1806
#부분합

n,m=map(int,input().split())
arr=list(map(int,input().split()))

sum=[0]*(len(arr)+1)
for i in range(len(arr)):
    sum[i+1]=sum[i]+arr[i]

s=0
e=1
mini=9999999

while s<len(sum):
    if sum[e]-sum[s]>=m:
        mini=min(mini,e-s)
        s+=1
    else:
        if e<len(sum)-1:
            e+=1
        else:
            s+=1
if mini==9999999:
    print(0)
else:
    print(mini)