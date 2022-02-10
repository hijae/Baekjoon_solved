#https://www.acmicpc.net/problem/2960
#에라토스테네스의 체

n,k=map(int,input().split())
arr=list(i for i in range(2,n+1))
count=0
i=2
while arr: #에라토스테네스의 체
    for j in arr:
        if j%i==0:
            arr.remove(j)
            count+=1
            if count==k: #입력받은 값과 현재 값 확인
                print(j) #출력
                exit() #종료
    i+=1