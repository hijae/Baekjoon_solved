#https://www.acmicpc.net/problem/1157
#단어 공부

s=sorted(input().upper())
alp= {}
for i in set(s):
    alp[i] = 0
max=-99
for i in s:
    alp[i] += 1
    if max<alp[i]:
        max=alp[i]

cnt=0
flag=-1
for i in alp:
    if alp[i]==max:
        cnt+=1
        flag=i
if cnt==1:
    print(flag)
else:
    print("?")