#https://www.acmicpc.net/problem/11721
#열 개씩 끊어 출력하기

arr=list(input())
for i in range(len(arr)):
    print(arr[i],end='')
    if i%10==9:
        print()
print()