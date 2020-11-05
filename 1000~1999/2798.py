#https://www.acmicpc.net/problem/2798
#블랙잭

max=0
n,m=map(int,input().split()) #카드의 갯수 n과 최대 합 m을 입력 받습니다.
arr=list(map(int,input().split())) #전체 카드 입력
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]<=m:
                if max<arr[i]+arr[j]+arr[k]:
                    max=arr[i]+arr[j]+arr[k] #모든 상황 확인해서 최대값 확인
print(max) #출력