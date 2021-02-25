n=int(input())

for i in range(max(1,n-54),n+1):
    t=i+sum(list(map(int,str(i))))
    if t==n:
        print(i)
        break
    if i==n:
        print(0)