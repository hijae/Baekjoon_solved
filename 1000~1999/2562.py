arr=[]
max=-99
for i in range(0,9):
    arr.append(int(input()))
for i in range(0,9):
    if max<arr[i]:
        max=arr[i]
        map=i
print(max)
print(map+1)