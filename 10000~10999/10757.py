#https://www.acmicpc.net/problem/10757
#큰 수 A+B
#파이썬으로는 간단하지만 C언어로는 문자열로 받아 한글자씩 분리하여 받아올림을 직접 처리해야 합니다.

a, b = input().split()
print(int(a) + int(b))