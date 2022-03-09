# https://www.acmicpc.net/problem/2587
# 대표값2

arr=[]
for i in range(5):
    arr.append(int(input()))
arr=sorted(arr)
print(sum(arr)//5)
print(arr[2])
