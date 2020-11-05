#https://www.acmicpc.net/problem/1009
#분산처리

arr=[[0],[1],[6,2,4,8],[1,3,9,7],[6,4],[5],[6],[1,7,9,3],[6,8,4,2],[1,9]] #거듭제곱의 1의 자리를 구하는 법의 주기를 미리 저장
t=int(input()) #테스트 케이스 수 입력
for i in range(t):
    a, b = input().split()
    if int(a)%10==0: #10으로 나눠질때 마지막 컴퓨터
        print(10)
        continue
    a=int(a)%10
    b=int(b)
    print(arr[a][b%len(arr[a])]) #주기에 맞춰 계산하여 출력