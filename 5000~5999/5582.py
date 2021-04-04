#https://www.acmicpc.net/problem/5582
#공통 부분 문자열
#pypy3로만 돌아갑니다. 파이썬으로 하려면 더 단순한 알고리즘이 필요합니다.

a=list(input())
b=list(input())
ans=0
LCS=[]
for i in range(len(a)+5):
    line=[]
    for j in range(len(b)+5):
        line.append(0)
    LCS.append(line)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        if LCS[i][j] > ans:
            ans = LCS[i][j]

print(ans)