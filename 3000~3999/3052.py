#acmicpc.net/problem/3052
#나머지

res=[]
for i in range(42):
    res.append(0)
for i in range(10):
    t=int(input())
    res[t%42]+=1
t=0
for i in res:
    if(i>0):
        t+=1
print(t)
