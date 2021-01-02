#https://www.acmicpc.net/problem/4673
#셀프 넘버

def sum(n):
    sum=int(n)
    while n>0:
        sum+=n%10
        n//=10
    return sum
arr = [0 for i in range(10001)]
for i in range(1,10001):
    check = sum(i)
    if check <10001:
        arr[check]=1
for i in range(1,10001):
    if arr[i]!=1:
        print(i)
