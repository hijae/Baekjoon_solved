#https://www.acmicpc.net/problem/2775
#부녀회장이 될테야

t=int(input())
arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(t):
    k=int(input())
    n=int(input())
    for y in range(n+1):
        arr[y]=y
    for y in range(k):
        for z in range(1,n+1):
            arr[z]=arr[z-1]+arr[z]
        print(arr[z])