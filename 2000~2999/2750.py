#https://www.acmicpc.net/problem/2750
#수 정렬하기

arr=[]
n=int(input())

for i in range(0,n):
    arr.append(int(input()))
arr.sort()
for i in arr:
    print(i)