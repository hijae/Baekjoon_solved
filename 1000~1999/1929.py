#https://www.acmicpc.net/problem/1929
#소수 구하기

import math

def pri(num):
    if num==1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True

m,n=map(int,input().split())

for i in range(m,n+1):
    if pri(i):
        print(i)