#https://www.acmicpc.net/problem/10809
#알파벳 찾기

s=input()
alp=[-1]*26
for i in range(len(s)):
    if alp[ord(s[i])-97]==-1:
        alp[ord(s[i])-97]=i
for i in range(26):
    print(alp[i],end=' ')
print()