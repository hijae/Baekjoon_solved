arr=[]
n=int(input())

for i in range(0,n):
    arr.append(int(input()))
arr.sort()
for i in arr:
    print(i)