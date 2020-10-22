m=1
n=int(input())
if n==1:
    print(1)
for i in range(0,n):
    if n>m and n<=m+i*6:
        print(i+1)
        break
    m=m+i*6
