#https://www.acmicpc.net/problem/10808
#알파벳 개수

s=input()
alp=[0]*26
for i in range(len(s)):
    alp[ord(s[i])-97]+=1
for i in range(26):
    print(alp[i],end=' ')
print()