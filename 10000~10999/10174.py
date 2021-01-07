#https://www.acmicpc.net/problem/10174
#팰린드롬

n=int(input())
for i in range(n):
    arr=input().upper()
    flag=0
    for i in range(len(arr)//2):
        if arr[len(arr)-i-1]!=arr[i]:
            flag=1
    if flag==1:
        print("No")
    else:
        print("Yes")