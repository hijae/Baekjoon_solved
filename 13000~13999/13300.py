#https://www.acmicpc.net/problem/13300
#방 배정

n,k=map(int,input().split())
arr=[[0 for i in range(6)] for j in range(2)]

for i in range(n):
    s,y=map(int,input().split())
    arr[s][y-1]+=1
cnt=0
for i in range(2):
    for j in range(6):
        if(arr[i][j]%k==0):
            cnt+=arr[i][j]//k
        else:
            cnt+=(arr[i][j]+k-1)//k
print(cnt)