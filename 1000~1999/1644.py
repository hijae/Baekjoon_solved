#https://www.acmicpc.net/problem/1644
#소수의 연속합

n=int(input())

prifl=[True for i in range(n+1)]

for i in range(2,int(n**0.5+1)):
    if prifl[i]:
        for j in range(i+i,n+1,i):
            prifl[j]=False
pri=[i for i, j in enumerate(prifl) if j==True and i>=2 ]
prisum=[0]*(len(pri)+1)
for i in range(len(pri)):
    prisum[i+1]=prisum[i]+pri[i]

s=0
e=1
cnt=0
if n==1:
    cnt=0
else:
    while s<len(prisum):
        if prisum[e]-prisum[s]==n:
            cnt+=1
            s+=1
        elif prisum[e]-prisum[s]>n:
            s+=1
        else:
            if e<len(prisum)-1:
                e+=1
            else:
                s+=1
print(cnt)