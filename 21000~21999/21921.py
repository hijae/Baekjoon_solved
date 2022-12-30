# https://www.acmicpc.net/problem/21921
# 블로그

n,x=map(int,input().split())
arr=list(map(int,input().split()))
sumlist=[0]*len(arr)

for i in range(len(arr)):
    # do not use sum
    sumlist[i]=sumlist[i-1]+arr[i]
    if i>=x:
        sumlist[i]-=arr[i-x]
if max(sumlist)==0:
    print('SAD')
else:
    print(max(sumlist))
    print(sumlist.count(max(sumlist)))