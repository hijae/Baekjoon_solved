sum=0
min=9999
for i in range(0,7):
    t=int(input())
    if t%2==1:
        sum+=t
        if t<min:
            min=t
if sum==0:
    print(-1)
else:
    print(sum)
    print(min)