#https://www.acmicpc.net/problem/9243
#파일 완전 삭제

n=int(input())
den=list(input())
enc=list(input())
for i in range(len(den)):
    den[i]=int(den[i])
    enc[i]=int(enc[i])
for i in range(n):
    for j in range(0,len(den)):
        if den[j]==1:
            den[j]=0
        else:
            den[j]=1
if den==enc:
    print("Deletion succeeded")
else:
    print("Deletion failed")