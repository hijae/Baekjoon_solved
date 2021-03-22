#https://www.acmicpc.net/problem/11650
#좌표 정렬하기

n=int(input())
arr=[[0 for j in range(2)] for i in range(n)]
for i in range(n):
    arr[i][0],arr[i][1]=map(int,input().split())
arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])
for i,j in arr:
    print(i,j)