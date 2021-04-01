#https://www.acmicpc.net/problem/10974
#모든 순열

n=int(input())
fl=[0 for i in range(n)]
arr=[0 for i in range(n)]
def nm(cnt):
    if cnt==n:
        for i in range(n):
            print(arr[i]+1,end=' ')
        print()
        return
    for i in range(n):
        if fl[i]==0:
            arr[cnt]=i
            fl[i]=1
            nm(cnt+1)
            fl[i]=0
nm(0)