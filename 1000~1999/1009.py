#https://www.acmicpc.net/problem/1009
#분산처리

arr=[[0],[1],[6,2,4,8],[1,3,9,7],[6,4],[5],[6],[1,7,9,3],[6,8,4,2],[1,9]]
t=int(input())
for i in range(t):
    a, b = input().split()
    if int(a)%10==0:
        print(10)
        continue
    a=int(a)%10
    b=int(b)
    print(arr[a][b%len(arr[a])])