#https://www.acmicpc.net/problem/8958
#OX퀴즈

n=int(input())
for i in range(n):
    arr=input()
    sum=0
    flag=0
    for j in arr:
        if j=='O':
            flag+=1
            sum+=flag
        else:
            flag=0
    print(sum)