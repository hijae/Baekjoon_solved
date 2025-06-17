# https://www.acmicpc.net/problem/23348
# 스트릿 코딩 파이터

A, B, C = map(int, input().split())
N = int(input())
max_score = 0

for _ in range(N):
	score = 0
	for _ in range(3):
		a, b, c = map(int, input().split())
		score = score + A * a + B * b + C * c
	max_score = max(max_score, score)
print(max_score)