#https://www.acmicpc.net/problem/10773
#제로

k=int(input())
arr=[]
for i in range(k):
    t=int(input())
    if t==0:
        arr.pop()
    else:
        arr.append(t)
print(sum(arr))