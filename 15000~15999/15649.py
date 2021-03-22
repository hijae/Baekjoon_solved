#https://www.acmicpc.net/problem/15649
#N과 M (1)

n,m=map(int,input().split())
arr=[0 for i in range(10)]
fl=[0 for i in range(10)]

def nm(cnt):
    if cnt==m:
        for i in range(m):
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