#https://www.acmicpc.net/problem/12813
#이진수 연산

a=int(input(),2)
b=int(input(),2)

n = 100000
mask=2**n-1

print(format(a&b,'b').zfill(n))
print(format(a|b,'b').zfill(n))
print(format(a^b,'b').zfill(n))
#파이썬의 not 연산이 다르게 동작하여 직접 연산해야합니다.
print(format(a^mask,'b').zfill(n))
print(format(b^mask,'b').zfill(n))