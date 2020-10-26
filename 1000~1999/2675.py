t=int(input())
for i in range(0,t):
    r,s=input().split()
    r=int(r)
    for j in s:
        for k in range(0,r):
            print(j,end='')
    print()