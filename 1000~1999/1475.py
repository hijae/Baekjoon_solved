#https://www.acmicpc.net/problem/1475
#방 번호

n=input()
arr=[0,0,0,0,0,0,0,0,0,0]
for i in n:
    if int(i)%10==6 or int(i)%10==9:
        arr[6]+=1
    else:
        arr[int(i)%10]+=1
if arr[6]%2==0:
    arr[6]//=2
else:
    arr[6]=arr[6]//2+1
max=-99
for i in range(0,9):
    if arr[i]>max:
        max=arr[i]
print(max)