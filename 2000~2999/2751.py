#https://www.acmicpc.net/problem/2751
#수 정렬하기 2
#Pypy3로 채점하면 시간제한을 넘길수있음

arr=[]
n=int(input())

for i in range(0,n):
    arr.append(int(input()))
arr.sort()
for i in arr:
    print(i)