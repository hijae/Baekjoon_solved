# https://www.acmicpc.net/problem/20833
# Kuber

# 1~N까지의 수의 세제곱의 합을 구하는 문제
# 1~N까지의 수의 세제곱의 합은 (N(N+1)/2)^2이다.

n=int(input())
print((n*(n+1)//2)**2)