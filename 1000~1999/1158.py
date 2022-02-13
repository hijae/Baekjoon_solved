#https://www.acmicpc.net/problem/1158
#요세푸스 문제

#큐 사용

n,k=map(int,input().split())
arr=[i for i in range(1,n+1)] #1~n까지 배열 생성
num=k-1
print("<",end="")
for i in range(n-1):
    print(arr.pop(num),end=', ') #큐에서 꺼내서 출력
    num+=k-1
    if len(arr) != 0: 
        num = num%len(arr) 
print(arr.pop(num),end='>')
print()