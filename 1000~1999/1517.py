n=int(input())
arr=list(map(int,input().split()))

sum=0
k=0
while k<n-1:
    last=n-1
    for j in range(n-1,k,-1):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            sum+=1
            last=j
        print(arr)
    k=last
print(sum)