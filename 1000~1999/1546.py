n=int(input())
arr=list(map(int,input().split()))
maxar=max(arr)
av=0
for i in range(0,n):
    av=av+arr[i]/maxar*100
print(av/n)
