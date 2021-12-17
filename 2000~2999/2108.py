#https://www.acmicpc.net/problem/2108
#통계학

from collections import Counter
import math
import sys

n=int(sys.stdin.readline())

sum=0
cen=[]
for i in range(n):
    t=int(sys.stdin.readline()) #속도를 위해 input대신 사용
    cen.append(t)
    sum+=t
cen.sort()


print(round(sum/n))
print(cen[n//2])
if n==1:
    print(cen[0])
else:
    com=Counter(cen).most_common(2)
    if com[0][1]==com[1][1]:
        print(com[1][0])
    else:
        print(com[0][0])
print(cen[n-1]-cen[0])