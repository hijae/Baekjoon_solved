# https://www.acmicpc.net/problem/11970
# Fence Painting

# 색칠된 펜스의 길이를 구하는 문제

a,b=map(int,input().split())
c,d=map(int,input().split())

print((b-a)+(d-c)-max(0,min(b,d)-max(a,c)))