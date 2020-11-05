#https://www.acmicpc.net/problem/1003
#피보나치 함수

zero = [1, 0, 1] #0호출 초기값
one = [0, 1, 1] #1호출 초기값


t=int(input()) #테스트 케이스 수 입력
for i in range(t):
    n = int(input()) #n 입력
    l = len(zero)
    if l <= n:
        for i in range(l, n + 1): #호출 횟수가 피보나치 수열을 따름으로 맞춰 계산
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("%d %d" % (zero[n], one[n])) #피보나치 수열에 따른 호출 횟수 출력