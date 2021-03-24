#https://www.acmicpc.net/problem/1100
#하얀 칸

arr=[]
for i in range(8):
    arr.append(input())
cnt=0
for i in range(8):
    for j in range(8):
        if arr[i][j]=='F':
            if j%2==i%2:
                cnt+=1
print(cnt)