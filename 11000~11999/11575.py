#https://www.acmicpc.net/problem/11575
#Affine Cipher

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    s=list(input())
    en=[]
    for i in range(len(s)):
        key=(a*(ord(s[i])-65)+b)%26
        print(chr(key+65),end='')
    print()