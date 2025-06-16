# https://www.acmicpc.net/problem/32941
# 왜 맘대로 예약하냐고

T, X = map(int, input().split())
N = int(input())

reservations = [0] * (T + 1)

for i in range(N):
	t = int(input())
	res = list(map(int, input().split()))
	for j in res:
		reservations[j] += 1

if reservations[X] == N:
	print("YES")
else:
	print("NO")