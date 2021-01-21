#https://www.acmicpc.net/problem/11365
#!밀비 급일

while(1):
    arr=input()
    if arr!="END":
        for i in range(len(arr)):
            print(arr[len(arr)-i-1],end='')
        print()
    else:
        break