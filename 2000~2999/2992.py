#https://www.acmicpc.net/problem/2992
#크면서 작은 수

mini=input()
n=list(mini)
mini=str(mini)
mini=int(mini)
fl=[0 for i in range(len(n))]
arr=[0 for i in range(len(n))]
minarr=[]
def nm(cnt):
    if cnt==len(n):
        t=0
        ten=10**(len(n)-1)
        for i in arr:
            t=t+int(i)*ten
            ten=ten//10
        if(t>mini):
            minarr.append(t)
        return
    for i in range(len(n)):
        if fl[i]==0:
            arr[cnt]=n[i]
            fl[i]=1
            nm(cnt+1)
            fl[i]=0

nm(0)
if len(minarr)==0:
    print(0)
else:
    minarr=sorted(minarr)
    for i in minarr:
        print(i)
        break