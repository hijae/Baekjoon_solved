#https://www.acmicpc.net/problem/9012
#괄호

n=int(input())
for _ in range(n):
    flag=0
    arr=list(input())
    for i in arr:
        if i=="(":
            flag+=1
        if i==")":
            flag-=1
        if flag==-1:
            break
    if flag==0:
        print("YES")
    else:
        print("NO")