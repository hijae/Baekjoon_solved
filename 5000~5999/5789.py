#https://www.acmicpc.net/problem/5789
#한다 안한다

n=int(input())
for i in range(n):
    t=list(input())
    if t[len(t)//2]==t[len(t)//2-1]:
        print("Do-it")
    else:
        print("Do-it-Not")