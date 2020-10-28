i=int(input())

arr=[0]*(i+2)
arr[1]=1
for i in range(2,i+2):
    arr[i] = arr[i-1]+arr[i-2]

print(arr[i-1])